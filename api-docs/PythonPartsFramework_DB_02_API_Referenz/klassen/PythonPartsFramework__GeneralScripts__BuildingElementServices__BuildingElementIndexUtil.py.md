---
title: "BuildingElementIndexUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementServices\BuildingElementIndexUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementIndexUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementServices\BuildingElementIndexUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the building element index utility

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementComposite`
- `BuildingElementUtil`
- `typing`

## Klassen

### `BuildingElementIndexUtil`

implementation of the building element index utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `modify_building_element_index` | `name: str, value: Any, build_ele: BuildingElement, build_ele_list: list[BuildingElement], build_ele_composite: BuildingElementComposite` | `bool` | modify the building element index  Args:     name:                the name of the property.     value:               new value for property.     build_ele:           building element with the parameter properties     build_ele_list:      list with the building elements     build_ele_composite: building element composite with the building element constraints  Returns:     palette refresh state |
| `set_building_element_index` | `index: int, script_name: str, build_ele_list: list[BuildingElement], build_ele_composite: BuildingElementComposite` | `None` | Set the building element index  Args:     index:               Element index     script_name:         Script name     build_ele_list:      list with the building elements     build_ele_composite: building element composite with the building element constraints |
| `check_building_element_index` | `build_ele_list: list[BuildingElement], build_ele_composite: BuildingElementComposite` | `None` | Check the building element index (e.g. set to 0 for hidden elements)  Args:     build_ele_list:      list with the building elements     build_ele_composite: building element composite with the building element constraints |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the building element index utility
"""

from typing import Any

from BuildingElement import BuildingElement
from BuildingElementComposite import BuildingElementComposite
from BuildingElementUtil import BuildingElementUtil

class BuildingElementIndexUtil:
    """ implementation of the building element index utility
    """

    ELEMENT_INDEX_NAME = "__ElementIndex__"

    @staticmethod
    def modify_building_element_index(name               : str,
                                      value              : Any,
                                      build_ele          : BuildingElement,
                                      build_ele_list     : list[BuildingElement],
                                      build_ele_composite: BuildingElementComposite) -> bool:
        """ modify the building element index

        Args:
            name:                the name of the property.
            value:               new value for property.
            build_ele:           building element with the parameter properties
            build_ele_list:      list with the building elements
            build_ele_composite: building element composite with the building element constraints

        Returns:
            palette refresh state
        """

        if name != BuildingElementIndexUtil.ELEMENT_INDEX_NAME:
            return False

        script_name = build_ele.script_name

        BuildingElementIndexUtil.set_building_element_index(value, script_name, build_ele_list, build_ele_composite)

        return True


    @staticmethod
    def set_building_element_index(index              : int,
                                   script_name        : str,
                                   build_ele_list     : list[BuildingElement],
                                   build_ele_composite: BuildingElementComposite):
        """ Set the building element index

        Args:
            index:               Element index
            script_name:         Script name
            build_ele_list:      list with the building elements
            build_ele_composite: building element composite with the building element constraints
        """

        script_list = BuildingElementUtil.count_scripts(build_ele_list)

        if script_list[script_name] < index:
            index = script_list[script_name]

        visible_count = 0

        for i, build_ele in enumerate(build_ele_list):
            if i > 0 and script_name == build_ele.script_name and build_ele_composite.is_element_visible(i - 1, build_ele_list):
                visible_count += 1

        index = min(visible_count, index)

        for build_ele in build_ele_list:
            if script_name == build_ele.script_name:
                if (prop := build_ele.get_property(BuildingElementIndexUtil.ELEMENT_INDEX_NAME)):
                    prop.value = index


    @staticmethod
    def check_building_element_index(build_ele_list     : list[BuildingElement],
                                     build_ele_composite: BuildingElementComposite):
        """ Check the building element index (e.g. set to 0 for hidden elements)

        Args:
            build_ele_list:      list with the building elements
            build_ele_composite: building element composite with the building element constraints
        """

        for i in range(1, len(build_ele_list)):
            if build_ele_composite.is_element_visible(i - 1, build_ele_list):
                prop = getattr(build_ele_list[i], BuildingElementIndexUtil.ELEMENT_INDEX_NAME, None)

                if prop  and  prop.value != 0:
                    _, composite_index_list = build_ele_composite.get_composite_build_ele_list(i - 1, build_ele_list)

                    for composite_index in composite_index_list:
                        BuildingElementIndexUtil.set_building_element_index(prop.value, build_ele_list[composite_index].script_name,
                                                                            build_ele_list, build_ele_composite)

```

</details>