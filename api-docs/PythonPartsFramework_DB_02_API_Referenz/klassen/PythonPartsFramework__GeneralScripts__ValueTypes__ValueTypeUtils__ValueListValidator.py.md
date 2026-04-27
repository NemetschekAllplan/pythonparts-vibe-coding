---
title: "ValueListValidator"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ValueListValidator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ValueListValidator

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ValueListValidator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

Implementation of the utilities for the control properties value list

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `ControlProperties`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `__future__`
- `collections.abc`
- `typing`

## Klassen

### `ValueListValidator`

Implementation of the utilities for the control properties value list
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `validate_list` | `values: list[ConvTypeVar], value_type: ParameterPropertyValueType, value_list: str, parameter_dict: dict[str, Any]` | `tuple[bool, list[ConvTypeVar]]` | validate the values in a list  Args:     values:         values     value_type:     value_type     value_list:     value list as pipe separated string or range command     parameter_dict: parameter dictionary for the range command  Returns:     returns update state, updated values |
| `validate_numeric_value` | `value: NumericConvTypeVar, value_type: ParameterPropertyValueType, value_list: str, converter: Callable[[str | int | float], NumericConvTypeVar], parameter_dict: dict[str, Any]` | `tuple[bool, NumericConvTypeVar]` | validate float and integer value  Args:     value:          value to test     value_type:     value type     value_list:     value list as pipe separated string or range command     converter:      value converter     parameter_dict: parameter dictionary for the range command  Returns:     (value was updated, value if present in the list or nearest value from the list) |
| `eval_value_list_formula` | `value_list: str, value: str, parameter_dict: dict[str, Any]` | `tuple[str, str]` | evaluate the value list formula and get the current value list  Args:     value_list:     value list as pipe separated string or range command     value:          new value     parameter_dict: parameter dictionary for the range command  Returns:     current value list |
| `get_list_from_value_list` | `value_list: str, value_type: str, converter: Callable[[str | int | float], ConvTypeVar], parameter_dict: dict[str, Any]` | `list[ConvTypeVar]` | convert the value list string to a list of values  Args:     value_list:     value list as pipe separated string or range command     value_type:     value type     converter:      converter function for the result type     parameter_dict: parameter dictionary for the range command  Returns:     list[Any]: converted values |
| `__list_from_range_string` | `range_string: str, value_type: str, converter: Callable[[str | int | float], ConvTypeVar], parameter_dict: dict[str, Any]` | `list[ConvTypeVar]` | create a value list from a range loop string  Args:     range_string:   range command string     value_type:     value_type     converter:      converter function for the result type     parameter_dict: parameter dictionary for the range command  Returns:     converted values |
| `get_value_by_text_id` | `ctrl_prop: ControlProperties, text_id: str` | `str | None` | Gets value from list of possible control values e.g. combo box, by text_id.  Args:     ctrl_prop: control properties     text_id:   text ID  Returns:     The value or None if there is no corresponding value. |
| `check_length` | `*value_lists` | `None` | Checks, whether the given value lists all contain the same number of entries separated with '|'  Args:     value_lists: value lists to check  Raises:     ValueError: when given value lists contain different number of entries  Examples:     >>> ValueListValidator.check_length("one|two|three", "four|five|six")     >>> ValueListValidator.check_length("one|two|three", "four|five")     ValueError: The value lists contain different number of entries. ... |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the utilities for the control properties value list
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import TYPE_CHECKING, Any, TypeVar

from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate
from Utilities.GeneralConstants import GeneralConstants

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from BuildingElementControlProperties import BuildingElementControlProperties
    from ParameterProperty import ParameterProperty

    from ..ParameterPropertyValueType import ParameterPropertyValueType

ConvTypeVar = TypeVar("ConvTypeVar", bound = float | int | str)

NumericConvTypeVar = TypeVar("NumericConvTypeVar", bound = float | int)

class ValueListValidator():
    """ Implementation of the utilities for the control properties value list
    """

    @staticmethod
    def validate_list(values        : list[ConvTypeVar],
                      value_type    : ParameterPropertyValueType,
                      value_list    : str,
                      parameter_dict: dict[str, Any]) -> tuple[bool, list[ConvTypeVar]]:
        """ validate the values in a list

        Args:
            values:         values
            value_type:     value_type
            value_list:     value list as pipe separated string or range command
            parameter_dict: parameter dictionary for the range command

        Returns:
            returns update state, updated values
        """

        is_update = False

        updated_values = []

        for value_item in values:
            if isinstance(value_item, list):
                update, upd_value = ValueListValidator.validate_list(value_item, value_type, value_list, parameter_dict)
            else:
                update, upd_value = value_type.validate_for_list_value(value_item, value_type,
                                                                       value_list, parameter_dict)

            is_update = is_update or update

            updated_values.append(upd_value)

        return is_update, updated_values


    @staticmethod
    def validate_numeric_value(value         : NumericConvTypeVar,
                               value_type    : ParameterPropertyValueType,
                               value_list    : str,
                               converter     : Callable[[(str | int | float)], NumericConvTypeVar],
                               parameter_dict: dict[str, Any]) -> tuple[bool, NumericConvTypeVar]:
        """ validate float and integer value

        Args:
            value:          value to test
            value_type:     value type
            value_list:     value list as pipe separated string or range command
            converter:      value converter
            parameter_dict: parameter dictionary for the range command

        Returns:
            (value was updated, value if present in the list or nearest value from the list)
        """

        values = ValueListValidator.get_list_from_value_list(value_list, value_type, converter, parameter_dict)

        if not values or value in values: #if value list is empty, return input value
            return False, value

        min_dist  = 1.0e10 if converter == float else 32000
        new_value = converter(0)

        for num_value in values:
            if (dist := abs(num_value - value)) < min_dist:
                min_dist  = dist
                new_value = num_value

        return True, new_value


    @staticmethod
    def eval_value_list_formula(value_list    : str,
                                value         : str,
                                parameter_dict: dict[str, Any]) -> tuple[str, str]:
        """ evaluate the value list formula and get the current value list

        Args:
            value_list:     value list as pipe separated string or range command
            value:          new value
            parameter_dict: parameter dictionary for the range command

        Returns:
            current value list
        """

        if GeneralConstants.LIST_SEPARATOR_START not in value_list and not StringEvaluate.is_python_script(value_list) and \
           value_list.find("\"") == -1 and GeneralConstants.TEXT_SEPARATOR in value_list:
            return value, value_list

        value_list_list = ValueListValidator.get_list_from_value_list(value_list, "string", str, parameter_dict)

        if value_list_list and value not in value_list_list:
            value = value_list_list[0]

        return value, GeneralConstants.TEXT_SEPARATOR.join(value_list_list)


    @staticmethod
    def get_list_from_value_list(value_list    : str,
                                 value_type    : str,
                                 converter     : Callable[[(str | int | float)], ConvTypeVar],
                                 parameter_dict: dict[str, Any]) -> list[ConvTypeVar]:
        """ convert the value list string to a list of values

        Args:
            value_list:     value list as pipe separated string or range command
            value_type:     value type
            converter:      converter function for the result type
            parameter_dict: parameter dictionary for the range command

        Returns:
            list[Any]: converted values
        """

        #----------------- evaluate the formula

        if StringEvaluate.is_python_script(value_list):
            value_list = StringEvaluate.exec_function_string(value_list, parameter_dict)

        elif GeneralConstants.TEXT_KEY in value_list:
            value_list = StringEvaluate.eval(value_list, parameter_dict, converter != str)


        #------------------ single value can be a parameter

        elif GeneralConstants.TEXT_SEPARATOR not in value_list and value_list in parameter_dict:
            param_value = parameter_dict[value_list]

            if isinstance(param_value, dict):
                value_list = GeneralConstants.TEXT_SEPARATOR.join([str(val) for val in param_value.values()])
            else:
                value_list = GeneralConstants.TEXT_SEPARATOR.join([str(val) for val in param_value])

        if not value_list:
            return []

        if not value_list:
            return []


        #----------------- standard value list or from range

        if GeneralConstants.LIST_SEPARATOR_START not in value_list:
            if converter != str:
                value_list = value_list.strip(GeneralConstants.TEXT_SEPARATOR)

            return [converter(value) for value in value_list.split(GeneralConstants.TEXT_SEPARATOR)]

        return ValueListValidator.__list_from_range_string(value_list, value_type, converter, parameter_dict)


    @staticmethod
    def __list_from_range_string(range_string  : str,
                                 value_type    : str,
                                 converter     : Callable[[(str | int | float)], ConvTypeVar],
                                 parameter_dict: dict[str, Any]) -> list[ConvTypeVar]:
        """ create a value list from a range loop string

        Args:
            range_string:   range command string
            value_type:     value_type
            converter:      converter function for the result type
            parameter_dict: parameter dictionary for the range command

        Returns:
            converted values
        """

        step = 1000 if value_type.find("length") != -1 else 1

        def float_range(start: float,
                        stop : float,
                        delta: float = step) -> Iterator[float]:
            """ execute the float range

            Args:
                start: start value
                stop:  end value
                delta: delta value

            Yield:
                value iterator
            """

            while start < stop:
                yield start

                start += delta

        if GeneralConstants.FLOAT_KEY in range_string or converter == float:
            range_string = range_string.replace("range", "float_range")

        parameter_dict["float_range"] = float_range

        try:
            return list(converter(value) for value in eval(range_string, parameter_dict))

        except TypeError:
            range_string = range_string.replace("range", "float_range")

            return list(converter(value) for value in eval(range_string, parameter_dict))


    @staticmethod
    def get_value_by_text_id(ctrl_prop: ControlProperties,
                             text_id  : str) -> (str | None):
        """ Gets value from list of possible control values e.g. combo box, by text_id.

        Args:
            ctrl_prop: control properties
            text_id:   text ID

        Returns:
            The value or None if there is no corresponding value.
        """

        if ctrl_prop.value_list_textids is None:
            return None

        text_ids = ctrl_prop.value_list_textids.split(GeneralConstants.TEXT_SEPARATOR)

        if text_id in text_ids:
            values = ctrl_prop.value_list.split(GeneralConstants.TEXT_SEPARATOR)
            return values[text_ids.index(text_id)]

        return None

    @staticmethod
    def check_length(*value_lists: str) -> None:
        """Checks, whether the given value lists all contain the same number of entries separated with '|'

        Args:
            value_lists: value lists to check

        Raises:
            ValueError: when given value lists contain different number of entries

        Examples:
            >>> ValueListValidator.check_length("one|two|three", "four|five|six")
            >>> ValueListValidator.check_length("one|two|three", "four|five")
            ValueError: The value lists contain different number of entries. ...
        """
        unequal_lengths = False
        leader = len(value_lists[0].split("|"))

        err_msg = "The value lists contain different number of entries. For example:\n"
        err_msg += f"This value list ({value_lists[0]}) contains {leader} entries\n"

        for value_list in value_lists[1:]:
            if (follower := len(value_list.split("|"))) != leader:
                err_msg += f"This value list ({value_list}) contains {follower} entries\n"
                unequal_lengths = True
                break

        if unequal_lengths:
            raise ValueError(err_msg)

```

</details>