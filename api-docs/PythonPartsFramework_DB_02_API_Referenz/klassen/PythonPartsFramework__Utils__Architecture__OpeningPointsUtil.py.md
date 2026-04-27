---
title: "OpeningPointsUtil"
source: "PythonPartsFramework\Utils\Architecture\OpeningPointsUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningPointsUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\OpeningPointsUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the opening points utilities

## Abhängigkeiten

- `NemAll_Python_ArchElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Palette`

## Klassen

### `OpeningPointsUtil`

implementation of the opening points utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_opening_end_point_for_axis_element` | `opening_start_pnt: AllplanGeo.Point2D, opening_width: float, placement_ele_axis: AllplanGeo.Line2D | AllplanGeo.Arc2D, placement_ele_polygon: AllplanGeo.Polygon2D | AllplanGeo.Polyline2D, placement_line: AllplanGeo.Line2D` | `AllplanGeo.Point2D` | create the opening points for an axis element  Args:     opening_start_pnt:     opening start point     opening_width:         opening width     placement_ele_axis:    opening placement element axis     placement_ele_polygon: opening placement element polygon / polyline     placement_line:        placement line  Returns:     end point of the opening |
| `create_opening_end_point_for_shaped_element` | `opening_start_pnt: AllplanGeo.Point2D, opening_width: float, placement_line: AllplanGeo.Line2D` | `AllplanGeo.Point2D` | create the opening points for a shaped element  Args:     opening_start_pnt: opening start point     opening_width:     opening width     placement_line:    placement line  Returns:     end point of the opening |
| `create_opening_points_for_axis_element` | `opening_start_pnt: AllplanGeo.Point2D, opening_end_pnt: AllplanGeo.Point2D, opening_width: float, placement_ele_thickness: float` | `tuple[AllplanGeo.Point2D, ...]` | create the opening points for an axis element  Args:     opening_start_pnt:       opening start point     opening_end_pnt:         opening end point     opening_width:           opening width     placement_ele_thickness: opening placement element thickness  Returns:     opening points |
| `get_opening_offset_points` | `element: AllplanEleAdapter.BaseElementAdapter, opening_start_pnt: AllplanGeo.Point2D, opening_end_pnt: AllplanGeo.Point2D, placement_line: AllplanGeo.Line2D` | `tuple[bool, AllplanGeo.Point2D, AllplanGeo.Point2D]` | get the left and right point for the opening offset  Args:     element:           opening placement element for the opening     opening_start_pnt: opening start point     opening_end_pnt:   opening end point     placement_line:    placement line from the opening start point  Returns:     points created, start offset point, end offset point |
| `get_start_point_from_start_offset` | `placement_ele_axis: AllplanGeo.Line2D | AllplanGeo.Arc2D | None, offset_start_pnt: AllplanGeo.Point2D, placement_line: AllplanGeo.Line2D, placement_arc: AllplanGeo.Arc2D | None, placement_ele_polygon: AllplanGeo.Polygon2D | AllplanGeo.Polyline2D, offset: float` | `tuple[bool, AllplanGeo.Point2D]` | get the start point by an offset from an offset start point  Args:     placement_ele_axis:    opening placement element axis     offset_start_pnt:      offset start point     placement_line:        placement line     placement_arc:         placement arc     placement_ele_polygon: opening placement element polygon / polyline     offset:                offset from the offset start point  Returns:     start point of the opening |
| `get_distance_from_offset_start_point` | `input_pnt: AllplanGeo.Point3D, placement_ele_axis: AllplanGeo.Line2D | AllplanGeo.Arc2D | None, offset_start_pnt: AllplanGeo.Point2D, placement_line: AllplanGeo.Line2D, placement_arc: AllplanGeo.Arc2D | None, placement_ele_polygon: AllplanGeo.Polygon2D | AllplanGeo.Polyline2D` | `float` | get the local distance between input and offset start point  Args:     input_pnt:             input point     placement_ele_axis:    opening placement element axis     offset_start_pnt:      offset start point     placement_line:        placement line     placement_arc:         placement arc     placement_ele_polygon: opening placement element polygon / polyline  Returns:     distance between input and start point |
| `get_start_point_from_end_offset` | `placement_ele_axis: AllplanGeo.Line2D | AllplanGeo.Arc2D | None, offset_end_pnt: AllplanGeo.Point2D, placement_line: AllplanGeo.Line2D, placement_arc: AllplanGeo.Arc2D | None, opening_width: float, placement_ele_polygon: AllplanGeo.Polygon2D | AllplanGeo.Polyline2D, offset: float` | `tuple[bool, AllplanGeo.Point2D]` | get the start point by an offset from an offset start point  Args:     placement_ele_axis:    opening placement element axis     offset_end_pnt:        offset end point     placement_line:        placement line     placement_arc:         placement arc     opening_width:         opening width     placement_ele_polygon: opening placement element polygon / polyline     offset:                offset from the offset start point  Returns:     start point of the opening |
| `get_distance_from_offset_end_point` | `input_pnt: AllplanGeo.Point3D, placement_ele_axis: AllplanGeo.Line2D | AllplanGeo.Arc2D | None, offset_end_pnt: AllplanGeo.Point2D, placement_line: AllplanGeo.Line2D, placement_arc: AllplanGeo.Arc2D | None, placement_ele_polygon: AllplanGeo.Polygon2D | AllplanGeo.Polyline2D` | `float` | get the local distance between input and offset end point  Args:     input_pnt:             input point     placement_ele_axis:    opening placement element axis     offset_end_pnt:        offset end point     placement_line:        placement line     placement_arc:         placement arc     placement_ele_polygon: opening placement element polygon / polyline  Returns:     distance between input and start point |
| `calc_point_at_placement_arc` | `local_dist: float, placement_arc: AllplanGeo.Arc2D, placement_polyline: AllplanGeo.Polyline2D` | `tuple[bool, AllplanGeo.Point2D]` | calculate the point at the placement arc  Args:     local_dist:         local point distance at the placement arc     placement_arc:      placement arc     placement_polyline: placement polyline  Returns:     found state, point at the polyline |
| `calc_door_swing_base_point_index` | `opening_start_pnt: AllplanGeo.Point2D, opening_end_pnt: AllplanGeo.Point2D, width: float, element_thickness: float, input_pnt: AllplanGeo.Point3D` | `int` | calculate the door swing base point index  Args:     opening_start_pnt: opening start point     opening_end_pnt:   opening end point     width:             with of the opening     element_thickness: element thickness     input_pnt:         input point  Returns:     door swing base point index |
| `select_opening_tier` | `input_pnt: AllplanGeo.Point3D, opening_tier_center: list[AllplanGeo.Point2D]` | `int` | select the opening tier  Args:     input_pnt:           input point     opening_tier_center: center for the opening tier  Returns:     returns |
| `select_opening_symbol_ref_pnt` | `input_pnt: AllplanGeo.Point3D, opening_tier_ref_pnt: tuple[AllplanGeo.Point2D, ...]` | `AllplanPalette.RefPointPosition` | select the reference point for the opening symbol  Args:     input_pnt:            input point     opening_tier_ref_pnt: opening tier reference points  Returns:     symbol reference point |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening points utilities
"""

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Palette as AllplanPalette

class OpeningPointsUtil():
    """ implementation of the opening points utilities
    """

    @staticmethod
    def create_opening_end_point_for_axis_element(opening_start_pnt    : AllplanGeo.Point2D,
                                                  opening_width        : float,
                                                  placement_ele_axis   : (AllplanGeo.Line2D | AllplanGeo.Arc2D),
                                                  placement_ele_polygon: (AllplanGeo.Polygon2D | AllplanGeo.Polyline2D),
                                                  placement_line       : AllplanGeo.Line2D) -> AllplanGeo.Point2D:
        """ create the opening points for an axis element

        Args:
            opening_start_pnt:     opening start point
            opening_width:         opening width
            placement_ele_axis:    opening placement element axis
            placement_ele_polygon: opening placement element polygon / polyline
            placement_line:        placement line

        Returns:
            end point of the opening
        """

        #----------------- opening points for a linear axis

        if isinstance(placement_ele_axis, AllplanGeo.Line2D):
            loc_start = AllplanGeo.TransformCoord.PointLocal(placement_line, opening_start_pnt).X

            opening_end_pnt = AllplanGeo.TransformCoord.PointGlobal(placement_line, loc_start + opening_width).To2D


        #----------------- opening points for a circular, spline axis or entity based wall

        else:
            _, dir_ele = AllplanGeo.Polyline2DUtil.GetPolyline2DSegment(AllplanGeo.Polyline2D(placement_ele_polygon), opening_start_pnt)

            dir_ele.TrimEnd(-100)

            error, opening_end_pnt = \
                AllplanGeo.Polygon2DUtil.FindPointOnPolygonWithDistance(AllplanGeo.Polygon2D(placement_ele_polygon.Points),
                                                                        opening_start_pnt, dir_ele.EndPoint,
                                                                        placement_ele_axis, opening_width)

            if error:
                opening_end_pnt = opening_start_pnt

        return opening_end_pnt


    @staticmethod
    def create_opening_end_point_for_shaped_element(opening_start_pnt: AllplanGeo.Point2D,
                                                    opening_width    : float,
                                                    placement_line   : AllplanGeo.Line2D) -> AllplanGeo.Point2D:
        """ create the opening points for a shaped element

        Args:
            opening_start_pnt: opening start point
            opening_width:     opening width
            placement_line:    placement line

        Returns:
            end point of the opening
        """

        loc_start = AllplanGeo.TransformCoord.PointLocal(placement_line, opening_start_pnt).X

        opening_end_pnt = AllplanGeo.TransformCoord.PointGlobal(placement_line, loc_start + opening_width).To2D

        return opening_end_pnt


    @staticmethod
    def create_opening_points_for_axis_element(opening_start_pnt      : AllplanGeo.Point2D,
                                               opening_end_pnt        : AllplanGeo.Point2D,
                                               opening_width          : float,
                                               placement_ele_thickness: float) -> tuple[AllplanGeo.Point2D, ...]:
        """ create the opening points for an axis element

        Args:
            opening_start_pnt:       opening start point
            opening_end_pnt:         opening end point
            opening_width:           opening width
            placement_ele_thickness: opening placement element thickness

        Returns:
            opening points
        """

        base_line = AllplanGeo.Line2D(opening_start_pnt, opening_end_pnt)

        opening_points = (opening_start_pnt, opening_end_pnt,
                          AllplanGeo.TransformCoord.PointGlobal(base_line, AllplanGeo.Point2D(opening_width,
                                                                                              placement_ele_thickness)).To2D,
                          AllplanGeo.TransformCoord.PointGlobal(base_line, AllplanGeo.Point2D(0, placement_ele_thickness)).To2D)

        return opening_points



    @staticmethod
    def get_opening_offset_points(element          : AllplanEleAdapter.BaseElementAdapter,
                                  opening_start_pnt: AllplanGeo.Point2D,
                                  opening_end_pnt  : AllplanGeo.Point2D,
                                  placement_line   : AllplanGeo.Line2D) -> tuple[bool, AllplanGeo.Point2D, AllplanGeo.Point2D]:
        """ get the left and right point for the opening offset

        Args:
            element:           opening placement element for the opening
            opening_start_pnt: opening start point
            opening_end_pnt:   opening end point
            placement_line:    placement line from the opening start point

        Returns:
            points created, start offset point, end offset point
        """

        if AllplanEleAdapter.AxisElementAdapter(element).HasAxis():
            res = AllplanArchEle.ArchitectureElementsGeometryService.GetOpeningOffsetPoints(element, opening_start_pnt, opening_end_pnt)

            return res

        return True, placement_line.StartPoint, placement_line.EndPoint


    @staticmethod
    def get_start_point_from_start_offset(placement_ele_axis   : (AllplanGeo.Line2D | AllplanGeo.Arc2D | None),
                                          offset_start_pnt     : AllplanGeo.Point2D,
                                          placement_line       : AllplanGeo.Line2D,
                                          placement_arc        : (AllplanGeo.Arc2D | None),
                                          placement_ele_polygon: (AllplanGeo.Polygon2D | AllplanGeo.Polyline2D),
                                          offset               : float) -> tuple[bool, AllplanGeo.Point2D]:
        """ get the start point by an offset from an offset start point

        Args:
            placement_ele_axis:    opening placement element axis
            offset_start_pnt:      offset start point
            placement_line:        placement line
            placement_arc:         placement arc
            placement_ele_polygon: opening placement element polygon / polyline
            offset:                offset from the offset start point

        Returns:
            start point of the opening
        """


        #----------------- calculate the new start point of the opening for a linear axis

        if isinstance(placement_ele_axis, AllplanGeo.Line2D):
            loc_start_pnt_dist = AllplanGeo.TransformCoord.PointLocal(placement_line, offset_start_pnt).X

            return True, AllplanGeo.TransformCoord.PointGlobal(placement_line, loc_start_pnt_dist + offset).To2D


        #----------------- calculate the new start point of the opening for a circular axis

        placement_polyline = AllplanArchEle.ArchitectureElementsGeometryService.GetOuterPolyline(
                                        AllplanGeo.Polygon2D(placement_ele_polygon.Points),
                                        placement_line, placement_ele_axis)

        if isinstance(placement_ele_axis, AllplanGeo.Arc2D):
            if placement_arc is None:
                return False, AllplanGeo.Point2D()

            loc_start_pnt_dist = AllplanGeo.TransformCoord.PointLocal(placement_arc, offset_start_pnt).X

            return OpeningPointsUtil.calc_point_at_placement_arc(loc_start_pnt_dist + offset,
                                                                 placement_arc, placement_polyline)


        #----------------- calculate the new start point of the opening for a polyline axis

        loc_start_pnt_dist = AllplanGeo.TransformCoord.PointLocal(placement_polyline, offset_start_pnt).X

        return True, AllplanGeo.TransformCoord.PointGlobal(placement_polyline, loc_start_pnt_dist + offset).To2D


    @staticmethod
    def get_distance_from_offset_start_point(input_pnt            : AllplanGeo.Point3D,
                                             placement_ele_axis   : (AllplanGeo.Line2D | AllplanGeo.Arc2D | None),
                                             offset_start_pnt     : AllplanGeo.Point2D,
                                             placement_line       : AllplanGeo.Line2D,
                                             placement_arc        : (AllplanGeo.Arc2D | None),
                                             placement_ele_polygon: (AllplanGeo.Polygon2D | AllplanGeo.Polyline2D)) -> float:
        """ get the local distance between input and offset start point

        Args:
            input_pnt:             input point
            placement_ele_axis:    opening placement element axis
            offset_start_pnt:      offset start point
            placement_line:        placement line
            placement_arc:         placement arc
            placement_ele_polygon: opening placement element polygon / polyline

        Returns:
            distance between input and start point
        """

        if isinstance(placement_ele_axis, AllplanGeo.Line2D):
            return AllplanGeo.TransformCoord.PointLocal(placement_line, input_pnt).X - \
                   AllplanGeo.TransformCoord.PointLocal(placement_line, offset_start_pnt).X

        if isinstance(placement_ele_axis, AllplanGeo.Arc2D):
            if placement_arc is None:
                return 0

            return AllplanGeo.TransformCoord.PointLocal(placement_arc, input_pnt).X - \
                   AllplanGeo.TransformCoord.PointLocal(placement_arc, offset_start_pnt).X

        placement_polyline = AllplanArchEle.ArchitectureElementsGeometryService.GetOuterPolyline(
                             AllplanGeo.Polygon2D(placement_ele_polygon.Points),
                                                  placement_line, placement_ele_axis)

        return AllplanGeo.TransformCoord.PointLocal(placement_polyline, input_pnt).X - \
               AllplanGeo.TransformCoord.PointLocal(placement_polyline, offset_start_pnt).X


    @staticmethod
    def get_start_point_from_end_offset(placement_ele_axis   : (AllplanGeo.Line2D | AllplanGeo.Arc2D | None),
                                        offset_end_pnt       : AllplanGeo.Point2D,
                                        placement_line       : AllplanGeo.Line2D,
                                        placement_arc        : (AllplanGeo.Arc2D | None),
                                        opening_width        : float,
                                        placement_ele_polygon: (AllplanGeo.Polygon2D | AllplanGeo.Polyline2D),
                                        offset               : float) -> tuple[bool, AllplanGeo.Point2D]:
        """ get the start point by an offset from an offset start point

        Args:
            placement_ele_axis:    opening placement element axis
            offset_end_pnt:        offset end point
            placement_line:        placement line
            placement_arc:         placement arc
            opening_width:         opening width
            placement_ele_polygon: opening placement element polygon / polyline
            offset:                offset from the offset start point

        Returns:
            start point of the opening
        """

        #----------------- calculate the new start point of the opening for a linear axis

        if isinstance(placement_ele_axis, AllplanGeo.Line2D):
            loc_end_pnt_dist = AllplanGeo.TransformCoord.PointLocal(placement_line, offset_end_pnt).X

            return True, AllplanGeo.TransformCoord.PointGlobal(placement_line,
                                                               loc_end_pnt_dist - offset - opening_width).To2D


        #----------------- calculate the new start point of the opening for a circular axis

        placement_polyline = AllplanArchEle.ArchitectureElementsGeometryService.GetOuterPolyline(
                             AllplanGeo.Polygon2D(placement_ele_polygon.Points),
                                                  placement_line, placement_ele_axis)

        if isinstance(placement_ele_axis, AllplanGeo.Arc2D):
            if placement_arc is None:
                return False, AllplanGeo.Point2D()

            loc_end_pnt_dist = AllplanGeo.TransformCoord.PointLocal(placement_arc, offset_end_pnt).X

            return OpeningPointsUtil.calc_point_at_placement_arc(loc_end_pnt_dist - offset - opening_width,
                                                                 placement_arc, placement_polyline)


        #----------------- calculate the new start point of the opening for a polyline axis

        if placement_polyline is None:
            return False, AllplanGeo.Point2D()

        loc_end_pnt_dist = AllplanGeo.TransformCoord.PointLocal(placement_polyline, offset_end_pnt).X

        opening_end_pnt = AllplanGeo.TransformCoord.PointGlobal(placement_polyline, loc_end_pnt_dist - offset)


        #----------------- get the start point at the polyline

        _, dir_ele = AllplanGeo.Polyline2DUtil.GetPolyline2DSegment(placement_polyline,
                                                                    opening_end_pnt.To2D)

        dir_ele.TrimStart(-100)

        found, opening_start_pnt = \
            AllplanGeo.Polygon2DUtil.FindPointOnPolygonWithDistance(AllplanGeo.Polygon2D(placement_ele_polygon.Points),
                                                                                         opening_end_pnt.To2D,
                                                                                         dir_ele.StartPoint,
                                                                                         placement_ele_axis,
                                                                                         opening_width)

        return (found == 0), opening_start_pnt


    @staticmethod
    def get_distance_from_offset_end_point(input_pnt            : AllplanGeo.Point3D,
                                           placement_ele_axis   : (AllplanGeo.Line2D | AllplanGeo.Arc2D | None),
                                           offset_end_pnt       : AllplanGeo.Point2D,
                                           placement_line       : AllplanGeo.Line2D,
                                           placement_arc        : (AllplanGeo.Arc2D | None),
                                           placement_ele_polygon: (AllplanGeo.Polygon2D | AllplanGeo.Polyline2D)) -> float:
        """ get the local distance between input and offset end point

        Args:
            input_pnt:             input point
            placement_ele_axis:    opening placement element axis
            offset_end_pnt:        offset end point
            placement_line:        placement line
            placement_arc:         placement arc
            placement_ele_polygon: opening placement element polygon / polyline

        Returns:
            distance between input and start point
        """

        if isinstance(placement_ele_axis, AllplanGeo.Line2D):
            return AllplanGeo.TransformCoord.PointLocal(placement_line, offset_end_pnt).X - \
                   AllplanGeo.TransformCoord.PointLocal(placement_line, input_pnt).X

        if isinstance(placement_ele_axis, AllplanGeo.Arc2D):
            if placement_arc is None:
                return 0

            return AllplanGeo.TransformCoord.PointLocal(placement_arc, offset_end_pnt).X - \
                   AllplanGeo.TransformCoord.PointLocal(placement_arc, input_pnt).X

        placement_polyline = AllplanArchEle.ArchitectureElementsGeometryService.GetOuterPolyline(
                             AllplanGeo.Polygon2D(placement_ele_polygon.Points),
                                                  placement_line, placement_ele_axis)

        return AllplanGeo.TransformCoord.PointLocal(placement_polyline, offset_end_pnt).X - \
               AllplanGeo.TransformCoord.PointLocal(placement_polyline, input_pnt).X


    @staticmethod
    def calc_point_at_placement_arc(local_dist        : float,
                                    placement_arc     : AllplanGeo.Arc2D,
                                    placement_polyline: AllplanGeo.Polyline2D) -> tuple[bool, AllplanGeo.Point2D]:
        """ calculate the point at the placement arc

        Args:
            local_dist:         local point distance at the placement arc
            placement_arc:      placement arc
            placement_polyline: placement polyline

        Returns:
            found state, point at the polyline
        """

        ortho_start_pnt = AllplanGeo.TransformCoord.PointGlobal(placement_arc,
                                                                AllplanGeo.Point2D(local_dist, 1000))
        ortho_end_pnt = AllplanGeo.TransformCoord.PointGlobal(placement_arc,
                                                              AllplanGeo.Point2D(local_dist, -1000))

        ortho_line = AllplanGeo.Line2D(ortho_start_pnt.To2D, ortho_end_pnt.To2D)

        found, intersect_pnts = AllplanGeo.IntersectionCalculus(ortho_line, placement_polyline)

        return (True, intersect_pnts[0].To2D) if found else (False, AllplanGeo.Point2D())

    @staticmethod
    def calc_door_swing_base_point_index(opening_start_pnt: AllplanGeo.Point2D,
                                         opening_end_pnt  : AllplanGeo.Point2D,
                                         width            : float,
                                         element_thickness: float,
                                         input_pnt        : AllplanGeo.Point3D) -> int:
        """ calculate the door swing base point index

        Args:
            opening_start_pnt: opening start point
            opening_end_pnt:   opening end point
            width:             with of the opening
            element_thickness: element thickness
            input_pnt:         input point

        Returns:
            door swing base point index
        """

        input_pnt_2d = input_pnt.To2D

        min_dist         = 1.0e10
        base_point_index = 1

        for index, pnt in enumerate(OpeningPointsUtil.create_opening_points_for_axis_element(opening_start_pnt, opening_end_pnt,
                                                                                             width, element_thickness)):
            if (dist := AllplanGeo.Vector2D(pnt, input_pnt_2d).GetLength()) < min_dist:
                min_dist = dist
                base_point_index = index + 1

        return base_point_index


    @staticmethod
    def select_opening_tier(input_pnt          : AllplanGeo.Point3D,
                            opening_tier_center: list[AllplanGeo.Point2D]) -> int:
        """ select the opening tier

        Args:
            input_pnt:           input point
            opening_tier_center: center for the opening tier

        Returns:
            returns
        """

        place_pnt  = input_pnt.To2D
        min_dist   = 1.0e10
        tier_index = 0

        for index, tier_center in enumerate(opening_tier_center):
            if (dist := AllplanGeo.Vector2D(place_pnt, tier_center).GetLength()) < min_dist:
                min_dist   = dist
                tier_index = index

        return tier_index + 1


    @staticmethod
    def select_opening_symbol_ref_pnt(input_pnt           : AllplanGeo.Point3D,
                                      opening_tier_ref_pnt: tuple[AllplanGeo.Point2D, ...]) -> AllplanPalette.RefPointPosition:
        """ select the reference point for the opening symbol

        Args:
            input_pnt:            input point
            opening_tier_ref_pnt: opening tier reference points

        Returns:
            symbol reference point
        """

        place_pnt = input_pnt.To2D

        min_dist      = 1.0e10
        ref_pnt_index = 1

        for index, tier_ref_pnt in enumerate(opening_tier_ref_pnt):
            if (dist := AllplanGeo.Vector2D(place_pnt, tier_ref_pnt).GetLength()) < min_dist:
                min_dist      = dist
                ref_pnt_index = index

        return [AllplanPalette.RefPointPosition.eTopLeft,
                AllplanPalette.RefPointPosition.eTopRight,
                AllplanPalette.RefPointPosition.eBottomRight,
                AllplanPalette.RefPointPosition.eBottomLeft][ref_pnt_index]

```

</details>