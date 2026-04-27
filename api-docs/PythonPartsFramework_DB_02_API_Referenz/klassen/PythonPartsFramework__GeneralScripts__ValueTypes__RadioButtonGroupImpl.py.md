---
title: "RadioButtonGroupImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\RadioButtonGroupImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# RadioButtonGroupImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\RadioButtonGroupImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the RadioButtonGroup value type

## Abhängigkeiten

- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.BaseValueToStringConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.ValueListValidator`
- `__future__`
- `typing`

## Klassen

### `RadioButtonGroupImpl`

implementation of the RadioButtonGroup value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: int` | `str` | convert the radio button group id to a string  Args:     value: new value  Returns:     radio button id as string |
| `get_value` | `value_str: str` | `Any` | get the radio button id from a string  Args:     value_str: value string  Returns:     value from string |
| `validate_for_list_value` | `value: list[int] | int, value_type: ParameterPropertyValueType, value_list: str, parameter_dict: dict[str, Any]` | `tuple[bool, list[int] | int]` | test for an existing integer value in the list  Args:     value:          value to test     value_type:     value type     value_list:     value list as pipe separated string or range command     parameter_dict: parameter dictionary for the range command  Returns:     (value was updated, value if present in the list or nearest value from the list) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the RadioButtonGroup value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from .ValueTypeUtils.ValueListValidator import ValueListValidator

from .ValueTypeUtils.BaseValueToStringConverter import BaseValueToStringConverter
from .ParameterPropertyValueType import ParameterPropertyValueType

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class RadioButtonGroupImpl(ParameterPropertyValueType):
    """ implementation of the RadioButtonGroup value type
    """

    @staticmethod
    def set_property_value(prop : ParameterProperty,
                           name : str,
                           value: Any) -> bool:
        """ Set the value of the property

        Args:
            prop:  property
            name:  name of the modified property
            value: new value

        Returns:
            update palette state
        """

        if (enum_dict := prop.enum_dict):
            value = enum_dict[value]

        ParameterPropertyValueType.set_property_value(prop, name, value)

        return True


    @staticmethod
    def to_string(value: int) -> str:
        """ convert the radio button group id to a string

        Args:
            value: new value

        Returns:
            radio button id as string
        """

        if repr(value).startswith("NemAll_Python"):
            return BaseValueToStringConverter.enum_to_string(value)

        return str(value)


    @staticmethod
    def get_value(value_str: str) -> Any:
        """ get the radio button id from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        return BaseStringToValueConverter.to_auto(value_str)


    @staticmethod
    def validate_for_list_value(value         : (list[int] | int),
                                value_type    : ParameterPropertyValueType,
                                value_list    : str,
                                parameter_dict: dict[str, Any]) -> tuple[bool, (list[int] | int)]:
        """ test for an existing integer value in the list

        Args:
            value:          value to test
            value_type:     value type
            value_list:     value list as pipe separated string or range command
            parameter_dict: parameter dictionary for the range command

        Returns:
            (value was updated, value if present in the list or nearest value from the list)
        """

        if isinstance(value, list):
            return ValueListValidator.validate_list(value, value_type, value_list, parameter_dict)

        return ValueListValidator.validate_numeric_value(value, value_type, value_list, int, parameter_dict)

```

</details>