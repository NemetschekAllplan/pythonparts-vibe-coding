---
title: "PointConnectionUtil"
source: "PythonPartsFramework\Utils\Connections\PointConnectionUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PointConnectionUtil

> **Pfad:** `PythonPartsFramework\Utils\Connections\PointConnectionUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the point connection utility

## Abhängigkeiten

- `BuildingElement`
- `PythonPartTransaction`
- `TypeCollections.ElementConnectorParameterList`
- `ValueTypes.ParameterPropertyValueTypes`

## Klassen

### `PointConnectionUtil`

implementation of the point connection utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_point_connection_elements` | `build_ele_list: list[BuildingElement], connect_to_elements: ConnectToElements` | `None` | add the elements from the POINT_CONNECTION value type  Args:     build_ele_list:      list with the building elements     connect_to_elements: elements for the to connection |
| `get_ele_connector_params` | `build_ele_list: list[BuildingElement]` | `ElementConnectorParameterList` | get the point connection parameter  Args:     build_ele_list: list with the building elements  Returns:     connection elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the point connection utility
"""

from BuildingElement import BuildingElement
from PythonPartTransaction import ConnectToElements

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from TypeCollections.ElementConnectorParameterList import ElementConnectorParameterList


class PointConnectionUtil():
    """ implementation of the point connection utility
    """

    @staticmethod
    def add_point_connection_elements(build_ele_list     : list[BuildingElement],
                                      connect_to_elements: ConnectToElements):
        """ add the elements from the POINT_CONNECTION value type

        Args:
            build_ele_list:      list with the building elements
            connect_to_elements: elements for the to connection
        """

        connect_to_elements.connection_elements.extend(ele_guid_str
            for build_ele in build_ele_list
                for prop in build_ele.get_properties()
                    if prop.value_type == ParameterPropertyValueTypes.POINT_CONNECTION
                        for connected_ele in prop.value.get_connected_elements()
                            if (ele_guid_str := str(connected_ele)) not in connect_to_elements.connection_elements)



    @staticmethod
    def get_ele_connector_params(build_ele_list: list[BuildingElement]) -> ElementConnectorParameterList:
        """ get the point connection parameter

        Args:
            build_ele_list: list with the building elements

        Returns:
            connection elements
        """

        ele_connector_params = ElementConnectorParameterList()

        ele_connector_params.extend(prop
            for build_ele in build_ele_list
                for prop in build_ele.get_properties()
                    if prop.value_type == ParameterPropertyValueTypes.POINT_CONNECTION and prop.value.is_valid())

        return ele_connector_params

```

</details>