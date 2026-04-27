---
title: "View2D"
source: "PythonPartsFramework\GeneralScripts\PythonPart\View2D.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# View2D

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPart\View2D.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the PythonPart

## Abhängigkeiten

- `NemAll_Python_BasisElements`
- `View`
- `__future__`

## Klassen

### `View2D`

Definition of a 2D view class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, elements: list[AllplanBasisEle.AllplanElement] | None=None, start_scale: float=0.0, end_scale: float=9999.0` | `None` | Initialization of 2D view class  Args:     elements:    elements. Defaults to None.     start_scale: start scale. Defaults to 0.     end_scale:   end scale. Defaults to 9999. |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart
"""
from __future__ import annotations

import NemAll_Python_BasisElements as AllplanBasisEle

from .View import View

class View2D(View):
    """ Definition of a 2D view class
    """

    def __init__(self,
                 elements    : (list[AllplanBasisEle.AllplanElement] | None) = None,
                 start_scale: float                                          = 0.,
                 end_scale   : float                                         = 9999.):
        """ Initialization of 2D view class

        Args:
            elements:    elements. Defaults to None.
            start_scale: start scale. Defaults to 0.
            end_scale:   end scale. Defaults to 9999.
        """

        super().__init__(AllplanBasisEle.MacroSlideType.eGeometry,
                         True, False, start_scale, end_scale, elements)

```

</details>