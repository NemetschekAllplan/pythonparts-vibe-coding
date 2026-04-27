---
title: "ParameterConnection"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Data\ParameterConnection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ParameterConnection

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Data\ParameterConnection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `werte`

## Übersicht

implementation of the data class for the parameter connection data

## Abhängigkeiten

- `BaseConnection`
- `BuildingElementParameterListUtil`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`
- `Utilities.GeneralConstants`
- `__future__`
- `dataclasses`
- `hashlib`
- `typing`

## Klassen

### `ParameterConnection`

implementation of the data class for the parameter connection data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, connection_element: AllplanEleAdapter.BaseElementAdapter, parameters: list[str]` | `None` | initialize  Args:     connection_element: element     parameters:         parameters |
| `element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | get the element  Returns:     element |
| `element` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `None` | set the element  Args:     element: element |
| `to_string` | `self` | `str` | convert the value to a string  Returns:     list as string |
| `get_value` | `value_str: str` | `ParameterConnection` | get the value from a string  Args:     value_str: value string  Returns:     value |
| `deep_copy` | `self` | `ParameterConnection` | execute a deep copy  Returns:     copied object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the data class for the parameter connection data
"""

from __future__ import annotations

from typing import cast

from dataclasses import dataclass

import hashlib

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from BuildingElementParameterListUtil import BuildingElementParameterListUtil
from DocumentManager import DocumentManager

from Utilities.GeneralConstants import GeneralConstants

from .BaseConnection import BaseConnection

@dataclass
class ParameterConnection(BaseConnection):
    """ implementation of the data class for the parameter connection data
    """

    def __init__(self,
                 connection_element: AllplanEleAdapter.BaseElementAdapter,
                 parameters        : list[str]):
        """ initialize

        Args:
            connection_element: element
            parameters:         parameters
        """

        self.__element        : AllplanEleAdapter.BaseElementAdapter
        self.__uuid           : AllplanEleAdapter.GUID
        self.__parameter_hash : str

        self.__parameters = parameters
        self.element      = connection_element


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

        if element.IsNull():
            self.__uuid           = AllplanEleAdapter.GUID()
            self.__parameter_hash = ""

            return


        #----------------- set the connection data

        self.__uuid = element.GetModelElementUUID()

        _, _, pyp_parameters = AllplanBaseEle.PythonPartService.GetParameter(element)

        param_str = ""

        for param in self.__parameters:
            if param == GeneralConstants.PLACEMENT_MATRIX_KEY:
                param_str += str(AllplanBaseEle.PythonPartService.GetPlacementMatrix(element)).replace(" ", "").replace("\n", "")

            else:
                param_str += cast(str, BuildingElementParameterListUtil.get_value_string(pyp_parameters, param))

        self.__parameter_hash = hashlib.sha224(param_str.encode('utf-8')).hexdigest()


    def to_string(self) -> str:
        """ convert the value to a string

        Returns:
            list as string
        """

        return f"ParameterConnection({','.join(self.__parameters)}{GeneralConstants.TEXT_SEPARATOR}{self.__uuid}" \
               f"{GeneralConstants.TEXT_SEPARATOR}{self.__parameter_hash})"


    @staticmethod
    def get_value(value_str: str) -> ParameterConnection:
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        value_str = value_str.split("(", 1)[-1].rstrip(")")

        if GeneralConstants.TEXT_SEPARATOR not in value_str:
            return ParameterConnection(AllplanEleAdapter.BaseElementAdapter(),
                                      [item.strip() for item in value_str.split(",")])

        parts = value_str.split(GeneralConstants.TEXT_SEPARATOR)

        uuid = AllplanEleAdapter.GUID.FromString(parts[1])

        connection = ParameterConnection(AllplanEleAdapter.BaseElementAdapter.FromGUID(uuid, DocumentManager.get_instance().document),
                                         [item.strip() for item in parts[0].split(",")])

        return connection


    def deep_copy(self) -> ParameterConnection:
        """ execute a deep copy

        Returns:
            copied object
        """

        connection = ParameterConnection(self.__element, self.__parameters)

        return connection

```

</details>