---
title: "GeneralOpeningSlopedBRepUtil"
source: "PythonPartsFramework\Utils\Architecture\GeneralOpeningSlopedBRepUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GeneralOpeningSlopedBRepUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\GeneralOpeningSlopedBRepUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the utility for a general opening created by a sloped BRep3D

## Abhängigkeiten

- `GeneralOpeningPolygonUtil`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Utility`
- `math`
- `typing`

## Klassen

### `GeneralOpeningSlopedBRepUtil`

" implementation of the utility for a general opening created by a sloped BRep3D
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_opening_polygons_and_plane_surfaces` | `general_ele: AllplanEleAdapter.BaseElementAdapter, opening_cut_geo: AllplanGeo.BRep3D` | `tuple[bool, AllplanGeo.BRep3D, AllplanGeo.BRep3D, AllplanGeo.Polygon2D]` | create the opening polygon and planes for a Polyhedron opening  Args:     general_ele:     general element     opening_cut_geo: geometry for the opening creation  Returns:     opening created state, bottom plane surface, top plane surface, opening polygon |
| `__get_left_right_face_path` | `opening: AllplanGeo.BRep3D` | `tuple[bool, AllplanGeo.Path3D, AllplanGeo.Path3D]` | get the left and right face path of the opening  Args:     opening: opening body  Returns:     face state, left face path, right face path |
| `__get_face_path` | `boundary_arcs: list[AllplanGeo.Arc3D]` | `tuple[bool, AllplanGeo.Path3D]` | get the face path  Args:     boundary_arcs: boundary arcs  Returns:     found state, face path |
| `__get_face_center` | `face_path: AllplanGeo.Path3D` | `AllplanGeo.Point3D` | get the center of the face  Args:     face_path: fact path  Returns:     center |
| `__get_face_arcs` | `face_path: AllplanGeo.Path3D` | `tuple[AllplanGeo.Arc3D, AllplanGeo.Arc3D]` | get the bottom and top arc of the surface  Args:     face_path: fact path  Returns:     center |
| `__create_plane_surface_from_body` | `cutting_body: AllplanGeo.BRep3D, cut_plane: AllplanGeo.Plane3D` | `None` | create the plane surface from the body  Args:     cutting_body: cutting body     cut_plane:    cutting plane |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the utility for a general opening created by a sloped BRep3D
"""

from typing import cast

import math

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Utility as AllplanUtil

from .GeneralOpeningPolygonUtil import GeneralOpeningPolygonUtil

class GeneralOpeningSlopedBRepUtil():
    """" implementation of the utility for a general opening created by a sloped BRep3D
    """

    NEEDED_ARCS      = 2
    FULL_CIRCLE_TEST = 359

    @staticmethod
    def create_opening_polygons_and_plane_surfaces(general_ele    : AllplanEleAdapter.BaseElementAdapter,
                                                   opening_cut_geo: AllplanGeo.BRep3D) -> tuple[bool,
                                                                                                AllplanGeo.BRep3D,
                                                                                                AllplanGeo.BRep3D,
                                                                                                AllplanGeo.Polygon2D]:
        """ create the opening polygon and planes for a Polyhedron opening

        Args:
            general_ele:     general element
            opening_cut_geo: geometry for the opening creation

        Returns:
            opening created state, bottom plane surface, top plane surface, opening polygon
        """

        error_result = (False, AllplanGeo.BRep3D(), AllplanGeo.BRep3D(), AllplanGeo.Polygon2D())


        #----------------- get the geometry of the element from the tiers

        element_geo, outer_element_geo = GeneralOpeningPolygonUtil.get_general_element_geometry(general_ele)

        if element_geo is None or outer_element_geo is None:
            return error_result

        error, brep_general_geo = AllplanGeo.CreateBRep3D(element_geo)

        if error != AllplanGeo.eGeometryErrorCode.eOK:
            return error_result


        #--------- get the opening as intersection body

        error, opening = AllplanGeo.Intersect(brep_general_geo, opening_cut_geo)

        if error != AllplanGeo.eGeometryErrorCode.eOK or not opening.IsValid():
            return error_result


        #----------------- get the opening cut plane axis

        has_face_path, left_face_path, right_face_path = GeneralOpeningSlopedBRepUtil.__get_left_right_face_path(opening)

        if not has_face_path:
            return error_result

        opening_cut_plane_axis = AllplanGeo.Line3D(GeneralOpeningSlopedBRepUtil.__get_face_center(left_face_path),
                                                   GeneralOpeningSlopedBRepUtil.__get_face_center(right_face_path))


        #----------------- calculate the opening polygon

        opening_polygon = GeneralOpeningPolygonUtil.calculate_opening_polygon(opening, opening_cut_plane_axis,
                                                                              outer_element_geo, general_ele)

        if not opening_polygon.IsValid():
            return error_result


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

        created, bottom_plane_surface, top_plane_surface = AllplanGeo.CutBrepWithPlane(opening_cut_geo, cut_plane)

        if created:
            if bottom_plane_surface.IsClosed():
                GeneralOpeningSlopedBRepUtil.__create_plane_surface_from_body(bottom_plane_surface, cut_plane)

            if top_plane_surface.IsClosed:
                GeneralOpeningSlopedBRepUtil.__create_plane_surface_from_body(top_plane_surface, cut_plane)


        return created, bottom_plane_surface, top_plane_surface, opening_polygon


    @staticmethod
    def __get_left_right_face_path(opening: AllplanGeo.BRep3D) -> tuple[bool, AllplanGeo.Path3D, AllplanGeo.Path3D]:    #NOSONAR
        """ get the left and right face path of the opening

        Args:
            opening: opening body

        Returns:
            face state, left face path, right face path
        """

        boundary_arcs : list[AllplanGeo.Arc3D] = []

        for face_index in range(0, opening.GetFaceCount()):
            error, face_boundary_curves = opening.GetFaceBoundaryCurves(face_index)

            if error != AllplanGeo.eGeometryErrorCode.eOK:
                continue

            for face_boundary_curve in face_boundary_curves:
                if not isinstance(face_boundary_curve, AllplanGeo.Path3D):
                    continue

                for index in range(face_boundary_curve.Count()):
                    geo_ele = face_boundary_curve.GetElement(index)

                    if isinstance(geo_ele, AllplanGeo.Arc3D) and geo_ele not in boundary_arcs:
                        boundary_arcs.append(geo_ele)


        #----------------- get the axis points

        found, left_face_path = GeneralOpeningSlopedBRepUtil.__get_face_path(boundary_arcs)

        if not found:
            return False, AllplanGeo.Path3D(), AllplanGeo.Path3D()

        found, right_face_path = GeneralOpeningSlopedBRepUtil.__get_face_path(boundary_arcs)

        if not found:
            return False, AllplanGeo.Path3D(), AllplanGeo.Path3D()

        return True, left_face_path, right_face_path


    @staticmethod
    def __get_face_path(boundary_arcs: list[AllplanGeo.Arc3D]) -> tuple[bool, AllplanGeo.Path3D]:
        """ get the face path

        Args:
            boundary_arcs: boundary arcs

        Returns:
            found state, face path
        """

        face_path = AllplanGeo.Path3D()
        face_path += boundary_arcs[0]

        del boundary_arcs[0]

        while not face_path.IsClosed():
            found = False

            for index, arc in enumerate(boundary_arcs):
                if face_path.Add(arc) == AllplanGeo.eGeometryErrorCode.eOK:
                    del boundary_arcs[index]

                    found = True

                    break

            if not found:
                return False, AllplanGeo.Path3D()

        return True, face_path


    @staticmethod
    def __get_face_center(face_path: AllplanGeo.Path3D) -> AllplanGeo.Point3D:
        """ get the center of the face

        Args:
            face_path: fact path

        Returns:
            center
        """

        bottom_arc, top_arc = GeneralOpeningSlopedBRepUtil.__get_face_arcs(face_path)

        bottom_pnt = bottom_arc.GetPoint(AllplanGeo.Angle(math.pi * 3 / 2))
        top_pnt    = top_arc.GetPoint(AllplanGeo.Angle(math.pi / 2))

        return (bottom_pnt + top_pnt) / 2


    @staticmethod
    def __get_face_arcs(face_path: AllplanGeo.Path3D) -> tuple[AllplanGeo.Arc3D, AllplanGeo.Arc3D]:
        """ get the bottom and top arc of the surface

        Args:
            face_path: fact path

        Returns:
            center
        """

        z_bottom = 1.0e10
        z_top = -1.0e10

        bottom_arc = AllplanGeo.Arc3D()
        top_arc    = AllplanGeo.Arc3D()


        #----------------- get the face center from the arcs of the surface path

        for index in range(face_path.Count()):
            min_max, _ = AllplanGeo.CalcMinMax(face_path.GetElement(index))

            if (z_min := min_max.GetMin().Z) < z_bottom:
                z_bottom   = z_min
                bottom_arc = cast(AllplanGeo.Arc3D, face_path.GetElement(index))

            if (z_max := min_max.GetMax().Z) > z_top:
                z_top   = z_max
                top_arc = cast(AllplanGeo.Arc3D, face_path.GetElement(index))

        return bottom_arc, top_arc


    @staticmethod
    def __create_plane_surface_from_body(cutting_body: AllplanGeo.BRep3D,
                                         cut_plane   : AllplanGeo.Plane3D):
        """ create the plane surface from the body

        Args:
            cutting_body: cutting body
            cut_plane:    cutting plane
        """

        trans_mat = cut_plane.GetTransformationMatrix()
        trans_mat.Reverse()

        local_cutting_body = AllplanGeo.Transform(cutting_body, trans_mat)

        del_faces = AllplanUtil.VecULongList()

        for face_index in range(local_cutting_body.GetFaceCount()):
            line_count = 0
            arc_count  = 0

            for path in local_cutting_body.GetFaceBoundaryCurves(face_index)[1]:
                for index in range(path.Count()):
                    ele = path.GetElement(index)

                    if isinstance(ele, AllplanGeo.Line3D):
                        line_count += 1

                    if isinstance(ele, AllplanGeo.Arc3D):
                        arc_count += 1

            if line_count == 4 or line_count == 1 and arc_count == 1:
                del_faces.append(face_index)

        if del_faces:
            cutting_body.DeleteFaces(del_faces)

```

</details>