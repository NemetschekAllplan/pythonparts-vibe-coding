---
title: "Spline2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Spline2DImpl.py"
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


# Spline2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Spline2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Spline2D value type

## Abhängigkeiten

- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypes.GeometryElements.SplineImpl`
- `importlib`
- `typing`

## Klassen

### `Spline2DImpl`

implementation of the Spline2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Spline2D] | AllplanGeo.Spline2D` | get the 2D spline from a string  Args:     value_str: 2D spline string  Returns:     2D spline(s) |
| `__get_value_spline2d` | `value_str: str` | `AllplanGeo.Spline2D` | get a 2D spline from a value string  Args:     value_str: Value string  Returns:     2D spline |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Spline2D value type
"""

from typing import Any

import importlib

import NemAll_Python_Geometry as AllplanGeo

import ValueTypes.GeometryElements.SplineImpl as SplineImpl      # pylint: disable=consider-using-from-import

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .CoordinateValueUtil import CoordinateValueUtil

importlib.reload(SplineImpl)    # the module is not visible in the reload table!

class Spline2DImpl(SplineImpl.SplineImpl):
    """ implementation of the Spline2D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Spline2D] | AllplanGeo.Spline2D):
        """ get the 2D spline from a string

        Args:
            value_str: 2D spline string

        Returns:
            2D spline(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Spline2DImpl.__get_value_spline2d, value_str)


    @staticmethod
    def __get_value_spline2d(value_str: str) -> AllplanGeo.Spline2D:
        """ get a 2D spline from a value string

        Args:
            value_str: Value string

        Returns:
            2D spline
        """

        spline = AllplanGeo.Spline2D()

        if not value_str:
            return spline

        value_str = value_str.replace("Spline2D", "")

        spline.StartVector = CoordinateValueUtil.get_xy_element(StringToValueUtil.get_property_string(value_str, "StartVector", "(0,0)"),
                                                                AllplanGeo.Vector2D())
        spline.EndVector   = CoordinateValueUtil.get_xy_element(StringToValueUtil.get_property_string(value_str, "EndVector", "(0,0)"),
                                                                AllplanGeo.Vector2D())

        return CoordinateValueUtil.add_coordinates(spline, StringToValueUtil.get_property_string(value_str, "Points", value_str))

```

</details>