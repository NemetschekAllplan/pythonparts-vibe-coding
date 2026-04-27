---
title: "ZDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\ZDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# ZDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\ZDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the z distance modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `math`

## Klassen

### `ZDistance`

modify the z distance
    

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
""" implementation of the z distance modification
"""

import math

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class ZDistance(BaseHandlePropUpdate):
    """ modify the z distance
    """

    def __call__(self):
        """ execute the value update
        """

        self.update_property_value(math.fabs(self._dist_pnt.Z) if self._is_abs_value else self._dist_pnt.Z)

```

</details>