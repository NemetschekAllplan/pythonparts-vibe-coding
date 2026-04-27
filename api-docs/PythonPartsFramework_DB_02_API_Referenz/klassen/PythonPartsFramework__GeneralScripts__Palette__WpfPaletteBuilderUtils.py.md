---
title: "WpfPaletteBuilderUtils"
source: "PythonPartsFramework\GeneralScripts\Palette\WpfPaletteBuilderUtils.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# WpfPaletteBuilderUtils

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\WpfPaletteBuilderUtils.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the wpf palette builder utils

## Abhängigkeiten

- `NemAll.Python.Palette.WPF.ViewModel`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `NemAll_Python_Palette`
- `__future__`
- `clr`
- `enum`
- `typing`

## Klassen

### `ConstructionPointSymbolType`

Enum representing flags for types of construction point symbols

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `WpfPaletteBuilderUtils`

implementation of the util functions for wpf palette builder
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `convert_double_str_to_palette_units` | `value_str: str, value_type: AllplanPalette.PaletteValueType` | `str` | Converts a double type value (length, angle), provided as a string,     to the units expected by the palette (mm)  Args:     value_str:  The numeric value as a string to be converted.      value_type: The type of the value to be converted (e.g. length, angle, etc.).  Returns:     str: The converted value formatted as a string        |
| `convert_double_str_list_to_palette_units` | `value_list_str: str, value_type: AllplanPalette.PaletteValueType` | `str` | Converts a list of length values, provided as a pipe-separated string, to the units expected by the palette.  Args:     value_list_str:  The numeric values as a pipe-separated string to be converted (e.g. "1.0|2.5|3.7").     value_type: The type of the value to be converted (e.g. length, angle, etc.).      Returns:     str: The converted values formatted as a pipe-separated string.         |
| `convert_length_to_palette_units` | `length_value: float` | `float` | Converts a length value to mm, as expected by the palette. Args:     length_value:  The length value in the python internal units              Returns:     The value converted to mm.        |
| `convert_angle_to_palette_units` | `angle_value: float` | `float` | Converts the angle value to rad, as expected by the palette. Args:     angle_value:  The angle value in the python internal units (deg)             Returns:     The value converted to rad. |
| `convert_to_DoubleValueType` | `value_type: AllplanPalette.PaletteValueType` | `DoubleValueType` | Converts PaletteValueType to .NET DoubleValueType.  Args:     value_type: The type of the value to be converted.  Returns:     DoubleValueType: The corresponding .NET DoubleValueType. |
| `get_string_index_in_fixture_list` | `string_list: Any, search_string: str` | `tuple[int, str]` | Gets the index of a string in a list of strings, ignoring any whitespace suffixes. Also returns the original value with trailing whitespaces if found.  Args:     string_list: List of strings (can be a .NET managed list)     search_string: The string to search for  Returns:     tuple[int, str]: A tuple containing:         - The index of the string if found, -1 otherwise         - The original string with whitespaces if found, empty string otherwise |
| `get_construction_point_symbol_type_filter` | `value_list: str` | `int` | Parses a pipe-separated string of point symbol types and returns combined flag value.  Args:     value_list: Pipe-separated string of symbol types (e.g. "LINE|ELEVATION")  Returns:     int: Combined flag value representing the filter for the point symbol types. |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the wpf palette builder utils
"""

from __future__ import annotations

from enum import Enum

from typing import Any

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Palette as AllplanPalette
import NemAll_Python_Geometry as AllplanGeo

import clr # pylint: disable=wrong-import-order

python_palette_dll_path = f"{AllplanSettings.AllplanPaths.GetPathOfApplication()}\\NemAll_Python_Palette_WPF.dll"

clr.AddReference(python_palette_dll_path)  # pylint: disable=no-member  # type: ignore

from NemAll.Python.Palette.WPF.ViewModel import ( # pylint: disable=wrong-import-order, wrong-import-position, import-error, no-name-in-module # type: ignore
    DoubleValueType
)

class ConstructionPointSymbolType(Enum):
    """Enum representing flags for types of construction point symbols"""
    ELEVATIONDIMENSION   = 1
    LINEDIMENSION        = 2
    ALIGNMENTDIMENSION   = 4
    CONSTRUCTIONELEMENT  = 8

class WpfPaletteBuilderUtils:
    """ implementation of the util functions for wpf palette builder
    """

    DOUBLE_VALUE_TYPE_MAPPING = {
        AllplanPalette.PaletteValueType.LENGTH: DoubleValueType.Length,
        AllplanPalette.PaletteValueType.ANGLE: DoubleValueType.Angle,
        AllplanPalette.PaletteValueType.DOUBLE: DoubleValueType.Double
    }

    @staticmethod
    def convert_double_str_to_palette_units(value_str:  str,
                                            value_type: AllplanPalette.PaletteValueType) -> str:
        """Converts a double type value (length, angle), provided as a string, 
           to the units expected by the palette (mm)

        Args:
            value_str:  The numeric value as a string to be converted. 
            value_type: The type of the value to be converted (e.g. length, angle, etc.).

        Returns:
            str: The converted value formatted as a string       
        """

        if value_type == AllplanPalette.PaletteValueType.LENGTH:
            return str(WpfPaletteBuilderUtils.convert_length_to_palette_units (float(value_str)))

        if value_type == AllplanPalette.PaletteValueType.ANGLE:
            return str(WpfPaletteBuilderUtils.convert_angle_to_palette_units (float(value_str)))

        return value_str

    @staticmethod
    def convert_double_str_list_to_palette_units(value_list_str: str,
                                                 value_type: AllplanPalette.PaletteValueType) -> str:
        """Converts a list of length values, provided as a pipe-separated string, to the units expected by the palette.

        Args:
            value_list_str:  The numeric values as a pipe-separated string to be converted (e.g. "1.0|2.5|3.7").
            value_type: The type of the value to be converted (e.g. length, angle, etc.).
            
        Returns:
            str: The converted values formatted as a pipe-separated string.        
        """
        if not value_list_str:
            return ""

        # Split the string by pipe character
        value_list = value_list_str.split('|')

        # Convert each value individually
        converted_values = []
        for value_str in value_list:
            converted_value = WpfPaletteBuilderUtils.convert_double_str_to_palette_units(value_str, value_type)
            converted_values.append(converted_value)

        # Join the converted values back with pipe separator
        return '|'.join(converted_values)

    @staticmethod
    def convert_length_to_palette_units(length_value: float) -> float:
        """Converts a length value to mm, as expected by the palette.
        Args:
            length_value:  The length value in the python internal units             
        Returns:
            The value converted to mm.       
        """

        length_factor = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        return length_value * length_factor

    @staticmethod
    def convert_angle_to_palette_units(angle_value: float) -> float:
        """Converts the angle value to rad, as expected by the palette.
        Args:
            angle_value:  The angle value in the python internal units (deg)            
        Returns:
            The value converted to rad.
        """

        return AllplanGeo.Angle.DegToRad(angle_value)

    @staticmethod
    def convert_to_DoubleValueType(value_type: AllplanPalette.PaletteValueType) -> DoubleValueType: # pylint: disable=invalid-name
        """Converts PaletteValueType to .NET DoubleValueType.

        Args:
            value_type: The type of the value to be converted.

        Returns:
            DoubleValueType: The corresponding .NET DoubleValueType.
        """

        # Return mapped value or default
        return WpfPaletteBuilderUtils.DOUBLE_VALUE_TYPE_MAPPING.get(value_type, None)

    @staticmethod
    def get_string_index_in_fixture_list(string_list:   Any,
                                         search_string: str) -> tuple[int, str]:
        """Gets the index of a string in a list of strings, ignoring any whitespace suffixes.
        Also returns the original value with trailing whitespaces if found.

        Args:
            string_list: List of strings (can be a .NET managed list)
            search_string: The string to search for

        Returns:
            tuple[int, str]: A tuple containing:
                - The index of the string if found, -1 otherwise
                - The original string with whitespaces if found, empty string otherwise
        """
        if not string_list or not search_string:
            return -1, ""

        # Iterate through the list
        for index, item in enumerate(string_list):
            item_str = str(item)

            # First strip all whitespaces from both sides
            cleaned_str = item_str.strip()

            # Remove the number prefix including the first space
            if (space_index := cleaned_str.find(' ')) != -1:
                cleaned_str = cleaned_str[space_index + 1:]

            if cleaned_str == search_string:
                return index, item_str

        return -1, ""

    @staticmethod
    def get_construction_point_symbol_type_filter(value_list: str) -> int:
        """Parses a pipe-separated string of point symbol types and returns combined flag value.

        Args:
            value_list: Pipe-separated string of symbol types (e.g. "LINE|ELEVATION")

        Returns:
            int: Combined flag value representing the filter for the point symbol types.
        """
        if not value_list:
            return 0

        result = 0

        for type_name in value_list.split('|'):
            try:
                result |= ConstructionPointSymbolType[type_name.strip().upper()].value
            except KeyError:
                continue

        return result

```

</details>