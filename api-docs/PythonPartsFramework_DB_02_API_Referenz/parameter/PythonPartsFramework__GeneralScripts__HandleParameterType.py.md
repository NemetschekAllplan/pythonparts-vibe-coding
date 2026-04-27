---
title: "HandleParameterType"
source: "PythonPartsFramework\GeneralScripts\HandleParameterType.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - parameter
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandleParameterType

> **Pfad:** `PythonPartsFramework\GeneralScripts\HandleParameterType.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `parameter`, `script`

## Übersicht

Implementation of the handle parameter type.

## Abhängigkeiten

- `enum`

## Klassen

### `HandleParameterType`

The parameter type defines the function to be used to recalculate the value
of the parameter property assigned to the handle.

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
""" Implementation of the handle parameter type.
"""

from enum import IntEnum

class HandleParameterType(IntEnum):
    """ The parameter type defines the function to be used to recalculate the value
    of the parameter property assigned to the handle.
    """

    X_DISTANCE      = 1
    """ Calculate the value from the x-distance between the reference and handle point """

    Y_DISTANCE      = 2
    """ Calculate the value from the y-distance between the reference and handle point """

    Z_DISTANCE      = 3
    """ Calculate the value from the z-distance between the reference and handle point """

    POINT           = 7
    """ Set the value to the handle point """

    POINT_DISTANCE  = 8
    """ Calculate the value from the distance between the reference and handle point """

    ANGLE           = 9
    """ Calculate the angle from the xy-plane vector between the reference and handle point"""

    Z_COORD         = 10
    """ Calculate the value for the "ZMin" or "ZMax" parameter. The distance
        between these values is adapted to the distance between the reference
        and handle point """

    VECTOR_DISTANCE = 12
    """ Calculate the value from the distance between the reference and handle point,
        transformed to the vector direction assigned to the HandleProperties"""

    CHECK_BOX = 13
    """ Use the handle as checkbox """

    INCREMENT_BUTTON = 14
    """ Use the handle as button to increment the value """

    DECREMENT_BUTTON = 15
    """ Use the handle as button to decrement the value """

    SPLIT_POINT = 16
    """ Use the handle as split point for a point list"""

    CURVE_POINT = 17
    """ Use the handle as curve point, allow to delete the point with shift + click """

    CURVE_SPLIT_POINT = 18
    """ Use the handle as curve split point """

    X_POINT_DISTANCE = 19
    """ Calculate the handle point from the x-distance between the reference and handle point """

    Y_POINT_DISTANCE = 20
    """ Calculate the handle point from the y-distance between the reference and handle point """

    Z_POINT_DISTANCE = 21
    """ Calculate the handle point from the y-distance between the reference and handle point """

    LENGTH_POINT_DISTANCE = 22
    """ Calculate the handle point from the length between the reference and handle point """

```

</details>