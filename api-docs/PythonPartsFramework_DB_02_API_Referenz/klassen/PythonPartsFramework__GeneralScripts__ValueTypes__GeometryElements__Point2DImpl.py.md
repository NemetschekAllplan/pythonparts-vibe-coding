---
title: "Point2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Point2DImpl.py"
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


# Point2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Point2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Point2D value type

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

### `Point2DImpl`

implementation of the Point2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[AllplanGeo.Point2D] | AllplanGeo.Point2D` | get the 2D point from a string  Args:     value_str: 2D point string  Returns:     2D point(s) |
| `__get_value_point2d` | `value_str: str` | `AllplanGeo.Point2D` | get a 2D point from a value string  Args:     value_str: Value string  Returns:     2D point |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Point2D value type
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

class Point2DImpl(CoordinateImpl):
    """ implementation of the Point2D value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[AllplanGeo.Point2D] | AllplanGeo.Point2D):
        """ get the 2D point from a string

        Args:
            value_str: 2D point string

        Returns:
            2D point(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Point2DImpl.__get_value_point2d, value_str)


    @staticmethod
    def __get_value_point2d(value_str: str) -> AllplanGeo.Point2D:
        """ get a 2D point from a value string

        Args:
            value_str: Value string

        Returns:
            2D point
        """

        return CoordinateValueUtil.get_xy_element(value_str.replace("Point2D", ""), AllplanGeo.Point2D())

```

</details>