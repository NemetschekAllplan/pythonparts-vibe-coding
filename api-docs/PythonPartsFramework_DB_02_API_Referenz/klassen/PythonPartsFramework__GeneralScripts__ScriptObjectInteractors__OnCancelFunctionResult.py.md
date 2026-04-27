---
title: "OnCancelFunctionResult"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\OnCancelFunctionResult.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# OnCancelFunctionResult

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\OnCancelFunctionResult.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

implementation of the OnCancelFunctionResult

## Abhängigkeiten

- `enum`
- `sys`
- `types`
- `typing`

## Klassen

### `OnCancelFunctionResult`

enumeration for the on_cancel_function result
    

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
""" implementation of the OnCancelFunctionResult
"""

from typing import Any

import sys
import enum

from types import ModuleType

def __reload__(_mod: ModuleType) -> Any:
    """ don't reload this module to avoid problems with the enum check

    Args:
        _mod: module

    Returns:
        current module
    """

    return sys.modules[__name__]


class OnCancelFunctionResult(enum.IntEnum):
    """ enumeration for the on_cancel_function result
    """

    CANCEL_INPUT    = 1
    CONTINUE_INPUT  = 2
    CREATE_ELEMENTS = 3
    NOT_IMPLEMENTED = 4
    RESTART         = 5

```

</details>