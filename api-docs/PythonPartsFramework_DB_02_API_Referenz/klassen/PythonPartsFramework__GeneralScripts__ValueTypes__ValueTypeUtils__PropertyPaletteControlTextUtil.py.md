---
title: "PropertyPaletteControlTextUtil"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\PropertyPaletteControlTextUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PropertyPaletteControlTextUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\PropertyPaletteControlTextUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the property palette control text util

## Abhängigkeiten

- `BuildingElementStringTable`
- `ControlProperties`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `__future__`
- `dataclasses`
- `typing`

## Klassen

### `PropertyPaletteControlTextData`

implementation of the the property palette control text data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `PropertyPaletteControlTextUtil`

implementation of the property palette control text util
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, global_str_table: BuildingElementStringTable` | `None` | initialize  Args:     global_str_table: global string table |
| `get_row_name_text` | `self, ctrl_props: ControlProperties, sub_value_name: str, sub_text_key: str` | `PropertyPaletteControlTextData` | get the row and and the text  Args:     ctrl_props:     control properties     sub_value_name: sub value name     sub_text_key:   sub text key  Returns:     palette text |
| `get_sub_text` | `member_text: dict[str, str], value_name: str, text: str, sub_value_name: str` | `str` | get the text of a sub value from the value  Args:     member_text:    member text     value_name:     value name     text:           text     sub_value_name: name of the sub value  Returns:         text of a sub value from the value |
| `__get_text` | `self, ctrl_props: ControlProperties, sub_value_name: str, sub_text_key: str` | `str` | get the final text  Args:     ctrl_props:     control properties     sub_value_name: sub value name     sub_text_key:   sub text key  Returns:     palette text |
| `__get_row_text` | `self, row_name: str, text: str, key: str, sub_name: str, member_text: dict[str, str]` | `str` | get the text for the row  Args:     row_name:    name of the row     text:        default text     key:         sub text key     sub_name:    name of the sub member     member_text: text for the sub members  Returns:     row text |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the property palette control text util
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from dataclasses import dataclass

from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties

from Utilities.GeneralConstants import GeneralConstants

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

@dataclass
class PropertyPaletteControlTextData:
    """ implementation of the the property palette control text data
    """

    row_name : str = ""
    text     : str = ""


class PropertyPaletteControlTextUtil():
    """ implementation of the property palette control text util
    """

    def __init__(self,
                 global_str_table: BuildingElementStringTable):
        """ initialize

        Args:
            global_str_table: global string table
        """

        self.global_str_table = global_str_table


    def get_row_name_text(self,
                          ctrl_props    : ControlProperties,
                          sub_value_name: str,
                          sub_text_key  : str) -> PropertyPaletteControlTextData:
        """ get the row and and the text

        Args:
            ctrl_props:     control properties
            sub_value_name: sub value name
            sub_text_key:   sub text key

        Returns:
            palette text
        """

        text = self.__get_text(ctrl_props, sub_value_name, sub_text_key)

        row_name = self.__get_row_text(ctrl_props.row_name, ctrl_props.text, sub_text_key,
                                       f"{ctrl_props.value_name}.{sub_value_name}",
                                       ctrl_props.member_text)

        return PropertyPaletteControlTextData(row_name, text)


    @staticmethod
    def get_sub_text(member_text   : dict[str, str],
                     value_name    : str,
                     text          : str,
                     sub_value_name: str) -> str:
        """ get the text of a sub value from the value

        Args:
            member_text:    member text
            value_name:     value name
            text:           text
            sub_value_name: name of the sub value

        Returns:
                text of a sub value from the value
        """

        if member_text:
            name   = f"{value_name}.{sub_value_name}"

            name_member_text = member_text.get(name, None)

            if name_member_text and name_member_text not in ["X", "Y", "Z"]:
                return name_member_text

            return f"{text} {sub_value_name.split('.')[-1].lower()}" if text else f"{value_name} {sub_value_name.lower()}"

        return f"{text} {sub_value_name.split('.')[-1].lower()}"


    def __get_text(self,
                   ctrl_props    : ControlProperties,
                   sub_value_name: str,
                   sub_text_key  : str) -> str:
        """ get the final text

        Args:
            ctrl_props:     control properties
            sub_value_name: sub value name
            sub_text_key:   sub text key

        Returns:
            palette text
        """

        if sub_value_name and ctrl_props.member_text:
            name = f"{ctrl_props.value_name}.{sub_value_name}"


            #------------- in case of a row use the text from the row

            if (name_member_text := ctrl_props.member_text.get(name, None)) is not None:
                if ctrl_props.row_name:
                    return ""

                return name_member_text

        key_text = f" {self.global_str_table.get_entry(sub_text_key)[0]}" if sub_text_key else ""

        return ctrl_props.text + key_text if ctrl_props.text else key_text


    def __get_row_text(self,
                       row_name   : str,
                       text       : str,
                       key        : str,
                       sub_name   : str,
                       member_text: dict[str, str]) -> str:
        """ get the text for the row

        Args:
            row_name:    name of the row
            text:        default text
            key:         sub text key
            sub_name:    name of the sub member
            member_text: text for the sub members

        Returns:
            row text
        """

        if not row_name:
            return ""

        if (sub_text := member_text.get(sub_name, None)) is not None:
            return sub_text

        if row_name.endswith(GeneralConstants.XYZ_IN_ROW_KEY) or row_name == GeneralConstants.EMPTY_ROW_NAME_KEY:
            return f"{text} {self.global_str_table.get_entry(key)[0]}" if key else text


        #----------------- as list index at the end

        if row_name.isnumeric():
            return f"{self.global_str_table.get_entry(key)[0]} {row_name}" if key else row_name


        #----------------- before sub text

        return f"{row_name} {self.global_str_table.get_entry(key)[0]}" if key else row_name

```

</details>