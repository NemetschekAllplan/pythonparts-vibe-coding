---
title: "Arc3DUtil"
source: "PythonPartsFramework\Utils\Geometry\Arc3DUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Arc3DUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\Arc3DUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of Arc3DUtil

- create a 3d arc

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `Arc3DUtil`

implementation of Arc3DUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create` | `x_center: float, y_center: float, radius: float, angle_start: float=0.0, angle_end: float=360.0` | `AllplanGeo.Arc3D | None` | create a 3d arc  Args:     x_center:    x coord center     y_center:    y coord center     radius:      radius     angle_start: start angle     angle_end:   end angle  Returns:     returns created arc or None if start and end angle are equal |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of Arc3DUtil

    - create a 3d arc
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class Arc3DUtil:
    """ implementation of Arc3DUtil
    """

    @staticmethod
    def create(x_center   : float,
               y_center   : float,
               radius     : float,
               angle_start: float = 0.,
               angle_end  : float = 360.) -> (AllplanGeo.Arc3D | None):
        """ create a 3d arc

        Args:
            x_center:    x coord center
            y_center:    y coord center
            radius:      radius
            angle_start: start angle
            angle_end:   end angle

        Returns:
            returns created arc or None if start and end angle are equal
        """

        if angle_start == angle_end:
            return None

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        radius = radius * length_fac

        return AllplanGeo.Arc3D(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x_center * length_fac, y_center * length_fac, 0)),
                                radius, radius,
                                AllplanGeo.Angle.DegToRad(angle_start),
                                AllplanGeo.Angle.DegToRad(angle_end), True)

```

</details>