---
title: "Line2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Line2DImpl.py"
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


# Line2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Line2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Line2D value type

## Abhängigkeiten

- `CoordinateValueUtil`
- `LineImpl`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `typing`

## Klassen

### `Line2DImpl`

implementation of the Line2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Line2D] | AllplanGeo.Line2D` | get the 2D line from a string  Args:     value_str: 2D line string  Returns:     2D line(s) |
| `__get_value_line2d` | `value_str: str` | `AllplanGeo.Line2D` | get a 2D line from a value string  Args:     value_str: Value string  Returns:     2D line |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Line2D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

from .CoordinateValueUtil import CoordinateValueUtil
from .LineImpl import LineImpl

class Line2DImpl(LineImpl):
    """ implementation of the Line2D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Line2D] | AllplanGeo.Line2D):
        """ get the 2D line from a string

        Args:
            value_str: 2D line string

        Returns:
            2D line(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Line2DImpl.__get_value_line2d, value_str)


    @staticmethod
    def __get_value_line2d(value_str: str) -> AllplanGeo.Line2D:
        """ get a 2D line from a value string

        Args:
            value_str: Value string

        Returns:
            2D line
        """

        coords_list = CoordinateValueUtil.get_coordinates_list(value_str.replace("Line2D", ""))

        if not coords_list or len(coords_list[0]) < CoordinateValueUtil.POINT_COUNT_2D * 2:
            return AllplanGeo.Line2D()

        return AllplanGeo.Line2D(coords_list[0][0], coords_list[0][1], coords_list[0][2], coords_list[0][3])

```

</details>