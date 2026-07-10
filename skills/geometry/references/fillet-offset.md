---
name: geometry-fillet-offset
description: How to fillet edges/lines and create offset curves or shell solids.
---

## Fillet

### Fillet Solid Edges (FilletCalculus3D)

Rounds edges of a `Polyhedron3D` or `BRep3D`. Result is always `BRep3D` (curved faces).

**Polyhedron** — must specify which edges to fillet:

```python
import NemAll_Python_Utility as AllplanUtil

edges = AllplanUtil.VecSizeTList([0, 1, 2, 5])  # edge indices

err, filleted = AllplanGeo.FilletCalculus3D.Calculate(
    polyhedron, edges, radius=50, propagation=True)
```

**BRep** — fillets all edges:

```python
err, filleted = AllplanGeo.FilletCalculus3D.Calculate(brep, radius=50)
```

### Fillet Two 2D Lines/Arcs (FilletCalculus2D)

Calculates fillet arc(s) between two `Line2D` or `Arc2D`.

```python
fillet_calc = AllplanGeo.FilletCalculus2D(line_a, line_b, r=200)

# Get all possible solutions (up to 16)
all_arcs = fillet_calc.GetFillets()

# Or get the one nearest to a point
nearest_arc = fillet_calc.GetNearest(AllplanGeo.Point2D(500, 300))
```

Check fillet type beforehand: `AllplanGeo.FilletCalculus2D.GetFilletType(line_a, line_b)`.

### Fillet Two 3D Lines (FilletCalculus3D)

Lines must be **coplanar**.

**Non-parallel:**

```python
err, trimmed_a, trimmed_b, fillet_arc = \
    AllplanGeo.FilletCalculus3D.Calculate(line_a, line_b, radius=50)
```

**Parallel** (radius = half distance between end of first and start of second):

```python
err, fillet_arc = AllplanGeo.FilletCalculus3D.Calculate(line_a, line_b)
```

> For parallel lines: line directions must be opposite. End of first connects to start of second.

## Offset

### Curve Offset

Creates a parallel curve at a distance. Works with Line, Arc, Polyline, Spline, Path (2D and 3D).

**By distance:**

```python
err, offset_curve = AllplanGeo.Offset(100, line_2d)
```

**By helping point** (determines which side):

```python
err, offset_curve = AllplanGeo.Offset(point, line_2d)
```

3D notes:
- 3D offset produces a **planar** curve in a specified `Plane3D` (extra argument).
- For `Line3D`, use `Offset3DPlane` instead of `Plane3D`.
- For `Line3D` with distance, also provide a point to determine offset direction.

### Face Offset (FaceOffset)

Calculates offset surfaces or shell solids from `Polyhedron3D` or `BRep3D`.

```python
face_offset = AllplanGeo.FaceOffset(solid, faceIndices=idx_vec)  # idx_vec optional
```

**Offset** — produces offset surface(s) (no volume, except when all faces selected on a polyhedron):

```python
err, geo_1, geo_2 = face_offset.Offset(
    offsetDistance      = 100,
    direction           = AllplanGeo.FaceOffset.eNormalDirection,
    useOffsetStepPierce = False,
    useOrthoVXSplit     = False,
    punchDirection      = None)   # None = offset in face normal direction
```

**Shell** — like offset but fills the space between source and offset (creates volume):

```python
err, shell_solid = face_offset.Shell(
    offsetDistance      = 100,
    direction           = AllplanGeo.FaceOffset.eNormalDirection,
    useOffsetStepPierce = False,
    useOrthoVXSplit     = False,
    punchDirection      = None)
```

- `direction`: Use `eNormalDirection`, `eOppositeDirection`, or `eBothDirections`.
- `punchDirection`: When set, overrides face normals (cannot be coplanar with offset faces).
- `useOffsetStepPierce`: Consider adjoining non-selected faces.
- `useOrthoVXSplit`: Fill transitions between source and result with solid.
