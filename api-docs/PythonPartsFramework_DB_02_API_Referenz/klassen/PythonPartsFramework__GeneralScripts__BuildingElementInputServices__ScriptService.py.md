---
title: "ScriptService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\ScriptService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# ScriptService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\ScriptService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the script service

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementComposite`
- `BuildingElementControlProperties`
- `ControlPropertiesUtil`
- `CreateElementResult`
- `HandleParameterType`
- `HandleProperties`
- `HandlePropertiesService`
- `InputData`
- `NemAll_Python_Geometry`
- `NemAll_Python_Utility`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `traceback`
- `typing`

## Klassen

### `ScriptService`

implementation of the script service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `initialize_control_properties` | `input_data: InputData` | `bool` | initialize the control properties  Args:     input_data: input data  Returns:     successfully executed state |
| `create_element` | `input_data: InputData, warn_missing_function: bool=False` | `bool` | create the element  Args:     input_data:             input data     warn_missing_function:  show a warning in the trace window of the function is not implemented  Returns:     element is created: True/False |
| `modify_element_property` | `name: str, value: Any, prop: ParameterProperty | None, build_ele_index: int, build_ele_script: Any, build_ele_list: list[BuildingElement], build_ele_ctrl_props_list: list[BuildingElementControlProperties], build_ele_composite: BuildingElementComposite` | `bool` | Modify property of element  Args:     name:                      the name of the property.     value:                     new value for property.     prop:                      property     build_ele_index:           index of the building element     build_ele_script:          building element script     build_ele_list:            list with the building elements     build_ele_ctrl_props_list: list with the building element control properties     build_ele_composite:       building element composite with the building element constraints  Returns:     update palette state |
| `move_handle` | `input_data: InputData, input_pnt: AllplanGeo.Point3D` | `bool` | Move a handle  Args:     input_data: input data     input_pnt:  input point  Returns:     Handle is moved: True/False |
| `set_element_result_data` | `input_data: InputData, create_ele_result: CreateElementResult | None` | `None` | modify the control properties  Args:     input_data:        input data     create_ele_result: created element result data |
| `update_palette` | `input_data: InputData, handle_prop: HandleProperties` | `None` | modify the control properties  Args:     input_data:  input data     handle_prop: handle properties |
| `modify_control_properties` | `input_data: InputData, name: str, event_id: int` | `bool` | modify the control properties  Args:     input_data: input data     name:       name of the modified value     event_id:   event ID in case of button click  Returns:     update of the property palette is necessary |
| `trace_call_stack` | `input_data: InputData, fct_name: str` | `bool` | trace the call stack  Args:     input_data: input data     fct_name:   function name  Returns:     False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""implementation of the script service
"""

# pylint: disable=bare-except

from typing import Any

import traceback

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Utility as AllplanUtil

from BuildingElement import BuildingElement
from BuildingElementComposite import BuildingElementComposite
from BuildingElementControlProperties import BuildingElementControlProperties
from ControlPropertiesUtil import ControlPropertiesUtil
from CreateElementResult import CreateElementResult
from HandleParameterType import HandleParameterType
from HandleProperties import HandleProperties
from HandlePropertiesService import HandlePropertiesService
from ParameterProperty import ParameterProperty

from Utilities.GeneralConstants import GeneralConstants

from .InputData import InputData

class ScriptService():
    """ implementation of the script service
    """


    @staticmethod
    def initialize_control_properties(input_data: InputData) -> bool:
        """ initialize the control properties

        Args:
            input_data: input data

        Returns:
            successfully executed state
        """

        if getattr(input_data.build_ele_script, "initialize_control_properties", None) is None:
            return True

        ctrl_prop_util = ControlPropertiesUtil(input_data.build_ele_ctrl_props_list, input_data.build_ele_list)


        #----------------- call for single building element

        if len(input_data.build_ele_list) == 1:
            try:
                input_data.build_ele_script.initialize_control_properties(input_data.build_ele_list[0], ctrl_prop_util,
                                                                          input_data.last_input_doc)

            except:
                traceback.print_exc()

                return False

            return True


        #----------------- call for a list of building elements

        try:
            input_data.build_ele_script.initialize_control_properties(input_data.build_ele_list, ctrl_prop_util,
                                                                      input_data.last_input_doc)

        except:
            traceback.print_exc()

            return False

        return True


    @staticmethod
    def create_element(input_data           : InputData,
                       warn_missing_function: bool = False) -> bool:
        """ create the element

        Args:
            input_data:             input data
            warn_missing_function:  show a warning in the trace window of the function is not implemented

        Returns:
            element is created: True/False
        """

        if (create_element := getattr(input_data.build_ele_script, "create_element", None)) is None:
            if not warn_missing_function:
                return True

            print()
            print("===========================================================================")
            print()
            print(f"Attention: function 'create_element' is not implemented in {input_data.build_ele_list[0].script_name}!!!")
            print()
            print("===========================================================================")
            print()

            return True


        #-----------------execute the function

        if len(input_data.build_ele_list) == 1:
            try:
                create_ele_result = create_element(input_data.build_ele_list[0], input_data.last_input_doc)

            except:
                return ScriptService.trace_call_stack(input_data, "create_element")

        elif input_data.build_ele_composite:
            input_data.build_ele_composite.connect_building_element_values(input_data.build_ele_list)

            try:
                create_ele_result = create_element(input_data.build_ele_list,
                                                   input_data.build_ele_composite,
                                                   input_data.last_input_doc)

            except:
                return ScriptService.trace_call_stack(input_data, "create_element")

        if create_ele_result is None:
            return False

        ScriptService.set_element_result_data(input_data, create_ele_result)

        return True


    @staticmethod
    def modify_element_property(name                     : str,
                                value                    : Any,
                                prop                     : (ParameterProperty | None),
                                build_ele_index          : int,
                                build_ele_script         : Any,
                                build_ele_list           : list[BuildingElement],
                                build_ele_ctrl_props_list: list[BuildingElementControlProperties],
                                build_ele_composite      : BuildingElementComposite) -> bool:
        """ Modify property of element

        Args:
            name:                      the name of the property.
            value:                     new value for property.
            prop:                      property
            build_ele_index:           index of the building element
            build_ele_script:          building element script
            build_ele_list:            list with the building elements
            build_ele_ctrl_props_list: list with the building element control properties
            build_ele_composite:       building element composite with the building element constraints

        Returns:
            update palette state
        """

        if (modify_prop := getattr(build_ele_script, "modify_element_property", None)) is None:
            return False

        build_ele            = build_ele_list[build_ele_index]
        build_ele_ctrl_props = build_ele_ctrl_props_list[build_ele_index]


        #--------- use the input value from the dialog input

        if prop:
            ctrl_prop = build_ele_ctrl_props.get_property(name)

            if ctrl_prop and ctrl_prop.value_dialog:
                value = prop.value


        #--------- modify the value

        result = modify_prop(build_ele, name, value) if len(build_ele_list) == 1 else \
                 modify_prop(build_ele_list, build_ele_composite, name, value, build_ele_index)

        return False if result is None else result


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


        #----------------- in case of missing implementation execute default

        if (move_handle := getattr(input_data.build_ele_script, "move_handle", None)) is None:
            HandlePropertiesService.update_property_value(input_data.build_ele_list[0], handle_prop, input_pnt)

            if (created := ScriptService.create_element(input_data)):
                ScriptService.update_palette(input_data, handle_prop)

            return created


        #----------------- modify the handle

        if len(input_data.build_ele_list) == 1:
            try:
                handle_result = move_handle(input_data.build_ele_list[0], handle_prop,         \
                                            local_pnt, input_data.last_input_doc)
            except:
                return ScriptService.trace_call_stack(input_data, "move_handle")
        else:
            try:
                handle_result = move_handle(input_data.build_ele_list, input_data.build_ele_composite, \
                                            handle_prop, local_pnt, input_data.last_input_doc)
            except:
                return ScriptService.trace_call_stack(input_data, "move_handle")

        ScriptService.set_element_result_data(input_data, handle_result)

        ScriptService.update_palette(input_data, handle_prop)

        return True


    @staticmethod
    def set_element_result_data(input_data       : InputData,
                                create_ele_result: (CreateElementResult | None)):
        """ modify the control properties

        Args:
            input_data:        input data
            create_ele_result: created element result data
        """

        if create_ele_result is None:
            return


        #----------------- get the data for the created element

        if isinstance(create_ele_result, (list, tuple)):
            input_data.create_ele_result = CreateElementResult(*create_ele_result)
        else:
            input_data.create_ele_result = create_ele_result

            if input_data.create_ele_result.placement_point:
                pnt = AllplanGeo.Point3D(input_data.create_ele_result.placement_point)

                input_data.set_insert_matrix_from_point(pnt)


    @staticmethod
    def update_palette(input_data : InputData,
                       handle_prop: HandleProperties):
        """ modify the control properties

        Args:
            input_data:  input data
            handle_prop: handle properties
        """

        update_palette = ScriptService.modify_control_properties(input_data, ",".join(handle_prop.get_parameter_names()), 0)

        for param_data in handle_prop.parameter_data:
            if param_data.param_type in [HandleParameterType.CHECK_BOX,
                                         HandleParameterType.INCREMENT_BUTTON,
                                         HandleParameterType.DECREMENT_BUTTON]:
                update_palette = True

                break

        if update_palette and input_data.palette_service:
            input_data.palette_service.update_palette(-1, True)


    @staticmethod
    def modify_control_properties(input_data: InputData,
                                  name      : str,
                                  event_id  : int) -> bool:
        """ modify the control properties

        Args:
            input_data: input data
            name:       name of the modified value
            event_id:   event ID in case of button click

        Returns:
            update of the property palette is necessary
        """

        if getattr(input_data.build_ele_script, "modify_control_properties", None) is None:
            return False

        name = name.removesuffix(GeneralConstants.DIALOG_BUTTON_KEY)

        if len(input_data.build_ele_list) == 1:
            try:
                return input_data.build_ele_script.modify_control_properties(input_data.build_ele_list[0],
                                                                             ControlPropertiesUtil(input_data.build_ele_ctrl_props_list,
                                                                                                   input_data.build_ele_list),
                                                                             name, event_id, input_data.last_input_doc)
            except:
                return ScriptService.trace_call_stack(input_data, "modify_control_properties")

        try:
            return input_data.build_ele_script.modify_control_properties(input_data.build_ele_list,
                                                                         ControlPropertiesUtil(input_data.build_ele_ctrl_props_list,
                                                                                               input_data.build_ele_list),
                                                                         name, event_id, input_data.last_input_doc)
        except:
            return ScriptService.trace_call_stack(input_data, "modify_control_properties")


    @staticmethod
    def trace_call_stack(input_data: InputData,
                         fct_name  : str) -> bool:
        """ trace the call stack

        Args:
            input_data: input data
            fct_name:   function name

        Returns:
            False
        """

        traceback.print_exc()

        AllplanUtil.ShowMessageBox(f"Exception occurred during {fct_name} in script {input_data.build_ele_list[0].script_name}" \
                                   f"---> please have a look at the trace window",
                                   AllplanUtil.MB_OK)

        return False

```

</details>