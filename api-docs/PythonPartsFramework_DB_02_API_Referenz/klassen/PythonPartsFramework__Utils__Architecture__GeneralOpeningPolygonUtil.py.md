---
title: "GeneralOpeningPolygonUtil"
source: "PythonPartsFramework\Utils\Architecture\GeneralOpeningPolygonUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GeneralOpeningPolygonUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\GeneralOpeningPolygonUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the utility for the general opening polygon creation from an opening body

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`

## Klassen

### `GeneralOpeningPolygonUtil`

" implementation of the utility for the general opening polygon creation from an opening body
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_general_element_geometry` | `general_ele: AllplanEleAdapter.BaseElementAdapter` | `tuple[AllplanGeo.Polyhedron3D | None, AllplanGeo.Polygon2D | None]` | get the geometry of the general element  Args:     general_ele: general element  Returns:     3D geometry, ground view polygon |
| `calculate_opening_polygon` | `opening: AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D, axis_line: AllplanGeo.Line3D, outer_element_geo: AllplanGeo.Polygon2D, general_ele: AllplanEleAdapter.BaseElementAdapter` | `AllplanGeo.Polygon2D` | calculate the opening polygon  Args:     opening:           opening     axis_line:         axis line     outer_element_geo: outer element geometry     general_ele:       general element  Returns:     opening polygon |
| `__get_extended_opening_outlines` | `opening: AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D, axis_line: AllplanGeo.Line3D` | `tuple[AllplanGeo.Line2D, AllplanGeo.Line2D]` | get the extended opening out lines  Args:     opening:   opening     axis_line: axis line  Returns:     opening out lines |
| `__get_geo_points_in_line_area` | `parent_ele: AllplanEleAdapter.BaseElementAdapter, line: AllplanGeo.Line2D` | `list[AllplanGeo.Point2D]` | get the points in the local area of the line  Args:     parent_ele: parent element     line:       line  Returns:     points |
| `__exend_intersection_points` | `intersection_points: tuple[AllplanGeo.Point3D, AllplanGeo.Point3D], points: list[AllplanGeo.Point2D]` | `tuple[AllplanGeo.Point3D, AllplanGeo.Point3D]` | extend the intersection points  Args:     intersection_points: intersection points     points:              points  Returns:     extended intersection points |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the utility for the general opening polygon creation from an opening body
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

class GeneralOpeningPolygonUtil():
    """" implementation of the utility for the general opening polygon creation from an opening body
    """

    @staticmethod
    def get_general_element_geometry(general_ele: AllplanEleAdapter.BaseElementAdapter) -> tuple[(AllplanGeo.Polyhedron3D | None),
                                                                                                 (AllplanGeo.Polygon2D | None)]:
        """ get the geometry of the general element

        Args:
            general_ele: general element

        Returns:
            3D geometry, ground view polygon
        """

        element_geo       = None
        outer_element_geo = None

        for child_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetTierElements(general_ele):
            if (tier_geo := child_ele.GetModelGeometry()) is None:
                continue

            if element_geo is None:
                element_geo = tier_geo
            else:
                _, element_geo = AllplanGeo.MakeUnion(element_geo, tier_geo)

            ground_view_tier_geo = child_ele.GetGroundViewArchitectureElementGeometry()

            if outer_element_geo is None:
                outer_element_geo = ground_view_tier_geo
            else:
                _, outer_element_geo = AllplanGeo.MakeUnion(outer_element_geo, ground_view_tier_geo)

        return element_geo, outer_element_geo


    @staticmethod
    def calculate_opening_polygon(opening          : (AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D),
                                  axis_line        : AllplanGeo.Line3D,
                                  outer_element_geo: AllplanGeo.Polygon2D,
                                  general_ele      : AllplanEleAdapter.BaseElementAdapter) -> AllplanGeo.Polygon2D:
        """ calculate the opening polygon

        Args:
            opening:           opening
            axis_line:         axis line
            outer_element_geo: outer element geometry
            general_ele:       general element

        Returns:
            opening polygon
        """

        outer_line1, outer_line2 = GeneralOpeningPolygonUtil.__get_extended_opening_outlines(opening, axis_line)

        found, start_points = AllplanGeo.IntersectionCalculus(outer_line1, outer_element_geo)

        if not found:
            return AllplanGeo.Polygon2D()

        found, end_points = AllplanGeo.IntersectionCalculus(outer_line2, outer_element_geo)

        if not found:
            return AllplanGeo.Polygon2D()

        if general_ele.GetElementAdapterType().GetGuid() in [AllplanEleAdapter.CircularWall_TypeUUID,
                                                             AllplanEleAdapter.ElementWall_TypeUUID]:
            points = GeneralOpeningPolygonUtil.__get_geo_points_in_line_area(general_ele,
                                                                             AllplanGeo.Line2D(start_points[0].To2D,
                                                                                               end_points[0].To2D)) + \
                     GeneralOpeningPolygonUtil.__get_geo_points_in_line_area(general_ele,
                                                                             AllplanGeo.Line2D(start_points[1].To2D,
                                                                                               end_points[1].To2D))

            start_points = GeneralOpeningPolygonUtil.__exend_intersection_points(start_points, points)
            end_points   = GeneralOpeningPolygonUtil.__exend_intersection_points(end_points, points)

        return AllplanGeo.Polygon2D([start_points[0].To2D, start_points[1].To2D, end_points[1].To2D,
                                     end_points[0].To2D, start_points[0].To2D])


    @staticmethod
    def __get_extended_opening_outlines(opening  : (AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D),
                                        axis_line: AllplanGeo.Line3D) -> tuple[AllplanGeo.Line2D, AllplanGeo.Line2D]:
        """ get the extended opening out lines

        Args:
            opening:   opening
            axis_line: axis line

        Returns:
            opening out lines
        """

        axis_angle = AllplanGeo.Vector2D(axis_line.StartPoint.To2D, axis_line.EndPoint.To2D).GetAngle()

        rot_angle = AllplanGeo.Angle(-axis_angle.Rad)

        opening_local = AllplanGeo.Rotate(opening, AllplanGeo.Axis3D(AllplanGeo.Point3D(), AllplanGeo.Vector3D(0, 0, 1000)), rot_angle)

        min_max = AllplanGeo.CalcMinMax(opening_local)[0]

        pnt1 = AllplanGeo.Rotate(min_max.Min, axis_angle).To2D
        pnt2 = AllplanGeo.Rotate(AllplanGeo.Point2D(min_max.Max.X, min_max.Min.Y), axis_angle)
        pnt3 = AllplanGeo.Rotate(AllplanGeo.Point2D(min_max.Min.X, min_max.Max.Y), axis_angle)
        pnt4 = AllplanGeo.Rotate(min_max.Max, axis_angle).To2D

        outer_line1 = AllplanGeo.Line2D(pnt1, pnt2)
        outer_line2 = AllplanGeo.Line2D(pnt3, pnt4)

        outer_line1.Extend(1000)
        outer_line2.Extend(1000)

        return outer_line1, outer_line2


    @staticmethod
    def __get_geo_points_in_line_area(parent_ele: AllplanEleAdapter.BaseElementAdapter,
                                    line      : AllplanGeo.Line2D) -> list[AllplanGeo.Point2D]:
        """ get the points in the local area of the line

        Args:
            parent_ele: parent element
            line:       line

        Returns:
            points
        """

        points = []

        line_length = AllplanGeo.CalcLength(line)

        for arch_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetTierElements(parent_ele):
            for pnt in arch_ele.GetGeometry().Points:
                if 0 <= AllplanGeo.TransformCoord.PointLocal(line, pnt).X <= line_length:
                    points.append(pnt)

        return points


    @staticmethod
    def __exend_intersection_points(intersection_points: tuple[AllplanGeo.Point3D, AllplanGeo.Point3D],
                                    points             : list[AllplanGeo.Point2D]) -> tuple[AllplanGeo.Point3D, AllplanGeo.Point3D]:
        """ extend the intersection points

        Args:
            intersection_points: intersection points
            points:              points

        Returns:
            extended intersection points
        """

        line = AllplanGeo.Line3D(*intersection_points)

        for pnt in points:
            if (x_loc := AllplanGeo.TransformCoord.PointLocal(line, pnt.To3D).X) < 0.:
                line.TrimStart(x_loc)

            if (x_loc := x_loc - AllplanGeo.CalcLength(line)) > 0:
                line.TrimEnd(-x_loc)

        return line.StartPoint, line.EndPoint

```

</details>