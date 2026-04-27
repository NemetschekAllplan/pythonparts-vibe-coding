---
title: "InputScriptCreator"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InputScriptCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# InputScriptCreator

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InputScriptCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the input script creator

## Abhängigkeiten

- `BuildingElementPaletteService`
- `FunctionLockService`
- `HandleModificationService`
- `InputData`
- `InputMode`
- `InputService`
- `InteractorService`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_IFW_Input`
- `PythonScriptType`
- `ScriptObjectService`
- `ScriptService`
- `typing`

## Klassen

### `InputScriptCreator`

implementation of the input script creator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `execute` | `input_data: InputData` | `tuple[bool, Any]` | create the input script  Args:     input_data: input data  Returns:     (successfully started, started script object) |
| `start_standard_pythonpart` | `input_data: InputData, update_palette: bool` | `bool` | start the standard PythonPart input  Args:     input_data:     input data     update_palette: update palette state  Returns:     start state |
| `execute_pre_element_delete` | `input_data: InputData` | `bool` | execute the pre element delete  Args:     input_data: input data  Returns:     pre element delete handled state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the input script creator
"""

from typing import Any

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_IFW_Input as AllplanIFW

from BuildingElementPaletteService import BuildingElementPaletteService
from HandleModificationService import HandleModificationService
from InputMode import InputMode

from .FunctionLockService import FunctionLockService
from .InputData import InputData
from .InputService import InputService
from .InteractorService import InteractorService
from .PythonScriptType import PythonScriptType
from .ScriptObjectService import ScriptObjectService
from .ScriptService import ScriptService

class InputScriptCreator:
    """ implementation of the input script creator
    """

    @staticmethod
    def execute(input_data: InputData) -> tuple[bool, Any]:
        """ create the input script

        Args:
            input_data: input data

        Returns:
            (successfully started, started script object)
        """


        #----------------- check for pre PythonPart delete

        if input_data.execution_event == AllplanSettings.ExecutionEvent.eDelete:
            return InputScriptCreator.execute_pre_element_delete(input_data), None


        #----------------- Start the interactor

        if input_data.build_ele_list[0].is_interactor:
            return InteractorService.start_interactor(input_data, input_data.is_only_update)


        #----------------- Create the element

        if not ScriptService.initialize_control_properties(input_data):
            return False, input_data.build_ele_script

        if not ScriptObjectService.create_script_object(input_data) and not ScriptService.create_element(input_data, True):
            return False, input_data.build_ele_script

        if (update_palette := input_data.palette_service is not None):
            input_data.palette_service.switch_pythonpart(input_data.build_ele_list, input_data.build_ele_composite,
                                                         input_data.build_ele_script,
                                                         input_data.build_ele_ctrl_props_list, input_data.file_name)
        else:
            input_data.palette_service = BuildingElementPaletteService(input_data.build_ele_list, input_data.build_ele_composite,
                                                                       input_data.build_ele_script,
                                                                       input_data.build_ele_ctrl_props_list, input_data.file_name)

        return InputScriptCreator.start_standard_pythonpart(input_data, update_palette), input_data.build_ele_script


    @staticmethod
    def start_standard_pythonpart(input_data    : InputData,
                                  update_palette: bool) -> bool:
        """ start the standard PythonPart input

        Args:
            input_data:     input data
            update_palette: update palette state

        Returns:
            start state
        """

        #----------------- show the palette

        if input_data.is_only_update:
            return True

        FunctionLockService.reset_is_only_update_locks()

        if input_data.execution_event == AllplanSettings.ExecutionEvent.eHandles:
            BuildingElementPaletteService.set_palette_lock(True)

        if input_data.palette_service:
            if update_palette:
                input_data.palette_service.update_palette(-1, True)
            else:
                input_data.palette_service.show_palette(input_data.part_name, True)

        if input_data.python_script_type == PythonScriptType.SCRIPT_OBJECT and \
           input_data.script_object.script_object_interactor is not None or \
           input_data.is_modify_elements and not input_data.create_ele_result.handles:
            return True


        #----------------- create the handle modification service

        input_data.handle_modi_service = HandleModificationService(input_data.coord_input, input_data.build_ele_list,
                                                                   input_data.build_ele_ctrl_props_list, input_data.asso_ref_ele,
                                                                   not input_data.modification_ele_list.is_modification_element())


        #----------------- Start the placement point input

        if not input_data.b_insert_point and not input_data.create_ele_result.placement_point:
            str_tmp = input_data.str_table_service.get_string("e_SET_POINT_TO", "Set the to point / Angle")

            input_data.coord_input.InitFirstPointValueInput(AllplanIFW.InputStringConvert(str_tmp),   \
                                                            AllplanIFW.ValueInputControlData(
                                                                AllplanIFW.eValueInputControlType.eANGLE_COMBOBOX,
                                                                True, False))

        else:
            str_tmp = input_data.str_table_service.get_string("e_SELECT_HANDLE", "Select the handle")

            if input_data.execution_event != AllplanSettings.ExecutionEvent.eHandles:
                input_data.coord_input.InitFirstPointValueInput( \
                    AllplanIFW.InputStringConvert(str_tmp),   \
                    AllplanIFW.ValueInputControlData(AllplanIFW.eValueInputControlType.eANGLE_COMBOBOX,
                                                    True, False))

            InputService.recalculate_and_draw_preview(input_data, True, True, False)

            if input_data.input_mode != InputMode.HandleSelect:
                input_data.handle_modi_service.start(input_data.create_ele_result.handles,input_data.insert_matrix,
                                            input_data.coord_input.GetInputViewDocument(), input_data.coord_input.GetViewWorldProjection(),
                                            True)

            input_data.input_mode = InputMode.HandleSelect

        return True


    @staticmethod
    def execute_pre_element_delete(input_data: InputData) -> bool:
        """ execute the pre element delete

        Args:
            input_data: input data

        Returns:
            pre element delete handled state
        """

        if (execute_pre_element_delete := getattr(input_data.build_ele_script, "execute_pre_element_delete", None)) is None:
            return False

        execute_pre_element_delete(input_data.coord_input.GetInputViewDocument(), input_data.build_ele_list,
                                   input_data.modification_ele_list)

        return True

```

</details>