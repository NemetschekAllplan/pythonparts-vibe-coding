---
title: "GeometryUtil"
source: "PythonPartsFramework\SmartPartUtils\GeometryUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GeometryUtil

> **Pfad:** `PythonPartsFramework\SmartPartUtils\GeometryUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the SmartPart geometry utilities 

## Abhängigkeiten

- `NemAll_Python_Geometry`

## Klassen

### `GeometryUtil`

implementation of the SmartPart geometry utilities 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `poly_element_2d` | `fill_frame, *args` | `AllplanGeo.Polygon2D` | create a  by point coordinates  |
| `poly_element_2d_by_state` | `fill_frame, *args` | `AllplanGeo.Polygon2D` | create a Polygon2D by point coordinates and a state  |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the SmartPart geometry utilities """

import NemAll_Python_Geometry as AllplanGeo

class GeometryUtil():
    """ implementation of the SmartPart geometry utilities """


    @staticmethod
    def poly_element_2d(fill_frame, *args) -> AllplanGeo.Polygon2D:
        """ create a  by point coordinates """

        poly = AllplanGeo.Polygon2D() if fill_frame & 4 else AllplanGeo.Polyline2D()

        for index in range(0, len(args), 2):
            poly += AllplanGeo.Point2D(args[index], args[index + 1])

        if fill_frame & 4 and  poly.StartPoint != poly.EndPoint:
            poly += poly.StartPoint

        return poly


    @staticmethod
    def poly_element_2d_by_state(fill_frame, *args) -> AllplanGeo.Polygon2D:
        """ create a Polygon2D by point coordinates and a state """

        poly = AllplanGeo.Polygon2D() if fill_frame & 4 else AllplanGeo.Polyline2D()

        for index in range(0, len(args), 3):
            x_val  = args[index]
            y_val  = args[index + 1]
            state = args[index + 2]

            if state == 0:
                poly += AllplanGeo.Point2D(x_val, y_val)

            elif state == 100:
                poly += poly.GetLastPoint() + AllplanGeo.Point2D(x_val, y_val)

            else:
                assert False, "GeometryUtil: state " + str(state) + "not implemented"

        if fill_frame & 4 and poly.StartPoint != poly.EndPoint:
            poly += poly.StartPoint

        return poly

```

</details>