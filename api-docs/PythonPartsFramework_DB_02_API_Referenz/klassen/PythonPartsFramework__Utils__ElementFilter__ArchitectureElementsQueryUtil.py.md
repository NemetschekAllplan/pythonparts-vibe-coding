---
title: "ArchitectureElementsQueryUtil"
source: "PythonPartsFramework\Utils\ElementFilter\ArchitectureElementsQueryUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ArchitectureElementsQueryUtil

> **Pfad:** `PythonPartsFramework\Utils\ElementFilter\ArchitectureElementsQueryUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the selection query utilities for architecture elements

## Abhängigkeiten

- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`

## Klassen

### `ArchitectureElementsQueryUtil`

implementation of the selection query utilities for architecture elements
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_arch_general_opening_elements_query` | `-` | `AllplanIFW.SelectionQuery` | create a query for the elements with a possible general opening input  Returns:     selection query |
| `create_arch_door_window_opening_elements_query` | `-` | `AllplanIFW.SelectionQuery` | create a query for the elements with a possible door/window input  Returns:     selection query |
| `create_vertical_arch_opening_query` | `-` | `AllplanIFW.SelectionQuery` | create a query for the vertical architecture opening elements  Returns:     selection query |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the selection query utilities for architecture elements
"""

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

class ArchitectureElementsQueryUtil():
    """ implementation of the selection query utilities for architecture elements
    """

    @staticmethod
    def create_arch_general_opening_elements_query() -> AllplanIFW.SelectionQuery:
        """ create a query for the elements with a possible general opening input

        Returns:
            selection query
        """

        type_queries = [AllplanIFW.QueryTypeID(ele_guid) for ele_guid in (AllplanEleAdapter.WallTier_TypeUUID,
                                                                          AllplanEleAdapter.CircularWallTier_TypeUUID,
                                                                          AllplanEleAdapter.ElementWallTier_TypeUUID,
                                                                          AllplanEleAdapter.PolygonWallTier_TypeUUID,
                                                                          AllplanEleAdapter.ProfileWallTier_TypeUUID,
                                                                          AllplanEleAdapter.LineUpstandTier_TypeUUID,
                                                                          AllplanEleAdapter.CircularUpstandTier_TypeUUID,
                                                                          AllplanEleAdapter.ElementUpstandTier_TypeUUID,
                                                                          AllplanEleAdapter.Beam_TypeUUID,
                                                                          AllplanEleAdapter.Column_TypeUUID,
                                                                          AllplanEleAdapter.StripFoundation_TypeUUID,
                                                                          AllplanEleAdapter.IndividualFoundation_TypeUUID)]

        return AllplanIFW.SelectionQuery(type_queries)


    @staticmethod
    def create_arch_door_window_opening_elements_query() -> AllplanIFW.SelectionQuery:
        """ create a query for the elements with a possible door/window input

        Returns:
            selection query
        """

        type_queries = [AllplanIFW.QueryTypeID(ele_guid) for ele_guid in (AllplanEleAdapter.WallTier_TypeUUID,
                                                                          AllplanEleAdapter.CircularWallTier_TypeUUID,
                                                                          AllplanEleAdapter.ElementWallTier_TypeUUID,
                                                                          AllplanEleAdapter.ProfileWallTier_TypeUUID,
                                                                          AllplanEleAdapter.LineUpstandTier_TypeUUID,
                                                                          AllplanEleAdapter.CircularUpstandTier_TypeUUID,
                                                                          AllplanEleAdapter.ElementUpstandTier_TypeUUID)]

        return AllplanIFW.SelectionQuery(type_queries)


    @staticmethod
    def create_vertical_arch_opening_query() -> AllplanIFW.SelectionQuery:
        """ create a query for the vertical architecture opening elements

        Returns:
            selection query
        """

        type_queries = [AllplanIFW.QueryTypeID(ele_guid) for ele_guid in (AllplanEleAdapter.DoorTier_TypeUUID,
                                                                          AllplanEleAdapter.NicheTier_TypeUUID,
                                                                          AllplanEleAdapter.RecessTier_TypeUUID,
                                                                          AllplanEleAdapter.WindowTier_TypeUUID
                                                                          )]

        return AllplanIFW.SelectionQuery(type_queries)

```

</details>