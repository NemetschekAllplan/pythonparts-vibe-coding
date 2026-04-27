---
title: "XmlParameterTextReader"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterTextReader.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlParameterTextReader

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterTextReader.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `xml`

## Übersicht

implementation of the parameter text reader

## Abhängigkeiten

- `BuildingElementStringTable`
- `NemAll_Python_AllplanSettings`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `XMLReader.XmlElementTreeUtil`
- `xml.etree`

## Klassen

### `XmlParameterTextReader`

implementation of the parameter text reader
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_prop_text` | `param: ElementTree.Element, local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable, is_visual_script: bool, parent_node_value_type: str='', is_include: bool=False` | `str` | Get the property text  Args:     param:                  parameter     local_str_table:        local string table     global_str_table:       global string table     is_visual_script:       visual script state     parent_node_value_type: value type of the parent node     is_include:             process include state  Returns:     property text |
| `__get_include_text` | `param: ElementTree.Element, local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable, is_visual_script: bool` | `str` | get the text from include  Args:     param:            parameter     local_str_table:  local string table     global_str_table: global string table     is_visual_script: visual script state  Returns:     text from include |
| `__get_multiple_text` | `text: str | None, text_id: str, local_str_table: BuildingElementStringTable` | `str` | get a multiple text  Args:     text:            text     text_id:         text ID     local_str_table: local string table  Returns:     multiple test |
| `get_localisation` | `str_val_id: str, local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable, default_text: str | None=None` | `str` | Localization for text ids  Args:     str_val_id:       string with id to search in the string tables     local_str_table:  local string table     global_str_table: global string table     default_text:     default text  Returns:     localized string |
| `__get_text_from_string_table` | `str_table: BuildingElementStringTable, text_id: str, text: str | None, text_inc: str` | `str` | get the text from the string table  Args:     str_table: string table     text_id:   text ID     text:      text     text_inc:  include text  Returns:     text from string table |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the parameter text reader
"""

# pylint:disable=magic-value-comparison

from xml.etree import ElementTree

import NemAll_Python_AllplanSettings as AllplanSettings

from BuildingElementStringTable import BuildingElementStringTable
from StringEvaluate import StringEvaluate

from Utilities.GeneralConstants import GeneralConstants

from XMLReader.XmlElementTreeUtil import XmlElementTreeUtil

class XmlParameterTextReader():
    """ implementation of the parameter text reader
    """

    @staticmethod
    def get_prop_text(param                 : ElementTree.Element,
                      local_str_table       : BuildingElementStringTable,
                      global_str_table      : BuildingElementStringTable,
                      is_visual_script      : bool,
                      parent_node_value_type: str  = "",
                      is_include            : bool = False) -> str:
        """ Get the property text

        Args:
            param:                  parameter
            local_str_table:        local string table
            global_str_table:       global string table
            is_visual_script:       visual script state
            parent_node_value_type: value type of the parent node
            is_include:             process include state

        Returns:
            property text
        """

        #----------------- Check for text include

        text_inc = "" if is_include else XmlParameterTextReader.__get_include_text(param, local_str_table,
                                                                                   global_str_table, is_visual_script)


        #----------------- dynamic text creation

        if (text_dyn := XmlElementTreeUtil.get_tag_data(param, 'TextDyn', has_value_type = parent_node_value_type,
                                                        allow_multiline_text = True)):
            return StringEvaluate.TEXT_FROM_SCRIPT + text_dyn


        #----------------- get the text and id

        text, text_id = XmlElementTreeUtil.get_text_id_tag_data(param, parent_node_value_type, not is_include)

        if not text_id:
            if text:
                return text.replace("#", text_inc) if text_inc else text

            return ""


        #----------------- multiple texts or sub key texts

        if GeneralConstants.TEXT_SEPARATOR in text_id and local_str_table.is_valid():
            return XmlParameterTextReader.__get_multiple_text(text, text_id, local_str_table)


        #----------------- get from local string table

        if text_id.isnumeric():
            return XmlParameterTextReader.__get_text_from_string_table(local_str_table, text_id, text, text_inc)


        #-----------------get from global string table

        return XmlParameterTextReader.__get_text_from_string_table(global_str_table, text_id, text, text_inc)


    @staticmethod
    def __get_include_text(param           : ElementTree.Element,
                           local_str_table : BuildingElementStringTable,
                           global_str_table: BuildingElementStringTable,
                           is_visual_script: bool) -> str:
        """ get the text from include

        Args:
            param:            parameter
            local_str_table:  local string table
            global_str_table: global string table
            is_visual_script: visual script state

        Returns:
            text from include
        """

        text_inc = False if is_visual_script else XmlElementTreeUtil.get_tag_data(param, 'TextInc')

        if text_inc and local_str_table.is_valid():
            text_tmp, res = local_str_table.get_entry(text_inc)

            if not res  and  global_str_table.is_valid():
                text_tmp, res = global_str_table.get_entry(text_inc)

            if res:
                text_inc = text_tmp

        else:
            text_inc = XmlElementTreeUtil.get_tag_data(param,'TextIndex')

        return text_inc


    @staticmethod
    def __get_multiple_text(text           : (str | None),
                            text_id        : str,
                            local_str_table: BuildingElementStringTable) -> str:
        """ get a multiple text

        Args:
            text:            text
            text_id:         text ID
            local_str_table: local string table

        Returns:
            multiple test
        """

        text_ids   = text_id.replace(" ", "").replace("\n", "").split(GeneralConstants.TEXT_SEPARATOR)
        texts      = text.split(GeneralConstants.TEXT_SEPARATOR) if text is not None else []
        text_count = len(texts)

        if not ":" in text_id:
            return GeneralConstants.TEXT_SEPARATOR.join([local_str_table.get_entry(text_id)[0] if text_id != GeneralConstants.EMPTY_TEXT_ID
                                                            else \
                                                         texts[index] if index < text_count else "" \
                                                            for index, text_id in enumerate(text_ids)])

        #----------------- create the text for sub keys

        texts_from_ids = dict[str, str]()

        for item in texts:
            if ":" in item:
                key_value = item.split(":", 1)

                texts_from_ids[key_value[0]] = key_value[1]

        for item in text_ids:
            if not ":" in item:
                continue

            key_value = item.split(":")

            texts_from_ids[key_value[0]] = local_str_table.get_entry(key_value[1])[0]

        return GeneralConstants.TEXT_SEPARATOR + GeneralConstants.TEXT_SEPARATOR.join(
                                                    f"{key}:{value}" for key, value in texts_from_ids.items())


    @staticmethod
    def get_localisation(str_val_id      : str,
                         local_str_table : BuildingElementStringTable,
                         global_str_table: BuildingElementStringTable,
                         default_text    : (str | None) = None) -> str:
        """ Localization for text ids

        Args:
            str_val_id:       string with id to search in the string tables
            local_str_table:  local string table
            global_str_table: global string table
            default_text:     default text

        Returns:
            localized string
        """

        str_val_id = str_val_id.strip()

        if str_val_id.startswith("AllplanSettings."):
            text_id = StringEvaluate.eval(str_val_id, StringEvaluate.get_allplan_api_param_dict(), False)

            return AllplanSettings.AllplanLocalisationService.GetTextResource(text_id)

        res     = False
        str_tmp = ""

        if str_val_id.isnumeric() and local_str_table.is_valid():
            str_tmp, res = local_str_table.get_entry(str_val_id)

        elif global_str_table.is_valid():
            str_tmp, res = global_str_table.get_entry(str_val_id)

        if res is True:
            return str_tmp

        if default_text is not None:
            return default_text

        return str_val_id + ': not found'


    @staticmethod
    def __get_text_from_string_table(str_table: BuildingElementStringTable,
                                     text_id  : str,
                                     text     : (str | None),
                                     text_inc : str) -> str:
        """ get the text from the string table

        Args:
            str_table: string table
            text_id:   text ID
            text:      text
            text_inc:  include text

        Returns:
            text from string table
        """

        if not str_table.is_valid():
            return text if text is not None else ""

        str_tmp, res = str_table.get_entry(text_id)

        if res:
            return str_tmp.replace("#", text_inc) if text_inc else str_tmp

        if text:
            return text.replace("#", text_inc) if text_inc else text

        return str_tmp

```

</details>