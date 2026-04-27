---
title: "ReinfBarLabelPointerImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfBarLabelPointerImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ReinfBarLabelPointerImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfBarLabelPointerImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `werte`

## Übersicht

implementation of ReinfBarLabelPointer value type

## Abhängigkeiten

- `BaseReinfLabelPointerImpl`
- `BuildingElement`
- `NemAll_Python_Reinforcement`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `ReinfBarLabelPointerImpl`

implementation of the ReinfBarLabelPointer value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `AllplanReinf.BarLabelPointerProperties` | get the common properties from a string  Args:     value_str: common properties string  Returns:     common properties from the string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of ReinfBarLabelPointer value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import NemAll_Python_Reinforcement as AllplanReinf

from .BaseReinfLabelPointerImpl import BaseReinfLabelPointerImpl

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService


class ReinfBarLabelPointerImpl(BaseReinfLabelPointerImpl[AllplanReinf.BarLabelPointerProperties]):
    """ implementation of the ReinfBarLabelPointer value type
    """

    @staticmethod
    def get_value(value_str: str) -> AllplanReinf.BarLabelPointerProperties:
        """ get the common properties from a string

        Args:
            value_str: common properties string

        Returns:
            common properties from the string
        """

        return cast(AllplanReinf.BarLabelPointerProperties, BaseReinfLabelPointerImpl.get_pointer_value( \
                                                      value_str, AllplanReinf.BarLabelPointerProperties))

```

</details>