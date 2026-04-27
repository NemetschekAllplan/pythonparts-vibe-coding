---
title: "XPointDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\XPointDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# XPointDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\XPointDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the x coordinate modification

## Abhängigkeiten

- `BaseHandlePointUpdate`
- `NemAll_Python_Geometry`

## Klassen

### `XPointDistance`

modify the x coordinate
    

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
""" implementation of the x coordinate modification
"""

import NemAll_Python_Geometry as AllplanGeo

from .BaseHandlePointUpdate import BaseHandlePointUpdate

class XPointDistance(BaseHandlePointUpdate):
    """ modify the x coordinate
    """

    def __call__(self):
        """ execute the coordinate update
        """

        geo_ele = self._param_data.geo_element

        if isinstance(geo_ele, (AllplanGeo.Point2D, AllplanGeo.Point3D)):
            geo_ele.X = self._handle_prop.ref_point.X + self.value

        elif isinstance(geo_ele, AllplanGeo.Line2D):
            geo_ele.EndPoint = AllplanGeo.Point2D(self._handle_prop.ref_point.X + self.value,
                                                  geo_ele.EndPoint.Y)

        elif isinstance(geo_ele, AllplanGeo.Line3D):
            geo_ele.EndPoint = AllplanGeo.Point3D(self._handle_prop.ref_point.X + self.value,
                                                  geo_ele.EndPoint.Y, geo_ele.EndPoint.Z)

```

</details>