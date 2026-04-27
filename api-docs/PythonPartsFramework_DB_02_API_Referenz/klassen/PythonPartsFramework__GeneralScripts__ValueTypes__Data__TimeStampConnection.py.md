---
title: "TimeStampConnection"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Data\TimeStampConnection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# TimeStampConnection

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Data\TimeStampConnection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the data class for the time stamp connection data

## Abhängigkeiten

- `BaseConnection`
- `DocumentManager`
- `NemAll_Python_IFW_ElementAdapter`
- `Utilities.GeneralConstants`
- `__future__`
- `dataclasses`
- `typing`

## Klassen

### `TimeStampConnection`

implementation of the data class for the time stamp connection data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, connection_element: AllplanEleAdapter.BaseElementAdapter, time_stamp: int=0` | `None` | initialize  Args:     connection_element: element     time_stamp:         time stamp |
| `element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | get the element  Returns:     element |
| `element` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `None` | set the element  Args:     element: element |
| `to_string` | `self` | `str` | convert the value to a string  Returns:     list as string |
| `get_value` | `value_str: str` | `TimeStampConnection | list[TimeStampConnection]` | get the value from a string  Args:     value_str: value string  Returns:     value |
| `is_element_modified` | `self` | `bool` | get the element modification status  Returns:     True, when the element has been modified |
| `deep_copy` | `self` | `TimeStampConnection` | execute a deep copy  Returns:     copied object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the data class for the time stamp connection data
"""

from __future__ import annotations

from typing import cast

from dataclasses import dataclass

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from DocumentManager import DocumentManager

from Utilities.GeneralConstants import GeneralConstants

from .BaseConnection import BaseConnection

@dataclass
class TimeStampConnection(BaseConnection):
    """ implementation of the data class for the time stamp connection data
    """

    __element             : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()
    uuid                  : AllplanEleAdapter.GUID               = AllplanEleAdapter.GUID()
    time_stamp            : int                                  = 0

    __is_element_modified = False
    __org_element_uuid    = ""                                         # original element UUID, used for the copy operation


    def __init__(self,
                 connection_element: AllplanEleAdapter.BaseElementAdapter,
                 time_stamp        : int = 0):
        """ initialize

        Args:
            connection_element: element
            time_stamp:         time stamp
        """

        self.time_stamp = time_stamp
        self.element    = connection_element


    @property
    def element(self) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the element

        Returns:
            element
        """

        return self.__element


    @element.setter
    def element(self,
                element: AllplanEleAdapter.BaseElementAdapter):
        """ set the element

        Args:
            element: element
        """

        self.__element = element

        if element.IsValid():
            time_stamp = element.GetTimeStamp()

            self.__is_element_modified = time_stamp != self.time_stamp
            self.uuid                  = element.GetModelElementUUID()
            self.time_stamp            = time_stamp
        else:
            self.uuid                  = AllplanEleAdapter.GUID()
            self.time_stamp            = 0
            self.__is_element_modified = False


    def to_string(self) -> str:
        """ convert the value to a string

        Returns:
            list as string
        """

        return f"TimeStampConnection({self.uuid}{GeneralConstants.TEXT_SEPARATOR}{self.time_stamp})"


    @staticmethod
    def get_value(value_str: str) -> (TimeStampConnection | list[TimeStampConnection]):
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        if (value_str := value_str.split("(", 1)[-1].rstrip(")")) == GeneralConstants.EMPTY_LIST:
            return []

        if not (value_str := value_str.replace("(",  "").replace(")", "")):
            return TimeStampConnection(AllplanEleAdapter.BaseElementAdapter())


        #----------------- single connection

        if GeneralConstants.LIST_ITEM_SEPARATOR not in value_str:
            parts = value_str.split(GeneralConstants.TEXT_SEPARATOR)

            if not parts[0]:
                return TimeStampConnection(AllplanEleAdapter.BaseElementAdapter())

            uuid       = AllplanEleAdapter.GUID.FromString(parts[0])
            time_stamp = int(parts[1]) if parts[1] else 0

            connection = TimeStampConnection(AllplanEleAdapter.BaseElementAdapter.FromGUID(uuid, DocumentManager.get_instance().document),
                                             time_stamp)

            return connection


        #----------------- split the string and check for deleted elements

        connections = list[TimeStampConnection]()

        for item in value_str.split(";"):
            connection = cast(TimeStampConnection, TimeStampConnection.get_value(item))

            if not connection.element.IsNull():
                connections.append(connection)

        return connections


    @property
    def is_element_modified(self) -> bool:
        """ get the element modification status

        Returns:
            True, when the element has been modified
        """

        return self.__is_element_modified


    def deep_copy(self) -> TimeStampConnection:
        """ execute a deep copy

        Returns:
            copied object
        """

        connection = TimeStampConnection(self.__element, self.time_stamp)

        return connection

```

</details>