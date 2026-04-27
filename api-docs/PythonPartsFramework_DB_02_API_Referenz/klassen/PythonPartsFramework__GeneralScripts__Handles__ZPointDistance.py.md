---
title: "ZPointDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\ZPointDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# ZPointDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\ZPointDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the z coordinate modification

## Abhängigkeiten

- `BaseHandlePointUpdate`
- `NemAll_Python_Geometry`

## Klassen

### `ZPointDistance`

modify the z coordinate
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self` | `None` | execute the coordinate update          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the z coordinate modification
"""

import NemAll_Python_Geometry as AllplanGeo

from .BaseHandlePointUpdate import BaseHandlePointUpdate

class ZPointDistance(BaseHandlePointUpdate):
    """ modify the z coordinate
    """

    def __call__(self):
        """ execute the coordinate update
        """

        geo_ele = self._param_data.geo_element

        if isinstance(geo_ele, AllplanGeo.Point3D):
            geo_ele.Z = self._handle_prop.ref_point.Z + self.value

        elif isinstance(geo_ele, AllplanGeo.Line3D):
            geo_ele.EndPoint = AllplanGeo.Point3D(geo_ele.EndPoint.X, geo_ele.EndPoint.Y,
                                                  self._handle_prop.ref_point.Z + self.value)

```

</details>