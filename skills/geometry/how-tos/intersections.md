---
name: geometry-intersections
description: How to calculate geometric intersections between curves, planes, and solids.
---

## Choosing the Right Function

| First ↓ / Second → | Curve | Plane | Solid |
|---------------------|-------|-------|-------|
| **Curve** | `IntersectionCalculus` | `IntersectionCalculus` | `IntersectRayBRep` / `IntersectRayPolyhedron` |
| **Plane** | `IntersectionCalculus` | `Intersect` | `CutBrepWithPlane` / `CutPolyhedronWithPlane` |
| **Solid** | `IntersectRayBRep` / `IntersectRayPolyhedron` | `CutBrepWithPlane` / `CutPolyhedronWithPlane` | `Intersect` |

## Curve with Curve / Curve with Plane (IntersectionCalculus)

Returns intersection **points**.

```python
intersecting, points = AllplanGeo.IntersectionCalculus(
    ele1         = first_geometry,
    ele2         = second_geometry,
    eps          = 10,          # tolerance (relevant for splines only)
    maxSolutions = 3)           # relevant for splines only
```

- Works with any combination of Line, Arc, Polyline, Spline, Plane.
- Does **not** throw errors for incompatible types — just returns no intersection.
- To only check *whether* curves intersect (without computing points): `AllplanGeo.Intersecting(geo1, geo2)`.

## Solid with Solid (Intersect)

Returns the intersection **solid** (boolean intersection). See [boolean-operations.md](boolean-operations.md).

```python
intersecting, result = AllplanGeo.Intersect(solid_a, solid_b)
```

Quick collision check without computing the result solid: `AllplanGeo.Intersecting(solid_a, solid_b)`.

## Solid with Plane (CutPolyhedronWithPlane / CutBrepWithPlane)

Splits a solid into two halves.

```python
is_cutting, solid_above, solid_below = \
    AllplanGeo.CutBrepWithPlane(solid_to_cut, cutting_plane)
```

- `solid_above` is on the **positive side of the plane's normal vector** (not necessarily geometrically "above").
- To get the intersection polygon: inspect faces of `solid_below` for the one matching the cutting plane's normal.

Same API for polyhedrons:

```python
is_cutting, above, below = AllplanGeo.CutPolyhedronWithPlane(polyhedron, plane)
```

## Ray with Solid (IntersectRayPolyhedron / IntersectRayBRep)

Finds where a ray (point + direction vector) pierces a solid.

### Polyhedron

```python
err, result = AllplanGeo.IntersectRayPolyhedron(
    ray_point,
    ray_vector,
    polyhedron,
    AllplanGeo.IntersectRayPolyhedronFlag.ePositiveOnly,  # direction filter
    face_list)  # optional: limit to specific face indices
```

Result is `IntersectionRayPolyhedron` with: intersection point, face number, normal vector, lambda.

### BRep

```python
err, result = AllplanGeo.IntersectRayBRep(
    ray_point,
    ray_vector,
    brep,
    False)  # False = prefer positive direction hit
```

Result is `IntersectionRayBRep` with: intersection point, face number.
