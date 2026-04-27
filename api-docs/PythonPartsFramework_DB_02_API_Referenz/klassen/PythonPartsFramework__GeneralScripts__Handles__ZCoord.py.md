---
title: "ZCoord"
source: "PythonPartsFramework\GeneralScripts\Handles\ZCoord.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# ZCoord

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\ZCoord.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the z coordinate modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `NemAll_Python_Geometry`

## Klassen

### `ZCoord`

modify the z coordinate
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self` | `None` | execute the value update          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the z coordinate modification
"""

import NemAll_Python_Geometry as AllplanGeo

from .BaseHandlePropUpdate import BaseHandlePropUpdate

ZMIN_NAME = "ZMin"
ZMAX_NAME = "ZMax"

class ZCoord(BaseHandlePropUpdate):
    """ modify the z coordinate
    """

    def __call__(self):
        """ execute the value update
        """

        prop, _, name = self.get_property_data()

        if prop is None:
            return


        #----------------- update the min z coordinate

        if name == ZMIN_NAME:
            z_min, z_max = self.get_z_min_max()

            if z_min is None or z_max is None:
                return

            height = z_max.value - z_min.value

            new_height = AllplanGeo.Vector3D(self._dist_pnt).GetLength()

            z_min.value += height - new_height

            return


        #----------------- update the max z coordinate

        if name == ZMAX_NAME:
            z_min, z_max = self.get_z_min_max()

            if not z_min or not z_max:
                return

            height = z_max.value - z_min.value

            new_height = AllplanGeo.Vector3D(self._dist_pnt).GetLength()

            z_max.value += new_height - height

```

</details>