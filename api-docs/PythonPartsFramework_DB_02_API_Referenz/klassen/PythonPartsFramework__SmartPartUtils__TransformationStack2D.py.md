---
title: "TransformationStack2D"
source: "PythonPartsFramework\SmartPartUtils\TransformationStack2D.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TransformationStack2D

> **Pfad:** `PythonPartsFramework\SmartPartUtils\TransformationStack2D.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the transformation stack for 2D transformations 

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `typing`

## Klassen

### `TransformationStack2D`

implementation of the transformation stack for 2D transformations 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, length_unit: int` | `None` | initialize  |
| `translate` | `self, delta_x: float, delta_y: float` | `None` | add a translation to the stack  |
| `rotate` | `self, angle: float` | `None` | add a rotation to the stack  |
| `scale` | `self, x_fac: float, y_fac: float` | `None` | add a rotation to the stack  |
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
""" implementation of the transformation stack for 2D transformations """

from typing import List, Tuple, Any

import NemAll_Python_Geometry as AllplanGeo

class TransformationStack2D():
    """ implementation of the transformation stack for 2D transformations """

    def __init__(self,
                 length_unit: int):
        """ initialize """

        self.trans_stack : List[Tuple[int, Tuple[float, ...]]] = []

        self.length_fac = [1., 10., 100., 1000.][length_unit]


    def translate(self,
                  delta_x: float,
                  delta_y: float):
        """ add a translation to the stack """

        self.trans_stack.append((1, (delta_x * self.length_fac, delta_y * self.length_fac)))


    def rotate(self,
               angle: float):
        """ add a rotation to the stack """

        self.trans_stack.append((2, (angle,)))


    def scale(self,
              x_fac: float,
              y_fac: float):
        """ add a rotation to the stack """

        self.trans_stack.append((3, (x_fac, y_fac)))


    def restore(self, count: int):
        """ restore a transformation """

        self.trans_stack = self.trans_stack[:-count]


    def restore_all(self):
        """ restore all transformations """

        self.trans_stack.clear()


    def get_matrix(self):
        """ get the current transformation matrix """

        if not self.trans_stack:
            return AllplanGeo.Matrix2D()

        mat = AllplanGeo.Matrix2D()

        ref_pnt = AllplanGeo.Vector2D()
        x_scale = 1
        y_scale = 1

        for trans_type, data in self.trans_stack:
            if trans_type == 1:
                ref_pnt += AllplanGeo.Transform(AllplanGeo.Vector2D(data[0], data[1]), mat)

            elif trans_type == 2:
                angle = AllplanGeo.Angle()
                angle.Deg = data[0]

                mat.Rotation(AllplanGeo.Point2D(), angle)

            else:
                x_scale *= data[0]
                y_scale *= data[1]

        mat.Scaling(x_scale, y_scale)

        mat.Translate(ref_pnt)

        return mat


    def transform(self, geo_ele: Any):
        """ transform a geometry element with the current transformation matrix """

        return AllplanGeo.Transform(geo_ele, self.get_matrix())
```

</details>