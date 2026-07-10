---
name: geometry-basic-solids
description: How to create basic 3D solid shapes (cuboid, cylinder, cone, sphere) as Polyhedron3D or BRep3D.
---

## Polyhedron vs. BRep

| Aspect | Polyhedron3D | BRep3D |
|--------|-------------|--------|
| Engine | ALLPLAN internal | Parasolid |
| Faces | Planar only | Curved (NURBS) |
| Performance | Generally faster | Heavier |
| Model element type | `Volume3D_TypeUUID` | `BRep3D_Volume_TypeUUID` |

**Prefer polyhedrons** unless curved surfaces are needed. Never switch representation when modifying existing elements.

## Cuboid

### As Polyhedron

```python
cuboid = AllplanGeo.Polyhedron3D.CreateCuboid(
    placement = AllplanGeo.AxisPlacement3D(),
    length    = 1000,
    width     = 2000,
    height    = 3000)
```

Or from two corner points (lower-left to upper-right):

```python
cuboid = AllplanGeo.Polyhedron3D.CreateCuboid(
    AllplanGeo.Point3D(0, 0, 0),
    AllplanGeo.Point3D(1000, 2000, 3000))
```

> Ensure point_1 is lower-left and point_2 is upper-right, otherwise negative geometry is created.

### As BRep

```python
cuboid = AllplanGeo.BRep3D.CreateCuboid(
    placement = AllplanGeo.AxisPlacement3D(),
    length    = 1000.0,
    width     = 2000.0,
    height    = 3000.0)
```

Alternative: `Cuboid3D` object (more cuboid-specific methods):

```python
cuboid = AllplanGeo.Cuboid3D(
    refPoint=   AllplanGeo.Point3D(),
    startPoint= AllplanGeo.Point3D(),
    vec1=       AllplanGeo.Vector3D(1000, 0, 0),
    vec2=       AllplanGeo.Vector3D(0, 2000, 0),
    vec3=       AllplanGeo.Vector3D(0, 0, 3000))
```

All direction vectors must be perpendicular.

## Cylinder

### As BRep

```python
cylinder = AllplanGeo.BRep3D.CreateCylinder(
    placement    = AllplanGeo.AxisPlacement3D(),
    radius       = 500,
    height       = 1000,
    closedBottom = True,
    closedTop    = True)
```

Or via `Cylinder3D` (more control, supports elliptical/oblique):

```python
cylinder = AllplanGeo.Cylinder3D(
    refPlacement = AllplanGeo.AxisPlacement3D(),
    radiusMajor  = 500,
    radiusMinor  = 500,
    apex         = AllplanGeo.Point3D(0, 0, 1000))
```

> **Warning:** An elliptical or oblique `Cylinder3D` **cannot** create a `ModelElement3D` — it silently produces nothing.

### As Polyhedron

Create `Cylinder3D` first, then tessellate:

```python
cylinder = AllplanGeo.Cylinder3D(
    refPlacement = AllplanGeo.AxisPlacement3D(),
    radiusMajor  = 500,
    radiusMinor  = 300,
    apex         = AllplanGeo.Point3D(0, 0, 1000))

err, polyhedron = AllplanGeo.CreatePolyhedron(cylinder, 36)  # 36 segments
```

## Cone

### As BRep

```python
cone = AllplanGeo.Cone3D(
    refPlacement = AllplanGeo.AxisPlacement3D(),
    radiusMajor  = 500,
    radiusMinor  = 200,
    apex         = AllplanGeo.Point3D(0, 0, 1000))

cone_brep = AllplanGeo.BRep3D.CreateCone(cone, True)  # True = closed caps
```

> Apex must be on the local Z axis. Oblique cones are not supported.

### As Polyhedron

Create BRep first, then tessellate:

```python
settings = AllplanGeo.ApproximationSettings(AllplanGeo.ASET_BREP_TESSELATION)
settings.SetBRepTesselation(0.2, AllplanGeo.Angle(), 0, 0)

err, polyhedron = AllplanGeo.CreatePolyhedron(cone_brep, settings)
```

## Sphere

### As BRep

```python
sphere = AllplanGeo.BRep3D.CreateSphere(
    placement = AllplanGeo.AxisPlacement3D(),
    radius    = 500)
```

### As Polyhedron

Tessellate the BRep:

```python
settings = AllplanGeo.ApproximationSettings(AllplanGeo.ASET_BREP_TESSELATION)
settings.SetBRepTesselation(0.2, AllplanGeo.Angle(), 0, 0)

err, polyhedron = AllplanGeo.CreatePolyhedron(sphere, settings)
```
