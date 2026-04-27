---
title: "LinearBarPlacementBuilder"
source: "PythonPartsFramework\StdReinfShapeBuilder\LinearBarPlacementBuilder.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# LinearBarPlacementBuilder

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\LinearBarPlacementBuilder.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`

## Übersicht

Implementation of the linear placement bar placement builder

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `enum`

## Klassen

### `StartEndPlacementRule`

Rules for linear rebar placements, determining how rebars are distributed when the placement
length is not an exact multiple of the spacing

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

### `create_linear_bar_placement_from_to_by_dist(position: int, shape: AllplanReinf.BendingShape, from_point: AllplanGeo.Point3D, to_point: AllplanGeo.Point3D, concrete_cover_left: float, concrete_cover_right: float, bar_distance: float, start_end_rule: StartEndPlacementRule=StartEndPlacementRule.AdditionalCover, global_move: bool=True)`

Create a linear rebar placement by:

-   start point
-   end point
-   bar spacing

Args:
    position:               Mark number
    shape:                  Shape for the placement
    from_point:             Start point of the placement
    to_point:               End point of the placement
    concrete_cover_left:    Concrete cover at the left placement side
    concrete_cover_right:   Concrete cover at the right placement side
    bar_distance:           Bar spacing
    start_end_rule:         Rule for the adaption of the distance / start-end cover
    global_move:            When set to True, the shape will be moved to the from_point of the placement.
                            Recommended, if the shape is created in a local coordinate system, near (0,0,0)

Returns:
    Bar placement

**Parameter:**
- `position: int`
- `shape: AllplanReinf.BendingShape`
- `from_point: AllplanGeo.Point3D`
- `to_point: AllplanGeo.Point3D`
- `concrete_cover_left: float`
- `concrete_cover_right: float`
- `bar_distance: float`
- `start_end_rule: StartEndPlacementRule=StartEndPlacementRule.AdditionalCover`
- `global_move: bool=True`

**Rückgabe:** `AllplanReinf.BarPlacement`

**Beispiel:**
```python
result = create_linear_bar_placement_from_to_by_dist(..., ..., ..., ..., ..., ..., ..., ..., ...)
```

### `create_linear_bar_placement_from_to_by_count(position: int, shape: AllplanReinf.BendingShape, from_point: AllplanGeo.Point3D, to_point: AllplanGeo.Point3D, concrete_cover_left: float, concrete_cover_right: float, bar_count: int, global_move: bool=True, remove_count_left: int=0, remove_count_right: int=0)`

Create a linear rebar placement by:

-   start point
-   end point
-   bar count

Args:
    position:               Mark number
    shape:                  Shape for the placement
    from_point:             Start point of the placement
    to_point:               End point of the placement
    concrete_cover_left:    Concrete cover at the left placement side
    concrete_cover_right:   Concrete cover at the right placement side
    bar_count:              Total count of rebars in the placement
    global_move:            When set to True, the shape will be moved to the from_point of the placement.
                            Recommended, if the shape is created in a local coordinate system, near (0,0,0)
    remove_count_left:      Count of rebars to be removed at the start
    remove_count_right:     Count of rebars to be removed at the end

Returns:
    Bar placement

**Parameter:**
- `position: int`
- `shape: AllplanReinf.BendingShape`
- `from_point: AllplanGeo.Point3D`
- `to_point: AllplanGeo.Point3D`
- `concrete_cover_left: float`
- `concrete_cover_right: float`
- `bar_count: int`
- `global_move: bool=True`
- `remove_count_left: int=0`
- `remove_count_right: int=0`

**Rückgabe:** `AllplanReinf.BarPlacement`

**Beispiel:**
```python
result = create_linear_bar_placement_from_to_by_count(..., ..., ..., ..., ..., ..., ..., ..., ..., ...)
```

### `create_linear_bar_placement_from_by_dist_count(position: int, shape: AllplanReinf.BendingShape, from_point: AllplanGeo.Point3D, direction_point: AllplanGeo.Point3D, concrete_cover: float, bar_distance: float, bar_count: int, global_move: bool=True)`

Create a linear rebar placement by:

-   start point
-   direction point
-   bar count
-   bar spacing

Args:
    position:               Mark number
    shape:                  Shape for the placement
    from_point:             Start point of the placement
    direction_point:        Direction point
    concrete_cover:         Concrete cover at the start
    bar_distance:           Bar spacing
    bar_count:              Bar count
    global_move:            When set to True, the shape will be moved to the from_point of the placement.
                            Recommended, if the shape is created in a local coordinate system, near (0,0,0)

Returns:
    Bar placement

**Parameter:**
- `position: int`
- `shape: AllplanReinf.BendingShape`
- `from_point: AllplanGeo.Point3D`
- `direction_point: AllplanGeo.Point3D`
- `concrete_cover: float`
- `bar_distance: float`
- `bar_count: int`
- `global_move: bool=True`

**Rückgabe:** `AllplanReinf.BarPlacement`

**Beispiel:**
```python
result = create_linear_bar_placement_from_by_dist_count(..., ..., ..., ..., ..., ..., ..., ...)
```

### `calculate_length_of_regions(value_list: list[tuple[float, float, float]], from_point: AllplanGeo.Point3D, to_point: AllplanGeo.Point3D, concrete_cover_left: float, concrete_cover_right: float)`

Create list with the start and end points of individual linear placements (called regions),
that compose one, greater linear placement. The points are calculated based on region's length,
bar spacing to be applied in the region and the rebar diameter, that should be placed in the region.
This is a helper function to be used in combination with the create_linear_bar_placement_from_to_by_dist
function to create e.g., stirrups inside beams, where the spacing varies along the beam's axis.

Args:
    value_list:             list with individual placement regions represented by tuples
                            (region length, bar spacing, bar diameter). IMPORTANT: At least one region
                            must have a zero length. Its length will be calculated by the function, so
                            that the total sum of all region lengths equals the distance between
                            start and end point.
    from_point:             Start point of the total parent
    to_point:               End point of the total
    concrete_cover_left:    Concrete cover at the start point
    concrete_cover_right:   Concrete cover at the end point

Returns:
    Bar placement points as list of tuples (start point, end point)

**Parameter:**
- `value_list: list[tuple[float`
- `float`
- `float]]`
- `from_point: AllplanGeo.Point3D`
- `to_point: AllplanGeo.Point3D`
- `concrete_cover_left: float`
- `concrete_cover_right: float`

**Rückgabe:** `list[tuple[AllplanGeo.Point3D, AllplanGeo.Point3D]]`

**Beispiel:**
```python
result = calculate_length_of_regions(..., ..., ..., ..., ..., ..., ...)
```

### `check_placement_length_by_distance(length: float, distance: float)`

Adjusts the length of the placement so that it is a multiple of the rebar spacing

Args:
    length:      length of the placement
    distance:    rebar spacing

Returns:
    Adjusted length of the placement

**Parameter:**
- `length: float`
- `distance: float`

**Rückgabe:** `float`

**Beispiel:**
```python
result = check_placement_length_by_distance(..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Implementation of the linear placement bar placement builder
"""
from enum import IntEnum

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf


class StartEndPlacementRule(IntEnum):
    """Rules for linear rebar placements, determining how rebars are distributed when the placement
    length is not an exact multiple of the spacing"""

    AdditionalCover      = 1
    """Spacing is preserved, concrete cover is increased at both ends"""

    AdditionalCoverLeft  = 2
    """Spacing is preserved, concrete cover at start is increased"""

    AdditionalCoverRight = 3
    """Spacing is preserved, concrete cover at end is increased"""

    AdaptDistance        = 4
    """Spacing is adapted to match the placement length"""

def create_linear_bar_placement_from_to_by_dist(position            : int,
                                                shape               : AllplanReinf.BendingShape,
                                                from_point          : AllplanGeo.Point3D,
                                                to_point            : AllplanGeo.Point3D,
                                                concrete_cover_left : float,
                                                concrete_cover_right: float,
                                                bar_distance        : float,
                                                start_end_rule      : StartEndPlacementRule = StartEndPlacementRule.AdditionalCover,
                                                global_move         : bool                  = True) -> AllplanReinf.BarPlacement:
    """Create a linear rebar placement by:

    -   start point
    -   end point
    -   bar spacing

    Args:
        position:               Mark number
        shape:                  Shape for the placement
        from_point:             Start point of the placement
        to_point:               End point of the placement
        concrete_cover_left:    Concrete cover at the left placement side
        concrete_cover_right:   Concrete cover at the right placement side
        bar_distance:           Bar spacing
        start_end_rule:         Rule for the adaption of the distance / start-end cover
        global_move:            When set to True, the shape will be moved to the from_point of the placement.
                                Recommended, if the shape is created in a local coordinate system, near (0,0,0)

    Returns:
        Bar placement
    """
    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    place_length = dist_vec.GetLength() - shape.GetDiameter() - concrete_cover_left - concrete_cover_right

    if place_length <= 0:
        return AllplanReinf.BarPlacement(position, 0, dist_vec, AllplanGeo.Point3D(), AllplanGeo.Point3D(), shape)

    count = int(place_length / bar_distance)

    add_cover = 0.


    #------------------ small difference will be adapted

    if (place_length - count * bar_distance) > bar_distance - 1:
        count += 1


    #------------------ adapt the concrete cover or the distance

    else:
        if start_end_rule == StartEndPlacementRule.AdditionalCover:
            add_cover = (place_length - count * bar_distance) / 2.

        elif start_end_rule == StartEndPlacementRule.AdditionalCoverLeft:
            add_cover = place_length - count * bar_distance

        elif start_end_rule == StartEndPlacementRule.AdditionalCoverRight:
            add_cover = 0.

        else:
            count = count + 1
            bar_distance = place_length / count

    start_point = AllplanGeo.TransformCoord.PointGlobal(AllplanGeo.Line3D(from_point, to_point),
                                                        concrete_cover_left + shape.GetDiameter() / 2. + add_cover)

    if not global_move:
        start_point -= from_point

    start_shape = AllplanReinf.BendingShape(shape)

    start_shape.Move(AllplanGeo.Vector3D(start_point))

    dist_vec.Normalize(bar_distance)

    return AllplanReinf.BarPlacement(position, count + 1, dist_vec, start_point,
                                     start_point + dist_vec * count, start_shape)


def create_linear_bar_placement_from_to_by_count(position            : int,
                                                 shape               : AllplanReinf.BendingShape,
                                                 from_point          : AllplanGeo.Point3D,
                                                 to_point            : AllplanGeo.Point3D,
                                                 concrete_cover_left : float,
                                                 concrete_cover_right: float,
                                                 bar_count           : int,
                                                 global_move         : bool = True,
                                                 remove_count_left   : int  = 0,
                                                 remove_count_right  : int  = 0) -> AllplanReinf.BarPlacement:
    """Create a linear rebar placement by:

    -   start point
    -   end point
    -   bar count

    Args:
        position:               Mark number
        shape:                  Shape for the placement
        from_point:             Start point of the placement
        to_point:               End point of the placement
        concrete_cover_left:    Concrete cover at the left placement side
        concrete_cover_right:   Concrete cover at the right placement side
        bar_count:              Total count of rebars in the placement
        global_move:            When set to True, the shape will be moved to the from_point of the placement.
                                Recommended, if the shape is created in a local coordinate system, near (0,0,0)
        remove_count_left:      Count of rebars to be removed at the start
        remove_count_right:     Count of rebars to be removed at the end

    Returns:
        Bar placement
    """

    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    place_length = dist_vec.GetLength() - shape.GetDiameter() - concrete_cover_left - concrete_cover_right

    bar_distance = place_length if bar_count == 1 else place_length / (bar_count - 1)

    start_point = AllplanGeo.TransformCoord.PointGlobal(AllplanGeo.Line3D(from_point, to_point),
                                                        concrete_cover_left + shape.GetDiameter() / 2.)

    if not global_move:
        start_point -= from_point

    start_shape = AllplanReinf.BendingShape(shape)

    start_shape.Move(AllplanGeo.Vector3D(start_point))

    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    if dist_vec.IsZero():
        return AllplanReinf.BarPlacement()

    dist_vec.Normalize(bar_distance)

    if remove_count_left:
        move_vec = dist_vec * float(remove_count_left)

        start_shape.Move(move_vec)

    if bar_count == 1:
        return AllplanReinf.BarPlacement(position,
                                         bar_count - remove_count_left - remove_count_right,
                                         dist_vec,
                                         start_point + dist_vec / 2,start_point + dist_vec / 2,
                                         start_shape)

    return AllplanReinf.BarPlacement(position,
                                     bar_count - remove_count_left - remove_count_right,
                                     dist_vec,
                                     start_point,start_point + dist_vec * (bar_count - 1),
                                     start_shape)


def create_linear_bar_placement_from_by_dist_count(position       : int,
                                                   shape          : AllplanReinf.BendingShape,
                                                   from_point     : AllplanGeo.Point3D,
                                                   direction_point: AllplanGeo.Point3D,
                                                   concrete_cover : float,
                                                   bar_distance   : float,
                                                   bar_count      : int,
                                                   global_move    : bool = True) -> AllplanReinf.BarPlacement :
    """Create a linear rebar placement by:

    -   start point
    -   direction point
    -   bar count
    -   bar spacing

    Args:
        position:               Mark number
        shape:                  Shape for the placement
        from_point:             Start point of the placement
        direction_point:        Direction point
        concrete_cover:         Concrete cover at the start
        bar_distance:           Bar spacing
        bar_count:              Bar count
        global_move:            When set to True, the shape will be moved to the from_point of the placement.
                                Recommended, if the shape is created in a local coordinate system, near (0,0,0)

    Returns:
        Bar placement
    """

    start_point = AllplanGeo.TransformCoord.PointGlobal(AllplanGeo.Line3D(from_point, direction_point),
                                                        concrete_cover + shape.GetDiameter() / 2.)

    if not global_move:
        start_point -= from_point

    start_shape = AllplanReinf.BendingShape(shape)

    start_shape.Move(AllplanGeo.Vector3D(start_point))

    dist_vec = AllplanGeo.Vector3D(from_point, direction_point)

    dist_vec.Normalize(bar_distance)

    end_point = start_point + dist_vec * (bar_count - 1)

    return AllplanReinf.BarPlacement(position, bar_count, dist_vec, start_point, end_point, start_shape)


def calculate_length_of_regions(value_list          : list[tuple[float, float, float]],
                                from_point          : AllplanGeo.Point3D,
                                to_point            : AllplanGeo.Point3D,
                                concrete_cover_left : float,
                                concrete_cover_right: float) -> list[tuple[AllplanGeo.Point3D,AllplanGeo.Point3D]]:
    """Create list with the start and end points of individual linear placements (called regions),
    that compose one, greater linear placement. The points are calculated based on region's length,
    bar spacing to be applied in the region and the rebar diameter, that should be placed in the region.
    This is a helper function to be used in combination with the create_linear_bar_placement_from_to_by_dist
    function to create e.g., stirrups inside beams, where the spacing varies along the beam's axis.

    Args:
        value_list:             list with individual placement regions represented by tuples
                                (region length, bar spacing, bar diameter). IMPORTANT: At least one region
                                must have a zero length. Its length will be calculated by the function, so
                                that the total sum of all region lengths equals the distance between
                                start and end point.
        from_point:             Start point of the total parent
        to_point:               End point of the total
        concrete_cover_left:    Concrete cover at the start point
        concrete_cover_right:   Concrete cover at the end point

    Returns:
        Bar placement points as list of tuples (start point, end point)
    """

    value_count = len(value_list)

    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    place_length = dist_vec.GetLength() - value_list[0][2] / 2 - value_list[value_count - 1][2] / 2 -   \
                   concrete_cover_left - concrete_cover_right


    #------------------ adapt the length to the distance

    real_length = []
    dist_next = []

    rest_index = -1

    length_sum = 0

    for i in range(value_count):
        value = value_list[i]

        if value[0]:
            length = check_placement_length_by_distance(value[0], value[1])

            length_sum += length

            real_length.append(length)
        else:
            real_length.append(0)

            rest_index = i


    #------------------ get the distance to the next region

    use_value_next = True

    for i in range(value_count - 1):
        value = value_list[i]
        value_next = value_list[i + 1]

        if not value[0]  or  not use_value_next:
            use_value_next = False
            dist_next.append(value[1])
        else:
            dist_next.append(value_next[1])

        length_sum += dist_next[i]


    #------------------ Calculate and set the rest

    real_length[rest_index] = place_length - length_sum


    #------------------ Create the real length at the left side

    x_start = concrete_cover_left

    place_line = AllplanGeo.Line3D(from_point, to_point)

    place_points = []

    for i in range(value_count):
        if i:
            x_start += dist_next[i - 1] - value[2] / 2

        value = value_list[i]

        x_end     = x_start + real_length[i] + value[2]
        x_end_org = x_end

        dist     = x_end - x_start - value_list[i][2]
        dist_new = check_placement_length_by_distance(dist, value_list[i][1])
        diff     = dist_new - dist

        if i == rest_index and  diff > 0:
            if i == 0:
                x_end += diff
            elif i == value_count - 1:
                x_start -= diff
            else:
                x_start -= diff / 2
                x_end   += diff / 2

        place_points.append((AllplanGeo.TransformCoord.PointGlobal(place_line, x_start),
                             AllplanGeo.TransformCoord.PointGlobal(place_line, x_end)))

        x_start = x_end_org - value[2] / 2.

    return place_points


def check_placement_length_by_distance(length   : float,
                                       distance : float) -> float:
    """Adjusts the length of the placement so that it is a multiple of the rebar spacing

    Args:
        length:      length of the placement
        distance:    rebar spacing

    Returns:
        Adjusted length of the placement
    """

    count = int(length / distance)

    if length - float(count * distance) > 10.:
        count += 1

    return float(count * distance)

```

</details>