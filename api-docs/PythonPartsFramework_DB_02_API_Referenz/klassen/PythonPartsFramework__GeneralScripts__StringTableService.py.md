---
title: "StringTableService"
source: "PythonPartsFramework\GeneralScripts\StringTableService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# StringTableService

> **Pfad:** `PythonPartsFramework\GeneralScripts\StringTableService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the string table service

## Abhängigkeiten

- `BuildingElementMaterialStringTable`
- `BuildingElementStringTable`
- `NemAll_Python_AllplanSettings`

## Klassen

### `StringTableService`

Definition of class StringTableService

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, path: str` | `None` | Initialize the data  Args:     path: Path to string table folder. |
| `get_string` | `self, string_id: str, string: str` | `str` | Get a string from the table  Returns:     String from the ID if exist, default string otherwise  Args:     string_id:  String ID (if empty, take it for {...} part of the string     string:     Default string in case of no existing ID |
| `get_string_table_entry` | `string_table: BuildingElementStringTable, string_id: str, string: str` | `str` | Get a string from the table  Returns:     String from the ID if exist, default string otherwise  Args:     string_table: string table     string_id:    String ID (if empty, take it for {...} part of the string     string:       Default string in case of no existing ID |
| `str_table` | `self` | `BuildingElementStringTable` | get the string table  Returns:     string table |
| `material_str_table` | `self` | `BuildingElementMaterialStringTable` | get the material string table  Returns:     material string table |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Implementation of the string table service
"""

from BuildingElementStringTable import BuildingElementStringTable
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable

import NemAll_Python_AllplanSettings as AllplanSettings

class StringTableService:
    """
    Definition of class StringTableService
    """

    def __init__(self,
                 path: str):
        """
        Initialize the data

        Args:
            path: Path to string table folder.
        """

        path_strtable = path + '\\Stringtable\\BuildingElement.py'

        language = AllplanSettings.AllplanLocalisationService.AllplanLanguage()


        # create string table from non numeric ids

        self.__str_table = BuildingElementStringTable(path_strtable, False, language)

        self.has_str_table = self.__str_table.is_valid()

        path_strtable = path + '\\Stringtable\\BuildingElementMaterial.py'


        # for materials there is only the global string table
        # create string table from non numeric ids beginning with mat_

        self.__material_str_table = BuildingElementMaterialStringTable(path_strtable, False, language)


    def get_string(self,
                   string_id: str,
                   string   : str) -> str:
        """
        Get a string from the table

        Returns:
            String from the ID if exist, default string otherwise

        Args:
            string_id:  String ID (if empty, take it for {...} part of the string
            string:     Default string in case of no existing ID
        """

        if self.has_str_table is True:
            return self.get_string_table_entry(self.__str_table, string_id, string)

        return string


    @staticmethod
    def get_string_table_entry(string_table: BuildingElementStringTable,
                               string_id   : str,
                               string      : str) -> str:
        """
        Get a string from the table

        Returns:
            String from the ID if exist, default string otherwise

        Args:
            string_table: string table
            string_id:    String ID (if empty, take it for {...} part of the string
            string:       Default string in case of no existing ID
        """

        if not string_table:
            return string

        if not string_id:
            if not string:
                return ""

            if (ipb := string.rfind("{")) != -1:
                string_id = string[ipb + 1:].split("}")[0]
                string    = string[0: ipb].rstrip(" ")

        if not string_id:
            if string.isdigit():
                string_id = string
            else:
                return string

        str_tmp_res, res = string_table.get_entry(string_id)

        if res:
            return str_tmp_res

        return string

    @property
    def str_table(self) -> BuildingElementStringTable:
        """ get the string table

        Returns:
            string table
        """

        return self.__str_table

    @property
    def material_str_table(self) -> BuildingElementMaterialStringTable:
        """ get the material string table

        Returns:
            material string table
        """

        return self.__material_str_table

```

</details>