---
title: "StringToValueConverter"
source: "PythonPartsFramework\GeneralScripts\StringToValueConverter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# StringToValueConverter

> **Pfad:** `PythonPartsFramework\GeneralScripts\StringToValueConverter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

Script for BuildingElementXMLValue

## Abhängigkeiten

- `BuildingElementStringTable`
- `NemAll_Python_Utility`
- `ParameterProperty`
- `ValueListUtil`
- `ValueTypes.ParameterPropertyValueType`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.ValueTypeUtils.ValueType`
- `collections`
- `typing`

## Klassen

### `StringToValueConverter`

Definition of class StringToValueConverter

Convert a string value to the real value

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_type: ParameterPropertyValueType, value_str: str, str_table: BuildingElementStringTable | None=None, attribute_id: int | list[int]=0` | `Any` | Get the value for the value type  Args:     value_type:   value type     value_str:    value string     str_table:    string table     attribute_id: attribute ID  Returns:     returns |
| `get_default_value` | `prop: ParameterProperty, value_str: str` | `Any` | Get the default value for the property  Args:     prop:      parameter property     value_str: value string  Returns:     default value |
| `from_range_string` | `range_string: str, parameter_dict: Dict[str, Any]` | `List[Any]` | create a value list from a range loop string  Args:     range_string:   range string     parameter_dict: parameter dict  Returns:     value list |
| `to_value_by_type_converter` | `type_converter: Callable, value_str: str` | `Any` | Convert the value string to a value by the type converter, a list is possible and can have the formate "[...] * xx"  Args:     type_converter: type converter function     value_str:      value string  Returns:     returns |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementXMLValue
"""

from typing import Dict, List, Any, Iterator, Callable

from collections import namedtuple

import NemAll_Python_Utility as AllplanUtil

from BuildingElementStringTable import BuildingElementStringTable
from ParameterProperty import ParameterProperty
from ValueListUtil import ValueListUtil

from ValueTypes.ValueTypeUtils.ValueType import ValueType

from ValueTypes.ParameterPropertyValueType import ParameterPropertyValueType
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

class StringToValueConverter():
    """ Definition of class StringToValueConverter

    Convert a string value to the real value
    """

    convert_to_empty_list = "[_]"
    use_current_setting   = "-1"

    @staticmethod
    def get_value(value_type  : ParameterPropertyValueType,
                  value_str   : str,
                  str_table   : (BuildingElementStringTable | None) = None,
                  attribute_id: (int | list[int])                   = 0) -> Any:
        """ Get the value for the value type

        Args:
            value_type:   value type
            value_str:    value string
            str_table:    string table
            attribute_id: attribute ID

        Returns:
            returns
        """

        if isinstance(value_type, ValueType):
            value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(value_type)

        if not value_type.has_impl:
            if value_type.startswith("$"):      # user defined for VS
                return None

            AllplanUtil.ShowMessageBox(f"StringToValueConverter: Value type {value_type} doesn't exist!!!",  AllplanUtil.MB_OK)

            return None

        return value_type.get_value_extend(value_str, attribute_id, str_table)


    @staticmethod
    def get_default_value(prop     : ParameterProperty,
                          value_str: str) -> Any:
        """ Get the default value for the property

        Args:
            prop:      parameter property
            value_str: value string

        Returns:
            default value
        """

        if (default_value := StringToValueConverter.get_value(prop.value_type, value_str, None, prop.attribute_id)) is None:
            return None

        if not prop.value_type.startswith("namedtuple"):
            return default_value

        if not (named_tuple_def := prop.named_tuple_def):
            return None

        field_names = [name.split("(")[0] for name in named_tuple_def.field_names]

        return namedtuple(named_tuple_def.typename, field_names)(*default_value)


    @staticmethod
    def from_range_string(range_string  : str,
                          parameter_dict: Dict[str, Any]) -> List[Any]:
        """ create a value list from a range loop string

        Args:
            range_string:   range string
            parameter_dict: parameter dict

        Returns:
            value list
        """

        def float_range(start: float,
                        stop : float,
                        delta: float) -> Iterator:
            """ get a float range

            Args:
                start: start value
                stop:  stop value
                delta: delta value

            Yield:
                returns
            """

            while start < stop:         # pylint: disable=while-used
                yield start

                start += delta

        if range_string.find(".") != -1:
            range_string = range_string.replace("range", "float_range")

        parameter_dict["float_range"] = float_range

        try:
            return list(value for value in eval(range_string, parameter_dict))

        except TypeError:
            range_string = range_string.replace("range", "float_range")

            return list(value for value in eval(range_string, parameter_dict))


    @staticmethod
    def to_value_by_type_converter(type_converter: Callable,
                                   value_str     : str) -> Any:
        """ Convert the value string to a value by the type converter, a list is possible and
        can have the formate "[...] * xx"

        Args:
            type_converter: type converter function
            value_str:      value string

        Returns:
            returns
        """

        if value_str == StringToValueConverter.convert_to_empty_list:
            return []

        if value_str.find("[") == -1:
            return type_converter(value_str)

        value_parts = value_str.partition("]")

        left_str  = value_parts[0].strip("[")
        right_str = value_parts[2]

        values = left_str.split(";")

        ele_list = [type_converter(value) for value in values]

        if not right_str:
            return ele_list


        #----------------- multiply

        count = eval("1" + right_str)

        ValueListUtil.resize_list(ele_list, count)

        return ele_list

```

</details>