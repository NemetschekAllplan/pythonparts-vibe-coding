---
title: "BuildingElementStringTableBase"
source: "PythonPartsFramework\GeneralScripts\BuildingElementStringTableBase.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementStringTableBase

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementStringTableBase.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Script for BuildingElementStringTable

## Abhängigkeiten

- `NemAll_Python_Utility`
- `TraceService`
- `XMLReader.XmlElementTreeUtil`
- `abc`
- `os`
- `sys`

## Klassen

### `BuildingElementStringTableBase`

Definition of class StringTable
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, path: str, numeric: bool, lang: str, force_lang_name: bool=False` | `None` | Initialization of class StringTableBase  Args:     path:            path of according .py file. The file name will be set internally to _xyz.xml     numeric:         the string table will be created only from numeric (123..) text ids or not numeric text ids (e_THE_VALUE)     lang:            language short cut     force_lang_name: force the language name |
| `get_language` | `self` | `str` | Get the language  Returns:     language of the string table |
| `get_path` | `self` | `str` | Get the path  Returns:     path of the string table file |
| `is_valid` | `self` | `bool` | Checks if string table is valid  Returns:     True/False for success and the string result |
| `get_path_and_filename` | `self` | `str` | returns the path and filename of the string table  Returns:     the path and filename of the string table |
| `_get_path_from_lang` | `self` | `bool` | Replaces the ending ".pyp" at the end of self.path with language specific ending "_language.xml"  Returns:     path exist: True/False |
| `_read_file` | `self, info_text: str, path: str` | `None` | Reads the complete file and creates the string table depending to current language  Args:     info_text: info text for the trace     path:      full file path |
| `enable_error_msg_box` | `-` | `None` | enable the message box for the error messages  |
| `_trace_message` | `msg: str` | `None` | trace the message and show a message box (if enabled)  Args:     msg: message to show |
| `add_entry` | `self, _text_id: str, _lang_str: str` | `None` | add the entry  |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementStringTable
"""

#pylint: disable=global-statement
#pylint: disable=bare-except

import os
import sys
import abc

import NemAll_Python_Utility as AllplanUtil

from TraceService import TraceService, TraceLevel

from XMLReader.XmlElementTreeUtil import XmlElementTreeUtil

SHOW_ERROR_MSG_BOX = False


class BuildingElementStringTableBase(abc.ABC):
    """ Definition of class StringTable
    """

    def __init__(self,
                 path           : str,
                 numeric        : bool,
                 lang           : str,
                 force_lang_name: bool = False):
        """ Initialization of class StringTableBase

        Args:
            path:            path of according .py file. The file name will be set internally to _xyz.xml
            numeric:         the string table will be created only from numeric (123..) text ids or not numeric text ids (e_THE_VALUE)
            lang:            language short cut
            force_lang_name: force the language name
        """

        self._is_numeric      = numeric
        self._language        = lang
        self._path            = path
        self._m_is_valid      = False
        self._force_lang_name = force_lang_name
        self.str_table        = {}


    def get_language(self) -> str:
        """ Get the language

        Returns:
            language of the string table
        """

        return self._language


    def get_path(self) -> str:
        """ Get the path

        Returns:
            path of the string table file
        """

        return self._path


    def is_valid(self) -> bool:
        """ Checks if string table is valid

        Returns:
            True/False for success and the string result
        """
        return self._m_is_valid


    def get_path_and_filename(self) -> str:
        """ returns the path and filename of the string table

        Returns:
            the path and filename of the string table
        """
        return self._path


    def _get_path_from_lang(self) -> bool:
        """ Replaces the ending ".pyp" at the end of self.path with language specific ending "_language.xml"

        Returns:
            path exist: True/False
        """

        #----------------- combine the new filename

        # abc.xxx -> abc_deu.xml for german language

        path_parts = os.path.splitext(self._path)

        path_old  = path_parts[0] + '_' + self._language + '.xml'

        trace_err = path_parts[1].lower() in {".py", ".pyp", ""}

        self._path = path_old.replace('\\\\', '\\') #remove double signs


        #----------------- add \\\\ for unc path

        if os.path.exists(self._path):
            return True

        if self._path.find('\\') != 0:
            if trace_err:
                self._trace_message(f"Filename {self._path} does not exist")

            if self._language == "deu":                                     # pylint: disable=magic-value-comparison
                self._path = path_old.replace("_deu.xml", "_eng.xml")

                if os.path.exists(self._path):
                    if trace_err:
                        self._trace_message("Use the english string table")

                    return True

            return False


        #----------------- create and check the full file path

        if AllplanUtil.IsExecutedByUnitTest():
            return False

        self._path = '\\' + self._path

        if os.path.exists(self._path) is False:
            if trace_err:
                self._trace_message(f"Filename {self._path} does not exist")

            return False

        return True


    def _read_file(self,
                   info_text: str,
                   path     : str):
        """ Reads the complete file and creates the string table depending to current language

        Args:
            info_text: info text for the trace
            path:      full file path
        """

        TraceService().trace(TraceLevel.STRING_TABLE_NAME, info_text + path)

        try:
            doc = XmlElementTreeUtil.parse(path)

        except:
            except_info = sys.exc_info()

            if not self._is_numeric:
                self._trace_message(f"read file for common string table: \n\n{path}\n\n{except_info[1]}")
            else:
                self._trace_message(f"read file for global string table: \n\n{path}\n\n{except_info[1]}")
            return


        #----------------- read the string table

        for node_element in XmlElementTreeUtil.get_elements_by_tag_name(doc, "Item"):
            text_id     = XmlElementTreeUtil.get_tag_data(node_element, "TextId")
            lang_string = XmlElementTreeUtil.get_tag_data(node_element, "Text", "", True)

            if     text_id.isnumeric() and     self._is_numeric  or \
               not text_id.isnumeric() and not self._is_numeric:
                if self.add_entry(text_id, lang_string) is False:
                    self._trace_message(f"String table entry was not created.\n\n{text_id}\n\n{lang_string}")

                else:
                    self._m_is_valid = True


        #----------------- read the include files

        for node_element in XmlElementTreeUtil.get_elements_by_tag_name(doc, "IncludeLanguageFile"):
            if node_element.text is not None and (dir_name := os.path.dirname(self._path)) is not None:
                self._read_file(info_text, f"{dir_name}\\{node_element.text}_{self._language}.xml")


    @staticmethod
    def enable_error_msg_box():
        """ enable the message box for the error messages """

        global SHOW_ERROR_MSG_BOX

        SHOW_ERROR_MSG_BOX = True


    @staticmethod
    def _trace_message(msg: str):
        """ trace the message and show a message box (if enabled)

        Args:
            msg: message to show
        """

        TraceService().trace(TraceLevel.STRING_TABLE_NAME, f"\n\n{'=' * 80}")
        TraceService().trace(TraceLevel.STRING_TABLE_NAME, "\nString table error:\n")
        TraceService().trace(TraceLevel.STRING_TABLE_NAME, msg)
        TraceService().trace(TraceLevel.STRING_TABLE_NAME, "")
        TraceService().trace(TraceLevel.STRING_TABLE_NAME, f"\n\n{'=' * 80}")

        if SHOW_ERROR_MSG_BOX:
            AllplanUtil.ShowMessageBox(msg, AllplanUtil.MB_OK)


    @abc.abstractmethod
    def add_entry(self,
                  _text_id: str,
                  _lang_str: str):
        """ add the entry """

```

</details>