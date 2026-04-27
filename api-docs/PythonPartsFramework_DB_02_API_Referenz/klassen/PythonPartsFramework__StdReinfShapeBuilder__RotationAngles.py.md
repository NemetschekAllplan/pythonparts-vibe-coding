---
title: "RotationAngles"
source: "PythonPartsFramework\StdReinfShapeBuilder\RotationAngles.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# RotationAngles

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\RotationAngles.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`

## Übersicht

Implementation of the model angles class

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `__future__`

## Klassen

### `RotationAngles`

Class describing the rotation of a geometrical object around the three axes (X,Y,Z)
in order to transform it from local to global coordinate system or the other way around.

Often used in context of transforming a bending shape (rebar or mesh).

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, angle_x: float, angle_y: float, angle_z: float` | `None` | Construct the object by setting all three angles. The angles are given in degrees.  Args:     angle_x:    Rotation angle (degree) around the local x axis     angle_y:    Rotation angle (degree) around the local y axis     angle_z:    Rotation angle (degree) around the local z axis |
| `angle_x` | `self` | `float` | Rotation angle around the X axis (in degrees)          |
| `angle_y` | `self` | `float` | Rotation angle around the Y axis (in degrees)          |
| `angle_z` | `self` | `float` | Rotation angle around the Z axis (in degrees)          |
| `get_rotation_matrix` | `self` | `AllplanGeo.Matrix3D` | Get a 3D transformation matrix (4x4) describing the rotation around the origin (0,0,0).  Returns:     Transformation matrix describing the rotation |
| `change_rotation` | `self` | `RotationAngles` | Inverse rotation direction  Returns:     RotationAngles with the inverted rotation direction |
| `__repr__` | `self` | `str` | Create a string from the object data  Returns:     string with the object data |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""Implementation of the model angles class"""

from __future__ import annotations

import NemAll_Python_Geometry as AllplanGeo


class RotationAngles():
    """Class describing the rotation of a geometrical object around the three axes (X,Y,Z)
    in order to transform it from local to global coordinate system or the other way around.

    Often used in context of transforming a bending shape (rebar or mesh).
    """

    def __init__(self,
                 angle_x: float,
                 angle_y: float,
                 angle_z: float):
        """Construct the object by setting all three angles. The angles are given in degrees.

        Args:
            angle_x:    Rotation angle (degree) around the local x axis
            angle_y:    Rotation angle (degree) around the local y axis
            angle_z:    Rotation angle (degree) around the local z axis
        """

        self.prop_angle_x = angle_x
        self.prop_angle_y = angle_y
        self.prop_angle_z = angle_z

    @property
    def angle_x(self) -> float:
        """Rotation angle around the X axis (in degrees)
        """
        return self.prop_angle_x


    @property
    def angle_y(self) -> float:
        """Rotation angle around the Y axis (in degrees)
        """
        return self.prop_angle_y


    @property
    def angle_z(self) -> float:
        """Rotation angle around the Z axis (in degrees)
        """
        return self.prop_angle_z


    def get_rotation_matrix(self) -> AllplanGeo.Matrix3D:
        """Get a 3D transformation matrix (4x4) describing the rotation around the origin (0,0,0).

        Returns:
            Transformation matrix describing the rotation
        """
        rot_mat = AllplanGeo.Matrix3D()
        rot_angle = AllplanGeo.Angle()

        rot_angle.SetDeg(self.angle_x)

        rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(1000, 0, 0)), rot_angle)

        rot_angle.SetDeg(self.angle_y)

        rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(0, 1000, 0)), rot_angle)

        rot_angle.SetDeg(self.angle_z)

        rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(0, 0, 1000)), rot_angle)

        return rot_mat

    def change_rotation(self) -> RotationAngles:
        """Inverse rotation direction

        Returns:
            RotationAngles with the inverted rotation direction
        """

        return RotationAngles(-self.angle_x, -self.angle_y, -self.angle_z)

    def __repr__(self) -> str:
        """Create a string from the object data

        Returns:
            string with the object data
        """
        description =  '<%s>\n'\
            '   x-angle = %s\n'\
            '   y-angle = %s\n'\
            '   z-angle = %s\n'\
            % (self.__class__.__name__,
               self.angle_x,
               self.angle_y,
               self.angle_z)
        return description

```

</details>