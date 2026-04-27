---
title: "YDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\YDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# YDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\YDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the y distance modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `math`

## Klassen

### `YDistance`

modify the y distance
    

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
""" implementation of the y distance modification
"""

import math

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class YDistance(BaseHandlePropUpdate):
    """ modify the y distance
    """

    def __call__(self):
        """ execute the value update
        """

        self.update_property_value(math.fabs(self._dist_pnt.Y) if self._is_abs_value else self._dist_pnt.Y)

```

</details>