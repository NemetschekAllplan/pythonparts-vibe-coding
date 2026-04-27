---
title: "PythonPartScriptObjectUtil"
source: "PythonPartsFramework\Utils\PythonPart\PythonPartScriptObjectUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PythonPartScriptObjectUtil

> **Pfad:** `PythonPartsFramework\Utils\PythonPart\PythonPartScriptObjectUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the PythonPart script object utility

## Abhängigkeiten

- `BaseScriptObject`
- `BuildingElement`
- `BuildingElementInputServices.InputData`
- `BuildingElementInputServices.ScriptObjectService`
- `BuildingElementService`
- `FileNameService`
- `NemAll_Python_IFW_Input`
- `StringTableService`
- `collections.abc`

## Klassen

### `PythonPartScriptObjectUtil`

implementation of the PythonPart script object utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, coord_input: AllplanIFW.CoordinateInput, pyp_file: str` | `None` | initialize  Args:     coord_input: API object for the coordinate input, element selection, ... in the Allplan view     pyp_file:    name of the pyp file |
| `create_script_object` | `self` | `BaseScriptObject | None` | create the script object  Returns:     created script object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart script object utility
"""

from collections.abc import Callable

import NemAll_Python_IFW_Input as AllplanIFW

from BaseScriptObject import BaseScriptObject
from BuildingElement import BuildingElement
from BuildingElementService import BuildingElementService
from FileNameService import FileNameService
from StringTableService import StringTableService

from BuildingElementInputServices.InputData import InputData
from BuildingElementInputServices.ScriptObjectService import ScriptObjectService

class PythonPartScriptObjectUtil(InputData):
    """ implementation of the PythonPart script object utility
    """

    def __init__(self,
                 coord_input: AllplanIFW.CoordinateInput,
                 pyp_file   : str):
        """ initialize

        Args:
            coord_input: API object for the coordinate input, element selection, ... in the Allplan view
            pyp_file:    name of the pyp file
        """

        super().__init__(coord_input, pyp_file)

        self.pyp_file      = pyp_file
        self.sub_build_ele = BuildingElement()
        self.coord_input   = coord_input

        self.exec_switch_pythonpart : Callable = None


    def create_script_object(self) -> (BaseScriptObject | None):
        """ create the script object

        Returns:
            created script object
        """

        _, file_name = FileNameService.get_pyp_path_from_lib_struct(self.pyp_file)

        str_table_service = StringTableService(file_name)

        result, self.build_ele_script, self.build_ele_list, self.build_ele_ctrl_props_list,    \
            self.build_ele_composite, _, file_name = \
            BuildingElementService.read_data_from_pyp(file_name, str_table_service.str_table, False, \
                                                      str_table_service.material_str_table, "", True, "")

        if not result:
            return None

        return self.script_object if ScriptObjectService.create_script_object(self) else None

```

</details>