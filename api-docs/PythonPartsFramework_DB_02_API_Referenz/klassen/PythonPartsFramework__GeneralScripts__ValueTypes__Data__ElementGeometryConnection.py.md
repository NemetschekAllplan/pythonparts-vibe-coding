---
title: "ElementGeometryConnection"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Data\ElementGeometryConnection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ElementGeometryConnection

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Data\ElementGeometryConnection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the data class for the element geometry connection data

## Abhängigkeiten

- `BaseConnection`
- `DocumentManager`
- `GeometryElements.GeometryObjectImpl`
- `NemAll_Python_IFW_ElementAdapter`
- `Utilities.GeneralConstants`
- `__future__`
- `dataclasses`
- `enum`
- `hashlib`
- `typing`

## Klassen

### `GeometryType`

definition of the geometry type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ElementGeometryConnection`

implementation of the data class for the element geometry connection data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, element: AllplanEleAdapter.BaseElementAdapter, geometry_type: GeometryType` | `None` | initialize  Args:     element:       element     geometry_type: geometry type |
| `geometry` | `self` | `Any` | get the geometry  Returns:     element geometry |
| `element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | get the element  Returns:     element |
| `element` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `None` | set the element  Args:     element: element |
| `get_connected_element_uuid` | `self` | `str` | get the connected element UUIDs  Returns:     connected elements |
| `to_string` | `self` | `str` | convert the value to a string  Returns:     list as string |
| `get_value` | `value_str: str` | `ElementGeometryConnection` | get the value from a string  Args:     value_str: value string  Returns:     element geometry connection |
| `is_valid` | `self` | `bool` | check if the element is valid  Returns:     True if valid, False otherwise |
| `deep_copy` | `self` | `ElementGeometryConnection` | execute a deep copy  Returns:     copied object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the data class for the element geometry connection data
"""

from __future__ import annotations

from typing import Any

from dataclasses import dataclass

import enum
import hashlib

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from DocumentManager import DocumentManager

from Utilities.GeneralConstants import GeneralConstants

from ..GeometryElements.GeometryObjectImpl import GeometryObjectImpl

from .BaseConnection import BaseConnection


class GeometryType(enum.IntEnum):
    """ definition of the geometry type
    """

    BASE_GEOMETRY = 1
    """ base geometry of the element"""

    MODEL_GEOMETRY = 2
    """ model geometry of the element"""

    GROUNDVIEW_ARCH_ELE_GEOMETRY = 3
    """ ground view architecture element geometry"""

    PURE_ARCH_ELE_GEOMETRY = 4
    """ pure architecture element geometry without openings, ..."""


@dataclass
class ElementGeometryConnection(BaseConnection):
    """ implementation of the data class for the element geometry connection data
    """

    def __init__(self,
                 element      : AllplanEleAdapter.BaseElementAdapter,
                 geometry_type: GeometryType):
        """ initialize

        Args:
            element:       element
            geometry_type: geometry type
        """

        self.__element       = AllplanEleAdapter.BaseElementAdapter()
        self.__geometry      = Any
        self.__geometry_type = geometry_type

        self.element = element


    @property
    def geometry(self) -> Any:
        """ get the geometry

        Returns:
            element geometry
        """

        return self.__geometry


    @property
    def element(self) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the element

        Returns:
            element
        """

        return self.__element

    @element.setter
    def element(self, element: AllplanEleAdapter.BaseElementAdapter) -> None:
        """ set the element

        Args:
            element: element
        """

        self.__element = element

        if element.IsNull():
            return

        match self.__geometry_type:
            case GeometryType.BASE_GEOMETRY:
                self.__geometry = element.GetGeometry()

            case GeometryType.MODEL_GEOMETRY:
                self.__geometry = element.GetModelGeometry()

            case GeometryType.GROUNDVIEW_ARCH_ELE_GEOMETRY:
                self.__geometry = element.GetGroundViewArchitectureElementGeometry()

            case GeometryType.PURE_ARCH_ELE_GEOMETRY:
                self.__geometry = element.GetPureArchitectureElementGeometry()


    def get_connected_element_uuid(self) -> str:
        """ get the connected element UUIDs

        Returns:
            connected elements
        """

        return str(self.__element.GetElementUUID())


    def to_string(self) -> str:
        """ convert the value to a string

        Returns:
            list as string
        """

        geo_str = "" if self.element.IsNull() else GeometryObjectImpl.to_string(self.__geometry)

        geo_hash = hashlib.sha224(geo_str.encode('utf-8')).hexdigest()

        return f"ElementGeometryConnection({self.__element.GetElementUUID()}{GeneralConstants.TEXT_SEPARATOR}{geo_hash})"


    @staticmethod
    def get_value(value_str: str) -> ElementGeometryConnection:
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            element geometry connection
        """

        value_str = value_str.split("(", 1)[-1].rstrip(")")

        if value_str == GeneralConstants.EMPTY_LIST or not value_str:
            return ElementGeometryConnection(AllplanEleAdapter.BaseElementAdapter(), GeometryType.BASE_GEOMETRY)

        element_uuid, _ = value_str.split(GeneralConstants.TEXT_SEPARATOR)

        connection = ElementGeometryConnection(
            AllplanEleAdapter.BaseElementAdapter.FromGUID(AllplanEleAdapter.GUID.FromString(element_uuid),
            DocumentManager.get_instance().document), GeometryType.BASE_GEOMETRY)

        return connection


    def is_valid(self) -> bool:
        """ check if the element is valid

        Returns:
            True if valid, False otherwise
        """

        return not self.__element.IsNull()


    def deep_copy(self) -> ElementGeometryConnection:
        """ execute a deep copy

        Returns:
            copied object
        """

        connection = ElementGeometryConnection(self.__element, self.__geometry_type)

        return connection

```

</details>