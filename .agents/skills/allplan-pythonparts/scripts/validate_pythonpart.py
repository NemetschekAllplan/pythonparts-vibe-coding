#!/usr/bin/env python3
"""Deterministic validator for Allplan PythonPart file pairs."""

from __future__ import annotations

import ast
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

HALLUCINATION_PATTERNS = {
    "AllplanGeo.Box3D": re.compile(r"\bAllplanGeo\.Box3D\s*\("),
    "AllplanGeo.Cylinder": re.compile(r"\bAllplanGeo\.Cylinder\s*\("),
    "AllplanGeo.Sphere": re.compile(r"\bAllplanGeo\.Sphere\s*\("),
    "ModelEleList.add": re.compile(r"\bModelEleList\.add\s*\("),
    "Polyhedron3D.CreateBox": re.compile(r"\bPolyhedron3D\.CreateBox\s*\("),
    "geometry.transform": re.compile(r"\bgeometry\.transform\s*\("),
}

CANONICAL_ALIASES = {
    "NemAll_Python_Geometry": "AllplanGeo",
    "NemAll_Python_BasisElements": "AllplanBasisEle",
    "NemAll_Python_BaseElements": "AllplanBaseEle",
    "NemAll_Python_ArchElements": "AllplanArchEle",
    "NemAll_Python_Reinforcement": "AllplanReinf",
    "NemAll_Python_IFW_Input": "AllplanIFW",
    "NemAll_Python_IFW_ElementAdapter": "AllplanElementAdapter",
    "NemAll_Python_AllplanSettings": "AllplanSettings",
    "NemAll_Python_Utility": "AllplanUtil",
    "NemAll_Python_Palette": "AllplanPalette",
}

BOOLEAN_FUNCTIONS = {"MakeUnion", "MakeSubtraction", "MakeIntersection"}


@dataclass
class Finding:
    severity: str
    message: str
    line: int | None = None


def resolve_base(argument: str) -> tuple[Path, Path, str]:
    raw = Path(argument)
    if raw.suffix.lower() in {".py", ".pyp"}:
        base = raw.with_suffix("")
    else:
        base = raw
    py_path = base.with_suffix(".py")
    pyp_path = base.with_suffix(".pyp")
    return py_path, pyp_path, str(base)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def find_hallucinations(py_text: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = py_text.splitlines()
    for idx, line in enumerate(lines, start=1):
        for label, pattern in HALLUCINATION_PATTERNS.items():
            if pattern.search(line):
                findings.append(Finding("ERROR", f"Forbidden API pattern detected: {label}", idx))
    return findings


def parse_python_ast(py_text: str) -> ast.AST:
    return ast.parse(py_text)


def check_import_aliases(tree: ast.AST) -> list[Finding]:
    findings: list[Finding] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Import):
            continue
        for alias in node.names:
            expected = CANONICAL_ALIASES.get(alias.name)
            if expected is None:
                continue
            if alias.asname != expected:
                findings.append(
                    Finding(
                        "ERROR",
                        f"Canonical alias mismatch for {alias.name}: expected '{expected}', got '{alias.asname}'",
                        node.lineno,
                    )
                )
    return findings


def build_parent_map(tree: ast.AST) -> dict[ast.AST, ast.AST]:
    parent_map: dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parent_map[child] = parent
    return parent_map


def call_function_name(call: ast.Call) -> str | None:
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    if isinstance(call.func, ast.Name):
        return call.func.id
    return None


def check_boolean_unpacking(tree: ast.AST, parent_map: dict[ast.AST, ast.AST]) -> list[Finding]:
    findings: list[Finding] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn_name = call_function_name(node)
        if fn_name not in BOOLEAN_FUNCTIONS:
            continue

        parent = parent_map.get(node)
        valid = False
        if isinstance(parent, ast.Assign) and len(parent.targets) == 1:
            target = parent.targets[0]
            if isinstance(target, (ast.Tuple, ast.List)) and len(target.elts) == 2:
                valid = True
        elif isinstance(parent, ast.AnnAssign):
            target = parent.target
            if isinstance(target, (ast.Tuple, ast.List)) and len(target.elts) == 2:
                valid = True

        if not valid:
            findings.append(
                Finding(
                    "ERROR",
                    f"{fn_name} must unpack tuple return as 'err, result = ...'",
                    node.lineno,
                )
            )
    return findings


def extract_build_ele_params(py_text: str) -> set[str]:
    return set(re.findall(r"\bbuild_ele\.([A-Za-z_][A-Za-z0-9_]*)\.value\b", py_text))


def parse_pyp_parameter_names(pyp_text: str) -> tuple[set[str], list[Finding]]:
    findings: list[Finding] = []
    names: list[str] = []
    try:
        root = ET.fromstring(pyp_text)
    except ET.ParseError as exc:
        findings.append(Finding("ERROR", f"PYP XML is not parseable: {exc}"))
        return set(), findings

    for param in root.findall(".//Parameter"):
        name_node = param.find("Name")
        if name_node is None:
            name_node = param.find("n")
        if name_node is None:
            continue
        name_value = (name_node.text or "").strip()
        if name_value:
            names.append(name_value)

    duplicates = sorted({name for name in names if names.count(name) > 1})
    for dup in duplicates:
        findings.append(Finding("ERROR", f"Duplicate parameter name in PYP: {dup}"))

    return set(names), findings


def check_param_consistency(py_text: str, pyp_names: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    py_params = sorted(extract_build_ele_params(py_text))
    missing = [name for name in py_params if name not in pyp_names]
    for name in missing:
        findings.append(Finding("ERROR", f"Parameter used in .py but missing in .pyp: {name}"))
    return findings


def is_number_constant(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and isinstance(node.value, (int, float))


def constant_value(node: ast.AST) -> float:
    return float(node.value)  # type: ignore[arg-type]


def check_units_warning(tree: ast.AST) -> list[Finding]:
    findings: list[Finding] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr != "CreateCuboid":
            continue

        numeric_values: list[float] = []

        if len(node.args) >= 3 and all(is_number_constant(arg) for arg in node.args[:3]):
            numeric_values.extend([constant_value(arg) for arg in node.args[:3]])

        for kw in node.keywords:
            if kw.arg in {"length", "width", "height"} and kw.value is not None and is_number_constant(kw.value):
                numeric_values.append(constant_value(kw.value))

        if numeric_values and any(0.0 < value < 10.0 for value in numeric_values):
            findings.append(
                Finding(
                    "WARNING",
                    "CreateCuboid uses small numeric values (<10). Check mm vs m units.",
                    node.lineno,
                )
            )
    return findings


def print_findings(title: str, findings: list[Finding]) -> None:
    safe_print(title)
    for finding in findings:
        if finding.line is None:
            safe_print(f"- [{finding.severity}] {finding.message}")
        else:
            safe_print(f"- [{finding.severity}] line {finding.line}: {finding.message}")


def safe_print(message: str) -> None:
    try:
        print(message)
    except UnicodeEncodeError:
        fallback = message.encode("ascii", errors="ignore").decode("ascii")
        print(fallback)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python validate_pythonpart.py <basename>")
        return 2

    py_path, pyp_path, base_label = resolve_base(argv[1])
    findings: list[Finding] = []
    warnings: list[Finding] = []

    if not py_path.exists():
        findings.append(Finding("ERROR", f"Missing .py file: {py_path}"))
    if not pyp_path.exists():
        findings.append(Finding("ERROR", f"Missing .pyp file: {pyp_path}"))

    if findings:
        print_findings(f"❌ {len(findings)} issue(s) found for '{base_label}':", findings)
        return 1

    py_text = read_text(py_path)
    pyp_text = read_text(pyp_path)

    findings.extend(find_hallucinations(py_text))

    try:
        tree = parse_python_ast(py_text)
    except SyntaxError as exc:
        findings.append(Finding("ERROR", f"Python syntax error: {exc.msg}", exc.lineno))
        print_findings(f"❌ {len(findings)} issue(s) found for '{base_label}':", findings)
        return 1

    parent_map = build_parent_map(tree)
    findings.extend(check_import_aliases(tree))
    findings.extend(check_boolean_unpacking(tree, parent_map))

    pyp_names, pyp_findings = parse_pyp_parameter_names(pyp_text)
    findings.extend(pyp_findings)
    findings.extend(check_param_consistency(py_text, pyp_names))

    warnings.extend(check_units_warning(tree))

    if findings:
        print_findings(f"❌ {len(findings)} issue(s) found for '{base_label}':", findings)
        if warnings:
            print_findings(f"⚠️ {len(warnings)} warning(s):", warnings)
        return 1

    safe_print("✅ Validation passed")
    if warnings:
        print_findings(f"⚠️ {len(warnings)} warning(s):", warnings)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
