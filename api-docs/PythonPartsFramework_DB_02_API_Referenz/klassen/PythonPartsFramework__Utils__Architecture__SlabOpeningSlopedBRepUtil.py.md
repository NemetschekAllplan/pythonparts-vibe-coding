---
title: "SlabOpeningSlopedBRepUtil"
source: "PythonPartsFramework\Utils\Architecture\SlabOpeningSlopedBRepUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# SlabOpeningSlopedBRepUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\SlabOpeningSlopedBRepUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the utility for a slab opening created by a sloped BRep3D

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Utility`
- `math`
- `typing`

## Klassen

### `SlabOpeningSlopedBRepUtil`

" implementation of the utility for a slab opening created by a sloped BRep3D
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, document: AllplanEleAdapter.DocumentAdapter` | `None` | initialize  Args:     document: document |
| `create_opening_polygons_and_plane_surfaces` | `self, slab: AllplanEleAdapter.BaseElementAdapter, opening_cut_geo: AllplanGeo.BRep3D` | `tuple[bool, AllplanGeo.Polygon2D, AllplanGeo.Polyhedron3D | None, AllplanGeo.Polyhedron3D | None]` | create the opening polygons and planes for a BRep opening  Args:     slab:            slab     opening_cut_geo: geometry for the opening creation  Returns:     opening created state, opening polygon, bottom plane surface, top plane surface |
| `__get_opening_polygon_for_brep_body` | `self, bottom_arc: AllplanGeo.Arc3D, top_arc: AllplanGeo.Arc3D` | `tuple[AllplanGeo.Polygon2D, AllplanGeo.Vector3D, AllplanGeo.Point3D]` | get the full opening polygon for an opening created by a BRep body  Args:     bottom_arc: bottom arc of the opening     top_arc:    top arc of the opening  Returns:     opening: opening polygon, opening direction vector, opening center point |
| `__get_brep_opening_arcs` | `opening: AllplanGeo.BRep3D` | `tuple[AllplanGeo.Arc3D | None, AllplanGeo.Arc3D | None]` | get the bottom and top arc of the -BRep opening  Args:     opening: opening body  Returns:     bottom arc, top arc |
| `__create_opening_polyhedron_plane_sufaces` | `self, bottom_arc: AllplanGeo.Arc3D, top_arc: AllplanGeo.Arc3D` | `tuple[AllplanGeo.Polyhedron3D, AllplanGeo.Polyhedron3D]` | create the opening Polyhedron planes from the BRep opening  Args:     bottom_arc: bottom arc of the opening     top_arc:    top arc of the opening  Returns:     bottom plane surface, top plane surface |
| `__create_polyhedron_from_slope_polygon` | `slope_polyline: AllplanGeo.Polyline3D` | `AllplanGeo.Polyhedron3D` | create a slope polyhedron  Args:     slope_polyline: slope polyline  Returns:     slope polyhedron |
| `__create_opening_brep_plane_surfaces` | `self, opening: AllplanGeo.BRep3D, opening_center_point: AllplanGeo.Point3D, opening_dir_vec: AllplanGeo.Vector3D` | `tuple[AllplanGeo.BRep3D, AllplanGeo.BRep3D]` | create the opening BRep planes  Args:     opening:              opening body     opening_center_point: opening center     opening_dir_vec:      opening direction vector  Returns:     bottom plane surface, top plane surface |
| `__create_rectangular_top_surface` | `opening: AllplanGeo.BRep3D` | `AllplanGeo.BRep3D` | create a rectangular surface for the top reference plane  Args:     opening: opening body  Returns:     top surface |
| `__create_rectangular_bottom_surface` | `opening: AllplanGeo.BRep3D` | `AllplanGeo.BRep3D` | create a rectangular surface for the bottom reference plane  Args:     opening: opening body  Returns:     bottom surface |
| `__create_rectangular_bottom_offset_surface` | `bottom_surface: AllplanGeo.BRep3D` | `AllplanGeo.BRep3D` | create a rectangular offset surface for the bottom reference plane  Args:     bottom_surface: bottom surface  Returns:     top surface |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the utility for a slab opening created by a sloped BRep3D
"""

# pylint: disable=unused-private-member

from typing import cast

import math

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Utility as AllplanUtil

class SlabOpeningSlopedBRepUtil():
    """" implementation of the utility for a slab opening created by a sloped BRep3D
    """

    NEEDED_ARCS      = 2
    FULL_CIRCLE_TEST = 359

    def __init__(self,
                 document: AllplanEleAdapter.DocumentAdapter):
        """ initialize

        Args:
            document: document
        """

        self.document = document

        self.opening_division = 36 # must create a point a each coordinate axis point to have the same points
        self.slope_division   = 18 # for the opening polygon and the opening slopes


    def create_opening_polygons_and_plane_surfaces(self,
                                                   slab           : AllplanEleAdapter.BaseElementAdapter,
                                                   opening_cut_geo: AllplanGeo.BRep3D) -> tuple[bool,
                                                                                                AllplanGeo.Polygon2D,
                                                                                                (AllplanGeo.Polyhedron3D | None),
                                                                                                (AllplanGeo.Polyhedron3D | None)]:
        """ create the opening polygons and planes for a BRep opening

        Args:
            slab:            slab
            opening_cut_geo: geometry for the opening creation

        Returns:
            opening created state, opening polygon, bottom plane surface, top plane surface
        """

        error, brep_slab_geo = AllplanGeo.CreateBRep3D(slab.GetModelGeometry())

        if error != AllplanGeo.eGeometryErrorCode.eOK:
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()


        #--------- get the opening as intersection body

        error, opening = AllplanGeo.Intersect(brep_slab_geo, opening_cut_geo)

        if error != AllplanGeo.eGeometryErrorCode.eOK or not opening.IsValid():
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()


        #----------------- get the bottom and top arc of the opening

        bottom_arc, top_arc = self.__get_brep_opening_arcs(opening)

        if bottom_arc is None or top_arc is None:
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()


        #----------------- get the opening polygon

        opening_polygon, _opening_dir_vec, _opening_center_point = self.__get_opening_polygon_for_brep_body(bottom_arc, top_arc)

        if not opening_polygon.IsValid():
            return False, AllplanGeo.Polygon2D(), AllplanGeo.Polyhedron3D(), AllplanGeo.Polyhedron3D()


        #------------------- create the plane surfaces

        if AllplanGeo.Comparison.Equal(bottom_arc.GetCenter().To2D, top_arc.GetCenter().To2D, AllplanGeo.GetRelativeTolerance()):
            return True, opening_polygon, None, None

        #bottom_surface, top_surface = self.__create_opening_brep_plane_surfaces(opening, _opening_center_point, _opening_dir_vec)

        bottom_surface, top_surface = self.__create_opening_polyhedron_plane_sufaces(bottom_arc, top_arc)

        return True, opening_polygon, bottom_surface, top_surface


    def __get_opening_polygon_for_brep_body(self,
                                            bottom_arc: AllplanGeo.Arc3D,
                                            top_arc   : AllplanGeo.Arc3D) -> tuple[AllplanGeo.Polygon2D,
                                                                                   AllplanGeo.Vector3D, AllplanGeo.Point3D]:
        """ get the full opening polygon for an opening created by a BRep body

        Args:
            bottom_arc: bottom arc of the opening
            top_arc:    top arc of the opening

        Returns:
            opening: opening polygon, opening direction vector, opening center point
        """

        #----------------- vertical opening

        if AllplanGeo.Comparison.Equal(bottom_arc.GetCenter().To2D, top_arc.GetCenter().To2D, AllplanGeo.GetRelativeTolerance()):
            opening_polygon = AllplanGeo.ConvertTo2D(AllplanGeo.Polygonize(bottom_arc, self.slope_division))[1]

            return AllplanGeo.Polygon2D(opening_polygon.Points), AllplanGeo.Vector3D(), AllplanGeo.Point3D()


        #----------------- get the opening polygon from the bottom ellipse

        opening_dir_vec = bottom_arc.GetXAxis() * -1

        bottom_arc = AllplanGeo.Arc3D(bottom_arc.GetCenter(), bottom_arc.GetXAxis(), AllplanGeo.Vector3D(0, 0, 1000),
                                      bottom_arc.GetMinorRadius(), bottom_arc.GetMajorRadius(), math.pi / 2, math.pi)

        _, bottom_arc_polygon = AllplanGeo.ConvertTo2D(AllplanGeo.Polygonize(bottom_arc, self.slope_division))


        #----------------- get the opening polygon from the top ellipse

        top_arc = AllplanGeo.Arc3D(top_arc.GetCenter(), top_arc.GetXAxis(), AllplanGeo.Vector3D(0, 0, 1000),
                                   top_arc.GetMinorRadius(), top_arc.GetMajorRadius(), math.pi * 3 / 2, math.pi)

        top_arc_polygon = AllplanGeo.Polygonize(top_arc, self.slope_division)


        #----------------- create the full opening polygon

        opening_polygon = AllplanGeo.Polygon2D(bottom_arc_polygon.Points)

        for pnt in top_arc_polygon.Points:
            opening_polygon += pnt.To2D

        opening_polygon += opening_polygon.StartPoint

        return opening_polygon, opening_dir_vec, (bottom_arc.GetCenter() + top_arc.GetCenter()) / 2


    @staticmethod
    def __get_brep_opening_arcs(opening: AllplanGeo.BRep3D) -> tuple[(AllplanGeo.Arc3D  | None), (AllplanGeo.Arc3D | None)]: # NOSONAR
        """ get the bottom and top arc of the -BRep opening

        Args:
            opening: opening body

        Returns:
            bottom arc, top arc
        """

        bottom_arc = None
        top_arc    = None

        for face_index in range(0, opening.GetFaceCount()):
            error, face_boundary_curves = opening.GetFaceBoundaryCurves(face_index)

            if error != AllplanGeo.eGeometryErrorCode.eOK:
                continue

            for face_boundary_curve in face_boundary_curves:
                if not isinstance(face_boundary_curve, AllplanGeo.Path3D):
                    continue

                for index in range(face_boundary_curve.Count()):
                    geo_ele = face_boundary_curve.GetElement(index)

                    if isinstance(geo_ele, AllplanGeo.Arc3D) and \
                       abs(cast(AllplanGeo.Arc3D, geo_ele).GetDeltaAngle().Deg) > SlabOpeningSlopedBRepUtil.FULL_CIRCLE_TEST:
                        if bottom_arc is None or geo_ele.GetCenter().Z < bottom_arc.GetCenter().Z:
                            bottom_arc = geo_ele

                        if top_arc is None or geo_ele.GetCenter().Z > top_arc.GetCenter().Z:
                            top_arc = geo_ele

        return bottom_arc, top_arc


    def __create_opening_polyhedron_plane_sufaces(self,
                                                  bottom_arc: AllplanGeo.Arc3D,
                                                  top_arc   : AllplanGeo.Arc3D) -> tuple[AllplanGeo.Polyhedron3D, AllplanGeo.Polyhedron3D]:
        """ create the opening Polyhedron planes from the BRep opening

        Args:
            bottom_arc: bottom arc of the opening
            top_arc:    top arc of the opening

        Returns:
            bottom plane surface, top plane surface
        """

        #------------- get the left opening slope

        arc = AllplanGeo.Arc3D(bottom_arc.GetCenter(), bottom_arc.GetXAxis(), AllplanGeo.Vector3D(0, 0, 1000),
                               bottom_arc.GetMinorRadius(), bottom_arc.GetMajorRadius(), math.pi / 2, math.pi)

        bottom_polyline = AllplanGeo.Polygonize(arc, self.slope_division)

        arc = AllplanGeo.Arc3D(top_arc.GetCenter(), top_arc.GetXAxis(), AllplanGeo.Vector3D(0, 0, 1000),
                               top_arc.GetMinorRadius(), top_arc.GetMajorRadius(), math.pi / 2, math.pi)

        top_polyline = AllplanGeo.Polygonize(arc, self.slope_division)

        top_polyline.Reverse()

        left_slope_polyline = AllplanGeo.Polyline3D(bottom_polyline)
        left_slope_polyline += top_polyline


        #------------- get the right opening slope

        arc = AllplanGeo.Arc3D(bottom_arc.GetCenter(), bottom_arc.GetXAxis(), AllplanGeo.Vector3D(0, 0, 1000),
                               bottom_arc.GetMinorRadius(), bottom_arc.GetMajorRadius(), math.pi / 2 * 3, math.pi)

        bottom_polyline = AllplanGeo.Polygonize(arc, self.slope_division)

        arc = AllplanGeo.Arc3D(top_arc.GetCenter(), top_arc.GetXAxis(), AllplanGeo.Vector3D(0, 0, 1000),
                               top_arc.GetMinorRadius(), top_arc.GetMajorRadius(), math.pi / 2 * 3, math.pi)

        top_polyline = AllplanGeo.Polygonize(arc, self.slope_division)
        top_polyline.Reverse()

        right_slope_polyline = AllplanGeo.Polyline3D(bottom_polyline)
        right_slope_polyline += top_polyline


        #----------------- build the slope faces

        left_slope  = self.__create_polyhedron_from_slope_polygon(left_slope_polyline)
        right_slope = self.__create_polyhedron_from_slope_polygon(right_slope_polyline)


        #----------------- get the bottom and top opening plane surfaces

        bottom_polyline = AllplanGeo.Polygonize(bottom_arc, self.opening_division)
        top_polyline    = AllplanGeo.Polygonize(top_arc, self.opening_division)

        bottom_polygon = AllplanGeo.Polygon3D(bottom_polyline.Points)
        top_polygon    = AllplanGeo.Polygon3D(top_polyline.Points)

        _, bottom_surface = AllplanGeo.CreatePolyhedron(bottom_polygon)
        _, top_surface    = AllplanGeo.CreatePolyhedron(top_polygon)


        #----------------- unite the slope and the parallel surface

        _, bottom_surface = AllplanGeo.MakeUnion(bottom_surface,right_slope)
        _, top_surface    = AllplanGeo.MakeUnion(top_surface, left_slope)

        return bottom_surface, top_surface


    @staticmethod
    def __create_polyhedron_from_slope_polygon(slope_polyline: AllplanGeo.Polyline3D) -> AllplanGeo.Polyhedron3D:
        """ create a slope polyhedron

        Args:
            slope_polyline: slope polyline

        Returns:
            slope polyhedron
        """

        slope = AllplanGeo.Polyhedron3D()

        slope_builder = AllplanGeo.Polyhedron3DBuilder(slope)
        slope.SetType(AllplanGeo.PolyhedronType.tFaces)


        #----------------- add the vertices

        for pnt in slope_polyline.Points:
            slope_builder.AppendVertex(pnt)


        #----------------- create the edges

        for pnt_index in range(0, slope_polyline.Count() - 1):
            slope.AppendEdge(AllplanGeo.GeometryEdge(pnt_index, pnt_index + 1))

        slope.AppendEdge(AllplanGeo.GeometryEdge(slope_polyline.Count() - 1, 0))

        end_index = slope_polyline.Count() - 2

        for pnt_index in range(1, int((slope_polyline.Count() - 2) / 2)):
            slope.AppendEdge(AllplanGeo.GeometryEdge(pnt_index, end_index))

            end_index -= 1


        #----------------- create the faces

        start_vert_edge = slope_polyline.Count() - 1

        orientation = True

        end_index = int((slope_polyline.Count() - 2) / 2)

        for edge_index in range(0, end_index):
            face = slope.CreateFace(4)
            face.AppendEdge(edge_index, True)

            if edge_index == end_index - 1:
                face.AppendEdge(edge_index + 1, orientation)
            else:
                face.AppendEdge(start_vert_edge + edge_index + 1, orientation)

            face.AppendEdge(start_vert_edge - edge_index - 1, True)
            face.AppendEdge(start_vert_edge + edge_index, True)

            orientation = False

        slope_builder.Complete()

        return slope


    #---------------------------------- the direct use of the BRep slopes as planes creates wrong opening geometry ------------------------


    def __create_opening_brep_plane_surfaces(self,
                                             opening             : AllplanGeo.BRep3D,
                                             opening_center_point: AllplanGeo.Point3D,
                                             opening_dir_vec     : AllplanGeo.Vector3D) -> tuple[AllplanGeo.BRep3D, AllplanGeo.BRep3D]:
        """ create the opening BRep planes

        Args:
            opening:              opening body
            opening_center_point: opening center
            opening_dir_vec:      opening direction vector

        Returns:
            bottom plane surface, top plane surface
        """

        slope = AllplanGeo.BRep3D(opening)
        slope.DeleteFaces(AllplanUtil.VecULongList([1, 2]))

        cut_plane = AllplanGeo.Plane3D(opening_center_point, opening_dir_vec)

        _, left_slope, right_slope = AllplanGeo.CutBrepWithPlane(slope, cut_plane)

        top_surface = AllplanGeo.BRep3D(opening)
        top_surface.DeleteFaces(AllplanUtil.VecULongList([0, 1]))

        bottom_surface = AllplanGeo.BRep3D(opening)
        bottom_surface.DeleteFaces(AllplanUtil.VecULongList([0, 2]))


        #--------- modify the surfaces for the plane (try to solve geometry problems)

        top_surface    = self.__create_rectangular_top_surface(opening)
        #bottom_surface = self.__create_rectangular_bottom_surface(opening)
        #bottom_surface = self.__create_rectangular_bottom_offset_surface(bottom_surface)


        #--------- unite the slope and the parallel surface

        _, top_surface    = AllplanGeo.MakeUnion(top_surface, left_slope)
        _, bottom_surface = AllplanGeo.MakeUnion(bottom_surface,right_slope)


        #--------- create the planes

        return bottom_surface, top_surface


    @staticmethod
    def __create_rectangular_top_surface(opening: AllplanGeo.BRep3D) -> AllplanGeo.BRep3D:
        """ create a rectangular surface for the top reference plane

        Args:
            opening: opening body

        Returns:
            top surface
        """

        top_min_max = AllplanGeo.CalcMinMax(opening)[0]

        z_top = top_min_max.Max.Z

        top_min_max.Inflate(100)

        top_polygon = AllplanGeo.Polygon3D()
        top_polygon += AllplanGeo.Point3D(top_min_max.Min.X, top_min_max.Min.Y, z_top)
        top_polygon += AllplanGeo.Point3D(top_min_max.Max.X, top_min_max.Min.Y, z_top)
        top_polygon += AllplanGeo.Point3D(top_min_max.Max.X, top_min_max.Max.Y, z_top)
        top_polygon += AllplanGeo.Point3D(top_min_max.Min.X, top_min_max.Max.Y, z_top)
        top_polygon += AllplanGeo.Point3D(top_min_max.Min.X, top_min_max.Min.Y, z_top)

        _, top_poly_surface = AllplanGeo.CreatePolyhedron(top_polygon)

        _, top_surface = AllplanGeo.CreateBRep3D(top_poly_surface)

        return top_surface


    @staticmethod
    def __create_rectangular_bottom_surface(opening: AllplanGeo.BRep3D) -> AllplanGeo.BRep3D:
        """ create a rectangular surface for the bottom reference plane

        Args:
            opening: opening body

        Returns:
            bottom surface
        """

        bottom_min_max = AllplanGeo.CalcMinMax(opening)[0]

        z_bottom = bottom_min_max.Min.Z

        bottom_min_max.Inflate(100)

        bottom_polygon = AllplanGeo.Polygon3D()
        bottom_polygon += AllplanGeo.Point3D(bottom_min_max.Min.X, bottom_min_max.Min.Y, z_bottom)
        bottom_polygon += AllplanGeo.Point3D(bottom_min_max.Max.X, bottom_min_max.Min.Y, z_bottom)
        bottom_polygon += AllplanGeo.Point3D(bottom_min_max.Max.X, bottom_min_max.Max.Y, z_bottom)
        bottom_polygon += AllplanGeo.Point3D(bottom_min_max.Min.X, bottom_min_max.Max.Y, z_bottom)
        bottom_polygon += AllplanGeo.Point3D(bottom_min_max.Min.X, bottom_min_max.Min.Y, z_bottom)

        _, bottom_poly_surface = AllplanGeo.CreatePolyhedron(bottom_polygon)

        _, bottom_surface = AllplanGeo.CreateBRep3D(bottom_poly_surface)

        return bottom_surface


    @staticmethod
    def __create_rectangular_bottom_offset_surface(bottom_surface: AllplanGeo.BRep3D) -> AllplanGeo.BRep3D:
        """ create a rectangular offset surface for the bottom reference plane

        Args:
            bottom_surface: bottom surface

        Returns:
            top surface
        """

        bottom_edge = cast(AllplanGeo.Arc3D, bottom_surface.GetEdgeParametricGeometry(0))

        bottom_polygon = AllplanGeo.Polygonize(bottom_edge, 30)

        z_bottom = bottom_polygon.StartPoint.Z

        _, bottom_offset_polygon = AllplanGeo.Offset(200, AllplanGeo.ConvertTo2D(bottom_polygon)[1], False)

        bottom_polygon = AllplanGeo.Polygon3D()

        for pnt in bottom_offset_polygon.Points:
            bottom_polygon += AllplanGeo.Point3D(pnt.X, pnt.Y, z_bottom)

        bottom_polygon += bottom_polygon.StartPoint

        _, bottom_poly_surface = AllplanGeo.CreatePolyhedron(bottom_polygon)

        _, bottom_surface = AllplanGeo.CreateBRep3D(bottom_poly_surface)

        return bottom_surface

```

</details>