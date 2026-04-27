---
title: "PointConnection"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Data\PointConnection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PointConnection

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Data\PointConnection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the data class for the point connection data

## Abhängigkeiten

- `BaseConnection`
- `DocumentManager`
- `GeometryElements.Point3DImpl`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Utility`
- `Utilities.GeneralConstants`
- `__future__`
- `dataclasses`
- `hashlib`

## Klassen

### `PointConnection`

implementation of the data class for the parameter connection data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, docking_point: AllplanIFW.DockingPoint` | `None` | initialize  Args:     docking_point: docking point |
| `point` | `self` | `AllplanGeo.Point3D` | get the point  Returns:     point |
| `is_valid` | `self` | `bool` | test fof valid connection  Returns:     valid state |
| `get_connected_elements` | `self` | `AllplanUtil.VecGUIDList` | get the connected elements  Returns:     connected elements |
| `to_string` | `self` | `str` | convert the value to a string  Returns:     list as string |
| `get_value` | `value_str: str` | `PointConnection | list[PointConnection]` | get the value from a string  Args:     value_str: value string  Returns:     value |
| `reset` | `self` | `None` | reset the connection          |
| `deep_copy` | `self` | `PointConnection` | execute a deep copy  Returns:     copied object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the data class for the point connection data
"""

from __future__ import annotations

from dataclasses import dataclass

import hashlib

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Utility as AllplanUtil

from DocumentManager import DocumentManager

from Utilities.GeneralConstants import GeneralConstants

from ..GeometryElements.Point3DImpl import Point3DImpl

from .BaseConnection import BaseConnection

@dataclass
class PointConnection(BaseConnection):
    """ implementation of the data class for the parameter connection data
    """

    __docking_point : AllplanIFW.DockingPoint = AllplanIFW.DockingPoint()
    __point         : AllplanGeo.Point3D      = AllplanGeo.Point3D()
    __point_hash    : str                     = ""


    def __init__(self,
                 docking_point: AllplanIFW.DockingPoint):
        """ initialize

        Args:
            docking_point: docking point
        """

        self.__docking_point = docking_point

        if not docking_point.IsValid():
            self.__point_hash = ""

            return


        #----------------- set the connection data

        self.__point = docking_point.GetPoint(DocumentManager.get_instance().document)

        point_str = Point3DImpl.to_string(self.__point)

        self.__point_hash = hashlib.sha224(point_str.encode('utf-8')).hexdigest()


    @property
    def point(self) -> AllplanGeo.Point3D:
        """ get the point

        Returns:
            point
        """

        return self.__point


    def is_valid(self) -> bool:
        """ test fof valid connection

        Returns:
            valid state
        """

        return self.__docking_point.IsValid()


    def get_connected_elements(self) -> AllplanUtil.VecGUIDList:
        """ get the connected elements

        Returns:
            connected elements
        """

        return self.__docking_point.GetDockedElements() if self.is_valid() else AllplanUtil.VecGUIDList()


    def to_string(self) -> str:
        """ convert the value to a string

        Returns:
            list as string
        """

        if not self.__docking_point.IsValid():
            return ""

        docking_pnt_str = self.__docking_point.ToString().replace("\n", GeneralConstants.TEXT_SEPARATOR)

        return f"PointConnection({self.__point_hash}{GeneralConstants.TEXT_SEPARATOR}{docking_pnt_str})"


    @staticmethod
    def get_value(value_str: str) -> (PointConnection | list[PointConnection]):
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        if (value_str := value_str.split("(", 1)[-1].rstrip(")")) == GeneralConstants.EMPTY_LIST:
            return []

        if GeneralConstants.TEXT_SEPARATOR not in value_str:
            return PointConnection(AllplanIFW.DockingPoint())

        connection_point_str = value_str.split(GeneralConstants.TEXT_SEPARATOR, 1)[-1].replace(GeneralConstants.TEXT_SEPARATOR, "\n")

        docking_point = AllplanIFW.DockingPoint()

        docking_point.FromString(connection_point_str)

        return PointConnection(docking_point)


    def reset(self):
        """ reset the connection
        """

        self.__docking_point = AllplanIFW.DockingPoint()
        self.__point_hash    = ""


    def deep_copy(self) -> PointConnection:
        """ execute a deep copy

        Returns:
            copied object
        """

        return PointConnection(self.__docking_point)

```

</details>