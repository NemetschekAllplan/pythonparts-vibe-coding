---
name: geometry-transformations
description: How to translate, rotate, scale, reflect, and project geometry using transformation matrices.
---

## Matrix Basics

- 2D: `Matrix2D` (3×3). 3D: `Matrix3D` (4×4).
- Apply to geometry via multiplication: `geometry *= matrix` or `result = geometry * matrix`.
- Alternative: `AllplanGeo.Transform(geometry, matrix)`.
- Matrices compose via multiplication (**order matters** — not commutative).

## Translation

Move geometry by a vector.

```python
matrix = AllplanGeo.Matrix3D()
matrix.SetTranslation(AllplanGeo.Vector3D(100, 200, 300))
geometry *= matrix
```

Shortcut without matrix:

```python
result = AllplanGeo.Move(geometry, AllplanGeo.Vector3D(100, 200, 300))
```

## Rotation

Rotate around an axis (defined as `Line3D`) by an angle. Direction follows right-hand rule.

```python
axis = AllplanGeo.Line3D(AllplanGeo.Point3D(0,0,0), AllplanGeo.Point3D(0,0,1))
angle = AllplanGeo.Angle.FromDeg(45)

matrix = AllplanGeo.Matrix3D()
matrix.SetRotation(axis, angle)
geometry *= matrix
```

Shortcut (2D):

```python
result = AllplanGeo.Rotate(geometry, AllplanGeo.Point2D(0,0), angle)
```

## Scaling

Scale by factors per axis. Reference point is origin.

```python
matrix = AllplanGeo.Matrix3D()
matrix.SetScaling(2.0, 1.5, 1.0)  # Sx, Sy, Sz
geometry *= matrix
```

## Reflection (Mirror)

Reflection = scaling by -1. Dedicated methods exist for arbitrary mirror planes.

```python
matrix = AllplanGeo.Matrix3D()
matrix.SetReflection(AllplanGeo.Plane3D(AllplanGeo.Point3D(), AllplanGeo.Vector3D(1,0,0)))
```

> **Warning:** Matrix-based reflection creates **negative geometry** (inverted normals). Use `AllplanGeo.Mirror()` instead for solids:

```python
mirror_plane = AllplanGeo.Plane3D(AllplanGeo.Point3D(), AllplanGeo.Vector3D(1, 0, 0))
result = AllplanGeo.Mirror(geometry, mirror_plane)
```

## Projection

Construct a view-direction matrix from predefined types:

```python
matrix = AllplanGeo.Matrix3D(AllplanGeo.eProjectionMatrixType.RIGHT_2D)
```

Useful for setting view matrices (e.g., `ViewSectionElement.ViewMatrix`) or for `HiddenCalculus` observer setup.

## Composing Transformations

### Additive Methods (modify in-place)

`Set*` overwrites the matrix. Methods without `Set` prefix **add** to existing:

```python
matrix = AllplanGeo.Matrix3D()
matrix.SetScaling(2, 2, 2)           # matrix = scaling only
matrix.Rotation(axis, angle)         # adds rotation (after scaling)
matrix.Translate(AllplanGeo.Vector3D(0, 0, 500))  # adds translation (after rotation)
```

Execution order when applied: scale → rotate → translate.

### Matrix Multiplication

Combine two full matrices. **Left is applied first:**

```python
combined = first_matrix * second_matrix
geometry *= combined  # applies first_matrix, then second_matrix
```
