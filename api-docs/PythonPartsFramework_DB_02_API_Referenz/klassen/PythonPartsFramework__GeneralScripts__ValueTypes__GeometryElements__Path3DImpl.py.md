---
title: "Path3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Path3DImpl.py"
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


# Path3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Path3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Path3D value type

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `Path3DImpl`

implementation of the Path3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[AllplanGeo.Path3D] | AllplanGeo.Path3D` | get the 2D path from a string  Args:     value_str: 2D path string  Returns:     2D path(s) |
| `to_string` | `value: AllplanGeo.Path3D` | `str` | convert the path to a string  Args:     value: path value  Returns:     path as string |
| `__get_value_path3d` | `_value_str: str` | `AllplanGeo.Path3D` | get a 3D path from a value string  Args:     _value_str: Value string  Returns:     3D path |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Path3D value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ..ParameterPropertyValueType import ParameterPropertyValueType

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class Path3DImpl(ParameterPropertyValueType):
    """ implementation of the Path3D value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[AllplanGeo.Path3D] | AllplanGeo.Path3D):
        """ get the 2D path from a string

        Args:
            value_str: 2D path string

        Returns:
            2D path(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Path3DImpl.__get_value_path3d, value_str)


    @staticmethod
    def to_string(value: AllplanGeo.Path3D) -> str:
        """ convert the path to a string

        Args:
            value: path value

        Returns:
            path as string
        """

        return str(value).replace("\n", "").replace(" ", "")


    @staticmethod
    def __get_value_path3d(_value_str: str) -> AllplanGeo.Path3D:
        """ get a 3D path from a value string

        Args:
            _value_str: Value string

        Returns:
            3D path
        """

        return AllplanGeo.Path3D()

```

</details>