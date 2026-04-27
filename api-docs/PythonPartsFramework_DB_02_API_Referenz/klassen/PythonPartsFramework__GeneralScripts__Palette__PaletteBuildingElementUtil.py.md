---
title: "PaletteBuildingElementUtil"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteBuildingElementUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PaletteBuildingElementUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteBuildingElementUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the building element utilities for the palette

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`

## Klassen

### `PaletteBuildingElementUtil`

implementation of the building element utilities for the palette
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_build_ele_index` | `page_building_ele: list[list[int]], build_ele_list: list[BuildingElement], page: int, name: str` | `int` | Get the start page and building element index of a building element from a page  Args:     page_building_ele: Building element index assigned to a page like [[0, 1], [1], [2], [3], [3], [3]]     build_ele_list:    list with the building elements     page:              Page index from the palette control     name:              Name of the control  Returns:     index of the building element |
| `get_page_from_building_element_index` | `build_ele_index: int, page_building_ele: list[list[int]], controls_prop_list: list[BuildingElementControlProperties], value_name: str` | `int` | Get page of a building element from a building element index  Args:     build_ele_index:    Building element index     page_building_ele:  Building element index assigned to a page like [[0, 1], [1], [2], [3], [3], [3]]     controls_prop_list: Controls property list     value_name:         Name of the value  Returns:     page index of the building element |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the building element utilities for the palette
"""

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties

class PaletteBuildingElementUtil():
    """ implementation of the building element utilities for the palette
    """

    PAGE_INDEX_KEY = 1000

    @staticmethod
    def get_build_ele_index(page_building_ele: list[list[int]],
                            build_ele_list   : list[BuildingElement],
                            page             : int,
                            name             : str) -> int:
        """ Get the start page and building element index of a building element from a page

        Args:
            page_building_ele: Building element index assigned to a page like [[0, 1], [1], [2], [3], [3], [3]]
            build_ele_list:    list with the building elements
            page:              Page index from the palette control
            name:              Name of the control

        Returns:
            index of the building element
        """

        #----------------- get the index from the parameter name

        if not page_building_ele:
            for index, build_ele in enumerate(build_ele_list):
                if build_ele.get_property(name) is not None:
                    return index


        #----------------- get the index for the building element range

        build_ele_indexes = page_building_ele[page]

        if len(build_ele_indexes) == 1:
            return build_ele_indexes[0]

        for build_ele_index in build_ele_indexes:
            if build_ele_list[build_ele_index].get_property(name) is not None:
                return build_ele_index

        return 0


    @staticmethod
    def get_page_from_building_element_index(build_ele_index   : int,
                                             page_building_ele : list[list[int]],
                                             controls_prop_list: list[BuildingElementControlProperties],
                                             value_name        : str) -> int:
        """ Get page of a building element from a building element index

        Args:
            build_ele_index:    Building element index
            page_building_ele:  Building element index assigned to a page like [[0, 1], [1], [2], [3], [3], [3]]
            controls_prop_list: Controls property list
            value_name:         Name of the value

        Returns:
            page index of the building element
        """

        if build_ele_index >= PaletteBuildingElementUtil.PAGE_INDEX_KEY:
            build_ele_index -= PaletteBuildingElementUtil.PAGE_INDEX_KEY

        for page_index, build_ele_indexes in enumerate(page_building_ele):
            for index in build_ele_indexes:
                if index == build_ele_index and \
                   next((True for prop in controls_prop_list[build_ele_index] if value_name == prop.value_name), False):
                    return page_index

        return 0

```

</details>