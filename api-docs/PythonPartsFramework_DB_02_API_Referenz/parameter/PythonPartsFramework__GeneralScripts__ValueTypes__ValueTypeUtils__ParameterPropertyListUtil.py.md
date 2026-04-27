---
title: "ParameterPropertyListUtil"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ParameterPropertyListUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ParameterPropertyListUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ParameterPropertyListUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `utility`, `werte`

## Übersicht

implementation of the parameter property list utilities

## Abhängigkeiten

- `MultiIndex`
- `NemAll_Python_Geometry`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `__future__`
- `collections.abc`
- `typing`

## Klassen

### `ParameterPropertyListUtil`

implementation of the parameter property list utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_list_index_2dim` | `name: str` | `tuple[int, int] | None` | get the list index  Args:     name: name of the modified property  Returns:     list index, None if not exist |
| `get_list_index` | `name: str` | `int | None` | get the list index  Args:     name: name of the modified property  Returns:     list index, None if not exist |
| `get_item_value` | `prop: ParameterProperty, name: str` | `Any` | get the value for the item defined in the name  Args:     prop: parameter property     name: name of the modified property  Returns:     parameter property |
| `set_item_value` | `prop: ParameterProperty, name: str, value: Any, get_value: Callable[[str], Any] | None=None` | `bool` | Set the value of the item defined in the name  Args:     prop:      property     name:      name of the modified property     value:     new value     get_value: string to value convertor  Returns:     update palette state |
| `__get_tuple_indexes` | `name: str` | `list[int]` | get the tuple indexes  Args:     name: name of the modified property  Returns:     tuple indexes |
| `get_tuple_list_indexes` | `name: str` | `tuple[int, list[int]]` | get the tuple indexes from a name like Width[2](0)  Args:     name: name of the modified property  Returns:     tuple(row index, tuple index), row index = -1 if not exist |
| `set_sub_item_value` | `items: Any, sub_item_name: str, value: Any` | `Any` | set the sub item value  Args:     items:         items     sub_item_name: sub item name     value:         new value  Returns:     modified value |
| `set_sub_item_angle_value` | `items: Any, sub_item_name: str, value: Any` | `Any` | set the sub item angle value  Args:     items:         items     sub_item_name: sub item name     value:         new value  Returns:     modified value |
| `get_multiple_list_index` | `name: str` | `MultiIndex | None` | get the multiple list index  Args:     name: name of the modified property  Returns:     multiple list indexes, None if not exist |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the parameter property list utilities
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from collections.abc import Callable

import NemAll_Python_Geometry as AllplanGeo

from Utilities.GeneralConstants import GeneralConstants

from ..MultiIndex import MultiIndex

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty


class ParameterPropertyListUtil():
    """ implementation of the parameter property list utilities
    """

    @staticmethod
    def get_list_index_2dim(name: str) -> (tuple[int, int] | None):
        """ get the list index

        Args:
            name: name of the modified property

        Returns:
            list index, None if not exist
        """

        if (separator := name.find(GeneralConstants.LIST_SEPARATOR_2_DIM)) == -1:
            return None

        return int(name[:separator].split(GeneralConstants.LIST_SEPARATOR_START)[-1]. \
                                    split(GeneralConstants.LIST_SEPARATOR_END)[0]),   \
               int(name[separator:].split(GeneralConstants.LIST_SEPARATOR_START)[-1]. \
                                    split(GeneralConstants.LIST_SEPARATOR_END)[0])

    @staticmethod
    def get_list_index(name: str) -> (int | None):
        """ get the list index

        Args:
            name: name of the modified property

        Returns:
            list index, None if not exist
        """

        if GeneralConstants.LIST_SEPARATOR_START not in name:
            return None

        return int(name.split(GeneralConstants.LIST_SEPARATOR_START)[-1]. \
                        split(GeneralConstants.LIST_SEPARATOR_END)[0])


    @staticmethod
    def get_item_value(prop: ParameterProperty,
                       name: str) -> Any:
        """ get the value for the item defined in the name

        Args:
            prop: parameter property
            name: name of the modified property

        Returns:
            parameter property
        """

        if (index_2d := ParameterPropertyListUtil.get_list_index_2dim(name)) is not None:
            return prop.value[index_2d[0]][index_2d[1]]

        if (list_index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            return prop.value[list_index]

        return prop.value


    @staticmethod
    def set_item_value(prop     : ParameterProperty,
                       name     : str,
                       value    : Any,
                       get_value: (Callable[[str], Any] | None) = None) -> bool:
        """ Set the value of the item defined in the name

        Args:
            prop:      property
            name:      name of the modified property
            value:     new value
            get_value: string to value convertor

        Returns:
            update palette state
        """

        if (multi_index := ParameterPropertyListUtil.get_multiple_list_index(name)) is not None:
            if isinstance(value, str) and get_value is not None:
                value = get_value(value)

            for index_from, index_to in multi_index:
                for index in range(index_from, index_to + 1):
                    prop.value[index] = value

            prop.is_modified = True

            return True

        if (index_2d := ParameterPropertyListUtil.get_list_index_2dim(name)) is not None:
            prop.value[index_2d[0]][index_2d[1]] = value

            return False

        if (list_index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            if (count := list_index - len(prop.value)) >= 0:
                prop.value += [None] * (count + 1)

            prop.value[list_index] = value

            return False

        prop.value = value

        return False


    @staticmethod
    def __get_tuple_indexes(name: str) -> list[int]:
        """ get the tuple indexes

        Args:
            name: name of the modified property

        Returns:
            tuple indexes
        """

        parts = name.split(GeneralConstants.TUPLE_SEPARATOR_START)[1:]

        return [int(part.split(GeneralConstants.TUPLE_SEPARATOR_END)[0]) for part in parts]


    @staticmethod
    def get_tuple_list_indexes(name: str) -> tuple[int, list[int]]:
        """ get the tuple indexes from a name like Width[2](0)

        Args:
            name: name of the modified property

        Returns:
            tuple(row index, tuple index), row index = -1 if not exist
        """

        list_index = ParameterPropertyListUtil.get_list_index(name)

        return list_index if list_index is not None else -1, \
               ParameterPropertyListUtil.__get_tuple_indexes(name)


    @staticmethod
    def set_sub_item_value(items        : Any,
                           sub_item_name: str,
                           value        : Any) -> Any:
        """ set the sub item value

        Args:
            items:         items
            sub_item_name: sub item name
            value:         new value

        Returns:
            modified value
        """

        if isinstance(items, list):
            for item in items:
                setattr(item, sub_item_name, value)

        else:
            setattr(items, sub_item_name, value)

        return items


    @staticmethod
    def set_sub_item_angle_value(items        : Any,
                                 sub_item_name: str,
                                 value        : Any) -> Any:
        """ set the sub item angle value

        Args:
            items:         items
            sub_item_name: sub item name
            value:         new value

        Returns:
            modified value
        """

        angle     = AllplanGeo.Angle()
        angle.Deg = value

        return ParameterPropertyListUtil.set_sub_item_value(items, sub_item_name, angle)


    @staticmethod
    def get_multiple_list_index(name: str) -> (MultiIndex | None):
        """ get the multiple list index

        Args:
            name: name of the modified property

        Returns:
            multiple list indexes, None if not exist
        """

        if GeneralConstants.MULTI_INDEX_RANGE_SEPARATOR  not in name and \
           GeneralConstants.MULTI_INDEX_SINGLE_SEPARATOR not in name:
            return None

        return MultiIndex(name.split(GeneralConstants.LIST_SEPARATOR_START, 1)[-1]. \
                               split(GeneralConstants.LIST_SEPARATOR_END, 1)[0])

```

</details>