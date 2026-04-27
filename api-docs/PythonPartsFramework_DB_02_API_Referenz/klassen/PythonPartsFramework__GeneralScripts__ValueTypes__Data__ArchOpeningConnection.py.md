---
title: "ArchOpeningConnection"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Data\ArchOpeningConnection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ArchOpeningConnection

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Data\ArchOpeningConnection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the data class for the architecture opening connection data

## Abhängigkeiten

- `BaseConnection`
- `DocumentManager`
- `NemAll_Python_IFW_ElementAdapter`
- `Utilities.GeneralConstants`
- `__future__`
- `dataclasses`

## Klassen

### `ArchOpeningConnection`

implementation of the data class for the architecture opening connection data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, element: AllplanEleAdapter.BaseElementAdapter, placement_segment_index: int, left_aligned: bool` | `None` | initialize  Args:     element:                 opening element     placement_segment_index: placement segment index     left_aligned:            left aligned |
| `element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | get the opening_element  Returns:     opening_element |
| `element` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `None` | set the opening_element  Args:     element: opening element |
| `placement_segment_index` | `self` | `int` | get the placement segment index  Returns:     placement segment index |
| `left_aligned` | `self` | `bool` | get the left aligned flag  Returns:     left aligned flag |
| `get_connected_element_uuid` | `self` | `str` | get the connected element UUIDs  Returns:     connected elements |
| `to_string` | `self` | `str` | convert the value to a string  Returns:     list as string |
| `get_value` | `value_str: str` | `ArchOpeningConnection` | get the value from a string  Args:     value_str: value string  Returns:     architecture opening connection |
| `is_valid` | `self` | `bool` | check if the element is valid  Returns:     True if valid, False otherwise |
| `deep_copy` | `self` | `ArchOpeningConnection` | execute a deep copy  Returns:     copied object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the data class for the architecture opening connection data
"""

from __future__ import annotations

from dataclasses import dataclass

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from DocumentManager import DocumentManager

from Utilities.GeneralConstants import GeneralConstants

from .BaseConnection import BaseConnection

@dataclass
class ArchOpeningConnection(BaseConnection):
    """ implementation of the data class for the architecture opening connection data
    """

    def __init__(self,
                 element                : AllplanEleAdapter.BaseElementAdapter,
                 placement_segment_index: int,
                 left_aligned           : bool):
        """ initialize

        Args:
            element:                 opening element
            placement_segment_index: placement segment index
            left_aligned:            left aligned
        """

        self.__element    : AllplanEleAdapter.BaseElementAdapter
        self.__time_stamp : int
        self.__uuid       : AllplanEleAdapter.GUID

        self.element = element

        self.__placement_segment_index = placement_segment_index
        self.__left_aligned            = left_aligned


    @property
    def element(self) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the opening_element

        Returns:
            opening_element
        """

        return self.__element


    @element.setter
    def element(self,
                element: AllplanEleAdapter.BaseElementAdapter):
        """ set the opening_element

        Args:
            element: opening element
        """

        self.__element = element

        if element.IsValid():
            self.__uuid       = element.GetModelElementUUID()
            self.__time_stamp = element.GetTimeStamp()
        else:
            self.__uuid       = AllplanEleAdapter.GUID()
            self.__time_stamp = 0


    @property
    def placement_segment_index(self) -> int:
        """ get the placement segment index

        Returns:
            placement segment index
        """

        return self.__placement_segment_index


    @property
    def left_aligned(self) -> bool:
        """ get the left aligned flag

        Returns:
            left aligned flag
        """

        return self.__left_aligned


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

        return f"ArchOpeningConnection({self.__uuid}{GeneralConstants.TEXT_SEPARATOR}{self.__time_stamp}" \
               f"{GeneralConstants.TEXT_SEPARATOR}{self.__placement_segment_index}" \
               f"{GeneralConstants.TEXT_SEPARATOR}{self.__left_aligned})"


    @staticmethod
    def get_value(value_str: str) -> ArchOpeningConnection:
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            architecture opening connection
        """

        value_str = value_str.split("(", 1)[-1].rstrip(")")

        if value_str == GeneralConstants.EMPTY_LIST or not value_str:
            return ArchOpeningConnection(AllplanEleAdapter.BaseElementAdapter(), -1, True)

        parts = value_str.split(GeneralConstants.TEXT_SEPARATOR)

        uuid = AllplanEleAdapter.GUID.FromString(parts[0])

        return ArchOpeningConnection(AllplanEleAdapter.BaseElementAdapter.FromGUID(uuid, DocumentManager.get_instance().document), \
                                     int(parts[2]), bool(parts[3]))


    def is_valid(self) -> bool:
        """ check if the element is valid

        Returns:
            True if valid, False otherwise
        """

        return not self.__element.IsNull()


    def deep_copy(self) -> ArchOpeningConnection:
        """ execute a deep copy

        Returns:
            copied object
        """

        connection = ArchOpeningConnection(self.__element, self.__placement_segment_index, self.__left_aligned)

        return connection

```

</details>