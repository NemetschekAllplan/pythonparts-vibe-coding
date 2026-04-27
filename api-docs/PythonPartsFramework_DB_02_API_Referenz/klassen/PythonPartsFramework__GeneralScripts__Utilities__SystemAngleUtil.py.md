---
title: "SystemAngleUtil"
source: "PythonPartsFramework\GeneralScripts\Utilities\SystemAngleUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# SystemAngleUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\Utilities\SystemAngleUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the system angle utilities

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `SystemAngleUtil`

implementation of the system angle utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `execute_rotation` | `placement_mat: AllplanGeo.Matrix3D` | `AllplanGeo.Matrix3D` | execute the rotation by the system angle  Args:     placement_mat: placement matrix  Returns:     matrix with the included system angle rotation |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the system angle utilities
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class SystemAngleUtil():
    """ implementation of the system angle utilities
    """

    @staticmethod
    def execute_rotation(placement_mat: AllplanGeo.Matrix3D) -> AllplanGeo.Matrix3D:
        """ execute the rotation by the system angle

        Args:
            placement_mat: placement matrix

        Returns:
            matrix with the included system angle rotation
        """

        system_angle_mat = AllplanGeo.Matrix3D()
        system_angle_mat.SetRotation(AllplanGeo.Line3D(0, 0, 0, 0, 0, 1000),
                                    AllplanGeo.Angle(AllplanSettings.InputAngleSettings.GetSystemAngle()))

        return system_angle_mat * placement_mat

```

</details>