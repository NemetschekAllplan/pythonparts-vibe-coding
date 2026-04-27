---
title: "Spline3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Spline3DImpl.py"
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


# Spline3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Spline3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Spline3D value type

## Abhängigkeiten

- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `SplineImpl`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `typing`

## Klassen

### `Spline3DImpl`

implementation of the Spline3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Spline3D] | AllplanGeo.Spline3D` | get the 3D spline from a string  Args:     value_str: 3D spline string  Returns:     3D spline(s) |
| `__get_value_spline3d` | `value_str: str` | `AllplanGeo.Spline3D` | get a 3D spline from a value string  Args:     value_str: Value string  Returns:     3D spline |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Spline3D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .CoordinateValueUtil import CoordinateValueUtil
from .SplineImpl import SplineImpl

class Spline3DImpl(SplineImpl):
    """ implementation of the Spline3D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Spline3D] | AllplanGeo.Spline3D):
        """ get the 3D spline from a string

        Args:
            value_str: 3D spline string

        Returns:
            3D spline(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Spline3DImpl.__get_value_spline3d, value_str)


    @staticmethod
    def __get_value_spline3d(value_str: str) -> AllplanGeo.Spline3D:
        """ get a 3D spline from a value string

        Args:
            value_str: Value string

        Returns:
            3D spline
        """

        spline = AllplanGeo.Spline3D()

        if not value_str:
            return spline

        value_str = value_str.replace("Spline3D", "")

        spline.StartVector = CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "StartVector", "(0,0,0)"),
                                                                 AllplanGeo.Vector3D())
        spline.EndVector   = CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "EndVector", "(0,0,0)"),
                                                                 AllplanGeo.Vector3D())

        return CoordinateValueUtil.add_coordinates(spline, StringToValueUtil.get_property_string(value_str, "Points", value_str))

```

</details>