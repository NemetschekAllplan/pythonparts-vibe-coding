---
title: "StringUtil"
source: "PythonPartsFramework\Utils\StringUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# StringUtil

> **Pfad:** `PythonPartsFramework\Utils\StringUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the string utilities

## Abhängigkeiten

- `typing`

## Klassen

### `StringUtil`

implementation of the string utilities 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `split_string` | `string: str, pattern: str` | `Tuple[int, ...]` | split a string by a pattern  Args:     string:  string     pattern: pattern ... %s ... %n ...  Returns:     count of splitted strings, strings |
| `to_string` | `value: Any, length: int, fractions: int` | `None` | convert a value to a string  |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
implementation of the string utilities
"""

from typing import Tuple, Any,List

class StringUtil():
    """ implementation of the string utilities """

    @staticmethod
    def split_string(string : str,
                     pattern: str) -> Tuple[int, ...]:
        """ split a string by a pattern

        Args:
            string:  string
            pattern: pattern ... %s ... %n ...

        Returns:
            count of splitted strings, strings
        """

        # print("+++++++++++++++++++++++++++++++")
        # print(string)
        # print(pattern)


        #----------------- split the pattern string

        pattern_parts : List[str] = []
        index         = 0
        start_index   = 0

        while index < len(pattern):
            if pattern[index] == "%":
                if start_index < index:
                    pattern_parts.append(pattern[start_index: index])

                pattern_parts.append(pattern[index: index + 2])

                index += 2
                start_index = index
                continue

            index += 1

        if start_index < len(pattern) - 1:
            pattern_parts.append(pattern[start_index:])

        #print(pattern_parts)


        #----------------- split the string


        count      = 0
        result     = []
        i_pattern  = 0
        index      = 0

        while index < len(string):
            if pattern_parts[i_pattern] == "%s":
                if not result or result[-1] != " ":
                    result.append("")

                while index < len(string):
                    if i_pattern < len(pattern_parts) - 1:
                        part = pattern_parts[i_pattern + 1]

                        if string[index: index + len(part)] == part:
                            i_pattern += 2

                            result.append(part)

                            index += len(part)

                            break

                    result[-1] += string[index]

                    index += 1

            elif pattern_parts[i_pattern] == "%n":
                if not result or result[-1]:
                    result.append("")

                while index < len(string):
                    char = string[index]

                    if not char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "."]:
                        index += 1

                        if result[-1]:
                            i_pattern += 1

                        break

                    result[-1] += char

                    index += 1


        #----------------- convert the numeric values

        for index, value in enumerate(result):
            if pattern_parts[index] == "%n":
                result[index] = float(value) if value else 0


        #----------------- add missing entries

        count = 0

        for part in pattern_parts:
            if not part.startswith("%"):
                continue

            count = count + 1

            if count <= len(result):
                continue

            if part == "%s":
                result.append("")
            else:
                result.append(0)

        #print(result)

        return count, *result


    @staticmethod
    def to_string(value    : Any,
                  length   : int,
                  fractions: int):
        """ convert a value to a string """

        if isinstance(value, int):
            return f"{value:{length}d}"

        return f"{value:{length}.{fractions}f}"

```

</details>