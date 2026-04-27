---
title: "XmlStringToValueConverter"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlStringToValueConverter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlStringToValueConverter

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlStringToValueConverter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`, `xml`

## Übersicht

implementation of the XML string to value converter

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementListUtil`
- `BuildingElementTupleUtil`
- `StringToValueConverter`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueType`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `re`
- `typing`

## Klassen

### `XmlStringToValueConverter`

implementation of the XML string to value converter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `build_ele: BuildingElement, value_type: ParameterPropertyValueType, value_str: str, named_tuple_def: Any, attribute_id: int | list[int], local_str_table: Any, material_str_table: Any` | `Any` | Get the value for the value type  Args:     build_ele:          building element with the parameter properties     value_type:         value type     value_str:          value string     named_tuple_def:    named tuple definition     attribute_id:       attribute IDs     local_str_table:    local string table     material_str_table: material string table  Returns:     value |
| `__get_value_list` | `value_str: str, named_tuple_def: Any` | `list[str]` | get the value list  Args:     value_str:       value string     named_tuple_def: named tuple definition  Returns:     value list |
| `__get_value_tuple` | `value_str: str, value_type: ParameterPropertyValueType, named_tuple_def: Any` | `list[tuple | None] | (tuple | None)` | get the value for a tuple  Args:     value_str:       value string     value_type:      value type     named_tuple_def: name tuple definition  Returns:     tuple element |
| `__replace_constants` | `value_str: str, build_ele: BuildingElement` | `Any` | replace the constants in a value string  Args:     value_str: value string     build_ele: building element with the parameter properties  Returns:     value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the XML string to value converter
"""

from typing import Any

import re

from BuildingElement import BuildingElement
from BuildingElementListUtil import BuildingElementListUtil
from BuildingElementTupleUtil import BuildingElementTupleUtil
from StringToValueConverter import StringToValueConverter

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueType import ParameterPropertyValueType
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

class XmlStringToValueConverter():
    """ implementation of the XML string to value converter
    """

    @staticmethod
    def get_value(build_ele         : BuildingElement,
                  value_type        : ParameterPropertyValueType,
                  value_str         : str,
                  named_tuple_def   : Any,
                  attribute_id      : (int | list[int]),
                  local_str_table   : Any,
                  material_str_table: Any) -> Any:
        """ Get the value for the value type

        Args:
            build_ele:          building element with the parameter properties
            value_type:         value type
            value_str:          value string
            named_tuple_def:    named tuple definition
            attribute_id:       attribute IDs
            local_str_table:    local string table
            material_str_table: material string table

        Returns:
            value
        """

        if not value_type.has_impl and value_type.startswith("$"):
            return None if value_str != GeneralConstants.EMPTY_LIST else []

        if value_type.is_tuple_type():
            return XmlStringToValueConverter.__get_value_tuple(value_str, value_type, named_tuple_def)

        if value_type == ParameterPropertyValueTypes.LIST:
            return XmlStringToValueConverter.__get_value_list(value_str, named_tuple_def)

        if value_type == ParameterPropertyValueTypes.MATERIAL_BUTTON  and  material_str_table:
            tmp_search_str , res = material_str_table.get_entry(f"mat_{value_str}")

            if res:
                value_str = tmp_search_str

        if (ParameterPropertyValueTypes.is_resource_list_type(value_type) or \
            ParameterPropertyValueTypes.RADIO_BUTTON_GROUP == value_type):
            value_str = XmlStringToValueConverter.__replace_constants(value_str, build_ele)

        return StringToValueConverter.get_value(value_type, value_str, local_str_table, attribute_id)


    @staticmethod
    def __get_value_list(value_str      : str,
                         named_tuple_def: Any) -> list[str]:
        """ get the value list

        Args:
            value_str:       value string
            named_tuple_def: named tuple definition

        Returns:
            value list
        """

        if not value_str:
            return []

        return BuildingElementListUtil.get_list_element(value_str, ParameterPropertyValueTypesImpl.get_value_type_impl("list"),
                                                        named_tuple_def)


    @staticmethod
    def __get_value_tuple(value_str      : str,
                          value_type     : ParameterPropertyValueType,
                          named_tuple_def: Any) -> (list[(tuple | None)] | (tuple | None)):
        """ get the value for a tuple

        Args:
            value_str:       value string
            value_type:      value type
            named_tuple_def: name tuple definition

        Returns:
            tuple element
        """

        if value_str == GeneralConstants.EMPTY_TUPLE:
            return BuildingElementTupleUtil.get_tuple_element("", value_type, named_tuple_def)

        if not value_str:
            return BuildingElementTupleUtil.get_tuple_element(value_str, value_type, named_tuple_def)

        if value_str and not named_tuple_def and GeneralConstants.TEXT_SEPARATOR not in value_str:
            return value_type.get_value(value_str)

        if value_str[0] == GeneralConstants.LIST_SEPARATOR_START:
            return BuildingElementTupleUtil.get_tuple_element_list(value_str, value_type, named_tuple_def)

        return BuildingElementTupleUtil.get_tuple_element(value_str, value_type, named_tuple_def)


    @staticmethod
    def __replace_constants(value_str: str,
                            build_ele: BuildingElement) -> Any:
        """ replace the constants in a value string

        Args:
            value_str: value string
            build_ele: building element with the parameter properties

        Returns:
            value
        """

        value_str = value_str.strip()

        for key, value in build_ele.get_constant_dict().items():
            value_str = re.sub(fr"\b{key}\b",  str(value),  value_str)

        return value_str

```

</details>