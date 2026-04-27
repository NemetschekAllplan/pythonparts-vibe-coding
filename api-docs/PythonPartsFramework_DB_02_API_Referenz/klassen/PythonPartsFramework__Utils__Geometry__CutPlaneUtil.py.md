---
title: "CutPlaneUtil"
source: "PythonPartsFramework\Utils\Geometry\CutPlaneUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# CutPlaneUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\CutPlaneUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the cut plane util

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `TypeCollections.ModelEleList`
- `__future__`
- `math`
- `typing`

## Klassen

### `CutPlaneUtil`

implementation of the cut plane util
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `add_rotated_cut_plane` | `self, angle: float, plane_location: int, trans_matrix: AllplanGeo.Matrix3D` | `None` | add a rotated cut plane  Args:     angle:          roation angle in degrees     plane_location: location of the plane: 0 = XY     trans_matrix:   current transformation matrix |
| `cut_end` | `self` | `None` | clear the cut geometry          |
| `add_geometry` | `self, model_ele_list: ModelEleList, geo_ele: Any` | `None` | create a geometry object  Args:     model_ele_list: model element list     geo_ele:        geometry object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the cut plane util
"""

from __future__ import annotations

from typing import Any

import math

import NemAll_Python_Geometry as AllplanGeo

from TypeCollections.ModelEleList import ModelEleList

class CutPlaneUtil():
    """ implementation of the cut plane util
    """

    def __init__(self):
        """ initialize
        """

        self.cut_volumes: list[AllplanGeo.Polyhedron3D]         = []
        self.cut_planes : list[tuple[AllplanGeo.Plane3D, bool]] = []            # plane, cut_above


    def add_rotated_cut_plane(self,
                              angle         : float,
                              plane_location: int,
                              trans_matrix  : AllplanGeo.Matrix3D):
        """ add a rotated cut plane

        Args:
            angle:          roation angle in degrees
            plane_location: location of the plane: 0 = XY
            trans_matrix:   current transformation matrix
        """

        angle = math.radians(angle)

        match plane_location:
            case 0:
                plane = AllplanGeo.Plane3D(AllplanGeo.Point3D(0, 0, 0),
                                           AllplanGeo.Vector3D(0, math.sin(angle), math.cos(angle)))

                self.cut_planes.append((AllplanGeo.Transform(plane, trans_matrix), True))

            case _:
                assert False, f"unknown plane location {plane_location} for cut plane"


    def cut_end(self):
        """ clear the cut geometry
        """

        self.cut_planes.pop()


    def add_geometry(self,
                     model_ele_list: ModelEleList,
                     geo_ele       : Any):
        """ create a geometry object

        Args:
            model_ele_list: model element list
            geo_ele:        geometry object
        """

        if geo_ele is None:
            return

        if not self.cut_planes and not self.cut_volumes:
            model_ele_list.append_geometry_3d(geo_ele)

            return


        #----------------- cut the element

        geo_ele = model_ele_list.trans_stack.transform(geo_ele)

        for cut_volume in self.cut_volumes:
            result, cut_ele = AllplanGeo.MakeSubtraction(geo_ele, cut_volume)

            if result == AllplanGeo.eGeometryErrorCode.eOK:
                geo_ele = cut_ele

        for cut_plane, cut_above in self.cut_planes:
            if isinstance(geo_ele, AllplanGeo.BRep3D):
                result, above, below = AllplanGeo.CutBrepWithPlane(geo_ele, cut_plane)
            else:
                result, above, below = AllplanGeo.CutPolyhedronWithPlane(geo_ele, cut_plane)

            if result:
                geo_ele = above if cut_above else below

            else:
                print()
                print("not possible to cut by plane !!!!!!!!!!!!!!!!!!!!!!")
                print()

        model_ele_list.append_geometry_3d(geo_ele, use_trans_matrix = False)

```

</details>