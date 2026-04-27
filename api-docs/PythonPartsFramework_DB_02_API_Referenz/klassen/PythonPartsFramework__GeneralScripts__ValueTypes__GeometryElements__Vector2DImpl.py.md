---
title: "Vector2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Vector2DImpl.py"
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


# Vector2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Vector2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Vector2D value type

## Abhängigkeiten

- `CoordinateImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ParameterProperty`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `Vector2DImpl`

implementation of the Vector2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[AllplanGeo.Vector2D] | AllplanGeo.Vector2D` | get the 2D vector from a string  Args:     value_str: 2D vector string  Returns:     2D vector(s) |
| `__get_value_vector2d` | `value_str: str` | `AllplanGeo.Vector2D` | get a 2D vector from a value string  Args:     value_str: Value string  Returns:     2D vector |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Vector2D value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

from .CoordinateImpl import CoordinateImpl
from .CoordinateValueUtil import CoordinateValueUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class Vector2DImpl(CoordinateImpl):
    """ implementation of the Vector2D value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[AllplanGeo.Vector2D] | AllplanGeo.Vector2D):
        """ get the 2D vector from a string

        Args:
            value_str: 2D vector string

        Returns:
            2D vector(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Vector2DImpl.__get_value_vector2d, value_str)

    @staticmethod
    def __get_value_vector2d(value_str: str) -> AllplanGeo.Vector2D:
        """ get a 2D vector from a value string

        Args:
            value_str: Value string

        Returns:
            2D vector
        """

        return CoordinateValueUtil.get_xy_element(value_str.replace("Vector2D", ""), AllplanGeo.Vector2D())

```

</details>