---
title: "TransformationStack3D"
source: "PythonPartsFramework\SmartPartUtils\TransformationStack3D.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TransformationStack3D

> **Pfad:** `PythonPartsFramework\SmartPartUtils\TransformationStack3D.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the transformation stack for 3D transformations 

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `typing`

## Klassen

### `TransformationStack3D`

implementation of the transformation stack for 3D transformations 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, length_unit: int` | `None` | initialize  |
| `translate` | `self, delta_x: float, delta_y: float, delta_z: float` | `None` | add a translation to the stack  |
| `translate_x` | `self, delta_x: float` | `None` | add a x translation to the stack  |
| `translate_y` | `self, delta_y: float` | `None` | add a y translation to the stack  |
| `translate_z` | `self, delta_z: float` | `None` | add a z translation to the stack  |
| `rotate_x` | `self, angle: float` | `None` | add a rotation around the x axis to the stack  |
| `rotate_y` | `self, angle: float` | `None` | add a rotation around the y axis to the stack  |
| `rotate_z` | `self, angle: float` | `None` | add a rotation around the z axis to the stack  |
| `rotate` | `self, angle: float` | `None` | add a rotation to the stack  |
| `scale` | `self, x_fac: float, y_fac: float, z_fac: float` | `None` | add a rotation to the stack  |
| `restore` | `self, count: int` | `None` | restore a transformation  |
| `restore_all` | `self` | `None` | restore all transformations  |
| `get_matrix` | `self` | `None` | get the current transformation matrix  |
| `transform` | `self, geo_ele: Any` | `None` | transform a geometry element with the current transformation matrix  |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the transformation stack for 3D transformations """

from typing import List, Tuple, Any

import NemAll_Python_Geometry as AllplanGeo

class TransformationStack3D():
    """ implementation of the transformation stack for 3D transformations """

    def __init__(self,
                 length_unit: int):
        """ initialize """

        self.trans_stack : List[Tuple[int, Tuple[float, ...]]] = []

        self.length_fac = [1., 10., 100., 1000.][length_unit]


    def translate(self,
                  delta_x: float,
                  delta_y: float,
                  delta_z: float):
        """ add a translation to the stack """

        self.trans_stack.append((1, (delta_x * self.length_fac, delta_y * self.length_fac, delta_z * self.length_fac)))


    def translate_x(self,
                    delta_x: float):
        """ add a x translation to the stack """

        self.trans_stack.append((1, (delta_x * self.length_fac, 0, 0)))


    def translate_y(self,
                    delta_y: float):
        """ add a y translation to the stack """

        self.trans_stack.append((1, (0, delta_y * self.length_fac, 0)))


    def translate_z(self,
                    delta_z: float):
        """ add a z translation to the stack """

        self.trans_stack.append((1, (0, 0, delta_z * self.length_fac)))


    def rotate_x(self,
                 angle: float):
        """ add a rotation around the x axis to the stack """

        self.trans_stack.append((21, (angle,)))


    def rotate_y(self,
                 angle: float):
        """ add a rotation around the y axis to the stack """

        self.trans_stack.append((22, (angle,)))


    def rotate_z(self,
                 angle: float):
        """ add a rotation around the z axis to the stack """

        self.trans_stack.append((23, (angle,)))


    def rotate(self,
               angle: float):
        """ add a rotation to the stack """

        self.trans_stack.append((2, (angle,)))


    def scale(self,
              x_fac: float,
              y_fac: float,
              z_fac: float):
        """ add a rotation to the stack """

        self.trans_stack.append((3, (x_fac, y_fac, z_fac)))


    def restore(self, count: int):
        """ restore a transformation """

        self.trans_stack = self.trans_stack[:-count]


    def restore_all(self):
        """ restore all transformations """

        self.trans_stack.clear()


    def get_matrix(self):
        """ get the current transformation matrix """

        if not self.trans_stack:
            return AllplanGeo.Matrix3D()

        mat = AllplanGeo.Matrix3D()

        ref_pnt = AllplanGeo.Vector3D()
        x_scale = 1
        y_scale = 1
        z_scale = 1

        axis_placement = AllplanGeo.AxisPlacement3D()

        for trans_type, data in self.trans_stack:
            if trans_type == 1:
                ref_pnt += AllplanGeo.Transform(AllplanGeo.Vector3D(data[0], data[1], data[2]), mat)

            elif trans_type > 20:
                angle = AllplanGeo.Angle()
                angle.Deg = data[0]

                if trans_type == 21:
                    line = AllplanGeo.Line3D(0, 0, 0, 1000, 0, 0)

                elif trans_type == 22:
                    line = AllplanGeo.Line3D(0, 0, 0, 0, 1000, 0)

                else:
                    line = AllplanGeo.Line3D(0, 0, 0, 0, 0, 1000)

                line = AllplanGeo.Transform(line, mat)

                mat.Rotation(line, angle)

            else:
                x_scale *= data[0]
                y_scale *= data[1]
                z_scale *= data[2]

        mat.Scaling(x_scale, y_scale, z_scale)

        mat.Translate(ref_pnt)

        return mat


    def transform(self, geo_ele: Any):
        """ transform a geometry element with the current transformation matrix """

        return AllplanGeo.Transform(geo_ele, self.get_matrix())
```

</details>