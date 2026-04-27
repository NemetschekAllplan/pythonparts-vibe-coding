---
title: "GeometryTyping"
source: "PythonPartsFramework\TypeCollections\GeometryTyping.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
related:
  -
last_updated: "2026-02-20"
---


# GeometryTyping

> **Pfad:** `PythonPartsFramework\TypeCollections\GeometryTyping.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`

## Übersicht

implementation of the geometry typing

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `typing`

## Klassen

### `GeometryTyping`

implementation of the geometry element typing
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `is_curve_2d` | `geo_ele: CURVES` | `bool` | test for a 2D curve  Args:     geo_ele: geometry element  Returns:     curve 2D state |
| `is_curve_3d` | `geo_ele: CURVES` | `bool` | test for a 3D curve  Args:     geo_ele: geometry element  Returns:     curve 3D state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the geometry typing
"""

from typing import get_args

import NemAll_Python_Geometry as AllplanGeo

CURVES_2D = (AllplanGeo.Line2D | AllplanGeo.Arc2D | AllplanGeo.Polyline2D | AllplanGeo.Polygon2D |
             AllplanGeo.Spline2D | AllplanGeo.BSpline2D | AllplanGeo.Path2D)

POLY_CURVES_2D = (AllplanGeo.Polyline2D | AllplanGeo.Polygon2D |
                  AllplanGeo.Spline2D | AllplanGeo.BSpline2D)

CURVES_3D = (AllplanGeo.Line3D | AllplanGeo.Arc3D | AllplanGeo.Polyline3D | AllplanGeo.Polygon3D |
             AllplanGeo.Spline3D | AllplanGeo.BSpline3D | AllplanGeo.Path3D)

POLY_CURVES_3D = (AllplanGeo.Polyline3D | AllplanGeo.Polygon3D |
                  AllplanGeo.Spline3D | AllplanGeo.BSpline3D)

CURVES = CURVES_2D | CURVES_3D | None

POLY_CURVES = POLY_CURVES_2D | POLY_CURVES_3D | None

LINEAR_CURVES_3D = AllplanGeo.Line3D | AllplanGeo.Polyline3D | AllplanGeo.Polygon3D

SINGLE_POINT_CURCES = AllplanGeo.Line2D | AllplanGeo.Line3D | AllplanGeo.Arc2D | AllplanGeo.Arc3D | \
                      AllplanGeo.Path2D | AllplanGeo.Path3D

POINTS = AllplanGeo.Point3D | AllplanGeo.Point2D


class GeometryTyping():
    """ implementation of the geometry element typing
    """

    @staticmethod
    def is_curve_2d(geo_ele: CURVES) -> bool:
        """ test for a 2D curve

        Args:
            geo_ele: geometry element

        Returns:
            curve 2D state
        """

        return isinstance(geo_ele, get_args(CURVES_2D))


    @staticmethod
    def is_curve_3d(geo_ele: CURVES) -> bool:
        """ test for a 3D curve

        Args:
            geo_ele: geometry element

        Returns:
            curve 3D state
        """

        return isinstance(geo_ele, get_args(CURVES_3D))

```

</details>