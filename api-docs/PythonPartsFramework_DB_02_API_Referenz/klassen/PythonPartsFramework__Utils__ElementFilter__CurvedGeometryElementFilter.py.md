---
title: "CurvedGeometryElementFilter"
source: "PythonPartsFramework\Utils\ElementFilter\CurvedGeometryElementFilter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# CurvedGeometryElementFilter

> **Pfad:** `PythonPartsFramework\Utils\ElementFilter\CurvedGeometryElementFilter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the curved geometry element filter

## Abhängigkeiten

- `NemAll_Python_IFW_ElementAdapter`
- `ScriptObjectInteractors.BaseFilterObject`
- `TypeCollections.GeometryTyping`

## Klassen

### `CurvedGeometryElementFilter`

implementation of the curved geometry element filter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, filter_curve_2d: bool, filter_curve_3d: bool` | `None` | initialize  Args:     filter_curve_2d: filter 2D curves     filter_curve_3d: filter 3D curves |
| `__call__` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `bool` | execute the filtering  Args:     element: element to filter  Returns:     element fulfills the filter: True/False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the curved geometry element filter
"""

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from ScriptObjectInteractors.BaseFilterObject import BaseFilterObject

from TypeCollections.GeometryTyping import GeometryTyping

class CurvedGeometryElementFilter(BaseFilterObject):
    """ implementation of the curved geometry element filter
    """

    def __init__(self,
                 filter_curve_2d: bool,
                 filter_curve_3d: bool):
        """ initialize

        Args:
            filter_curve_2d: filter 2D curves
            filter_curve_3d: filter 3D curves
        """

        self.filter_curve_2d = filter_curve_2d
        self.filter_curve_3d = filter_curve_3d


    def __call__(self,
                 element: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ execute the filtering

        Args:
            element: element to filter

        Returns:
            element fulfills the filter: True/False
        """

        if (geo_ele := element.GetGeometry()) is None:
            return False

        if GeometryTyping.is_curve_2d(geo_ele):
            return self.filter_curve_2d

        return self.filter_curve_3d if GeometryTyping.is_curve_3d(geo_ele) else False

```

</details>