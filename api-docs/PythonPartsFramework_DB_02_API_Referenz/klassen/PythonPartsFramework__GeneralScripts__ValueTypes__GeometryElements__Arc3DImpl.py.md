---
title: "Arc3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Arc3DImpl.py"
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


# Arc3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Arc3DImpl.py`  
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

### `Arc3DImpl`

implementation of the Arc3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Arc3D] | AllplanGeo.Arc3D` | get the 3D arc from a string  Args:     value_str: 3D arc string  Returns:     3D arc(s) |
| `__get_value_arc3d` | `value_str: str` | `AllplanGeo.Arc3D` | get a 3D arc from a value string  Args:     value_str: Value string  Returns:     3D arc |

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

class Arc3DImpl(ArcImpl):
    """ implementation of the Arc3D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Arc3D] | AllplanGeo.Arc3D):
        """ get the 3D arc from a string

        Args:
            value_str: 3D arc string

        Returns:
            3D arc(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Arc3DImpl.__get_value_arc3d, value_str)


    @staticmethod
    def __get_value_arc3d(value_str: str) -> AllplanGeo.Arc3D:
        """ get a 3D arc from a value string

        Args:
            value_str: Value string

        Returns:
            3D arc
        """

        if not value_str  or  value_str == CoordinateValueUtil.EMPTY_GEO:
            return AllplanGeo.Arc3D()

        return AllplanGeo.Arc3D(CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "CenterPoint", "()"),
                                                                    AllplanGeo.Point3D()),
                                CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "XDirection", "1,0,0"),
                                                                    AllplanGeo.Vector3D()),
                                CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "ZAxis", "0,0,1"),
                                                                    AllplanGeo.Vector3D()),
                                StringToValueUtil.get_property_float(value_str, "MinorRadius", "0"),
                                StringToValueUtil.get_property_float(value_str, "MajorRadius", "0"),
                                StringToValueUtil.get_property_angle(value_str, "StartAngle", "0"),
                                StringToValueUtil.get_property_angle(value_str, "EndAngle", "0"),
                                StringToValueUtil.get_property_bool(value_str, "IsCounterClockwise", True))

```

</details>