---
title: "InputService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InputService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# InputService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InputService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the input service

## Abhängigkeiten

- `BuildingElementListService`
- `BuildingElementServices.BuildingElementModification`
- `DocumentManager`
- `HandleParameterType`
- `HandlePropertiesService`
- `InputData`
- `InputMode`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_IFW_Input`
- `PythonPartPreview`
- `PythonPartTransaction`
- `PythonScriptType`
- `ScriptObjectService`
- `ScriptService`
- `StringEvaluate`
- `TypeCollections.ElementConnectorParameterList`
- `Utilities.GeneralConstants`
- `Utils.Connections.ElementConnectionUtil`
- `Utils.Connections.PointConnectionUtil`
- `ValueTypes.ParameterPropertyValueTypes`
- `typing`
- `webbrowser`

## Klassen

### `InputService`

implementation of the input service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `modify_element_property` | `input_data: InputData, page: int, name: str, value: Any` | `None` | Modify property of element  Args:     input_data: input data     page      : the page of the property     name      : the name of the property.     value     : new value for property. |
| `create_elements_in_db` | `input_data: InputData` | `None` | Create the elements in the data base  Args:     input_data: input |
| `__create_elements_in_db` | `input_data: InputData` | `None` | create the elements in the data base  Args:     input_data: input data |
| `recalculate_and_draw_preview` | `input_data: InputData, to_screen: bool, draw_input_controls: bool, use_static_preview: bool` | `None` | recalculate and draw the preview  Args:     input_data:          input data     to_screen:           direct draw to the screen True/False     draw_input_controls: draw the input controls: True/False     use_static_preview:  use the static preview state |
| `draw_preview` | `input_data: InputData, to_screen: bool, draw_handles: bool, draw_input_controls: bool, use_static_preview: bool` | `None` | Draw the preview  Args:     input_data:          input data     to_screen:           direct draw to the screen True/False     draw_handles:        draw the handles True/False     draw_input_controls: draw the input controls: True/False     use_static_preview:  use the static preview state |
| `modify_active_page` | `input_data: InputData, name: str, value: Any` | `bool` | modify the active page  Args:     input_data: input data     name:       the name of the property.     value:      new value for property.  Returns:     modified page state |
| `open_web_browser` | `input_data: InputData, event_id: int` | `None` | open the web browser  Args:     input_data: input data     event_id:   event id of the clicked button control |
| `__execute_update_after_modification` | `input_data: InputData, update_palette: bool` | `bool` | execute the update after the modification  Args:     input_data:     input data     update_palette: update palette state  Returns:     update palette state |
| `__modify_point_distance` | `input_data: InputData, name: str, value: Any` | `bool` | check and execute the point distance modification  Args:     input_data: input data     name:       the name of the property.     value:      new value for property.  Returns:     True if the point distance was modified, otherwise False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the input service
"""

from typing import Any

import webbrowser


import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_IFW_Input as AllplanIFW

from BuildingElementListService import BuildingElementListService
from DocumentManager import DocumentManager
from HandleParameterType import HandleParameterType
from HandlePropertiesService import HandlePropertiesService
from InputMode import InputMode
from PythonPartPreview import PythonPartPreview
from PythonPartTransaction import PythonPartTransaction
from StringEvaluate import StringEvaluate

from BuildingElementServices.BuildingElementModification import BuildingElementModification

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from TypeCollections.ElementConnectorParameterList import ElementConnectorParameterList

from Utils.Connections.ElementConnectionUtil import ElementConnectionUtil
from Utils.Connections.PointConnectionUtil import PointConnectionUtil

from .InputData import InputData
from .PythonScriptType import PythonScriptType
from .ScriptObjectService import ScriptObjectService
from .ScriptService import ScriptService

class InputService():
    """ implementation of the input service
    """

    ACTIVE_PAGE_KEY     = "___ActivePage___"
    PRECAST_ELEMENT_KEY = "precastelementtypecatalogreference"
    DOM_KEY             = "___DOM___SubmitChanges___"
    MULTIMATERIAL_KEY   = "multimateriallayoutcatalogreference"

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


        #----------------- finalize the DOM input

        if input_data.palette_service is not None and name == InputService.DOM_KEY:
            input_data.palette_service.update_palette(-1, True)

            InputService.draw_preview(input_data, False, True, True, False)

            return

        if "___DOM" in name:
            value /= AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        name = name.replace("___DOM", "")


        #----------------- check for point distances

        if InputService.__modify_point_distance(input_data, name, value):
            if InputService.__execute_update_after_modification(input_data, True) and input_data.palette_service is not None:
                input_data.palette_service.update_palette(-1, False)

            return


        #----------------- modify the property in a standard PythonPart
        #                  - modify the value
        #                  - execute the modification function of the script for further checks and modifications

        if input_data.palette_service is None:
            return

        input_data.is_modified_parameter = True

        modify_service = BuildingElementModification(input_data.build_ele_list, input_data.build_ele_composite, input_data.build_ele_script,
                                                     input_data.build_ele_ctrl_props_list)

        update_palette = modify_service.modify_element_property(page, name, value, input_data.palette_service.page_building_ele,
                                                                input_data.palette_service.palette_builder, input_data.script_object)

        prop = input_data.build_ele_list[0].get_property(name)

        if prop is not None and prop.value_type.lower() in [InputService.PRECAST_ELEMENT_KEY, InputService.MULTIMATERIAL_KEY]:
            input_data.palette_service.update_palette(-1, False)

        if ScriptService.modify_control_properties(input_data, name, 0):
            update_palette = True


        #----------------- check for a palette update due to a control refresh

        if next((build_ele_ctrl_props.is_refresh_control() for build_ele_ctrl_props in input_data.build_ele_ctrl_props_list), False):
            update_palette = True


        #----------------- execute after modification

        if InputService.__execute_update_after_modification(input_data, update_palette):
            input_data.palette_service.update_palette(-1, False)


    @staticmethod
    def create_elements_in_db(input_data: InputData):
        """ Create the elements in the data base

        Args:
            input_data: input
        """

        if not input_data.is_only_update:
            input_data.handle_modi_service.stop()

        input_data.input_mode  = InputMode.WriteToDB
        input_data.expand_util = None

        if input_data.create_ele_result.elements or input_data.create_ele_result.elements_to_delete is not None:
            if input_data.is_modify_elements:
                if input_data.is_modified_parameter:
                    AllplanBaseEle.ModifyElements(input_data.coord_input.GetInputViewDocument(),
                                                  input_data.create_ele_result.elements)
                else:
                    AllplanIFW.VisibleService.ShowAllElements()
            else:
                InputService.__create_elements_in_db(input_data)

        input_data.build_ele_service.write_data_to_default_favorite_file(input_data.build_ele_list)

        input_data.is_modify_elements = False


    @staticmethod
    def __create_elements_in_db(input_data: InputData):
        """ create the elements in the data base

        Args:
            input_data: input data
        """

        doc = input_data.coord_input.GetInputViewDocument()


        #----------------- get the property connections

        create_ele_result    = input_data.create_ele_result
        connect_to_elements  = create_ele_result.connect_to_ele
        ele_connector_params = ElementConnectorParameterList()

        if any(isinstance(ele, AllplanBasisEle.MacroElement) for ele in create_ele_result.elements):
            PointConnectionUtil.add_point_connection_elements(input_data.build_ele_list, connect_to_elements)
            ElementConnectionUtil.add_geometry_element_connection_elements(input_data.build_ele_list, connect_to_elements)
        else:
            ele_connector_params = PointConnectionUtil.get_ele_connector_params(input_data.build_ele_list)


        #----------------- execute the transaction

        pyp_transaction = PythonPartTransaction(doc,
                                                connect_to_ele       = connect_to_elements,
                                                ele_connector_params = ele_connector_params)

        pyp_transaction.execute(input_data.insert_matrix,
                                input_data.coord_input.GetViewWorldProjection(),
                                create_ele_result.elements,
                                input_data.modification_ele_list,
                                create_ele_result.reinf_rearrange,
                                create_ele_result.append_reinf_pos_nr,
                                input_data.asso_ref_ele,
                                uuid_parameter_name = create_ele_result.uuid_parameter_name,
                                elements_to_delete  = create_ele_result.elements_to_delete,
                                elements_to_hide    = create_ele_result.elements_to_hide,
                                elements_to_show    = create_ele_result.elements_to_show)


    @staticmethod
    def recalculate_and_draw_preview(input_data         : InputData,
                                     to_screen          : bool,
                                     draw_input_controls: bool,
                                     use_static_preview : bool):
        """ recalculate and draw the preview

        Args:
            input_data:          input data
            to_screen:           direct draw to the screen True/False
            draw_input_controls: draw the input controls: True/False
            use_static_preview:  use the static preview state
        """

        match input_data.python_script_type:
            case PythonScriptType.SCRIPT_OBJECT:
                if input_data.script_object.script_object_interactor is not None:
                    input_data.script_object.script_object_interactor.on_preview_draw()
                    return

                if use_static_preview and input_data.create_ele_result.as_static_preview:
                    return

                ScriptObjectService.execute_script_object(input_data)

            case PythonScriptType.STANDARD:
                if not ScriptService.create_element(input_data):
                    return

        InputService.draw_preview(input_data, to_screen, True, draw_input_controls, use_static_preview)


    @staticmethod
    def draw_preview(input_data         : InputData,
                     to_screen          : bool,
                     draw_handles       : bool,
                     draw_input_controls: bool,
                     use_static_preview : bool):
        """ Draw the preview

        Args:
            input_data:          input data
            to_screen:           direct draw to the screen True/False
            draw_handles:        draw the handles True/False
            draw_input_controls: draw the input controls: True/False
            use_static_preview:  use the static preview state
        """

        if input_data.python_script_type == PythonScriptType.SCRIPT_OBJECT  and \
           input_data.script_object.script_object_interactor is not None or \
           use_static_preview and input_data.create_ele_result.as_static_preview:
            return

        input_doc = input_data.coord_input.GetInputViewDocument()
        view_proj = input_data.coord_input.GetViewWorldProjection()

        if input_data.input_mode == InputMode.RefPoint:
            input_data.last_input_doc = input_doc
            input_data.last_view_proj = view_proj
        else:
            if input_doc.GetDocumentID() == input_data.last_input_doc.GetDocumentID():
                input_data.last_view_proj = view_proj

            input_doc = input_data.last_input_doc
            view_proj = input_data.last_view_proj


        #----------------- Draw the handles

        if draw_handles and input_data.input_mode == InputMode.HandleSelect:
            input_data.handle_modi_service.start(input_data.create_ele_result.handles, input_data.insert_matrix,
                                                 input_doc, view_proj, draw_input_controls)

        if input_data.create_ele_result.preview_symbols is not None:
            input_data.create_ele_result.preview_symbols.draw(input_data.insert_matrix,
                                                              input_data.coord_input.GetViewWorldProjection(),
                                                              not input_data.modification_ele_list.is_modification_element())


        #----------------- Draw the element preview

        PythonPartPreview.execute(input_doc,
                                  input_data.insert_matrix,
                                  input_data.create_ele_result.preview_elements,
                                  not input_data.create_ele_result.elements, input_data.asso_ref_ele,
                                  not input_data.modification_ele_list.is_modification_element(),
                                  input_data.create_ele_result.as_static_preview)

        PythonPartPreview.execute(input_doc,
                                  input_data.insert_matrix,
                                  input_data.create_ele_result.elements,
                                  to_screen, input_data.asso_ref_ele,
                                  not input_data.modification_ele_list.is_modification_element(),
                                  input_data.create_ele_result.as_static_preview,
                                  input_data.create_ele_result.elements_to_hide,
                                  input_data.create_ele_result.elements_to_show,
                                  input_data.create_ele_result.hidden_preview_elements,
                                  input_data.create_ele_result.visible_preview_elements)

    @staticmethod
    def modify_active_page(input_data: InputData,
                           name      : str,
                           value     : Any) -> bool:
        """ modify the active page

        Args:
            input_data: input data
            name:       the name of the property.
            value:      new value for property.

        Returns:
            modified page state
        """

        if name != InputService.ACTIVE_PAGE_KEY:
            return False

        set_page_index = getattr(input_data.interactor, "set_active_palette_page_index", None) \
                            if input_data.python_script_type == PythonScriptType.INTERACTOR else \
                         getattr(input_data.build_ele_script, "set_active_palette_page_index", None)

        if set_page_index:
            set_page_index(value)

        input_data.active_page = value

        return True


    @staticmethod
    def open_web_browser(input_data: InputData,
                         event_id  : int):
        """ open the web browser

        Args:
            input_data: input data
            event_id:   event id of the clicked button control
        """

        str_event_id = str(event_id)

        for ctrl_props, build_ele in zip(input_data.build_ele_ctrl_props_list, input_data.build_ele_list):
            param_dict = StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_local_string_table())

            for ctrl_prop in ctrl_props:
                prop = build_ele.get_property(ctrl_prop.value_name)

                if prop is None or prop.value_type not in {ParameterPropertyValueTypes.BUTTON,
                                                           ParameterPropertyValueTypes.PICTURE_BUTTON,
                                                           ParameterPropertyValueTypes.PICTURE_RESOURCE_BUTTON}:
                    continue

                prop_event_id = StringEvaluate.eval_constants(ctrl_prop.event_id, param_dict)

                if prop_event_id == str_event_id and ctrl_prop.value_list_2.startswith("http"):
                    webbrowser.open(ctrl_prop.value_list_2)

                    return


    @staticmethod
    def __execute_update_after_modification(input_data    : InputData,
                                            update_palette: bool) -> bool:
        """ execute the update after the modification

        Args:
            input_data:     input data
            update_palette: update palette state

        Returns:
            update palette state
        """

        #------------- palette update is needed for changed parameter values as result of a
        #              new PythonPart creation in draw_preview

        param_list = list[str]()

        if not update_palette:
            param_list = BuildingElementListService.get_params_list(input_data.build_ele_list)

        InputService.recalculate_and_draw_preview(input_data, True, True, False)

        if not update_palette:
            update_palette = param_list != BuildingElementListService.get_params_list(input_data.build_ele_list)

        return update_palette


    @staticmethod
    def __modify_point_distance(input_data: InputData,
                                name      : str,
                                value     : Any) -> bool:
        """ check and execute the point distance modification

        Args:
            input_data: input data
            name:       the name of the property.
            value:      new value for property.

        Returns:
            True if the point distance was modified, otherwise False
        """

        for handle_prop in input_data.create_ele_result.handles:
            for handle_param in handle_prop.parameter_data:
                if name == handle_param.param_prop_name and \
                   handle_param.param_type in {HandleParameterType.X_POINT_DISTANCE,
                                               HandleParameterType.Y_POINT_DISTANCE,
                                               HandleParameterType.Z_POINT_DISTANCE,
                                               HandleParameterType.LENGTH_POINT_DISTANCE}:
                    input_data.is_modified_parameter = True

                    HandlePropertiesService.update_point(handle_prop, name, value)

                    return True

        return False

```

</details>