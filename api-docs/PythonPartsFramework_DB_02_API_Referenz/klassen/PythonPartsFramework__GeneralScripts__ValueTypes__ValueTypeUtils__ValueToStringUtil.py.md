---
title: "ValueToStringUtil"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ValueToStringUtil.py"
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


# ValueToStringUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ValueToStringUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the value to string utilities

## Abhängigkeiten

- `typing`

## Klassen

### `ValueToStringUtil`

implementation of the value to string utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `check_to_string_strip` | `value: Any` | `str` | check for a strip string  Args:     value: value  Returns:     value string |
| `to_string_strip` | `value: Any` | `str` | Convert the value to a string and strip " " and "   Args:     value: value  Returns:     value string |
| `trim_value_string` | `value_str: str` | `str` | Trim a value string from an object  Args:     value_str:     Value string  Returns:     trimmed value string |
| `replace_blanks_around_name` | `text: str, name: str` | `str` | replace the blanks before and after a name  Args:     text: text     name: name  Returns:     adapted text |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the value to string utilities
"""

from typing import Any

class ValueToStringUtil():
    """ implementation of the value to string utilities
    """

    @staticmethod
    def check_to_string_strip(value: Any) -> str:
        """ check for a strip string

        Args:
            value: value

        Returns:
            value string
        """

        object_type = str(type(value))

        if "NemAll_Python_" in object_type or \
           "ReinforcementShapeProperties" in object_type or \
           "PlaneReferences" in object_type:
            return ValueToStringUtil.to_string_strip(value)

        return str(value)


    @staticmethod
    def to_string_strip(value: Any) -> str:
        """ Convert the value to a string and strip " " and "\n

        Args:
            value: value

        Returns:
            value string
        """

        return ValueToStringUtil.trim_value_string(str(value))


    @staticmethod
    def trim_value_string(value_str: str) -> str:
        """ Trim a value string from an object

        Args:
            value_str:     Value string

        Returns:
            trimmed value string
        """

        value_str = value_str.replace("\n", "")


        #----------------- replace the blanks

        if "FixtureProperties" in value_str:
            value_str = ValueToStringUtil.replace_blanks_around_name(value_str, "FixtureProperties")
            value_str = ValueToStringUtil.replace_blanks_around_name(value_str, "PathShortcut")
            value_str = ValueToStringUtil.replace_blanks_around_name(value_str, "Group")

            return ValueToStringUtil.replace_blanks_around_name(value_str, "Element")

        if "PrecastLayerProperties" in value_str:
            value_str = value_str.replace(" ", "")
            value_str = value_str.replace("\t", "")
            return value_str

        if "PlaneReferences" in value_str:
            value_str = value_str.replace(":", "_")

        if "Matrix" not in value_str:
            return value_str.replace(" ", "")

        while value_str.find("  ") != -1:
            value_str = value_str.replace("  ", " ")

        return value_str.replace("( ", "(")


    @staticmethod
    def replace_blanks_around_name(text: str,
                                   name: str) -> str:
        """ replace the blanks before and after a name

        Args:
            text: text
            name: name

        Returns:
            adapted text
        """

        to_replace = f" {name}"

        while text.find(to_replace) != -1:
            text = text.replace(to_replace, name)

        to_replace = f"{name} "

        while text.find(to_replace) != -1:
            text = text.replace(to_replace, name)

        return text

```

</details>