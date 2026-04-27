---
title: "BuildingElementReinforcementUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementReinforcementUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementReinforcementUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementReinforcementUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `utility`

## Übersicht

Script for BuildingElementReinforcementUtil

## Abhängigkeiten

- `ValueTypes.Reinforcement.ReinforcementShapeBarPropertiesImpl`
- `ValueTypes.Reinforcement.ReinforcementShapeMeshPropertiesImpl`

## Klassen

### `BuildingElementReinforcementUtil`

Definition of class BuildingElementReinforcementUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value_reinforcementshapeproperties` | `value_str` | `None` | Get the reinforcement shape properties from a value string  Args:   value_str   Value string  Return: Reinforcement shape properties |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementReinforcementUtil
"""

from ValueTypes.Reinforcement.ReinforcementShapeBarPropertiesImpl import ReinforcementShapeBarPropertiesImpl
from ValueTypes.Reinforcement.ReinforcementShapeMeshPropertiesImpl import ReinforcementShapeMeshPropertiesImpl


class BuildingElementReinforcementUtil():
    """ Definition of class BuildingElementReinforcementUtil
    """

    @staticmethod
    def get_value_reinforcementshapeproperties(value_str):
        """ Get the reinforcement shape properties from a value string

        Args:   value_str   Value string

        Return: Reinforcement shape properties
        """

        if "Diameter(0.0)" not in value_str:
            return ReinforcementShapeBarPropertiesImpl.get_value(value_str)

        return ReinforcementShapeMeshPropertiesImpl.get_value(value_str)

```

</details>