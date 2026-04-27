---
title: "ReinforcementElementUitl"
source: "PythonPartsFramework\Utils\Reinforcement\ReinforcementElementUitl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ReinforcementElementUitl

> **Pfad:** `PythonPartsFramework\Utils\Reinforcement\ReinforcementElementUitl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

implementation of the reinforcement element utilities

## Abhängigkeiten

- `NemAll_Python_IFW_ElementAdapter`

## Klassen

### `ReinforcementElementUtil`

implementation of the reinforcement element utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_spiral_from_placement` | `bars_ele: AllplanEleAdapter.BaseElementAdapter` | `AllplanEleAdapter.BaseElementAdapter` | get the spiral from the placement  Args:     bars_ele: bars element  Returns:     spiral |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the reinforcement element utilities
"""

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

class ReinforcementElementUtil():
    """ implementation of the reinforcement element utilities
    """

    @staticmethod
    def get_spiral_from_placement(bars_ele: AllplanEleAdapter.BaseElementAdapter) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the spiral from the placement

        Args:
            bars_ele: bars element

        Returns:
            spiral
        """

        if bars_ele == AllplanEleAdapter.BarsSpiralPlacement_TypeUUID:
            return bars_ele

        bars_placement_ele = AllplanEleAdapter.BaseElementAdapter()

        while not (bars_ele := AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(bars_ele)).IsNull():
            if (bars_placement_ele := bars_ele) == AllplanEleAdapter.BarsLinearPlacement_TypeUUID:
                break

        if bars_placement_ele.IsNull():
            return bars_placement_ele

        if (spiral_ele := next((ele for ele in AllplanEleAdapter.BaseElementAdapterService.GetConnectedElements(bars_placement_ele)
                 if ele == AllplanEleAdapter.BarsSpiralPlacement_TypeUUID), None)) is not None:
            return spiral_ele

        return AllplanEleAdapter.BaseElementAdapter()

```

</details>