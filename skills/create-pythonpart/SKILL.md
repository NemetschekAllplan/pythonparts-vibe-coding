---
name: create-pythonpart
description: >
  Step-by-step workflow for creating a PythonPart using the Script Object contract.
  Use this skill whenever the user asks to create, build, or scaffold a new PythonPart.
applyTo: "**"
---

## Overview

A PythonPart consists of exactly **two required files**:

| File | Purpose |
|------|---------|
| `MyPythonPart.pyp` | XML file — defines metadata, palette parameters, lives in `Library\` |
| `MyPythonPart.py`  | Python script — implements the business logic, lives in `PythonPartsScripts\` |

The **Script Object contract** is the default choice. It is the most versatile contract:
- for a simple PythonPart requires only two functions and a class with one method to be implemented
- standard input steps (like selecting an element or drawing a line) are predefined in the framework and can be easily added
- if the user has specific requirements for an input step, it is possible to implement a fully custom one

---


## Step 1 — Gather requirements

Before writing any code, establish the following with the user:

1. **Name** — what should the PythonPart be called? (used for file names and `<Title>`)
2. What is the **purpose** of the PythonPart? Should it create parametric element, modify existing ones, or something else? This will determine the parameters and overall structure of the script. 
3. What inputs does the user provide in the palette? This will determine the UI (property palette) and the parameters in the step 3.
4. **Target directory** — Office (`std`) or Private (`usr`)? Default to `std`.

## Step 2 -- Figure out user's ALLPLAN version and environment paths

Try to find out the ALLPLAN version the user is working with based on the paths included in the workspace. Use the skill `environment-paths` to find out the paths, so you know where to place the files in Step 5.

## Step 3 — Create the PYP file

Use the **`property-palette`** skill to design the palette: it covers the full PYP file structure, all parameter types, and has a ready-to-use template.

The only rules to keep in mind here:
- `<Name>` inside `<Script>` is the path to the `.py` file **relative to the `PythonPartsScripts\` directory**
- `<Version>` must be a string that can be converted to `float` (e.g. `"1.0"`)
- Every `<Parameter>` `<Name>` must be PascalCase with no spaces — it becomes a Python attribute on `build_ele`

---

## Step 4 — Create the PY file

Use the **`pythonpart-script`** skill for the full contract rules, template, and guidance on adding
input steps. The template is also available in `skills/pythonpart-script/templates/MyPythonPart.py`.

---

## Step 5 — Place the files

Use the skill `environment-paths` to find out the correct paths for the user, so you know where to place the files. Remember:

- PYP file goes to `Library\` subfolder of either `std` or `usr`
- PY file goes to `PythonPartsScripts\` subfolder of either `std` or `usr`

---

## Step 6 — Verify before handing off

Run through this checklist mentally before presenting the files to the user:

- [ ] `<Name>` in `<Script>` matches the actual `.py` file path under `PythonPartsScripts\`
- [ ] Every `<Parameter>` `<Name>` used in `execute()` exists in the PYP file
- [ ] `execute()` returns `CreateElementResult`
- [ ] No logic runs at module level (imports and function/class definitions only)
- [ ] `check_allplan_version` and `create_script_object` are present as module-level functions
- [ ] The class inherits from `BaseScriptObject`


