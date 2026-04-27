---
title: "Path2DUtil"
source: "PythonPartsFramework\Utils\Geometry\Path2DUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Path2DUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\Path2DUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implemenentation of the Path2DUtil

- create a Path2D from lines, polylines, tangent arcs and center radius point arcs

## Abhängigkeiten

- `Arc2DUtil`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `__future__`
- `typing`

## Klassen

### `TangentArc2DSegment`

TangentArc2D segment

This class represents a segment of a tangent arc in 2D space.
It is initialized with an end point and can be scaled by a matrix.

The `execute` method is intended to create an arc based on a tangent line.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, end: AllplanGeo.Point2D` | `None` | initialize  Args:     end:  end point |
| `__mul__` | `self, scale_mat: AllplanGeo.Matrix2D` | `TangentArc2DSegment` | multiply the geometry with a matrix  Args:     scale_mat: scale matrix  Returns:     scaled tangent arc |
| `execute` | `self, tangent: AllplanGeo.Line2D` | `AllplanGeo.Arc2D` | execute the builder  Args:     tangent: tangent line  Returns:     created arc |

### `CenterRadiusPointArc2DSegment`

CenterRadiusArc2D segment

This class represents a segment of an arc defined by its center and radius point.
It is initialized with a center and a radius point, and can be scaled by a matrix.

The `execute` method is intended to create an arc based on the center and radius.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, center_point: AllplanGeo.Point2D, radius_point: AllplanGeo.Point2D` | `None` | initialize  Args:     center_point: center point     radius_point: radius point |
| `__mul__` | `self, scale_mat: AllplanGeo.Matrix2D` | `CenterRadiusPointArc2DSegment` | multiply the geometry with a matrix  Args:     scale_mat: scale matrix  Returns:     scaled center radius arc |
| `execute` | `self, start_point: AllplanGeo.Point2D` | `AllplanGeo.Arc2D` | execute the builder  Args:     start_point: start point of the arc  Returns:     created arc |
| `__repr__` | `self` | `str` | string representation  Returns:     string representation |

### `Path2DUtil`

implemenentation of the Path2DUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, geo_elements: list[AllplanGeo.Point2D | AllplanGeo.Line2D | AllplanGeo.Polyline2D | AllplanGeo.Arc2D | TangentArc2DSegment | CenterRadiusPointArc2DSegment]` | `None` | initilaize  Args:     geo_elements: geometry elements |
| `execute` | `self` | `AllplanGeo.Path2D` | execute the builder  Returns:     path |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implemenentation of the Path2DUtil

    - create a Path2D from lines, polylines, tangent arcs and center radius point arcs
"""

from __future__ import annotations

from typing import cast

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

from .Arc2DUtil import Arc2DUtil


class TangentArc2DSegment():
    """ TangentArc2D segment

        This class represents a segment of a tangent arc in 2D space.
        It is initialized with an end point and can be scaled by a matrix.

        The `execute` method is intended to create an arc based on a tangent line.
    """

    def __init__(self,
                 end : AllplanGeo.Point2D):
        """ initialize

        Args:
            end:  end point
        """

        self.end_pnt = end


    def __mul__(self,
                scale_mat: AllplanGeo.Matrix2D) -> TangentArc2DSegment:
        """ multiply the geometry with a matrix

        Args:
            scale_mat: scale matrix

        Returns:
            scaled tangent arc
        """

        return TangentArc2DSegment(self.end_pnt * scale_mat)


    def execute(self,
                tangent: AllplanGeo.Line2D) -> AllplanGeo.Arc2D:
        """ execute the builder

        Args:
            tangent: tangent line

        Returns:
            created arc
        """

        return Arc2DUtil.create_arc_from_tangent_and_end_point(tangent, self.end_pnt)


class CenterRadiusPointArc2DSegment():
    """ CenterRadiusArc2D segment

        This class represents a segment of an arc defined by its center and radius point.
        It is initialized with a center and a radius point, and can be scaled by a matrix.

        The `execute` method is intended to create an arc based on the center and radius.
    """

    def __init__(self,
                 center_point: AllplanGeo.Point2D,
                 radius_point: AllplanGeo.Point2D):
        """ initialize

        Args:
            center_point: center point
            radius_point: radius point
        """

        self.center_point = center_point
        self.radius_point = radius_point


    def __mul__(self,
                scale_mat: AllplanGeo.Matrix2D) -> CenterRadiusPointArc2DSegment:
        """ multiply the geometry with a matrix

        Args:
            scale_mat: scale matrix

        Returns:
            scaled center radius arc
        """

        return CenterRadiusPointArc2DSegment(self.center_point * scale_mat, self.radius_point * scale_mat)


    def execute(self,
                start_point: AllplanGeo.Point2D) -> AllplanGeo.Arc2D:
        """ execute the builder

        Args:
            start_point: start point of the arc

        Returns:
            created arc
        """

        return Arc2DUtil.create_arc_from_center_start_end_point(self.center_point, start_point, self.radius_point)


    def __repr__(self) -> str:
        """ string representation

        Returns:
            string representation
        """

        return f"CenterRadiusPointArc2DSegment(center_point={self.center_point}, radius_point={self.radius_point})"



class Path2DUtil():
    """ implemenentation of the Path2DUtil
    """

    def __init__(self,
                 geo_elements: list[(AllplanGeo.Point2D | AllplanGeo.Line2D | AllplanGeo.Polyline2D | AllplanGeo.Arc2D | \
                                     TangentArc2DSegment | CenterRadiusPointArc2DSegment)]):
        """ initilaize

        Args:
            geo_elements: geometry elements
        """

        self.geo_elements = geo_elements


    def execute(self) -> AllplanGeo.Path2D:
        """ execute the builder

        Returns:
            path
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        scale_mat = AllplanGeo.Matrix2D()
        scale_mat.Scaling(length_fac, length_fac)

        path = AllplanGeo.Path2D()

        before_geo_element = None
        add_arc_end_pnt    = False


        #----------------- create the path from the geometry elements

        for _geo_element in self.geo_elements:
            geo_element = _geo_element * scale_mat

            match geo_element:
                case _ if isinstance(geo_element, AllplanGeo.Line2D):
                    if add_arc_end_pnt:
                        path += AllplanGeo.Line2D(path.EndPoint, geo_element.StartPoint)

                        add_arc_end_pnt = False

                    if AllplanGeo.CalcLength(geo_element) > 0:
                        path += geo_element

                case _ if isinstance(geo_element, AllplanGeo.Polyline2D):
                    if add_arc_end_pnt:
                        path += AllplanGeo.Line2D(path.EndPoint, geo_element.StartPoint)

                        add_arc_end_pnt = False

                    path += geo_element

                case _ if isinstance(geo_element, AllplanGeo.Arc2D):
                    path += geo_element

                    add_arc_end_pnt = geo_element.EndPoint

                case _ if isinstance(geo_element, TangentArc2DSegment):
                    if isinstance(before_geo_element, AllplanGeo.Line2D):
                        path += geo_element.execute(cast(AllplanGeo.Line2D, before_geo_element))

                    elif isinstance(before_geo_element, AllplanGeo.Polyline2D):
                        path += geo_element.execute(cast(AllplanGeo.Polyline2D, before_geo_element).GetLines()[-1])

                    else:
                        assert False, "TangentArc2D must be started with a line"

                case _ if isinstance(geo_element, CenterRadiusPointArc2DSegment):
                    if isinstance(before_geo_element, (AllplanGeo.Line2D, AllplanGeo.Polyline2D)):
                        path += geo_element.execute(path.EndPoint)

                    elif isinstance(before_geo_element, AllplanGeo.Point2D):
                        path += geo_element.execute(cast(AllplanGeo.Point2D, before_geo_element))

                    else:
                        assert False, "CenterRadiusPointArc2DSegment must be started with a line"

                case _ if isinstance(geo_element, AllplanGeo.Point2D) and not path.IsEmpty():
                    path += AllplanGeo.Line2D(path.EndPoint, geo_element)

            before_geo_element = geo_element

        return path

```

</details>