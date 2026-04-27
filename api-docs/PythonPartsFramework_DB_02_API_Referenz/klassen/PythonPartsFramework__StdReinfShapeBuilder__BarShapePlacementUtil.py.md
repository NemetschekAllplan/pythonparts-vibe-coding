---
title: "BarShapePlacementUtil"
source: "PythonPartsFramework\StdReinfShapeBuilder\BarShapePlacementUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BarShapePlacementUtil

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\BarShapePlacementUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

Module with the bar shape placement utility class

## Abhängigkeiten

- `GeometryValidate`
- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `StdReinfShapeBuilder.BarPlacementUtil`
- `StdReinfShapeBuilder.RotationAngles`

## Klassen

### `BarShapePlacementUtil`

Implementation of the bar shape placement utility.

This class can be used to calculate the placement of longitudinal bars in relation to
multiple transverse shapes (e.g. stirrup, s-hook). An example use-case is the calculation
of the position of the longitudinal bar in the corner of a stirrup or at the intersection
of the legs of two stirrups.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | Constructor |
| `add_shape` | `self, shape_id: int | str, shape: AllplanReinf.BendingShape` | `None` | Add a shape to the shape list  Args:     shape_id:   ID of the reference shape     shape:      Shape |
| `is_shape_created` | `self, shape_id: int | str` | `bool` | Check if the shape of given id exists in the list  Args:     shape_id:   ID of the reference shape  Returns:     True if shape exists, False otherwise |
| `get_side_length` | `self, shape_id: int | str, side_number: int` | `float` | Gets the leg's length of the given shape  Args:     shape_id:       ID of the reference shape     side_number:    Number of the leg  Return:     Length of the leg |
| `get_placent_line_cover_from_side` | `self, shape_id: int | str, side_number: int, b_above_side: bool` | `tuple[AllplanGeo.Line3D, float]` | Get the placement line cover from a shape leg by side number  Args:     shape_id:       ID of the reference shape     side_number:    Number of the shape leg     b_above_side:   Cover above the side: True/False  Returns:     Placement line     Local placement cover |
| `get_placement_from_bending_roller` | `self, shape_id: int | str, side_number: int, b_roller_start_point: bool, placement_base_line: AllplanGeo.Line2D | AllplanGeo.Line3D, b_placment_start_point: bool, placement_diameter: float, local_angles: RotationAngles` | `float` | Get the placement cover from the bending roller of a defined side number  Args:     shape_id:               ID of the reference shape     side_number:            Number of the shape leg     b_roller_start_point:   True = roller at the start point / False = roller at the end point     placement_base_line:    Base line of the placement     b_placment_start_point: True = placement start point / False = placement end point     placement_diameter:     Diameter of the longitudinal bar     local_angles:           Rotation from global to local coordinate system  Returns:     Local placement cover to a placement base line |
| `get_placement_from_side_intersection` | `self, shape_id1: int | str, side_number1: int, b_above_side1: bool, shape_id2: int | str, side_number2: int, b_above_side2: bool, placement_base_line: AllplanGeo.Line2D, b_placment_start_point: bool, placement_diameter: float, local_angles: RotationAngles` | `float` | Get the placement cover from the side intersection of two defined side numbers.  Args:     shape_id1:              ID of the first shape     side_number1:           Number of the first shape leg     b_above_side1:          Cover above the first side: True/False     shape_id2:              ID of the second shape     side_number2:           Number of the second shape leg     b_above_side2:          Cover above the second side: True/False     placement_base_line:    Base line of the placement     b_placment_start_point: True = placement start point / False = placement end point     placement_diameter:     Diameter of the longitudinal bar     local_angles:           Rotation from global to local coordinate system  Returns:     Local placement cover to a placement base line |
| `get_placement_in_side_intersection` | `self, shape_id1: int | str, side_number1: int, b_above_side1: bool, shape_id2: int | str, side_number2: int, b_above_side2: bool, placement_diameter: float, local_angles: RotationAngles` | `AllplanGeo.Point2D | AllplanGeo.Point3D` | Get the placement point at the intersection of two legs.  Args:     shape_id1:              ID of the first reference shape     side_number1:           Leg number of the first reference shape, beginning with 1     b_above_side1:          True will calculate the placement point above the first leg, False below     shape_id2:              ID of the second reference shape     side_number2:           Leg number of the second reference shape, beginning with 1     b_above_side2:          True will calculate the placement point above the second leg, False below     placement_diameter:     Diameter of the longitudinal bar     local_angles:           Rotation from global to local coordinate system  Returns:     Local placement point |
| `get_placement_at_shape_side` | `self, shape_id: int | str, side_number: int, ref_pnt_fac: float, b_above_side: bool, placement_diameter: float, local_angles: RotationAngles` | `tuple[AllplanGeo.Line2D, float, float]` | Calculate the local placement line at a given leg of the reference shape in its local coordinate system  Args:     shape_id:               ID of the reference shape     side_number:            Number of the leg of the reference shape, beginning with 1     ref_pnt_fac:            Factor for the reference point calculation.                             (-1 = at the side from left to right)     b_above_side:           When set to True, the placement line is created above the leg     placement_diameter:     Diameter of the longitudinal bar     local_angles:           Rotation from global to local coordinate system  Returns:     Placement line in local coordinate system     Cover at the start of the line     Cover at the end of the line |
| `get_placement_at_shape_side_intersection` | `self, shape_id1: int | str, side_number1: int, shape_id2: int | str, side_number2: int, shape_id3: int | str, side_number3: int, b_above_side3: bool, placement_diameter: float, local_angles: RotationAngles` | `tuple[AllplanGeo.Line2D, float, float]` | Calculates the placement line on the specified leg of the third reference shape, starting at the intersection with the leg of the first reference shape and ending a the intersection with leg of the second reference shape.  Args:     shape_id1:              ID of the first reference shape     side_number1:           Number of the leg of the first reference shape, beginning with 1     shape_id2:              ID of the second reference shape     side_number2:           Number of the leg of the second reference shape, beginning with 1     shape_id3:              ID of the third reference shape     side_number3:           Number of the leg of the third reference shape, beginning with 1     b_above_side3:          When True, the placement line will be calculated above the leg, otherwise below     placement_diameter:     Diameter of the longitudinal bar     local_angles:           Rotation from global to local coordinate system  Returns:     Placement line in local coordinate system     Cover at the start of the line     Cover at the end of the line |
| `get_placement_in_corner` | `self, shape_id: int | str, corner_number: int, placement_diameter: float, local_angles: RotationAngles` | `AllplanGeo.Point3D` | Calculate the placement point for a longitudinal bar in the corner of the given reference shape  Args:     shape_id:               ID of the reference shape     corner_number:          Number of the corner in the reference shape, beginning with 1     placement_diameter:     Diameter of the longitudinal bar     local_angles:           Rotation from global to local coordinate system  Returns:     Position of corner bar in the local coordinate system of the reference shape. |
| `get_placement_in_side_corners` | `self, shape_id: int | str, side_number: int, placement_diameter: float, local_angles: RotationAngles` | `tuple[AllplanGeo.Line2D, float, float]` | Calculate the placement line on the entire length of the specified leg of the reference shape.  Note, that the calculation cannot be done in the first leg!  Args:     shape_id:               ID of the reference shape     side_number:            Number of the shape's leg, beginning with 1     placement_diameter:     Diameter of the longitudinal bar     local_angles:           Rotation from global to local coordinate system  Returns:     Placement line in local coordinate system     Cover at the start of the line     Cover at the end of the line |
| `get_placement` | `self, reinf_def, param_dict, diameter, local_angles` | `None` | Calculate the local placement line inside the local X/Y coordinate system of the shapes  Args:     reinf_def:          Reinforcement definition     param_dict:         Parameter dictionary     local_angles:       Rotation from global to local coordinate system  Returns:     Placement line in local coordinate system     Cover at the start of the line     Cover at the end of the line |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""Module with the bar shape placement utility class"""


import GeometryValidate as GeometryValidate
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

from StdReinfShapeBuilder.BarPlacementUtil import (get_placement_end_from_bending_roller, get_placement_inside_bending_roller,
                                                   get_placement_inside_side_intersection, get_placement_start_from_bending_roller)
from StdReinfShapeBuilder.RotationAngles import RotationAngles


class BarShapePlacementUtil:
    """Implementation of the bar shape placement utility.

    This class can be used to calculate the placement of longitudinal bars in relation to
    multiple transverse shapes (e.g. stirrup, s-hook). An example use-case is the calculation
    of the position of the longitudinal bar in the corner of a stirrup or at the intersection
    of the legs of two stirrups.
    """

    def __init__(self):
        """Constructor"""
        self.shapes = {}


    def add_shape(self, shape_id : int|str, shape: AllplanReinf.BendingShape):
        """Add a shape to the shape list

        Args:
            shape_id:   ID of the reference shape
            shape:      Shape
        """

        self.shapes[shape_id] = AllplanReinf.BendingShape(shape)


    def is_shape_created(self, shape_id : int|str) -> bool:
        """Check if the shape of given id exists in the list

        Args:
            shape_id:   ID of the reference shape

        Returns:
            True if shape exists, False otherwise
        """

        return shape_id in self.shapes


    def get_side_length(self, shape_id : int|str, side_number: int) -> float:
        """Gets the leg's length of the given shape

        Args:
            shape_id:       ID of the reference shape
            side_number:    Number of the leg

        Return:
            Length of the leg
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        if side_number > shape_pol.Count():
            print("index error in get_side_length")
            return 0.

        return AllplanGeo.CalcLength(shape_pol.GetLine(side_number - 1))


    def get_placent_line_cover_from_side(self,
                                         shape_id    : int|str,
                                         side_number : int,
                                         b_above_side: bool) -> tuple[AllplanGeo.Line3D, float]:
        """Get the placement line cover from a shape leg by side number

        Args:
            shape_id:       ID of the reference shape
            side_number:    Number of the shape leg
            b_above_side:   Cover above the side: True/False

        Returns:
            Placement line
            Local placement cover
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        rad = shape.GetDiameter() / 2.

        if b_above_side is False:
            rad = -rad

        return AllplanGeo.Line3D(shape_pol[side_number - 1], shape_pol[side_number]), rad


    def get_placement_from_bending_roller(self,
                                          shape_id              : int|str,
                                          side_number           : int,
                                          b_roller_start_point  : bool,
                                          placement_base_line   : AllplanGeo.Line2D|AllplanGeo.Line3D,
                                          b_placment_start_point: bool,
                                          placement_diameter    : float,
                                          local_angles          : RotationAngles) -> float:
        """Get the placement cover from the bending roller of a defined side number

        Args:
            shape_id:               ID of the reference shape
            side_number:            Number of the shape leg
            b_roller_start_point:   True = roller at the start point / False = roller at the end point
            placement_base_line:    Base line of the placement
            b_placment_start_point: True = placement start point / False = placement end point
            placement_diameter:     Diameter of the longitudinal bar
            local_angles:           Rotation from global to local coordinate system

        Returns:
            Local placement cover to a placement base line
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        roller_base_side3d = AllplanGeo.Line3D(shape_pol[side_number - 1], shape_pol[side_number])

        roller_base_side = AllplanGeo.Line2D(AllplanGeo.Transform(roller_base_side3d,
                                                                  local_angles.get_rotation_matrix()))


        #----------------- get the local roller distance to the shape leg

        if b_roller_start_point:
            bending_roller = shape.GetBendingRoller()[side_number - 2]

            cover = get_placement_start_from_bending_roller(shape, side_number, bending_roller,
                                                            roller_base_side, placement_diameter,
                                                            local_angles)

            cover_pnt = AllplanGeo.TransformCoord.PointGlobal(roller_base_side, cover)

        else:
            bending_roller = shape.GetBendingRoller()[side_number - 1]

            cover = get_placement_end_from_bending_roller(shape, side_number, bending_roller,
                                                          roller_base_side, placement_diameter,
                                                          local_angles)

            cover_pnt = AllplanGeo.TransformCoord.PointGlobal(roller_base_side,
                                                              AllplanGeo.CalcLength(roller_base_side) - cover)


        #----------------- get the cover to the placement base side

        if b_placment_start_point:
            return AllplanGeo.TransformCoord.PointLocal(placement_base_line, cover_pnt).X
        else:
            return AllplanGeo.CalcLength(placement_base_line) - \
                AllplanGeo.TransformCoord.PointLocal(placement_base_line, cover_pnt).X


    def get_placement_from_side_intersection(self,
                                             shape_id1             : int|str,
                                             side_number1          : int,
                                             b_above_side1         : bool,
                                             shape_id2             : int|str,
                                             side_number2          : int,
                                             b_above_side2         : bool,
                                             placement_base_line   : AllplanGeo.Line2D,
                                             b_placment_start_point: bool,
                                             placement_diameter    : float,
                                             local_angles          : RotationAngles) -> float:
        """Get the placement cover from the side intersection of two defined side numbers.

        Args:
            shape_id1:              ID of the first shape
            side_number1:           Number of the first shape leg
            b_above_side1:          Cover above the first side: True/False
            shape_id2:              ID of the second shape
            side_number2:           Number of the second shape leg
            b_above_side2:          Cover above the second side: True/False
            placement_base_line:    Base line of the placement
            b_placment_start_point: True = placement start point / False = placement end point
            placement_diameter:     Diameter of the longitudinal bar
            local_angles:           Rotation from global to local coordinate system

        Returns:
            Local placement cover to a placement base line
        """

        place_pnt = get_placement_inside_side_intersection(self.shapes[shape_id1], side_number1,
                                                           b_above_side1,
                                                           self.shapes[shape_id2], side_number2,
                                                           b_above_side2,
                                                           placement_diameter,
                                                           local_angles)

        if b_placment_start_point:
            cover = AllplanGeo.TransformCoord.PointLocal(placement_base_line, place_pnt).X - placement_diameter / 2
        else:
            cover = AllplanGeo.CalcLength(placement_base_line) - AllplanGeo.TransformCoord.PointLocal(
                placement_base_line, place_pnt).X - placement_diameter / 2

        return cover


    def get_placement_in_side_intersection(self,
                                           shape_id1         : int|str,
                                           side_number1      : int,
                                           b_above_side1     : bool,
                                           shape_id2         : int|str,
                                           side_number2      : int,
                                           b_above_side2     : bool,
                                           placement_diameter: float,
                                           local_angles      : RotationAngles) -> AllplanGeo.Point2D|AllplanGeo.Point3D:
        """Get the placement point at the intersection of two legs.

        Args:
            shape_id1:              ID of the first reference shape
            side_number1:           Leg number of the first reference shape, beginning with 1
            b_above_side1:          True will calculate the placement point above the first leg, False below
            shape_id2:              ID of the second reference shape
            side_number2:           Leg number of the second reference shape, beginning with 1
            b_above_side2:          True will calculate the placement point above the second leg, False below
            placement_diameter:     Diameter of the longitudinal bar
            local_angles:           Rotation from global to local coordinate system

        Returns:
            Local placement point
        """

        return get_placement_inside_side_intersection(self.shapes[shape_id1], side_number1,
                                                      b_above_side1,
                                                      self.shapes[shape_id2], side_number2,
                                                      b_above_side2,
                                                      placement_diameter,
                                                      local_angles)

    def get_placement_at_shape_side(self,
                                    shape_id          : int|str,
                                    side_number       : int,
                                    ref_pnt_fac       : float,
                                    b_above_side      : bool,
                                    placement_diameter: float,
                                    local_angles      : RotationAngles) -> tuple[AllplanGeo.Line2D, float, float]:
        """Calculate the local placement line at a given leg of the reference shape in its local coordinate system

        Args:
            shape_id:               ID of the reference shape
            side_number:            Number of the leg of the reference shape, beginning with 1
            ref_pnt_fac:            Factor for the reference point calculation.
                                    (-1 = at the side from left to right)
            b_above_side:           When set to True, the placement line is created above the leg
            placement_diameter:     Diameter of the longitudinal bar
            local_angles:           Rotation from global to local coordinate system

        Returns:
            Placement line in local coordinate system
            Cover at the start of the line
            Cover at the end of the line
        """

        shape_cover_line, concrete_cover = self.get_placent_line_cover_from_side(shape_id, side_number, b_above_side)

        del shape_cover_line

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        placement_base_line3d = AllplanGeo.Line3D(shape_pol[side_number - 1], shape_pol[side_number])

        placement_base_line = AllplanGeo.Line2D(AllplanGeo.Transform(placement_base_line3d,
                                                                     local_angles.get_rotation_matrix()))

        if side_number == 1:
            placement_cover_left = 0
        else:
            placement_cover_left =  \
                self.get_placement_from_bending_roller(shape_id, side_number, True, placement_base_line, True,
                                                       placement_diameter, local_angles)

        if side_number == self.shapes[shape_id].GetShapePolyline().Count() - 1:
            placement_cover_right = 0
        else:
            placement_cover_right = \
                self.get_placement_from_bending_roller(shape_id, side_number, False, placement_base_line, False,
                                                       placement_diameter, local_angles)


        #----------------- Check the intersections

        if ref_pnt_fac != -1:
            dist = placement_diameter / 2. if b_above_side else -placement_diameter / 2.

            err, intersect_line = AllplanGeo.Offset(dist, placement_base_line)

            if not GeometryValidate.offset(err):
                return (AllplanGeo.Line2D(), 0, 0)

            side_length = AllplanGeo.CalcLength(placement_base_line)

            x_ref = side_length * ref_pnt_fac

            for shape_id_iter, shape_iter in self.shapes.items():
                if shape_id_iter != shape_id:
                    polyline = shape_iter.GetShapePolyline()

                    for i_side in range(0, polyline.Count() - 1):
                        if i_side + 1 >= polyline.Count():
                            print("index error in get_placement_at_shape_side")
                            break

                        side_line_3d = polyline.GetLine(i_side)

                        side_line = AllplanGeo.Line2D(AllplanGeo.Transform(side_line_3d,
                                                                           local_angles.get_rotation_matrix()))

                        result, i_pnt = AllplanGeo.IntersectionCalculus(intersect_line, side_line)

                        if result:
                            x_loc = AllplanGeo.TransformCoord.PointLocal(placement_base_line, i_pnt).X


                            #----------------- new left cover

                            if x_loc < x_ref  and  x_loc > placement_cover_left:
                                y_start = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                               side_line.StartPoint).Y
                                y_end = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line.EndPoint).Y

                                b_roller_pnt_start = False
                                b_roller_pnt_end = False


                                #----- check for bending roller at the end point of the line before intersection line

                                if i_side > 0  and abs(y_start) < placement_diameter:
                                    side_line3d_before = polyline.GetLine(i_side - 1)

                                    side_line_before = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_before,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_before.StartPoint).X > \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_before.EndPoint).X:
                                        b_roller_pnt_end = True


                                #----- check for bending roller at the start point of the line after intersection line

                                if i_side < polyline.Count() - 2  and abs(y_end) < placement_diameter:
                                    if i_side + 2 >= polyline.Count():
                                        print("index error in get_placement_at_shape_side")
                                        break

                                    side_line3d_after = polyline.GetLine(i_side + 1)

                                    side_line_after = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_after,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_after.StartPoint).X < \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_after.EndPoint).X:
                                        b_roller_pnt_start = True


                                #----------------- mew cover from bending roller or intersection

                                if b_roller_pnt_start:
                                    placement_cover_left = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side + 2, True, placement_base_line, True, placement_diameter,
                                        local_angles)

                                elif b_roller_pnt_end:
                                    placement_cover_left = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side, False, placement_base_line, True, placement_diameter,
                                        local_angles)

                                else:
                                    place_pnt = get_placement_inside_side_intersection(
                                        shape, side_number, b_above_side,
                                        shape_iter, i_side + 1, y_start > 0., placement_diameter,
                                        local_angles)

                                    placement_cover_left = AllplanGeo.TransformCoord.PointLocal(
                                        placement_base_line, place_pnt).X - placement_diameter / 2


                            #----------------- new right cover

                            elif x_loc > x_ref  and x_loc < side_length - placement_cover_right:
                                y_start = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                               side_line.StartPoint).Y
                                y_end = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line.EndPoint).Y

                                b_roller_pnt_start = False
                                b_roller_pnt_end = False


                                #-------- check for bending roller at the end point of the line before intersection line

                                if i_side > 0  and abs(y_start) < placement_diameter:
                                    side_line3d_before = polyline.GetLine(i_side - 1)

                                    side_line_before = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_before,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_before.StartPoint).X < \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_before.EndPoint).X:
                                        b_roller_pnt_end = True


                                #----- check for bending roller at the start point of the line after intersection line

                                if i_side < polyline.Count() - 2  and abs(y_end) < placement_diameter:
                                    side_line3d_after = polyline.GetLine(i_side)

                                    side_line_after = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_after,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_after.StartPoint).X > \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_after.EndPoint).X:
                                        b_roller_pnt_start = True


                                #----------------- mew cover from bending roller or intersection

                                if b_roller_pnt_start:
                                    placement_cover_right = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side + 2, True, placement_base_line, False, placement_diameter,
                                        local_angles)

                                elif b_roller_pnt_end:
                                    placement_cover_right = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side, False, placement_base_line, False, placement_diameter,
                                        local_angles)
                                else:
                                    place_pnt = get_placement_inside_side_intersection(
                                        shape, side_number, b_above_side,
                                        shape_iter, i_side + 1, y_start < 0., placement_diameter,
                                        local_angles)

                                    placement_cover_right = side_length - AllplanGeo.TransformCoord.PointLocal(
                                        placement_base_line, place_pnt).X - placement_diameter / 2


        #----------------- calculate the placement line

        if concrete_cover > 0.:
            concrete_cover += placement_diameter / 2

        elif concrete_cover < 0.:
            concrete_cover -= placement_diameter / 2

        err, placement_line_local = AllplanGeo.Offset(concrete_cover, placement_base_line)

        if not GeometryValidate.offset(err):
            return (AllplanGeo.Line2D(), 0, 0)

        return (placement_line_local, placement_cover_left, placement_cover_right)


    def get_placement_at_shape_side_intersection(self,
                                                 shape_id1         : int|str,
                                                 side_number1      : int,
                                                 shape_id2         : int|str,
                                                 side_number2      : int,
                                                 shape_id3         : int|str,
                                                 side_number3      : int,
                                                 b_above_side3     : bool,
                                                 placement_diameter: float,
                                                 local_angles      : RotationAngles) -> tuple[AllplanGeo.Line2D, float, float]:
        """Calculates the placement line on the specified leg of the third reference shape, starting at the
        intersection with the leg of the first reference shape and ending a the intersection with leg of the
        second reference shape.

        Args:
            shape_id1:              ID of the first reference shape
            side_number1:           Number of the leg of the first reference shape, beginning with 1
            shape_id2:              ID of the second reference shape
            side_number2:           Number of the leg of the second reference shape, beginning with 1
            shape_id3:              ID of the third reference shape
            side_number3:           Number of the leg of the third reference shape, beginning with 1
            b_above_side3:          When True, the placement line will be calculated above the leg, otherwise below
            placement_diameter:     Diameter of the longitudinal bar
            local_angles:           Rotation from global to local coordinate system

        Returns:
            Placement line in local coordinate system
            Cover at the start of the line
            Cover at the end of the line
        """
        shape = self.shapes[shape_id3]

        shape_pol = shape.GetShapePolyline()

        placement_base_line3d = AllplanGeo.Line3D(shape_pol[side_number3 - 1], shape_pol[side_number3])

        placement_base_line = AllplanGeo.Line2D(AllplanGeo.Transform(placement_base_line3d,
                                                                     local_angles.get_rotation_matrix()))

        b_above_side1 = True
        b_above_side2 = True

        pnt_1_3 = self.get_placement_in_side_intersection(shape_id1, side_number1, b_above_side1,
                                                          shape_id3, side_number3, b_above_side3,
                                                          placement_diameter, local_angles)

        pnt_2_3 = self.get_placement_in_side_intersection(shape_id2, side_number2, b_above_side2,
                                                          shape_id3, side_number3, b_above_side3,
                                                          placement_diameter, local_angles)

        length_3 = self.get_side_length(shape_id3, side_number3)

        pnt_1 = AllplanGeo.TransformCoord.PointLocal(placement_base_line, pnt_1_3).X
        pnt_2 = AllplanGeo.TransformCoord.PointLocal(placement_base_line, pnt_2_3).X

        diff_pnt_1_2 = abs((pnt_1 - pnt_2) / 2.)

        ref_pnt = pnt_1
        if pnt_1 > pnt_2 :
            ref_pnt = pnt_2

        ref_pnt = ref_pnt + diff_pnt_1_2

        ref_pnt_fac = ref_pnt / length_3

        return self.get_placement_at_shape_side(shape_id3, side_number3, ref_pnt_fac, b_above_side3,
                                                placement_diameter,
                                                local_angles)


    def get_placement_in_corner(self,
                                shape_id          : int|str,
                                corner_number     : int,
                                placement_diameter: float,
                                local_angles      : RotationAngles) -> AllplanGeo.Point3D:
        """ Calculate the placement point for a longitudinal bar in the corner of the given reference shape

        Args:
            shape_id:               ID of the reference shape
            corner_number:          Number of the corner in the reference shape, beginning with 1
            placement_diameter:     Diameter of the longitudinal bar
            local_angles:           Rotation from global to local coordinate system

        Returns:
            Position of corner bar in the local coordinate system of the reference shape.
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        if corner_number > shape_pol.Count():
            return AllplanGeo.Point3D()

        placement_base_line3d = AllplanGeo.Line3D(shape_pol[corner_number - 1], shape_pol[corner_number])

        AllplanGeo.Line2D(AllplanGeo.Transform(placement_base_line3d, local_angles.get_rotation_matrix()))

        bending_roller = shape.GetBendingRoller()

        if corner_number > len(bending_roller):
            return AllplanGeo.Point3D()

        bending_roller = bending_roller[corner_number - 1]

        return get_placement_inside_bending_roller(shape, corner_number, bending_roller, placement_diameter,
                                                   local_angles)


    def get_placement_in_side_corners(self,
                                      shape_id          : int|str,
                                      side_number       : int,
                                      placement_diameter: float,
                                      local_angles      : RotationAngles) -> tuple[AllplanGeo.Line2D, float, float]:
        """Calculate the placement line on the entire length of the specified leg of the reference shape.

        Note, that the calculation cannot be done in the first leg!

        Args:
            shape_id:               ID of the reference shape
            side_number:            Number of the shape's leg, beginning with 1
            placement_diameter:     Diameter of the longitudinal bar
            local_angles:           Rotation from global to local coordinate system

        Returns:
            Placement line in local coordinate system
            Cover at the start of the line
            Cover at the end of the line
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        bending_roller_list = shape.GetBendingRoller()

        if side_number - 1 >= len(bending_roller_list):
            return (AllplanGeo.Line2D(), 0, 0)

        bending_roller = bending_roller_list[side_number - 2]

        corner_pnt1 = get_placement_inside_bending_roller(shape, side_number - 1, bending_roller, placement_diameter,
                                                          local_angles)

        bending_roller = bending_roller_list[side_number - 1]

        corner_pnt2 = get_placement_inside_bending_roller(shape, side_number, bending_roller, placement_diameter,
                                                          local_angles)

        place_line_axis = AllplanGeo.Line2D(AllplanGeo.Point2D(corner_pnt1), AllplanGeo.Point2D(corner_pnt2))

        place_line_axis.TrimStart(-placement_diameter / 2.)
        place_line_axis.TrimEnd(-placement_diameter / 2.)

        return (place_line_axis, 0, 0)


    def get_placement(self,
                      reinf_def,
                      param_dict,
                      diameter,
                      local_angles):
        """Calculate the local placement line inside the local X/Y coordinate system of the shapes

        Args:
            reinf_def:          Reinforcement definition
            param_dict:         Parameter dictionary
            local_angles:       Rotation from global to local coordinate system

        Returns:
            Placement line in local coordinate system
            Cover at the start of the line
            Cover at the end of the line
        """

        diameter_str =  reinf_def.get_attribute("Diameter")

        angle_str = ",local_angles"

        param_dict["local_angles"] = local_angles


        #----------------- placement in the shape corner, at the shape

        placement =  reinf_def.get_attribute("Placement")

        if placement:
            if placement.find("in_corner") != -1:
                placement = "ShapePlaceUtil.get_placement_" + placement

                placement = placement.replace(")", "," + diameter_str + angle_str + ")")

                corner_pnt = AllplanGeo.Point2D(eval(placement, param_dict))

                return (AllplanGeo.Line2D(corner_pnt, corner_pnt), 0, 0)

            elif placement.find("in_side_intersection") != -1:
                placement = "ShapePlaceUtil.get_placement_" + placement

                placement = placement.replace(")", "," + diameter_str + angle_str + ")")

                corner_pnt = AllplanGeo.Point2D(eval(placement, param_dict))

                return (AllplanGeo.Line2D(corner_pnt, corner_pnt), 0, 0)


            #----------------- placement at the shape leg

            else:
                placement = "ShapePlaceUtil.get_placement_" + placement

                placement = placement.replace(")", "," + diameter_str + angle_str + ")")

                return eval(placement, param_dict)


        #--------------- get the single placement cover values

        else:
            shape_cover_line3d, concrete_cover = eval(
                "ShapePlaceUtil.get_placent_line_cover_" + reinf_def.get_attribute("ConcreteCoverShape"), param_dict)

            shape_cover_line = AllplanGeo.Line2D(AllplanGeo.Transform(shape_cover_line3d,
                                                                      local_angles.get_rotation_matrix()))

            placement_cover_left_str  = reinf_def.get_attribute("PlacementCoverLeft")
            placement_cover_right_str = reinf_def.get_attribute("PlacementCoverRight")

            param_dict["ShapeCoverLine"] = shape_cover_line

            if placement_cover_left_str.find("from") != -1:
                placement_cover_left_str = placement_cover_left_str.replace(
                    ")", ",ShapeCoverLine,True," + diameter_str + angle_str + ")")

                placement_cover_left_str = "ShapePlaceUtil.get_placement_" + placement_cover_left_str

                placement_cover_left = eval(placement_cover_left_str, param_dict)
            else:
                placement_cover_left = eval(placement_cover_left_str, param_dict)

            if placement_cover_right_str.find("from") != -1:
                placement_cover_right_str = placement_cover_right_str.replace(
                    ")", ",ShapeCoverLine,False," + diameter_str + angle_str + ")")

                placement_cover_right_str = "ShapePlaceUtil.get_placement_" + placement_cover_right_str

                placement_cover_right = eval(placement_cover_right_str, param_dict)
            else:
                placement_cover_right = eval(placement_cover_right_str, param_dict)


        #----------------- calculate the placement line

        if concrete_cover > 0.:
            concrete_cover += diameter / 2

        elif concrete_cover < 0.:
            concrete_cover -= diameter / 2

        err, placement_line_local = AllplanGeo.Offset(concrete_cover,
                                                      AllplanGeo.Line2D(shape_cover_line.StartPoint,
                                                                        shape_cover_line.EndPoint))

        if not GeometryValidate.offset(err):
            return (AllplanGeo.Line2D(), 0, 0)

        return (placement_line_local, placement_cover_left, placement_cover_right)

```

</details>