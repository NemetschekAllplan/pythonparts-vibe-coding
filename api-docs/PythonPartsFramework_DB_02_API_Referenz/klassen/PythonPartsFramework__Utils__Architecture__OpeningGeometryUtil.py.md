---
title: "OpeningGeometryUtil"
source: "PythonPartsFramework\Utils\Architecture\OpeningGeometryUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningGeometryUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\OpeningGeometryUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the opening geometry utility functions

## Abhängigkeiten

- `NemAll_Python_ArchElements`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `Utils.Geometry.Arc2DUtil`
- `dataclasses`

## Klassen

### `OpeningGeometry`

implementation of the wall opening geometry
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `OpeningGeometryUtil`

utility functions for opening geometry
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_arch_opening_geometry_by_sel_point` | `element: AllplanEleAdapter.BaseElementAdapter, sel_point: AllplanGeo.Point2D` | `OpeningGeometry` | get the wall opening geometry from the selected element and the selection point  Args:     element:   opening element     sel_point: selection point  Returns:     opening geometry |
| `get_arch_opening_geometry_by_segment` | `element: AllplanEleAdapter.BaseElementAdapter, segment_index: int, left_aligned: bool` | `OpeningGeometry` | get the wall opening geometry from the selected element and the segment index  Args:     element:       opening element     segment_index: segment index     left_aligned:  left aligned  Returns:     opening geometry |
| `__get_wall_opening_geometry` | `element: AllplanEleAdapter.BaseElementAdapter, segment: AllplanGeo.Line2D, left_aligned: bool` | `OpeningGeometry` | get the wall opening geometry  Args:     element:      opening element     segment:      segment     left_aligned: left aligned  Returns:     opening geometry |
| `__get_slab_opening_geometry` | `element: AllplanEleAdapter.BaseElementAdapter, segment: AllplanGeo.Line2D, left_aligned: bool` | `tuple[OpeningGeometry, bool]` | get the slab opening geometry  Args:     element:      opening element     segment:      segment     left_aligned: left aligned  Returns:     opening geometry, circular opening flag |
| `__create_opening_polygon` | `width: float, depth: float, radius: float, shape_type: AllplanArchEle.VerticalOpeningShapeType | AllplanArchEle.ShapeType` | `AllplanGeo.Polygon2D` | create the opening polygon based on the opening element properties  Args:     width:      with of the opening     depth:      depth of the opening     radius:     radius of the opening     shape_type: shape type of the opening  Returns:     opening polygon |
| `__create_placement_matrix` | `opening_dir_vec: AllplanGeo.Vector2D, opening_pnt: AllplanGeo.Point2D, plane_ref: AllplanArchEle.PlaneReferences, opening_geo: OpeningGeometry` | `None` | create the placement matrix for the opening geometry  Args:     opening_dir_vec: opening direction vector     opening_pnt:     opening point     plane_ref:       plane reference     opening_geo:     opening geometry to set the placement matrix |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening geometry utility functions
"""

from dataclasses import dataclass

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Geometry as AllplanGeo

from Utils.Geometry.Arc2DUtil import Arc2DUtil

@dataclass
class OpeningGeometry:
    """ implementation of the wall opening geometry
    """

    opening_width   = 1000.
    opening_depth   = 300.
    opening_height  = 2000.
    opening_polygon = AllplanGeo.Polygon2D()
    tier_depth      = 300.
    exterior_offset = 0.0
    interior_offset = 0.0
    placement_point = AllplanGeo.Point3D()
    rotation_mat    = AllplanGeo.Matrix3D()
    left_aligned    = True
    segment_index   = -1


class OpeningGeometryUtil():
    """ utility functions for opening geometry
    """
    @staticmethod
    def get_arch_opening_geometry_by_sel_point(element  : AllplanEleAdapter.BaseElementAdapter,
                                               sel_point: AllplanGeo.Point2D) -> OpeningGeometry:
        """ get the wall opening geometry from the selected element and the selection point

        Args:
            element:   opening element
            sel_point: selection point

        Returns:
            opening geometry
        """

        #----------------- get the opening polygon and segment

        opening_polygon = element.GetGeometry()

        if not isinstance(opening_polygon, (AllplanGeo.Polygon2D, AllplanGeo.Polyline2D)):
            return OpeningGeometry()

        if isinstance(opening_polygon, AllplanGeo.Polyline2D):
            opening_polygon = AllplanGeo.Polygon2D(opening_polygon.Points)

        segment, _, _ = AllplanArchEle.ArchitectureElementsGeometryService.GetOutlineSegmentAndPoint(element, sel_point)

        eps = AllplanGeo.GetAbsoluteTolerance()

        segment_index = next((line_index for line_index, line in enumerate(opening_polygon.GetSegments()[1])
                              if AllplanGeo.Comparison.Equal(line, segment, eps)), -1)

        left_aligned = AllplanGeo.Vector2D(segment.StartPoint, sel_point).GetLength() < \
                       AllplanGeo.Vector2D(segment.EndPoint, sel_point).GetLength()


        #----------------- get the opening geometry

        match element.GetElementAdapterType().GetGuid():
            case AllplanEleAdapter.SlabOpening_TypeUUID:
                opening_geo, is_circular = OpeningGeometryUtil.__get_slab_opening_geometry(element, segment, left_aligned)

                if is_circular:
                    left_aligned = True

            case _:
                opening_geo = OpeningGeometryUtil.__get_wall_opening_geometry(element, segment, left_aligned)

        opening_geo.segment_index = segment_index
        opening_geo.left_aligned  = left_aligned

        return opening_geo


    @staticmethod
    def get_arch_opening_geometry_by_segment(element      : AllplanEleAdapter.BaseElementAdapter,
                                             segment_index: int,
                                             left_aligned : bool) -> OpeningGeometry:
        """ get the wall opening geometry from the selected element and the segment index

        Args:
            element:       opening element
            segment_index: segment index
            left_aligned:  left aligned

        Returns:
            opening geometry
        """

        opening_polygon = element.GetGeometry()

        if isinstance(opening_polygon, AllplanGeo.Polyline2D):
            opening_polygon = AllplanGeo.Polygon2D(opening_polygon.Points)

        segment = opening_polygon.GetSegments()[1][segment_index]


        #----------------- get the opening geometry

        match element.GetElementAdapterType().GetGuid():
            case AllplanEleAdapter.SlabOpening_TypeUUID:
                opening_geo, _ = OpeningGeometryUtil.__get_slab_opening_geometry(element, segment, left_aligned)

            case _:
                opening_geo = OpeningGeometryUtil.__get_wall_opening_geometry(element, segment, left_aligned)

        opening_geo.segment_index = segment_index
        opening_geo.left_aligned  = left_aligned

        return opening_geo


    @staticmethod
    def __get_wall_opening_geometry(element     : AllplanEleAdapter.BaseElementAdapter,
                                    segment     : AllplanGeo.Line2D,
                                    left_aligned: bool) -> OpeningGeometry:
        """ get the wall opening geometry

        Args:
            element:      opening element
            segment:      segment
            left_aligned: left aligned

        Returns:
            opening geometry
        """

        #----------------- set the opening data

        opening_ele = AllplanBaseEle.GetElement(element)

        if isinstance(opening_ele, AllplanArchEle.GeneralOpeningElement):
            opening_ele_prop = opening_ele.Properties

        elif isinstance(opening_ele, AllplanArchEle.DoorOpeningElement):
            opening_ele_prop = opening_ele.Properties

        elif isinstance(opening_ele, AllplanArchEle.WindowOpeningElement):
            opening_ele_prop = opening_ele.Properties

        else:
            return OpeningGeometry()

        wall_element = AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(element)

        general_axis_ele = AllplanEleAdapter.AxisElementAdapter(wall_element)

        tier_number    = AllplanEleAdapter.BaseElementAdapterChildElementsService.GetTierNumber(element) - 1
        tier_thickness = general_axis_ele.GetTierThickness()


        #----------------- get the opening data

        plane_ref = opening_ele_prop.PlaneReferences

        opening_geo = OpeningGeometry()

        opening_geo.opening_height = plane_ref.AbsTopElevation - plane_ref.AbsBottomElevation
        opening_geo.opening_width  = opening_ele_prop.GetGeometryProperties().Width
        opening_geo.opening_depth  = general_axis_ele.GetThickness()
        opening_geo.tier_depth     = tier_thickness[tier_number]

        opening_geo.opening_polygon = OpeningGeometryUtil.__create_opening_polygon(opening_geo.opening_width, opening_geo.opening_height,
                                                                                   opening_geo.opening_width / 2,
                                                                                   opening_ele_prop.GetGeometryProperties().Shape)

        for index in range(0, tier_number):
            opening_geo.interior_offset += tier_thickness[index]

        for index in range(tier_number + 1, len(tier_thickness)):
            opening_geo.exterior_offset += tier_thickness[index]

        opening_dir_vec = AllplanGeo.Vector2D(segment.StartPoint, segment.EndPoint)
        opening_pnt     = segment.StartPoint if left_aligned else segment.EndPoint

        OpeningGeometryUtil.__create_placement_matrix(opening_dir_vec, opening_pnt, plane_ref, opening_geo)

        return opening_geo


    @staticmethod
    def __get_slab_opening_geometry(element     : AllplanEleAdapter.BaseElementAdapter,
                                    segment     : AllplanGeo.Line2D,
                                    left_aligned: bool) -> tuple[OpeningGeometry, bool]:
        """ get the slab opening geometry

        Args:
            element:      opening element
            segment:      segment
            left_aligned: left aligned

        Returns:
            opening geometry, circular opening flag
        """

        #----------------- set the opening data

        opening_ele = AllplanBaseEle.GetElement(element)

        if isinstance(opening_ele, AllplanArchEle.SlabOpeningElement):
            opening_ele_prop = opening_ele.Properties

        else:
            return OpeningGeometry(), False


        #----------------- get the opening data

        plane_ref = opening_ele_prop.PlaneReferences

        opening_geo = OpeningGeometry()

        opening_geo.opening_height = plane_ref.AbsTopElevation - plane_ref.AbsBottomElevation

        match opening_ele_prop.ShapeType:
            case AllplanArchEle.ShapeType.eRectangular:
                opening_dir_vec = AllplanGeo.Vector2D(segment.StartPoint, segment.EndPoint)
                opening_pnt     = segment.StartPoint if left_aligned else segment.EndPoint

                opening_geo.opening_width  = opening_ele_prop.Width
                opening_geo.opening_depth  = opening_ele_prop.Depth

            case AllplanArchEle.ShapeType.eCircular:
                _, center = AllplanGeo.CenterCalculus.Calculate(AllplanGeo.Polygon2D(element.GetGeometry().Points), True, 0)

                radius = opening_ele_prop.Radius

                opening_pnt = center.To2D - AllplanGeo.Point2D(radius, radius)

                opening_dir_vec = AllplanGeo.Vector2D(opening_pnt,
                                                      center.To2D + AllplanGeo.Vector2D(radius, -radius))

                opening_geo.opening_width  = radius * 2
                opening_geo.opening_depth  = radius * 2

        opening_geo.tier_depth = opening_geo.opening_depth

        opening_geo.opening_polygon = OpeningGeometryUtil.__create_opening_polygon(opening_geo.opening_width, opening_geo.opening_depth,
                                                                                   opening_ele_prop.Radius,
                                                                                   opening_ele_prop.ShapeType)

        OpeningGeometryUtil.__create_placement_matrix(opening_dir_vec, opening_pnt, plane_ref, opening_geo)

        return opening_geo, opening_ele_prop.ShapeType == AllplanArchEle.ShapeType.eCircular


    @staticmethod
    def __create_opening_polygon(width     : float,
                                 depth     : float,
                                 radius    : float,
                                 shape_type: (AllplanArchEle.VerticalOpeningShapeType | AllplanArchEle.ShapeType)) -> AllplanGeo.Polygon2D:
        """ create the opening polygon based on the opening element properties

        Args:
            width:      with of the opening
            depth:      depth of the opening
            radius:     radius of the opening
            shape_type: shape type of the opening

        Returns:
            opening polygon
        """

        opening_polygon = AllplanGeo.Polygon2D()

        match shape_type:
            case AllplanArchEle.VerticalOpeningShapeType.eRectangle  | AllplanArchEle.ShapeType.eRectangular:
                opening_polygon += AllplanGeo.Point2D(width, 0)
                opening_polygon += AllplanGeo.Point2D(width, depth)
                opening_polygon += AllplanGeo.Point2D(0, depth)
                opening_polygon += AllplanGeo.Point2D(0, 0)
                opening_polygon += AllplanGeo.Point2D(width, 0)

            case AllplanArchEle.VerticalOpeningShapeType.eCircle | AllplanArchEle.ShapeType.eCircular:
                if (opening_polygon := Arc2DUtil.create_polygonized_arc(radius, radius, radius)) is None:
                    return AllplanGeo.Polygon2D()

            case _:
                return AllplanGeo.Polygon2D()

        return opening_polygon


    @staticmethod
    def __create_placement_matrix(opening_dir_vec: AllplanGeo.Vector2D,
                                  opening_pnt    : AllplanGeo.Point2D,
                                  plane_ref      : AllplanArchEle.PlaneReferences,
                                  opening_geo    : OpeningGeometry):
        """ create the placement matrix for the opening geometry

        Args:
            opening_dir_vec: opening direction vector
            opening_pnt:     opening point
            plane_ref:       plane reference
            opening_geo:     opening geometry to set the placement matrix
        """

        #----------------- create the placement matrix

        rotation_mat = AllplanGeo.Matrix3D()
        rotation_mat.SetRotation(AllplanGeo.Line3D(0, 0, 0, 0, 0, 1000), opening_dir_vec.GetAngle())

        opening_geo.rotation_mat = rotation_mat

        opening_geo.placement_point = AllplanGeo.Point3D(opening_pnt.X, opening_pnt.Y, plane_ref.AbsBottomElevation)

```

</details>