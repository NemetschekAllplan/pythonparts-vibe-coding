---
title: "Arc2DUtil"
source: "PythonPartsFramework\Utils\Geometry\Arc2DUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Arc2DUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\Arc2DUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the arc 2D utility class

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `__future__`

## Klassen

### `Arc2DUtil`

implementation of the arc 2D utility class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create` | `center: AllplanGeo.Point2D, radius: float, angle_start: float=0.0, angle_end: float=360.0` | `AllplanGeo.Arc2D | None` | create a 2d arc  Args:     center:      center point of the arc     radius:      radius     angle_start: start angle     angle_end:   end angle  Returns:     created arc or None if start and end angle are equal |
| `create_circle` | `center_point: AllplanGeo.Point2D, radius: float` | `None` | create a 2d circle  Args:     center_point: center point of the circle     radius:       radius |
| `create_arc_from_tangent_and_end_point` | `tangent: AllplanGeo.Line2D, end_point: AllplanGeo.Point2D` | `AllplanGeo.Arc2D` | create an arc tangential from a line to a point  Args:     tangent:   tangent line     end_point: end point of the arc  Returns:     created arc |
| `create_arc_from_center_start_end_point` | `center_point: AllplanGeo.Point2D, start_point: AllplanGeo.Point2D, end_point: AllplanGeo.Point2D` | `AllplanGeo.Arc2D` | create an arc from center, start and end point  Args:     center_point: center point of the arc     start_point:  start point of the arc     end_point:    end point of the arc  Returns:     created arc |
| `create_arc_from_center_start_delta` | `center_point: AllplanGeo.Point2D, start_point: AllplanGeo.Point2D, delta_angle: float` | `AllplanGeo.Arc2D` | create an arc from center, start point and delta angle  Args:     center_point: center point of the arc     start_point:  start point of the arc     delta_angle:  angle between start and end point  Returns:     created arc |
| `create_polygonized_arc` | `x_center: float, y_center: float, radius: float, angle_start: float=0.0, angle_end: float=360.0` | `AllplanGeo.Polygon2D | None` | create a 2d arc converted to a polygon  Args:     x_center:    x coordinate center     y_center:    y coordinate center     radius:      radius     angle_start: start angle     angle_end:   end angle  Returns:     created arc or None if start and end angle are equal |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the arc 2D utility class
"""

from __future__ import annotations

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class Arc2DUtil():
    """ implementation of the arc 2D utility class
    """

    @staticmethod
    def create(center     : AllplanGeo.Point2D,
               radius     : float,
               angle_start: float = 0.,
               angle_end  : float = 360.) -> (AllplanGeo.Arc2D | None):
        """ create a 2d arc

        Args:
            center:      center point of the arc
            radius:      radius
            angle_start: start angle
            angle_end:   end angle

        Returns:
            created arc or None if start and end angle are equal
        """

        if angle_start == angle_end:
            return None

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        radius = radius * length_fac

        return AllplanGeo.Arc2D(AllplanGeo.Point2D(center.X * length_fac, center.Y * length_fac),
                                radius, radius, 0.,
                                AllplanGeo.Angle.DegToRad(angle_start),
                                AllplanGeo.Angle.DegToRad(angle_end))


    @staticmethod
    def create_circle(center_point: AllplanGeo.Point2D,
                      radius      : float):
        """ create a 2d circle

        Args:
            center_point: center point of the circle
            radius:       radius
        """

        Arc2DUtil.create(center_point, radius)


    @staticmethod
    def create_arc_from_tangent_and_end_point(tangent  : AllplanGeo.Line2D,
                                              end_point: AllplanGeo.Point2D) -> AllplanGeo.Arc2D:
        """ create an arc tangential from a line to a point

        Args:
            tangent:   tangent line
            end_point: end point of the arc

        Returns:
            created arc
        """

        loc_arc_pnt = AllplanGeo.TransformCoord.PointLocal(tangent, end_point)

        loc_perpend_pnt = AllplanGeo.Point2D(AllplanGeo.CalcLength(tangent), loc_arc_pnt.Y)

        perpendicular = AllplanGeo.Line2D(tangent.EndPoint,
                                          AllplanGeo.TransformCoord.PointGlobal(tangent, loc_perpend_pnt).To2D)


        #----------------- calculate the bisector

        chord = AllplanGeo.Line2D(tangent.EndPoint, end_point)

        loc_bisector_end = AllplanGeo.TransformCoord.PointLocal(chord, AllplanGeo.Point2D(AllplanGeo.CalcLength(chord) / 2, -1000))

        bisector = AllplanGeo.Line2D(AllplanGeo.Point2D((chord.StartPoint + chord.EndPoint) / 2),
                                    AllplanGeo.TransformCoord.PointGlobal(chord, loc_bisector_end).To2D)


        #---------------- calculate the center and radius

        result, center_pnt = AllplanGeo.IntersectionCalculusEx(perpendicular, bisector)

        if not result:
            return AllplanGeo.Arc2D()

        radius = AllplanGeo.Vector2D(center_pnt, end_point).GetLength()


        #---------------- create the arc

        start_angle = AllplanGeo.Vector2D(center_pnt, tangent.EndPoint).GetAngle()
        end_angle   = AllplanGeo.Vector2D(center_pnt, end_point).GetAngle()

        if start_angle.Get() > end_angle.Get():
            start_angle, end_angle = end_angle, start_angle

        return AllplanGeo.Arc2D(center_pnt, radius, radius, 0, start_angle.Get(), end_angle.Get())


    @staticmethod
    def create_arc_from_center_start_end_point(center_point: AllplanGeo.Point2D,
                                               start_point : AllplanGeo.Point2D,
                                               end_point   : AllplanGeo.Point2D) -> AllplanGeo.Arc2D:
        """ create an arc from center, start and end point

        Args:
            center_point: center point of the arc
            start_point:  start point of the arc
            end_point:    end point of the arc

        Returns:
            created arc
        """

        radius = AllplanGeo.Vector2D(center_point, start_point).GetLength()

        start_angle = AllplanGeo.Vector2D(center_point, start_point).GetAngle()
        end_angle   = AllplanGeo.Vector2D(center_point, end_point).GetAngle()

        if start_angle.Get() > end_angle.Get():
            start_angle, end_angle = end_angle, start_angle

        return AllplanGeo.Arc2D(center_point, radius, radius, 0, start_angle.Get(), end_angle.Get())


    @staticmethod
    def create_arc_from_center_start_delta(center_point: AllplanGeo.Point2D,
                                           start_point : AllplanGeo.Point2D,
                                           delta_angle : float) -> AllplanGeo.Arc2D:
        """ create an arc from center, start point and delta angle

        Args:
            center_point: center point of the arc
            start_point:  start point of the arc
            delta_angle:  angle between start and end point

        Returns:
            created arc
        """

        radius = AllplanGeo.Vector2D(center_point, start_point).GetLength()

        start_angle = AllplanGeo.Vector2D(center_point, start_point).GetAngle()
        end_angle   = start_angle + AllplanGeo.Angle.FromDeg(delta_angle)

        if start_angle.Get() > end_angle.Get():
            start_angle, end_angle = end_angle, start_angle

        return AllplanGeo.Arc2D(center_point, radius, radius, 0, start_angle.Get(), end_angle.Get())


    @staticmethod
    def create_polygonized_arc(x_center   : float,
                               y_center   : float,
                               radius     : float,
                               angle_start: float = 0.,
                               angle_end  : float = 360.) -> (AllplanGeo.Polygon2D | None):
        """ create a 2d arc converted to a polygon

        Args:
            x_center:    x coordinate center
            y_center:    y coordinate center
            radius:      radius
            angle_start: start angle
            angle_end:   end angle

        Returns:
            created arc or None if start and end angle are equal
        """

        if (arc := Arc2DUtil.create(AllplanGeo.Point2D(x_center, y_center), radius, angle_start, angle_end)) is None:
            return None

        result, polyline = AllplanGeo.Polygonize(arc, arc.StartPoint, arc.EndPoint, 36, False)

        if not result:
            return None

        return AllplanGeo.Polygon2D(polyline.Points)

```

</details>