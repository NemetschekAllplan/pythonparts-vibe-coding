---
title: "BuildingElementSubElementUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementSubElementUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementSubElementUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementSubElementUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

Implementation of the sub element utilities

## Abhängigkeiten

- `FileNameService`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Utility`
- `os`

## Klassen

### `BuildingElementSubElementUtil`

Definition of service class FileNameService
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_file_name` | `file_name: str, sub_elements_file: str, library_preview: bool` | `str` | Get the full name of the file with the sub elements  Args:     file_name:         Full name of the pyp file     sub_elements_file: Name of the sub elements file, "?" = open file dialog     library_preview:   Called for library preview  Returns:     file name |
| `get_file_name_from_parameter` | `parameter_data: list[str], sub_file_param_name: str` | `str` | get the name of the sub file from a parameter  Args:     parameter_data:      parameter data     sub_file_param_name: parameter name of the sub file  Returns:     name of the sub file |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the sub element utilities
"""

# pylint: disable=global-statement

import os

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Utility as AllplanUtil

from FileNameService import FileNameService

STATIC_NODE_SCRIPT_DEFAULT_PATH = ""

class BuildingElementSubElementUtil():
    """ Definition of service class FileNameService
    """

    @staticmethod
    def get_file_name(file_name        : str,
                      sub_elements_file: str,
                      library_preview  : bool) -> str:
        """ Get the full name of the file with the sub elements

        Args:
            file_name:         Full name of the pyp file
            sub_elements_file: Name of the sub elements file, "?" = open file dialog
            library_preview:   Called for library preview

        Returns:
            file name
        """

        if sub_elements_file.find("NodeScripts\\") != -1:
            return STATIC_NODE_SCRIPT_DEFAULT_PATH + "\\" + sub_elements_file

        if len(sub_elements_file):
            path = os.path.dirname(os.path.abspath(file_name))

            if sub_elements_file == "?":
                if library_preview:
                    return file_name

                default_dir = AllplanUtil.DefaultDirectories()

                default_dir.AddDirectory(AllplanSettings.AllplanPaths.GetStdPath())
                default_dir.AddDirectory(AllplanSettings.AllplanPaths.GetUsrPath())
                default_dir.AddDirectory(AllplanSettings.AllplanPaths.GetCurPrjPath())

                sub_elements_file =  AllplanUtil.FileDialog.AskOpenFile(file_name, "Select the file with the sub elements",
                                                                        "pypsub-files(*.pypsub)|*.pypsub|", "pypsub", default_dir)

                return sub_elements_file if sub_elements_file != file_name else ""


            #---------------- get the real path

            if (global_path := FileNameService.get_global_standard_path(sub_elements_file)):
                return global_path


            #----------------- not etc dependent

            if sub_elements_file.find("\\") != -1:
                path = path[:path.rfind("\\")]

            file_name = path + "\\" + sub_elements_file

        return file_name

    @staticmethod
    def get_file_name_from_parameter(parameter_data     : list[str],
                                     sub_file_param_name: str) -> str:
        """ get the name of the sub file from a parameter

        Args:
            parameter_data:      parameter data
            sub_file_param_name: parameter name of the sub file

        Returns:
            name of the sub file
        """

        if (data := next((data for data in parameter_data if data.startswith(sub_file_param_name)), None)) is None:
            return ""

        if (etc_index := data.lower().find("/etc/")) == -1:
            etc_index = data.find("=")

            sub_file_name = data[etc_index + 1:].strip()
        else:
            sub_file_name = AllplanSettings.AllplanPaths.GetPythonPartsEtcPath() + data[etc_index + 5:]

        return sub_file_name.replace("\n","")

```

</details>