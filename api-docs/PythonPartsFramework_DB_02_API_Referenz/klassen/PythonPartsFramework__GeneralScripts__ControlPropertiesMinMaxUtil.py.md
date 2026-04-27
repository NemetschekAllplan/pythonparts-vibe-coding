---
title: "ControlPropertiesMinMaxUtil"
source: "PythonPartsFramework\GeneralScripts\ControlPropertiesMinMaxUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ControlPropertiesMinMaxUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ControlPropertiesMinMaxUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

Implementation of the utilities for the control properties min/max value

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `BuildingElementStringTable`
- `ControlProperties`
- `ParameterProperty`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `ValueTypes.MultiIndex`
- `ValueTypes.MultiIndexImpl`
- `ValueTypes.ParameterPropertyValueTypes`
- `typing`

## Klassen

### `ControlPropertiesMinMaxUtil`

Implementation of the utilities for the control properties min/max value 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `validate_value` | `ctrl_prop: ControlProperties, prop: ParameterProperty, value: Any, name: str, parameter_dict: dict[str, Any]` | `Any` | check and adapt the value accordingly to the min/max value  Args:     ctrl_prop     : control property     prop          : parameter property     value         : value to test     name          : name of the value, including the name of the sub value (tuple field name, geometry .X, ...)     parameter_dict: parameter dictionary for the range command  Returns:     value, adapted to the min/max value |
| `check_min_max_value` | `build_ele: BuildingElement, control_props: BuildingElementControlProperties, parameter_dict: dict[str, Any], global_str_table: BuildingElementStringTable` | `bool` | Check the value range and value of all parameters.  This is necessary if the value of a parameter used in a min/max value condition changes.  Args:     build_ele:        building element with the parameter properties     control_props:    Control properties     parameter_dict:   Parameter dictionary     global_str_table: global string table  Returns:     a value is adapted to the min or max value: True/False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the utilities for the control properties min/max value
"""

from typing import Any

from BuildingElementControlProperties import BuildingElementControlProperties
from ControlProperties import ControlProperties
from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.MultiIndex import MultiIndex
from ValueTypes.MultiIndexImpl import MultiIndexImpl
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

class ControlPropertiesMinMaxUtil():
    """ Implementation of the utilities for the control properties min/max value """

    @staticmethod
    def validate_value(ctrl_prop     : ControlProperties,
                       prop          : ParameterProperty,
                       value         : Any,
                       name          : str,
                       parameter_dict: dict[str, Any]) -> Any:
        """ check and adapt the value accordingly to the min/max value

        Args:
            ctrl_prop     : control property
            prop          : parameter property
            value         : value to test
            name          : name of the value, including the name of the sub value (tuple field name, geometry .X, ...)
            parameter_dict: parameter dictionary for the range command

        Returns:
            value, adapted to the min/max value
        """

        parameter_dict |= StringEvaluate.get_allplan_geometry_dict()


        #----------------- test min value

        min_value_res = prop.value_type.validate_minimal_value(ctrl_prop, parameter_dict)

        has_min_cond, _ = min_value_res.get_min_value_state()

        if has_min_cond and (min_value := min_value_res.get_value(prop, name)) is not None:
            if prop.value_type == ParameterPropertyValueTypes.MULTIINDEX:
                _, new_value = MultiIndexImpl.test_and_update_for_min_value(MultiIndex(value), min_value)

                value = new_value.get_indexes(False)
            else:
                if GeneralConstants.SUB_NAME_SEPARATOR in name:
                    min_value = getattr(min_value, name.split(GeneralConstants.SUB_NAME_SEPARATOR)[-1])

                if isinstance(value, str):
                    value = prop.value_type.string_to_unit_value(value)

                value = max(value, min_value)


        #----------------- test max value

        max_value_res = prop.value_type.validate_maximal_value(ctrl_prop, parameter_dict)

        has_max_cond, _ = max_value_res.get_max_value_state()

        if has_max_cond and (max_value := max_value_res.get_value(prop, name)) is not None:
            if prop.value_type == ParameterPropertyValueTypes.MULTIINDEX:
                _, new_value = MultiIndexImpl.test_and_update_for_max_value(MultiIndex(value), max_value)

                value = new_value.get_indexes(False)
            else:
                if GeneralConstants.SUB_NAME_SEPARATOR in name:
                    max_value = getattr(max_value, name.split(GeneralConstants.SUB_NAME_SEPARATOR)[-1])

                if isinstance(value, str):
                    value = prop.value_type.string_to_unit_value(value)

                value = min(value, max_value)

        return value


    @staticmethod
    def check_min_max_value(build_ele       : BuildingElement,
                            control_props   : BuildingElementControlProperties,
                            parameter_dict  : dict[str, Any],
                            global_str_table: BuildingElementStringTable) -> bool:
        """ Check the value range and value of all parameters.

        This is necessary if the value of a parameter used
        in a min/max value condition changes.

        Args:
            build_ele:        building element with the parameter properties
            control_props:    Control properties
            parameter_dict:   Parameter dictionary
            global_str_table: global string table

        Returns:
            a value is adapted to the min or max value: True/False
        """

        is_update = False

        parameter_dict |= StringEvaluate.get_allplan_geometry_dict()

        for ctrl_prop in control_props:
            if (prop := build_ele.get_property(ctrl_prop.value_name)) is None:
                continue


            #----------------- check the minimal and maximal value

            min_value_res = prop.value_type.validate_minimal_value(ctrl_prop, parameter_dict)
            max_value_res = prop.value_type.validate_maximal_value(ctrl_prop, parameter_dict)

            has_min_cond, is_update_min = min_value_res.get_min_value_state()
            has_max_cond, is_update_max = max_value_res.get_max_value_state()

            if not has_min_cond and not has_max_cond:
                continue

            is_update = is_update or is_update_min is True or is_update_max is True

            if has_min_cond:
                is_update |= prop.value_type.validate_for_min_value(prop, ctrl_prop, min_value_res, global_str_table)

            if has_max_cond:
                is_update |= prop.value_type.validate_for_max_value(prop, ctrl_prop, max_value_res, global_str_table)

        return is_update

```

</details>