---
title: "BSpline2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BSpline2DImpl.py"
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


# BSpline2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BSpline2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the BSpline2D value type

## Abhängigkeiten

- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypes.GeometryElements.BSplineImpl`
- `importlib`
- `typing`

## Klassen

### `BSpline2DImpl`

implementation of the BSpline2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.BSpline2D] | AllplanGeo.BSpline2D` | get the 2D b-spline from a string  Args:     value_str: 2D b-spline string  Returns:     2D b-spline(s) |
| `__get_value_bspline2d` | `value_str: str` | `AllplanGeo.BSpline2D` | get a 2D bspline from a value string  Args:     value_str: Value string  Returns:     2D bspline |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the BSpline2D value type
"""

from typing import Any

import importlib

import NemAll_Python_Geometry as AllplanGeo

import ValueTypes.GeometryElements.BSplineImpl as BSplineImpl      # pylint: disable=consider-using-from-import

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .CoordinateValueUtil import CoordinateValueUtil

importlib.reload(BSplineImpl)    # the module is not visible in the reload table!

class BSpline2DImpl(BSplineImpl.BSplineImpl):
    """ implementation of the BSpline2D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.BSpline2D] | AllplanGeo.BSpline2D):
        """ get the 2D b-spline from a string

        Args:
            value_str: 2D b-spline string

        Returns:
            2D b-spline(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(BSpline2DImpl.__get_value_bspline2d, value_str)


    @staticmethod
    def __get_value_bspline2d(value_str: str) -> AllplanGeo.BSpline2D:
        """ get a 2D bspline from a value string

        Args:
            value_str: Value string

        Returns:
            2D bspline
        """

        if not value_str:
            return AllplanGeo.BSpline2D()

        value_str = value_str.replace("BSpline2D", "")

        bspline = AllplanGeo.BSpline2D(AllplanGeo.Point2DList(),
                                       CoordinateValueUtil.get_double_list(StringToValueUtil.get_property_string(value_str, "Weights", "")),
                                       CoordinateValueUtil.get_double_list(StringToValueUtil.get_property_string(value_str, "Knots", "")),
                                       StringToValueUtil.get_property_int(value_str, "Degree", 0),
                                       StringToValueUtil.get_property_bool(value_str, "IsPeriodic", False))

        return CoordinateValueUtil.add_coordinates(bspline, StringToValueUtil.get_property_string(value_str, "Points", value_str))

```

</details>