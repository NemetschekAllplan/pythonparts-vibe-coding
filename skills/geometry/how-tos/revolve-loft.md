---
name: geometry-revolve-loft
description: How to create solids by revolving a profile around an axis or lofting between multiple profiles.
---

## Revolve (CreateRevolvedBRep3D)

Creates a solid by revolving a profile around an axis. Result is always `BRep3D`.

Rules:
- Profile curves must form a closed shape (otherwise creates a surface).
- Axis must not intersect the profile (causes self-intersection).
- All profile shapes must be planar.

```python
# Define profile as a list of curves forming a closed shape
profile_curves = []

spline = AllplanGeo.Spline3D()
spline += AllplanGeo.Point3D(200, 0, 0)
spline += AllplanGeo.Point3D(400, 0, 300)
spline += AllplanGeo.Point3D(300, 0, 600)
spline += AllplanGeo.Point3D(500, 0, 900)
profile_curves.append(spline)

# Close the profile with a line
profile_curves.append(AllplanGeo.Line3D(spline.EndPoint, spline.StartPoint))

# Define rotation axis
axis = AllplanGeo.Axis3D(AllplanGeo.Point3D(), AllplanGeo.Vector3D(0, 0, 1))

err, revolved = AllplanGeo.CreateRevolvedBRep3D(
    profiles_object = profile_curves,
    axis            = axis,
    rotationAngle   = AllplanGeo.Angle(),  # 0 = full 360°
    closecaps       = True,                # True = closed solid
    numprofiles     = 0)                   # must be 0 for full rotation
```

Key parameters:
- `rotationAngle`: Set to `AllplanGeo.Angle()` (= 0) for full 360°. Non-zero = partial revolution.
- `closecaps`: `True` creates caps at start/end of partial revolution.
- `numprofiles`: Must be 0 for full rotation. For partial, controls intermediate profile count.

## Loft (CreateLoftedBRep3D)

Creates a solid by joining two or more planar profiles. Result is always `BRep3D`.

Rules:
- All profiles must be planar.
- Profiles must be closed for a solid (open = surface).
- Must not self-intersect or create twisted surfaces.

> **Warning:** No rails are defined — lofting connects profiles point-by-point (first point of profile 1 to first point of profile 2). Misaligned start points cause twisted geometry.

```python
err, lofted = AllplanGeo.CreateLoftedBRep3D(
    outerProfiles_object = profiles,     # list of closed, planar curves
    innerProfiles_object = [],           # optional: inner profiles for hollow shapes
    closecaps            = True,         # cap the ends
    createprofileedges   = False,        # create edges at profile locations
    linear               = False,        # False = smooth interpolation between profiles
    periodic             = False)        # True = connect last profile back to first (ring)
```

Key parameters:
- `innerProfiles_object`: Define openings/hollows by adding inner profile outlines.
- `linear`: `True` = straight connections. `False` = smooth B-spline transitions.
- `periodic`: `True` = closed ring (first profile = last). Note: periodic lofts produce a surface, not a solid.
