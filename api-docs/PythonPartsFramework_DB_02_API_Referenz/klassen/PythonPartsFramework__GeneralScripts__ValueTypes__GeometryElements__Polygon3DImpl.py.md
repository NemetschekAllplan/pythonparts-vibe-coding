---
title: "Polygon3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polygon3DImpl.py"
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


# Polygon3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polygon3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Polygon3D value type

## Abhängigkeiten

- `BasePolyPointsImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `typing`

## Klassen

### `Polygon3DImpl`

implementation of the Polygon3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Polygon3D] | AllplanGeo.Polygon3D` | get the 3D polygon from a string  Args:     value_str: 3D polygon string  Returns:     3D polygon(s) |
| `__get_value_polygon3d` | `value_str: str` | `AllplanGeo.Polygon3D` | get a 3D polygon from a value string  Args:     value_str: Value string  Returns:     3D polygon |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Polygon3D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .BasePolyPointsImpl import BasePolyPointsImpl
from .CoordinateValueUtil import CoordinateValueUtil

class Polygon3DImpl(BasePolyPointsImpl):
    """ implementation of the Polygon3D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Polygon3D] | AllplanGeo.Polygon3D):
        """ get the 3D polygon from a string

        Args:
            value_str: 3D polygon string

        Returns:
            3D polygon(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Polygon3DImpl.__get_value_polygon3d, value_str)


    @staticmethod
    def __get_value_polygon3d(value_str: str) -> AllplanGeo.Polygon3D:
        """ get a 3D polygon from a value string

        Args:
            value_str: Value string

        Returns:
            3D polygon
        """

        poly = CoordinateValueUtil.add_coordinates(AllplanGeo.Polygon3D(),
                                                   StringToValueUtil.get_property_string(value_str, "Points",
                                                                                         value_str.replace("Polygon3D", "")))

        if poly.Empty():
            return poly

        if not AllplanGeo.Comparison.Equal(poly.StartPoint, poly.EndPoint):
            poly += poly.StartPoint

        return poly

```

</details>