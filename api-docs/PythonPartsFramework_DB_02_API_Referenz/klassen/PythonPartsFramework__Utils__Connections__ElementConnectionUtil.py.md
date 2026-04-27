---
title: "ElementConnectionUtil"
source: "PythonPartsFramework\Utils\Connections\ElementConnectionUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ElementConnectionUtil

> **Pfad:** `PythonPartsFramework\Utils\Connections\ElementConnectionUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the element connection utility

## Abhängigkeiten

- `BuildingElement`
- `PythonPartTransaction`
- `ValueTypes.ParameterPropertyValueTypes`

## Klassen

### `ElementConnectionUtil`

implementation of the element connection utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_geometry_element_connection_elements` | `build_ele_list: list[BuildingElement], connect_to_elements: ConnectToElements` | `None` | add the elements from the ElementGeometryConnection value type  Args:     build_ele_list:      list with the building elements     connect_to_elements: elements for the to connection |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the element connection utility
"""

from BuildingElement import BuildingElement
from PythonPartTransaction import ConnectToElements

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes


class ElementConnectionUtil():
    """ implementation of the element connection utility
    """

    @staticmethod
    def add_geometry_element_connection_elements(build_ele_list     : list[BuildingElement],
                                                 connect_to_elements: ConnectToElements):
        """ add the elements from the ElementGeometryConnection value type

        Args:
            build_ele_list:      list with the building elements
            connect_to_elements: elements for the to connection
        """

        for build_ele in build_ele_list:
            for prop in build_ele.get_properties():
                if prop.value_type in (ParameterPropertyValueTypes.ELEMENT_GEOMETRY_CONNECTION,
                                       ParameterPropertyValueTypes.ARCH_OPENING_CONNECTION):
                    if isinstance(prop.value, list):
                        connect_to_elements.connection_elements.extend(str(item.get_connected_element_uuid())
                                                                       for item in prop.value if not item.element.IsNull())

                    elif not prop.value.element.IsNull():
                        connect_to_elements.connection_elements.append(str(prop.value.get_connected_element_uuid()))

                if prop.value_type == ParameterPropertyValueTypes.ARCH_OPENING_CONNECTION:
                    connect_to_elements.connect_pyp_as_child = True

```

</details>