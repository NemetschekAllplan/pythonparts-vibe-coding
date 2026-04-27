---
title: "BuildingElementMaterialStringTable"
source: "PythonPartsFramework\GeneralScripts\BuildingElementMaterialStringTable.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementMaterialStringTable

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementMaterialStringTable.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Script for BuildingElementMaterialStringTable

## Abhängigkeiten

- `BuildingElementStringTableBase`
- `typing`

## Klassen

### `BuildingElementMaterialStringTable`

Definition of class MaterialStringTable
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, path: str, numeric: bool, lang: str` | `None` | Initialization of class StringTable  Args:     path:    path of according .py file. The file name will be set internally to _xyz.xml     numeric: the string table will be created only from numeric (123..) text ids or not numeric text ids (e_THE_VALUE)     lang:    language short cut |
| `get_entry` | `self, str_val_number: str` | `Tuple[str, bool]` | Returns an string table entry  Args:     str_val_number: value or number of the string  Returns:     (string result, True/False for success) |
| `add_entry` | `self, val_number: str, val_str: str` | `bool` | Creates an string table entry  Args:     val_number: index number in the list     val_str:    string value  Returns:     True for success     False if number already exists |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementMaterialStringTable
"""

from typing import Tuple

from BuildingElementStringTableBase import BuildingElementStringTableBase


class BuildingElementMaterialStringTable(BuildingElementStringTableBase):
    """ Definition of class MaterialStringTable
    """

    MATERIAL_EXT = "mat_"

    def __init__(self,
                 path   : str,
                 numeric: bool,
                 lang   : str):
        """ Initialization of class StringTable

        Args:
            path:    path of according .py file. The file name will be set internally to _xyz.xml
            numeric: the string table will be created only from numeric (123..) text ids or not numeric text ids (e_THE_VALUE)
            lang:    language short cut
        """

        super().__init__(path, numeric, lang)

        if not path:
            return


        #----------------- Create the string table

        if not self._get_path_from_lang():
            return

        self._read_file("Read material stringtable: ", self._path)


    def get_entry(self,
                  str_val_number: str) -> Tuple[str, bool]:
        """ Returns an string table entry

        Args:
            str_val_number: value or number of the string

        Returns:
            (string result, True/False for success)
        """

        if not self.is_valid():
            self._trace_message("material stringtable is not valid: " + self._path)

            return str_val_number, False

        if (str_val_number := str.lower(str_val_number)) in self.str_table:
            return self.str_table[str_val_number], True

        if str_val_number and str_val_number != BuildingElementMaterialStringTable.MATERIAL_EXT:
            self._trace_message("mat_" + str_val_number + " was not found in stringtable: " + self._path)

        return str_val_number, False


    def add_entry(self,
                  val_number: str,
                  val_str   : str) -> bool:
        """ Creates an string table entry

        Args:
            val_number: index number in the list
            val_str:    string value

        Returns:
            True for success
            False if number already exists
        """

        if self._is_numeric:
            print("Only non numeric material string are valid")
            return False

        val_number = str.lower(val_number)

        if not val_number.startswith(BuildingElementMaterialStringTable.MATERIAL_EXT):
            self._trace_message("BuildingElementMaterialStringtable.py Value for text id not valid."\
                                " It has to start with a lowercase ""mat_"" " \
                                "\\nCurrent value TextId = " + val_number)

            return False

        if val_number in self.str_table:
            self._trace_message('BuildingElementMaterialStringTable, add_entry: text id ' + str(val_number) + ' allready exists')
            return False

        self.str_table[val_number] = val_str

        return True

```

</details>