---
title: "CylinderUtil"
source: "PythonPartsFramework\Utils\Geometry\CylinderUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# CylinderUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\CylinderUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of CylinderUtil class

- create a cylinder

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `CylinderUtil`

implementation of CylinderUtil class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `by_radius` | `height: float, radius: float` | `AllplanGeo.BRep3D | None` | create a cylinder  Args:     height: height     radius: radius  Returns:     create cylinder or None if invalid parameters |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of CylinderUtil class

    - create a cylinder
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class CylinderUtil():
    """ implementation of CylinderUtil class
    """

    @staticmethod
    def by_radius(height: float,
                  radius: float) -> (AllplanGeo.BRep3D | None):
        """ create a cylinder

        Args:
            height: height
            radius: radius

        Returns:
            create cylinder or None if invalid parameters
        """

        if radius <= 0:
            return None

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        cylinder = AllplanGeo.BRep3D.CreateCylinder(AllplanGeo.AxisPlacement3D(),
                                                    radius * length_fac,
                                                    abs(height) * length_fac)

        if height < 0:
            cylinder = AllplanGeo.Move(cylinder, AllplanGeo.Vector3D(0, 0, height * length_fac))

        return cylinder if cylinder.IsValid() else None

```

</details>