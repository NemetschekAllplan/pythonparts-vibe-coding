---
title: "BaseFloatImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\BaseFloatImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BaseFloatImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\BaseFloatImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the base class for the float based value types

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.ValueListValidator`
- `__future__`
- `typing`

## Klassen

### `BaseFloatImpl`

implementation of the base class for the float based value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string` | `value: float` | `str` | convert the length to a string  Args:     value: new value  Returns:     length as string |
| `get_value` | `value_str: str` | `list[float] | float` | get the length from a string  Args:     value_str: value string  Returns:     value from string |
| `validate_for_list_value` | `value: list[float] | float, value_type: ParameterPropertyValueType, value_list: str, parameter_dict: dict[str, Any]` | `tuple[bool, list[float] | float]` | test for an existing float value in the list  Args:     value:          value to test     value_type:     value type     value_list:     value list as pipe separated string or range command     parameter_dict: parameter dictionary for the range command  Returns:     (value was updated, value if present in the list or nearest value from the list) |
| `get_min_value` | `-` | `float` | get the minimal value  Returns:     get the minimal value |
| `get_max_value` | `-` | `float` | get the maximal value  Returns:     get the maximal value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base class for the float based value types
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from .ValueTypeUtils.ValueListValidator import ValueListValidator

from .ParameterPropertyValueType import ParameterPropertyValueType

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class BaseFloatImpl(ParameterPropertyValueType):
    """ implementation of the base class for the float based value types
    """

    @staticmethod
    def to_string(value: float) -> str:
        """ convert the length to a string

        Args:
            value: new value

        Returns:
            length as string
        """

        value_str = str(float(value))   # create float value, maybe boolean value

        return value_str if "." in value_str else f"{value_str}.0"      # pylint: disable=magic-value-comparison


    @staticmethod
    def get_value(value_str: str) -> (list[float] | float):
        """ get the length from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        return BaseStringToValueConverter.to_float(value_str)


    @staticmethod
    def validate_for_list_value(value         : (list[float] | float),
                                value_type    : ParameterPropertyValueType,
                                value_list    : str,
                                parameter_dict: dict[str, Any]) -> tuple[bool, (list[float] | float)]:
        """ test for an existing float value in the list

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

        return ValueListValidator.validate_numeric_value(value, value_type, value_list, float, parameter_dict)


    @staticmethod
    def get_min_value() -> float:
        """ get the minimal value

        Returns:
            get the minimal value
        """

        return -1.7976931348623157e+300


    @staticmethod
    def get_max_value() -> float:
        """ get the maximal value

        Returns:
            get the maximal value
        """

        return 1.7976931348623157e+300

```

</details>