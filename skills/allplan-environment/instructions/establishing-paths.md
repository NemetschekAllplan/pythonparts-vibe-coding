# Establishing paths from Registry

If the `etc` or `prg` paths are not already part of the user's workspace, you can find them in the registry as an emergency fallback. Ensure you replace `<ALLPLAN_VERSION>` with the actual version (e.g., `2025.0`).

## `prg` (Program Path)
Stored in registry under `HKEY_LOCAL_MACHINE\SOFTWARE\NEMETSCHEK\ALLPLAN\<ALLPLAN_VERSION>\InstallRoot`
- `ProgramDataDrive`: Drive letter
- `ProgramDataPath`: Folder path

## `etc` (Data Path)
The **parent folder** of the `etc` path is stored in registry under `HKEY_LOCAL_MACHINE\SOFTWARE\NEMETSCHEK\ALLPLAN\<ALLPLAN_VERSION>\InstallRoot`
- `DataDrive`: Drive letter
- `DataPath`: Folder path
