---
title: "PolyPointsDistanceType"
source: "PythonPartsFramework\Utils\HandleCreator\PolyPointsDistanceType.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PolyPointsDistanceType

> **Pfad:** `PythonPartsFramework\Utils\HandleCreator\PolyPointsDistanceType.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `utility`

## Übersicht

define the distance type for poly points

## Abhängigkeiten

- `enum`
- `sys`
- `types`
- `typing`

## Klassen

### `PolyPointsDistanceType`

enum for the distance type of the poly points
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

### `__reload__(_mod: ModuleType)`

don't reload this module to avoid problems with the enum check

Args:
    _mod: module

Returns:
    current module

**Parameter:**
- `_mod: ModuleType`

**Rückgabe:** `Any`

**Beispiel:**
```python
result = __reload__(...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" define the distance type for poly points
"""

from typing import Any

import enum
import sys

from types import ModuleType

class PolyPointsDistanceType(enum.Flag):
    """ enum for the distance type of the poly points
    """
    NONE    = 0
    DELTA_X = 1
    DELTA_Y = 2
    DELTA_Z = 4
    LENGTH  = 8
    ALL     = DELTA_X | DELTA_Y | DELTA_Z | LENGTH


def __reload__(_mod: ModuleType) -> Any:
    """ don't reload this module to avoid problems with the enum check

    Args:
        _mod: module

    Returns:
        current module
    """

    return sys.modules[__name__]

```

</details>