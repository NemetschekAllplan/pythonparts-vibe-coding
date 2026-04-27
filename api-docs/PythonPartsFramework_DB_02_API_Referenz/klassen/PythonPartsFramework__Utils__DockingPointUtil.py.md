---
title: "DockingPointUtil"
source: "PythonPartsFramework\Utils\DockingPointUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# DockingPointUtil

> **Pfad:** `PythonPartsFramework\Utils\DockingPointUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

Implementation of the docking point utilities

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `__future__`
- `typing`

## Klassen

### `DockingPointUtil`

Implementation of the docking point utilities 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_docking_points` | `element_key: str, element: Any` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_line2d_docking_points` | `element_key: str, element: AllplanGeo.Line2D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_line3d_docking_points` | `element_key: str, element: AllplanGeo.Line3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_polyline2d_docking_points` | `element_key: str, element: AllplanGeo.Polyline2D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_polyline3d_docking_points` | `element_key: str, element: AllplanGeo.Polyline3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_polygon2d_docking_points` | `element_key: str, element: AllplanGeo.Polygon2D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_polygon3d_docking_points` | `element_key: str, element: AllplanGeo.Polygon3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_spline2d_docking_points` | `element_key: str, element: AllplanGeo.Spline2D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_spline3d_docking_points` | `element_key: str, element: AllplanGeo.Spline3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_bspline2d_docking_points` | `element_key: str, element: AllplanGeo.BSpline2D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_bspline3d_docking_points` | `element_key: str, element: AllplanGeo.BSpline3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_arc2d_docking_points` | `element_key: str, element: AllplanGeo.Arc2D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_arc3d_docking_points` | `element_key: str, element: AllplanGeo.Arc3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_polyhedron3d_docking_points` | `element_key: str, element: AllplanGeo.Polyhedron3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_brep3d_docking_points` | `element_key: str, element: AllplanGeo.BRep3D` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     element:     geometry element  Returns:     list with the docking points |
| `__get_poly_point_curve2d_docking_points` | `element_key: str, points: List[AllplanGeo.Point2D]` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     points:      Points  Returns:     list with the docking points |
| `__get_poly_point_curve3d_docking_points` | `element_key: str, points: List[AllplanGeo.Point3D]` | `List[Tuple[str, AllplanGeo.Point3D]]` | get the docking points  Args:     element_key: geometry element key     points:        Returns:     list with the docking points |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Implementation of the docking point utilities
"""

# pylint: disable=unused-private-member

from __future__ import annotations

from typing import Any, Callable, List, Tuple, Optional

import NemAll_Python_Geometry as AllplanGeo

class DockingPointUtil():
    """ Implementation of the docking point utilities """

    @staticmethod
    def get_docking_points(element_key: str,
                           element    : Any) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        value_type = str(type(element))

        value_type = value_type.replace("<class 'NemAll_Python_Geometry.", "")[:-2].lower()

        geo_fct: Optional[Callable] = getattr(DockingPointUtil, "_DockingPointUtil__get_" + value_type + "_docking_points", None)

        if geo_fct is None:
            print("Missing function for type: " + value_type)
            return []

        if value_type.find("2d") != -1:
            return geo_fct(element_key, element)

        return geo_fct(element_key, element)


    @staticmethod
    def __get_line2d_docking_points(element_key: str,
                                    element: AllplanGeo.Line2D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        docking_points = [(element_key + "s", AllplanGeo.Point3D(element.StartPoint)),
                          (element_key + "e", AllplanGeo.Point3D(element.EndPoint))]

        return docking_points


    @staticmethod
    def __get_line3d_docking_points(element_key: str,
                                    element: AllplanGeo.Line3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        docking_points = [(element_key + "s", element.StartPoint),
                          (element_key + "e", element.EndPoint)]

        return docking_points


    @staticmethod
    def __get_polyline2d_docking_points(element_key: str,
                                        element: AllplanGeo.Polyline2D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve2d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_polyline3d_docking_points(element_key: str,
                                        element: AllplanGeo.Polyline3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve3d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_polygon2d_docking_points(element_key: str,
                                        element: AllplanGeo.Polygon2D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve2d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_polygon3d_docking_points(element_key: str,
                                        element: AllplanGeo.Polygon3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve3d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_spline2d_docking_points(element_key: str,
                                      element: AllplanGeo.Spline2D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve2d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_spline3d_docking_points(element_key: str,
                                      element: AllplanGeo.Spline3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve3d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_bspline2d_docking_points(element_key: str,
                                       element: AllplanGeo.BSpline2D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve2d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_bspline3d_docking_points(element_key: str,
                                       element: AllplanGeo.BSpline3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        return DockingPointUtil.__get_poly_point_curve3d_docking_points(element_key, element.Points)


    @staticmethod
    def __get_arc2d_docking_points(element_key: str,
                                   element: AllplanGeo.Arc2D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        docking_points = [(element_key + "s", AllplanGeo.Point3D(element.StartPoint)),
                          (element_key + "c", AllplanGeo.Point3D(element.Center)),
                          (element_key + "e", AllplanGeo.Point3D(element.EndPoint))]

        return docking_points


    @staticmethod
    def __get_arc3d_docking_points(element_key: str,
                                   element: AllplanGeo.Arc3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        docking_points = [(element_key + "s", element.StartPoint),
                          (element_key + "c", element.Center),
                          (element_key + "e", element.EndPoint)]

        return docking_points


    @staticmethod
    def __get_polyhedron3d_docking_points(element_key: str,
                                          element: AllplanGeo.Polyhedron3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """

        docking_points = []

        for index, vertex in enumerate(element.GetVertices()):
            docking_points.append((element_key + str(index), vertex))

        return docking_points


    @staticmethod
    def __get_brep3d_docking_points(element_key: str,
                                    element: AllplanGeo.BRep3D) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            element:     geometry element

        Returns:
            list with the docking points
        """
        docking_points = []


        #----------------- cone

        cone_data = element.IsCone()

        if cone_data[0]:
            center = cone_data[1].GetOrigin()

            local_mat = cone_data[1].GetTransformationMatrix()
            local_mat.SetTranslation(AllplanGeo.Vector3D())

            height_vec        = AllplanGeo.Transform(AllplanGeo.Vector3D(0, 0, cone_data[4]), local_mat)
            bottom_radius_vec = AllplanGeo.Transform(AllplanGeo.Vector3D(cone_data[2], 0, 0), local_mat)
            top_radius_vec    = AllplanGeo.Transform(AllplanGeo.Vector3D(cone_data[3], 0, 0), local_mat)

            docking_points.append((element_key + "b", center))
            docking_points.append((element_key + "t", center + height_vec))
            docking_points.append((element_key + "br", center + bottom_radius_vec))
            docking_points.append((element_key + "bl", center - bottom_radius_vec))
            docking_points.append((element_key + "tl", center + height_vec + top_radius_vec))
            docking_points.append((element_key + "tr", center + height_vec - top_radius_vec))

            return docking_points


        #----------------- sphere

        sphere_data = element.IsSphere()

        if sphere_data[0]:
            center = sphere_data[1].GetOrigin()

            docking_points.append((element_key + "c", center))
            docking_points.append((element_key + "r", center + AllplanGeo.Vector3D(sphere_data[2], 0, 0)))

            return docking_points


        #----------------- general BRep3D

        _, vertices = element.GetVertices()

        for index, vertex in enumerate(vertices):
            docking_points.append((element_key + str(index), vertex))

        return docking_points


    @staticmethod
    def __get_poly_point_curve2d_docking_points(element_key: str,
                                                points: List[AllplanGeo.Point2D]) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            points:      Points

        Returns:
            list with the docking points
        """

        return [(element_key + str(index), AllplanGeo.Point3D(point)) for index, point in enumerate(points)]


    @staticmethod
    def __get_poly_point_curve3d_docking_points(element_key: str,
                                                points: List[AllplanGeo.Point3D]) -> List[Tuple[str, AllplanGeo.Point3D]]:
        """ get the docking points

        Args:
            element_key: geometry element key
            points:      

        Returns:
            list with the docking points
        """

        return [(element_key + str(index), point) for index, point in enumerate(points)]

```

</details>