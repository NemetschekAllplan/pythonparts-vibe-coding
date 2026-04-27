---
title: "PythonPartViewData"
source: "PythonPartsFramework\GeneralScripts\PythonPartViewData.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PythonPartViewData

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPartViewData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the data class for the view data 

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `dataclasses`

## Klassen

### `PythonPartViewData`

Data class with the properties of a PythonPart view 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the data class for the view data """

from dataclasses import dataclass

import NemAll_Python_BaseElements as AllplanBaseEle

@dataclass
class PythonPartViewData():
    """ Data class with the properties of a PythonPart view """

    visible_in_2d     : bool = True
    """Whether the view should be visible in the ground view"""
    visible_in_3d     : bool = True
    """Whether the view should be visible in the isometric view"""
    start_scale       : float = 0
    """The scale, from which the view is displayed (scale range's lower limit)"""
    end_scale         : float = 9999
    """The scale, to which the view is displayed (scale range's upper limit)"""
    ref_pnt1_x        : float = 0
    """X coordinate of the first resizing point"""
    ref_pnt1_y        : float = 0
    """Y coordinate of the first resizing point"""
    ref_pnt1_z        : float = 0
    """Z coordinate of the first resizing point"""
    ref_pnt2_x        : float = 0
    """X coordinate of the second resizing point"""
    ref_pnt2_y        : float = 0
    """Y coordinate of the second resizing point"""
    ref_pnt2_z        : float = 0
    """Z coordinate of the second resizing point"""
    visibility_layer_a: bool = True
    """Whether the view should be visible on layer A"""
    visibility_layer_b: bool = True
    """Whether the view should be visible on layer B"""
    visibility_layer_c: bool = True
    """Whether the view should be visible on layer C"""
    scale_x           : int = 1
    """Direction, in which the view should be resized, when the whole PythonPart is resized
    in the X direction.

    -   1 - in X direction;
    -   2 - in Y direction;
    -   3 - in Z direction
    """
    scale_y           : int = 2
    """Direction, in which the view should be resized, when the whole PythonPart is resized
    in the Y direction.

    -   1 - in X direction;
    -   2 - in Y direction;
    -   3 - in Z direction
    """
    scale_z           : int = 3
    """Direction, in which the view should be resized, when the whole PythonPart is resized
    in the Y direction.

    -   1 - in X direction;
    -   2 - in Y direction;
    -   3 - in Z direction
    """
    all_drawing_types : bool = True
    """ add drawing type state """

    drawing_types : list[int | AllplanBaseEle.DrawingTypeService.DefaultDrawingTypes] | None = None

```

</details>