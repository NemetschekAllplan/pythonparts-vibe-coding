---
title: "StartFunctionResult"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\StartFunctionResult.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# StartFunctionResult

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\StartFunctionResult.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

implementation of the StartFunctionResult

## Abhängigkeiten

- `enum`
- `sys`
- `types`
- `typing`

## Klassen

### `StartFunctionResult`

enumeration for the start_function result
    

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
""" implementation of the StartFunctionResult
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


class StartFunctionResult(enum.IntEnum):
    """ enumeration for the start_function result
    """

    NOT_IMPLEMENTED       = 0
    """ not implemented """

    CANCEL_INPUT          = 1
    """ cancel the input """

    CONTINUE_INPUT        = 2
    """ continue the input """

    PRE_SELECTED_ELEMENTS = 3
    """ direct use of the pre-selected elements """
```

</details>