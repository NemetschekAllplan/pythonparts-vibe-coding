---
title: "VectorDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\VectorDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# VectorDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\VectorDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the vector distance modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `NemAll_Python_Geometry`

## Klassen

### `VectorDistance`

modify the value by a vector distance
    

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
""" implementation of the vector distance modification
"""

import NemAll_Python_Geometry as AllplanGeo

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class VectorDistance(BaseHandlePropUpdate):
    """ modify the value by a vector distance
    """

    def __call__(self):
        """ execute the value update
        """

        if (dir_vector := self._param_data.dir_vector) is None and \
           (dir_vector := self._handle_prop.dir_vector) is None:
            return

        dir_line = AllplanGeo.Line3D(self._handle_prop.ref_point, dir_vector)

        value = AllplanGeo.TransformCoord.PointLocal(dir_line, self._local_input_pnt).X

        self.update_property_value(value)

```

</details>