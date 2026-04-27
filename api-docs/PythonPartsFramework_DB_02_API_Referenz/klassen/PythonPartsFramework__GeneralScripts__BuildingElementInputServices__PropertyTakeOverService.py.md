---
title: "PropertyTakeOverService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\PropertyTakeOverService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PropertyTakeOverService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\PropertyTakeOverService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the property take over service

## Abhängigkeiten

- `BuildingElementComposite`
- `BuildingElementInputServices.InputData`
- `BuildingElementInputServices.InputService`
- `BuildingElementInputServices.ScriptObjectService`
- `BuildingElementServices.BuildingElementModification`
- `InputMode`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `ScriptObjectInteractors.DockingPointInteractor`
- `Utilities.GeneralConstants`
- `typing`

## Klassen

### `PropertyTakeOverService`

implementation of the property take over service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo, input_data: InputData` | `bool` | Handles the process mouse message event  Args:     mouse_msg:  mouse message ID     pnt:        input point in Allplan view coordinates     msg_info:   additional mouse message info     input_data: input data  Returns:     True/False for success. |
| `modify_element_property` | `self, input_data: InputData, page: int, name: str, value: Any` | `bool` | Modify property of element  Args:     input_data: input data     page:       page index of the modified property     name:       the name of the property.     value:      new value for property.  Returns:     executed state |
| `assign_selected_value` | `self` | `bool` | assign the selected value to the take over parameter  Returns:     value assigned |
| `close` | `input_data: InputData` | `None` | close the take over  Args:     input_data: input data |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the property take over service
"""

# pylint: disable=redefined-variable-type

from typing import Any

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW

from BuildingElementComposite import BuildingElementComposite

from BuildingElementInputServices.InputData import InputData
from BuildingElementInputServices.InputService import InputService
from BuildingElementInputServices.ScriptObjectService import ScriptObjectService
from InputMode import InputMode

from BuildingElementServices.BuildingElementModification import BuildingElementModification

from ScriptObjectInteractors.DockingPointInteractor import DockingPointInteractor

from Utilities.GeneralConstants import GeneralConstants

class PropertyTakeOverService():
    """ implementation of the property take over service
    """

    def __init__(self):
        """ initialize
        """

        self.script_object_interactor : (DockingPointInteractor | None) = None

        self.is_draw_preview = False


    def process_mouse_msg(self,
                          mouse_msg : int,
                          pnt       : AllplanGeo.Point2D,
                          msg_info  : AllplanIFW.AddMsgInfo,
                          input_data: InputData) -> bool:
        """ Handles the process mouse message event

        Args:
            mouse_msg:  mouse message ID
            pnt:        input point in Allplan view coordinates
            msg_info:   additional mouse message info
            input_data: input data

        Returns:
            True/False for success.
        """

        #----------------- input interactor for standard PythonPart

        if not self.script_object_interactor:
            return False

        if not self.script_object_interactor.process_mouse_msg(mouse_msg, pnt, msg_info):
            self.assign_selected_value()
            self.close(input_data)

            input_data.input_mode = InputMode.HandleSelect

        elif self.is_draw_preview:
            docking_pnt = self.script_object_interactor.docking_point

            if docking_pnt.IsValid():
                input_data.set_insert_matrix_from_point(docking_pnt.GetPoint(input_data.coord_input.GetInputViewDocument()))

            InputService.draw_preview(input_data, False, False, False, False)

        return True


    def modify_element_property(self,
                                input_data: InputData,
                                page      : int,
                                name      : str,
                                value     : Any) -> bool:
        """ Modify property of element

        Args:
            input_data: input data
            page:       page index of the modified property
            name:       the name of the property.
            value:      new value for property.

        Returns:
            executed state
        """

        #----------------- start the point take over interactor

        if name.endswith(GeneralConstants.PALETTE_BUTTON_POINT_TAKE_OVER_KEY) and input_data.palette_service:
            self.script_object_interactor = \
                DockingPointInteractor(input_data.build_ele_list[0].get_existing_property( \
                                       name.removesuffix(GeneralConstants.PALETTE_BUTTON_POINT_TAKE_OVER_KEY)),
                                       None)

            self.script_object_interactor.start_input(input_data.coord_input)

            self.is_draw_preview = True

            return True


        #----------------- execute the modification

        if not self.script_object_interactor or not input_data.palette_service:
            return False

        modify_service = BuildingElementModification([self.script_object_interactor.build_ele],
                                                      BuildingElementComposite(), None,
                                                      [self.script_object_interactor.build_ele_ctrl_props])

        if modify_service.modify_element_property(page, name, value, input_data.palette_service.page_building_ele,
                                                  input_data.palette_service.palette_builder, self.script_object_interactor):
            input_data.palette_service.update_palette(-1, False)

        return True


    def assign_selected_value(self) -> bool:
        """ assign the selected value to the take over parameter

        Returns:
            value assigned
        """

        if not self.script_object_interactor:
            return False

        self.script_object_interactor.assign_selected_value()

        self.script_object_interactor = None

        return True


    @staticmethod
    def close(input_data: InputData):
        """ close the take over

        Args:
            input_data: input data
        """

        if input_data.palette_service is not None:
            input_data.palette_service.refresh_palette(input_data.build_ele_list, input_data.build_ele_ctrl_props_list)

        InputService.recalculate_and_draw_preview(input_data, True, False, False)

        ScriptObjectService.start_next_input(input_data)

        str_tmp = input_data.str_table_service.get_string("e_SELECT_HANDLE", "Select the handle")

        input_data.coord_input.InitFirstPointValueInput(AllplanIFW.InputStringConvert(str_tmp),   \
                                                        AllplanIFW.ValueInputControlData(AllplanIFW.eValueInputControlType.eANGLE_COMBOBOX,
                                                                                         True, False))

```

</details>