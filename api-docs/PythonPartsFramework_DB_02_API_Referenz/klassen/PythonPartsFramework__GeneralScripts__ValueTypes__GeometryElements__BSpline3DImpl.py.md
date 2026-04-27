---
title: "BSpline3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BSpline3DImpl.py"
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


# BSpline3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BSpline3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the BSpline3D value type

## Abhängigkeiten

- `BSplineImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `typing`

## Klassen

### `BSpline3DImpl`

implementation of the BSpline3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.BSpline3D] | AllplanGeo.BSpline3D` | get the 3D b-spline from a string  Args:     value_str: 3D b-spline string  Returns:     3D b-spline(s) |
| `__get_value_bspline3d` | `value_str: str` | `AllplanGeo.BSpline3D` | get a 3D bspline from a value string  Args:     value_str: Value string  Returns:     3D bspline |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the BSpline3D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .BSplineImpl import BSplineImpl
from .CoordinateValueUtil import CoordinateValueUtil

class BSpline3DImpl(BSplineImpl):
    """ implementation of the BSpline3D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.BSpline3D] | AllplanGeo.BSpline3D):
        """ get the 3D b-spline from a string

        Args:
            value_str: 3D b-spline string

        Returns:
            3D b-spline(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(BSpline3DImpl.__get_value_bspline3d, value_str)


    @staticmethod
    def __get_value_bspline3d(value_str: str) -> AllplanGeo.BSpline3D:
        """ get a 3D bspline from a value string

        Args:
            value_str: Value string

        Returns:
            3D bspline
        """

        if not value_str:
            return AllplanGeo.BSpline3D()

        value_str = value_str.replace("BSpline3D", "")

        bspline = AllplanGeo.BSpline3D(AllplanGeo.Point3DList(),
                                       CoordinateValueUtil.get_double_list(StringToValueUtil.get_property_string(value_str, "Weights", "")),
                                       CoordinateValueUtil.get_double_list(StringToValueUtil.get_property_string(value_str, "Knots", "")),
                                       StringToValueUtil.get_property_int(value_str, "Degree", 0),
                                       StringToValueUtil.get_property_bool(value_str, "IsPeriodic", False))

        return CoordinateValueUtil.add_coordinates(bspline, StringToValueUtil.get_property_string(value_str, "Points", value_str))

```

</details>