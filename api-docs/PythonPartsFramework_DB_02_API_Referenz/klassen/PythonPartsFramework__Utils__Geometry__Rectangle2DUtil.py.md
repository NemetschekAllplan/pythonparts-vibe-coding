---
title: "Rectangle2DUtil"
source: "PythonPartsFramework\Utils\Geometry\Rectangle2DUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Rectangle2DUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\Rectangle2DUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the 2D rectangle utility functions

- create a rectangle polygon by center point, rotation angle, width and thickness
- create a rectangle polygon by corner points

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `Rectangle2DUtil`

implementation of the 2D rectangle utility functions
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `polygon_by_center` | `center_point: AllplanGeo.Point2D, rotation_angle: AllplanGeo.Angle, width: float, thickness: float` | `AllplanGeo.Polygon2D` | create a rectangle polygon by center point, rotation angle, width and thickness  Args:     center_point:   center point     rotation_angle: rotation angle     width:          width     thickness:      thickness  Returns:     rectangle polygon |
| `polygon_by_sizes` | `width: float, thickness: float, rotation_angle: AllplanGeo.Angle` | `AllplanGeo.Polygon2D` | create a rectangle polygon by width and thickness, located at origin  Args:     width:          width     thickness:      thickness     rotation_angle: rotation angle  Returns:     rectangle polygon |
| `polygon_by_corner_points` | `bottom_left: AllplanGeo.Point2D, top_right: AllplanGeo.Point2D` | `AllplanGeo.Polygon2D` | create a model element for a 2d rectangle by corner points  Args:     bottom_left: bottom left corner point     top_right:   top right corner point  Returns:     returns |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the 2D rectangle utility functions

    - create a rectangle polygon by center point, rotation angle, width and thickness
    - create a rectangle polygon by corner points
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class Rectangle2DUtil():
    """ implementation of the 2D rectangle utility functions
    """

    @staticmethod
    def polygon_by_center(center_point  : AllplanGeo.Point2D,
                          rotation_angle: AllplanGeo.Angle,
                          width         : float,
                          thickness     : float) -> AllplanGeo.Polygon2D:
        """ create a rectangle polygon by center point, rotation angle, width and thickness

        Args:
            center_point:   center point
            rotation_angle: rotation angle
            width:          width
            thickness:      thickness

        Returns:
            rectangle polygon
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        width     = width     * length_fac
        thickness = thickness * length_fac

        rect_poly = AllplanGeo.Polygon2D([AllplanGeo.Point2D(-width / 2, -thickness / 2),
                                          AllplanGeo.Point2D(width / 2, -thickness / 2),
                                          AllplanGeo.Point2D(width / 2, thickness / 2),
                                          AllplanGeo.Point2D(-width / 2, thickness / 2),
                                          AllplanGeo.Point2D(-width / 2, -thickness / 2)])

        rot_mat = AllplanGeo.Matrix2D()

        rot_mat.SetRotation(AllplanGeo.Point2D(), rotation_angle)
        rot_mat.Translate(AllplanGeo.Vector2D(AllplanGeo.Point2D(), center_point))

        return AllplanGeo.Transform(rect_poly, rot_mat)


    @staticmethod
    def polygon_by_sizes(width         : float,
                         thickness     : float,
                         rotation_angle: AllplanGeo.Angle) -> AllplanGeo.Polygon2D:
        """ create a rectangle polygon by width and thickness, located at origin

        Args:
            width:          width
            thickness:      thickness
            rotation_angle: rotation angle

        Returns:
            rectangle polygon
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        width     = width     * length_fac
        thickness = thickness * length_fac

        rect_poly = AllplanGeo.Polygon2D.CreateRectangle(AllplanGeo.Point2D(), AllplanGeo.Point2D(width, thickness))

        rot_mat = AllplanGeo.Matrix2D()

        rot_mat.SetRotation(AllplanGeo.Point2D(), rotation_angle)

        return AllplanGeo.Transform(rect_poly, rot_mat)



    @staticmethod
    def polygon_by_corner_points(bottom_left: AllplanGeo.Point2D,
                                 top_right  : AllplanGeo.Point2D) -> AllplanGeo.Polygon2D:
        """ create a model element for a 2d rectangle by corner points

        Args:
            bottom_left: bottom left corner point
            top_right:   top right corner point

        Returns:
            returns
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        return AllplanGeo.Polygon2D.CreateRectangle(AllplanGeo.Point2D(bottom_left.X  * length_fac, bottom_left.Y * length_fac),
                                                    AllplanGeo.Point2D(top_right.X    * length_fac, top_right.Y   * length_fac))

```

</details>