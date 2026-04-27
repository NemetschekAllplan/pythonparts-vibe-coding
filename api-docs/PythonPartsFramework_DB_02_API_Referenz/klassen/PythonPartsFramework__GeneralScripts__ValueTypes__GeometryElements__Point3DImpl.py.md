---
title: "Point3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Point3DImpl.py"
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


# Point3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Point3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Point3D value type

## Abhängigkeiten

- `CoordinateImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ParameterProperty`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `Point3DImpl`

implementation of the Point3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[AllplanGeo.Point3D] | AllplanGeo.Point3D` | get the 3D point from a string  Args:     value_str: 3D point string  Returns:     3D point(s) |
| `__get_value_point3d` | `value_str: str` | `AllplanGeo.Point3D` | get a 3D point from a value string  Args:     value_str: Value string  Returns:     3D point |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Point3D value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

from .CoordinateImpl import CoordinateImpl
from .CoordinateValueUtil import CoordinateValueUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class Point3DImpl(CoordinateImpl):
    """ implementation of the Point3D value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[AllplanGeo.Point3D] | AllplanGeo.Point3D):
        """ get the 3D point from a string

        Args:
            value_str: 3D point string

        Returns:
            3D point(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Point3DImpl.__get_value_point3d, value_str)


    @staticmethod
    def __get_value_point3d(value_str: str) -> AllplanGeo.Point3D:
        """ get a 3D point from a value string

        Args:
            value_str: Value string

        Returns:
            3D point
        """

        return CoordinateValueUtil.get_xyz_element(value_str.replace("Point3D", ""), AllplanGeo.Point3D())

```

</details>