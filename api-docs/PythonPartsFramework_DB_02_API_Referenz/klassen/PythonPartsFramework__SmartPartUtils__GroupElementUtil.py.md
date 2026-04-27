---
title: "GroupElementUtil"
source: "PythonPartsFramework\SmartPartUtils\GroupElementUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GroupElementUtil

> **Pfad:** `PythonPartsFramework\SmartPartUtils\GroupElementUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the group element utility 

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `SmartPartUtils.TransformationStack3D`
- `typing`

## Klassen

### `GroupElementUtil`

implementation of the group element utility 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, length_unit: int` | `None` | initialize  |
| `add_group` | `self, name: str` | `None` | add a foil  |
| `add_line3d` | `self, x_start: float, y_start: float, z_start: float, x_end: float, y_end: float, z_end: float` | `None` | add a 2d line  |
| `add_box` | `self, length: float, width: float, height: float` | `None` | add a box  |
| `add_prism` | `self, height: float, polygon: AllplanGeo.Polygon2D` | `None` | add a prism  |
| `get_trans_stack` | `self` | `TransformationStack3D` | get the transformation stack  |
| `union` | `self, polyheds1: Any, polyheds2: Any` | `None` | create a union from two groups  |
| `diff` | `self, polyhed1: Any, polyhed2: Any` | `None` | create a diff from two groups  |
| `get_group_elements` | `self, name: str` | `List[Any]` | get the group elements  |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the group element utility """

from typing import Any, List

import NemAll_Python_Geometry as AllplanGeo

from SmartPartUtils.TransformationStack3D import TransformationStack3D

class GroupElementUtil():
    """ implementation of the group element utility """

    def __init__(self,
                 length_unit: int):
        """ initialize """

        self.trans_stack_3d = TransformationStack3D(length_unit)
        self.length_fac     = [1., 10., 100., 1000.][length_unit]
        self.group_ele_list = {}
        self.model_ele_list = Any


    def add_group(self, name: str):
        """ add a foil """

        self.group_ele_list[name] = []
        self.model_ele_list       = self.group_ele_list[name]

        self.trans_stack_3d.restore_all()


    def add_line3d(self,
                   x_start: float,
                   y_start: float,
                   z_start: float,
                   x_end  : float,
                   y_end  : float,
                   z_end  : float):
        """ add a 2d line """

        line = AllplanGeo.Line3D(x_start * self.length_fac, y_start * self.length_fac, z_start * self.length_fac,
                                 x_end * self.length_fac, y_end * self.length_fac, z_end * self.length_fac)

        mat = self.trans_stack_3d.get_matrix()

        self.model_ele_list.append(AllplanGeo.Transform(line, mat))


    def add_box(self,
                length: float,
                width : float,
                height: float):
        """ add a box """

        box = AllplanGeo.Polyhedron3D.CreateCuboid(length * self.length_fac, width * self.length_fac, height * self.length_fac)

        mat = self.trans_stack_3d.get_matrix()

        self.model_ele_list.append(AllplanGeo.Transform(box, mat))


    def add_prism(self,
                  height: float,
                  polygon: AllplanGeo.Polygon2D):
        """ add a prism """

        ref_pnt = polygon[0]

        path = AllplanGeo.Polyline3D()
        path += AllplanGeo.Point3D(ref_pnt)
        path += AllplanGeo.Point3D(ref_pnt.X, ref_pnt.Y, height * self.length_fac)

        scale_mat = AllplanGeo.Matrix2D()
        scale_mat.Scaling(self.length_fac, self.length_fac)

        polygon = AllplanGeo.Transform(polygon, scale_mat)

        _, polyhed = AllplanGeo.CreatePolyhedron(polygon, ref_pnt, path)

        mat = self.trans_stack_3d.get_matrix()

        self.model_ele_list.append(AllplanGeo.Transform(polyhed, mat))


    def get_trans_stack(self) -> TransformationStack3D:
        """ get the transformation stack """

        return self.trans_stack_3d


    def union(self,
              polyheds1: Any,
              polyheds2: Any):
        """ create a union from two groups """

        if isinstance(polyheds1, str):
            polyheds = self.group_ele_list[polyheds1]

        elif not isinstance(polyheds1, list):
            polyheds = [polyheds1]

        else:
            polyheds = polyheds1

        if isinstance(polyheds2, str):
            if polyheds2:
                polyheds += self.group_ele_list[polyheds2]

        elif isinstance(polyheds2, list):
            polyheds += polyheds2

        else:
            polyheds.append(polyheds2)

        union = polyheds[0]

        for polyhed in polyheds[1:]:
            err, union = AllplanGeo.MakeUnion(union, polyhed)

            if err:
                print("Union is not possible")
                break

        return union


    def diff(self,
             polyhed1: Any,
             polyhed2: Any):
        """ create a diff from two groups """

        diff = self.union(polyhed1, "")

        if isinstance(polyhed2, str):
            polyhed2 = self.group_ele_list[polyhed2]

        elif not isinstance(polyhed2, list):
            polyhed2 = [polyhed2]

        for polyhed in polyhed2:
            err, diff = AllplanGeo.MakeSubtraction(diff, polyhed)

            if err:
                print("Diff is not possible")
                break

        return diff


    def get_group_elements(self, name: str) -> List[Any]:
        """ get the group elements """

        return self.group_ele_list[name]

```

</details>