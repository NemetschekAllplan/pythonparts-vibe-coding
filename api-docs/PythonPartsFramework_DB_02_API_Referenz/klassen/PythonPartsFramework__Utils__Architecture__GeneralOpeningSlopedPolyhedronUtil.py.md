---
title: "GeneralOpeningSlopedPolyhedronUtil"
source: "PythonPartsFramework\Utils\Architecture\GeneralOpeningSlopedPolyhedronUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GeneralOpeningSlopedPolyhedronUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\GeneralOpeningSlopedPolyhedronUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the utility for a general opening created by a sloped Polyhedron3D

## Abhängigkeiten

- `GeneralOpeningPolygonUtil`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Utility`
- `math`

## Klassen

### `GeneralOpeningSlopedPolyhedronUtil`

" implementation of the utility for a general opening created by a sloped Polyhedron3D
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_opening_polygon_and_plane_surfaces` | `general_ele: AllplanEleAdapter.BaseElementAdapter, opening_cut_geo: AllplanGeo.Polyhedron3D` | `tuple[bool, AllplanGeo.Polyhedron3D, AllplanGeo.Polyhedron3D, AllplanGeo.Polygon2D]` | create the opening polygon and planes for a Polyhedron opening  Args:     general_ele:    general element     opening_cut_geo: geometry for the opening creation  Returns:     opening created state, bottom plane surface, top plane surface, opening polygon |
| `__get_opening_cut_plane_axis` | `opening_cut_geo: AllplanGeo.Polyhedron3D, outer_element_geo: AllplanGeo.Polygon2D` | `tuple[bool, AllplanGeo.Line3D]` | get the cut plane axis for the creation of the bottom and top plane  Args:     opening_cut_geo:   geometry for the opening creation     outer_element_geo: outer element geometry  Returns:     axis state, opening cut plane axis |
| `__remove_vertical_faces` | `polyhedron: AllplanGeo.Polyhedron3D` | `None` | remove the vertical faces  Args:     polyhedron: polyhedron |
| `__create_plane_surface_from_body` | `cutting_body: AllplanGeo.Polyhedron3D, cut_plane: AllplanGeo.Plane3D` | `None` | create the plane surface from the body  Args:     cutting_body: cutting body     cut_plane:    cutting plane |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the utility for a general opening created by a sloped Polyhedron3D
"""

import math

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Utility as AllplanUtil

from .GeneralOpeningPolygonUtil import GeneralOpeningPolygonUtil

class GeneralOpeningSlopedPolyhedronUtil():
    """" implementation of the utility for a general opening created by a sloped Polyhedron3D
    """

    NEEDED_INTERSECTIONS = 2

    @staticmethod
    def create_opening_polygon_and_plane_surfaces(general_ele    : AllplanEleAdapter.BaseElementAdapter,
                                                  opening_cut_geo: AllplanGeo.Polyhedron3D) -> tuple[bool,
                                                                                                     AllplanGeo.Polyhedron3D,
                                                                                                     AllplanGeo.Polyhedron3D,
                                                                                                     AllplanGeo.Polygon2D]:
        """ create the opening polygon and planes for a Polyhedron opening

        Args:
            general_ele:    general element
            opening_cut_geo: geometry for the opening creation

        Returns:
            opening created state, bottom plane surface, top plane surface, opening polygon
        """

        #----------------- get the geometry of the element from the tiers

        element_geo, outer_element_geo = GeneralOpeningPolygonUtil.get_general_element_geometry(general_ele)

        if element_geo is None or outer_element_geo is None:
            return False, AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polygon2D()


        #----------------- get the opening as intersection body

        intersected, opening = AllplanGeo.Intersect(element_geo, opening_cut_geo)

        if not intersected:
            return False, AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polygon2D()


        #----------------- get the opening cut plane axis

        has_opening_axis, opening_cut_plane_axis = \
            GeneralOpeningSlopedPolyhedronUtil.__get_opening_cut_plane_axis(opening_cut_geo, outer_element_geo)

        if not has_opening_axis:
            return False, AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polygon2D()


        #----------------- calculate the opening polygon

        opening_polygon = GeneralOpeningPolygonUtil.calculate_opening_polygon(opening, opening_cut_plane_axis,
                                                                              outer_element_geo, general_ele)

        if not opening_polygon.IsValid():
            return False, AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polygon2D()


        #----------------- create the cutting plane for the bottom and top surface creation

        axis_polygon = AllplanGeo.Polygon3D()
        axis_polygon += opening_cut_plane_axis.StartPoint
        axis_polygon += opening_cut_plane_axis.EndPoint
        axis_polygon += opening_cut_plane_axis.EndPoint + AllplanGeo.Point3D(0, 0, 1000)
        axis_polygon += opening_cut_plane_axis.StartPoint

        ortho_vec     = axis_polygon.GetPlane()[1].GetVector()
        cut_plane_vec = ortho_vec * AllplanGeo.Vector3D(opening_cut_plane_axis.StartPoint, opening_cut_plane_axis.EndPoint)

        if cut_plane_vec.Z > 0:
            cut_plane_vec.Reverse()

        cut_plane = AllplanGeo.Plane3D(opening_cut_plane_axis.GetCenterPoint(), cut_plane_vec)


        #----------------- get the bottom and top plane surface of the opening
        #                  use the opening cut geometry to avoid numeric problems in the preview calculation

        created, bottom_plane_surface, top_plane_surface = AllplanGeo.CutPolyhedronWithPlane(opening_cut_geo, cut_plane)

        if created:
            if bottom_plane_surface.Type == AllplanGeo.PolyhedronType.tVolume:
                GeneralOpeningSlopedPolyhedronUtil.__create_plane_surface_from_body(bottom_plane_surface, cut_plane)

            if top_plane_surface.Type == AllplanGeo.PolyhedronType.tVolume:
                GeneralOpeningSlopedPolyhedronUtil.__create_plane_surface_from_body(top_plane_surface, cut_plane)

            GeneralOpeningSlopedPolyhedronUtil.__remove_vertical_faces(bottom_plane_surface)
            GeneralOpeningSlopedPolyhedronUtil.__remove_vertical_faces(top_plane_surface)

        return created, bottom_plane_surface, top_plane_surface, opening_polygon


    @staticmethod
    def __get_opening_cut_plane_axis(opening_cut_geo  : AllplanGeo.Polyhedron3D,
                                 outer_element_geo: AllplanGeo.Polygon2D) -> tuple[bool, AllplanGeo.Line3D]:
        """ get the cut plane axis for the creation of the bottom and top plane

        Args:
            opening_cut_geo:   geometry for the opening creation
            outer_element_geo: outer element geometry

        Returns:
            axis state, opening cut plane axis
        """

        dir_angle = None

        z_min_left  = 1.0e10
        z_max_left  = -1.0e10

        max_left_pnt  = None
        max_right_pnt = None


        #----------------- get the coordinates of the axis

        for line in opening_cut_geo.GetEdgesLines()[1]:
            line_2d = AllplanGeo.Line2D(line)

            found, intersection_points = AllplanGeo.IntersectionCalculus(line_2d, outer_element_geo)

            if not found or len(intersection_points) < GeneralOpeningSlopedPolyhedronUtil.NEEDED_INTERSECTIONS:
                continue

            length    = AllplanGeo.CalcLength(line_2d)
            start_vec = AllplanGeo.Vector2D(line_2d.StartPoint, intersection_points[0].To2D)
            end_vec   = AllplanGeo.Vector2D(line_2d.StartPoint, intersection_points[1].To2D)

            line_vec = AllplanGeo.Vector3D(line.StartPoint, line.EndPoint)

            left_point  = line.StartPoint + line_vec * start_vec.GetLength() / length
            right_point = line.StartPoint + line_vec * end_vec.GetLength() / length


            #------------- set the first point

            if dir_angle is None:
                z_min_left  = left_point.Z
                z_max_left  = left_point.Z

                max_left_pnt  = left_point
                max_right_pnt = right_point

                dir_angle = start_vec.GetAngle().Deg

                continue


            #--------------- check for new max and min point

            if abs(dir_angle - start_vec.GetAngle().Deg) > math.pi / 2:
                left_point, right_point = right_point, left_point

            z_min_left = min(z_min_left, left_point.Z)

            if left_point.Z > z_max_left:
                z_max_left    = left_point.Z
                max_left_pnt  = left_point
                max_right_pnt = right_point

        if max_left_pnt is None or max_right_pnt is None:
            return False, AllplanGeo.Line3D()


        #----------------- calculate the axis for the section plane

        dist_axis_vec = AllplanGeo.Vector3D(0, 0, z_max_left - z_min_left) / 2

        return True, AllplanGeo.Line3D(max_left_pnt - dist_axis_vec, max_right_pnt - dist_axis_vec)


    @staticmethod
    def __remove_vertical_faces(polyhedron: AllplanGeo.Polyhedron3D):
        """ remove the vertical faces

        Args:
            polyhedron: polyhedron
        """

        eps = AllplanGeo.GetRelativeTolerance()

        del_faces = AllplanUtil.VecSizeTList()

        for face_index in range(polyhedron.GetFacesCount()):
            if abs(polyhedron.GetNormalVectorOfFace(face_index)[1].Z) < eps:
                del_faces.append(face_index)

        if del_faces:
            polyhedron.DeleteFaces(del_faces)


    @staticmethod
    def __create_plane_surface_from_body(cutting_body: AllplanGeo.Polyhedron3D,
                                         cut_plane   : AllplanGeo.Plane3D):
        """ create the plane surface from the body

        Args:
            cutting_body: cutting body
            cut_plane:    cutting plane
        """

        eps = AllplanGeo.GetRelativeTolerance()

        trans_mat = cut_plane.GetTransformationMatrix()
        trans_mat.Reverse()

        local_cutting_body = AllplanGeo.Transform(cutting_body, trans_mat)

        del_faces = AllplanUtil.VecSizeTList()

        for face_index in range(local_cutting_body.GetFacesCount()):
            normal_vec = local_cutting_body.GetNormalVectorOfFace(face_index)[1]

            if abs(normal_vec.Z) < eps:
                del_faces.append(face_index)
            else:
                is_surface_at_cut_plane = True

                for edge in local_cutting_body.GetFace(face_index).GetEdges():
                    _, start_pnt, end_ptn = local_cutting_body.GetEdgeVertices(edge)

                    if abs(start_pnt.Z) > eps or abs(end_ptn.Z) > eps:
                        is_surface_at_cut_plane = False
                        break

                if is_surface_at_cut_plane:
                    del_faces.append(face_index)

        if del_faces:
            cutting_body.DeleteFaces(del_faces)

```

</details>