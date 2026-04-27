---
title: "ArchOpeningConnectionImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Connections\ArchOpeningConnectionImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ArchOpeningConnectionImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Connections\ArchOpeningConnectionImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the architecture opening connection value type

## Abhängigkeiten

- `BaseConnectionImpl`
- `Data.ArchOpeningConnection`
- `ParameterProperty`
- `__future__`
- `typing`

## Klassen

### `ArchOpeningConnectionImpl`

implementation of the architecture opening connection value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string` | `value: ArchOpeningConnection` | `str` | convert the value to a string  Args:     value: new value  Returns:     list as string |
| `get_value` | `value_str: str` | `ArchOpeningConnection` | get the value from a string  Args:     value_str: value string  Returns:     value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the architecture opening connection value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..Data.ArchOpeningConnection import ArchOpeningConnection

from .BaseConnectionImpl import BaseConnectionImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class ArchOpeningConnectionImpl(BaseConnectionImpl):
    """ implementation of the architecture opening connection value type
    """

    @staticmethod
    def to_string(value: ArchOpeningConnection) -> str:
        """ convert the value to a string

        Args:
            value: new value

        Returns:
            list as string
        """

        return value.to_string()


    @staticmethod
    def get_value(value_str: str) -> ArchOpeningConnection:
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        return ArchOpeningConnection.get_value(value_str)

```

</details>