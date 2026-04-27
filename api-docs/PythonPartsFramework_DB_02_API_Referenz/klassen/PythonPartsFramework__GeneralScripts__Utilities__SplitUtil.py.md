---
title: "SplitUtil"
source: "PythonPartsFramework\GeneralScripts\Utilities\SplitUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# SplitUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\Utilities\SplitUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the split utilities

## Abhängigkeiten

- Keine

## Klassen

### `SplitUtil`

implementation of the split utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `split_by_comma` | `text: str` | `list[str]` | split the text by a comma, check for comma in quotes or brackets  Args:     text: text  Returns:     pars of the splitted text |
| `split_string_with_bracket_parts` | `str_to_split: str, separator: str` | `list[str]` | Split a string with bracket parts in a list like:     tuple1(12,5),3.4,8,tuple2(12,7),3 in [tuple1(12,5), 3.4, 8, tuple2(12,7), 3]  Args:     str_to_split: string to split     separator:    separator  Returns:     split string as list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the split utilities
"""

COMMA = ","

class SplitUtil():
    """ implementation of the split utilities
    """

    @staticmethod
    def split_by_comma(text: str) -> list[str]:
        """ split the text by a comma, check for comma in quotes or brackets

        Args:
            text: text

        Returns:
            pars of the splitted text
        """

        if COMMA not in text:
            return [text]

        in_quotes   = False
        in_brackets = 0
        i_start     = 0
        parts       = []

        for index, char in enumerate(text):
            match char:
                case ",":
                    if not in_quotes and not in_brackets:
                        parts.append(text[i_start: index])
                        i_start = index + 1

                case "\"":
                    in_quotes = not in_quotes

                case "(" | "[":
                    in_brackets += 1

                case ")" | "]":
                    in_brackets -= 1

        parts.append(text[i_start:])

        return parts


    @staticmethod
    def split_string_with_bracket_parts(str_to_split: str,
                                        separator   : str) -> list[str]:
        """ Split a string with bracket parts in a list like:
            tuple1(12,5),3.4,8,tuple2(12,7),3 in [tuple1(12,5), 3.4, 8, tuple2(12,7), 3]

        Args:
            str_to_split: string to split
            separator:    separator

        Returns:
            split string as list
        """

        if not str_to_split:
            return []

        split_index = []

        is_split = True

        for index, char in enumerate(str_to_split):
            match char:
                case "(":
                    is_split = False

                case ")":
                    is_split = True

                case _:
                    if char == separator and is_split:
                        split_index.append(index)


        #----------------- split the string

        str_list = []

        start = 0

        for index in split_index:
            str_list.append(str_to_split[start: index])

            start = index + 1

        if not str_list:
            return [str_to_split]

        str_list.append(str_to_split[split_index[-1] + 1:])

        return str_list

```

</details>