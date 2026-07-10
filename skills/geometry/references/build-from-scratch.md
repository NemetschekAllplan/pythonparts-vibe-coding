---
name: geometry-build-from-scratch
description: How to build BRep3D or Polyhedron3D geometry from scratch using builders.
---

## BRep3DBuilder

Constructs a BRep by explicitly defining faces, loops, edges, and vertices. Use when no standard creation method fits.

### Workflow

1. **Define faces** — Each face is a surface (`Plane3D` or `BSplineSurface3D`). Normal must point **outward** for closed solids.
2. **Define loops** — Each face has one or more closed edge loops.
3. **Define edges** — Curves (`Line3D`, `Arc3D`, `BSpline3D`, `Polyline3D`) where surfaces meet. Orientation follows right-hand rule relative to face normal.
4. **Define vertices** — Points where edges meet. Closed edge = 1 vertex; open edge = 2 vertices (start, end).

### Example: Cylinder

```python
builder = AllplanGeo.BRep3DBuilder()
builder.Init(True)  # True = closed solid

# Top face (planar)
top_surface = AllplanGeo.Plane3D(AllplanGeo.Point3D(0, 0, 1000),
                                 AllplanGeo.Vector3D(0, 0, 1))
top_face_idx = builder.AddFace(top_surface, sense=True)  # normal already points out
top_loop_idx = builder.AddLoop(top_face_idx)
top_edge_idx = builder.AddEdge(curve_object=top_circle,  # Arc3D or BSpline3D
                               curveSense=True,
                               edgeSense=True,
                               loopIdx=top_loop_idx,
                               precision=0.5)
top_vtx_idx = builder.AddVertex(point=top_circle.StartPoint,
                                edgeIdx=top_edge_idx,
                                precision=0.5)
builder.CheckLoop(top_loop_idx)

# Bottom face — flip sense if normal points wrong direction
bottom_face_idx = builder.AddFace(bottom_surface, sense=False)
# ... define loop, edge, vertex similarly

# Lateral face — use BSplineSurface3D for curved surface
lateral_face_idx = builder.AddFace(lateral_nurbs, sense=True)
lateral_loop_idx = builder.AddLoop(lateral_face_idx)
# Add edges (reuse existing edge indices with flipped sense)
builder.AddEdge(top_edge_idx, False, lateral_loop_idx)     # reuse, flip
builder.AddEdge(side_edge_idx, False, lateral_loop_idx)
builder.AddEdge(bottom_edge_idx, False, lateral_loop_idx)
builder.CheckLoop(lateral_loop_idx)

brep = builder.Complete()
```

### Key Rules

- `sense` on `AddFace`: `True` if the surface's normal already points outward, `False` to flip.
- `curveSense` on `AddEdge`: `True` if the curve's direction matches the loop direction, `False` to flip.
- `edgeSense`: Controls how the edge is traversed in its loop.
- Reuse existing edges/vertices by passing their index (shorter overload of `AddEdge`/`AddVertex`).
- Always call `CheckLoop()` after completing a loop.
- Call `Complete()` to finalize.

## Polyhedron3DBuilder

Builds a polyhedron by defining vertices, edges, and faces explicitly. All faces are planar.

### Workflow

1. **Initialize** empty polyhedron and set type.
2. **Append vertices** using the builder.
3. **Define edges** as vertex-index pairs (`GeometryEdge`).
4. **Define faces** as ordered sequences of oriented edges (`OrientedEdge`).
5. **Complete** the builder.

### Example: Pyramid

```python
pyramid = AllplanGeo.Polyhedron3D()
pyramid.SetType(AllplanGeo.PolyhedronType.tVolume)

builder = AllplanGeo.Polyhedron3DBuilder(pyramid)
builder.AppendVertex(AllplanGeo.Point3D(-500, -500, 0))    # idx 0
builder.AppendVertex(AllplanGeo.Point3D( 500, -500, 0))    # idx 1
builder.AppendVertex(AllplanGeo.Point3D( 500,  500, 0))    # idx 2
builder.AppendVertex(AllplanGeo.Point3D(-500,  500, 0))    # idx 3
builder.AppendVertex(AllplanGeo.Point3D(   0,    0, 1000)) # idx 4

# Edges: index pairs
pyramid.AppendEdge(AllplanGeo.GeometryEdge(0, 1))  # edge 0
pyramid.AppendEdge(AllplanGeo.GeometryEdge(1, 2))  # edge 1
pyramid.AppendEdge(AllplanGeo.GeometryEdge(2, 3))  # edge 2
pyramid.AppendEdge(AllplanGeo.GeometryEdge(3, 0))  # edge 3
pyramid.AppendEdge(AllplanGeo.GeometryEdge(0, 4))  # edge 4
pyramid.AppendEdge(AllplanGeo.GeometryEdge(1, 4))  # edge 5
pyramid.AppendEdge(AllplanGeo.GeometryEdge(2, 4))  # edge 6
pyramid.AppendEdge(AllplanGeo.GeometryEdge(3, 4))  # edge 7

# Faces: ordered oriented edges
base = pyramid.CreateFace(4)  # 4 edges
base.AppendEdge(AllplanGeo.OrientedEdge(0, True))
base.AppendEdge(AllplanGeo.OrientedEdge(1, True))
base.AppendEdge(AllplanGeo.OrientedEdge(2, True))
base.AppendEdge(AllplanGeo.OrientedEdge(3, True))

face_1 = pyramid.CreateFace(3)
face_1.AppendEdge(4, True)
face_1.AppendEdge(5, False)
face_1.AppendEdge(0, False)

# ... remaining faces follow same pattern

builder.Complete()
```

### Key Rules

- `OrientedEdge(index, positive)`: `positive=True` means traverse edge in its defined direction. `False` = reverse.
- All faces must have consistent winding (all CW or all CCW when viewed from outside).
- `PolyhedronType.tVolume` for solids, other types exist for surfaces/edges.
