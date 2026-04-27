---
title: "ReinforcementShapePropertiesImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinforcementShapePropertiesImpl.py"
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


# ReinforcementShapePropertiesImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinforcementShapePropertiesImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `werte`

## Übersicht

implementation of the ReinforcementShapeProperties value type

## Abhängigkeiten

- `BaseIntImpl`
- `ParameterProperty`
- `ReinforcementShapeBarPropertiesImpl`
- `ReinforcementShapeMeshPropertiesImpl`
- `StdReinfShapeBuilder.ReinforcementShapeProperties`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `ReinforcementShapePropertiesImpl`

implementation of the ReinforcementShapeProperties value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `ReinforcementShapeProperties` | get the shape properties from a string  Args:     value_str: value string  Returns:     value from string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the ReinforcementShapeProperties value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING


from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties

from ..BaseIntImpl import BaseIntImpl
from .ReinforcementShapeBarPropertiesImpl import ReinforcementShapeBarPropertiesImpl
from .ReinforcementShapeMeshPropertiesImpl import ReinforcementShapeMeshPropertiesImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ReinforcementShapePropertiesImpl(BaseIntImpl):
    """ implementation of the ReinforcementShapeProperties value type
    """

    EMPTY_DIAMETER = "Diameter(0.0)"

    @staticmethod
    def get_value(value_str: str) -> ReinforcementShapeProperties:
        """ get the shape properties from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        if ReinforcementShapePropertiesImpl.EMPTY_DIAMETER not in value_str:
            return ReinforcementShapeBarPropertiesImpl.get_value(value_str)

        return ReinforcementShapeMeshPropertiesImpl.get_value(value_str)

```

</details>