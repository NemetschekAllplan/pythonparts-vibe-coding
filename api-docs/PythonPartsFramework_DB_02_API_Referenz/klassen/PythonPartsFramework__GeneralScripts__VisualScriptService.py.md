---
title: "VisualScriptService"
source: "PythonPartsFramework\GeneralScripts\VisualScriptService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# VisualScriptService

> **Pfad:** `PythonPartsFramework\GeneralScripts\VisualScriptService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the VisualScript service

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `BuildingElementConverter`
- `BuildingElementListService`
- `BuildingElementService`
- `BuildingElementValueUtil`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Utility`
- `NodeScript`
- `ParameterProperty`
- `StringTableService`
- `TypeCollections.ModificationElementList`
- `__future__`
- `dataclasses`
- `typing`

## Klassen

### `DefaultValue`

implementation of the data class for the default value 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `VisualScriptService`

implementation of the VisualScript service 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, coord_input: AllplanIFW.CoordinateInput, script_path: str, global_str_table_service: StringTableService, build_ele_list: list[BuildingElement], control_props_list: list[BuildingElementControlProperties], default_values: list[DefaultValue]` | `None` | Initialize the script  Args:     coord_input:              API object for the coordinate input, element selection, ... in the Allplan view     script_path:              script path     global_str_table_service: global string table service     build_ele_list:           list with the building elements     control_props_list:       control properties list     default_values:           default values  Raises:     ValueError: raised in case of wrong script |
| `close_all` | `self` | `None` | close the VS script          |
| `modify_element_property` | `self, page: int, name: str, value: Any` | `None` | Modify property of element  Args:     page:  page index of the modified property     name:  the name of the property.     value: new value for property. |
| `on_cancel_function` | `self` | `bool` | Check for input function cancel in case of ESC  Returns:     True/False for success. |
| `on_control_event` | `self, event_id: int` | `None` | Handles on control event  Args:     event_id: event id of the clicked button control |
| `get_preview_elements` | `self` | `list[Any]` | get the preview elements created by the script  Returns:     preview elements of the script |
| `create_pythonpart` | `self, placement_matrix: AllplanGeo.Matrix3D, local_placement_matrix: AllplanGeo.Matrix3D` | `list[Any]` | create the PythonPart  Args:     placement_matrix:       placement matrix of the PythonPart (model placement)     local_placement_matrix: local placement matrix of the PythonPart, used for the local geometry transformation   Returns:     created PythonPart elements |
| `reset_param_values` | `self` | `None` | reset the parameter values          |
| `execute_save_favorite` | `self, file_name: str` | `None` | save the favorite data  Args:     file_name: file name |
| `execute_load_favorite` | `self, file_name: str` | `None` | load the favorite data  Args:     file_name: file name |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the VisualScript service
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from dataclasses import dataclass

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Utility as AllplanUtil

import BuildingElementValueUtil

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementConverter import BuildingElementConverter
from BuildingElementListService import BuildingElementListService
from BuildingElementService import BuildingElementService
from ParameterProperty import ParameterProperty
from StringTableService import StringTableService

from TypeCollections.ModificationElementList import ModificationElementList

if TYPE_CHECKING:
    from NodeScript import NodeScript

@dataclass
class DefaultValue():
    """ implementation of the data class for the default value """

    element_id: str     # element id of the building element
    name      : str     # name of the parameter property
    value     : str     # value


class VisualScriptService():
    """ implementation of the VisualScript service """

    NODE_SCRIPT = "NodeScript"

    def __init__(self,
                 coord_input             : AllplanIFW.CoordinateInput,
                 script_path             : str,
                 global_str_table_service: StringTableService,
                 build_ele_list          : list[BuildingElement],
                 control_props_list      : list[BuildingElementControlProperties],
                 default_values          : list[DefaultValue]):
        """ Initialize the script

        Args:
            coord_input:              API object for the coordinate input, element selection, ... in the Allplan view
            script_path:              script path
            global_str_table_service: global string table service
            build_ele_list:           list with the building elements
            control_props_list:       control properties list
            default_values:           default values

        Raises:
            ValueError: raised in case of wrong script
        """

        self.parent_build_ele_list     = build_ele_list
        self.parent_control_props_list = control_props_list


        #----------------- create the visual script

        result, build_ele_script, self.build_ele_list, self.control_props_list, self.build_ele_composite, _, _ = \
            BuildingElementService().read_data_from_pyp(script_path,
                                                        global_str_table_service.str_table, False,
                                                        global_str_table_service.material_str_table, "", False)

        if not result or build_ele_script is None:
            return

        if build_ele_script.__name__ != VisualScriptService.NODE_SCRIPT:
            msg = "Invalid script selected for Visual Scripting Service."

            AllplanUtil.ShowMessageBox(msg, AllplanUtil.MB_OK)

            raise ValueError(msg)

        self.script_build_ele = self.build_ele_list[0]

        self.build_ele_list    [0] = build_ele_list[0]
        self.control_props_list[0] = control_props_list[0]


        #----------------- set the default values

        if default_values is not None:
            for default_value in default_values:
                element_id = f"{default_value.element_id}___"

                if not (build_ele := next((build_ele for build_ele in self.build_ele_list if build_ele.element_id == element_id), None)):
                    AllplanUtil.ShowMessageBox(f"Building element with element ID={default_value.element_id} not found",
                                               AllplanUtil.MB_OK)
                    continue

                BuildingElementConverter.read_from_list(build_ele,
                                                        [f"{default_value.name}={default_value.value}"],
                                                        ParameterProperty.Persistent.MODEL)


        #----------------- create the sub interactor

        self.interactor : (NodeScript | None) = build_ele_script.create_sub_interactor(coord_input, script_path, global_str_table_service,
                                                                                       self.build_ele_list, self.build_ele_composite,
                                                                                       self.control_props_list, ModificationElementList(),
                                                                                       True, False)


    def close_all(self):
        """ close the VS script
        """

        if self.interactor:
            self.interactor.close_all()


    def modify_element_property(self,
                                page : int,
                                name : str,
                                value: Any):
        """ Modify property of element

        Args:
            page:  page index of the modified property
            name:  the name of the property.
            value: new value for property.
        """

        if self.parent_build_ele_list[0].get_property(name):
            BuildingElementValueUtil.update_value(name, value, self.parent_build_ele_list[0], self.parent_control_props_list[0])

            return

        if self.interactor is not None:
            self.interactor.modify_element_property(page, name, value)


    def on_cancel_function(self) -> bool:
        """ Check for input function cancel in case of ESC

        Returns:
            True/False for success.
        """

        if self.interactor is not None:
            self.interactor.close_all()

        return True


    def on_control_event(self,
                         event_id: int):
        """ Handles on control event

        Args:
            event_id: event id of the clicked button control
        """

        if self.interactor:
            self.interactor.on_control_event(event_id)


    def get_preview_elements(self) -> list[Any]:
        """ get the preview elements created by the script

        Returns:
            preview elements of the script
        """

        return [] if self.interactor is None else self.interactor.get_preview_elements()


    def create_pythonpart(self,
                          placement_matrix      : AllplanGeo.Matrix3D,
                          local_placement_matrix: AllplanGeo.Matrix3D) -> list[Any]:
        """ create the PythonPart

        Args:
            placement_matrix:       placement matrix of the PythonPart (model placement)
            local_placement_matrix: local placement matrix of the PythonPart, used for the local geometry transformation


        Returns:
            created PythonPart elements
        """

        if self.interactor is None:
            return []

        self.build_ele_list[0] = self.script_build_ele

        elements = self.interactor.create_pythonpart(self.build_ele_list, placement_matrix, local_placement_matrix)

        self.build_ele_list[0] = self.parent_build_ele_list[0]

        return elements


    def reset_param_values(self):
        """ reset the parameter values
        """

        BuildingElementListService.reset_param_values(self.parent_build_ele_list)

        if self.interactor is not None:
            self.interactor.reset_param_values(self.build_ele_list)


    def execute_save_favorite(self,
                              file_name: str):
        """ save the favorite data

        Args:
            file_name: file name
        """

        BuildingElementListService.write_to_file(file_name, self.build_ele_list)


    def execute_load_favorite(self,
                              file_name: str):
        """ load the favorite data

        Args:
            file_name: file name
        """

        BuildingElementListService.read_from_file(file_name, self.build_ele_list)

        if self.interactor is not None:
            self.interactor.update_after_favorite_read()

```

</details>