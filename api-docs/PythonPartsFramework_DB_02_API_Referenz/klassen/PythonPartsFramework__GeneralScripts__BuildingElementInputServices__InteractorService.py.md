---
title: "InteractorService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InteractorService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# InteractorService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InteractorService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

implementation of the interactor service

## Abhängigkeiten

- `BaseInteractor`
- `BuildingElementInputServices.InputData`
- `BuildingElementPaletteService`
- `DocumentManager`
- `FunctionLockService`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Utility`
- `PythonScriptType`
- `ScriptObjectInteractors.BaseScriptObjectInteractor`
- `TestHelper.ProfileUtil`
- `inspect`
- `os`
- `traceback`
- `typing`

## Klassen

### `InteractorService`

implementation of the interactor service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `start_interactor` | `input_data: InputData, is_only_update: bool` | `tuple[bool, object]` | start the interactor  Args:     input_data:      input data     is_only_update: only update state  Returns:     created interactor state, interactor object |
| `on_preview_draw` | `input_data: InputData` | `None` | Handles the preview draw event.  This event is triggered, when an input in the dialog line is done (e.g. input of a coordinate).  Args:     input_data: input data |
| `on_mouse_leave` | `input_data: InputData` | `None` | Handles the mouse leave event.  This event is triggered, when the mouse leaves the viewport.  Args:     input_data: input data |
| `on_control_event` | `input_data: InputData, event_id: int` | `None` | Handles the on control event.  Called when an event is triggered by a palette control (ex. button).  Args:     input_data: input data     event_id:   event id of the clicked button control |
| `on_cancel_function` | `input_data: InputData, is_cancel_by_menu_function: bool` | `bool` | Handles the cancel function event  This event is triggered when the ESC button is hit during the runtime of the PythonPart.  Args:     input_data:                 input data     is_cancel_by_menu_function: cancel by menu function state  Returns:     True when the PythonPart framework should terminate the PythonPart, False otherwise. |
| `on_value_input_control_enter` | `input_data: InputData` | `bool` | Handles the value input control enter event.  This event is triggered, when enter key is hit during the input inside the input control located in the dialog line.  Args:     input_data: input data  Returns:     True/False for success. |
| `on_shortcut_control_input` | `input_data: InputData, value: int` | `bool` | Handles the input inside the shortcut control  Args:     input_data: input data     value:      shortcut value  Returns:     message was processed: True/False |
| `on_input_undo` | `input_data: InputData` | `bool` | Process the input undo event  Args:     input_data: input data  Returns:     message was processed: True/False |
| `modify_element_property` | `input_data: InputData, page: int, name: str, value: Any` | `None` | Modify property of element  Args:     input_data: input data     page      : the page of the property     name      : the name of the property.     value     : new value for property. |
| `process_mouse_msg` | `input_data: InputData, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool` | Handles the process mouse message event  Args:     input_data: input data     mouse_msg:  mouse message ID     pnt:        input point in Allplan view coordinates     msg_info:   additional mouse message info  Returns:     True/False for success. |
| `save_load_favorite` | `input_data: InputData, is_save: bool, file_name: str` | `bool` | Save or load a favorite  Args:     input_data: input data     is_save:    True = save, False = load     file_name:  Name of the favorite file  Returns:     executed state |
| `reset_param_values` | `input_data: InputData` | `None` | Reset to original parameter values from PYP file  Args:     input_data: input data |
| `__get_script_object_interactor` | `input_data: InputData` | `BaseScriptObjectInteractor | None` | get the script object interactor  Args:     input_data: input data  Returns:     script object interactor |
| `__get_base_interactor` | `input_data: InputData` | `BaseInteractor | None` | get the base interactor  Args:     input_data: input data  Returns:     base interactor |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the interactor service
"""

# pylint: disable=not-callable

from typing import Any, cast

import os
import inspect
import traceback

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Utility as AllplanUtil

from BaseInteractor import BaseInteractor, BaseInteractorData
from BuildingElementInputServices.InputData import InputData
from BuildingElementPaletteService import BuildingElementPaletteService
from DocumentManager import DocumentManager

from ScriptObjectInteractors.BaseScriptObjectInteractor import BaseScriptObjectInteractor

from TestHelper.ProfileUtil import ProfileUtil

from .FunctionLockService import FunctionLockService
from .PythonScriptType import PythonScriptType

try:
    ALLOW_PROFILE = __import__("gprof2dot")

except ModuleNotFoundError:
    ALLOW_PROFILE = None

class InteractorService():
    """ implementation of the interactor service
    """

    @staticmethod
    def start_interactor(input_data     : InputData,
                         is_only_update: bool) -> tuple[bool, object]:
        """ start the interactor

        Args:
            input_data:      input data
            is_only_update: only update state

        Returns:
            created interactor state, interactor object
        """
        if is_only_update:
            BuildingElementPaletteService.set_palette_lock(True)


        #----------------- get the signature

        pyp_path, _ = os.path.split(input_data.file_name)

        if (create_interactor := getattr(input_data.build_ele_script, "create_interactor", None)) is None:
            AllplanUtil.ShowMessageBox("Function 'create_interactor' not implemented in the py-file", AllplanUtil.MB_OK)
            return False, input_data.build_ele_script

        arg_spec = inspect.getfullargspec(create_interactor)

        func_param_count = len(arg_spec.args)

        BuildingElementPaletteService.set_update_lock(True)


        #----------------- create the interactor

        try:
            match func_param_count:
                case 1:
                    input_data.interactor = create_interactor(BaseInteractorData(input_data.coord_input,
                                                                                 input_data.modification_ele_list,
                                                                                 is_only_update,
                                                                                 input_data.execution_event,
                                                                                 input_data.modification_matrix,
                                                                                 pyp_path,
                                                                                 input_data.str_table_service,
                                                                                 input_data.build_ele_list,
                                                                                 input_data.build_ele_composite,
                                                                                 input_data.build_ele_ctrl_props_list,
                                                                                 input_data.modification_ele_list,
                                                                                 input_data.exec_switch_pythonpart,
                                                                                 input_data.org_and_copy_ele_guids))

                case 3:
                    input_data.interactor = create_interactor(input_data.coord_input, pyp_path, input_data.str_table_service)

                case 7:
                    input_data.interactor = create_interactor(input_data.coord_input, pyp_path, input_data.str_table_service,
                                                              input_data.build_ele_list, input_data.build_ele_composite,
                                                              input_data.build_ele_ctrl_props_list, input_data.modification_ele_list)

                case _:
                    input_data.interactor = create_interactor(input_data.coord_input, pyp_path, True, input_data.str_table_service,
                                                              input_data.build_ele_list, input_data.build_ele_composite,
                                                              input_data.build_ele_ctrl_props_list, input_data.modification_ele_list)


        except:                         # pylint: disable=bare-except
            traceback.print_exc()

            BuildingElementPaletteService.set_update_lock(False)

            return False, input_data.build_ele_script

        BuildingElementPaletteService.set_update_lock(False)

        input_data.python_script_type = PythonScriptType.INTERACTOR

        if input_data.interactor and (script_object_interactor := InteractorService.__get_script_object_interactor(input_data)) is not None:
            script_object_interactor.start_input(input_data.coord_input)

        return True, input_data.build_ele_script


    @staticmethod
    def on_preview_draw(input_data: InputData):
        """ Handles the preview draw event.

        This event is triggered, when an input in the dialog line is done (e.g. input of a coordinate).

        Args:
            input_data: input data
        """

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            interactor.on_preview_draw()


    @staticmethod
    def on_mouse_leave(input_data: InputData):
        """ Handles the mouse leave event.

        This event is triggered, when the mouse leaves the viewport.

        Args:
            input_data: input data
        """

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            interactor.on_mouse_leave()


    @staticmethod
    def on_control_event(input_data: InputData,
                         event_id  : int):
        """ Handles the on control event.

        Called when an event is triggered by a palette control (ex. button).

        Args:
            input_data: input data
            event_id:   event id of the clicked button control
        """

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            interactor.on_control_event(event_id)


    @staticmethod
    def on_cancel_function(input_data                : InputData,
                           is_cancel_by_menu_function: bool) -> bool:
        """ Handles the cancel function event

        This event is triggered when the ESC button is hit during the runtime of the PythonPart.

        Args:
            input_data:                 input data
            is_cancel_by_menu_function: cancel by menu function state

        Returns:
            True when the PythonPart framework should terminate the PythonPart, False otherwise.
        """

        if input_data.interactor is None:
            return True

        # In case this is the result of starting a menu function, the PyP must be closed completely.
        # This can be handled by implementing "on_cancel_by_menu_function" or by
        # calling self.interactor.on_cancel_function() 10 times. This last measure is to prevent
        # infinite loops or partially cancelled scripts that lead to the palette still being opened
        # and potential crashes. The number of times is arbitrary high, because some scripts need one or
        # two calls to that function, other would require more calls; this way we should be safe that all
        # the scripts will be correctly cancelled.

        if is_cancel_by_menu_function:
            if (cancel_fct := getattr(input_data.interactor, "on_cancel_by_menu_function", None)) is not None:
                cancel_fct()

                return True

            ret = False

            for _ in range(10):
                if input_data.interactor.on_cancel_function():
                    ret = True

                    break

            if not ret:
                AllplanUtil.ShowMessageBox("The 'on_cancel' function doesn't return a final True", AllplanUtil.MB_OK)

                return False


        #----------------- execute the on cancel in the interactor

        else:
            ret = input_data.interactor.on_cancel_function()

        if input_data.is_only_update:
            FunctionLockService.reset_is_only_update_locks()

            DocumentManager.get_instance().clear_pythonpart_element()

        if ret:
            input_data.interactor = cast(BaseInteractor, None)

        return ret


    @staticmethod
    def on_value_input_control_enter(input_data: InputData) -> bool:
        """ Handles the value input control enter event.

        This event is triggered, when enter key is hit during the input inside the input control
        located in the dialog line.

        Args:
            input_data: input data

        Returns:
            True/False for success.
        """

        if not input_data.interactor:
            return False

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            return interactor.on_value_input_control_enter()

        return False


    @staticmethod
    def on_shortcut_control_input(input_data: InputData,
                                  value     : int) -> bool:
        """ Handles the input inside the shortcut control

        Args:
            input_data: input data
            value:      shortcut value

        Returns:
            message was processed: True/False
        """

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            return interactor.on_shortcut_control_input(value)

        return False


    @staticmethod
    def on_input_undo(input_data: InputData) -> bool:
        """ Process the input undo event

        Args:
            input_data: input data

        Returns:
            message was processed: True/False
        """

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            return interactor.on_input_undo()

        return False


    @staticmethod
    def modify_element_property(input_data: InputData,
                                page      : int,
                                name      : str,
                                value     : Any):
        """ Modify property of element

        Args:
            input_data: input data
            page      : the page of the property
            name      : the name of the property.
            value     : new value for property.
        """

        DocumentManager.get_instance().document = input_data.coord_input.GetInputViewDocument()

        name = name.replace("___DOM", "")

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            interactor.modify_element_property(page, name, value)

        elif input_data.interactor:
            input_data.interactor.modify_element_property(page, name, value)


    @staticmethod
    def process_mouse_msg(input_data: InputData,
                          mouse_msg : int,
                          pnt       : AllplanGeo.Point2D,
                          msg_info  : AllplanIFW.AddMsgInfo) -> bool:
        """ Handles the process mouse message event

        Args:
            input_data: input data
            mouse_msg:  mouse message ID
            pnt:        input point in Allplan view coordinates
            msg_info:   additional mouse message info

        Returns:
            True/False for success.
        """

        if (interactor := input_data.interactor) is None:
            return False

        script_object_interactor = InteractorService.__get_script_object_interactor(input_data)

        if not input_data.coord_input.IsMouseMove(mouse_msg) and ALLOW_PROFILE is not None and AllplanUtil.KeyboardState.IsCtrlKeyPressed():
            if script_object_interactor:
                res = ProfileUtil.profile(script_object_interactor.process_mouse_msg,
                                          mouse_msg, pnt, msg_info, calls_to_print = 20, show_graphical_results = True)

                if not res:
                    interactor.start_next_input()

            else:
                res = ProfileUtil.profile(interactor.process_mouse_msg, mouse_msg, pnt, msg_info,
                                          calls_to_print = 20, show_graphical_results = True)

            return res is True

        if script_object_interactor:
            if not script_object_interactor.process_mouse_msg(mouse_msg, pnt, msg_info):
                interactor.start_next_input()

            return True

        return interactor.process_mouse_msg(mouse_msg, pnt, msg_info)


    @staticmethod
    def save_load_favorite(input_data: InputData,
                           is_save   : bool,
                           file_name : str) -> bool:
        """ Save or load a favorite

        Args:
            input_data: input data
            is_save:    True = save, False = load
            file_name:  Name of the favorite file

        Returns:
            executed state
        """

        if (interactor := InteractorService.__get_base_interactor(input_data)) is None:
            return False

        if is_save:
            if (save_fct := getattr(interactor, "execute_save_favorite", None)):
                save_fct(file_name)

                return True

            return False


        #----------------- load favorite

        if (load_fct := getattr(interactor, "execute_load_favorite", None)):
            load_fct(file_name)

            return True

        if (update_fct := getattr(interactor, "update_after_favorite_read", None)):
            update_fct()

            return True

        return False


    @staticmethod
    def reset_param_values(input_data: InputData):
        """ Reset to original parameter values from PYP file

        Args:
            input_data: input data
        """

        if (interactor := InteractorService.__get_base_interactor(input_data)) is not None:
            if (reset_fct := getattr(interactor, "reset_param_values", None)):
                reset_fct(input_data.build_ele_list)


    @staticmethod
    def __get_script_object_interactor(input_data: InputData) -> (BaseScriptObjectInteractor | None):
        """ get the script object interactor

        Args:
            input_data: input data

        Returns:
            script object interactor
        """

        return getattr(input_data.interactor, "script_object_interactor", None)


    @staticmethod
    def __get_base_interactor(input_data: InputData) -> (BaseInteractor | None):
        """ get the base interactor

        Args:
            input_data: input data

        Returns:
            base interactor
        """

        if input_data.interactor is None:
            return None

        if (interactor := getattr(input_data.interactor, "script_object_interactor", None)) is None:
            return input_data.interactor

        return interactor if isinstance(interactor, BaseInteractor) else None

```

</details>