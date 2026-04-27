---
title: "ComboBoxValueListUtil"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ComboBoxValueListUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ComboBoxValueListUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ComboBoxValueListUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the value list utility of the combo box

## Abhängigkeiten

- `BuildingElementStringTable`
- `NemAll_Python_AllplanSettings`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `__future__`
- `codecs`
- `pathlib`
- `typing`

## Klassen

### `ComboBoxValueListUtil`

implementation of the value list utility of the combo box
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, value_list_path: str, value_list: str, value_type: ParameterPropertyValueType` | `None` | initialize  Args:     value_list_path: value list path     value_list:      value list     value_type:      value type |
| `write_value_list` | `self` | `None` | write the value list to the file          |
| `update` | `self, value: Any` | `bool` | update the value list  Args:     value: value  Returns:     update state |
| `delete_item` | `self, value: Any` | `bool` | delete the value from the list  Args:     value: value  Returns:     delete state |
| `get_first_item` | `self` | `Any | None` | get the first list item  Returns:     first list item |
| `get_value_list` | `self` | `str` | get the value list  Returns:     value list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the value list utility of the combo box
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import codecs
import pathlib

import NemAll_Python_AllplanSettings as AllplanSettings

if TYPE_CHECKING:
    from BuildingElementStringTable import BuildingElementStringTable
    from ParameterProperty import ParameterProperty

    from ..ParameterPropertyValueType import ParameterPropertyValueType

class ComboBoxValueListUtil():
    """ implementation of the value list utility of the combo box
    """

    def __init__(self,
                 value_list_path: str,
                 value_list     : str,
                 value_type     : ParameterPropertyValueType):
        """ initialize

        Args:
            value_list_path: value list path
            value_list:      value list
            value_type:      value type
        """

        self.__value_list = [value_type.get_value(value_str) for value_str in value_list.split("|")]

        match value_list_path[:3]:
            case "usr":
                self.__value_list_path = AllplanSettings.AllplanPaths.GetUsrPath() + value_list_path[4:]

            case "std":
                self.__value_list_path = AllplanSettings.AllplanPaths.GetStdPath() + value_list_path[4:]

            case "prj":
                self.__value_list_path = AllplanSettings.AllplanPaths.GetCurPrjPath() + value_list_path[4:]

            case _:
                self.value_list_path = value_list_path


        #----------------- check the path and read the data

        pathlib.Path(self.__value_list_path).parent.mkdir(parents = True, exist_ok = True)

        if not pathlib.Path(self.__value_list_path).exists():
            return

        with codecs.open(self.__value_list_path, 'r', encoding = 'utf8') as file:
            items = file.readlines()

            self.__value_list = []

            self.__value_list = [value_type.get_value(value_str.rstrip()) for value_str in items]


    def write_value_list(self):
        """ write the value list to the file
        """

        with codecs.open(self.__value_list_path, 'w', encoding = 'utf8') as file:
            for item in self.__value_list:
                file.write(str(item))
                file.write("\n")


    def update(self,
               value: Any) -> bool:
        """ update the value list

        Args:
            value: value

        Returns:
            update state
        """

        if isinstance(value, list):
            modified = False

            for item in value:
                modified |= self.update(item)

            return modified


        #----------------- single value

        if value in self.__value_list:
            return False

        self.__value_list.append(value)
        self.__value_list.sort()

        self.write_value_list()

        return True


    def delete_item(self,
                    value: Any) -> bool:
        """ delete the value from the list

        Args:
            value: value

        Returns:
            delete state
        """

        if value not in self.__value_list:
            return False

        del self.__value_list[self.__value_list.index(value)]

        self.write_value_list()

        return True


    def get_first_item(self) -> (Any | None):
        """ get the first list item

        Returns:
            first list item
        """

        return self.__value_list[0] if self.__value_list else None


    def get_value_list(self) -> str:
        """ get the value list

        Returns:
            value list
        """

        return "|".join(str(value) for value in self.__value_list)

```

</details>