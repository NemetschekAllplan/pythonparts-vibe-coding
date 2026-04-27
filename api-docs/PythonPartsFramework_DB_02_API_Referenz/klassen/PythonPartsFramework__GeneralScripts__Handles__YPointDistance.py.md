---
title: "YPointDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\YPointDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# YPointDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\YPointDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the y coordinate modification

## Abhängigkeiten

- `BaseHandlePointUpdate`
- `NemAll_Python_Geometry`

## Klassen

### `YPointDistance`

modify the y coordinate
    

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
""" implementation of the y coordinate modification
"""

import NemAll_Python_Geometry as AllplanGeo

from .BaseHandlePointUpdate import BaseHandlePointUpdate

class YPointDistance(BaseHandlePointUpdate):
    """ modify the y coordinate
    """

    def __call__(self):
        """ execute the coordinate update
        """

        geo_ele = self._param_data.geo_element

        if isinstance(geo_ele, (AllplanGeo.Point2D, AllplanGeo.Point3D)):
            geo_ele.Y = self._handle_prop.ref_point.Y + self.value

        elif isinstance(geo_ele, AllplanGeo.Line2D):
            geo_ele.EndPoint = AllplanGeo.Point2D(geo_ele.EndPoint.X,
                                                  self._handle_prop.ref_point.Y + self.value)

        elif isinstance(geo_ele, AllplanGeo.Line3D):
            geo_ele.EndPoint = AllplanGeo.Point3D(geo_ele.EndPoint.X,
                                                  self._handle_prop.ref_point.Y + self.value,
                                                  geo_ele.EndPoint.Z)

```

</details>