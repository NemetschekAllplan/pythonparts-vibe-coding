---
title: "ScriptObjectService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\ScriptObjectService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# ScriptObjectService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\ScriptObjectService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the script object service

## Abhängigkeiten

- `BaseScriptObject`
- `BuildingElementValueConstraint`
- `ControlPropertiesMinMaxUtil`
- `ControlPropertiesUtil`
- `ControlPropertiesValueListUtil`
- `HandlePropertiesService`
- `InputData`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Utility`
- `PythonScriptType`
- `ScriptObjectInteractors.OnCancelFunctionResult`
- `ScriptObjectInteractors.StartFunctionResult`
- `ScriptService`
- `StringEvaluate`
- `TestHelper.ProfileUtil`
- `TypeCollections`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ValueTypeUtils.MinMaxValidator`
- `typing`

## Klassen

### `ScriptObjectService`

implementation of the script object service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_script_object` | `input_data: InputData` | `bool` | create the element  Args:     input_data: input data  Returns:     script object is created: True/False |
| `start_input` | `input_data: InputData` | `bool` | execute the script object  Args:     input_data: input data  Returns:     next input is started: True/False |
| `start_next_input` | `input_data: InputData` | `bool` | start the next input  Args:     input_data: input data  Returns:     next input is started: True/False |
| `execute_script_object` | `input_data: InputData` | `None` | execute the script object  Args:     input_data: input data |
| `on_preview_draw` | `input_data: InputData` | `bool` | Handles the preview draw event.  This event is triggered, when an input in the dialog line is done (e.g. input of a coordinate).  Args:     input_data: input data  Returns:     execute general preview draw state |
| `on_mouse_leave` | `input_data: InputData` | `bool` | Handles the mouse leave event.  This event is triggered, when the mouse leaves the viewport.  Args:     input_data: input data  Returns:     execute general mouse leave state |
| `process_mouse_msg` | `input_data: InputData, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool | None` | Handles the process mouse message event  Args:     input_data: input data     mouse_msg:  mouse message ID     pnt:        input point in Allplan view coordinates     msg_info:   additional mouse message info  Returns:     True/False for success. |
| `move_handle` | `input_data: InputData, input_pnt: AllplanGeo.Point3D` | `bool` | Move a handle  Args:     input_data: input data     input_pnt:  input point  Returns:     Handle is moved: True/False |
| `on_control_event` | `input_data: InputData, event_id: int` | `None` | Handles the on control event.  Called when an event is triggered by a palette control (ex. button).  Args:     input_data: input data     event_id:   event id of the clicked button control |
| `on_cancel_function` | `input_data: InputData` | `OnCancelFunctionResult` | Cancel the input function  Args:     input_data: input data  Returns:     on cancel function result |
| `on_value_input_control_enter` | `input_data: InputData` | `bool` | Handles the value input control enter event.  This event is triggered, when enter key is hit during the input inside the input control located in the dialog line.  Args:     input_data: input data  Returns:     True/False for success. |
| `on_shortcut_control_input` | `input_data: InputData, value: int` | `bool` | Handles the input inside the shortcut control  Args:     input_data: input data     value:      shortcut value  Returns:     message was processed: True/False |
| `on_input_undo` | `input_data: InputData` | `bool` | Process the input undo event  Args:     input_data: input data  Returns:     message was processed: True/False |
| `process_mouse_move` | `input_data: InputData, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `None` | Handles the process mouse message event  Args:     input_data: input data     mouse_msg:  mouse message ID     pnt:        input point in Allplan view coordinates     msg_info:   additional mouse message info |
| `__set_placement_point` | `input_data: InputData` | `None` | Set the placement point  Args:     input_data: input data |
| `__check_min_max_values` | `input_data: InputData` | `None` | Check the min/max values  Args:     input_data: input data |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the script object service
"""

from typing import cast

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Utility as AllplanUtil

from BaseScriptObject import BaseScriptObject, BaseScriptObjectData
from BuildingElementValueConstraint import BuildingElementValueConstraint
from ControlPropertiesUtil import ControlPropertiesUtil
from ControlPropertiesMinMaxUtil import ControlPropertiesMinMaxUtil
from ControlPropertiesValueListUtil import ControlPropertiesValueListUtil
from HandlePropertiesService import HandlePropertiesService
from StringEvaluate import StringEvaluate

from ScriptObjectInteractors.StartFunctionResult import StartFunctionResult
from ScriptObjectInteractors.OnCancelFunctionResult import OnCancelFunctionResult

from ValueTypes.ValueTypeUtils.MinMaxValidator import MinMaxValidator
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from TypeCollections import ModelEleList

from TestHelper.ProfileUtil import ProfileUtil

from .InputData import InputData
from .PythonScriptType import PythonScriptType
from .ScriptService import ScriptService

try:
    ALLOW_PROFILE = __import__("gprof2dot")

except ModuleNotFoundError:
    ALLOW_PROFILE = None

class ScriptObjectService():
    """ implementation of the script object service
    """

    @staticmethod
    def create_script_object(input_data: InputData) -> bool:
        """ create the element

        Args:
            input_data: input data

        Returns:
            script object is created: True/False
        """

        if (create_script_object := getattr(input_data.build_ele_script, "create_script_object", None)) is None:
            return False

        def update_palette():
            if not input_data.palette_service:
                return

            input_data.palette_service.update_palette(-1, True)

        script_object_data = BaseScriptObjectData(input_data.coord_input,
                                                  input_data.modification_ele_list,
                                                  input_data.is_only_update,
                                                  input_data.execution_event,
                                                  input_data.modification_matrix,
                                                  ControlPropertiesUtil(input_data.build_ele_ctrl_props_list,
                                                                        input_data.build_ele_list),
                                                  input_data.exec_switch_pythonpart,
                                                  update_palette,
                                                  input_data.org_and_copy_ele_guids)

        input_data.python_script_type = PythonScriptType.SCRIPT_OBJECT

        input_data.script_object = cast(BaseScriptObject, create_script_object(input_data.build_ele_list[0],
                                                                               script_object_data))

        script_object = input_data.script_object

        script_object.start_input()

        if script_object.script_object_interactor is not None:
            if script_object.script_object_interactor.start_input(input_data.coord_input) == StartFunctionResult.PRE_SELECTED_ELEMENTS:
                ScriptObjectService.start_next_input(input_data)

                ScriptObjectService.execute_script_object(input_data)

            return True

        ScriptObjectService.execute_script_object(input_data)

        return True


    @staticmethod
    def start_input(input_data: InputData) -> bool:
        """ execute the script object

        Args:
            input_data: input data

        Returns:
            next input is started: True/False
        """

        input_data.is_modify_elements         = False
        input_data.create_ele_result.elements = ModelEleList()

        input_data.script_object.start_input()

        for prop in input_data.build_ele_list[0].get_properties():
            if prop.value_type == ParameterPropertyValueTypes.POINT_CONNECTION:
                prop.value.reset()

        if input_data.script_object.script_object_interactor is not None:
            input_data.script_object.script_object_interactor.start_input(input_data.coord_input)

        return True


    @staticmethod
    def start_next_input(input_data: InputData) -> bool:
        """ start the next input

        Args:
            input_data: input data

        Returns:
            next input is started: True/False
        """

        input_data.script_object.start_next_input()

        if input_data.script_object.script_object_interactor is None:
            for build_ele, ctrl_prop_list in zip(input_data.build_ele_list, input_data.build_ele_ctrl_props_list):
                BuildingElementValueConstraint.check_property_constraint_init(build_ele, ctrl_prop_list)

            ScriptObjectService.execute_script_object(input_data)

        else:
            input_data.script_object.script_object_interactor.start_input(input_data.coord_input)

        return True


    @staticmethod
    def execute_script_object(input_data: InputData):
        """ execute the script object

        Args:
            input_data: input data
        """

        input_data.create_ele_result = input_data.script_object.execute()

        if input_data.is_switch_pythonpart:
            input_data.is_switch_pythonpart = False

            return

        if  input_data.create_ele_result.placement_point is None and \
            (param := input_data.build_ele_list[0].get_property("__PlacementPointConnection__")) is not None:
            if param.value.is_valid():
                input_data.create_ele_result.placement_point = param.value.point

        ScriptObjectService.__set_placement_point(input_data)



        #----------------- test for modify elements

        input_data.is_modify_elements = False

        for ele in input_data.create_ele_result.elements:
            if isinstance(ele, AllplanBasisEle.AllplanElement):
                if not ele.GetBaseElementAdapter().IsNull():
                    input_data.is_modify_elements                = True
                    input_data.create_ele_result.placement_point = AllplanGeo.Point3D()

                    input_data.set_insert_matrix_from_point(AllplanGeo.Point3D())

                    break


    @staticmethod
    def on_preview_draw(input_data: InputData) -> bool:
        """ Handles the preview draw event.

        This event is triggered, when an input in the dialog line is done (e.g. input of a coordinate).

        Args:
            input_data: input data

        Returns:
            execute general preview draw state
        """

        if input_data.script_object.script_object_interactor is not None:
            input_data.script_object.script_object_interactor.on_preview_draw()

            return False

        return True


    @staticmethod
    def on_mouse_leave(input_data: InputData) -> bool:
        """ Handles the mouse leave event.

        This event is triggered, when the mouse leaves the viewport.

        Args:
            input_data: input data

        Returns:
            execute general mouse leave state
        """

        if input_data.script_object.script_object_interactor is not None:
            input_data.script_object.script_object_interactor.on_mouse_leave()

            return False

        return True


    @staticmethod
    def process_mouse_msg(input_data: InputData,
                          mouse_msg : int,
                          pnt       : AllplanGeo.Point2D,
                          msg_info  : AllplanIFW.AddMsgInfo) -> (bool | None):
        """ Handles the process mouse message event

        Args:
            input_data: input data
            mouse_msg:  mouse message ID
            pnt:        input point in Allplan view coordinates
            msg_info:   additional mouse message info

        Returns:
            True/False for success.
        """

        #----------------- input interactor for standard PythonPart

        if input_data.script_object.script_object_interactor is None:
            return None

        res = ProfileUtil.profile(input_data.script_object.script_object_interactor.process_mouse_msg,
                                  mouse_msg, pnt, msg_info, calls_to_print = 20, show_graphical_results = True) \
                if not input_data.coord_input.IsMouseMove(mouse_msg) and ALLOW_PROFILE is not None and \
                   AllplanUtil.KeyboardState.IsCtrlKeyPressed() else \
              input_data.script_object.script_object_interactor.process_mouse_msg(mouse_msg, pnt, msg_info)

        if not res:
            ScriptObjectService.start_next_input(input_data)

            return False

        return True


    @staticmethod
    def move_handle(input_data: InputData,
                    input_pnt : AllplanGeo.Point3D) -> bool:
        """ Move a handle

        Args:
            input_data: input data
            input_pnt:  input point

        Returns:
            Handle is moved: True/False
        """

        if (handle_prop := input_data.handle_modi_service.handle_prop) is None:
            return False

        if (local_pnt := input_data.handle_modi_service.get_local_handle_point(input_pnt)) is None:
            return False


        #----------------- execute the function from the script object

        input_data.is_modified_parameter = True

        try:                                                                                                        # pylint: disable=too-many-try-statements
            if (result := input_data.script_object.move_handle(handle_prop, local_pnt)) is not None:
                input_data.create_ele_result = result

                print("move_handle: remove execute_script from move_handle and return nothing")

                ScriptObjectService.__set_placement_point(input_data)

                ScriptService.update_palette(input_data, handle_prop)

                return True


        #----------------- in case of missing implementation execute default

        except NotImplementedError:
            HandlePropertiesService.update_property_value(input_data.build_ele_list[0], handle_prop, local_pnt)


        #----------------- execute the script object

        ScriptObjectService.__check_min_max_values(input_data)

        ScriptObjectService.execute_script_object(input_data)

        ScriptService.update_palette(input_data, handle_prop)

        return True


    @staticmethod
    def on_control_event(input_data: InputData,
                         event_id  : int):
        """ Handles the on control event.

        Called when an event is triggered by a palette control (ex. button).

        Args:
            input_data: input data
            event_id:   event id of the clicked button control
        """

        if input_data.script_object.on_control_event(event_id) and input_data.palette_service:
            input_data.palette_service.update_palette(-1, False)


    @staticmethod
    def on_cancel_function(input_data: InputData) -> OnCancelFunctionResult:
        """ Cancel the input function

        Args:
            input_data: input data

        Returns:
            on cancel function result
        """

        #----------------- only in case of handle modification check the modified state

        if input_data.execution_event in {AllplanSettings.ExecutionEvent.eHandles,
                                          AllplanSettings.ExecutionEvent.ePropertyPalette} and not input_data.is_modified_parameter:
            return OnCancelFunctionResult.CANCEL_INPUT


        #----------------- execute the cancel function from the script object

        match (result := input_data.script_object.on_cancel_function()):
            case OnCancelFunctionResult.RESTART:
                if input_data.execution_event in {AllplanSettings.ExecutionEvent.eHandles,
                                                  AllplanSettings.ExecutionEvent.ePropertyPalette}:
                    return OnCancelFunctionResult.CANCEL_INPUT

                ScriptObjectService.start_input(input_data)

            case OnCancelFunctionResult.CONTINUE_INPUT:
                ScriptObjectService.start_next_input(input_data)

            case OnCancelFunctionResult.NOT_IMPLEMENTED:
                if input_data.script_object.script_object_interactor is not None:
                    if (result := input_data.script_object.script_object_interactor.on_cancel_function()) is \
                                  OnCancelFunctionResult.CONTINUE_INPUT:
                        ScriptObjectService.start_next_input(input_data)

        return result


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

        if input_data.script_object.on_value_input_control_enter():
            ScriptObjectService.start_next_input(input_data)
            return True

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

        return input_data.script_object.on_shortcut_control_input(value)


    @staticmethod
    def on_input_undo(input_data: InputData) -> bool:
        """ Process the input undo event

        Args:
            input_data: input data

        Returns:
            message was processed: True/False
        """

        return input_data.script_object.on_input_undo()


    @staticmethod
    def process_mouse_move(input_data: InputData,
                           mouse_msg : int,
                           pnt       : AllplanGeo.Point2D,
                           msg_info  : AllplanIFW.AddMsgInfo):
        """ Handles the process mouse message event

        Args:
            input_data: input data
            mouse_msg:  mouse message ID
            pnt:        input point in Allplan view coordinates
            msg_info:   additional mouse message info
        """

        input_data.script_object.process_mouse_move(input_data.coord_input.GetInputPoint(mouse_msg, pnt, msg_info).GetPoint())


    @staticmethod
    def __set_placement_point(input_data: InputData):
        """ Set the placement point

        Args:
            input_data: input data
        """

        if input_data.create_ele_result.placement_point:
            pnt = AllplanGeo.Point3D(input_data.create_ele_result.placement_point)

            input_data.set_insert_matrix_from_point(pnt)


    @staticmethod
    def __check_min_max_values(input_data: InputData):
        """ Check the min/max values

        Args:
            input_data: input data
        """

        build_ele            = input_data.build_ele_list[0]
        build_ele_ctrl_props = input_data.build_ele_ctrl_props_list[0]

        param_dict = StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_local_string_table())

        MinMaxValidator.set_lock_update_message(True)

        ControlPropertiesMinMaxUtil.check_min_max_value(build_ele, build_ele_ctrl_props, param_dict,
                                                        build_ele.get_global_string_table())

        ControlPropertiesValueListUtil.validate_values(build_ele, build_ele_ctrl_props, param_dict)

        MinMaxValidator.set_lock_update_message(False)

```

</details>