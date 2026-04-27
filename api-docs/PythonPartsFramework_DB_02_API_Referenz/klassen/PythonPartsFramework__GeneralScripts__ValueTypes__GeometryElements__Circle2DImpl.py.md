---
title: "Circle2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Circle2DImpl.py"
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


# Circle2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Circle2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Circle2D value type

## Abhängigkeiten

- `CircleImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `math`
- `typing`

## Klassen

### `Circle2DImpl`

implementation of the Circle2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Arc2D] | AllplanGeo.Arc2D` | get the 2D circle from a string  Args:     value_str: 2D circle string  Returns:     2D circle(s) |
| `__get_value_circle2d` | `value_str: str` | `AllplanGeo.Arc2D` | get a 2D circle from a value string  Args:     value_str: Value string  Returns:     2D circle |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Circle2D value type
"""

from typing import Any

import math

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .CircleImpl import CircleImpl
from .CoordinateValueUtil import CoordinateValueUtil

class Circle2DImpl(CircleImpl):
    """ implementation of the Circle2D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Arc2D] | AllplanGeo.Arc2D):
        """ get the 2D circle from a string

        Args:
            value_str: 2D circle string

        Returns:
            2D circle(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Circle2DImpl.__get_value_circle2d, value_str)


    @staticmethod
    def __get_value_circle2d(value_str: str) -> AllplanGeo.Arc2D:
        """ get a 2D circle from a value string

        Args:
            value_str: Value string

        Returns:
            2D circle
        """

        if not value_str  or  value_str == CoordinateValueUtil.EMPTY_GEO:
            return AllplanGeo.Arc2D()

        return AllplanGeo.Arc2D(CoordinateValueUtil.get_xy_element(StringToValueUtil.get_property_string(value_str, "CenterPoint", "(0,0)"),
                                                                   AllplanGeo.Point2D()),
                                StringToValueUtil.get_property_float(value_str, "MajorRadius", "0"),
                                StringToValueUtil.get_property_float(value_str, "MajorRadius", "0"),
                                0, 0, math.pi * 2 , True)

```

</details>