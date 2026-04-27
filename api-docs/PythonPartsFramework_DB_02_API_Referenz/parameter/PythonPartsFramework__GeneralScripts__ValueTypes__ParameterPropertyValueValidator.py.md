---
title: "ParameterPropertyValueValidator"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ParameterPropertyValueValidator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ParameterPropertyValueValidator

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ParameterPropertyValueValidator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `werte`

## Übersicht

implementation of the parameter property value validator

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypes.ValueTypeUtils.MinMaxValidator`
- `ValueTypes.ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `struct`
- `typing`

## Klassen

### `ParameterPropertyValueValidator`

implementation of the parameter property value validator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `validate_minimal_value` | `ctrl_prop: ControlProperties, parameter_dict: dict[str, Any]` | `ValidateMinValueResult` | validate, whether the minimal value of the control property has changed  Args:     ctrl_prop:      control property     parameter_dict: parameter dictionary for the range command  Returns:     min value validation result |
| `validate_maximal_value` | `ctrl_prop: ControlProperties, parameter_dict: dict[str, Any]` | `ValidateMaxValueResult` | validate, whether the maximal value of the control property has changed  Args:     ctrl_prop:      control property     parameter_dict: parameter dictionary for the range command  Returns:     min value validation result |
| `validate_for_list_value` | `value: float | int | str, _value_type: str, _value_list: str, _parameter_dict: dict[str, Any]` | `tuple[bool, float | int | str]` | test for an existing float value in the list  Args:     value:           value to test     _value_type:     value type     _value_list:     value list as pipe separated string or range command     _parameter_dict: parameter dictionary for the range command  Returns:     (value was updated, value if present in the list or nearest value from the list) |
| `validate_for_min_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, min_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the minimal value  Args:     prop:             property     ctrl_prop:        control properties     min_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `validate_for_max_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, max_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the maximal value  Args:     prop:             property     ctrl_prop:        control properties     max_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `get_min_value` | `-` | `int` | get the minimal value  Returns:     get the minimal value |
| `get_max_value` | `-` | `int` | get the maximal value  Returns:     get the maximal value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the parameter property value validator
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import struct

from StringEvaluate import StringEvaluate

import ValueTypes.ValueTypeUtils.MinMaxValidator

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from BuildingElementStringTable import BuildingElementStringTable
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty

    from ValueTypes.ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ParameterPropertyValueValidator():
    """ implementation of the parameter property value validator
    """

    class ValidateMinValueResult():
        """ result of the min value validation
        """

        def __init__(self,
                     ctrl_prop     : ControlProperties,
                     parameter_dict: dict[str, Any]):
            """ initialize

            Args:
                ctrl_prop:      control properties
                parameter_dict: parameter dictionary for the range command
            """

            self.has_minimal_cond = False
            self.value_changed    = False


            #------------- use the default min value

            if not (min_value_condition := ctrl_prop.min_value_condition):
                self.min_value = ctrl_prop.min_value

                return


            #-------------- check for a new min value

            self.min_value = StringEvaluate.eval(min_value_condition, parameter_dict)

            self.has_minimal_cond = True

            if self.min_value == "":
                self.has_minimal_cond = False
                self.value_changed    = False
                self.min_value        = ctrl_prop.min_value

            elif self.min_value != ctrl_prop.min_value:
                ctrl_prop.min_value   = self.min_value
                self.value_changed    = True


        def get_min_value_state(self) -> tuple[bool, bool]:
            """ get the min value state

            Returns:
                has minimal condition, minimal value changed
            """

            return self.has_minimal_cond, self.value_changed


        def get_value(self,
                      _prop: ParameterProperty,
                      _name: str) -> Any:
            """ get the value

            Args:
                _prop: property
                _name: name of the value, including the name of the sub value (tuple field name, geometry .X, ...)

            Returns:
                value
            """

            return self.min_value


    class ValidateMaxValueResult():
        """ result of the max value validation
        """

        def __init__(self,
                     ctrl_prop     : ControlProperties,
                     parameter_dict: dict[str, Any]):
            """ initialize

            Args:
                ctrl_prop:      control properties
                parameter_dict: parameter dictionary for the range command
            """

            self.has_maximal_cond = False
            self.value_changed    = False


            #------------- use the default max value

            if not (max_value_condition := ctrl_prop.max_value_condition):
                self.max_value = ctrl_prop.max_value

                return


            #------------- check for a new max value

            self.max_value = StringEvaluate.eval(max_value_condition, parameter_dict)

            self.has_maximal_cond = True

            if self.max_value == "":
                self.has_maximal_cond = False
                self.value_changed    = False
                self.max_value        = ctrl_prop.max_value

            elif self.max_value != ctrl_prop.max_value:
                ctrl_prop.max_value   = self.max_value
                self.value_changed    = True


        def get_max_value_state(self) -> tuple[bool, bool]:
            """ get the max value state

            Returns:
                has maximal condition, maximal value changed
            """

            return self.has_maximal_cond, self.value_changed


        def get_value(self,
                      _prop: ParameterProperty,
                      _name: str) -> Any:
            """ get the value

            Args:
                _prop: property
                _name: name of the value, including the name of the sub value (tuple field name, geometry .X, ...)

            Returns:
                value
            """

            return self.max_value


    @staticmethod
    def validate_minimal_value(ctrl_prop     : ControlProperties,
                               parameter_dict: dict[str, Any]) -> ValidateMinValueResult:
        """ validate, whether the minimal value of the control property has changed

        Args:
            ctrl_prop:      control property
            parameter_dict: parameter dictionary for the range command

        Returns:
            min value validation result
        """

        return ParameterPropertyValueValidator.ValidateMinValueResult(ctrl_prop, parameter_dict)


    @staticmethod
    def validate_maximal_value(ctrl_prop     : ControlProperties,
                               parameter_dict: dict[str, Any]) -> ValidateMaxValueResult:
        """ validate, whether the maximal value of the control property has changed

        Args:
            ctrl_prop:      control property
            parameter_dict: parameter dictionary for the range command

        Returns:
            min value validation result
        """

        return ParameterPropertyValueValidator.ValidateMaxValueResult(ctrl_prop, parameter_dict)


    @staticmethod
    def validate_for_list_value(value          : (float | int | str),
                                _value_type    : str,
                                _value_list    : str,
                                _parameter_dict: dict[str, Any]) -> tuple[bool, (float | int | str)]:
        """ test for an existing float value in the list

        Args:
            value:           value to test
            _value_type:     value type
            _value_list:     value list as pipe separated string or range command
            _parameter_dict: parameter dictionary for the range command

        Returns:
            (value was updated, value if present in the list or nearest value from the list)
        """

        return False, value


    @staticmethod
    def validate_for_min_value(prop            : ParameterProperty,
                               ctrl_prop       : ControlProperties,
                               min_value       : Any,
                               global_str_table: BuildingElementStringTable) -> bool:
        """ validate for the minimal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            min_value:        min value
            global_str_table: global string table

        Returns:
            palette update state
        """

        def test_min(value    : Any,
                     min_value: Any) -> tuple[bool, Any]:
            """ test for the min value

            Args:
                value:     value
                min_value: min value

            Returns:
                min value assigned state, min value
            """

            return (True, min_value) if value < min_value else (False, value)

        return ValueTypes.ValueTypeUtils.MinMaxValidator.MinMaxValidator.validate_for_min_value(prop, ctrl_prop, min_value,
                                                                                                global_str_table, test_min)


    @staticmethod
    def validate_for_max_value(prop            : ParameterProperty,
                               ctrl_prop       : ControlProperties,
                               max_value       : Any,
                               global_str_table: BuildingElementStringTable) -> bool:
        """ validate for the maximal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            max_value:        min value
            global_str_table: global string table

        Returns:
            palette update state
        """

        def test_max(value    : Any,
                     max_value: Any) -> tuple[bool, Any]:
            """ test for the max value

            Args:
                value:     value
                max_value: max value

            Returns:
                max value assigned state, max value
            """

            return (True, max_value) if value > max_value else (False, value)

        return ValueTypes.ValueTypeUtils.MinMaxValidator.MinMaxValidator.validate_for_max_value(prop, ctrl_prop, max_value,
                                                                                                global_str_table, test_max)


    @staticmethod
    def get_min_value() -> int:
        """ get the minimal value

        Returns:
            get the minimal value
        """

        return - 2 ** (struct.Struct('i').size * 8 - 1)


    @staticmethod
    def get_max_value() -> int:
        """ get the maximal value

        Returns:
            get the maximal value
        """

        return 2 ** (struct.Struct('i').size * 8 - 1) - 1

```

</details>