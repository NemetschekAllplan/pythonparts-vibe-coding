---
title: "HandlePropUpdateData"
source: "PythonPartsFramework\GeneralScripts\Handles\HandlePropUpdateData.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandlePropUpdateData

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\HandlePropUpdateData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the handle property update data

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `Utilities.ModuleReloaderUtil`
- `__future__`
- `importlib`
- `sys`
- `types`
- `typing`

## Klassen

### `HandlePropUpdateData`

handle update data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, name: str` | `None` | initialize  Args:     name: name of the update class |
| `get_handle_prop_update` | `self` | `BaseHandlePropUpdate` | get the handle property update class  Returns:     returns |

## Funktionen

### `__reload__(_mod: ModuleType)`

don't reload this module to avoid problems with the isinstance check

Args:
    _mod: module

Returns:
    current module

**Parameter:**
- `_mod: ModuleType`

**Rückgabe:** `ModuleType`

**Beispiel:**
```python
result = __reload__(...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the handle property update data
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from types import ModuleType

import importlib
import sys

from Utilities.ModuleReloaderUtil import ModuleReloaderUtil

if TYPE_CHECKING:
    from .BaseHandlePropUpdate import BaseHandlePropUpdate


class HandlePropUpdateData(ModuleReloaderUtil):
    """ handle update data
    """

    def __init__(self,
                 name: str):
        """ initialize

        Args:
            name: name of the update class
        """

        self.name     = name
        self.module   = None
        self.reloaded = False


    def get_handle_prop_update(self) -> BaseHandlePropUpdate:
        """ get the handle property update class

        Returns:
            returns
        """

        if self.module is None:
            self.module = __import__(f"Handles.{self.name}", fromlist = self.name)

        if self.RELOAD_MODULE and not self.reloaded:
            self.module = importlib.reload(self.module)

            self.reloaded = True

        return getattr(self.module, self.name)


def __reload__(_mod: ModuleType) -> ModuleType:
    """ don't reload this module to avoid problems with the isinstance check

    Args:
        _mod: module

    Returns:
        current module
    """

    HandlePropUpdateData.set_reload()

    return sys.modules[__name__]

```

</details>