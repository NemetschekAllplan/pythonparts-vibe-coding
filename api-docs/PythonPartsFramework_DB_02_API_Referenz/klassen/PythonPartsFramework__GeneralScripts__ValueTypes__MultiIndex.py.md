---
title: "MultiIndex"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\MultiIndex.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# MultiIndex

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\MultiIndex.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the multi index

## Abhängigkeiten

- `Utilities.GeneralConstants`
- `__future__`
- `collections.abc`
- `typing`

## Klassen

### `MultiIndex`

" implementation of the multi index
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, indexes: str | int` | `None` | create the index list  Args:     indexes: indexes |
| `__iter__` | `self` | `Generator[tuple[int, int], Any, Any]` | get the data frame iterator  Yields:     multi index |
| `__getitem__` | `self, key: int | slice` | `tuple[int, int] | list[tuple[int, int]]` | get the item  Args:     key:  item key  Returns:     item(s) |
| `__setitem__` | `self, index: int, value: tuple[int, int]` | `None` | set the item  Args:     index: index     value: value |
| `get_indexes` | `self, as_list_index: bool` | `str` | get the indexes as string like 1,3-4  Args:     as_list_index: create the index as list index (0 based)  Returns:     index string |
| `__len__` | `self` | `int` | get the index section count  Returns:     index section count |
| `__repr__` | `self` | `str` | convert to string  Returns:     value string |
| `__index__` | `self` | `int` | Determines integer value to use, when object is used as an index in a list  Returns:     minimal integer value inside self.__multi_index |
| `deep_copy` | `self` | `MultiIndex` | execute a deep copy  Returns:     copied object |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the multi index
"""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from Utilities.GeneralConstants import GeneralConstants


class MultiIndex():
    """" implementation of the multi index
    """

    def __init__(self,
                 indexes: (str | int)):
        """ create the index list

        Args:
            indexes: indexes
        """

        self.__multi_index = []

        if isinstance(indexes, int):
            indexes = str(indexes)

        for index in indexes.split(GeneralConstants.MULTI_INDEX_SINGLE_SEPARATOR):
            left, _, right = index.partition(GeneralConstants.MULTI_INDEX_RANGE_SEPARATOR)

            if (right := right.strip()):
                left_index  = int(left.strip())

                if (right_index := int(right)) < left_index:
                    left_index, right_index = right_index, left_index

                self.__multi_index.append((left_index, right_index))
            else:
                single_index = int(left.strip())

                self.__multi_index.append((single_index, single_index))


    def __iter__(self) -> Generator[(tuple[int, int]), Any, Any]:
        """ get the data frame iterator

        Yields:
            multi index

        """

        yield from self.__multi_index


    def __getitem__(self,
                    key : (int | slice)) -> (tuple[int, int] | list[tuple[int, int]]):
        """ get the item

        Args:
            key:  item key

        Returns:
            item(s)
        """

        return self.__multi_index[key]


    def __setitem__(self,
                    index: int,
                    value: tuple [int, int]):
        """ set the item

        Args:
            index: index
            value: value
        """
        self.__multi_index[index] = value


    def get_indexes(self,
                    as_list_index: bool) -> str:
        """ get the indexes as string like 1,3-4

        Args:
            as_list_index: create the index as list index (0 based)

        Returns:
            index string
        """

        indexes = ""

        diff = int(as_list_index)

        for index_from, index_to in self.__multi_index:
            if index_from == index_to:
                indexes += f"{index_from - diff}{GeneralConstants.MULTI_INDEX_SINGLE_SEPARATOR}"
            else:
                indexes += \
                    f"{index_from - diff}{GeneralConstants.MULTI_INDEX_RANGE_SEPARATOR}{index_to - diff}" \
                    f"{GeneralConstants.MULTI_INDEX_SINGLE_SEPARATOR}"

        return indexes.rstrip(GeneralConstants.MULTI_INDEX_SINGLE_SEPARATOR)


    def __len__(self) -> int:
        """ get the index section count

        Returns:
            index section count
        """

        return len(self.__multi_index)


    def __repr__(self) -> str:
        """ convert to string

        Returns:
            value string
        """

        return str(self.__multi_index)


    def __index__(self) -> int:
        """ Determines integer value to use, when object is used as an index in a list

        Returns:
            minimal integer value inside self.__multi_index
        """

        return min(min(numbers) for numbers in self.__multi_index) - 1


    def deep_copy(self) -> MultiIndex:
        """ execute a deep copy

        Returns:
            copied object
        """

        return MultiIndex(self.get_indexes(False))

```

</details>