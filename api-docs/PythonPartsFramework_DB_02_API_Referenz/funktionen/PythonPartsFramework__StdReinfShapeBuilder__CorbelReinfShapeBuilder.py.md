---
title: "CorbelReinfShapeBuilder"
source: "PythonPartsFramework\StdReinfShapeBuilder\CorbelReinfShapeBuilder.py"
type: "module"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# CorbelReinfShapeBuilder

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\CorbelReinfShapeBuilder.py`  
> **Typ:** Modul  
> **Tags:** `bewehrung`

## Übersicht

Implementation of the functions for the creation of the reinforcement corbel shapes

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `StdReinfShapeBuilder.ReinforcementShapeProperties`
- `StdReinfShapeBuilder.RotationAngles`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `column_corbel_shape_type1(column_width: float, column_thickness: float, corbel_width: float, corbel_top: float, model_angles: RotationAngles, shape_props: ReinforcementShapeProperties, concrete_cover: float)`

Create a 3-dimensional rebar shape for the column corbel. The created shape has 5 legs in total.
The corbel is assumed to be at the right side of the columns rectangular cross-section.
The shape's legs are created in following directions: Z+, X+, Y+, X-, Z-.
This means, that from above the generated shape will look like Ↄ

In addition, following assumptions are made:

-   First and last legs (the vertical ones, parallel to Z axis) are 1m long
-   Bending roller is the same for all legs
-   Cross section of the column is a rectangle
-   Corbel Y-dimension is the same as the Y-dimension of the column's cross section
-   All concrete covers are assumed to be identical

Args:
    column_width:        Width (X-dimension) of the column's cross-section
    column_thickness:    Thickness (Y-dimension) of the column's cross-section
    corbel_width:        Corbel width (X-dimension)
    corbel_top:          Elevation (Z-coordinate) of the corbel's top surface
    model_angles:        Angles to rotate the shape from local to global coordinate system.
    shape_props:         Shape properties
    concrete_cover:      Concrete cover at the shape sides

Returns:
    Bar shape in world coordinates

**Parameter:**
- `column_width: float`
- `column_thickness: float`
- `corbel_width: float`
- `corbel_top: float`
- `model_angles: RotationAngles`
- `shape_props: ReinforcementShapeProperties`
- `concrete_cover: float`

**Rückgabe:** `AllplanReinf.BendingShape`

**Beispiel:**
```python
result = column_corbel_shape_type1(..., ..., ..., ..., ..., ..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""Implementation of the functions for the creation of the reinforcement corbel shapes
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties
from StdReinfShapeBuilder.RotationAngles import RotationAngles


def column_corbel_shape_type1(column_width    : float,
                              column_thickness: float,
                              corbel_width    : float,
                              corbel_top      : float,
                              model_angles    : RotationAngles,
                              shape_props     : ReinforcementShapeProperties,
                              concrete_cover  : float) -> AllplanReinf.BendingShape:
    """Create a 3-dimensional rebar shape for the column corbel. The created shape has 5 legs in total.
    The corbel is assumed to be at the right side of the columns rectangular cross-section.
    The shape's legs are created in following directions: Z+, X+, Y+, X-, Z-.
    This means, that from above the generated shape will look like Ↄ

    In addition, following assumptions are made:

    -   First and last legs (the vertical ones, parallel to Z axis) are 1m long
    -   Bending roller is the same for all legs
    -   Cross section of the column is a rectangle
    -   Corbel Y-dimension is the same as the Y-dimension of the column's cross section
    -   All concrete covers are assumed to be identical

    Args:
        column_width:        Width (X-dimension) of the column's cross-section
        column_thickness:    Thickness (Y-dimension) of the column's cross-section
        corbel_width:        Corbel width (X-dimension)
        corbel_top:          Elevation (Z-coordinate) of the corbel's top surface
        model_angles:        Angles to rotate the shape from local to global coordinate system.
        shape_props:         Shape properties
        concrete_cover:      Concrete cover at the shape sides

    Returns:
        Bar shape in world coordinates
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(0., 0.), concrete_cover),
                             (AllplanGeo.Point2D(0., corbel_top), -concrete_cover),
                             (AllplanGeo.Point2D(column_width + corbel_width, corbel_top), -concrete_cover),
                             (concrete_cover + shape_props.diameter / 2)])

    shape_builder.SetSideLengthStart(1000.)

    shape = shape_builder.CreateShape(shape_props)

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

        shape_pol = shape.GetShapePolyline()
        shape_pol1 = AllplanGeo.Move(shape_pol,
                                     AllplanGeo.Vector3D(0, column_thickness - concrete_cover * 2 - \
                                                         shape_props.diameter, 0))

        for i in range(2, -1, -1):
            shape_pol += shape_pol1[i]

        bending_roller_vec = shape.GetBendingRoller()

        bending_roller_vec.append(shape_props.bending_roller)
        bending_roller_vec.append(shape_props.bending_roller)
        bending_roller_vec.append(shape_props.bending_roller)

        shape.SetShapePolyline(shape_pol)
        shape.SetBendingRoller(bending_roller_vec)

    return shape

```

</details>