---
title: "Path2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Path2DImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# Path2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Path2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Path2D value type

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `Path2DImpl`

implementation of the Path2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[AllplanGeo.Path2D] | AllplanGeo.Path2D` | get the 2D path from a string  Args:     value_str: 2D path string  Returns:     2D path(s) |
| `to_string` | `value: AllplanGeo.Path2D` | `str` | convert the path to a string  Args:     value: path value  Returns:     path as string |
| `__get_value_path2d` | `_value_str: str` | `AllplanGeo.Path2D` | get a 2D path from a value string  Args:     _value_str: Value string  Returns:     2D path |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Path2D value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class Path2DImpl(ParameterPropertyValueType):
    """ implementation of the Path2D value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[AllplanGeo.Path2D] | AllplanGeo.Path2D):
        """ get the 2D path from a string

        Args:
            value_str: 2D path string

        Returns:
            2D path(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Path2DImpl.__get_value_path2d, value_str)


    @staticmethod
    def to_string(value: AllplanGeo.Path2D) -> str:
        """ convert the path to a string

        Args:
            value: path value

        Returns:
            path as string
        """

        return str(value).replace("\n", "").replace(" ", "")


    @staticmethod
    def __get_value_path2d(_value_str: str) -> AllplanGeo.Path2D:
        """ get a 2D path from a value string

        Args:
            _value_str: Value string

        Returns:
            2D path
        """

        return AllplanGeo.Path2D()

```

</details>