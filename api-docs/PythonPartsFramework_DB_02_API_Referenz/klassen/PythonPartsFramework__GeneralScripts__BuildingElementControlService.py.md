---
title: "BuildingElementControlService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementControlService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementControlService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementControlService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the building element palette service

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `BuildingElementParameterPropertyUtil`
- `ControlProperties`
- `DocumentManager`
- `StringEvaluate`
- `re`
- `typing`

## Klassen

### `BuildingElementControlService`

Definition of class BuildingElementControlService
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `check_visible_state` | `build_ele: BuildingElement, control_props: BuildingElementControlProperties, param_dict: Dict[str, Any], value_name: str, update_ctrl_state: bool` | `None` | Check for an update of a visible state  Args:     build_ele:         Building element     control_props:     Control properties     param_dict:        Parameter dictionary     value_name:        Updated value name     update_ctrl_state: Update the control state |
| `check_enable_state` | `build_ele: BuildingElement, control_props: BuildingElementControlProperties, param_dict: Dict[str, Any], value_name: str, update_ctrl_state: bool` | `None` | Check for an update of an enable state  Args:     build_ele:         Building element     control_props:     Control properties     param_dict:        Parameter dictionary     value_name:        Updated value name     update_ctrl_state: Update the control state |
| `__check_state` | `build_ele: BuildingElement, control_props: BuildingElementControlProperties, param_dict: Dict[str, Any], value_name: str, update_ctrl_state: bool, state_name: str` | `None` | Check for an update of a control state  Args:     build_ele:         Building element     control_props:     Control properties     param_dict:        Parameter dictionary     value_name:        Updated value name     update_ctrl_state: Update the control state     state_name:        Name of the state: "visible" or "enable" |
| `add_check_state_functions` | `param_dict: Dict[str, Any], control_props: BuildingElementControlProperties` | `None` | Add internal functions for the state check to the parameter dict.  This allows to get access to the function in the <Visible> and <Enable> tag of the parameter |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the building element palette service
"""

from typing import List, Dict, Any

import re

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from StringEvaluate import StringEvaluate

import BuildingElementParameterPropertyUtil
from BuildingElementControlProperties import BuildingElementControlProperties


class BuildingElementControlService:
    """ Definition of class BuildingElementControlService
    """

    @staticmethod
    def check_visible_state(build_ele        : BuildingElement,
                            control_props    : BuildingElementControlProperties,
                            param_dict       : Dict[(str, Any)],
                            value_name       : str,
                            update_ctrl_state: bool):
        """ Check for an update of a visible state

        Args:
            build_ele:         Building element
            control_props:     Control properties
            param_dict:        Parameter dictionary
            value_name:        Updated value name
            update_ctrl_state: Update the control state
        """

        return BuildingElementControlService.__check_state(build_ele, control_props, param_dict, value_name, update_ctrl_state, "visible")


    @staticmethod
    def check_enable_state(build_ele        : BuildingElement,
                           control_props    : BuildingElementControlProperties,
                           param_dict       : Dict[(str, Any)],
                           value_name       : str,
                           update_ctrl_state: bool):
        """ Check for an update of an enable state

        Args:
            build_ele:         Building element
            control_props:     Control properties
            param_dict:        Parameter dictionary
            value_name:        Updated value name
            update_ctrl_state: Update the control state
        """

        return BuildingElementControlService.__check_state(build_ele, control_props, param_dict, value_name, update_ctrl_state, "enable")


    @staticmethod
    def __check_state(build_ele        : BuildingElement,
                      control_props    : BuildingElementControlProperties,
                      param_dict       : Dict[(str, Any)],
                      value_name       : str,
                      update_ctrl_state: bool,
                      state_name       : str):
        """ Check for an update of a control state

        Args:
            build_ele:         Building element
            control_props:     Control properties
            param_dict:        Parameter dictionary
            value_name:        Updated value name
            update_ctrl_state: Update the control state
            state_name:        Name of the state: "visible" or "enable"
        """

        if not "__StringTable" in param_dict:
            param_dict["__StringTable"] = build_ele.get_string_tables()[0]

        BuildingElementControlService.add_check_state_functions(param_dict, control_props)

        result = False

        def find_name_in_condition(condition):
            return re.compile(f'\b({value_name})\b', flags=re.IGNORECASE).search(condition) is not None


        #--------------------- check and update the visible state

        cond_name = state_name + "_condition"

        for ctrl_prop in control_props:
            if state_name == "enable" and not ctrl_prop.visible:
                continue

            condition = getattr(ctrl_prop, cond_name)

            if condition and condition.find("|") == -1:         # e.g. geometry sub parameter
                param_prop_name = BuildingElementParameterPropertyUtil.get_property_value_name(ctrl_prop.value_name)

                param_prop = build_ele.get_property(param_prop_name)

                if param_prop and param_prop.value_type.find("tuple") != -1:
                    state = [StringEvaluate.eval_condition(cond, param_dict) if cond and cond.find("$list_row") == -1 else True for cond in condition.split(",")]

                elif condition.find("$list_row") == -1:
                    if condition.find(" return ") != -1:
                        state = StringEvaluate.exec_function_string(condition, param_dict)
                    else:
                        state = StringEvaluate.eval_condition(condition, param_dict)
                else:
                    state = True

                if getattr(ctrl_prop, state_name) != state or find_name_in_condition(condition):
                    if not update_ctrl_state:
                        return True

                    result = True

                    setattr(ctrl_prop, state_name, state)

        return result


    @staticmethod
    def add_check_state_functions(param_dict   : Dict[str, Any],
                                  control_props: BuildingElementControlProperties):
        """ Add internal functions for the state check to the parameter dict.

            This allows to get access to the function in the <Visible> and <Enable> tag
            of the parameter
        """

        def __is_visible_control(ctrl_name):
            visible_ctrl_prop = next((__ctrl_prop for __ctrl_prop in control_props if __ctrl_prop.value_name == ctrl_name), None)

            return visible_ctrl_prop.visible if visible_ctrl_prop else False

        def __is_input_mode():
            return DocumentManager.get_instance().pythonpart_element.IsNull()

        param_dict["__is_visible_control"] = __is_visible_control
        param_dict["__is_input_mode"]      = __is_input_mode

```

</details>