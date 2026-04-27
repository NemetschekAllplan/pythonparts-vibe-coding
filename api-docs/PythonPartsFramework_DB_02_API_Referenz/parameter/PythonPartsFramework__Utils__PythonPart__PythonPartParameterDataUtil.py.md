---
title: "PythonPartParameterDataUtil"
source: "PythonPartsFramework\Utils\PythonPart\PythonPartParameterDataUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PythonPartParameterDataUtil

> **Pfad:** `PythonPartsFramework\Utils\PythonPart\PythonPartParameterDataUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the PythonPart parameter data utilities

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `BuildingElementListService`
- `BuildingElementMaterialStringTable`
- `BuildingElementService`
- `BuildingElementStringTable`
- `BuildingElementSubElementUtil`
- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`

## Klassen

### `PythonPartParameterDataUtil`

implementation of the PythonPart parameter data utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_data` | `python_part_ele: AllplanEleAdapter.BaseElementAdapter, str_table: BuildingElementStringTable, material_str_table: BuildingElementMaterialStringTable` | `tuple[list[BuildingElement], list[BuildingElementControlProperties]]` | initialize  Args:     python_part_ele:    PythonPart element     str_table:          string table     material_str_table: material string table  Returns:     list of building elements, list of control properties list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart parameter data utilities
"""

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementStringTable import BuildingElementStringTable
from BuildingElementListService import BuildingElementListService
from BuildingElementService import BuildingElementService
from BuildingElementSubElementUtil import BuildingElementSubElementUtil

class PythonPartParameterDataUtil():
    """ implementation of the PythonPart parameter data utilities
    """

    @staticmethod
    def get_data(python_part_ele   : AllplanEleAdapter.BaseElementAdapter,
                 str_table         : BuildingElementStringTable,
                 material_str_table: BuildingElementMaterialStringTable) -> tuple[list[BuildingElement],
                                                                                  list[BuildingElementControlProperties]]:
        """ initialize

        Args:
            python_part_ele:    PythonPart element
            str_table:          string table
            material_str_table: material string table

        Returns:
            list of building elements, list of control properties list
        """

        sucess, file_name, parameter_data = AllplanBaseEle.PythonPartService.GetParameter(python_part_ele)

        if not sucess:
            return [], []


        #----------------- read the PythonPart

        sub_file_name     = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter_data, "SubElementsName")
        add_sub_file_name = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter_data, "__AddPypSubFile__")

        result, build_ele_script, build_ele_list, build_ele_ctrl_props_list, _, _, _ = \
            BuildingElementService.read_data_from_pyp(file_name, str_table, False,
                                                      material_str_table, sub_file_name, False, add_sub_file_name)

        if not result or build_ele_script is None:
            return [], []

        if parameter_data:
            BuildingElementListService.read_fav_data(parameter_data, build_ele_list, is_modification_mode = True,
                                                     script = build_ele_script)

        return build_ele_list, build_ele_ctrl_props_list

```

</details>