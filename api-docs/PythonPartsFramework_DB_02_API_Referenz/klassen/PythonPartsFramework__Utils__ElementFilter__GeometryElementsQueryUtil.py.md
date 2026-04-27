---
title: "GeometryElementsQueryUtil"
source: "PythonPartsFramework\Utils\ElementFilter\GeometryElementsQueryUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GeometryElementsQueryUtil

> **Pfad:** `PythonPartsFramework\Utils\ElementFilter\GeometryElementsQueryUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the selection query utilities for geometry elements

## Abhängigkeiten

- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`

## Klassen

### `GeometryElementsQueryUtil`

implementation of the selection query utilities for geometry elements
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_surface_elements_query` | `-` | `AllplanIFW.SelectionQuery` | create a query for the geometry elements with a surface  Returns:     selection query |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the selection query utilities for geometry elements
"""

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

class GeometryElementsQueryUtil():
    """ implementation of the selection query utilities for geometry elements
    """

    @staticmethod
    def create_surface_elements_query() -> AllplanIFW.SelectionQuery:
        """ create a query for the geometry elements with a surface

        Returns:
            selection query
        """

        type_queries = [AllplanIFW.QueryTypeID(ele_guid) for ele_guid in (AllplanEleAdapter.Volume3D_TypeUUID,
                                                                          AllplanEleAdapter.BRep3D_Volume_TypeUUID,
                                                                          AllplanEleAdapter.Cylinder3D_TypeUUID,
                                                                          AllplanEleAdapter.BRep3D_Surface_TypeUUID,
                                                                          AllplanEleAdapter.Area3D_TypeUUID)]

        return AllplanIFW.SelectionQuery(type_queries)

```

</details>