---
title: "BuildingElementStringTableManager"
source: "PythonPartsFramework\GeneralScripts\BuildingElementStringTableManager.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementStringTableManager

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementStringTableManager.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Script for BuildingElementStringTableManager functions

## Abhängigkeiten

- `__future__`
- `typing`

## Klassen

### `BuildingElementStringTableManager`

Singleton class for the string table manager 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize  Raises:     PermissionError: raised in case of multiple init |
| `get_instance` | `-` | `BuildingElementStringTableManager` | Get the one an only instance for the string table manager  Returns:     building element string table manager |
| `get_global_string_table` | `self, path: str` | `dict[str, str] | None` | Get the global string table  Args:     path: path of the string table  Returns:     string table |
| `add_string_table` | `self, path: str, str_table: dict[str, str]` | `None` | Add a string table to the global string table  Args:     path:      path of the string table     str_table: string table |
| `clear_global_string_table` | `self` | `None` | Clear the global string table          |
| `set_use_global_string_table` | `self, use_global_table: bool` | `None` | Set the state of the global string table usage  Args:     use_global_table: use the global string table True/False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementStringTableManager functions
"""

# pylint: disable=unused-private-member

from __future__ import annotations

from typing import cast

class BuildingElementStringTableManager():
    """ Singleton class for the string table manager """

    __instance = None


    def __init__(self):
        """ initialize

        Raises:
            PermissionError: raised in case of multiple init
        """

        if BuildingElementStringTableManager.__instance is not None:
            raise PermissionError("BuildingElementStringTableManager is a singleton")

        BuildingElementStringTableManager.__instance = self

        self.__use_global_string_table = True
        self.__global_string_table     : dict[str, dict[str, str]] = {}


    @staticmethod
    def get_instance() -> BuildingElementStringTableManager:
        """ Get the one an only instance for the string table manager

        Returns:
            building element string table manager
        """

        if BuildingElementStringTableManager.__instance is None:
            BuildingElementStringTableManager()

        return cast(BuildingElementStringTableManager, BuildingElementStringTableManager.__instance)


    def get_global_string_table(self,
                                path: str) -> (dict[str, str] | None):
        """ Get the global string table

        Args:
            path: path of the string table

        Returns:
            string table
        """

        if not self.__use_global_string_table:
            return None

        if path in self.__global_string_table:
            return self.__global_string_table[path]

        return None


    def add_string_table(self,
                         path     : str,
                         str_table: dict[str, str]):
        """ Add a string table to the global string table

        Args:
            path:      path of the string table
            str_table: string table
        """

        if self.__use_global_string_table:
            self.__global_string_table[path] = str_table


    def clear_global_string_table(self):
        """ Clear the global string table
        """

        self.__global_string_table.clear()


    def set_use_global_string_table(self,
                                    use_global_table: bool):
        """ Set the state of the global string table usage

        Args:
            use_global_table: use the global string table True/False
        """

        self.__use_global_string_table = use_global_table

```

</details>