---
title: "PointDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\PointDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# PointDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\PointDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the x distance modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `NemAll_Python_Geometry`
- `math`

## Klassen

### `PointDistance`

modify the point distance
    

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
""" implementation of the x distance modification
"""

import math

import NemAll_Python_Geometry as AllplanGeo

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class PointDistance(BaseHandlePropUpdate):
    """ modify the point distance
    """

    def __call__(self):
        """ execute the value update
        """

        self.update_property_value(math.fabs(self._dist_pnt.GetDistance(AllplanGeo.Point3D())))

```

</details>