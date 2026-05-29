---
name: environment-paths
description: >
  Guide, how to find out the ALLPLAN version the user is working and what are the environment paths relevant for PythonParts development.
  Use this skill whenever you are not where to put the generated files, or where to look for existing ones.
---

## Overview

### `prg`

The path with ALLPLAN binaries; DO NOT use it for placing any files, as it is read-only; stored in registry under `HKEY_LOCAL_MACHINE\SOFTWARE\NEMETSCHEK\ALLPLAN\<ALLPLAN_VERSION>\InstallRoot`, in entries `ProgramDataDrive` with the drive letter and `ProgramDataPath` with the path. Replace `<ALLPLAN_VERSION>` with the actual version, e.g. `2025.0`.

### `etc`
The path with ALLPLAN resources (other than binaries); DO NOT use it for placing any files, as it is read-only; you can read files from here; The **parent folder** of the `etc` path is stored in registry under `HKEY_LOCAL_MACHINE\SOFTWARE\NEMETSCHEK\ALLPLAN\<ALLPLAN_VERSION>\InstallRoot`, in entries `DataDrive` with the drive letter and `DataPath` with the path. Replace `<ALLPLAN_VERSION>` with the actual version, e.g. `2025.0`.

### `std`
The path for office-wide resources; files placed here are available for all users in the office; not stored in registry, you have to ask the user or infer it from the workspace paths; usually `c:\Data\Allplan\Allplan <ALLPLAN_VERSION>\Std\`

### `usr`
The path for user-specific resources; files placed here are available only for the current user; also not stored in registry, you have to ask the user or infer it from the workspace paths; usually `C:\Users\<username>\Documents\Nemetschek\ALLPLAN\<ALLPLAN_VERSION>\Usr\<allplan_username>\`; `allplan_username` can be `local`

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

- Never save files in `etc\` — it is managed by ALLPLAN and may be overwritten on update.
- The subdirectory name inside `Library\` and `PythonPartsScripts\` should match (best practice).

## Framework files

Framework files are stored in the `PythonPartsFramework\` sub-folder of the `etc` path:

- `PythonPartsFramework\InterfaceStubs` contain stub files with python signatures for ALLPLAN API; look here when you need to find out how to call a certain ALLPLAN function, or what parameters it requires; 
