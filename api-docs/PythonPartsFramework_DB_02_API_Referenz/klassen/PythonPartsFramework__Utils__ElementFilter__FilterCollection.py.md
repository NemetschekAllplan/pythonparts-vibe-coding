---
title: "FilterCollection"
source: "PythonPartsFramework\Utils\ElementFilter\FilterCollection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# FilterCollection

> **Pfad:** `PythonPartsFramework\Utils\ElementFilter\FilterCollection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the filter collection

## Abhängigkeiten

- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `ScriptObjectInteractors.BaseFilterObject`
- `collections.abc`

## Klassen

### `FilterCollection`

implementation of the filter collection
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, and_filter: bool=False` | `None` | initialize  Args:     and_filter: combine the filters with an AND operation |
| `append` | `self, ele_filter: BaseFilterObject | AllplanIFW.SelectionQuery | Callable[[AllplanEleAdapter.BaseElementAdapter], bool]` | `None` | append a filter  Args:     ele_filter: filter |
| `__call__` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `bool` | execute the filter collection  Args:     element: element to filter  Returns:     element fulfills the filter: True/False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the filter collection
"""

from collections.abc import Callable

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from ScriptObjectInteractors.BaseFilterObject import BaseFilterObject

class FilterCollection(BaseFilterObject):
    """ implementation of the filter collection
    """

    def __init__(self,
                 and_filter: bool = False):
        """ initialize

        Args:
            and_filter: combine the filters with an AND operation
        """

        self.and_filter = and_filter

        self.filters : list[(BaseFilterObject | AllplanIFW.SelectionQuery | Callable[[AllplanEleAdapter.BaseElementAdapter], bool])] = []


    def append(self,
               ele_filter: (BaseFilterObject | AllplanIFW.SelectionQuery | Callable[[AllplanEleAdapter.BaseElementAdapter], bool])):
        """ append a filter

        Args:
            ele_filter: filter
        """

        self.filters.append(ele_filter)


    def __call__(self, element: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ execute the filter collection

        Args:
            element: element to filter

        Returns:
            element fulfills the filter: True/False
        """

        return all(ele_filter(element) for ele_filter in self.filters) if self.and_filter else \
               any(ele_filter(element) for ele_filter in self.filters)

```

</details>