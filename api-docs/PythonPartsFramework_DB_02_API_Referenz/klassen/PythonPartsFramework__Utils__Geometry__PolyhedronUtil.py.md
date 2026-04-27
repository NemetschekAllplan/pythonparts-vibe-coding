---
title: "PolyhedronUtil"
source: "PythonPartsFramework\Utils\Geometry\PolyhedronUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PolyhedronUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\PolyhedronUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of PolyhedronUtil class

- create box polyhedron

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `PolyhedronUtil`

Utility class for polyhedron operations.
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_box` | `length: float, width: float, height: float` | `AllplanGeo.Polyhedron3D` | Create a box polyhedron with given dimensions.  Args:     length: length of the box     width:  width of the box     height: height of the box  Returns:     polyhedron representing the box |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of PolyhedronUtil class

    - create box polyhedron
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class PolyhedronUtil:
    """ Utility class for polyhedron operations.
    """

    @staticmethod
    def create_box(length: float,
                   width : float,
                   height: float) -> AllplanGeo.Polyhedron3D:
        """ Create a box polyhedron with given dimensions.

        Args:
            length: length of the box
            width:  width of the box
            height: height of the box

        Returns:
            polyhedron representing the box
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        length *= length_fac
        width  *= length_fac
        height *= length_fac

        x_left = 0 if length > 0 else length
        y_left = 0 if width  > 0 else width
        z_left = 0 if height > 0 else height

        return AllplanGeo.Polyhedron3D.CreateCuboid(AllplanGeo.Point3D(x_left, y_left, z_left),
                                                    AllplanGeo.Point3D(x_left + abs(length),
                                                                       y_left + abs(width),
                                                                       z_left + abs(height)))

```

</details>