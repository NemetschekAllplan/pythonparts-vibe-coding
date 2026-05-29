---
name: geometry-sweep
description: How to create solids by sweeping profiles along a path or along rails.
---

## Sweep Along Path

Sweeps a planar profile along a curve. Constraints:
- Profile must be planar.
- Resulting solid must not self-intersect.
- Must not create twisted surfaces.

### As BRep (CreateSweptBRep3D)

Accepts any curve type for both profile and path. Profile need not be closed (open = surface).

```python
profile = AllplanGeo.Arc3D(center=AllplanGeo.Point3D(),
                           minor=100, major=100,
                           startAngle=0, deltaAngle=2 * math.pi)

path = AllplanGeo.Spline3D([
    AllplanGeo.Point3D(0, 0, 0),
    AllplanGeo.Point3D(-100, 0, 500),
    AllplanGeo.Point3D(0, 0, 900),
    AllplanGeo.Point3D(1000, 0, 1300)])

err, swept_brep = AllplanGeo.CreateSweptBRep3D(
    profiles_object = [profile],       # list — can sweep multiple profiles
    path_object     = path,
    closecaps       = True,            # False = open ends (surface only)
    railrotation    = AllplanGeo.SweepRotationType.Unlocked)  # preserve angle to path
```

### As Polyhedron (CreateSweptPolyhedron3D)

Limited to `Polyline3D` for both profile and path. Profile must be closed.

```python
profile = AllplanGeo.Polyline3D([
    AllplanGeo.Point3D(0, 0, 0),
    AllplanGeo.Point3D(100, 0, 0),
    AllplanGeo.Point3D(100, 100, 0),
    AllplanGeo.Point3D(0, 100, 0),
    AllplanGeo.Point3D(0, 0, 0)])

profiles = AllplanGeo.Polyline3DList()
profiles.append(profile)

path = AllplanGeo.Polyline3D([
    AllplanGeo.Point3D(0, 0, 0),
    AllplanGeo.Point3D(0, 0, 500),
    AllplanGeo.Point3D(200, 0, 1000)])

err, swept_poly = AllplanGeo.CreateSweptPolyhedron3D(
    profiles     = profiles,
    path         = path,
    closecaps    = True,
    railrotation = True,          # True = preserve angle to path
    rotAxis      = AllplanGeo.Vector3D())  # ignored when railrotation=True
```

When `railrotation=False`, the profile rotates around `rotAxis` instead (must be non-zero then).

## Rail Sweep (CreateRailSweptBRep3D)

Sweeps **two or more** profiles along **one or more** rails. Same constraints as path sweep.

```python
err, rail_swept = AllplanGeo.CreateRailSweptBRep3D(
    profiles_object = profiles,    # list of profile curves
    rails_object    = rails,       # list of rail curves connecting profiles
    closecaps       = True,
    uniformScaling  = True,        # scale profile uniformly to fit rails
    railrotation    = True)        # preserve angle between rail and profile
```

- Profiles can be different shapes (e.g., square at bottom, circle at top).
- Rails are curves connecting corresponding points across profiles (typically splines).
- Result is always a `BRep3D`.
