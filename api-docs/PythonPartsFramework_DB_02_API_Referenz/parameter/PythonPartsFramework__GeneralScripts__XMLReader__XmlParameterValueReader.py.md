---
title: "XmlParameterValueReader"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterValueReader.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - werte
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlParameterValueReader

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterValueReader.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `werte`, `xml`

## Übersicht

implementation of the parameter reader

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueType`
- `ValueTypes.ParameterPropertyValueTypes`
- `XmlElementTreeUtil`
- `XmlParameterTextReader`
- `enum`
- `itertools`
- `xml.etree`

## Klassen

### `XmlParameterValueReader`

implementation of the parameter reader
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value_str` | `param: ElementTree.Element, value_type: str, local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable, is_imperial_unit: bool, build_ele: BuildingElement` | `str` | Extract the value of the control  Args:     param:            parameter from the element tree     value_type:       type of the parameter     local_str_table:  local string table     global_str_table: global string table     is_imperial_unit: is imperial unit state     build_ele:        building element with the parameter properties  Returns:     value string |
| `__get_value_str_named_tuple` | `local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable, value_str: str, value_text_id: str` | `str` | get the value string for a named tuple  Args:     local_str_table:  local string table     global_str_table: global string table     value_str:        value string     value_text_id:    value text IDs  Returns:     named tuple value string |
| `get_value_list` | `param: ElementTree.Element, value_type: ParameterPropertyValueType, local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable` | `str` | Extract the value list of control  Args:     param:            Check this parameter node for a value list statement     value_type:       value type     local_str_table:  local string table     global_str_table: global string table  Returns:     value list string |
| `get_value_text_list` | `param: ElementTree.Element, text: str, value_type: ParameterPropertyValueType, value_count: int, local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable` | `tuple[str, str]` | Extract the value text list of control  Args:     param:            check this parameter node for a value text list statement     text:             text     value_type:       value type     value_count:      value count     local_str_table:  local string table     global_str_table: global string table  Returns:     value list string, text |
| `get_value_list_2` | `param: ElementTree.Element` | `str` | Extract the value list 2 of control  Args:     param: Check this parameter node for a value list statement  Returns:     value list string |
| `get_enum_dict` | `param: ElementTree.Element` | `tuple[dict[int, IntEnum], str]` | get the enumeration list  Args:     param: Check this parameter node for a value list statement  Returns:     enum list, value list string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the parameter reader
"""

from xml.etree import ElementTree

from enum import IntEnum
from itertools import zip_longest

from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from StringEvaluate import StringEvaluate

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueType import ParameterPropertyValueType

from Utilities.GeneralConstants import GeneralConstants

from .XmlElementTreeUtil import XmlElementTreeUtil
from .XmlParameterTextReader import XmlParameterTextReader

class XmlParameterValueReader():
    """ implementation of the parameter reader
    """

    EMPTY_ID         = "0"
    ALLPLAN_PICT_RES = "AllplanSettings.PictRes"

    @staticmethod
    def get_value_str(param           : ElementTree.Element,
                      value_type      : str,
                      local_str_table : BuildingElementStringTable,
                      global_str_table: BuildingElementStringTable,
                      is_imperial_unit: bool,
                      build_ele       : BuildingElement) -> str:
        """ Extract the value of the control

        Args:
            param:            parameter from the element tree
            value_type:       type of the parameter
            local_str_table:  local string table
            global_str_table: global string table
            is_imperial_unit: is imperial unit state
            build_ele:        building element with the parameter properties

        Returns:
            value string
        """

        has_str_table = local_str_table and local_str_table.is_valid()
        value_str     = XmlElementTreeUtil.get_tag_data(param, "Value",
                                                        allow_multiline_text = value_type in {ParameterPropertyValueTypes.TEXT,
                                                                                              ParameterPropertyValueTypes.STRING})


        #----------------- check for imperial unit value

        if is_imperial_unit:
            if (imp_value_str := XmlElementTreeUtil.get_tag_data(param, "ImperialValue")):
                value_str = imp_value_str


        #----------------- id with PythonScripts for dynamic text creation

        if value_type in {ParameterPropertyValueTypes.TEXT, ParameterPropertyValueTypes.PICTURE} and \
           (text_dyn := XmlElementTreeUtil.get_tag_data(param,'ValueTextDyn', allow_multiline_text = True)):
            return StringEvaluate.TEXT_FROM_SCRIPT + text_dyn


        #----------------- check for text from the string table

        if not has_str_table or \
           (value_type.split("(")[0] not in {'stringcombobox', 'text', 'string', 'namedtuple'}):
            return value_str

        if not (value_text_id := XmlElementTreeUtil.get_tag_data(param, 'ValueTextId', allow_multiline_text = True)):
            return value_str


        #----------------- get the value string

        param_dict = build_ele.get_parameter_dict()

        if value_type.startswith("namedtuple"):
            return XmlParameterValueReader.__get_value_str_named_tuple(local_str_table, global_str_table, value_str, value_text_id)

        value_text_id = str(eval(value_text_id, param_dict))
        value_str     = XmlParameterTextReader.get_localisation(value_text_id, local_str_table, global_str_table, value_str)

        return value_str


    @staticmethod
    def __get_value_str_named_tuple(local_str_table : BuildingElementStringTable,
                                    global_str_table: BuildingElementStringTable,
                                    value_str       : str,
                                    value_text_id   : str) -> str:
        """ get the value string for a named tuple

        Args:
            local_str_table:  local string table
            global_str_table: global string table
            value_str:        value string
            value_text_id:    value text IDs

        Returns:
            named tuple value string
        """
        new_value_str = []

        for value, value_id in zip(value_str.split("|"), value_text_id.split("|")):
            if value_id and value_id != XmlParameterValueReader.EMPTY_ID:
                new_value_str.append(XmlParameterTextReader.get_localisation(value_id, local_str_table, global_str_table))
            else:
                new_value_str.append(value)

        return "|".join(new_value_str)


    @staticmethod
    def get_value_list(param           : ElementTree.Element,
                       value_type      : ParameterPropertyValueType,
                       local_str_table : BuildingElementStringTable,
                       global_str_table: BuildingElementStringTable) -> str:
        """ Extract the value list of control

        Args:
            param:            Check this parameter node for a value list statement
            value_type:       value type
            local_str_table:  local string table
            global_str_table: global string table

        Returns:
            value list string
        """

        value_list = XmlElementTreeUtil.get_tag_data(param, 'ValueList', allow_multiline_text = True)

        is_tuple = value_type.is_tuple_type()

        if value_type != ParameterPropertyValueTypes.STRING_COMBO_BOX and not is_tuple or not local_str_table.is_valid():
            return value_list

        if not (value_list_tag := XmlElementTreeUtil.get_tag_data(param, 'ValueList_TextIds')):
            return value_list

        if not is_tuple:
            text_ids      = value_list_tag.split("|")
            default_texts = value_list.split("|")

            return "|".join([XmlParameterTextReader.get_localisation(text_id, local_str_table, global_str_table, default_text)
                             for text_id, default_text in zip(text_ids, default_texts)])



        #----------------- value list for a tuple

        value_list = []

        value_type_str = value_type.split("(", 1)[-1].rstrip(")")

        for tuple_value_type, list_tag in zip(value_type_str.split(","), value_list_tag.split(",")):
            if tuple_value_type == ParameterPropertyValueTypes.STRING_COMBO_BOX:
                value_list.append("|".join([XmlParameterTextReader.get_localisation(id, local_str_table, global_str_table) \
                                            for id in list_tag.split("|")]))
            else:
                value_list.append(list_tag)

        return ",".join(value_list)


    @staticmethod
    def get_value_text_list(param           : ElementTree.Element,
                            text            : str,
                            value_type      : ParameterPropertyValueType,
                            value_count     : int,
                            local_str_table : BuildingElementStringTable,
                            global_str_table: BuildingElementStringTable) -> tuple[str, str]:
        """ Extract the value text list of control

        Args:
            param:            check this parameter node for a value text list statement
            text:             text
            value_type:       value type
            value_count:      value count
            local_str_table:  local string table
            global_str_table: global string table

        Returns:
            value list string, text
        """

        value_text_list = XmlElementTreeUtil.get_tag_data(param, 'ValueTextList', allow_multiline_text = True)

        if (value_text_id_list := XmlElementTreeUtil.get_tag_data(param, 'ValueTextIdList', allow_multiline_text = True)):
            value_text_list = "|".join([XmlParameterTextReader.get_localisation(text_id, local_str_table, global_str_table, default_text)
                                        for text_id, default_text in zip_longest(value_text_id_list.split(GeneralConstants.TEXT_SEPARATOR),
                                                                                 value_text_list.split(GeneralConstants.TEXT_SEPARATOR),
                                                                                 fillvalue = "")])

        if value_text_list:
            return f"{value_text_list}{'|' * (max(value_count - value_text_list.count(GeneralConstants.TEXT_SEPARATOR) - 1, 0))}", text

        if value_type.is_tuple_type():
            return value_text_list, text

        if GeneralConstants.TEXT_SEPARATOR not in text:
            return "|" * (value_count - 1), text


        #----------------- old version: split the text

        parts = text.split(GeneralConstants.TEXT_SEPARATOR)

        if (parts_count :=len(parts)) <= value_count:
            return f"{text}{'|' * (value_count - parts_count)}", ""

        return "|".join(parts[1:]), parts[0]


    @staticmethod
    def get_value_list_2(param: ElementTree.Element) -> str:
        """ Extract the value list 2 of control

        Args:
            param: Check this parameter node for a value list statement

        Returns:
            value list string
        """

        if (value_list_2 := XmlElementTreeUtil.get_tag_data(param, 'ValueList2')):
            repl_text = f"{GeneralConstants.TEXT_SEPARATOR} "

            while repl_text in value_list_2:
                value_list_2 = value_list_2.replace(repl_text, GeneralConstants.TEXT_SEPARATOR)

            return value_list_2

        value_list_2 = XmlElementTreeUtil.get_tag_data(param, 'EnumList2')

        if XmlParameterValueReader.ALLPLAN_PICT_RES not in value_list_2:
            return value_list_2

        values = eval(f"[{value_list_2.replace('|', ',')}]",  StringEvaluate.get_allplan_api_param_dict())

        return "|".join(str(int(item)) for item in values)


    @staticmethod
    def get_enum_dict(param: ElementTree.Element) -> tuple[dict[int, IntEnum], str]:
        """ get the enumeration list

        Args:
            param: Check this parameter node for a value list statement

        Returns:
            enum list, value list string
        """

        if not (enum_list_str := XmlElementTreeUtil.get_tag_data(param, 'EnumList', allow_multiline_text = True)):
            return {}, ""

        enum_list = eval(f"[{enum_list_str.replace('|', ',')}]",  StringEvaluate.get_allplan_api_param_dict())

        return {int(item) : item for item in enum_list}, \
               "|".join(str(int(item)) for item in enum_list)

```

</details>