---
title: "AttributeIdValue"
source: "PythonPartsFramework\GeneralScripts\AttributeIdValue.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# AttributeIdValue

> **Pfad:** `PythonPartsFramework\GeneralScripts\AttributeIdValue.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the data class for the attribute id and value 

## Abhängigkeiten

- `dataclasses`
- `sys`
- `types`
- `typing`

## Klassen

### `AttributeIdValue`

implementation of the data class for the attribute id and value 

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
""" implementation of the data class for the attribute id and value """

from typing import Any

from dataclasses import dataclass
from types import ModuleType

import sys

@dataclass
class AttributeIdValue():
    """ implementation of the data class for the attribute id and value """

    attribute_id : int = 0
    value        : Any = ""


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