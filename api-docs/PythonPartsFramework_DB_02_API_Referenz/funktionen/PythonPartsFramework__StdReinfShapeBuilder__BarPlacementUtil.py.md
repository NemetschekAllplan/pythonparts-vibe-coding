---
title: "BarPlacementUtil"
source: "PythonPartsFramework\StdReinfShapeBuilder\BarPlacementUtil.py"
type: "module"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BarPlacementUtil

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\BarPlacementUtil.py`  
> **Typ:** Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

Implementation of the bar placement utilities

## Abhängigkeiten

- `GeometryValidate`
- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `StdReinfShapeBuilder.RotationAngles`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `get_placement_start_from_bending_roller(shape: AllplanReinf.BendingShape, side_number: int, bending_roller: float, base_line: AllplanGeo.Line2D | AllplanGeo.Line3D, placement_diameter: float, local_angles: RotationAngles)`

For the placement of longitudinal bars, located on one of the legs of a transverse bar
(e.g. a stirrup), this function calculates the X-component between the edge of the
concrete cross-section and the start point of the placement of the longitudinal bars

    │    │           │    │
    │    │           │    │
    │    │ o   o   o │ <- longitudinal bars
    │    ╰───────────╯ <- transverse bar (e.g. stirrup)
    │                     │
    └─────────────────────┘ outline
    <-----> calculated distance

Args:
    shape:              Bending shape of the transverse bar
    side_number:        Number of the leg, on which the longitudinal bars are located (starting from 1)
    bending_roller:     Bending roller if the transverse bar
    base_line:          The outline of the concrete cross section
    placement_diameter: Bar diameter of the longitudinal bars
    local_angles:       Model angles to get the local x/y coordinate system for the calculation

Returns:
    Calculated distance to the placement start

**Parameter:**
- `shape: AllplanReinf.BendingShape`
- `side_number: int`
- `bending_roller: float`
- `base_line: AllplanGeo.Line2D | AllplanGeo.Line3D`
- `placement_diameter: float`
- `local_angles: RotationAngles`

**Rückgabe:** `float`

**Beispiel:**
```python
result = get_placement_start_from_bending_roller(..., ..., ..., ..., ..., ...)
```

### `get_placement_end_from_bending_roller(shape: AllplanReinf.BendingShape, side_number: int, bending_roller: float, base_line: AllplanGeo.Line2D | AllplanGeo.Line3D, placement_diameter: float, local_angles: RotationAngles)`

For the placement of longitudinal bars, located on one of the legs of a transverse bar
(e.g. a stirrup), this function calculates the X-component between the edge of the
concrete cross-section and the end point of the placement of the longitudinal bars

    │    │           │    │
    │    │           │    │
    │    │ o   o   o │ <- longitudinal bars
    │    ╰───────────╯ <- transverse bar (e.g. stirrup)
    │                     │
    └─────────────────────┘ outline
                    <-----> calculated distance

Args:
    shape:              Bending shape of the transverse bar
    side_number:        Number of the leg, on which the longitudinal bars are located (starting from 1)
    bending_roller:     Bending roller if the transverse bar
    base_line:          The outline of the concrete cross section
    placement_diameter: Bar diameter of the longitudinal bars
    local_angles:       Model angles to get the local x/y coordinate system for the calculation

Returns:
    Calculated distance to the placement end

**Parameter:**
- `shape: AllplanReinf.BendingShape`
- `side_number: int`
- `bending_roller: float`
- `base_line: AllplanGeo.Line2D | AllplanGeo.Line3D`
- `placement_diameter: float`
- `local_angles: RotationAngles`

**Rückgabe:** `float`

**Beispiel:**
```python
result = get_placement_end_from_bending_roller(..., ..., ..., ..., ..., ...)
```

### `get_placement_inside_bending_roller(shape: AllplanReinf.BendingShape, corner_number: int, bending_roller: float, placement_diameter: float, local_angles: RotationAngles, global_point: bool=False)`

Calculate the position of a placement inside the bending roller

    │ │
    │ │ X  <--- calculated point
    │ ╰────────
    ╰────────── transverse bar (e.g. stirrup)

Args:
    shape:              Bending shape of the transverse bar
    corner_number:      Number of the transverse bar's corner, in which the placement point
                        should be calculated (starting from 1)
    bending_roller:     Bending roller of the transverse bar
    placement_diameter: Bar diameter of the longitudinal bar
    local_angles:       Model angles to get the local x/y coordinate system for the calculation
    global_point:       If set to True, the result will be a point in global coordinates.
                        Otherwise, the point in local coordinate system will be returned.

Returns:
    Local point of the longitudinal bar placement

**Parameter:**
- `shape: AllplanReinf.BendingShape`
- `corner_number: int`
- `bending_roller: float`
- `placement_diameter: float`
- `local_angles: RotationAngles`
- `global_point: bool=False`

**Rückgabe:** `AllplanGeo.Point3D`

**Beispiel:**
```python
result = get_placement_inside_bending_roller(..., ..., ..., ..., ..., ...)
```

### `get_placement_inside_side_intersection(shape1: AllplanReinf.BendingShape, side_number1: int, above_side1: bool, shape2: AllplanReinf.BendingShape, side_number2: int, above_side2: bool, placement_diameter: float, local_angles: RotationAngles, global_point: bool=False)`

Calculate the position of a longitudinal bar placed at an intersection of two
legs of transverse bars (e.g. two stirrups)

    ║ ┌─ calculated placement point
    ║ x    ║   ║
    ╬══════╝<--first shape
    ║          ║
    ╚══════════╝<--second shape

Args:
    shape1:             Shape of the first transverse rebar
    side_number1:       Number of the leg in the first shape to consider in the calculation (starting from 1)
    above_side1:        When set to True, the point will be calculated above the leg of the first shape.
                        Otherwise below.
    shape2:             Shape of the second transverse rebar
    side_number2:       Number of the leg in the second shape to consider in the calculation (starting from 1)
    above_side2:        When set to True, the point will be calculated above the leg of the second shape.
                        Otherwise below.
    placement_diameter: Bar diameter of the longitudinal bar
    local_angles:       Model angles to get the local x/y coordinate system for the calculation
    global_point:       If set to True, the result will be a 3D point in global coordinates.
                        Otherwise, a 2D point in local coordinate system will be returned.

Returns:
    local placement point as Point2D

**Parameter:**
- `shape1: AllplanReinf.BendingShape`
- `side_number1: int`
- `above_side1: bool`
- `shape2: AllplanReinf.BendingShape`
- `side_number2: int`
- `above_side2: bool`
- `placement_diameter: float`
- `local_angles: RotationAngles`
- `global_point: bool=False`

**Rückgabe:** `AllplanGeo.Point2D | AllplanGeo.Point3D`

**Beispiel:**
```python
result = get_placement_inside_side_intersection(..., ..., ..., ..., ..., ..., ..., ..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""Implementation of the bar placement utilities"""

import GeometryValidate as GeometryValidate
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

from StdReinfShapeBuilder.RotationAngles import RotationAngles


def get_placement_start_from_bending_roller(shape             : AllplanReinf.BendingShape,
                                            side_number       : int,
                                            bending_roller    : float,
                                            base_line         : AllplanGeo.Line2D | AllplanGeo.Line3D,
                                            placement_diameter: float,
                                            local_angles      : RotationAngles) -> float:
    """For the placement of longitudinal bars, located on one of the legs of a transverse bar
    (e.g. a stirrup), this function calculates the X-component between the edge of the
    concrete cross-section and the start point of the placement of the longitudinal bars

        │    │           │    │
        │    │           │    │
        │    │ o   o   o │ <- longitudinal bars
        │    ╰───────────╯ <- transverse bar (e.g. stirrup)
        │                     │
        └─────────────────────┘ outline
        <-----> calculated distance

    Args:
        shape:              Bending shape of the transverse bar
        side_number:        Number of the leg, on which the longitudinal bars are located (starting from 1)
        bending_roller:     Bending roller if the transverse bar
        base_line:          The outline of the concrete cross section
        placement_diameter: Bar diameter of the longitudinal bars
        local_angles:       Model angles to get the local x/y coordinate system for the calculation

    Returns:
        Calculated distance to the placement start
    """

    local_shape = AllplanReinf.BendingShape(shape)

    local_shape.Rotate(local_angles)

    bar_poly = local_shape.GetShapePolyline()

    line1 = AllplanGeo.Line2D(bar_poly.GetLine(side_number - 2))
    line2 = AllplanGeo.Line2D(bar_poly.GetLine(side_number - 1))

    dist = (bending_roller / 2. + 0.5) * shape.GetDiameter()

    if AllplanGeo.TransformCoord.PointLocal(line2, line1.StartPoint).Y < 0.:
        dist *= -1

    err, par_line_1 = AllplanGeo.Offset(dist, line1)

    if not GeometryValidate.offset(err):
        return 0

    err, par_line_2 = AllplanGeo.Offset(dist, line2)

    if not GeometryValidate.offset(err):
        return 0

    result, roller_pnt = AllplanGeo.IntersectionCalculusEx(par_line_1, par_line_2)

    if not GeometryValidate.intersection(result):
        return 0

    return AllplanGeo.TransformCoord.PointLocal(base_line, roller_pnt).X - placement_diameter / 2.


def get_placement_end_from_bending_roller(shape             : AllplanReinf.BendingShape,
                                          side_number       : int,
                                          bending_roller    : float,
                                          base_line         : AllplanGeo.Line2D | AllplanGeo.Line3D,
                                          placement_diameter: float,
                                          local_angles      : RotationAngles) -> float               :
    """For the placement of longitudinal bars, located on one of the legs of a transverse bar
    (e.g. a stirrup), this function calculates the X-component between the edge of the
    concrete cross-section and the end point of the placement of the longitudinal bars

        │    │           │    │
        │    │           │    │
        │    │ o   o   o │ <- longitudinal bars
        │    ╰───────────╯ <- transverse bar (e.g. stirrup)
        │                     │
        └─────────────────────┘ outline
                        <-----> calculated distance

    Args:
        shape:              Bending shape of the transverse bar
        side_number:        Number of the leg, on which the longitudinal bars are located (starting from 1)
        bending_roller:     Bending roller if the transverse bar
        base_line:          The outline of the concrete cross section
        placement_diameter: Bar diameter of the longitudinal bars
        local_angles:       Model angles to get the local x/y coordinate system for the calculation

    Returns:
        Calculated distance to the placement end
    """

    local_shape = AllplanReinf.BendingShape(shape)

    local_shape.Rotate(local_angles)

    bar_poly = local_shape.GetShapePolyline()

    if side_number + 1 >= bar_poly.Count():
        print("index error in get_placement_end_from_bending_roller")
        return AllplanGeo.Point3D()

    line1 = AllplanGeo.Line2D(bar_poly.GetLine(side_number - 1))
    line2 = AllplanGeo.Line2D(bar_poly.GetLine(side_number))

    dist = (bending_roller / 2. + 0.5) * shape.GetDiameter()

    if AllplanGeo.TransformCoord.PointLocal(line1, line2.EndPoint).Y < 0.:
        dist *= -1

    err, par_line_1 = AllplanGeo.Offset(dist, line1)

    if not GeometryValidate.offset(err):
        return 0

    err, par_line_2 = AllplanGeo.Offset(dist, line2)

    if not GeometryValidate.offset(err):
        return 0

    result, roller_pnt = AllplanGeo.IntersectionCalculusEx(par_line_1, par_line_2)

    if not GeometryValidate.intersection(result):
        return 0

    return AllplanGeo.CalcLength(base_line) - \
           AllplanGeo.TransformCoord.PointLocal(base_line, roller_pnt).X - placement_diameter / 2.


def get_placement_inside_bending_roller(shape             : AllplanReinf.BendingShape,
                                        corner_number     : int,
                                        bending_roller    : float,
                                        placement_diameter: float,
                                        local_angles      : RotationAngles,
                                        global_point      : bool = False) -> AllplanGeo.Point3D:
    """Calculate the position of a placement inside the bending roller

        │ │
        │ │ X  <--- calculated point
        │ ╰────────
        ╰────────── transverse bar (e.g. stirrup)

    Args:
        shape:              Bending shape of the transverse bar
        corner_number:      Number of the transverse bar's corner, in which the placement point
                            should be calculated (starting from 1)
        bending_roller:     Bending roller of the transverse bar
        placement_diameter: Bar diameter of the longitudinal bar
        local_angles:       Model angles to get the local x/y coordinate system for the calculation
        global_point:       If set to True, the result will be a point in global coordinates.
                            Otherwise, the point in local coordinate system will be returned.

    Returns:
        Local point of the longitudinal bar placement
    """

    local_shape = AllplanReinf.BendingShape(shape)

    local_shape.Rotate(local_angles)

    bar_poly = local_shape.GetShapePolyline()

    if corner_number + 1 >= bar_poly.Count():
        print("index error in get_placement_inside_bending_roller")
        return AllplanGeo.Point3D()

    line1 = AllplanGeo.Line2D(bar_poly.GetLine(corner_number - 1))
    line2 = AllplanGeo.Line2D(bar_poly.GetLine(corner_number))

    rad = (bending_roller / 2. + 0.5) * shape.GetDiameter()

    fillet = AllplanGeo.FilletCalculus2D(line1, line2, rad)

    arc = fillet.GetNearest(line1.EndPoint)

    arc_len = AllplanGeo.CalcLength(arc)

    center = AllplanGeo.TransformCoord.PointGlobal(arc, arc_len / 2)

    line = AllplanGeo.Line2D(AllplanGeo.Point2D(center), arc.Center)

    corner_pnt = AllplanGeo.TransformCoord.PointGlobal(line, shape.GetDiameter() / 2 + placement_diameter / 2)

    if global_point:
        global_angles = local_angles.change_rotation()

        corner_pnt = AllplanGeo.Transform(corner_pnt, global_angles.get_rotation_matrix())

    return corner_pnt


def get_placement_inside_side_intersection(shape1            : AllplanReinf.BendingShape,
                                           side_number1      : int,
                                           above_side1       : bool,
                                           shape2            : AllplanReinf.BendingShape,
                                           side_number2      : int,
                                           above_side2       : bool,
                                           placement_diameter: float,
                                           local_angles      : RotationAngles,
                                           global_point      : bool = False) -> AllplanGeo.Point2D | AllplanGeo.Point3D:
    """Calculate the position of a longitudinal bar placed at an intersection of two
    legs of transverse bars (e.g. two stirrups)

        ║ ┌─ calculated placement point
        ║ x    ║   ║
        ╬══════╝<--first shape
        ║          ║
        ╚══════════╝<--second shape

    Args:
        shape1:             Shape of the first transverse rebar
        side_number1:       Number of the leg in the first shape to consider in the calculation (starting from 1)
        above_side1:        When set to True, the point will be calculated above the leg of the first shape.
                            Otherwise below.
        shape2:             Shape of the second transverse rebar
        side_number2:       Number of the leg in the second shape to consider in the calculation (starting from 1)
        above_side2:        When set to True, the point will be calculated above the leg of the second shape.
                            Otherwise below.
        placement_diameter: Bar diameter of the longitudinal bar
        local_angles:       Model angles to get the local x/y coordinate system for the calculation
        global_point:       If set to True, the result will be a 3D point in global coordinates.
                            Otherwise, a 2D point in local coordinate system will be returned.

    Returns:
        local placement point as Point2D
    """

    local_shape1 = AllplanReinf.BendingShape(shape1)
    local_shape2 = AllplanReinf.BendingShape(shape2)

    local_shape1.Rotate(local_angles)
    local_shape2.Rotate(local_angles)

    bar_poly1 = local_shape1.GetShapePolyline()
    bar_poly2 = local_shape2.GetShapePolyline()

    rad = placement_diameter / 2.

    direction1 = 1 if above_side1 else -1
    direction2 = 1 if above_side2 else -1

    if side_number1 >= bar_poly1.Count():
        print("index error in get_placement_inside_side_intersection 1:")
        return AllplanGeo.Point3D()

    err, par_line_1 = AllplanGeo.Offset((shape1.GetDiameter() / 2. + rad) * direction1,
                                        AllplanGeo.Line2D(bar_poly1.GetLine(side_number1 - 1)))

    if not GeometryValidate.offset(err):
        return AllplanGeo.Point2D()

    if side_number2 >= bar_poly2.Count():
        print("index error in get_placement_inside_side_intersection 1:")
        return AllplanGeo.Point3D()

    err, par_line_2 = AllplanGeo.Offset((shape2.GetDiameter() / 2. + rad) * direction2,
                                        AllplanGeo.Line2D(bar_poly2.GetLine(side_number2 - 1)))

    if not GeometryValidate.offset(err):
        return AllplanGeo.Point2D()

    result, place_pnt = AllplanGeo.IntersectionCalculusEx(par_line_1, par_line_2)

    if not GeometryValidate.intersection(result):
        return AllplanGeo.Point2D()

    if global_point:
        global_angles = local_angles.change_rotation()

        place_pnt = AllplanGeo.Transform(AllplanGeo.Point3D(place_pnt), global_angles.get_rotation_matrix())

    return place_pnt

```

</details>