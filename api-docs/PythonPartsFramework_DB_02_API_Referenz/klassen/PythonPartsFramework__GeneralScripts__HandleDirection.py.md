---
title: "HandleDirection"
source: "PythonPartsFramework\GeneralScripts\HandleDirection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandleDirection

> **Pfad:** `PythonPartsFramework\GeneralScripts\HandleDirection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

Script for HandleDirection

## Abhängigkeiten

- `enum`

## Klassen

### `HandleDirection`

Class with the definition of the handle directions.

The handle direction is used to set the allowed input direction
for the move of the handle.

The special direction **CLICK** allows to used the handle as
button or checkbox.

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
"""
Script for HandleDirection
"""

# pylint: disable=invalid-name

from enum import IntEnum

class HandleDirection(IntEnum):
    """
    Class with the definition of the handle directions.

    The handle direction is used to set the allowed input direction
    for the move of the handle.

    The special direction **CLICK** allows to used the handle as
    button or checkbox.

    """

    x_dir      = 1
    """ deprecated, use X_DIR """

    y_dir      = 2
    """ deprecated, use Y_DIR """

    z_dir      = 3
    """ deprecated, use Z_DIR """

    xy_dir     = 4
    """ deprecated, use XY_DIR """

    xz_dir     = 5
    """ deprecated, use XZ_DIR """

    yz_dir     = 6
    """ deprecated, use YZ_DIR """

    xyz_dir    = 7
    """ deprecated, use XYZ_DIR """

    point_dir  = 8
    """ deprecated, use POINT_DIR """

    angle      = 9
    """ deprecated, use XYZ_DIR """

    z_coord    = 10
    """ deprecated, use XYZ_DIR """

    plane_dir  = 11
    """ deprecated, use PLANE_DIR """

    vector_dir = 12
    """ deprecated, use VECTOR_DIR """


    #--------------------- enums with correct naming style

    X_DIR = x_dir
    """ Move the handle in x-direction.
        Draw an arrow symbol in x-direction """

    Y_DIR = y_dir
    """ Move the handle in y-direction.
        Draw an arrow symbol in y-direction """

    Z_DIR = z_dir
    """ Move the handle in z-direction.
        Draw an arrow symbol in z-direction """

    XY_DIR = xy_dir
    """ Move the handle in xy direction.
        Draw an arrow symbol in reference-handle point-direction """

    XZ_DIR = xz_dir
    """ Move the handle in xz direction.
        Draw an arrow symbol in reference-handle point-direction """

    YZ_DIR = yz_dir
    """ Move the handle in yz direction.
        Draw an arrow symbol in reference-handle point-direction """

    XYZ_DIR = xyz_dir
    """ Move the handle in xyz direction. """

    POINT_DIR = point_dir
    """ Move the handle in point direction, defined by the reference and handle point.
        Draw an arrow symbol in reference-handle point-direction """

    ANGLE = angle
    """ Move the handle in xy direction.
        Show a circle as info. """

    Z_COORD = z_coord
    """ Move the handle in point direction, defined by the reference and handle point.
        Draw an arrow symbol in reference-handle point-direction """

    PLANE_DIR = plane_dir
    """ Move the handle in xy direction on the defined plane from HandleProperties
        Draw an arrow symbol in reference-handle point-direction """

    VECTOR_DIR = vector_dir
    """ Move the handle in the direction defined by the vector from HandleProperties """

    CLICK = 13
    """ handle can be used as button, ..."""

```

</details>