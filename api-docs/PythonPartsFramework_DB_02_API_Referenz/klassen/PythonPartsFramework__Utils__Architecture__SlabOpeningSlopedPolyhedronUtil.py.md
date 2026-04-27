---
title: "SlabOpeningSlopedPolyhedronUtil"
source: "PythonPartsFramework\Utils\Architecture\SlabOpeningSlopedPolyhedronUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# SlabOpeningSlopedPolyhedronUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\SlabOpeningSlopedPolyhedronUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the utility for a slab opening created by a sloped Polyhedron3D

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Utility`

## Klassen

### `SlabOpeningSlopedPolyhedronUtil`

" implementation of the utility for a slab opening created by a sloped Polyhedron3D
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, document: AllplanEleAdapter.DocumentAdapter` | `None` | initialize  Args:     document: document |
| `create_opening_polygons_and_plane_surfaces` | `self, slab: AllplanEleAdapter.BaseElementAdapter, opening_cut_geo: AllplanGeo.Polyhedron3D` | `tuple[bool, AllplanGeo.Polygon2D, AllplanGeo.Polyhedron3D | None, AllplanGeo.Polyhedron3D | None]` | create the opening polygons and planes for a Polyhedron opening  Args:     slab:            slab     opening_cut_geo: geometry for the opening creation  Returns:     opening created state, opening polygon, bottom plane surface, top plane surface |
| `__get_bottom_top_face` | `opening: AllplanGeo.Polyhedron3D` | `tuple[int, int, AllplanGeo.Polygon3D, AllplanGeo.Polygon3D]` | get the index of the bottom and top face  Args:     opening: opening body  Returns:     bottom and top face index, bottom and top face polygon |
| `__get_bottom_top_face_from_volume` | `opening: AllplanGeo.Polyhedron3D` | `tuple[int, int, AllplanGeo.Polygon3D, AllplanGeo.Polygon3D]` | get the bottom and top face data  Args:     opening: opening body  Returns:     bottom and top face index, bottom and top face polygon |
| `__get_bottom_top_face_from_surface` | `opening: AllplanGeo.Polyhedron3D` | `tuple[AllplanGeo.Polygon3D, AllplanGeo.Polygon3D]` | get the bottom and top face data  Args:     opening: opening body  Returns:     bottom and top face polygon |
| `__get_face_polygon_from_lines` | `lines: list[AllplanGeo.Line3D]` | `AllplanGeo.Polygon3D` | get the face polygon from the boundary lines  Args:     lines: face lines  Returns:     face polygon |
| `__get_opening_slopes` | `opening: AllplanGeo.Polyhedron3D, bottom_face_index: int, top_face_index: int, bottom_face_polygon: AllplanGeo.Polygon3D, top_face_polygon: AllplanGeo.Polygon3D` | `tuple[bool, AllplanGeo.Polyhedron3D, AllplanGeo.Polyhedron3D]` | get the opening slopes  Args:     opening:             opening body     bottom_face_index:   bottom face index     top_face_index:      top face index     bottom_face_polygon: bottom face polygon     top_face_polygon:    top face polygon  Returns:     slopes created, lef slope, right slope |
| `__remove_vertical_faces` | `polyhedron: AllplanGeo.Polyhedron3D` | `None` | remove the vertical faces  Args:     polyhedron: polyhedron |
| `__get_opening_polygon_for_polyhedron_body` | `bottom_face_polygon: AllplanGeo.Polygon3D, top_face_polygon: AllplanGeo.Polygon3D` | `AllplanGeo.Polygon2D` | get the opening polygon for an opening created by a Polyhedron surface  Args:     bottom_face_polygon: bottom face polygon     top_face_polygon:    top face polygon  Returns:     opening: opening polygon, direction line |
| `__get_polyhedron_face` | `polyhedron: AllplanGeo.Polyhedron3D, face_index: int` | `AllplanGeo.Polygon3D` | get a Polyhedron face  Args:     polyhedron: Polyhedron     face_index: face index  Returns:     Polyhedron face as polygon |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the utility for a slab opening created by a sloped Polyhedron3D
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Utility as AllplanUtil

class SlabOpeningSlopedPolyhedronUtil():
    """" implementation of the utility for a slab opening created by a sloped Polyhedron3D
    """

    def __init__(self,
                 document: AllplanEleAdapter.DocumentAdapter):
        """ initialize

        Args:
            document: document
        """

        self.document = document


    def create_opening_polygons_and_plane_surfaces(self,
                                                   slab           : AllplanEleAdapter.BaseElementAdapter,
                                                   opening_cut_geo: AllplanGeo.Polyhedron3D) -> tuple[bool,
                                                                                                      AllplanGeo.Polygon2D,
                                                                                                      (AllplanGeo.Polyhedron3D  | None),
                                                                                                      (AllplanGeo.Polyhedron3D  | None)]:
        """ create the opening polygons and planes for a Polyhedron opening

        Args:
            slab:            slab
            opening_cut_geo: geometry for the opening creation

        Returns:
            opening created state, opening polygon, bottom plane surface, top plane surface
        """

        polyhedron_slab_geo = slab.GetModelGeometry()


        #----------------- get the opening as intersection body

        intersected, opening = AllplanGeo.Intersect(polyhedron_slab_geo, opening_cut_geo)

        if not intersected:
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()


        #----------------- get the opening polygon

        bottom_face_index, top_face_index, bottom_face_polygon, top_face_polygon = \
            SlabOpeningSlopedPolyhedronUtil.__get_bottom_top_face(opening)

        if not bottom_face_polygon.IsValid() or not top_face_polygon.IsValid():
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()

        opening_polygon = self.__get_opening_polygon_for_polyhedron_body(bottom_face_polygon, top_face_polygon)

        if not opening_polygon.IsValid():
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()


        #----------------- get the slopes

        if AllplanGeo.Comparison.Equal(AllplanGeo.CenterCalculus.Calculate(bottom_face_polygon, True, 0)[1].To2D,
                                       AllplanGeo.CenterCalculus.Calculate(top_face_polygon, True, 0)[1].To2D,
                                       AllplanGeo.GetAbsoluteTolerance()):
            return True, opening_polygon, None, None

        has_slopes, left_slope, right_slope = self.__get_opening_slopes(opening, bottom_face_index, top_face_index,
                                                                        bottom_face_polygon, top_face_polygon)

        if not has_slopes:
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()

        self.__remove_vertical_faces(left_slope)
        self.__remove_vertical_faces(right_slope)


        #------------------- create the bottom and te top plane surface

        _, bottom_surface = AllplanGeo.CreatePolyhedron(bottom_face_polygon)
        _, top_surface    = AllplanGeo.CreatePolyhedron(top_face_polygon)


        #----------------- unite the slope and the parallel surface

        _, bottom_surface = AllplanGeo.MakeUnion(bottom_surface, right_slope)
        _, top_surface    = AllplanGeo.MakeUnion(top_surface, left_slope)

        return True, opening_polygon, bottom_surface, top_surface


    @staticmethod
    def __get_bottom_top_face(opening: AllplanGeo.Polyhedron3D) -> tuple[int, int,
                                                                         AllplanGeo.Polygon3D, AllplanGeo.Polygon3D]:
        """ get the index of the bottom and top face

        Args:
            opening: opening body

        Returns:
            bottom and top face index, bottom and top face polygon
        """

        if opening.GetType() == AllplanGeo.PolyhedronType.tVolume:
            return SlabOpeningSlopedPolyhedronUtil.__get_bottom_top_face_from_volume(opening)

        return -1, -1, *SlabOpeningSlopedPolyhedronUtil.__get_bottom_top_face_from_surface(opening)


    @staticmethod
    def __get_bottom_top_face_from_volume(opening: AllplanGeo.Polyhedron3D) -> tuple[int, int,
                                                                                     AllplanGeo.Polygon3D, AllplanGeo.Polygon3D]:
        """ get the bottom and top face data

        Args:
            opening: opening body

        Returns:
            bottom and top face index, bottom and top face polygon
        """

        min_max = AllplanGeo.CalcMinMax(opening)[0]

        z_bottom = min_max.Min.Z
        z_top    = min_max.Max.Z

        bottom_index = -1
        top_index    = -1

        for face_index in range(opening.GetFacesCount()):
            polygon = SlabOpeningSlopedPolyhedronUtil.__get_polyhedron_face(opening, face_index)

            if next((False for pnt in polygon.Points if abs(pnt.Z - z_bottom) > 1), True):
                bottom_index = face_index

            if next((False for pnt in polygon.Points if abs(pnt.Z - z_top) > 1), True):
                top_index = face_index

            if bottom_index != -1 and top_index != -1:
                return bottom_index, top_index, \
                       SlabOpeningSlopedPolyhedronUtil.__get_polyhedron_face(opening, bottom_index), \
                       SlabOpeningSlopedPolyhedronUtil.__get_polyhedron_face(opening, top_index)

        return bottom_index, top_index, AllplanGeo.Polygon3D(), AllplanGeo.Polygon3D()


    @staticmethod
    def __get_bottom_top_face_from_surface(opening: AllplanGeo.Polyhedron3D) -> tuple[AllplanGeo.Polygon3D, AllplanGeo.Polygon3D]:
        """ get the bottom and top face data

        Args:
            opening: opening body

        Returns:
            bottom and top face polygon
        """

        min_max = AllplanGeo.CalcMinMax(opening)[0]

        z_bottom = min_max.Min.Z
        z_top    = min_max.Max.Z


        #----------------- get the bottom and top lines

        bottom_lines: list[AllplanGeo.Line3D] = []
        top_lines   : list[AllplanGeo.Line3D] = []

        for line in opening.GetEdgesLines()[1]:
            if abs(line.StartPoint.Z - z_bottom) < 1. and abs(line.EndPoint.Z - z_bottom) < 1.:
                bottom_lines.append(line)

            if abs(line.StartPoint.Z - z_top) < 1. and abs(line.EndPoint.Z - z_top) < 1.:
                top_lines.append(line)


        #----------------- create the bottom face polygon

        bottom_face_polygon = SlabOpeningSlopedPolyhedronUtil.__get_face_polygon_from_lines(bottom_lines)

        if bottom_face_polygon.GetPlane()[1].GetVector().Z > 0.1:
            bottom_face_polygon.Reverse()

        top_face_polygon = SlabOpeningSlopedPolyhedronUtil.__get_face_polygon_from_lines(top_lines)

        if top_face_polygon.GetPlane()[1].GetVector().Z < -0.1:
            top_face_polygon.Reverse()

        return bottom_face_polygon, top_face_polygon


    @staticmethod
    def __get_face_polygon_from_lines(lines: list[AllplanGeo.Line3D]) -> AllplanGeo.Polygon3D:
        """ get the face polygon from the boundary lines

        Args:
            lines: face lines

        Returns:
            face polygon
        """

        #----------------- create the top face polygon

        face_polygon = AllplanGeo.Polygon3D()
        face_polygon += lines[0].StartPoint
        face_polygon += lines[0].EndPoint

        del lines[0]

        while face_polygon.StartPoint != face_polygon.EndPoint:
            for index, line in enumerate(lines):
                if line.StartPoint == face_polygon.EndPoint:
                    face_polygon += line.EndPoint
                    del lines[index]
                    break

                if line.EndPoint == face_polygon.EndPoint:
                    face_polygon += line.StartPoint
                    del lines[index]
                    break

        return face_polygon


    @staticmethod
    def __get_opening_slopes(opening            : AllplanGeo.Polyhedron3D,
                             bottom_face_index  : int,
                             top_face_index     : int,
                             bottom_face_polygon: AllplanGeo.Polygon3D,
                             top_face_polygon   : AllplanGeo.Polygon3D) -> tuple[bool, AllplanGeo.Polyhedron3D, AllplanGeo.Polyhedron3D]:
        """ get the opening slopes

        Args:
            opening:             opening body
            bottom_face_index:   bottom face index
            top_face_index:      top face index
            bottom_face_polygon: bottom face polygon
            top_face_polygon:    top face polygon

        Returns:
            slopes created, lef slope, right slope
        """

        _, bottom_center = AllplanGeo.CenterCalculus.Calculate(bottom_face_polygon, True, 0)
        _, top_center    = AllplanGeo.CenterCalculus.Calculate(top_face_polygon, True, 0)


        #----------------- create a cut plane to get the left and right slope

        axis_polygon = AllplanGeo.Polygon3D([bottom_center, top_center, AllplanGeo.Point3D(top_center.X, top_center.Y, 0)])

        normal_vec = AllplanGeo.Vector3D(bottom_center, top_center) * axis_polygon.GetPlane()[1].GetVector()

        if normal_vec.Z < 0:
            normal_vec.Reverse()

        cut_plane = AllplanGeo.Plane3D(bottom_center, normal_vec)


        #----------------- get the slopes

        opening_surface = AllplanGeo.Polyhedron3D(opening)

        if bottom_face_index != -1:
            opening_surface.DeleteFaces(AllplanUtil.VecSizeTList([bottom_face_index, top_face_index]))

        has_slopes, left_slope, right_slope = AllplanGeo.CutPolyhedronWithPlane(opening_surface, cut_plane)

        if has_slopes:
            SlabOpeningSlopedPolyhedronUtil.__remove_vertical_faces(left_slope)
            SlabOpeningSlopedPolyhedronUtil.__remove_vertical_faces(right_slope)

        return has_slopes, left_slope, right_slope


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
    def __get_opening_polygon_for_polyhedron_body(bottom_face_polygon: AllplanGeo.Polygon3D,
                                                  top_face_polygon   : AllplanGeo.Polygon3D) -> AllplanGeo.Polygon2D:
        """ get the opening polygon for an opening created by a Polyhedron surface

        Args:
            bottom_face_polygon: bottom face polygon
            top_face_polygon:    top face polygon

        Returns:
            opening: opening polygon, direction line
        """

        _, bottom_polygon = AllplanGeo.ConvertTo2D(bottom_face_polygon)
        _, top_polygon    = AllplanGeo.ConvertTo2D(top_face_polygon)

        if AllplanGeo.Comparison.Equal(AllplanGeo.CenterCalculus.Calculate(bottom_polygon, True, 0)[1],
                                       AllplanGeo.CenterCalculus.Calculate(top_polygon, True, 0)[1],
                                       AllplanGeo.GetAbsoluteTolerance()):
            return bottom_polygon

        error, opening_polygon = AllplanGeo.MakeUnion(bottom_polygon, top_polygon)

        if error != AllplanGeo.eGeometryErrorCode.eOK:
            return AllplanGeo.Polygon2D()


        #----------------- remove the intersection points

        intersected, intersect_pnts = AllplanGeo.IntersectionCalculus(bottom_polygon, top_polygon)

        if not intersected:
            return opening_polygon

        eps = AllplanGeo.GetAbsoluteTolerance()

        for pnt in intersect_pnts:
            pnt_2d = pnt.To2D

            for index, pol_pnt in enumerate(opening_polygon.Points):
                if AllplanGeo.Comparison.Equal(pnt_2d, pol_pnt, eps):
                    opening_polygon.Remove(index)
                    break

        return opening_polygon



    @staticmethod
    def __get_polyhedron_face(polyhedron: AllplanGeo.Polyhedron3D,
                              face_index: int) -> AllplanGeo.Polygon3D:
        """ get a Polyhedron face

        Args:
            polyhedron: Polyhedron
            face_index: face index

        Returns:
            Polyhedron face as polygon
        """

        polygon = AllplanGeo.Polygon3D()

        polyhedron_face = polyhedron.GetFace(face_index)

        for edge in  polyhedron_face.GetEdges():
            _, start_vertex, end_vertex = polyhedron.GetEdgeVertices(edge)

            if polygon.Count() == 0:
                polygon += start_vertex

            polygon += end_vertex

        return polygon

```

</details>