---
title: "AttributeUtil"
source: "PythonPartsFramework\Utils\General\AttributeUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# AttributeUtil

> **Pfad:** `PythonPartsFramework\Utils\General\AttributeUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

" implementation of the attribute utilities

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `ParameterProperty`
- `typing`

## Klassen

### `AttributeUtil`

implementation of the attribute utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_enum_id_from_value_string` | `prop: ParameterProperty` | `int` | get the enum ID from the value string  Args:     prop: parameter property  Returns:     enum ID |
| `get_enum_id_from_string` | `attribute_id: int, enum_str: str` | `int` | get the enum ID from the value string  Args:     attribute_id: attribute ID     enum_str:     enum string  Returns:     enum ID |
| `get_enum_value_string_from_id` | `prop: ParameterProperty, enum_id: int` | `str` | get the enum value string from the ID  Args:     prop:    parameter property     enum_id: enum ID  Returns:     enum string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""" implementation of the attribute utilities
"""

from typing import cast

import NemAll_Python_BaseElements as AllplanBaseEle

from ParameterProperty import ParameterProperty

class AttributeUtil:
    """ implementation of the attribute utilities
    """

    @staticmethod
    def get_enum_id_from_value_string(prop: ParameterProperty) -> int:
        """ get the enum ID from the value string

        Args:
            prop: parameter property

        Returns:
            enum ID
        """

        return AllplanBaseEle.AttributeService.GetEnumIDFromValueString(cast(int, prop.attribute_id), prop.value)

    @staticmethod
    def get_enum_id_from_string(attribute_id: int,
                                enum_str    : str) -> int:
        """ get the enum ID from the value string

        Args:
            attribute_id: attribute ID
            enum_str:     enum string

        Returns:
            enum ID
        """

        return AllplanBaseEle.AttributeService.GetEnumIDFromValueString(cast(int, attribute_id), enum_str)


    @staticmethod
    def get_enum_value_string_from_id(prop   : ParameterProperty,
                                      enum_id: int) -> str:
        """ get the enum value string from the ID

        Args:
            prop:    parameter property
            enum_id: enum ID

        Returns:
            enum string
        """

        return AllplanBaseEle.AttributeService.GetEnumValueStringFromID(cast(int, prop.attribute_id), enum_id)

```

</details>