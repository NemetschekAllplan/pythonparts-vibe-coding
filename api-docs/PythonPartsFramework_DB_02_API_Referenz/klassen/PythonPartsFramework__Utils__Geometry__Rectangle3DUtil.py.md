---
title: "Rectangle3DUtil"
source: "PythonPartsFramework\Utils\Geometry\Rectangle3DUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Rectangle3DUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\Rectangle3DUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the 3D rectangle utility functions

- create a rectangle polygon by center point, rotation angle, width and thickness
- create a rectangle polygon by corner points

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `Rectangle2DUtil`

## Klassen

### `Rectangle3DUtil`

implementation of the 3D rectangle utility functions
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `polygon_by_sizes` | `width: float, thickness: float, rotation_angle: AllplanGeo.Angle, z_plane: float` | `AllplanGeo.Polygon3D` | create a rectangle polygon by width and thickness, located at origin  Args:     width:          width     thickness:      thickness     rotation_angle: rotation angle     z_plane:        z plane  Returns:     rectangle polygon |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the 3D rectangle utility functions

    - create a rectangle polygon by center point, rotation angle, width and thickness
    - create a rectangle polygon by corner points
"""

import NemAll_Python_Geometry as AllplanGeo

from .Rectangle2DUtil import Rectangle2DUtil

class Rectangle3DUtil():
    """ implementation of the 3D rectangle utility functions
    """

    @staticmethod
    def polygon_by_sizes(width         : float,
                         thickness     : float,
                         rotation_angle: AllplanGeo.Angle,
                         z_plane       : float) -> AllplanGeo.Polygon3D:
        """ create a rectangle polygon by width and thickness, located at origin

        Args:
            width:          width
            thickness:      thickness
            rotation_angle: rotation angle
            z_plane:        z plane

        Returns:
            rectangle polygon
        """

        return AllplanGeo.ConvertTo3D(Rectangle2DUtil.polygon_by_sizes(width, thickness, rotation_angle), z_plane)[1]

```

</details>