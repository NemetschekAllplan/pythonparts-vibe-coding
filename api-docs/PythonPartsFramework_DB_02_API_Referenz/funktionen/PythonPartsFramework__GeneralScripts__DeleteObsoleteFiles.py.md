---
title: "DeleteObsoleteFiles"
source: "PythonPartsFramework\GeneralScripts\DeleteObsoleteFiles.py"
type: "module"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# DeleteObsoleteFiles

> **Pfad:** `PythonPartsFramework\GeneralScripts\DeleteObsoleteFiles.py`  
> **Typ:** Modul  
> **Tags:** `script`

## Übersicht

Delete the obsolete files

## Abhängigkeiten

- `FileNameService`
- `NemAll_Python_AllplanSettings`
- `glob`
- `os`
- `shutil`
- `traceback`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `delete_obsolete_files()`

Delete the obsolete files 

**Parameter:**
- Keine

**Rückgabe:** `None`

**Beispiel:**
```python
result = delete_obsolete_files()
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Delete the obsolete files
"""

# pylint: disable=bare-except

import glob
import os
import shutil
import traceback

import NemAll_Python_AllplanSettings as AllplanSettings

from FileNameService import FileNameService

def delete_obsolete_files():
    """ Delete the obsolete files """

    try:
        file_name = AllplanSettings.AllplanPaths.GetEtcPath() + "PythonPartsFramework\\FilesToDelete.dat"

        if file_name.find("\\DeliveryData\\") != -1:
            return

        if not os.path.exists(file_name):
            return

        with open(file_name, 'r', encoding = "utf-8") as file:
            for line in file:
                line = line.strip("\n")

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) < 2 or not parts[1].startswith("etc\\"):
                    continue

                del_file_pattern = FileNameService.get_global_standard_path(parts[1])

                if parts[0] == "d":
                    if os.path.exists(del_file_pattern):
                        shutil.rmtree(del_file_pattern)
                else:
                    for del_file_name in glob.glob(del_file_pattern):
                        if os.path.exists(del_file_name):
                            os.remove(del_file_name)

        if os.access(file_name, os.W_OK):
            os.remove(file_name)

    except:
        traceback.print_exc()

```

</details>