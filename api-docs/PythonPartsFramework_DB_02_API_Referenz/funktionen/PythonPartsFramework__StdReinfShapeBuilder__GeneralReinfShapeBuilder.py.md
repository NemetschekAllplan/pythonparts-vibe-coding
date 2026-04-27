---
title: "GeneralReinfShapeBuilder"
source: "PythonPartsFramework\StdReinfShapeBuilder\GeneralReinfShapeBuilder.py"
type: "module"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# GeneralReinfShapeBuilder

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\GeneralReinfShapeBuilder.py`  
> **Typ:** Modul  
> **Tags:** `bewehrung`

## Übersicht

Implementation of the functions for the creation of the general reinforcement shapes

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`
- `StdReinfShapeBuilder.ConcreteCoverProperties`
- `StdReinfShapeBuilder.ReinforcementShapeProperties`
- `Utils.RotationUtil`
- `math`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `get_hook_type_from_angle(hook_type: AllplanReinf.HookType | int, hook_angle: float)`

Determines the hook type based on the given angle

Args:
    hook_type:  Type of the hook. If set to -1, hook type is determined based on given angle.
                Otherwise, given hook type is returned.
    hook_angle: Hook angle

Returns:
    Determined hook type

**Parameter:**
- `hook_type: AllplanReinf.HookType | int`
- `hook_angle: float`

**Rückgabe:** `AllplanReinf.HookType`

**Beispiel:**
```python
result = get_hook_type_from_angle(..., ...)
```

### `create_longitudinal_shape_with_hooks(length: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, start_hook: float=0, end_hook: float=0)`

Create a straight bar shape, optionally with standard 90° hooks at start and/or end.
The shape is created in the XY coordinate system, along X axis.

Args:
    length:                     Length of the reference line.
    model_angles:               Angles to rotate the shape from local to global coordinate system
    shape_props:                Shape properties
    concrete_cover_props:       Concrete covers. Relevant are: left, right and bottom cover
    start_hook:                 Hook length at the start. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
    end_hook:                   Hook length at the end. Default value (0) calculates the length automatically.
                                If set to -1: no hook.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `start_hook: float=0`
- `end_hook: float=0`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_longitudinal_shape_with_hooks(..., ..., ..., ..., ..., ...)
```

### `create_longitudinal_shape_with_user_hooks(length: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, start_hook: float=0.0, end_hook: float=0.0, start_hook_angle: float=90.0, end_hook_angle: float=90.0, hook_type_start: AllplanReinf.HookType | int=-1, hook_type_end: AllplanReinf.HookType | int=-1)`

Create a straight bar shape, optionally with user defined hooks at start and/or end.
The shape is created in the local XY coordinate system, along X axis.

Args:
    length:                 Length of the reference line.
    model_angles:           Angles to rotate the shape from local to global coordinate system
    shape_props:            Shape properties
    concrete_cover_props:   Concrete covers. Relevant are: left, right and bottom cover
    start_hook:             Hook length at the start. Default value (0) calculates the length automatically.
                            If set to -1: no hook.
    end_hook:               Hook length at the end. Default value (0) calculates the length automatically.
                            If set to -1: no hook.
    start_hook_angle:       Hook angle at start. Value between [-180, 180]
    end_hook_angle:         Hook angle at end. Value between [-180, 180]
    hook_type_start:        Type of the hook at the start. By default determined based on angle.
    hook_type_end:          Type of the hook at the end. By default determined based on angle.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `start_hook: float=0.0`
- `end_hook: float=0.0`
- `start_hook_angle: float=90.0`
- `end_hook_angle: float=90.0`
- `hook_type_start: AllplanReinf.HookType | int=-1`
- `hook_type_end: AllplanReinf.HookType | int=-1`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_longitudinal_shape_with_user_hooks(..., ..., ..., ..., ..., ..., ..., ..., ..., ...)
```

### `create_longitudinal_shape_with_anchorage(from_point: AllplanGeo.Point2D | AllplanGeo.Point3D, to_point: AllplanGeo.Point2D | AllplanGeo.Point3D, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, start_anchorage: float=0, end_anchorage: float=0)`

Create a straight bar shape, optionally with anchorage.
The shape is created in the local XY coordinate system, along X axis.

Args:
    from_point:             Start point of the reference line.
    to_point:               End point of the reference line.
    shape_props:            Shape properties.
    concrete_cover_props:   Concrete covers. Relevant are: bottom cover.
                            If the anchorage length at start or end is set to 0, then
                            also left or right cover respectively are considered.
    start_anchorage:        Anchorage length at the start.
    end_anchorage:          Anchorage length at the end.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `from_point: AllplanGeo.Point2D | AllplanGeo.Point3D`
- `to_point: AllplanGeo.Point2D | AllplanGeo.Point3D`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `start_anchorage: float=0`
- `end_anchorage: float=0`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_longitudinal_shape_with_anchorage(..., ..., ..., ..., ..., ...)
```

### `create_l_shape_with_hooks(length: float, width: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, start_hook: float=0, end_hook: float=0)`

Create an L-shape, optionally with standard 90° hooks at start and/or end.
The shape is created in local XY coordinate system like this: ⅃

Args:
    length:                     Length of the reference line parallel to X axis
    width:                      Length of the reference line parallel to Y axis
    model_angles:               Angles to rotate the shape from local to global coordinate system
    shape_props:                Shape properties
    concrete_cover_props:       Concrete cover properties. Relevant are all: bottom, left, right and top.
    start_hook:                 Hook length at the start. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
    end_hook:                   Hook length at the end. Default value (0) calculates the length automatically.
                                If set to -1: no hook.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `width: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `start_hook: float=0`
- `end_hook: float=0`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_l_shape_with_hooks(..., ..., ..., ..., ..., ..., ...)
```

### `create_stirrup(length: float, width: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, stirrup_type: AllplanReinf.StirrupType=AllplanReinf.StirrupType.Normal, hook_length: float=0)`

Create a rectangular stirrup shape with default hooks.
The shape is created in local XY coordinate system.

Args:
    length:                     Length of the reference rectangle (X-direction).
    width:                      Width of the reference rectangle (Y-direction).
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover_props:       Concrete covers: bottom, left, right and top.
    stirrup_type:               Type of the stirrup.
    hook_length:                Hook length. Default value (0) calculates the length automatically.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `width: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `stirrup_type: AllplanReinf.StirrupType=AllplanReinf.StirrupType.Normal`
- `hook_length: float=0`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_stirrup(..., ..., ..., ..., ..., ..., ...)
```

### `create_stirrup_with_user_hooks(length: float, width: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, stirrup_type: AllplanReinf.StirrupType, hook_length_start: float, hook_angle_start: float, hook_length_end: float, hook_angle_end: float)`

Create a rectangular stirrup shape with user defined hooks.
The shape is created in local XY coordinate system.

Args:
    length:                     Length of the reference rectangle (X-direction).
    width:                      Width of the reference rectangle (Y-direction).
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover_props:       Concrete covers: bottom, left, right and top.
    stirrup_type:               Type of the stirrup.
    hook_length_start:          Hook length at start. When set to 0, the length is calculated automatically.
    hook_angle_start:           Hook angle at start. When set to 0, the angle is calculated automatically
                                based on stirrup type.
    hook_length_end:            Hook length at end. When set to 0, the length is calculated automatically.
    hook_angle_end:             Hook angle at end. When set to 0, the angle is calculated automatically
                                based on stirrup type.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `width: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `stirrup_type: AllplanReinf.StirrupType`
- `hook_length_start: float`
- `hook_angle_start: float`
- `hook_length_end: float`
- `hook_angle_end: float`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_stirrup_with_user_hooks(..., ..., ..., ..., ..., ..., ..., ..., ..., ...)
```

### `create_open_stirrup(length: float, width: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, start_hook: float=0, end_hook: float=0, start_hook_angle: float=90.0, end_hook_angle: float=90.0, hook_type: AllplanReinf.HookType | int=-1)`

Create a rectangular stirrup shape, open on the top side.
The shape is created in local XY coordinate system.

Args:
    length:                     Length of the reference rectangle (X-direction).
    width:                      Width of the reference rectangle (Y-direction).
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover_props:       Concrete covers: bottom, left, right and top.
    start_hook:                 Length of the left hook. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
    end_hook:                   Length of the right hook. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
    start_hook_angle:           Angle of the left hook [-180, 180]
    end_hook_angle:             Angle of the right hook [-180, 180]
    hook_type:                  Type of the hook at the end. By default determined based on angle.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `width: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `start_hook: float=0`
- `end_hook: float=0`
- `start_hook_angle: float=90.0`
- `end_hook_angle: float=90.0`
- `hook_type: AllplanReinf.HookType | int=-1`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_open_stirrup(..., ..., ..., ..., ..., ..., ..., ..., ..., ...)
```

### `create_s_hook(length: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, hook_length: float=0)`

Create an S-hook shape with 180° hooks at both ends.
The shape is created in local XY coordinate system, along the X-axis.

Args:
    length:                     Length of the reference line
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover_props:       Concrete covers. Relevant are: left and right cover.
    hook_length:                Length of both hooks. Default value (0) calculates the length automatically.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `hook_length: float=0`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_s_hook(..., ..., ..., ..., ...)
```

### `create_hook_stirrup(length: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, hook_length: float=0, hook_start_angle: float=180.0, hook_end_angle: float=180.0)`

Create a hook stirrup with user defined hooks at both ends.
The shape is created in local XY coordinate system, along the X-axis.

Args:
    length:                     Length of the reference line
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover_props:       Concrete covers. Relevant are: left and right cover.
    hook_length:                Length of both hooks. Default value (0) calculates the length automatically.
    hook_start_angle:           Angle of the left hook.
    hook_end_angle:             Angle of the right hook.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `hook_length: float=0`
- `hook_start_angle: float=180.0`
- `hook_end_angle: float=180.0`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_hook_stirrup(..., ..., ..., ..., ..., ..., ...)
```

### `create_spacer(length: float, width: float, height: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties)`

Create a spacer shape. Created shape is 3-dimensional with total 5 legs.
Concrete covers are not considered. Legs nr:

-   1 and 5 are parallel to X-axis
-   2 and 4 are parallel to Z-axis
-   3 is parallel to Y-axis

Args:
    length:                     Length of the box bounding the shape (X-direction).
    width:                      Width of the box bounding the shape (Y-direction).
    height:                     Height of the box bounding the shape (Z-direction).
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `length: float`
- `width: float`
- `height: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_spacer(..., ..., ..., ..., ...)
```

### `create_u_link(width: float, side_length: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, hook_length: float)`

Create a U-bar with both left and right legs of the same length. Optionally with
hooks at both ends. The shape is created in local XY coordinate system, with its open
side pointing upwards (in Y+ direction) like in the letter U.

Args:
    width:                      Width of the U-bar base line.
    side_length:                Length of both left and right leg.
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover_props:       Concrete covers. Relevant are: left, right and bottom cover.
    hook_length:                Length of both hooks. When set to 0, it's calculated automatically.
                                When set to -1, no hooks are created.

Returns:
    Bar shape of the u link shape in world coordinates

**Parameter:**
- `width: float`
- `side_length: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `hook_length: float`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_u_link(..., ..., ..., ..., ..., ...)
```

### `create_u_link_variable(width: float, side_length_start: float, side_length_end: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover_props: ConcreteCoverProperties, start_hook: float=0.0, end_hook: float=0.0, start_hook_angle: float=90.0, end_hook_angle: float=90.0, hook_type_start: AllplanReinf.HookType | int=-1, hook_type_end: AllplanReinf.HookType | int=-1)`

Create an u-bar with different lengths of the left and right leg.
Optionally with hooks at the end of right and/or left leg.
The shape is created in local XY coordinate system, with its open side
pointing upwards (in Y+ direction) like in the letter U.

Args:
    width:                      Width of the U-bar base line.
    side_length_start:          Length of the left leg.
    side_length_end:            Length of the right leg.
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover_props:       Concrete covers. Relevant are: left, right and bottom cover.
    start_hook:                 Length of the hook at the end of the left leg. When set to 0, it's
                                calculated automatically. When set to -1, hook is not created.
    end_hook:                   Length of the hook at the end of the right leg. When set to 0, it's
                                calculated automatically. When set to -1, hook is not created.
    start_hook_angle:           Angle of the hook of the left leg [-180, 180].
    end_hook_angle:             Angle of the hook of the right leg [-180, 180].
    hook_type_start:            Type of the hook of the left leg. By default determined based on angle.
    hook_type_end:              Type of the hook of the right leg. By default determined based on angle.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `width: float`
- `side_length_start: float`
- `side_length_end: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover_props: ConcreteCoverProperties`
- `start_hook: float=0.0`
- `end_hook: float=0.0`
- `start_hook_angle: float=90.0`
- `end_hook_angle: float=90.0`
- `hook_type_start: AllplanReinf.HookType | int=-1`
- `hook_type_end: AllplanReinf.HookType | int=-1`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_u_link_variable(..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ...)
```

### `create_freeform_shape_with_hooks(points: AllplanGeo.Point2DList | AllplanGeo.Point3DList | list[AllplanGeo.Point2D] | list[AllplanGeo.Point3D], model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover: float, start_hook: float=0, end_hook: float=0)`

Create a free form shape based on points. Optionally with standard 90°
hooks at start and/or end of the shape.

Args:
    points:                     Points of the geometry side (min. 2 points)
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover:             Concrete cover. Will be applied on all sides.
    start_hook:                 Length of the hook at the start. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
    end_hook:                   Length of the hook at the end. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
Returns:
    Bar shape in world coordinates

**Parameter:**
- `points: AllplanGeo.Point2DList | AllplanGeo.Point3DList | list[AllplanGeo.Point2D] | list[AllplanGeo.Point3D]`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover: float`
- `start_hook: float=0`
- `end_hook: float=0`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_freeform_shape_with_hooks(..., ..., ..., ..., ..., ...)
```

### `create_circle_stirrup_with_user_hooks(radius: float, model_angles: RotationUtil, shape_props: ReinforcementShapeProperties, concrete_cover: float, overlap: float, hook_length_start: float, hook_angle_start: float, hook_length_end: float, hook_angle_end: float)`

Create a circle stirrup shape. If rotation angles all set to 0, the shape is created in local
XY coordinate system. The center of the reference circle is the (0,0) point.

Args:
    radius:                     Radius of the reference circle.
    model_angles:               Angles to rotate the shape from local to global coordinate system.
    shape_props:                Shape properties.
    concrete_cover:             Concrete cover.
    overlap:                    Overlap length.
    hook_length_start:          Length of the hook at the start. When set to 0, the length
                                will be calculated automatically.
    hook_angle_start:           Hook angle at the start. When set to 0, it will be calculated automatically.
    hook_length_end:            Length of the hook at the end. When set to 0, the length
                                will be calculated automatically.
    hook_angle_end:             Hook angle at the end. When set to 0, it will be calculated automatically.

Returns:
    Bar shape in world coordinates

**Parameter:**
- `radius: float`
- `model_angles: RotationUtil`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover: float`
- `overlap: float`
- `hook_length_start: float`
- `hook_angle_start: float`
- `hook_length_end: float`
- `hook_angle_end: float`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = create_circle_stirrup_with_user_hooks(..., ..., ..., ..., ..., ..., ..., ..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""Implementation of the functions for the creation of the general reinforcement shapes
"""

import math

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_Utility as AllplanUtil

from Utils.RotationUtil import RotationUtil

from StdReinfShapeBuilder.ConcreteCoverProperties import ConcreteCoverProperties
from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties


def get_hook_type_from_angle(hook_type:  AllplanReinf.HookType|int,
                             hook_angle: float) -> AllplanReinf.HookType:
    """Determines the hook type based on the given angle

    Args:
        hook_type:  Type of the hook. If set to -1, hook type is determined based on given angle.
                    Otherwise, given hook type is returned.
        hook_angle: Hook angle

    Returns:
        Determined hook type
    """

    if hook_type != -1:
        return hook_type

    if abs(hook_angle) < 134:
        return AllplanReinf.HookType.eAngle

    return  AllplanReinf.HookType.eStirrup


def create_longitudinal_shape_with_hooks(length              : float,
                                         model_angles        : RotationUtil,
                                         shape_props         : ReinforcementShapeProperties,
                                         concrete_cover_props: ConcreteCoverProperties,
                                         start_hook          : float = 0,
                                         end_hook            : float = 0) -> AllplanReinf.BendingShape:

    """Create a straight bar shape, optionally with standard 90° hooks at start and/or end.
    The shape is created in the XY coordinate system, along X axis.

    Args:
        length:                     Length of the reference line.
        model_angles:               Angles to rotate the shape from local to global coordinate system
        shape_props:                Shape properties
        concrete_cover_props:       Concrete covers. Relevant are: left, right and bottom cover
        start_hook:                 Hook length at the start. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.
        end_hook:                   Hook length at the end. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (concrete_cover_props.right)])

    if start_hook == 0:
        shape_builder.SetAnchorageHookStart(90)
    elif start_hook > 0:
        shape_builder.SetHookStart(start_hook, 90, AllplanReinf.HookType.eAnchorage)

    if end_hook == 0:
        shape_builder.SetAnchorageHookEnd(90)
    elif end_hook > 0:
        shape_builder.SetHookEnd(end_hook, 90, AllplanReinf.HookType.eAnchorage)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_longitudinal_shape_with_user_hooks(length: float,
                                              model_angles        : RotationUtil,
                                              shape_props         : ReinforcementShapeProperties,
                                              concrete_cover_props: ConcreteCoverProperties,
                                              start_hook          : float = 0.0,
                                              end_hook            : float = 0.0,
                                              start_hook_angle    : float = 90.0,
                                              end_hook_angle      : float = 90.0,
                                              hook_type_start     : AllplanReinf.HookType|int = -1,
                                              hook_type_end       : AllplanReinf.HookType|int = -1) -> AllplanReinf.BendingShape:

    """Create a straight bar shape, optionally with user defined hooks at start and/or end.
    The shape is created in the local XY coordinate system, along X axis.

    Args:
        length:                 Length of the reference line.
        model_angles:           Angles to rotate the shape from local to global coordinate system
        shape_props:            Shape properties
        concrete_cover_props:   Concrete covers. Relevant are: left, right and bottom cover
        start_hook:             Hook length at the start. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
        end_hook:               Hook length at the end. Default value (0) calculates the length automatically.
                                If set to -1: no hook.
        start_hook_angle:       Hook angle at start. Value between [-180, 180]
        end_hook_angle:         Hook angle at end. Value between [-180, 180]
        hook_type_start:        Type of the hook at the start. By default determined based on angle.
        hook_type_end:          Type of the hook at the end. By default determined based on angle.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (concrete_cover_props.right)])

    if start_hook >= 0:
        shape_builder.SetHookStart(start_hook, start_hook_angle,
                                   get_hook_type_from_angle(hook_type_start, start_hook_angle))

    if end_hook >= 0:
        shape_builder.SetHookEnd(end_hook, end_hook_angle,
                                 get_hook_type_from_angle(hook_type_end, end_hook_angle))

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_longitudinal_shape_with_anchorage(from_point          : AllplanGeo.Point2D|AllplanGeo.Point3D,
                                             to_point            : AllplanGeo.Point2D|AllplanGeo.Point3D,
                                             shape_props         : ReinforcementShapeProperties,
                                             concrete_cover_props: ConcreteCoverProperties,
                                             start_anchorage     : float = 0,
                                             end_anchorage       : float = 0) -> AllplanReinf.BendingShape:
    """Create a straight bar shape, optionally with anchorage.
    The shape is created in the local XY coordinate system, along X axis.

    Args:
        from_point:             Start point of the reference line.
        to_point:               End point of the reference line.
        shape_props:            Shape properties.
        concrete_cover_props:   Concrete covers. Relevant are: bottom cover.
                                If the anchorage length at start or end is set to 0, then
                                also left or right cover respectively are considered.
        start_anchorage:        Anchorage length at the start.
        end_anchorage:          Anchorage length at the end.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(from_point, concrete_cover_props.left),
                             (to_point, concrete_cover_props.bottom),
                             (concrete_cover_props.right)])

    if start_anchorage != 0:
        shape_builder.SetAnchorageLengthStart(start_anchorage)

    if end_anchorage != 0:
        shape_builder.SetAnchorageLengthEnd(end_anchorage)

    return shape_builder.CreateShape(shape_props)


def create_l_shape_with_hooks(length              : float,
                              width               : float,
                              model_angles        : RotationUtil,
                              shape_props         : ReinforcementShapeProperties,
                              concrete_cover_props: ConcreteCoverProperties,
                              start_hook          : float = 0,
                              end_hook            : float = 0) -> AllplanReinf.BendingShape:
    """Create an L-shape, optionally with standard 90° hooks at start and/or end.
    The shape is created in local XY coordinate system like this: ⅃

    Args:
        length:                     Length of the reference line parallel to X axis
        width:                      Length of the reference line parallel to Y axis
        model_angles:               Angles to rotate the shape from local to global coordinate system
        shape_props:                Shape properties
        concrete_cover_props:       Concrete cover properties. Relevant are all: bottom, left, right and top.
        start_hook:                 Hook length at the start. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.
        end_hook:                   Hook length at the end. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(length, width), concrete_cover_props.right),
                             (concrete_cover_props.top)])

    if start_hook == 0:
        shape_builder.SetAnchorageHookStart(90)
    elif start_hook > 0:
        shape_builder.SetHookStart(start_hook, 90, AllplanReinf.HookType.eAnchorage)

    if end_hook == 0:
        shape_builder.SetAnchorageHookEnd(90)
    elif end_hook > 0:
        shape_builder.SetHookEnd(end_hook, 90, AllplanReinf.HookType.eAnchorage)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stirrup(length              : float,
                   width               : float,
                   model_angles        : RotationUtil,
                   shape_props         : ReinforcementShapeProperties,
                   concrete_cover_props: ConcreteCoverProperties,
                   stirrup_type        : AllplanReinf.StirrupType = AllplanReinf.StirrupType.Normal,
                   hook_length         : float = 0) -> AllplanReinf.BendingShape :
    """Create a rectangular stirrup shape with default hooks.
    The shape is created in local XY coordinate system.

    Args:
        length:                     Length of the reference rectangle (X-direction).
        width:                      Width of the reference rectangle (Y-direction).
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover_props:       Concrete covers: bottom, left, right and top.
        stirrup_type:               Type of the stirrup.
        hook_length:                Hook length. Default value (0) calculates the length automatically.

    Returns:
        Bar shape in world coordinates
    """

    return create_stirrup_with_user_hooks(length, width, model_angles, shape_props, concrete_cover_props, stirrup_type,
                                          hook_length, 0, hook_length, 0)

def create_stirrup_with_user_hooks(length              : float,
                                   width               : float,
                                   model_angles        : RotationUtil,
                                   shape_props         : ReinforcementShapeProperties,
                                   concrete_cover_props: ConcreteCoverProperties,
                                   stirrup_type        : AllplanReinf.StirrupType,
                                   hook_length_start   : float,
                                   hook_angle_start    : float,
                                   hook_length_end     : float,
                                   hook_angle_end      : float) -> AllplanReinf.BendingShape:

    """Create a rectangular stirrup shape with user defined hooks.
    The shape is created in local XY coordinate system.

    Args:
        length:                     Length of the reference rectangle (X-direction).
        width:                      Width of the reference rectangle (Y-direction).
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover_props:       Concrete covers: bottom, left, right and top.
        stirrup_type:               Type of the stirrup.
        hook_length_start:          Hook length at start. When set to 0, the length is calculated automatically.
        hook_angle_start:           Hook angle at start. When set to 0, the angle is calculated automatically
                                    based on stirrup type.
        hook_length_end:            Hook length at end. When set to 0, the length is calculated automatically.
        hook_angle_end:             Hook angle at end. When set to 0, the angle is calculated automatically
                                    based on stirrup type.

    Returns:
        Bar shape in world coordinates
    """
    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(length, width), concrete_cover_props.top),
                             (AllplanGeo.Point2D(0, width), concrete_cover_props.top),
                             (AllplanGeo.Point2D(0, 0), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(length, width), concrete_cover_props.right),
                             (concrete_cover_props.top)])

    if stirrup_type == AllplanReinf.StirrupType.Torsion:
        shape_builder.AddPoint(AllplanGeo.Point2D(0, width), concrete_cover_props.top, 0)

    if hook_length_start > 0  and  hook_angle_start != 0:
        shape_builder.SetHookStart(hook_length_start, hook_angle_start, AllplanReinf.HookType.eStirrup)

    elif hook_length_start > 0:
        shape_builder.SetHookStart(hook_length_start, 0, AllplanReinf.HookType.eStirrup)

    if hook_length_end > 0  and  hook_angle_end != 0:
        shape_builder.SetHookEnd(hook_length_end, hook_angle_end, AllplanReinf.HookType.eStirrup)

    elif hook_length_end > 0:
        shape_builder.SetHookEnd(hook_length_end, 0, AllplanReinf.HookType.eStirrup)

    shape = shape_builder.CreateStirrup(shape_props,
                                        stirrup_type)


    #----------------- Rotate the shape in the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_open_stirrup(length              : float,
                        width               : float,
                        model_angles        : RotationUtil,
                        shape_props         : ReinforcementShapeProperties,
                        concrete_cover_props: ConcreteCoverProperties,
                        start_hook          : float = 0,
                        end_hook            : float = 0,
                        start_hook_angle    : float = 90.0,
                        end_hook_angle      : float = 90.0,
                        hook_type           : AllplanReinf.HookType|int = -1) -> AllplanReinf.BendingShape:
    """Create a rectangular stirrup shape, open on the top side.
    The shape is created in local XY coordinate system.

    Args:
        length:                     Length of the reference rectangle (X-direction).
        width:                      Width of the reference rectangle (Y-direction).
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover_props:       Concrete covers: bottom, left, right and top.
        start_hook:                 Length of the left hook. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.
        end_hook:                   Length of the right hook. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.
        start_hook_angle:           Angle of the left hook [-180, 180]
        end_hook_angle:             Angle of the right hook [-180, 180]
        hook_type:                  Type of the hook at the end. By default determined based on angle.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(0, width), concrete_cover_props.top),
                             (AllplanGeo.Point2D(0, 0), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(length, width), concrete_cover_props.right),
                             (concrete_cover_props.top)])

    if start_hook >= 0:
        shape_builder.SetHookStart(start_hook, start_hook_angle,
                                   get_hook_type_from_angle(hook_type, start_hook_angle))

    if end_hook >= 0:
        shape_builder.SetHookEnd(end_hook, end_hook_angle,
                                 get_hook_type_from_angle(hook_type, end_hook_angle))

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape in the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_s_hook(length              : float,
                  model_angles        : RotationUtil,
                  shape_props         : ReinforcementShapeProperties,
                  concrete_cover_props: ConcreteCoverProperties,
                  hook_length         : float = 0) -> AllplanReinf.BendingShape:
    """Create an S-hook shape with 180° hooks at both ends.
    The shape is created in local XY coordinate system, along the X-axis.

    Args:
        length:                     Length of the reference line
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover_props:       Concrete covers. Relevant are: left and right cover.
        hook_length:                Length of both hooks. Default value (0) calculates the length automatically.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), 0),
                             (concrete_cover_props.right)])

    shape_builder.SetHookStart(hook_length, 180, AllplanReinf.HookType.eStirrup)
    shape_builder.SetHookEnd(hook_length, -180, AllplanReinf.HookType.eStirrup)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_hook_stirrup(length              : float,
                        model_angles        : RotationUtil,
                        shape_props         : ReinforcementShapeProperties,
                        concrete_cover_props: ConcreteCoverProperties,
                        hook_length         : float = 0,
                        hook_start_angle    : float = 180.,
                        hook_end_angle      : float = 180. ) -> AllplanReinf.BendingShape:
    """Create a hook stirrup with user defined hooks at both ends.
    The shape is created in local XY coordinate system, along the X-axis.

    Args:
        length:                     Length of the reference line
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover_props:       Concrete covers. Relevant are: left and right cover.
        hook_length:                Length of both hooks. Default value (0) calculates the length automatically.
        hook_start_angle:           Angle of the left hook.
        hook_end_angle:             Angle of the right hook.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), 0),
                             (concrete_cover_props. right)])

    shape_builder.SetHookStart(hook_length, hook_start_angle, AllplanReinf.HookType.eStirrup)
    shape_builder.SetHookEnd(hook_length, hook_end_angle, AllplanReinf.HookType.eStirrup)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_spacer(length      : float,
                  width       : float,
                  height      : float,
                  model_angles: RotationUtil,
                  shape_props : ReinforcementShapeProperties) -> AllplanReinf.BendingShape:
    """Create a spacer shape. Created shape is 3-dimensional with total 5 legs.
    Concrete covers are not considered. Legs nr:

    -   1 and 5 are parallel to X-axis
    -   2 and 4 are parallel to Z-axis
    -   3 is parallel to Y-axis

    Args:
        length:                     Length of the box bounding the shape (X-direction).
        width:                      Width of the box bounding the shape (Y-direction).
        height:                     Height of the box bounding the shape (Z-direction).
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.

    Returns:
        Bar shape in world coordinates
    """

    len2 = length / 2

    shape_pol = AllplanGeo.Polyline3D()
    shape_pol += AllplanGeo.Point3D(0, 0, 0)
    shape_pol += AllplanGeo.Point3D(len2, 0, 0)
    shape_pol += AllplanGeo.Point3D(len2, 0, height)
    shape_pol += AllplanGeo.Point3D(len2, width, height)
    shape_pol += AllplanGeo.Point3D(len2, width, 0)
    shape_pol += AllplanGeo.Point3D(length, width, 0)

    br_list = AllplanUtil.VecDoubleList()

    bero = shape_props.bending_roller

    br_list[:] = [bero, bero, bero, bero]

    shape = AllplanReinf.BendingShape(shape_pol, br_list, shape_props.diameter, shape_props.steel_grade, -1,
                                      AllplanReinf.BendingShapeType.BarSpacer)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_u_link(width               : float,
                  side_length         : float,
                  model_angles        : RotationUtil,
                  shape_props         : ReinforcementShapeProperties,
                  concrete_cover_props: ConcreteCoverProperties,
                  hook_length         : float) -> AllplanReinf.BendingShape:
    """Create a U-bar with both left and right legs of the same length. Optionally with
    hooks at both ends. The shape is created in local XY coordinate system, with its open
    side pointing upwards (in Y+ direction) like in the letter U.

    Args:
        width:                      Width of the U-bar base line.
        side_length:                Length of both left and right leg.
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover_props:       Concrete covers. Relevant are: left, right and bottom cover.
        hook_length:                Length of both hooks. When set to 0, it's calculated automatically.
                                    When set to -1, no hooks are created.

    Returns:
        Bar shape of the u link shape in world coordinates
    """

    return create_u_link_variable(width, side_length, side_length, model_angles, shape_props, concrete_cover_props,
                                  hook_length, hook_length, 90, 90,
                                  AllplanReinf.HookType.eAnchorage, AllplanReinf.HookType.eAnchorage)


def create_u_link_variable(width               : float,
                           side_length_start   : float,
                           side_length_end     : float,
                           model_angles        : RotationUtil,
                           shape_props         : ReinforcementShapeProperties,
                           concrete_cover_props: ConcreteCoverProperties,
                           start_hook          : float = 0.0,
                           end_hook            : float = 0.0,
                           start_hook_angle    : float = 90.0,
                           end_hook_angle      : float = 90.0,
                           hook_type_start     : AllplanReinf.HookType|int = -1,
                           hook_type_end       : AllplanReinf.HookType|int = -1) -> AllplanReinf.BendingShape:
    """Create an u-bar with different lengths of the left and right leg.
    Optionally with hooks at the end of right and/or left leg.
    The shape is created in local XY coordinate system, with its open side
    pointing upwards (in Y+ direction) like in the letter U.

    Args:
        width:                      Width of the U-bar base line.
        side_length_start:          Length of the left leg.
        side_length_end:            Length of the right leg.
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover_props:       Concrete covers. Relevant are: left, right and bottom cover.
        start_hook:                 Length of the hook at the end of the left leg. When set to 0, it's
                                    calculated automatically. When set to -1, hook is not created.
        end_hook:                   Length of the hook at the end of the right leg. When set to 0, it's
                                    calculated automatically. When set to -1, hook is not created.
        start_hook_angle:           Angle of the hook of the left leg [-180, 180].
        end_hook_angle:             Angle of the hook of the right leg [-180, 180].
        hook_type_start:            Type of the hook of the left leg. By default determined based on angle.
        hook_type_end:              Type of the hook of the right leg. By default determined based on angle.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(0, side_length_start), 0),
                             (AllplanGeo.Point2D(0, 0), concrete_cover_props.left),
                             (AllplanGeo.Point2D(width, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(width, side_length_end), concrete_cover_props.right),
                             (0)])

    shape_builder.SetSideLengthStart(side_length_start)
    shape_builder.SetSideLengthEnd(side_length_end)

    if start_hook >= 0:
        shape_builder.SetHookStart(start_hook, start_hook_angle,
                                   get_hook_type_from_angle(hook_type_start, start_hook_angle))

    if end_hook >= 0:
        shape_builder.SetHookEnd(end_hook, end_hook_angle,
                                 get_hook_type_from_angle(hook_type_end, end_hook_angle))

    u_shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if u_shape.IsValid() is True:
        u_shape.Rotate(model_angles)

    return u_shape


def create_freeform_shape_with_hooks(points        : AllplanGeo.Point2DList|
                                                     AllplanGeo.Point3DList|
                                                     list[AllplanGeo.Point2D]|
                                                     list[AllplanGeo.Point3D],
                                     model_angles  : RotationUtil,
                                     shape_props   : ReinforcementShapeProperties,
                                     concrete_cover: float,
                                     start_hook    : float = 0,
                                     end_hook      : float = 0 ) -> AllplanReinf.BendingShape:
    """Create a free form shape based on points. Optionally with standard 90°
    hooks at start and/or end of the shape.

    Args:
        points:                     Points of the geometry side (min. 2 points)
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover:             Concrete cover. Will be applied on all sides.
        start_hook:                 Length of the hook at the start. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.
        end_hook:                   Length of the hook at the end. Default value (0) calculates the length automatically.
                                    If set to -1: no hook.
    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    for point in points:
        shape_builder.AddPoints([(AllplanGeo.Point2D(point), concrete_cover),(concrete_cover)])

    if start_hook == 0:
        shape_builder.SetAnchorageHookStart(90)
    elif start_hook > 0:
        shape_builder.SetHookStart(start_hook, 90, AllplanReinf.HookType.eAnchorage)

    if end_hook == 0:
        shape_builder.SetAnchorageHookEnd(90)
    elif end_hook > 0:
        shape_builder.SetHookEnd(end_hook, 90, AllplanReinf.HookType.eAnchorage)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_circle_stirrup_with_user_hooks(radius           : float,
                                          model_angles     : RotationUtil,
                                          shape_props      : ReinforcementShapeProperties,
                                          concrete_cover   : float,
                                          overlap          : float,
                                          hook_length_start: float,
                                          hook_angle_start : float,
                                          hook_length_end  : float,
                                          hook_angle_end   : float) -> AllplanReinf.BendingShape:

    """Create a circle stirrup shape. If rotation angles all set to 0, the shape is created in local
    XY coordinate system. The center of the reference circle is the (0,0) point.

    Args:
        radius:                     Radius of the reference circle.
        model_angles:               Angles to rotate the shape from local to global coordinate system.
        shape_props:                Shape properties.
        concrete_cover:             Concrete cover.
        overlap:                    Overlap length.
        hook_length_start:          Length of the hook at the start. When set to 0, the length
                                    will be calculated automatically.
        hook_angle_start:           Hook angle at the start. When set to 0, it will be calculated automatically.
        hook_length_end:            Length of the hook at the end. When set to 0, the length
                                    will be calculated automatically.
        hook_angle_end:             Hook angle at the end. When set to 0, it will be calculated automatically.

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    arc = AllplanGeo.Arc2D(AllplanGeo.Point2D (), radius, radius, 0, 0, 2 * math.pi, True)

    shape_builder.AddSides([(0),
                            (arc, concrete_cover),
                            (0)])

    shape_builder.SetFullCircleOverlap(overlap)

    if hook_length_start > 0  and  hook_angle_start != 0:
        shape_builder.SetHookStart(hook_length_start, hook_angle_start, AllplanReinf.HookType.eStirrup)

    elif hook_length_start > 0:
        shape_builder.SetHookStart(hook_length_start, 0, AllplanReinf.HookType.eStirrup)

    if hook_length_end > 0  and  hook_angle_end != 0:
        shape_builder.SetHookEnd(hook_length_end, hook_angle_end, AllplanReinf.HookType.eStirrup)

    elif hook_length_end > 0:
        shape_builder.SetHookEnd(hook_length_end, 0, AllplanReinf.HookType.eStirrup)

    shape = shape_builder.CreateStirrup(shape_props,
                                        AllplanReinf.StirrupType.FullCircle)


    #----------------- Rotate the shape in the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape

```

</details>