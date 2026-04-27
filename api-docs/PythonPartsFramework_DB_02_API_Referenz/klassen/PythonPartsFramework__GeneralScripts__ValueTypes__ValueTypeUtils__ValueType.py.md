---
title: "ValueType"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ValueType.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ValueType

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ValueType.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the value type

## Abhängigkeiten

- `Utilities.ModuleReloaderUtil`
- `__future__`
- `importlib`
- `sys`
- `types`
- `typing`

## Klassen

### `ValueType`

definition of the value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__new__` | `cls: type, _value_type_impl: str, value_type: str, _has_impl: bool, _is_persistent: bool` | `ValueType` | initialize  Args:     cls:              description     _value_type_impl: value type implementation     value_type:       value type     _has_impl:        has implementation state. Defaults to False.     _is_persistent:   persistent state  Returns:     created object |
| `__init__` | `self, value_type_impl: str, _value_type: str, has_impl: bool, is_persistent: bool` | `None` | initialize  Args:     value_type_impl: value type implementation     _value_type:     value type     has_impl:        has implementation state. Defaults to False.     is_persistent:   persistent state |
| `create_parameter_property_value_type` | `self` | `Any` | create the parameter property based value type  Returns:     parameter property based value type |

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
""" implementation of the value type
"""

# pylint: disable=global-statement

from __future__ import annotations

from typing import Any
from types import ModuleType

import importlib
import sys

from Utilities.ModuleReloaderUtil import ModuleReloaderUtil


class ValueType(str , ModuleReloaderUtil):
    """ definition of the value type
    """

    def __new__(cls             : type,
                _value_type_impl: str,
                value_type      : str,
                _has_impl       : bool,
                _is_persistent  : bool) -> ValueType:
        """ initialize

        Args:
            cls:              description
            _value_type_impl: value type implementation
            value_type:       value type
            _has_impl:        has implementation state. Defaults to False.
            _is_persistent:   persistent state

        Returns:
            created object
        """

        instance = super().__new__(cls, value_type.lower().replace(" ", ""))

        return instance


    def __init__(self,
                 value_type_impl: str,
                 _value_type    : str,
                 has_impl       : bool,
                 is_persistent  : bool):
        """ initialize

        Args:
            value_type_impl: value type implementation
            _value_type:     value type
            has_impl:        has implementation state. Defaults to False.
            is_persistent:   persistent state
        """

        self.has_impl        = has_impl
        self.value_type_impl = value_type_impl
        self.is_persistent   = is_persistent


    def create_parameter_property_value_type(self) -> Any:
        """ create the parameter property based value type

        Returns:
            parameter property based value type
        """

        value_type = self.value_type_impl.rsplit(".", 1)[-1]

        module = __import__(f"ValueTypes.{self.value_type_impl}", fromlist = value_type)

        if self.RELOAD_MODULE:
            module = importlib.reload(module)

        value_type_impl = getattr(module, value_type)

        return value_type_impl(self)


def __reload__(_mod: ModuleType) -> ModuleType:
    """ don't reload this module to avoid problems with the isinstance check

    Args:
        _mod: module

    Returns:
        current module
    """

    ValueType.set_reload()

    return sys.modules[__name__]

```

</details>