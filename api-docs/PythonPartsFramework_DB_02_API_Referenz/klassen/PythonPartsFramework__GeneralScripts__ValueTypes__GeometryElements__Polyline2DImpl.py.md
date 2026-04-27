---
title: "Polyline2DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polyline2DImpl.py"
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


# Polyline2DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polyline2DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Polyline2D value type

## Abhängigkeiten

- `BasePolyPointsImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `typing`

## Klassen

### `Polyline2DImpl`

implementation of the Polyline2D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Polyline2D] | AllplanGeo.Polyline2D` | get the 2D polyline from a string  Args:     value_str: 2D polyline string  Returns:     2D polyline(s) |
| `__get_value_polyline2d` | `value_str: str` | `AllplanGeo.Polyline2D` | get a 2D polyline from a value string  Args:     value_str: Value string  Returns:     2D polyline |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Polyline2D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .BasePolyPointsImpl import BasePolyPointsImpl
from .CoordinateValueUtil import CoordinateValueUtil

class Polyline2DImpl(BasePolyPointsImpl):
    """ implementation of the Polyline2D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Polyline2D] | AllplanGeo.Polyline2D):
        """ get the 2D polyline from a string

        Args:
            value_str: 2D polyline string

        Returns:
            2D polyline(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Polyline2DImpl.__get_value_polyline2d, value_str)


    @staticmethod
    def __get_value_polyline2d(value_str: str) -> AllplanGeo.Polyline2D:
        """ get a 2D polyline from a value string

        Args:
            value_str: Value string

        Returns:
            2D polyline
        """

        if value_str.find("Point2D") == 0:    # Plate / created from Polyline
            property_string = StringToValueUtil.get_property_string(value_str, "Point2D", value_str.replace("Polyline2D", ""))

        elif value_str.find("Vector2D") == 0:    # Plate / Trapezoid
            property_string = StringToValueUtil.get_property_string(value_str, "Vector2D", value_str.replace("Polyline2D", ""))

        else:
            property_string = StringToValueUtil.get_property_string(value_str, "Points", value_str.replace("Polyline2D", ""))

        return CoordinateValueUtil.add_coordinates(AllplanGeo.Polyline2D(), property_string)

```

</details>