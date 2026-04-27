---
title: "Angle"
source: "PythonPartsFramework\GeneralScripts\Handles\Angle.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# Angle

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\Angle.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the angle modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `NemAll_Python_Geometry`

## Klassen

### `Angle`

modify the angle
    

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
""" implementation of the angle modification
"""

import NemAll_Python_Geometry as AllplanGeo

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class Angle(BaseHandlePropUpdate):
    """ modify the angle
    """

    def __call__(self):
        """ execute the value update
        """

        if self._handle_prop.angle_placement:
            trans_mat = self._handle_prop.angle_placement.GetTransformationMatrix()
            trans_mat.Reverse()

            self.update_property_value(AllplanGeo.CalcAngle(
                                            AllplanGeo.Point2D(AllplanGeo.Transform(self._handle_prop.ref_point, trans_mat)),
                                            AllplanGeo.Point2D(AllplanGeo.Transform(self._local_input_pnt, trans_mat))).Deg)

        else:
            self.update_property_value(AllplanGeo.CalcAngle(AllplanGeo.Point2D(), AllplanGeo.Point2D(self._dist_pnt)).Deg)

```

</details>