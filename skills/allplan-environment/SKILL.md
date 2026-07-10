---
name: allplan-environment
description: Use this skill to find out the ALLPLAN version and environment paths for PythonPart development.
---

# Skill: ALLPLAN Environment

## Paths overview

- `prg` The path with ALLPLAN binaries. **Read-only** — do not place files here.

- `etc` The path with ALLPLAN resources. **Read-only** — do not place files here, but you can read files from it.

- `std` The path for office-wide resources. Files placed here are available for all users. Usually: `c:\Data\Allplan\Allplan <ALLPLAN_VERSION>\Std\`, but it can also be on a network drive.

- `usr` The path for user-specific resources. Files placed here are available only for the current user. Usually: `C:\Users\<username>\Documents\Nemetschek\ALLPLAN\<ALLPLAN_VERSION>\Usr\<allplan_username>\`, but it can also be on a network drive.

These paths should be part of the user's workspace. If they are not, the `etc` and `prg` paths can be read from the registry as an emergency fallback (see `instructions/establishing-paths.md`). There is no way to find out the `std` and `usr` paths. Ask the user to provide them.

## Where to put PYP and PY files

PYP files should be put in the `Library\` subfolder of either `std` or `usr`, depending on whether the PythonPart should be available for all users in the office or only for the current user.

PY files should be put in the `PythonPartsScripts\` subfolder in either `std` or `usr`, depending on where the corresponding PYP file is placed. The folder structure inside `PythonPartsScripts\` does not matter, as long as the path to the PY file is correctly specified in the PYP file. For complex PythonParts, it is recommended to apply a python-package-like structure to keep the files organized, e.g. `PythonPartsScripts\MyPythonPart\__init__.py` and `PythonPartsScripts\MyPythonPart\helper.py`. The entry point functions can be implemented in `__init__.py`. If that's the case, refer to the PY file in the PYP file as `MyPythonPart.py`, without the folder.

```
📁 std\   (or usr\)
├── 📁 Library\
│   └── 📁 MyPythonParts\
│       └── 📄 MyPythonPart.pyp
└── 📁 PythonPartsScripts\
    └── 📁 MyPythonParts\
        └── 📄 MyPythonPart.py
```

> **Never save files in `etc\`** — it is managed by ALLPLAN and will be overwritten on update.

The subdirectory name inside `Library\` and `PythonPartsScripts\` should match (best practice).

## Framework files

Framework files are stored in the `PythonPartsFramework\` sub-folder of the `etc` path:

| Sub-folder | Contents | When to use |
|---|---|---|
| `InterfaceStubs` | Python stub files for the ALLPLAN API | Look here for function signatures and parameter types. No runtime implementation, but sufficient for development. |
| `GeneralScript` | Python layer of the framework | Contains both internal framework code and public classes/functions intended for PythonPart scripts. |
| `Utils` | Developer helper utilities | Check here first for helpers to work with ALLPLAN data structures, geometry, and palette parameters. |

## Examples

A comprehensive collection of example PythonParts can be found on GitHub:
`https://github.com/NemetschekAllplan/PythonPartsExamples/tree/<ALLPLAN_VERSION>` (replace `<ALLPLAN_VERSION>` with the actual version, e.g. `2025` or `2026`). The PYP files are in the `Library/Examples/PythonParts` directory, and the PY files are in the `PythonPartsExampleScripts` directory.

Ideally, the user has downloaded these examples with a dedicated tool - look for them in the `usr\<username>\PythonPartsExamples` path.

---

## Related guides

- [Create a New PythonPart](skill://create-new-pythonpart) — end-to-end workflow for building a PythonPart from scratch
