---
title: "ElementGeometryConnectionImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Connections\ElementGeometryConnectionImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ElementGeometryConnectionImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Connections\ElementGeometryConnectionImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the element geometry connection value type

## Abhängigkeiten

- `BaseConnectionImpl`
- `Data.ElementGeometryConnection`
- `ParameterProperty`
- `__future__`
- `typing`

## Klassen

### `ElementGeometryConnectionImpl`

implementation of the element geometry connection value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string` | `value: ElementGeometryConnection` | `str` | convert the value to a string  Args:     value: new value  Returns:     list as string |
| `get_value` | `value_str: str` | `ElementGeometryConnection` | get the value from a string  Args:     value_str: value string  Returns:     value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the element geometry connection value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..Data.ElementGeometryConnection import ElementGeometryConnection

from .BaseConnectionImpl import BaseConnectionImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class ElementGeometryConnectionImpl(BaseConnectionImpl):
    """ implementation of the element geometry connection value type
    """

    @staticmethod
    def to_string(value: ElementGeometryConnection) -> str:
        """ convert the value to a string

        Args:
            value: new value

        Returns:
            list as string
        """

        return value.to_string()


    @staticmethod
    def get_value(value_str: str) -> ElementGeometryConnection:
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        return ElementGeometryConnection.get_value(value_str)

```

</details>