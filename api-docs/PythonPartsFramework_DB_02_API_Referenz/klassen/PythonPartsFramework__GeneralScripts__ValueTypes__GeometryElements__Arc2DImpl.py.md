---
title: "Arc2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Arc2DImpl.py"
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


# Arc2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Arc2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Arc2D value type

## Abhängigkeiten

- `ArcImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `typing`

## Klassen

### `Arc2DImpl`

implementation of the Arc2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Arc2D] | AllplanGeo.Arc2D` | get the 2D arc from a string  Args:     value_str: 2D arc string  Returns:     2D arc(s) |
| `get_value_arc2d` | `value_str: str` | `AllplanGeo.Arc2D` | get a 2D arc from a value string  Args:     value_str: Value string  Returns:     2D arc |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Arc2D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .ArcImpl import ArcImpl
from .CoordinateValueUtil import CoordinateValueUtil

class Arc2DImpl(ArcImpl):
    """ implementation of the Arc2D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Arc2D] | AllplanGeo.Arc2D):
        """ get the 2D arc from a string

        Args:
            value_str: 2D arc string

        Returns:
            2D arc(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Arc2DImpl.get_value_arc2d, value_str)


    @staticmethod
    def get_value_arc2d(value_str: str) -> AllplanGeo.Arc2D:
        """ get a 2D arc from a value string

        Args:
            value_str: Value string

        Returns:
            2D arc
        """

        if not value_str  or  value_str == CoordinateValueUtil.EMPTY_GEO:
            return AllplanGeo.Arc2D()

        return AllplanGeo.Arc2D(CoordinateValueUtil.get_xy_element(StringToValueUtil.get_property_string(value_str, "CenterPoint", "(0,0)"),
                                                                   AllplanGeo.Point2D()),
                                StringToValueUtil.get_property_float(value_str, "MinorRadius", "0"),
                                StringToValueUtil.get_property_float(value_str, "MajorRadius", "0"),
                                StringToValueUtil.get_property_angle(value_str, "AxisAngle", "0"),
                                StringToValueUtil.get_property_angle(value_str, "StartAngle", "0"),
                                StringToValueUtil.get_property_angle(value_str, "EndAngle", "0"),
                                StringToValueUtil.get_property_bool(value_str, "IsCounterClockwise", True))

```

</details>