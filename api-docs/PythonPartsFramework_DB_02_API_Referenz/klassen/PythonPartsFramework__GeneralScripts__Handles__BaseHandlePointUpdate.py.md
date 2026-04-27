---
title: "BaseHandlePointUpdate"
source: "PythonPartsFramework\GeneralScripts\Handles\BaseHandlePointUpdate.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# BaseHandlePointUpdate

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\BaseHandlePointUpdate.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the base class for the handle point update

## Abhängigkeiten

- `BuildingElement`
- `HandleParameterData`
- `HandleProperties`
- `__future__`
- `abc`
- `typing`

## Klassen

### `BaseHandlePointUpdate`

implementation of the  base class for the handle point update
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, handle_prop: HandleProperties, param_data: HandleParameterData, value: float` | `None` | initialize  Args:     handle_prop: handle property     param_data:  parameter data     value:       value |
| `__call__` | `self` | `None` | execute the value update          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base class for the handle point update
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import abc

from HandleParameterData import HandleParameterData
from HandleProperties import HandleProperties

if TYPE_CHECKING:
    from BuildingElement import BuildingElement

class BaseHandlePointUpdate(abc.ABC):
    """ implementation of the  base class for the handle point update
    """

    def __init__(self,
                 handle_prop: HandleProperties,
                 param_data : HandleParameterData,
                 value      : float):
        """ initialize

        Args:
            handle_prop: handle property
            param_data:  parameter data
            value:       value
        """

        self._handle_prop = handle_prop
        self._param_data  = param_data

        if (distance_factor := self._param_data.distance_factor) is None:
            distance_factor = self._handle_prop.distance_factor

        self.value = value * distance_factor


    @abc.abstractmethod
    def __call__(self):
        """ execute the value update
        """

```

</details>