# Verified Geometry Patterns

## Canonical import
```python
import NemAll_Python_Geometry as AllplanGeo
```

## Basic solids
```python
# from dimensions
solid = AllplanGeo.Polyhedron3D.CreateCuboid(1000.0, 500.0, 3000.0)

# from two points
solid2 = AllplanGeo.Polyhedron3D.CreateCuboid(
    AllplanGeo.Point3D(0.0, 0.0, 0.0),
    AllplanGeo.Point3D(1000.0, 500.0, 3000.0),
)
```

## Boolean operations return tuples
```python
err, union_result = AllplanGeo.MakeUnion(a, b)
err, cut_result = AllplanGeo.MakeSubtraction(a, b)
err, int_result = AllplanGeo.MakeIntersection(a, b)
```

## Transform is a free function
```python
m = AllplanGeo.Matrix3D()
transformed = AllplanGeo.Transform(geometry, m)
```

## Forbidden calls (hallucination traps)
- `AllplanGeo.Box3D(...)`
- `AllplanGeo.Cylinder(...)`
- `AllplanGeo.Sphere(...)`
- `Polyhedron3D.CreateBox(...)`
- `geometry.transform(...)`

## Notes
- Keep all dimensions in millimeters.
- Prefer simple verified geometry first, then refine.
- For unstable preview/runtime behavior, reduce to minimal stable primitives.
