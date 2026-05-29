---
name: geometry
description: Principles and techniques for creating and manipulating geometry using ALLPLAN's geometry engine (NemAll_Python_Geometry module).
---

## Overview

All geometry in ALLPLAN PythonParts is constructed using the `NemAll_Python_Geometry` module (aliased as `AllplanGeo`):

```python
import NemAll_Python_Geometry as AllplanGeo
```

Geometry objects are **pure mathematical constructs** — they define shapes in space but are not ALLPLAN model elements on their own. To place geometry into the model, wrap it in an `AllplanElement` (see the `allplan-elements` skill).

## Core Principles

### Units

- All coordinates and distances are in **millimeters**.
- All angles are in **radians** (use `AllplanGeo.Angle.FromDeg()` for degrees).

### 2D / 3D Duality

Most geometry types exist in both 2D and 3D variants (`Point2D`/`Point3D`, `Line2D`/`Line3D`, etc.). They share similar APIs but live in different coordinate spaces. A 3D object can often be constructed from its 2D counterpart (Z defaults to 0).

### Two Solid Representations

ALLPLAN supports two types of volumetric solids:

| Type | Class | Engine | Faces |
|------|-------|--------|-------|
| Polyhedron | `Polyhedron3D` | ALLPLAN internal | Planar only |
| BRep | `BRep3D` | Parasolid | Curved (NURBS) |

**Prefer polyhedrons** for performance. Use BRep when curved surfaces are required. Do not mix them in boolean operations — convert first.

> When a `BRep3D` constructs a `ModelElement3D`, the element type is `BRep3D_Volume_TypeUUID`.  
> When a `Polyhedron3D` is used, the type is `Volume3D_TypeUUID`.  
> Never switch between them when modifying existing elements.

### Transformation via Matrices

All spatial transformations (translate, rotate, scale, reflect) are expressed as `Matrix3D` (or `Matrix2D`). Apply with multiplication:

```python
geometry *= matrix
```

Matrices compose via multiplication (order matters — not commutative).

### Error Handling Pattern

Many geometry functions return an `(error_code, result)` tuple. Always check the error code before using the result.

```python
err, polyhedron = AllplanGeo.CreatePolyhedron(solid)
```

## Geometry Object Categories

| Category | Examples | Characteristics |
|----------|----------|-----------------|
| Primitives | `Point2D/3D`, `Vector2D/3D`, `Angle` | Building blocks, support arithmetic |
| Linear | `Line`, `Arc`, `Polyline`, `Spline`, `Axis` | Curves with length, no area |
| Areal | `Polygon2D/3D`, `Plane3D` | Closed/planar, have area |
| Volumetric | `Polyhedron3D`, `BRep3D` | Solids with volume |

## How-To Articles

Load these on demand based on the task:

- [**how-tos/geometry-objects.md**](how-tos/geometry-objects.md) — Constructing geometry primitives and curves (Point, Vector, Angle, Line, Arc, Polyline, Polygon, Spline, Axis, AxisPlacement, Plane)
- [**how-tos/basic-solids.md**](how-tos/basic-solids.md) — Creating basic 3D solids (cuboid, cylinder, cone, sphere) as Polyhedron or BRep
- [**how-tos/extrusion.md**](how-tos/extrusion.md) — Extruding profiles vertically or along a vector
- [**how-tos/sweep.md**](how-tos/sweep.md) — Sweeping profiles along a path or rails
- [**how-tos/revolve-loft.md**](how-tos/revolve-loft.md) — Creating solids by revolving or lofting profiles
- [**how-tos/build-from-scratch.md**](how-tos/build-from-scratch.md) — Building BRep or Polyhedron from scratch (BRep3DBuilder, Polyhedron3DBuilder)
- [**how-tos/boolean-operations.md**](how-tos/boolean-operations.md) — Union, subtraction, and intersection of solids
- [**how-tos/intersections.md**](how-tos/intersections.md) — Calculating geometric intersections (curve-curve, curve-plane, solid-solid, solid-plane, ray-solid)
- [**how-tos/transformations.md**](how-tos/transformations.md) — Translation, rotation, scaling, reflection, projection, and composing transformations
- [**how-tos/fillet-offset.md**](how-tos/fillet-offset.md) — Fillet edges/lines and offset curves/faces
- [**how-tos/measurement.md**](how-tos/measurement.md) — Length, area, volume calculation, center of gravity, comparison, and polyhedron validation/repair
- [**how-tos/hidden-calculation.md**](how-tos/hidden-calculation.md) — Projecting 3D geometry to 2D lines (visible/hidden edges)
- [**how-tos/tessellation.md**](how-tos/tessellation.md) — Converting BRep to Polyhedron via tessellation
