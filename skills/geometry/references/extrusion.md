---
name: geometry-extrusion
description: How to create solids by extruding 2D/3D profiles vertically or along a vector.
---

## Extrude Vertically (ClippedSweptSolid3D)

Extrudes a 2D profile along the Z-axis, bounded by two arbitrarily oriented planes. Result is a `Polyhedron3D`.

### Steps

1. **Create closed Polygon2D:**

```python
polygon = AllplanGeo.Polygon2D()
polygon += AllplanGeo.Point2D(0, 0)
polygon += AllplanGeo.Point2D(1000, 0)
polygon += AllplanGeo.Point2D(1000, 500)
polygon += AllplanGeo.Point2D(0, 500)
polygon += polygon.StartPoint  # close it
```

2. **Wrap in PolygonalArea2D** (can hold multiple polygons with same orientation):

```python
area = AllplanGeo.PolygonalArea2D()
area += polygon
```

3. **Define bounding planes** (top and bottom):

```python
bottom_plane = AllplanGeo.Plane3D(AllplanGeo.Point3D(0, 0, 0),
                                  AllplanGeo.Vector3D(0, 0, 1))
top_plane = AllplanGeo.Plane3D(AllplanGeo.Point3D(0, 0, 1000),
                               AllplanGeo.Vector3D(0, 0, 1))
```

> Planes can be tilted — this creates sloped top/bottom faces.

4. **Create and convert:**

```python
swept_solid = AllplanGeo.ClippedSweptSolid3D(area, bottom_plane, top_plane)
err, polyhedron = AllplanGeo.CreatePolyhedron(swept_solid)
```

## Extrude Along Vector (ExtrudedAreaSolid3D)

Extrudes a 3D planar profile along any vector (not limited to Z). Result is a `Polyhedron3D`.

### Steps

1. **Create closed Polygon3D** (can be freely oriented in space):

```python
polygon = AllplanGeo.Polygon3D()
polygon += AllplanGeo.Point3D(0, 0, 0)
polygon += AllplanGeo.Point3D(500, 0, 0)
polygon += AllplanGeo.Point3D(500, 300, 0)
polygon += AllplanGeo.Point3D(0, 300, 0)
polygon += polygon.StartPoint  # close it
```

2. **Wrap in PolygonalArea3D:**

```python
area = AllplanGeo.PolygonalArea3D()
area += polygon
```

> All polygons in the area must be **coplanar**. Validate with `area.GetPlane()`.

3. **Create ExtrudedAreaSolid3D:**

```python
extruded = AllplanGeo.ExtrudedAreaSolid3D()
extruded.SetDirection(AllplanGeo.Vector3D(0, 0, 1000))  # extrusion direction+length
extruded.SetRefPoint(polygon.StartPoint)
extruded.SetExtrudedArea(area)
```

> The extrusion vector does not have to be perpendicular to the polygon.

4. **Convert to Polyhedron:**

```python
err, polyhedron = AllplanGeo.CreatePolyhedron(extruded)
```
