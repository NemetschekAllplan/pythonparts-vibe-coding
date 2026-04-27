---
title: "BarShapePointDataList"
source: "PythonPartsFramework\StdReinfShapeBuilder\BarShapePointDataList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# BarShapePointDataList

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\BarShapePointDataList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`

## Übersicht

implementation of the list for the bar shape point data

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `typing`

## Klassen

### `BarShapePointDataList`

the rows can have the following tuple entries

(point: AllplanGeo.Point2D as geometry point,
 cover: float as concrete cover of the side before the point,
 bending_roller: float as optional bending roller at the side end,
 z_coord_bar: float as optional bar coordinate in z direction of the local shape coordinate system)

or

(point: AllplanGeo.Point3D as geometry point,
 cover: float as concrete cover of the side before the point,
 bending_roller: float as optional bending roller at the side end)

or

 cover: float as concrete cover at the end of the shape

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the list for the bar shape point data
"""

from typing import List, Union, Tuple

import NemAll_Python_Geometry as AllplanGeo

class BarShapePointDataList(List[Union[Tuple[AllplanGeo.Point2D, float],
                                       Tuple[AllplanGeo.Point2D, float, float],
                                       Tuple[AllplanGeo.Point2D, float, float, float],
                                       Tuple[AllplanGeo.Point3D, float],
                                       Tuple[AllplanGeo.Point3D, float, float],
                                       float]]):
    """ the rows can have the following tuple entries

        (point: AllplanGeo.Point2D as geometry point,
         cover: float as concrete cover of the side before the point,
         bending_roller: float as optional bending roller at the side end,
         z_coord_bar: float as optional bar coordinate in z direction of the local shape coordinate system)\n
        or\n
        (point: AllplanGeo.Point3D as geometry point,
         cover: float as concrete cover of the side before the point,
         bending_roller: float as optional bending roller at the side end)\n
        or\n
         cover: float as concrete cover at the end of the shape
        """

```

</details>