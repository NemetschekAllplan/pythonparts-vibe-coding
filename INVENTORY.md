INVENTORY:
[Agent instructions] AGENTS.md - Workspace operating contract for Allplan PythonPart development (193 lines, 10.67 KB)
[Brain / Learnings] brain.md - Accumulated session learnings and validated rules (598 lines, 54.39 KB)
[Anti-hallucination] anti_hallucination.md - Verified/forbidden API usage rules (117 lines, 5.27 KB)
[Pattern documentation] Grundlagen.md - Feasibility and maturity analysis framework (158 lines, 7.89 KB)
[Task prompt] promt.md - Workspace migration target specification (383 lines, 19.08 KB)
[Task prompt] 01_knowledgebase/PythonPartsFramework_DB/01_Grundlagen/promt.md - Documentation converter/indexer task definition (259 lines, 7.78 KB)
[API documentation] 01_knowledgebase/PythonPartsFramework_DB/02_API_Referenz/ - Full API reference corpus (535 files, 7.45 MB)
[API documentation] 01-2_knowledgebase/modules/ - Module-level Allplan API summaries (12 files, 0.08 MB)
[API documentation] 01-2_knowledgebase/framework/ - Framework class references (39 files, 0.02 MB)
[Pattern documentation] 01-2_knowledgebase/patterns/standard_pythonpart.md - Standard contract skeleton (83 lines, 2.49 KB)
[Pattern documentation] 01-2_knowledgebase/patterns/script_object.md - Script Object contract skeleton (51 lines, 1.85 KB)
[Pattern documentation] 01-2_knowledgebase/patterns/interactor.md - Interactor contract skeleton (68 lines, 2.08 KB)
[Pattern documentation] 01-2_knowledgebase/quickref/common_pitfalls.md - Verified pitfalls list (9 lines, 0.76 KB)
[Pattern documentation] 01-2_knowledgebase/quickref/imports.md - Canonical imports and alias examples (500 lines, 38.04 KB)
[Pattern documentation] 01-2_knowledgebase/quickref/pyp_tags.md - PYP tag quick reference (31 lines, 1.65 KB)
[Pattern documentation] 01-2_knowledgebase/quickref/value_type_map.md - ValueType mapping and units (12 lines, 0.85 KB)
[Example PythonParts] input/Hochregallager.py - Working Standard PythonPart implementation (447 lines, 23.46 KB)
[Example PythonParts] input/Hochregallager.pyp - Matching palette/config for Hochregallager (521 lines, 19.57 KB)
[Example PythonParts] input/BetonStuetze.py - Reinforced column implementation reference (438 lines, 18.18 KB)
[Templates] input/AIColumn.pyp - Parameter template-like PYP reference (128 lines, 4.47 KB)
[Configuration/Index] 01_knowledgebase/PythonPartsFramework_DB/_INDEX.md - Knowledge index metadata (945 lines, 200.28 KB)
[Configuration/Index] 01-2_knowledgebase/INVENTORY.md - Generated inventory of converted docs (3628 lines, 205.23 KB)
[Debug logs] 02_debug/ - Runtime diagnostic logs (3 files, 0.16 MB)
[Other assets] input/218829_tdb_INT_PR9000-A.pdf - External technical PDF source (n/a lines, 184.39 KB)

DUPLICATES:
- "Feature topic sets" (geometry/input/reinforcement/etc.) appear in both `01_knowledgebase/features/` and `01-2_knowledgebase/features/`.
- "Prompt concept documents" appear at root `promt.md` and `01_knowledgebase/PythonPartsFramework_DB/01_Grundlagen/promt.md`.
- "Inventory-style indexes" appear as `01_knowledgebase/PythonPartsFramework_DB/_INDEX.md` and `01-2_knowledgebase/INVENTORY.md` with overlapping purpose.

GAPS:
- No workspace-local Codex skill package (`.agents/skills/.../SKILL.md`) existed before migration.
- No deterministic `validate_pythonpart.py` script existed before migration.
- No custom `.agent.md` agents existed before migration.
- `out/` currently contains no active `.py` + `.pyp` pair.
- No standardized `projects/_template/prompt.md` task template existed before migration.

Notes:
- Per workspace rules, `old/` and `archiv/` were not used as content sources.
