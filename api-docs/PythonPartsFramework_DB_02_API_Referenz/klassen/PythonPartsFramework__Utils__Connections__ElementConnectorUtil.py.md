---
title: "ElementConnectorUtil"
source: "PythonPartsFramework\Utils\Connections\ElementConnectorUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - connector
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ElementConnectorUtil

> **Pfad:** `PythonPartsFramework\Utils\Connections\ElementConnectorUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `connector`, `utility`

## Übersicht

implementation of the element connector utility

## Abhängigkeiten

- `BuildingElementMaterialStringTable`
- `BuildingElementStringTable`
- `BuildingElementXML`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `PythonPartTransaction`
- `PythonPartUtil`
- `TypeCollections.ElementConnectorParameterList`
- `TypeCollections.ModificationElementList`
- `ValueTypes.ParameterPropertyValueTypes`

## Klassen

### `ElementConnectorUtil`

implementation of the element connector utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_element_connector_pythonpart` | `ele_connector_params: ElementConnectorParameterList, parent_ele: AllplanEleAdapter.BaseElementAdapter, doc: AllplanEleAdapter.DocumentAdapter` | `None` | creates an element connector PythonPart  Args:     ele_connector_params: list with the connector connections     parent_ele:           parent element which has the connections     doc:                  list with the element connector parameter |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the element connector utility
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementStringTable import BuildingElementStringTable
from BuildingElementXML import BuildingElementXML
from PythonPartUtil import PythonPartUtil

import PythonPartTransaction

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from TypeCollections.ElementConnectorParameterList import ElementConnectorParameterList
from TypeCollections.ModificationElementList import ModificationElementList

class ElementConnectorUtil():
    """ implementation of the element connector utility
    """


    @staticmethod
    def create_element_connector_pythonpart(ele_connector_params: ElementConnectorParameterList,
                                            parent_ele          : AllplanEleAdapter.BaseElementAdapter,
                                            doc                 : AllplanEleAdapter.DocumentAdapter):
        """ creates an element connector PythonPart

        Args:
            ele_connector_params: list with the connector connections
            parent_ele:           parent element which has the connections
            doc:                  list with the element connector parameter
        """

        while True:
            ele = AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(parent_ele)

            if ele.IsNull():
                break

            parent_ele = ele


        #----------------- get the building element for the connection

        file_name = f"{AllplanSettings.AllplanPaths.GetPythonPartsEtcPath()}" \
                    fr"PythonPartsFramework\Utils\Connections\ElementConnector.pyp"

        xml_ele = BuildingElementXML()

        connection_build_ele, _, _ = xml_ele.read_element_parameter(file_name,
                                                                    BuildingElementStringTable("", False, ""),
                                                                    BuildingElementMaterialStringTable("", False, ""))


        #----------------- create the connector PythonParts

        for connection_prop in ele_connector_params:
            if connection_prop.value_type == ParameterPropertyValueTypes.POINT_CONNECTION:
                connection_build_ele.PointConnections.value.append(connection_prop.value)
                connection_build_ele.PointConnectionNames.value.append(connection_prop.name)

            connection_build_ele.ParentElementUUID.value  = str(parent_ele.GetModelElementUUID())


        #----------------- create the PythonPart for the connection

            pyp_util = PythonPartUtil()

            connectors = pyp_util.create_pythonpart(connection_build_ele)

            pyp_trans = PythonPartTransaction.PythonPartTransaction(
                doc, connect_to_ele = PythonPartTransaction.ConnectToElements([str(guid) for guid in connection_prop.value.get_connected_elements()]))

            pyp_trans.execute(AllplanGeo.Matrix3D(), AllplanIFW.ViewWorldProjection(), connectors, ModificationElementList())

```

</details>