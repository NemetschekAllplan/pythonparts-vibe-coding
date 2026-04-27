---
title: "StringToValueUtil"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\StringToValueUtil.py"
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


# StringToValueUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\StringToValueUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

Script for StringToValueUtil

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Utility`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `math`
- `re`
- `typing`

## Klassen

### `StringToValueUtil`

Definition of class StringToValueUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_bool_value_from_str` | `value_str: str` | `bool` | Extract boolean value of string  Args:     value_str: String to parse for True or False.  Returns:     bool value from the string |
| `get_property_string` | `value_str: str, prop: str, default: Any` | `str` | Get the property string for a property  Args:     value_str:      Value string like "Center(1000,2000,300)MinorRadius(500)"     prop:           Property     default:        Default value string  Returns:     property string |
| `get_property_float` | `value_str: str, prop: str, default: float | str` | `float` | Get the float property value for a property  Args:     value_str:      Value string like "MinorRadius(500)"     prop:           Property     default:        Default value string  Returns:     property value |
| `get_property_angle` | `value_str: str, prop: str, default: float | str` | `float` | Get the angle property value for a property  Args:     value_str:      Value string like "Angle(50)"     prop:           Property     default:        Default value string  Returns:     property value |
| `get_property_geo_angle` | `value_str: str, prop: str, default: float | str` | `AllplanGeo.Angle` | Get the geometry angle property value for a property  Args:     value_str: Value string like "Angle(50)     prop:      Property     default:   Default value string  Returns:     property value |
| `get_property_int` | `value_str: str, prop: str, default: int | str` | `int` | Get the int property value for a property  Args:     value_str:      Value string like "Count(10)"     prop:           Property     default:        Default value string  Returns:     property value |
| `get_property_bool` | `value_str: str, prop: str, default: bool` | `bool` | Get the bool property value for a property  Args:     value_str:      Value string like "HasAxis(True)"     prop:           Property     default:        Default value string  Returns:     property value |
| `get_property_guid` | `value_str: str, prop: str, default: str` | `AllplanEleAdapter.GUID` | Get the int property value for a property  Args:     value_str:      Value string like "Center(1000,2000,300)MinorRadius(500)"     prop:           Property     default:        Default value string  Returns:     property value |
| `get_property_enum` | `value_str: str, prop: str, default: str, enums: list[T]` | `T | None` | Get the int property value for a property  Args:     value_str:      Value string like "Center(1000,2000,300)MinorRadius(500)"     prop:           Property     default:        Default value string     enums:          enumerations  Returns:     property value |
| `split_to_value_list` | `value_str: str` | `list[str]` | Split the string to a list of values  Args:     value_str: value string  Returns:     list of values |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for StringToValueUtil
"""

from typing import Any, Generic, TypeVar

import math
import re

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Utility as AllplanUtil

from StringEvaluate import StringEvaluate

from Utilities.GeneralConstants import GeneralConstants

T = TypeVar("T")

class StringToValueUtil(Generic[T]):
    """ Definition of class StringToValueUtil
    """

    @staticmethod
    def get_bool_value_from_str(value_str: str) -> bool:
        """ Extract boolean value of string

        Args:
            value_str: String to parse for True or False.

        Returns:
            bool value from the string
        """
        return value_str.lower() == GeneralConstants.LOWER_TRUE


    @staticmethod
    def get_property_string(value_str:str,
                            prop     : str,
                            default  : Any) -> str:
        """ Get the property string for a property

        Args:
            value_str:      Value string like "Center(1000,2000,300)MinorRadius(500)"
            prop:           Property
            default:        Default value string

        Returns:
            property string
        """

        #----------------- get the value of the property

        parts = re.split(fr"\b{prop}\b", value_str, 1)

        if len(parts) == 1:
            return default


        #----------------- get the value

        nclose = 0
        nopen  = 0

        value = parts[1].strip()

        for i, char in enumerate(value):
            if char == GeneralConstants.BRACKET_OPEN:
                nopen += 1

            elif char == GeneralConstants.BRACKET_CLOSE:
                nclose += 1

            if nopen == nclose:
                return value[1: i]

        return value[1:]


    @staticmethod
    def get_property_float(value_str: str,
                           prop     : str,
                           default  : (float | str)) -> float:
        """ Get the float property value for a property

        Args:
            value_str:      Value string like "MinorRadius(500)"
            prop:           Property
            default:        Default value string

        Returns:
            property value
        """

        return float(StringToValueUtil.get_property_string(value_str, prop, default))


    @staticmethod
    def get_property_angle(value_str: str,
                           prop     : str,
                           default  : (float | str)) -> float:
        """ Get the angle property value for a property

        Args:
            value_str:      Value string like "Angle(50)"
            prop:           Property
            default:        Default value string

        Returns:
            property value
        """

        math_dict = {"pi": math.pi}

        return float(eval(StringToValueUtil.get_property_string(value_str, prop, default), math_dict))  # pylint: disable=eval-used


    @staticmethod
    def get_property_geo_angle(value_str: str,
                               prop     : str,
                               default  : (float | str)) -> AllplanGeo.Angle:
        """ Get the geometry angle property value for a property

        Args:
            value_str: Value string like "Angle(50)
            prop:      Property
            default:   Default value string

        Returns:
            property value
        """

        math_dict = {"pi": math.pi}

        return AllplanGeo.Angle(float(eval(StringToValueUtil.get_property_string(value_str, prop, default), math_dict)))  # pylint: disable=eval-used


    @staticmethod
    def get_property_int(value_str: str,
                         prop     : str,
                         default  : (int | str)) -> int:
        """ Get the int property value for a property

        Args:
            value_str:      Value string like "Count(10)"
            prop:           Property
            default:        Default value string

        Returns:
            property value
        """

        return int(StringToValueUtil.get_property_string(value_str, prop, default))


    @staticmethod
    def get_property_bool(value_str: str,
                          prop     : str,
                          default  : bool) -> bool:
        """ Get the bool property value for a property

        Args:
            value_str:      Value string like "HasAxis(True)"
            prop:           Property
            default:        Default value string

        Returns:
            property value
        """

        return bool(int(StringToValueUtil.get_property_string(value_str, prop, default)))


    @staticmethod
    def get_property_guid(value_str: str,
                         prop      : str,
                         default   : str) -> AllplanEleAdapter.GUID:
        """ Get the int property value for a property

        Args:
            value_str:      Value string like "Center(1000,2000,300)MinorRadius(500)"
            prop:           Property
            default:        Default value string

        Returns:
            property value
        """

        return AllplanUtil.GUID.FromString(StringToValueUtil.get_property_string(value_str, prop, default)) # type: ignore


    @staticmethod
    def get_property_enum(value_str: str,
                          prop     : str,
                          default  : str,
                          enums    : list[T]) -> (T | None):
        """ Get the int property value for a property

        Args:
            value_str:      Value string like "Center(1000,2000,300)MinorRadius(500)"
            prop:           Property
            default:        Default value string
            enums:          enumerations

        Returns:
            property value
        """

        value = int(eval(StringToValueUtil.get_property_string(value_str, prop, default), StringEvaluate.get_allplan_api_param_dict()))  # pylint: disable=eval-used

        return next((enum_value for enum_value in enums if enum_value == value), None)


    @staticmethod
    def split_to_value_list(value_str: str) -> list[str]:
        """ Split the string to a list of values

        Args:
            value_str: value string

        Returns:
            list of values
        """

        if value_str.startswith(GeneralConstants.LIST_SEPARATOR_START):
            value_str = value_str[1:]

        if value_str.endswith(GeneralConstants.LIST_SEPARATOR_END):
            value_str = value_str[:-1]

        return [item.strip() for item in value_str.split(GeneralConstants.LIST_ITEM_SEPARATOR)]

```

</details>