---
title: "ProcessMouseMsgService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\ProcessMouseMsgService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# ProcessMouseMsgService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\ProcessMouseMsgService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the service for the mouse message processing

## Abhängigkeiten

- `GeometryExpandService`
- `InputData`
- `InputMode`
- `InputService`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `PythonScriptType`
- `ScriptObjectService`
- `ScriptService`
- `TypeCollections.ModelEleList`

## Klassen

### `ProcessMouseMsgService`

implementation of the service for the mouse message processing
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `process_input_state` | `input_data: InputData, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `tuple[bool, bool]` | process the input state for the mouse message  Args:     input_data: input data     mouse_msg:  mouse message ID     pnt:        input point in Allplan view coordinates     msg_info:   additional mouse message info  Returns:     next step state, continue input state |
| `process_handle_execution` | `input_data: InputData` | `bool` | process the handle execution state  Args:     input_data: input data  Returns:     True if the handle execution is active |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the service for the mouse message processing
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW

from InputMode import InputMode

from TypeCollections.ModelEleList import ModelEleList

from .GeometryExpandService import GeometryExpandService
from .InputData import InputData
from .InputService import InputService
from .PythonScriptType import PythonScriptType
from .ScriptObjectService import ScriptObjectService
from .ScriptService import ScriptService

class ProcessMouseMsgService():
    """ implementation of the service for the mouse message processing
    """

    @staticmethod
    def process_input_state(input_data: InputData,
                            mouse_msg : int,
                            pnt       : AllplanGeo.Point2D,
                            msg_info  : AllplanIFW.AddMsgInfo) -> tuple[bool, bool]:
        """ process the input state for the mouse message

        Args:
            input_data: input data
            mouse_msg:  mouse message ID
            pnt:        input point in Allplan view coordinates
            msg_info:   additional mouse message info

        Returns:
            next step state, continue input state
        """

        match input_data.input_mode:

            #----------------- Expand the geometry

            case InputMode.GeoExpand:
                has_exp_fct, expand = GeometryExpandService.process_mouse_msg(mouse_msg, pnt, msg_info, input_data, ScriptService())

                if not has_exp_fct:
                    return False, False

                if expand and not input_data.coord_input.IsMouseMove(mouse_msg):
                    input_data.input_mode = InputMode.RefPoint


        #----------------- Get the input point

            case InputMode.RefPoint:
                place_pnt = AllplanGeo.Point3D(input_data.create_ele_result.placement_point) \
                                if input_data.create_ele_result.placement_point else \
                            input_data.coord_input.GetInputPoint(mouse_msg, pnt, msg_info).GetPoint()

                input_data.set_insert_matrix_from_point(place_pnt)


        #----------------- Select a handle

            case InputMode.HandleSelect:
                if not input_data.handle_modi_service.process_mouse_msg(mouse_msg, pnt, msg_info):
                    InputService.draw_preview(input_data, False, False, True, True)

                    return False, True


        #----------------- Get the new handle point

            case InputMode.HandleModify:
                input_pnt = input_data.handle_modi_service.new_handle_point_input(mouse_msg, pnt, msg_info)

                match input_data.python_script_type:
                    case PythonScriptType.SCRIPT_OBJECT:
                        if not ScriptObjectService.move_handle(input_data, input_pnt):
                            InputService.draw_preview(input_data, False, False, False, False)

                            return False, True

                    case PythonScriptType.STANDARD:
                        if not ScriptService.move_handle(input_data, input_pnt):
                            InputService.draw_preview(input_data, False, False, False, False)

                            return False, True



        #----------------- Draw the preview

        InputService.draw_preview(input_data, False, False, False, False)

        return True, True


    @staticmethod
    def process_handle_execution(input_data: InputData) -> bool:
        """ process the handle execution state

        Args:
            input_data: input data

        Returns:
            True if the handle execution is active
        """

        if input_data.input_mode != InputMode.HandleModify or input_data.execution_event != AllplanSettings.ExecutionEvent.eHandles:
            return False


        #----------------- Continue or close the handle modification dependent on the selected element count.
        #                  For a single element only one undo step is created for all modifications by an on_cancel_function call

        input_data.is_modified_parameter = True
        input_data.input_mode            = InputMode.HandleSelect

        input_data.coord_input.StopHandleModification()


        #----------------- continue the input in case of single element modification

        if AllplanSettings.PythonPartsSettings.GetInstance().IsSingleElementModification():
            ScriptObjectService.execute_script_object(input_data)

            InputService.draw_preview(input_data, True, True, True, False)

            if input_data.create_ele_result.elements:
                InputService.create_elements_in_db(input_data)

                input_data.create_ele_result.elements = ModelEleList()

            return True


        #----------------- direct close of the modification in case of multiple elements

        ScriptObjectService.on_cancel_function(input_data)

        input_data.is_modified_parameter = False

        return True

```

</details>