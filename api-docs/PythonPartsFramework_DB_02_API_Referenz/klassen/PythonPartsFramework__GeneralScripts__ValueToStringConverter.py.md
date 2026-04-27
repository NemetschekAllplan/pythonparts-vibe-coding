---
title: "ValueToStringConverter"
source: "PythonPartsFramework\GeneralScripts\ValueToStringConverter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ValueToStringConverter

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueToStringConverter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

Script for BuildingElementXMLValue

## Abhängigkeiten

- `NemAll_Python_Utility`
- `ParameterProperty`
- `ValueTypes.ParameterPropertyValueType`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.Resources.AttributeImpl`
- `ValueTypes.ValueTypeUtils.ValueType`
- `typing`

## Klassen

### `ValueToStringConverter`

Definition of class ValueToStringConverter

Convert a string value to the real value

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string_from_value` | `value: Any, value_type: ParameterPropertyValueType, str_table: Any, attribute_id: int=0` | `str | None` | Get the string for the value type and value  Args:     value:        value     value_type:   value type     str_table:    string table     attribute_id: attribute ID  Returns:     value string |
| `to_string` | `prop: ParameterProperty, str_table: Any` | `str` | Get the string for the parameter property  Args:     prop:      parameter property     str_table: string table  Returns:     value string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementXMLValue
"""

# pylint: disable=unused-private-member

from typing import Any, cast

import NemAll_Python_Utility as AllplanUtil

from ParameterProperty import ParameterProperty

from ValueTypes.Resources.AttributeImpl import AttributeImpl
from ValueTypes.ValueTypeUtils.ValueType import ValueType

from ValueTypes.ParameterPropertyValueType import ParameterPropertyValueType
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

class ValueToStringConverter():
    """ Definition of class ValueToStringConverter

    Convert a string value to the real value
    """

    @staticmethod
    def to_string_from_value(value       : Any,
                             value_type  : ParameterPropertyValueType,
                             str_table   : Any,
                             attribute_id: int = 0) -> (str | None):
        """ Get the string for the value type and value

        Args:
            value:        value
            value_type:   value type
            str_table:    string table
            attribute_id: attribute ID

        Returns:
            value string
        """

        if isinstance(value_type, ValueType):
            value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(value_type)

        if not value_type.has_impl:
            if value_type.startswith("$"):
                return ""

            AllplanUtil.ShowMessageBox(f"ValueToStringConverter: Value type {value_type} doesn't exist!!!",  AllplanUtil.MB_OK)

            return ""

        if value_type == ParameterPropertyValueTypes.NAMED_TUPLE:
            return ""

        return value_type.to_string_extend(value, attribute_id, str_table)


    @staticmethod
    def to_string(prop     : ParameterProperty,
                  str_table: Any) -> str:
        """ Get the string for the parameter property

        Args:
            prop:      parameter property
            str_table: string table

        Returns:
            value string
        """

        return ValueToStringConverter.to_string_from_value(prop.value, prop.value_type, str_table, cast(int, prop.attribute_id))

```

</details>