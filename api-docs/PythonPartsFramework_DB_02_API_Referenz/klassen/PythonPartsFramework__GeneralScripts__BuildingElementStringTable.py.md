---
title: "BuildingElementStringTable"
source: "PythonPartsFramework\GeneralScripts\BuildingElementStringTable.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementStringTable

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementStringTable.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Script for BuildingElementStringTable

## Abhängigkeiten

- `BuildingElementStringTableBase`
- `BuildingElementStringTableManager`
- `TraceService`
- `string`

## Klassen

### `BuildingElementStringTable`

Definition of class StringTable
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, path: str, numeric: bool, lang: str, force_lang_name: bool=False` | `None` | Initialization of class StringTable  Args:     path:    path of according .py file.              The file name will be set internally to _xyz.xml     numeric: the string table will be created only from              numeric (123..) text ids or              not numeric text ids (e_THE_VALUE)     lang:    language shortcut     force_lang_name: force global table with language specific key (useful when working with more language mutations at once) |
| `__is_ascii_underline_numbers` | `input_str: str` | `bool` | check if a string contains only ascii signs underlines and numbers  Args:     input_str: input string to check  Returns:     underline numbers: True/False |
| `get_entry` | `self, str_val_number: str | int` | `tuple[str, bool]` | Returns a string table entry  Args:     str_val_number: value or number of the string  Returns:     (string entry, True/False for success) |
| `get_string` | `self, string_id: str | int, default_string: str` | `str` | Get a string from the table  Args:     string_id:      String ID (if empty, take it from {...} part of the string     default_string: Default string in case of no existing ID  Returns:     String from the ID if exist, default string otherwise |
| `get_key` | `self, entry: str` | `str | None` | Returns the key for a string table entry  Args:     entry: entry to search corresponding key  Returns:     Key, None if not found |
| `add_entry` | `self, val_number: str, val_str: str` | `bool` | Creates an string table entry  Args:     val_number: index number in the list     val_str:    string value  Returns:     True for success     False if number already exists |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementStringTable
"""

import string

from BuildingElementStringTableManager import BuildingElementStringTableManager
from BuildingElementStringTableBase import BuildingElementStringTableBase
from TraceService import TraceService

MIN_TEXT_ID = 1000
MAX_TEXT_ID = 30000


class BuildingElementStringTable(BuildingElementStringTableBase):
    """ Definition of class StringTable
    """

    def __init__(self,
                 path   : str,
                 numeric: bool,
                 lang   : str,
                 force_lang_name: bool = False):
        """ Initialization of class StringTable

        Args:
            path:    path of according .py file.
                     The file name will be set internally to _xyz.xml
            numeric: the string table will be created only from
                     numeric (123..) text ids or
                     not numeric text ids (e_THE_VALUE)
            lang:    language shortcut
            force_lang_name: force global table with language specific key (useful when working with more language mutations at once)
        """

        super().__init__(path, numeric, lang)

        if not path:
            return

        lang_path = path[:path.rfind(".")]

        if force_lang_name:
            lang_path += '_' + lang

        if (str_table := BuildingElementStringTableManager.get_instance().get_global_string_table(lang_path)) is not None:
            self.str_table   = str_table
            self._m_is_valid = True

            return


        #----------------- Create the string table

        if not self._get_path_from_lang():
            TraceService().set_trace_missing_text_id(False)
            return

        TraceService().set_trace_missing_text_id(True)

        self._read_file("Read stringtable: ", self._path)

        BuildingElementStringTableManager.get_instance().add_string_table(lang_path, self.str_table)


    @staticmethod
    def __is_ascii_underline_numbers(input_str: str) -> bool:
        """ check if a string contains only ascii signs underlines and numbers

        Args:
            input_str: input string to check

        Returns:
            underline numbers: True/False
        """

        for char in input_str:
            if char not in string.ascii_letters:
                if char != '_' and not char.isnumeric():    # pylint: disable=magic-value-comparison
                    return False

                continue


            #------------- all signs have to be uppercase

            if char != str.upper(char):
                return False

        return True


    def get_entry(self,
                  str_val_number: (str | int)) -> tuple[str, bool]:
        """ Returns a string table entry

        Args:
            str_val_number: value or number of the string

        Returns:
            (string entry, True/False for success)
        """

        if not self.is_valid():
            self._trace_message("stringtable is not valid: " + self._path)

            return str(str_val_number), False

        if str_val_number in self.str_table:
            return self.str_table[str_val_number], True

        if isinstance(str_val_number, int):
            return self.get_entry(str(str_val_number))

        if str_val_number and str_val_number != "0":    # pylint: disable=magic-value-comparison
            self._trace_message("TextId: " + str_val_number + " was not found in stringtable: " + self._path)

        return str_val_number, False


    def get_string(self,
                   string_id     : (str | int),
                   default_string: str) -> str:
        """ Get a string from the table

        Args:
            string_id:      String ID (if empty, take it from {...} part of the string
            default_string: Default string in case of no existing ID

        Returns:
            String from the ID if exist, default string otherwise
        """

        entry, exist = self.get_entry(string_id)

        return entry if exist else default_string


    def get_key(self,
                entry: str) -> (str | None):
        """ Returns the key for a string table entry

        Args:
            entry: entry to search corresponding key

        Returns:
            Key, None if not found
        """

        if not self.is_valid():
            self._trace_message("stringtable is not valid: " + self._path)

            return None

        return next((key for key, value in self.str_table.items() if value == entry), None)


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
            if int(val_number) < int(MIN_TEXT_ID) or int(val_number) >= int(MAX_TEXT_ID):
                self._trace_message("Value for text id not valid." \
                                    " It has to be in the range " + str(MIN_TEXT_ID - 1) + " < TextId <" + str(MAX_TEXT_ID - 1) + \
                                    "\n\nCurrent value TextId = " + val_number)

                return False

        else:
            str_front = val_number[:2]
            str_rear  = val_number[2:]

            if str_front != 'e_':   # pylint: disable=magic-value-comparison
                self._trace_message("Value for text id not valid."   \
                                    " It has to start with a lowercase \"e_\" " \
                                    "\\nCurrent value TextId = " + val_number)

                return False

            if not  self.__is_ascii_underline_numbers(str_rear):
                self._trace_message("Value for text id not valid." \
                                    "It has to contain the start sequence 'e_'" \
                                    " and only uppercase ascii signs, numbers and '_' behind it." \
                                    "\n\nCurrent value TextId = " + val_number)

                return False

        if val_number in self.str_table:
            self._trace_message('BuildingElementStringTable, add_entry: text id ' + str(val_number) + ' allready exists')
            return False

        self.str_table[val_number] = val_str

        return True

```

</details>