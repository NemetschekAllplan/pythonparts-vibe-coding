---
name: geometry-objects
description: How to construct geometry primitives and curves using the NemAll_Python_Geometry module.
---

## Primitives

### Angle

Represents an angle in **radians**.

```python
angle = AllplanGeo.Angle(math.pi / 2)        # from radians
angle = AllplanGeo.Angle.FromDeg(90)          # from degrees
value = float(angle)                          # always returns radians
```

Supports arithmetic: `+`, `-`, comparison operators.

### Point2D / Point3D

Coordinates in **millimeters**. Supports arithmetic (`+`, `-`, `/`, `*`).

```python
p2 = AllplanGeo.Point2D(1000, 1000)
p3 = AllplanGeo.Point3D(1000, 1000, 500)
p3 = AllplanGeo.Point3D(p2)                   # 2D→3D, Z=0
```

### Vector2D / Vector3D

Direction + magnitude. Coordinates in mm.

```python
v = AllplanGeo.Vector3D(1, 0, 0)
cross = v1 * v2                               # cross product (returns Vector3D)
dot = v1.DotProduct(v2)                       # dot product (returns float)
```

Note: 2D cross product `v1 * v2` returns a `Vector3D`.

## Linear Objects

### Line2D / Line3D

Directed line segment defined by start and end point.

```python
line = AllplanGeo.Line3D(AllplanGeo.Point3D(0,0,0), AllplanGeo.Point3D(1000,0,0))
```

### Arc2D / Arc3D

Represents circular or elliptical arcs. No separate circle/ellipse class — a closed arc is a circle.

```python
arc = AllplanGeo.Arc3D(center=     AllplanGeo.Point3D(),
                       xDir=       AllplanGeo.Vector3D(1, 0, 0),
                       normVector= AllplanGeo.Vector3D(0, 0, 1),
                       major=      500,
                       minor=      500,
                       startAngle= 0,
                       deltaAngle= 2 * math.pi)  # full circle

arc.IsClosed()    # True for full circle/ellipse
arc.IsCircle()    # True if major == minor
```

- `Arc3D` requires a normal vector (direction per right-hand rule).
- `Arc2D` uses `startangle`/`endangle`; `Arc3D` uses `startAngle`/`deltaAngle`.

### Polyline2D / Polyline3D

Open polygonal chain. Add points with `+=`. Points in 3D need not be coplanar.

```python
polyline = AllplanGeo.Polyline3D()
polyline += AllplanGeo.Point3D(0, 0, 0)
polyline += AllplanGeo.Point3D(1000, 500, 0)
polyline += AllplanGeo.Point3D(2000, 0, 300)
```

### Spline2D / Spline3D

Smooth curve through control points. Optional start/end tangent vectors.

```python
spline = AllplanGeo.Spline3D()
spline += AllplanGeo.Point3D(0, 0, 0)
spline += AllplanGeo.Point3D(500, 200, 100)
spline += AllplanGeo.Point3D(1000, 0, 0)
spline.StartVector = AllplanGeo.Vector3D(1, 1, 0)  # optional
spline.EndVector = AllplanGeo.Vector3D(1, -1, 0)   # optional
```

### Axis2D / Axis3D

Infinite line (no start/end, no length). Defined by point + direction vector.

```python
axis = AllplanGeo.Axis3D(AllplanGeo.Point3D(), AllplanGeo.Vector3D(0, 0, 1))
```

## Areal / Planar Objects

### Plane3D

Infinite plane. Defined by point + normal vector, or by three points.

```python
plane = AllplanGeo.Plane3D(AllplanGeo.Point3D(0, 0, 500),
                           AllplanGeo.Vector3D(0, 0, 1))
```

### Polygon2D / Polygon3D

Closed polygon. Rules:
- Does **not** auto-close: last point must equal first point.
- Orientation must be monotonous (all CW or all CCW).
- Must not self-intersect.
- 3D polygon must be **planar** (all points coplanar). Check with `IsValid()` / `IsValidStatus()`.

```python
polygon = AllplanGeo.Polygon3D()
polygon += AllplanGeo.Point3D(0, 0, 0)
polygon += AllplanGeo.Point3D(1000, 0, 0)
polygon += AllplanGeo.Point3D(1000, 1000, 0)
polygon += AllplanGeo.Point3D(0, 1000, 0)
polygon += polygon.Points[0]  # close it
```

**Compound polygons (holes):** Use opposite orientation for holes. Insert hole with `InsertPolygon()`:

```python
polygon.InsertPolygon(hole_polygon, position=len(polygon.Points))
```

### AxisPlacement2D / AxisPlacement3D

Local coordinate system. 2D: point + X-direction. 3D: origin + X-direction + Z-direction.

```python
placement = AllplanGeo.AxisPlacement3D(
    AllplanGeo.Point3D(),
    AllplanGeo.Vector3D(1, 0, 0),
    AllplanGeo.Vector3D(0, 0, 1))
```

X and Z vectors must be perpendicular. Validate with `IsValid()`.
