---
title: "OpeningHandlesUtil"
source: "PythonPartsFramework\Utils\Architecture\OpeningHandlesUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningHandlesUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\OpeningHandlesUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `utility`

## Übersicht

implementation of the opening handles utilities

## Abhängigkeiten

- `NemAll_Python_ArchElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Palette`
- `TypeCollections.HandleList`
- `Utils.HandleCreator`
- `math`

## Klassen

### `OpeningHandlesUtil`

implementation of the opening handles utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_opening_handles` | `opening_start_pnt: AllplanGeo.Point2D, opening_end_pnt: AllplanGeo.Point2D, offset_start_pnt: AllplanGeo.Point3D, offset_end_pnt: AllplanGeo.Point3D, element_axis: AllplanGeo.Line2D | AllplanGeo.Arc2D, placement_arc: AllplanGeo.Arc2D | None, input_field_above: bool, bottom_pnt: AllplanGeo.Point3D, handle_list: HandleList` | `None` | create the opening handles  Args:     opening_start_pnt: start point of the opening     opening_end_pnt:   end point of the opening     offset_start_pnt:  start offset point of the opening     offset_end_pnt:    end offset point of the opening     element_axis:      element axis     placement_arc:     placement arc of the opening     input_field_above: input field above the dimension line state     bottom_pnt:        bottom of the opening     handle_list:       handle list |
| `create_opening_depth_handle` | `opening_start_pnt: AllplanGeo.Point2D, element_axis: AllplanGeo.Line2D | AllplanGeo.Arc2D, element_polygon: AllplanGeo.Polygon2D | AllplanGeo.Polyline2D, placement_line: AllplanGeo.Line2D, placement_arc: AllplanGeo.Arc2D | None, bottom_pnt: AllplanGeo.Point3D, depth: float, handle_list: HandleList` | `None` | create the opening depth handle  Args:     opening_start_pnt: start point of the opening     element_axis:      element axis     element_polygon:   element polygon / polyline     placement_line:    placement line     placement_arc:     placement arc of the opening     bottom_pnt:        bottom of the opening     depth:             depth of the opening     handle_list:       handle list |
| `__create_arc_opening_handles` | `placement_arc: AllplanGeo.Arc2D | None, opening_start_pnt: AllplanGeo.Point3D, opening_end_pnt: AllplanGeo.Point3D, offset_start_pnt: AllplanGeo.Point3D, offset_end_pnt: AllplanGeo.Point3D, input_field_above: bool, handle_list: HandleList` | `None` | create the handles for an arc opening  Args:     placement_arc:     placement arc of the opening     opening_start_pnt: start point of the opening     opening_end_pnt:   end point of the opening     offset_start_pnt:  start offset point of the opening     offset_end_pnt:    end offset point of the opening     input_field_above: input field above the dimension line state     handle_list:       handle list |
| `create_opening_symbol_handles` | `opening_start_pnt: AllplanGeo.Point2D, opening_end_pnt: AllplanGeo.Point2D, width: float, depth: float, placement_ele: AllplanEleAdapter.BaseElementAdapter, opening_tier_index: int, has_tier_handle: bool, symbol_ref_pnt_index: AllplanPalette.RefPointPosition, bottom_pnt: AllplanGeo.Point3D, handle_list: HandleList` | `tuple[list[AllplanGeo.Point2D], tuple[AllplanGeo.Point2D, ...]]` | create the handles for the opening symbol  Args:     opening_start_pnt:    start point of the opening     opening_end_pnt:      end point of the opening     width:                with of the opening     depth:                depth of the opening     placement_ele:        placement element of the opening     opening_tier_index:   tier index of the symbol     has_tier_handle:      has a tier handle     symbol_ref_pnt_index: reference point index of the symbol     bottom_pnt:           bottom of the opening     handle_list:          handle list  Returns:     opening tier centers, opening symbol ref points |
| `create_door_swing_handle` | `opening_start_pnt: AllplanGeo.Point2D, opening_end_pnt: AllplanGeo.Point2D, width: float, element_thickness: float, door_swing_base_point_index: int, handle_list: HandleList` | `None` | create the door swing handle  Args:     opening_start_pnt:           start point of the opening     opening_end_pnt:             end point of the opening     width:                       with of the opening     element_thickness:           element thickness     door_swing_base_point_index: door swing base point index     handle_list:                 handle list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening handles utilities
"""

import math

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Palette as AllplanPalette

from TypeCollections.HandleList import HandleList

from Utils.HandleCreator import HandleCreator

class OpeningHandlesUtil():
    """ implementation of the opening handles utilities
    """

    @staticmethod
    def create_opening_handles(opening_start_pnt: AllplanGeo.Point2D,
                               opening_end_pnt  : AllplanGeo.Point2D,
                               offset_start_pnt : AllplanGeo.Point3D,
                               offset_end_pnt   : AllplanGeo.Point3D,
                               element_axis     : (AllplanGeo.Line2D | AllplanGeo.Arc2D),
                               placement_arc    : (AllplanGeo.Arc2D | None),
                               input_field_above: bool,
                               bottom_pnt       : AllplanGeo.Point3D,
                               handle_list      : HandleList):
        """ create the opening handles

        Args:
            opening_start_pnt: start point of the opening
            opening_end_pnt:   end point of the opening
            offset_start_pnt:  start offset point of the opening
            offset_end_pnt:    end offset point of the opening
            element_axis:      element axis
            placement_arc:     placement arc of the opening
            input_field_above: input field above the dimension line state
            bottom_pnt:        bottom of the opening
            handle_list:       handle list
        """

        opening_start_pnt_3d = opening_start_pnt.To3D + bottom_pnt
        opening_end_pnt_3d   = opening_end_pnt.To3D + bottom_pnt


        #----------------- width input controls

        HandleCreator.point_distance(handle_list, "Width", opening_end_pnt_3d, opening_start_pnt_3d,
                                     show_handles = False, input_field_above = False)


        #----------------- handles for the circular axis

        if isinstance(element_axis, AllplanGeo.Arc2D):
            OpeningHandlesUtil.__create_arc_opening_handles(placement_arc, opening_start_pnt_3d, opening_end_pnt_3d,
                                                            offset_start_pnt, offset_end_pnt, input_field_above, handle_list)

        #----------------- handles for the linear axis

        else:
            offset_start_pnt     = offset_start_pnt + bottom_pnt
            offset_end_pnt       = offset_end_pnt + bottom_pnt

            if isinstance(element_axis, AllplanGeo.Line2D):
                HandleCreator.point_distance(handle_list, "StartPoint", opening_start_pnt_3d, offset_start_pnt, input_field_above = False)
                HandleCreator.point_distance(handle_list, "EndPoint", opening_end_pnt_3d, offset_end_pnt)
                HandleCreator.point_distance(handle_list, "OffsetStartPoint", offset_start_pnt, opening_end_pnt_3d, False)
                HandleCreator.point_distance(handle_list, "OffsetEndPoint", offset_end_pnt, opening_start_pnt_3d, False)

            else:
                HandleCreator.point(handle_list, "StartPoint", opening_start_pnt_3d)
                HandleCreator.point(handle_list, "EndPoint", opening_end_pnt_3d)


    @staticmethod
    def create_opening_depth_handle(opening_start_pnt: AllplanGeo.Point2D,
                                    element_axis     : (AllplanGeo.Line2D | AllplanGeo.Arc2D),
                                    element_polygon  : (AllplanGeo.Polygon2D | AllplanGeo.Polyline2D),
                                    placement_line   : AllplanGeo.Line2D,
                                    placement_arc    : (AllplanGeo.Arc2D | None),
                                    bottom_pnt       : AllplanGeo.Point3D,
                                    depth            : float,
                                    handle_list      : HandleList):
        """ create the opening depth handle

        Args:
            opening_start_pnt: start point of the opening
            element_axis:      element axis
            element_polygon:   element polygon / polyline
            placement_line:    placement line
            placement_arc:     placement arc of the opening
            bottom_pnt:        bottom of the opening
            depth:             depth of the opening
            handle_list:       handle list
        """

        if placement_arc is None:
            return

        if isinstance(element_axis, AllplanGeo.Line2D):
            x_start = AllplanGeo.TransformCoord.PointLocal(placement_line, opening_start_pnt).X

            depth_pnt = AllplanGeo.TransformCoord.PointGlobal(placement_line, AllplanGeo.Point2D(x_start, depth))

            HandleCreator.point_distance(handle_list, "Depth", depth_pnt + bottom_pnt, opening_start_pnt.To3D + bottom_pnt)

        elif isinstance(element_axis, AllplanGeo.Arc2D):
            x_start = AllplanGeo.TransformCoord.PointLocal(placement_arc, opening_start_pnt).X

            depth_pnt = AllplanGeo.TransformCoord.PointGlobal(placement_arc, AllplanGeo.Point2D(x_start, depth))

            depth_ref_pnt = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, opening_start_pnt.To3D)[1]

            HandleCreator.point_distance(handle_list, "Depth", depth_pnt + bottom_pnt, bottom_pnt + depth_ref_pnt)

        else:
            _, segment_line = AllplanGeo.Polyline2DUtil.GetPolyline2DSegment(AllplanGeo.Polyline2D(element_polygon.Points),
                                                                             opening_start_pnt.To2D)

            x_start = AllplanGeo.TransformCoord.PointLocal(segment_line, opening_start_pnt).X

            depth_pnt = AllplanGeo.TransformCoord.PointGlobal(segment_line, AllplanGeo.Point2D(x_start, depth))

            HandleCreator.point_distance(handle_list, "Depth", depth_pnt + bottom_pnt, opening_start_pnt + bottom_pnt)


    @staticmethod
    def __create_arc_opening_handles(placement_arc    : (AllplanGeo.Arc2D | None),
                                     opening_start_pnt: AllplanGeo.Point3D,
                                     opening_end_pnt  : AllplanGeo.Point3D,
                                     offset_start_pnt : AllplanGeo.Point3D,
                                     offset_end_pnt   : AllplanGeo.Point3D,
                                     input_field_above: bool,
                                     handle_list      : HandleList):
        """ create the handles for an arc opening

        Args:
            placement_arc:     placement arc of the opening
            opening_start_pnt: start point of the opening
            opening_end_pnt:   end point of the opening
            offset_start_pnt:  start offset point of the opening
            offset_end_pnt:    end offset point of the opening
            input_field_above: input field above the dimension line state
            handle_list:       handle list
        """

        if placement_arc is None:
            return

        if placement_arc.CounterClockwise:
            start_offset_pnt1 = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, offset_start_pnt)[1]
            start_offset_pnt2 = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, opening_start_pnt)[1]
            end_offset_pnt1   = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, opening_end_pnt)[1]
            end_offset_pnt2   = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, offset_end_pnt)[1]
            offset_start_pnt  = start_offset_pnt1
            offset_end_pnt    = end_offset_pnt2
        else:
            start_offset_pnt1 = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, opening_start_pnt)[1]
            start_offset_pnt2 = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, offset_start_pnt)[1]
            end_offset_pnt1   = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, offset_end_pnt)[1]
            end_offset_pnt2   = AllplanGeo.PerpendicularCalculus.Calculate(placement_arc, opening_end_pnt)[1]
            offset_start_pnt  = start_offset_pnt2
            offset_end_pnt    = end_offset_pnt1

        if abs(placement_arc.MinorRadius - placement_arc.MajorRadius) < 1.:
            if placement_arc.CounterClockwise:
                HandleCreator.point_distance(handle_list, "StartPoint", start_offset_pnt1, start_offset_pnt2,
                                             show_handles      = False,
                                             input_field_above = input_field_above,
                                             center_point      = placement_arc.Center.To3D)
                HandleCreator.point_distance(handle_list, "StartPoint", start_offset_pnt2, start_offset_pnt1,
                                             has_input_field = False,
                                             center_point    = placement_arc.Center.To3D)
            else:
                HandleCreator.point_distance(handle_list, "StartPoint", start_offset_pnt1, start_offset_pnt2,
                                             input_field_above = input_field_above,
                                             center_point      = placement_arc.Center.To3D)

            HandleCreator.point_distance(handle_list, "EndPoint", opening_end_pnt, end_offset_pnt2, False,
                                         center_point = placement_arc.Center.To3D)

            HandleCreator.point_distance(handle_list, "EndOffset", end_offset_pnt1, end_offset_pnt2,
                                         show_handles      = False,
                                         input_field_above = input_field_above,
                                         center_point      = placement_arc.Center.To3D)

            HandleCreator.point_distance(handle_list, "OffsetStartPoint", offset_start_pnt, end_offset_pnt1, False,
                                        center_point = placement_arc.Center.To3D)
            HandleCreator.point_distance(handle_list, "OffsetEndPoint", offset_end_pnt, start_offset_pnt2, False,
                                        center_point = placement_arc.Center.To3D)
        else:
            HandleCreator.move(handle_list, "StartPoint", start_offset_pnt2, "", False)
            HandleCreator.move(handle_list, "EndPoint", end_offset_pnt2, "", False)


    @staticmethod
    def create_opening_symbol_handles(opening_start_pnt   : AllplanGeo.Point2D,
                                      opening_end_pnt     : AllplanGeo.Point2D,
                                      width               : float,
                                      depth               : float,
                                      placement_ele       : AllplanEleAdapter.BaseElementAdapter,
                                      opening_tier_index  : int,
                                      has_tier_handle     : bool,
                                      symbol_ref_pnt_index: AllplanPalette.RefPointPosition,
                                      bottom_pnt          : AllplanGeo.Point3D,
                                      handle_list         : HandleList) -> tuple[list[AllplanGeo.Point2D],
                                                                                             tuple[AllplanGeo.Point2D, ...]]:
        """ create the handles for the opening symbol

        Args:
            opening_start_pnt:    start point of the opening
            opening_end_pnt:      end point of the opening
            width:                with of the opening
            depth:                depth of the opening
            placement_ele:        placement element of the opening
            opening_tier_index:   tier index of the symbol
            has_tier_handle:      has a tier handle
            symbol_ref_pnt_index: reference point index of the symbol
            bottom_pnt:           bottom of the opening
            handle_list:          handle list

        Returns:
            opening tier centers, opening symbol ref points
        """

        #----------------- handle for the opening symbol move

        opening_line = AllplanGeo.Line2D(opening_start_pnt, opening_end_pnt)

        opening_tier_center : list[AllplanGeo.Point2D]       = []
        opening_tier_ref_pnt: tuple[AllplanGeo.Point2D, ...] = tuple()

        x_length = AllplanGeo.CalcLength(opening_line)
        x_center = x_length / 2
        y_start  = 0

        symbol_ref_pnt = AllplanGeo.Point2D()

        if placement_ele.GetElementAdapterType().IsTypeGroup(AllplanEleAdapter.ElementAdapterTypeGroup.eHYPERELEMENT_GROUP) and \
           AllplanEleAdapter.BaseElementAdapterChildElementsService.GetTierElements(placement_ele) != []:    # pylint: disable=consider-ternary-expression
            tier_thickness = AllplanEleAdapter.AxisElementAdapter(placement_ele).GetTierThickness()
        else:
            tier_thickness = (depth,)

        is_top_ref_pnt  = symbol_ref_pnt_index in {AllplanPalette.RefPointPosition.eTopLeft, AllplanPalette.RefPointPosition.eTopRight}

        dx = 0 if symbol_ref_pnt_index in {AllplanPalette.RefPointPosition.eBottomLeft, AllplanPalette.RefPointPosition.eTopLeft} else width

        is_placement_at_first_tier = \
            AllplanArchEle.ArchitectureElementsGeometryService.IsOpeningPlacementAtFirstTier(placement_ele,
                                                                                             opening_start_pnt, opening_end_pnt)

        opening_tier_index =  opening_tier_index - 1 if is_placement_at_first_tier else len(tier_thickness) - opening_tier_index


        #----------------- create the center point of the tier and the symbol tier reference points

        for index, tier_thickness in enumerate(tier_thickness):
            opening_tier_center.append(
                AllplanGeo.TransformCoord.PointGlobal(opening_line,
                                                      AllplanGeo.Point2D(x_center, y_start + tier_thickness / 2)).To2D)

            if index == opening_tier_index:
                opening_tier_ref_pnt = \
                    (AllplanGeo.TransformCoord.PointGlobal(opening_line, AllplanGeo.Point2D(0, y_start + tier_thickness)).To2D,
                     AllplanGeo.TransformCoord.PointGlobal(opening_line, AllplanGeo.Point2D(x_length, y_start + tier_thickness)).To2D,
                     AllplanGeo.TransformCoord.PointGlobal(opening_line, AllplanGeo.Point2D(x_length, y_start)).To2D,
                     AllplanGeo.TransformCoord.PointGlobal(opening_line, AllplanGeo.Point2D(0, y_start)).To2D)

                y_ref_pnt = y_start + 500 if is_top_ref_pnt else y_start + tier_thickness - 500

                symbol_ref_pnt = AllplanGeo.TransformCoord.PointGlobal(opening_line, AllplanGeo.Point2D(dx, y_ref_pnt)).To2D

            y_start += tier_thickness


        #----------------- create the symbol placement and reference point handle

        if has_tier_handle:
            HandleCreator.move_in_direction(handle_list, "SymbolPlacement",
                                            opening_tier_center[opening_tier_index].To3D + bottom_pnt,
                                            AllplanGeo.CalcAngle(opening_line)[0] + AllplanGeo.Angle(math.pi / 2),
                                            "Move the symbol to the tier")

        HandleCreator.move(handle_list, "SymbolRefPoint", symbol_ref_pnt.To3D + bottom_pnt, "Move the symbol reference point")

        handle_list[-1].handle_type = AllplanIFW.ElementHandleType.HANDLE_ARROW

        if not is_placement_at_first_tier:
            opening_tier_center.reverse()

        return opening_tier_center, opening_tier_ref_pnt


    @staticmethod
    def create_door_swing_handle(opening_start_pnt          : AllplanGeo.Point2D,
                                 opening_end_pnt            : AllplanGeo.Point2D,
                                 width                      : float,
                                 element_thickness          : float,
                                 door_swing_base_point_index: int,
                                 handle_list                : HandleList):
        """ create the door swing handle

        Args:
            opening_start_pnt:           start point of the opening
            opening_end_pnt:             end point of the opening
            width:                       with of the opening
            element_thickness:           element thickness
            door_swing_base_point_index: door swing base point index
            handle_list:                 handle list
        """

        base_line = AllplanGeo.Line2D(opening_start_pnt, opening_end_pnt)

        handle_pnt = AllplanGeo.TransformCoord.PointGlobal(base_line, AllplanGeo.Point2D(width / 2, -width / 2)) \
                        if door_swing_base_point_index in {1, 2} else \
                     AllplanGeo.TransformCoord.PointGlobal(base_line, AllplanGeo.Point2D(width / 2, element_thickness / 2 + width / 2))

        HandleCreator.point(handle_list, "DoorSwing", handle_pnt, info_text = "Door swing placement")

        handle_list[-1].handle_type = AllplanIFW.ElementHandleType.HANDLE_ARROW

```

</details>