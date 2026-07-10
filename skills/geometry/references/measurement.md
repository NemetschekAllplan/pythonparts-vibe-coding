---
name: geometry-measurement
description: How to calculate lengths, areas, volumes, centers of gravity, compare geometry, and validate/repair polyhedrons.
---

## Length (CalcLength)

```python
length = AllplanGeo.CalcLength(curve)  # any linear object
```

## Area (CalcArea)

For closed, **planar** objects only (e.g., `Polygon3D`):

```python
area = AllplanGeo.CalcArea(polygon)
```

For curved surfaces, use `CalcMass` on the BRep/Polyhedron representing that surface.

## Volume, Surface, Center of Gravity (CalcMass)

For closed-volume solids (`Polyhedron3D` or `BRep3D`). Also works on surfaces (to get curved surface area).

```python
mass = AllplanGeo.CalcMass(solid)
# mass.Volume, mass.Surface, mass.CenterOfGravity
```

> Center of gravity is (0,0,0) for surfaces — only valid for volumetric solids.

## Center of Curve (CenterCalculus)

```python
center = AllplanGeo.CenterCalculus(curve)
```

- Open curve: returns midpoint along the curve (not center of gravity).
- Closed curve (e.g., closed `Polygon3D`, closed `BSpline3D`): returns center of gravity of enclosed area.

## Comparison

### Equality

Without tolerance:

```python
geo_a == geo_b
```

With tolerance:

```python
AllplanGeo.Comparison.Equal(geo_a, geo_b, tolerance)
AllplanGeo.Comparison.EqualRel(geo_a, geo_b, tolerance)  # also considers ALLPLAN min-distance setting
```

> **Warning:** Tolerance is not a direct delta — it's used to *calculate* the delta based on floating-point precision. Use very small values (e.g., `1e-11`). For large coordinates, the effective delta grows.

### Position (DeterminePosition)

Determines where a point is relative to another geometry:

```python
result = AllplanGeo.Comparison.DeterminePosition(point, reference_geometry, tolerance)
```

Returns `eComparisionResult`:
- For solids: inside / outside
- For surfaces: on / not on
- For lines: on / at start / at end / above / below

> For 2D point vs. line: "above"/"below" is only meaningful when line goes left→right.

## Polyhedron Validation & Repair

Invalid polyhedrons (e.g., from import) cause boolean operation failures or wrong quantity results.

| Problem | Repair Method |
|---------|--------------|
| Inconsistent face normals | `PolyhedronUtil.RepairFaceNormals()` |
| Crossed face loops (figure-8) | `PolyhedronUtil.RepairPolyhedronCrossLoopFaces()` |
| Edge lying on another face | `PolyhedronUtil.SplitFacesAtEdges()` |
| Non-planar face | `PolyhedronUtil.SplitNonPlanarFaces()` |
| Redundant coplanar faces | `PolyhedronUtil.MergePlanarFaces()` |
| Overlapping edges | `PolyhedronUtil.SimplifyPolyhedron()` |
| General repair (combines several) | `PolyhedronUtil.RepairPolyhedron()` |

> Some methods are **mutators** — they modify the polyhedron in-place rather than returning a new one.
