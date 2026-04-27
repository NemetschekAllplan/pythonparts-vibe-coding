---
title: "ConeUtil"
source: "PythonPartsFramework\Utils\Geometry\ConeUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ConeUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\ConeUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of ConeUtil class

- create a Cone

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `ConeUtil`

implementation of ConeUtil class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create` | `height: float, radius_major: float, radius_minor: float, bottom_surface_angle: float, top_surface_angle: float` | `AllplanGeo.BRep3D | None` | create a Cone  Args:     height:               height     radius_major:         major radius     radius_minor:         minor radius     bottom_surface_angle: bottom surface angle     top_surface_angle:    top surface angle  Returns:     create Cone or None if invalid parameters |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of ConeUtil class

    - create a Cone
"""

# pylint: disable=magic-value-comparison

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class ConeUtil():
    """ implementation of ConeUtil class
    """

    @staticmethod
    def create(height              : float,
               radius_major        : float,
               radius_minor        : float,
               bottom_surface_angle: float,
               top_surface_angle   : float) -> (AllplanGeo.BRep3D | None):
        """ create a Cone

        Args:
            height:               height
            radius_major:         major radius
            radius_minor:         minor radius
            bottom_surface_angle: bottom surface angle
            top_surface_angle:    top surface angle

        Returns:
            create Cone or None if invalid parameters
        """

        if radius_major <= 0 or radius_minor <= 0:
            return None

        assert bottom_surface_angle == 90, "bottom_surface_angle must be 90 degrees"
        assert top_surface_angle    == 90, "top_surface_angle must be 90 degrees"

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        cone = AllplanGeo.Cone3D(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(0, 0, 0),
                                                            AllplanGeo.Vector3D(abs(height), 0, 0), AllplanGeo.Vector3D(0, 0, height)),
                                 radius_major * length_fac, radius_minor * length_fac,
                                 AllplanGeo.Point3D(0, 0, abs(height) * length_fac))

        if not cone.IsValid():
            return None

        brep = AllplanGeo.BRep3D.CreateCone(cone)

        return brep if brep.IsValid() else None

```

</details>