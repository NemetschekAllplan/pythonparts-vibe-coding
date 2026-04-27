---
title: "ParameterConnectionImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Connections\ParameterConnectionImpl.py"
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


# ParameterConnectionImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Connections\ParameterConnectionImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `werte`

## Übersicht

implementation of the time stamp connection value type

## Abhängigkeiten

- `Data.ParameterConnection`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `__future__`
- `typing`

## Klassen

### `ParameterConnectionImpl`

implementation of the time stamp connection value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string` | `value: ParameterConnection` | `str` | convert the value to a string  Args:     value: new value  Returns:     list as string |
| `get_value` | `value_str: str` | `ParameterConnection` | get the value from a string  Args:     value_str: value string  Returns:     value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the time stamp connection value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..Data.ParameterConnection import ParameterConnection

from ..ParameterPropertyValueType import ParameterPropertyValueType

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class ParameterConnectionImpl(ParameterPropertyValueType):
    """ implementation of the time stamp connection value type
    """

    @staticmethod
    def to_string(value: ParameterConnection) -> str:
        """ convert the value to a string

        Args:
            value: new value

        Returns:
            list as string
        """

        return value.to_string()


    @staticmethod
    def get_value(value_str: str) -> ParameterConnection:
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        return ParameterConnection.get_value(value_str)

```

</details>