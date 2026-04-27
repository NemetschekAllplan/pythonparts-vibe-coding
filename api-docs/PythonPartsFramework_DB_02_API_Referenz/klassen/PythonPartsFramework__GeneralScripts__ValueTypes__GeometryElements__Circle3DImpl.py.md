---
title: "Circle3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Circle3DImpl.py"
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


# Circle3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Circle3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Circle2D value type

## Abhängigkeiten

- `CircleImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `math`
- `typing`

## Klassen

### `Circle3DImpl`

implementation of the Circle3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Arc3D] | AllplanGeo.Arc3D` | get the 3D circle from a string  Args:     value_str: 3D circle string  Returns:     3D circle(s) |
| `__get_value_circle3d` | `value_str: str` | `AllplanGeo.Arc3D` | get a 3D circle from a value string  Args:     value_str: Value string  Returns:     3D circle |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Circle2D value type
"""

from typing import Any

import math

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .CircleImpl import CircleImpl
from .CoordinateValueUtil import CoordinateValueUtil

class Circle3DImpl(CircleImpl):
    """ implementation of the Circle3D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Arc3D] | AllplanGeo.Arc3D):
        """ get the 3D circle from a string

        Args:
            value_str: 3D circle string

        Returns:
            3D circle(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Circle3DImpl.__get_value_circle3d, value_str)


    @staticmethod
    def __get_value_circle3d(value_str: str) -> AllplanGeo.Arc3D:
        """ get a 3D circle from a value string

        Args:
            value_str: Value string

        Returns:
            3D circle
        """

        if not value_str  or  value_str == CoordinateValueUtil.EMPTY_GEO:
            return AllplanGeo.Arc3D()

        return AllplanGeo.Arc3D(CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "CenterPoint", "()"),
                                                                    AllplanGeo.Point3D()),
                                AllplanGeo.Vector3D(1, 0, 0),
                                CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "ZAxis", "0,0,1"),
                                                                    AllplanGeo.Vector3D()),
                                StringToValueUtil.get_property_float(value_str, "MajorRadius", "0"),
                                StringToValueUtil.get_property_float(value_str, "MajorRadius", "0"),
                                0,
                                math.pi * 2)

```

</details>