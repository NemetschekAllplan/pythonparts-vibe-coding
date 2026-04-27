---
title: "Polygon2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polygon2DImpl.py"
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


# Polygon2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polygon2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Polygon2D value type

## Abhängigkeiten

- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypes.GeometryElements.BasePolyPointsImpl`
- `importlib`
- `typing`

## Klassen

### `Polygon2DImpl`

implementation of the Polygon2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Polygon2D] | AllplanGeo.Polygon2D` | get the 2D polygon from a string  Args:     value_str: 2D polygon string  Returns:     2D polygon(s) |
| `__get_value_polygon2d` | `value_str: str` | `AllplanGeo.Polygon2D` | get a 2D polygon from a value string  Args:     value_str: Value string  Returns:     2D polygon |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Polygon2D value type
"""

from typing import Any

import importlib

import NemAll_Python_Geometry as AllplanGeo

import ValueTypes.GeometryElements.BasePolyPointsImpl as BasePolyPointsImpl      # pylint: disable=consider-using-from-import

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .CoordinateValueUtil import CoordinateValueUtil

importlib.reload(BasePolyPointsImpl)    # the module is not visible in the reload table!

class Polygon2DImpl(BasePolyPointsImpl.BasePolyPointsImpl):
    """ implementation of the Polygon2D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Polygon2D] | AllplanGeo.Polygon2D):
        """ get the 2D polygon from a string

        Args:
            value_str: 2D polygon string

        Returns:
            2D polygon(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Polygon2DImpl.__get_value_polygon2d, value_str)


    @staticmethod
    def __get_value_polygon2d(value_str: str) -> AllplanGeo.Polygon2D:
        """ get a 2D polygon from a value string

        Args:
            value_str: Value string

        Returns:
            2D polygon
        """

        poly = CoordinateValueUtil.add_coordinates(AllplanGeo.Polygon2D(),
                                                   StringToValueUtil.get_property_string(value_str, "Points",
                                                                                         value_str.replace("Polygon2D", "")))

        if poly.Empty():
            return poly

        if not AllplanGeo.Comparison.Equal(poly.StartPoint, poly.EndPoint):
            poly += poly.StartPoint

        return poly

```

</details>