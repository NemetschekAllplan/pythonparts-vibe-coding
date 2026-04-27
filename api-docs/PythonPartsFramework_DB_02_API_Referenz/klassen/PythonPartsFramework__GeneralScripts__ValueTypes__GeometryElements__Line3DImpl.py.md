---
title: "Line3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Line3DImpl.py"
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


# Line3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Line3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Line3D value type

## Abhängigkeiten

- `CoordinateValueUtil`
- `LineImpl`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `typing`

## Klassen

### `Line3DImpl`

implementation of the Line3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Line3D] | AllplanGeo.Line3D` | get the 3d line from a string  Args:     value_str: 3D line string  Returns:     3D line(s) |
| `__get_value_line3d` | `value_str: str` | `AllplanGeo.Line3D` | get a 2D line from a value string  Args:     value_str: Value string  Returns:     3D line |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Line3D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

from .CoordinateValueUtil import CoordinateValueUtil
from .LineImpl import LineImpl

class Line3DImpl(LineImpl):
    """ implementation of the Line3D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Line3D]| AllplanGeo.Line3D):
        """ get the 3d line from a string

        Args:
            value_str: 3D line string

        Returns:
            3D line(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Line3DImpl.__get_value_line3d, value_str)


    @staticmethod
    def __get_value_line3d(value_str: str) -> AllplanGeo.Line3D:
        """ get a 2D line from a value string

        Args:
            value_str: Value string

        Returns:
            3D line
        """

        coords_list = CoordinateValueUtil.get_coordinates_list(value_str.replace("Line3D", ""))

        if not coords_list  or  len(coords_list[0]) < CoordinateValueUtil.POINT_COUNT_3D * 2:
            return AllplanGeo.Line3D()

        return AllplanGeo.Line3D(coords_list[0][0], coords_list[0][1], coords_list[0][2],
                                 coords_list[0][3], coords_list[0][4], coords_list[0][5])

```

</details>