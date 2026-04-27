---
title: "BuildingElementInput"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInput.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementInput

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInput.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Script for BuildingElementInput

## Abhängigkeiten

- `BuildingElementInputServices.FunctionLockService`
- `BuildingElementInputServices.HandleInputSwitcher`
- `BuildingElementInputServices.InputData`
- `BuildingElementInputServices.InputScriptCreator`
- `BuildingElementInputServices.InputService`
- `BuildingElementInputServices.InteractorService`
- `BuildingElementInputServices.ProcessMouseMsgService`
- `BuildingElementInputServices.PropertyTakeOverService`
- `BuildingElementInputServices.PythonScriptType`
- `BuildingElementInputServices.ScriptObjectService`
- `BuildingElementInputServices.ScriptService`
- `BuildingElementListService`
- `BuildingElementStringTableManager`
- `BuildingElementSubElementUtil`
- `DeleteObsoleteFiles`
- `DocumentManager`
- `ErrorLogWindow`
- `FileNameService`
- `ImportHook`
- `InputMode`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Utility`
- `PythonPartPreview`
- `ScriptObjectInteractors.OnCancelFunctionResult`
- `TraceService`
- `TypeCollections.ModificationElementList`
- `locale`
- `os`
- `os.path`
- `sys`
- `typing`

## Klassen

### `BuildingElementInput`

Definition of class BuildingElementInput
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, coord_input: AllplanIFW.CoordinateInput, path: str` | `None` | Initialization of class BuildingElementInput  Args:     coord_input:    Coordinate input class     path:           Python script path |
| `start_input` | `self, file_name: str, parameter_data: list[str], msg_info: AllplanIFW.AddMsgInfo | None, modify_uuid_list: ModificationElementList, geo_matrix: AllplanGeo.Matrix3D, local_placement_matrix: AllplanGeo.Matrix3D, asso_ref_ele: AllplanElementAdapter.BaseElementAdapter, execution_event: AllplanSettings.ExecutionEvent=AllplanSettings.ExecutionEvent.eCreation, modification_matrix: AllplanGeo.Matrix3D=AllplanGeo.Matrix3D(), org_and_copy_ele_guids: dict[str, str] | None=None` | `tuple[bool, Any]` | Start the input function  Args:     file_name:              file name of the pyp file     parameter_data:         parameter data of the selected PythonPart     msg_info:               additional mouse message info     modify_uuid_list:       list with the UUIDs of the modified elements     geo_matrix:             placement matrix     local_placement_matrix: local placement matrix     asso_ref_ele:           reference element of the associative view     execution_event:        modification event     modification_matrix:    modification matrix     org_and_copy_ele_guids: Map of GUIDs for original and copy elements, for the case when python part was called by copy function.  Returns:     (successfully started, started script object) |
| `on_control_event` | `self, event_id: int` | `None` | On control event  Args:     event_id: event id of control. |
| `on_value_input_control_enter` | `self` | `bool` | Process the enter inside the value input control  Returns:     message was processed: True/False |
| `on_shortcut_control_input` | `self, value: int` | `bool` | Handles the input inside the shortcut control  Args:     value: shortcut value  Returns:     message was processed: True/False |
| `on_input_undo` | `self` | `bool` | Process the input undo event  Returns:     message was processed: True/False |
| `on_cancel_function` | `self` | `bool` | Cancel the input function  Returns:     True/False for success. |
| `on_preview_draw` | `self` | `None` | Handles the preview draw event          |
| `on_mouse_leave` | `self` | `None` | Handles the mouse leave event          |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool` | Handles the process mouse message event  Args:     mouse_msg: the mouse message.     pnt      : the input point.     msg_info : additional message info.  Returns:     True/False for success. |
| `modify_element_property` | `self, page: int, name: str, value: Any` | `None` | Modify property of element  Args:     page:   the page of the property     name:   the name of the property.     value:  new value for property. |
| `show_palette` | `self` | `None` | show the palette          |
| `close_palette` | `self` | `None` | Close the palette          |
| `save_load_favorite` | `self, is_save: bool, file_name: str` | `None` | Save or load a favorite  Args:     is_save:   True = save, False = load     file_name: Name of the favorite file |
| `reset_param_values` | `self` | `None` | Reset to original parameter values from PYP file          |
| `is_visualeditor_running` | `self, _power_management: bool, cancel_by_menu_function: bool` | `bool` | check for running visual editor  Args:     _power_management:       checking for power management     cancel_by_menu_function: cancel is execute due to menu function start  Returns:     Visual Editor is running |
| `__get_pyp_file_name` | `file_name: str` | `str` | Get the file name of the PythonPart  Args:     file_name: Name of the pyp file  Returns:     file name of the PythonPart |
| `__start_next_input` | `self` | `bool` | start the next input if multi placement is active  Returns:     next input is started: True/False |
| `__get_point_from_insert_matrix` | `self` | `AllplanGeo.Point3D` | Get input point from the insert matrix  Returns:     point from the insert matrix |
| `__switch_to_pythonpart_from_stack` | `self` | `bool` | Switch to another PythonPart from the stack  Returns:     input canceled state |
| `switch_pythonpart` | `self, file_name: str, add_current_to_stack: bool` | `None` | Switch to another PythonPart  Args:     file_name:            file name of the PythonPart     add_current_to_stack: add the current pyp file to the stack |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementInput
"""

# pylint: disable=too-many-instance-attributes
# pylint: disable=not-callable
# pylint: disable=bare-except

import locale
import os
import os.path
import sys

from typing import Any

import ErrorLogWindow

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_IFW_ElementAdapter as AllplanElementAdapter
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Utility as AllplanUtil

from BuildingElementListService import BuildingElementListService
from BuildingElementStringTableManager import BuildingElementStringTableManager
from BuildingElementSubElementUtil import BuildingElementSubElementUtil
from DeleteObsoleteFiles import delete_obsolete_files
from DocumentManager import DocumentManager
from FileNameService import FileNameService
from ImportHook import ImportHookFinder
from InputMode import InputMode
from TraceService import TraceService

from BuildingElementInputServices.FunctionLockService import FunctionLockService
from BuildingElementInputServices.HandleInputSwitcher import HandleInputSwitcher
from BuildingElementInputServices.InteractorService import InteractorService
from BuildingElementInputServices.InputData import InputData
from BuildingElementInputServices.InputService import InputService
from BuildingElementInputServices.InputScriptCreator import InputScriptCreator
from BuildingElementInputServices.ProcessMouseMsgService import ProcessMouseMsgService
from BuildingElementInputServices.PropertyTakeOverService import PropertyTakeOverService
from BuildingElementInputServices.PythonScriptType import PythonScriptType
from BuildingElementInputServices.ScriptObjectService import ScriptObjectService
from BuildingElementInputServices.ScriptService import ScriptService

from PythonPartPreview import PythonPartPreview

from ScriptObjectInteractors.OnCancelFunctionResult import OnCancelFunctionResult

from TypeCollections.ModificationElementList import ModificationElementList

sys.meta_path.append(ImportHookFinder)

os.environ['TCL_LIBRARY'] = f"{AllplanSettings.AllplanPaths.GetPrgPath()}\\Python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY']  = f"{AllplanSettings.AllplanPaths.GetPrgPath()}\\Python\\tcl\\tk8.6"

class BuildingElementInput(InputData):
    """ Definition of class BuildingElementInput
    """
    def __init__(self,
                 coord_input: AllplanIFW.CoordinateInput,
                 path       : str):
        """ Initialization of class BuildingElementInput

        Args:
            coord_input:    Coordinate input class
            path:           Python script path
        """

        locale.setlocale(locale.LC_TIME, "")

        self.property_take_over_service = PropertyTakeOverService()

        super().__init__(coord_input, path)

        self.is_cancel_by_menu_function = False

        TraceService(True)

        if not AllplanUtil.IsExecutedByUnitTest():
            delete_obsolete_files()

        ErrorLogWindow.clear_error_log_window()

        if (str_table := BuildingElementStringTableManager.get_instance()):
            str_table.clear_global_string_table()

        FileNameService.set_node_script_default_path(os.path.dirname(os.path.abspath(path)))

        DocumentManager.get_instance().document = self.coord_input.GetInputViewDocument()

        self.pyp_file_stack = list[str]()


    def start_input(self,
                    file_name             : str,
                    parameter_data        : list[str],
                    msg_info              : (AllplanIFW.AddMsgInfo | None),
                    modify_uuid_list      : ModificationElementList,
                    geo_matrix            : AllplanGeo.Matrix3D,
                    local_placement_matrix: AllplanGeo.Matrix3D,
                    asso_ref_ele          : AllplanElementAdapter.BaseElementAdapter,
                    execution_event       : AllplanSettings.ExecutionEvent = AllplanSettings.ExecutionEvent.eCreation,
                    modification_matrix   : AllplanGeo.Matrix3D            = AllplanGeo.Matrix3D(),
                    org_and_copy_ele_guids: (dict[str, str] | None)        = None) -> tuple[bool, Any]:
        """ Start the input function

        Args:
            file_name:              file name of the pyp file
            parameter_data:         parameter data of the selected PythonPart
            msg_info:               additional mouse message info
            modify_uuid_list:       list with the UUIDs of the modified elements
            geo_matrix:             placement matrix
            local_placement_matrix: local placement matrix
            asso_ref_ele:           reference element of the associative view
            execution_event:        modification event
            modification_matrix:    modification matrix
            org_and_copy_ele_guids: Map of GUIDs for original and copy elements, for the case when python part was called by copy function.

        Returns:
            (successfully started, started script object)
        """

        is_only_update = execution_event not in {AllplanSettings.ExecutionEvent.eCreation,
                                                 AllplanSettings.ExecutionEvent.eProperties,
                                                 AllplanSettings.ExecutionEvent.ePropertyPalette,
                                                 AllplanSettings.ExecutionEvent.eHandles}

        FunctionLockService.set_is_only_update_locks(is_only_update, execution_event)

        self.init_general_data(modify_uuid_list, asso_ref_ele, is_only_update, execution_event, modification_matrix,
                               {} if org_and_copy_ele_guids is None else org_and_copy_ele_guids)


        #----------------- get the sub file name from the input by ?

        sub_file_name     = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter_data, "SubElementsName")
        add_sub_file_name = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter_data, "__AddPypSubFile__")

        if sub_file_name:
            _, sub_file_name = FileNameService.get_pyp_path_from_lib_struct(sub_file_name, True)

        if add_sub_file_name:
            _, add_sub_file_name = FileNameService.get_pyp_path_from_lib_struct(add_sub_file_name, True)


        #------------------ Load the building element and prepare the script data

        file_name = self.__get_pyp_file_name(file_name)

        result,                             \
        self.build_ele_script,              \
        self.build_ele_list,                \
        self.build_ele_ctrl_props_list,     \
        self.build_ele_composite,           \
        self.part_name,                     \
        self.file_name = self.build_ele_service.read_data_from_pyp(file_name, self.str_table_service.str_table, False, \
                                                                   self.str_table_service.material_str_table, sub_file_name,
                                                                   execution_event == AllplanSettings.ExecutionEvent.eCreation,
                                                                   add_sub_file_name)

        if not result or self.build_ele_script is None:
            return False, self.build_ele_script

        self.prepare_script_data(parameter_data, msg_info, execution_event != AllplanSettings.ExecutionEvent.eCreation,
                                 geo_matrix, local_placement_matrix)

        self.exec_switch_pythonpart = self.switch_pythonpart

        result =  InputScriptCreator.execute(self)

        # we need to set the method modify_element_property as a callback for the palette's value change event handler

        if self.palette_service and self.palette_service.palette_builder and self.palette_service.palette_builder.change_handler:
            self.palette_service.palette_builder.change_handler.set_modify_property_callback(self.modify_element_property)

        return result


    def on_control_event(self, event_id: int):
        """ On control event

        Args:
            event_id: event id of control.
        """

        if InputService.open_web_browser(self, event_id):
            return


        #----------------- execute the control event for interactor / script object

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                InteractorService.on_control_event(self, event_id)

                return

            case PythonScriptType.SCRIPT_OBJECT:
                ScriptObjectService.on_control_event(self, event_id)

                InputService.recalculate_and_draw_preview(self, True, False, False)

                return


        #----------------- standard PythonPart

        if self.palette_service and self.palette_service.on_control_event(event_id):
            if ScriptService.modify_control_properties(self, "", event_id):
                self.palette_service.update_palette(-1, False)

            InputService.recalculate_and_draw_preview(self, True, False, False)

            return

        if ScriptService.modify_control_properties(self, "", event_id) and self.palette_service:
            self.palette_service.update_palette(-1, False)


    def on_value_input_control_enter(self) -> bool:
        """ Process the enter inside the value input control

        Returns:
            message was processed: True/False
        """

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                return InteractorService.on_value_input_control_enter(self)

            case PythonScriptType.SCRIPT_OBJECT:
                return ScriptObjectService.on_value_input_control_enter(self)

        return False


    def on_shortcut_control_input(self,
                                  value: int) -> bool:
        """ Handles the input inside the shortcut control

        Args:
            value: shortcut value

        Returns:
            message was processed: True/False
        """

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                return InteractorService.on_shortcut_control_input(self, value)

            case PythonScriptType.SCRIPT_OBJECT:
                return ScriptObjectService.on_shortcut_control_input(self, value)

        return False


    def on_input_undo(self) -> bool:
        """ Process the input undo event

        Returns:
            message was processed: True/False
        """

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                return InteractorService.on_input_undo(self)

            case PythonScriptType.SCRIPT_OBJECT:
                return ScriptObjectService.on_input_undo(self)

        return False


    def on_cancel_function(self) -> bool:
        """ Cancel the input function

        Returns:
            True/False for success.
        """

        PythonPartPreview.close()


        #----------------- close the take over

        if self.property_take_over_service.assign_selected_value():
            self.property_take_over_service.close(self)

            return False


        #----------------- cancel the input inside the interactor / script object

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                if not InteractorService.on_cancel_function(self, self.is_cancel_by_menu_function):
                    return False

                return self.__switch_to_pythonpart_from_stack()


            case PythonScriptType.SCRIPT_OBJECT:
                match ScriptObjectService.on_cancel_function(self):
                    case OnCancelFunctionResult.CANCEL_INPUT:
                        FunctionLockService.reset_is_only_update_locks()

                        return self.__switch_to_pythonpart_from_stack()

                    case (OnCancelFunctionResult.CONTINUE_INPUT | OnCancelFunctionResult.RESTART):
                        if self.python_script_type == PythonScriptType.SCRIPT_OBJECT:                   # maybe a new script was started
                            InputScriptCreator.start_standard_pythonpart(self, True)

                        return False


        #----------------- check the input mode

        if self.is_modify_elements:
            self.input_mode = InputMode.HandleSelect

        if self.input_mode in [InputMode.RefPoint, InputMode.GeoExpand]:
            return self.__switch_to_pythonpart_from_stack()


        #----------------- restore the original value in case of canceling the handle modification

        if self.input_mode == InputMode.HandleModify:
            self.handle_modi_service.reset_value()

            self.input_mode = InputMode.HandleSelect

            InputService.recalculate_and_draw_preview(self, True, True, False)

            return False


        #----------------- create the elements

        if self.execution_event == AllplanSettings.ExecutionEvent.eHandles:
            return True

        if self.input_mode == InputMode.HandleSelect:
            InputService.create_elements_in_db(self)

            if self.is_only_update:
                FunctionLockService.reset_is_only_update_locks()

                DocumentManager.get_instance().clear_pythonpart_element()

            if not self.__start_next_input():
                return self.__switch_to_pythonpart_from_stack()

        return False


    def on_preview_draw(self):                  # NOSONAR
        """ Handles the preview draw event
        """

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                InteractorService.on_preview_draw(self)

                return

            case PythonScriptType.SCRIPT_OBJECT:
                if not ScriptObjectService.on_preview_draw(self):
                    return


        #----------------- get the current point for the preview

        match self.input_mode:
            case InputMode.WriteToDB:
                return

            case InputMode.RefPoint:
                pnt = AllplanGeo.Point3D(self.create_ele_result.placement_point) if self.create_ele_result.placement_point else \
                      self.coord_input.GetCurrentPoint().GetPoint()

                self.set_insert_matrix_from_point(pnt)

                self.build_ele_list[0].set_insert_matrix(self.insert_matrix)

            case InputMode.HandleModify:
                if (handle_prop := self.handle_modi_service.handle_prop):
                    pnt = self.coord_input.GetCurrentPoint(self.__get_point_from_insert_matrix() + handle_prop.ref_point, True).GetPoint()

                    match self.python_script_type:
                        case PythonScriptType.SCRIPT_OBJECT:
                            if not ScriptObjectService.move_handle(self, pnt):
                                return

                        case PythonScriptType.STANDARD:
                            if not ScriptService.move_handle(self, pnt):
                                return


        #----------------- draw the preview

        if self.input_mode not in (InputMode.HandleSelect, InputMode.HandleModify):
            InputService.recalculate_and_draw_preview(self, True, False, True)
        else:
            InputService.draw_preview(self, True, False, False, True)


    def on_mouse_leave(self):
        """ Handles the mouse leave event
        """

        #----------------- mouse leave for the interactor

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                InteractorService.on_mouse_leave(self)

                return

            case PythonScriptType.SCRIPT_OBJECT:
                if not ScriptObjectService.on_mouse_leave(self):
                    return



        #----------------- draw the preview

        if self.input_mode > InputMode.RefPoint or \
           self.input_mode <= InputMode.RefPoint and self.python_script_type == PythonScriptType.SCRIPT_OBJECT:
            InputService.draw_preview(self, True, False, False, False)

        elif self.create_ele_result.placement_point:
            pnt = AllplanGeo.Point3D(self.create_ele_result.placement_point)

            self.set_insert_matrix_from_point(pnt)

            InputService.draw_preview(self, True, False, False, False)


    def process_mouse_msg(self,
                          mouse_msg: int,
                          pnt      : AllplanGeo.Point2D,
                          msg_info : AllplanIFW.AddMsgInfo) -> bool:
        """ Handles the process mouse message event

        Args:
            mouse_msg: the mouse message.
            pnt      : the input point.
            msg_info : additional message info.

        Returns:
            True/False for success.
        """

        if self.property_take_over_service.process_mouse_msg(mouse_msg, pnt, msg_info, self):
            return True


        #----------------- process the mouse message

        match self.python_script_type:
            case PythonScriptType.INTERACTOR:
                return InteractorService.process_mouse_msg(self, mouse_msg, pnt, msg_info)

            case PythonScriptType.SCRIPT_OBJECT:
                if (result := ScriptObjectService.process_mouse_msg(self, mouse_msg, pnt, msg_info)) is not None:
                    if not result:
                        InputScriptCreator.start_standard_pythonpart(self, True)

                    return True


        #----------------- check the next input state

        next_step, continue_input = ProcessMouseMsgService.process_input_state(self, mouse_msg, pnt, msg_info)

        if not next_step:
            return continue_input


        #----------------- Continue the input in case of wrong elements or mouse move

        if self.create_ele_result.is_empty():
            return True

        if self.coord_input.IsMouseMove(mouse_msg):
            return True

        if ProcessMouseMsgService.process_handle_execution(self):
            return True


        #----------------- continue with the next input mode

        if self.input_mode != InputMode.WriteToDB:
            self.input_mode = list(InputMode)[self.input_mode]

        if HandleInputSwitcher.execute(self, self.palette_service):
            return True

        InputService.create_elements_in_db(self)

        return self.__start_next_input()


    def modify_element_property(self,
                                page : int,
                                name : str,
                                value: Any):
        """ Modify property of element

        Args:
            page:   the page of the property
            name:   the name of the property.
            value:  new value for property.
        """

        if InputService.modify_active_page(self, name, value):
            return

        if self.property_take_over_service.modify_element_property(self, page, name, value):
            return


        #------------------- change to property palette state

        if self.execution_event == AllplanSettings.ExecutionEvent.eHandles:
            PythonPartPreview.set_preview_draw_lock(False)

            self.execution_event = AllplanSettings.ExecutionEvent.ePropertyPalette


        #------------------- modify the property

        match self.python_script_type:
            case PythonScriptType.SCRIPT_OBJECT:
                has_script_object_interactor = self.script_object.script_object_interactor

                InputService.modify_element_property(self, page, name, value)

                if has_script_object_interactor and not self.script_object.script_object_interactor:
                    InputScriptCreator.start_standard_pythonpart(self, True)

            case PythonScriptType.INTERACTOR:
                InteractorService.modify_element_property(self, page, name, value)

            case PythonScriptType.STANDARD:
                InputService.modify_element_property(self, page, name, value)


    def show_palette(self):
        """ show the palette
        """

        self.execution_event = AllplanSettings.ExecutionEvent.ePropertyPalette

        FunctionLockService.reset_is_only_update_locks()

        if self.palette_service is not None:
            self.palette_service.show_palette(self.part_name)


    def close_palette(self):
        """ Close the palette
        """

        if self.palette_service is not None:
            self.palette_service.close_palette()

        PythonPartPreview.close()


    def save_load_favorite(self,
                           is_save  : bool,
                           file_name: str):
        """ Save or load a favorite

        Args:
            is_save:   True = save, False = load
            file_name: Name of the favorite file
        """

        if InteractorService.save_load_favorite(self, is_save, file_name):
            return

        if is_save:
            BuildingElementListService.write_to_file(file_name, self.build_ele_list)
        else:
            BuildingElementListService.read_from_file(file_name, self.build_ele_list)

            if self.palette_service:
                self.palette_service.update_palette(-1, True)

            InputService.recalculate_and_draw_preview(self, True, True, False)


    def reset_param_values(self):
        """ Reset to original parameter values from PYP file
        """

        if self.python_script_type == PythonScriptType.INTERACTOR:
            InteractorService.reset_param_values(self)

            return

        BuildingElementListService.reset_param_values(self.build_ele_list)

        InputService.recalculate_and_draw_preview(self, True, True, False)

        if self.python_script_type == PythonScriptType.INTERACTOR:
            if (update_fct := getattr(self.interactor, "update_after_favorite_read", None)):
                update_fct()

            return

        if self.palette_service:
            self.palette_service.update_palette(-1, True)


    def is_visualeditor_running(self,
                                _power_management      : bool,
                                cancel_by_menu_function: bool) -> bool:
        """ check for running visual editor

        Args:
            _power_management:       checking for power management
            cancel_by_menu_function: cancel is execute due to menu function start

        Returns:
            Visual Editor is running
        """

        if (fct := getattr(self.interactor, "is_visualeditor", None)) is None:
            self.is_cancel_by_menu_function = cancel_by_menu_function

            return False

        return fct()


    @staticmethod
    def __get_pyp_file_name(file_name: str) -> str:
        """ Get the file name of the PythonPart

        Args:
            file_name: Name of the pyp file

        Returns:
            file name of the PythonPart
        """

        #----------------- start from Allplan command line

        params = file_name.split("|")

        file_name = params[-1]

        if file_name.startswith("@"):
            sys.argv  = ["Allplan_Command_Line"] + params[:-1]

            return file_name[1:]


        #----------------- start the allep installer

        if file_name.lower().endswith(".allep"):
            sys.argv  = file_name

            return r"\AllepPlugins\Plugin Manager.pyp"

        return file_name


    def __start_next_input(self) -> bool:
        """ start the next input if multi placement is active

        Returns:
            next input is started: True/False
        """

        self.is_modified_parameter = False

        if self.is_only_update or \
           not self.create_ele_result.multi_placement or \
           not DocumentManager.get_instance().pythonpart_element.IsNull():
            return False

        self.input_mode = InputMode.RefPoint

        AllplanIFW.BuildingElementInputControls().CloseControls()

        str_tmp = self.str_table_service.get_string("e_SET_POINT_TO", "Set the to point / Angle")

        self.coord_input.InitFirstPointValueInput(AllplanIFW.InputStringConvert(str_tmp),   \
                                                  AllplanIFW.ValueInputControlData(AllplanIFW.eValueInputControlType.eANGLE_COMBOBOX,
                                                  True, False))

        if self.python_script_type == PythonScriptType.SCRIPT_OBJECT and ScriptObjectService.start_input(self) and self.palette_service:
            self.palette_service.update_palette(-1, True)

            ScriptObjectService.execute_script_object(self)

        return True


    def __get_point_from_insert_matrix(self) -> AllplanGeo.Point3D:
        """ Get input point from the insert matrix

        Returns:
            point from the insert matrix

        """
        trans_vec = self.insert_matrix.GetTranslationVector()

        return AllplanGeo.Point3D(trans_vec.X, trans_vec.Y, trans_vec.Z)


    def __switch_to_pythonpart_from_stack(self) -> bool:
        """ Switch to another PythonPart from the stack

        Returns:
            input canceled state
        """

        if self.pyp_file_stack:
            self.switch_pythonpart(self.pyp_file_stack.pop(), False)

            return False

        return True


    def switch_pythonpart(self,
                          file_name           : str,
                          add_current_to_stack: bool):
        """ Switch to another PythonPart

        Args:
            file_name:            file name of the PythonPart
            add_current_to_stack: add the current pyp file to the stack
        """

        if add_current_to_stack:
            self.pyp_file_stack.append(self.file_name)

        self.init_input_data()

        file_name = self.__get_pyp_file_name(file_name)

        result,                             \
        self.build_ele_script,              \
        self.build_ele_list,                \
        self.build_ele_ctrl_props_list,     \
        self.build_ele_composite,           \
        self.part_name,                     \
        self.file_name = self.build_ele_service.read_data_from_pyp(file_name, self.str_table_service.str_table, False, \
                                                                   self.str_table_service.material_str_table, "", True, "")

        if not result or self.build_ele_script is None:
            return

        if self.build_ele_list[0].is_interactor and self.palette_service:
            self.palette_service.close_palette()

        self.prepare_script_data([], None, False, AllplanGeo.Matrix3D(), AllplanGeo.Matrix3D())

        self.is_switch_pythonpart = True

        InputScriptCreator.execute(self)

```

</details>