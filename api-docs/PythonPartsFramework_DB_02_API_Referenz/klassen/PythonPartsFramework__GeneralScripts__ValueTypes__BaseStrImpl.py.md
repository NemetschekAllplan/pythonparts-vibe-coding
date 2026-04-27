---
title: "BaseStrImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\BaseStrImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BaseStrImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\BaseStrImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the base class for the str based value types

## Abhängigkeiten

- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.ValueListValidator`
- `__future__`
- `typing`

## Klassen

### `BaseStrImpl`

implementation of the String value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string` | `value: str` | `str` | convert the string to a string  Args:     value: new value  Returns:     string as string |
| `get_value` | `value_str: str` | `list[str] | str` | get the string from a string  Args:     value_str: value string  Returns:     value from string |
| `validate_for_list_value` | `value: list[str] | str, value_type: ParameterPropertyValueType, value_list: str, parameter_dict: dict[str, Any]` | `tuple[bool, list[str] | str]` | test for an existing string value in the list  Args:     value:          value to test     value_type:     value type     value_list:     value list as pipe separated string or range command     parameter_dict: parameter dictionary for the range command  Returns:     (value was updated, value if present in the list or first value from the list) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base class for the str based value types
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from .ValueTypeUtils.ValueListValidator import ValueListValidator

from .ParameterPropertyValueType import ParameterPropertyValueType

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class BaseStrImpl(ParameterPropertyValueType):
    """ implementation of the String value type
    """

    @staticmethod
    def to_string(value: str) -> str:
        """ convert the string to a string

        Args:
            value: new value

        Returns:
            string as string
        """

        return str(value)


    @staticmethod
    def get_value(value_str: str) -> (list[str] | str):
        """ get the string from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        return BaseStringToValueConverter.to_str(value_str)


    @staticmethod
    def validate_for_list_value(value         : (list[str] | str),
                                value_type    : ParameterPropertyValueType,
                                value_list    : str,
                                parameter_dict: dict[str, Any]) -> tuple[bool, (list[str] | str)]:
        """ test for an existing string value in the list

        Args:
            value:          value to test
            value_type:     value type
            value_list:     value list as pipe separated string or range command
            parameter_dict: parameter dictionary for the range command

        Returns:
            (value was updated, value if present in the list or first value from the list)
        """

        if isinstance(value, list):
            return ValueListValidator.validate_list(value, value_type, value_list, parameter_dict)

        values = ValueListValidator.get_list_from_value_list(value_list, value_type, str, parameter_dict)

        return (False, value) if value in values or not values else (True, values[0])

```

</details>