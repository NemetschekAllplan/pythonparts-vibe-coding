---
name: geometry-tessellation
description: How to convert BRep3D to Polyhedron3D via tessellation (surface approximation).
---

## Purpose

Tessellation approximates curved BRep surfaces with planar faces (triangles/quads), producing a `Polyhedron3D`. Required when:

- You need to perform polyhedron-only operations on a BRep.
- Using `HiddenCalculus` (only accepts polyhedrons).
- Mixing BRep with polyhedrons in boolean operations.

## Steps

### 1. Define Tessellation Settings

```python
settings = AllplanGeo.ApproximationSettings(AllplanGeo.ASET_BREP_TESSELATION)
settings.SetBRepTesselation(
    density   = 0.5,             # 0..1, higher = denser mesh (required)
    maxAngle  = AllplanGeo.Angle(),  # max angle between faces, 0 = ignored (1°–90°)
    minLength = 0.0,             # min edge length, 0 = ignored
    maxLength = 0.0)             # max edge length, 0 = ignored
```

| Parameter | Effect |
|-----------|--------|
| `density` | **Required.** 0–1 factor controlling mesh density. Higher = smoother but heavier. |
| `maxAngle` | Limits angle between adjacent faces. Lower = smoother. Range: 1°–90°, 0 = off. |
| `minLength` | Minimum triangle edge length. Higher = sparser mesh. 0 = off. |
| `maxLength` | Maximum triangle edge length. Lower = denser mesh. 0 = off. |

### 2. Create Polyhedron

```python
err, polyhedron = AllplanGeo.CreatePolyhedron(brep, settings)
```

## Quick Tessellation (Cylinder3D)

Some objects like `Cylinder3D` support direct tessellation by segment count:

```python
err, polyhedron = AllplanGeo.CreatePolyhedron(cylinder_3d, 36)  # 36 segments
```

## Notes

- Tessellation is **lossy** — curved surfaces become faceted.
- For the reverse direction (polyhedron → BRep): use `AllplanGeo.CreateBRep3D(polyhedron)` (lossless).
- The `density` parameter alone is usually sufficient. Add constraints only when specific smoothness or performance requirements exist.
