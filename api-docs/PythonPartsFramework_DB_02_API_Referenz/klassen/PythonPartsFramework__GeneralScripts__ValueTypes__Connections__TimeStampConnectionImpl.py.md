---
title: "TimeStampConnectionImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Connections\TimeStampConnectionImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# TimeStampConnectionImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Connections\TimeStampConnectionImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the time stamp connection value type

## Abhängigkeiten

- `BaseConnectionImpl`
- `Data.TimeStampConnection`
- `ParameterProperty`
- `__future__`
- `typing`

## Klassen

### `TimeStampConnectionImpl`

implementation of the time stamp connection value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string` | `value: TimeStampConnection | list[TimeStampConnection]` | `str` | convert the value to a string  Args:     value: new value  Returns:     list as string |
| `get_value` | `value_str: str` | `TimeStampConnection | list[TimeStampConnection]` | get the value from a string  Args:     value_str: value string  Returns:     value |

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

from ..Data.TimeStampConnection import TimeStampConnection

from .BaseConnectionImpl import BaseConnectionImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class TimeStampConnectionImpl(BaseConnectionImpl[TimeStampConnection]):
    """ implementation of the time stamp connection value type
    """

    @staticmethod
    def to_string(value: (TimeStampConnection | list[TimeStampConnection])) -> str:
        """ convert the value to a string

        Args:
            value: new value

        Returns:
            list as string
        """

        if not isinstance(value, list):
            return value.to_string()

        return ";".join(item.to_string() for item in value)


    @staticmethod
    def get_value(value_str: str) -> (TimeStampConnection | list[TimeStampConnection]):
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        return TimeStampConnection.get_value(value_str)

```

</details>