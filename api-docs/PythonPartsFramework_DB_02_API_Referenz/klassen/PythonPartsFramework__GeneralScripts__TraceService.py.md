---
title: "TraceService"
source: "PythonPartsFramework\GeneralScripts\TraceService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# TraceService

> **Pfad:** `PythonPartsFramework\GeneralScripts\TraceService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the trace utilities

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `enum`
- `string`
- `typing`

## Klassen

### `TraceLevel`

Definition of the trace levels
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `TraceService`

Definition of service class TraceService
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, reset: bool=False` | `None` | initialize  Args:     reset: reset state |
| `__getattr__` | `self, name: str` | `Any` | get the attribute  Args:     name: attribute name  Returns:     attribute |
| `__make_trace_readable` | `input_str: str` | `str` | Converts a string in trace readable signs  Args:     input_str: input string to convert  Returns:     traceable string |
| `trace_1` | `value: str` | `None` | Converts signs in value to printable, if necessary and prints value  Arg:    value string to print into trace  Args:     value: value to print |
| `trace_2` | `str_value_front: str, str_value_back: str` | `None` | If necessary converts signs in str_value_front and str_value_back to printable and prints both  Arg:    value string to print into trace  Args:     str_value_front: front string     str_value_back:  back string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the trace utilities
"""

# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=magic-value-comparison

from typing import Any

import string
import enum

import NemAll_Python_AllplanSettings as AllplanSettings

class TraceLevel(enum.IntEnum):
    """ Definition of the trace levels
    """

    PYP_FILE_NAME      = 1
    STRING_TABLE_NAME  = 2
    SCRIPT_NAME        = 3
    LANGUAGE_FILE_NAME = 4
    VS_NODE_LOAD_INFO  = 5
    FAVORITE_FILE_NAME = 6
    MISSING_TEXT_ID    = 7


class TraceService:
    """ Definition of service class TraceService
    """

    class __TraceService():
        """ implementation of the internal class """

        def __init__(self):
            """ read the data """

            self.trace_level_dict = {}

            file_name = f"{AllplanSettings.AllplanPaths.GetUsrPath()}PythonPartTraceLevel.dat"

            try:                                                        # pylint: disable=too-many-try-statements
                with open(file_name, 'r', encoding="utf8") as file:
                    for line in file.readlines():
                        name, _, value = line.partition("=")

                        self.trace_level_dict[getattr(TraceLevel, name, None)] = value.strip(" \n") == "True"

            except FileNotFoundError:
                pass


        def is_trace_enabled(self,
                             trace_level: TraceLevel) -> bool:
            """ is the trace enabled for the given trace level

            Args:
                trace_level: trace level

            Returns:
                trace enabled state
            """

            return self.trace_level_dict.get(trace_level, False)


        def trace(self,
                  trace_level: TraceLevel,
                  *args      : Any):
            """ trace the arguments

            Args:
                trace_level: trace level
                *args:       arguments to print
            """

            if self.is_trace_enabled(trace_level):
                print(*[TraceService.__make_trace_readable(arg) for arg in args], flush = True)


        def set_trace_missing_text_id(self,
                                      trace_state: bool):
            """ set the trace state for a missing text id

            Args:
                trace_state: trace state
            """

            self.trace_level_dict[TraceLevel.MISSING_TEXT_ID] = trace_state


    #----------------- access to the internal implementation

    instance = None

    def __init__(self,
                 reset: bool = False):
        """ initialize

        Args:
            reset: reset state
        """

        if reset or not TraceService.instance:
            TraceService.instance = TraceService.__TraceService()

        self.instance = TraceService.instance


    def __getattr__(self,
                    name: str) -> Any:
        """ get the attribute

        Args:
            name: attribute name

        Returns:
            attribute
        """

        return getattr(self.instance, name)


    @staticmethod
    def __make_trace_readable(input_str: str) -> str:
        """ Converts a string in trace readable signs

        Args:
            input_str: input string to convert

        Returns:
            traceable string
        """

        res =''

        for char in input_str:
            if char not in string.printable:
                if char.isnumeric():
                    res += char
                else:
                    res += '?'# sign char is not trace readable
            else:
                res += char

        return res


    @staticmethod
    def trace_1(value: str):
        """ Converts signs in value to printable, if necessary and prints value

        Arg:    value string to print into trace

        Args:
            value: value to print
        """

        strtmp = TraceService.__make_trace_readable(value)

        print(strtmp, flush = True)


    @staticmethod
    def trace_2(str_value_front: str,
                str_value_back : str):
        """ If necessary converts signs in str_value_front and str_value_back to printable and prints both

        Arg:    value string to print into trace

        Args:
            str_value_front: front string
            str_value_back:  back string
        """

        strtmp_back  = TraceService.__make_trace_readable(str_value_back)
        strtmp_front = TraceService.__make_trace_readable(str_value_front)

        print(strtmp_front, strtmp_back, flush = True)

```

</details>