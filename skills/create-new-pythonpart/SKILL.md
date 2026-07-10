---
name: create-new-pythonpart
description: Use this skill when creating a new PythonPart. This skill provides the most high-level guidance and links to more specific skills for each step of the process.
---

# Skill: Create a New PythonPart

## Overview

A PythonPart consists of exactly **two required files**:

| File | Purpose |
|------|---------|
| `MyPythonPart.pyp` | XML file — defines metadata, palette parameters, lives in `Library\` |
| `MyPythonPart.py`  | Python script — implements the business logic, lives in `PythonPartsScripts\` |

The **Script Object contract** is the default choice. It is the most versatile contract:
- for a workflow involving only input in the property palette, it requires only two functions and a class with one method to be implemented
- standard input steps (like selecting an element or drawing a line) are predefined in the framework and can be easily added
- if the user has specific requirements for an input step, it is possible to implement a fully custom one

## Step 1 — Gather requirements

Before writing any code, establish the following with the user:

1. **Name** — what should the PythonPart be called? (used for file names and `<Title>`)
2. **Purpose** - what is the PythonPart supposed to do? Should it create parametric element, modify existing ones, import/export data? 
3. **Workflow** - how does the user want to **interact** with the PythonPart? What inputs does the user provide in the UI? What are the required workflow steps (like selecting an element, drawing a line, etc.)?
4. **UI** - Are additional UI components beyond the palette required (like a dialog with advanced options)?
5. **Target directory** — Office (`std`) or Private (`usr`)? Default to `std`.

## Step 2 — Understand the ALLPLAN environment

Use the `allplan-environment` skill to determine the ALLPLAN version and the exact paths for `std` and `usr`. If an ALLPLAN runtime discovery tool is available in the workspace, use it. Otherwise, ask the user for the `std` and `usr` paths directly — there is no reliable way to infer them automatically.

## Step 3 — Create the PYP file

Use the `ui-design` skill to design the UI. This will involve creating a PYP file with parameter definitions and the layout of the property palette (the standard UI framework offered by ALLPLAN). In rare cases, the capabilities of the property palette may not be sufficient, and you may need to implement a custom UI (like a dialog with advanced options).

## Step 4 — Create the PY file

Use the `pythonpart-script` skill for the full contract rules, template, and guidance on adding input steps.

## Step 5 — Place the files

Save the files in the directories determined in Step 2. Remember:

- PYP file goes to `Library\` subfolder of either `std` or `usr`
- PY file goes to `PythonPartsScripts\` subfolder of either `std` or `usr`

---

## Related guides

- [ALLPLAN Environment](skill://allplan-environment) — how to find version, paths, and framework files
- [Property Palette (UI Design)](skill://ui-design) — how to build the PYP file
- [PythonPart Script](skill://pythonpart-script) — how to write the PY file
- [ALLPLAN Elements](skill://allplan-elements) — how to create geometry and elements in the script
