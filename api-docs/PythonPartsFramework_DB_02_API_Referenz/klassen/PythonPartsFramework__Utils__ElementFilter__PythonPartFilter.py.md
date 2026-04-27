---
title: "PythonPartFilter"
source: "PythonPartsFramework\Utils\ElementFilter\PythonPartFilter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PythonPartFilter

> **Pfad:** `PythonPartsFramework\Utils\ElementFilter\PythonPartFilter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the PythonPart filter

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`
- `ScriptObjectInteractors.BaseFilterObject`

## Klassen

### `PythonPartFilter`

implementation of the PythonPart filter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `bool` | execute the filtering  Args:     element: element to filter  Returns:     element fulfills the filter: True/False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart filter
"""

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from ScriptObjectInteractors.BaseFilterObject import BaseFilterObject

class PythonPartFilter(BaseFilterObject):
    """ implementation of the PythonPart filter
    """

    def __call__(self, element: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ execute the filtering

        Args:
            element: element to filter

        Returns:
            element fulfills the filter: True/False
        """

        return AllplanBaseEle.PythonPartService.IsPythonPartElement(element) or \
               AllplanBaseEle.PythonPartService.IsPythonPartGroupElement(element)

```

</details>