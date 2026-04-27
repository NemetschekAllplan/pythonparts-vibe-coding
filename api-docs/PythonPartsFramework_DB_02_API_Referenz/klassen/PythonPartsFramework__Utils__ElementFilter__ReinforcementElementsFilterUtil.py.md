---
title: "ReinforcementElementsFilterUtil"
source: "PythonPartsFramework\Utils\ElementFilter\ReinforcementElementsFilterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ReinforcementElementsFilterUtil

> **Pfad:** `PythonPartsFramework\Utils\ElementFilter\ReinforcementElementsFilterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

implementation of the selection query utilities for reinforcement elements

## Abhängigkeiten

- `FilterCollection`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `ScriptObjectInteractors.BaseFilterObject`

## Klassen

### `BarPlacementFilter`

implementation of the bar placement filter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, placement_type: AllplanEleAdapter.GUID` | `None` | initialize  Args:     placement_type: placement type |
| `__call__` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `bool` | execute the filtering  Args:     element: element to filter  Returns:     element fulfills the filter: True/False |

### `BarSpiralPlacementFilter`

implementation of the spiral bar placement filter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `bool` | execute the filtering  Args:     element: element to filter  Returns:     element fulfills the filter: True/False |

### `ReinforcementElementsFilterUtil`

implementation of the selection query utilities for reinforcement elements
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_linear_bar_placement_filter` | `-` | `FilterCollection` | create the element selection filter for a linear bar placement  Returns:     selection query |
| `create_spiral_bar_placement_filter` | `-` | `FilterCollection` | create the element selection filter for a spiral bar placement  Returns:     selection query |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the selection query utilities for reinforcement elements
"""

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from ScriptObjectInteractors.BaseFilterObject import BaseFilterObject

from .FilterCollection import FilterCollection


class BarPlacementFilter(BaseFilterObject):
    """ implementation of the bar placement filter
    """

    def __init__(self,
                 placement_type: AllplanEleAdapter.GUID):
        """ initialize

        Args:
            placement_type: placement type
        """

        self.placement_type = placement_type


    def __call__(self,
                 element: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ execute the filtering

        Args:
            element: element to filter

        Returns:
            element fulfills the filter: True/False
        """

        if element == self.placement_type:
            return True

        while not (element := AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(element)).IsNull():
            if element == self.placement_type:
                return True

        return False


class BarSpiralPlacementFilter(BaseFilterObject):
    """ implementation of the spiral bar placement filter
    """

    def __call__(self,
                 element: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ execute the filtering

        Args:
            element: element to filter

        Returns:
            element fulfills the filter: True/False
        """

        if element == AllplanEleAdapter.BarsSpiralPlacement_TypeUUID:
            return True

        if element != AllplanEleAdapter.BarsRepresentationLine_TypeUUID:
            return False

        bars_placement_ele = AllplanEleAdapter.BaseElementAdapter()

        while not (element := AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(element)).IsNull():
            if (bars_placement_ele := element) == AllplanEleAdapter.BarsLinearPlacement_TypeUUID:
                break

        if bars_placement_ele.IsNull():
            return False


        #----------------- the spiral is connected to the linear placement

        if any(ele == AllplanEleAdapter.BarsSpiralPlacement_TypeUUID
               for ele in AllplanEleAdapter.BaseElementAdapterService.GetConnectedElements(bars_placement_ele)):
            return True

        return False


class ReinforcementElementsFilterUtil():
    """ implementation of the selection query utilities for reinforcement elements
    """

    @staticmethod
    def create_linear_bar_placement_filter() -> FilterCollection:
        """ create the element selection filter for a linear bar placement

        Returns:
            selection query
        """

        type_queries = [AllplanIFW.QueryTypeID(ele_guid) for ele_guid in (AllplanEleAdapter.BarsRepresentationLine_TypeUUID,
                                                                          AllplanEleAdapter.BarsAreaRepresentationLine_TypeUUID)]

        placement_filter = FilterCollection(True)

        placement_filter.append(AllplanIFW.SelectionQuery(type_queries))

        placement_filter.append(BarPlacementFilter(AllplanEleAdapter.BarsLinearPlacement_TypeUUID))

        return placement_filter


    @staticmethod
    def create_spiral_bar_placement_filter() -> FilterCollection:
        """ create the element selection filter for a spiral bar placement

        Returns:
            selection query
        """

        placement_filter = FilterCollection(True)

        placement_filter.append(BarSpiralPlacementFilter())

        return placement_filter

```

</details>