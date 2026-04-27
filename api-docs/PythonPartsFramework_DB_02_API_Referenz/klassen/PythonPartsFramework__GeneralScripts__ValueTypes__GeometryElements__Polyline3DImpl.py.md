---
title: "Polyline3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polyline3DImpl.py"
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


# Polyline3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Polyline3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Polyline3D value type

## Abhängigkeiten

- `BasePolyPointsImpl`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.StringToValueUtil`
- `typing`

## Klassen

### `Polyline3DImpl`

implementation of the Polyline3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: Any` | `list[AllplanGeo.Polyline3D] | AllplanGeo.Polyline3D` | get the 3D polyline from a string  Args:     value_str: 3D polyline string  Returns:     3D polyline(s) |
| `__get_value_polyline3d` | `value_str: str` | `AllplanGeo.Polyline3D` | get a 3D polyline from a value string  Args:     value_str: Value string  Returns:     3D polyline |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Polyline3D value type
"""

from typing import Any

import NemAll_Python_Geometry as AllplanGeo

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

from .BasePolyPointsImpl import BasePolyPointsImpl
from .CoordinateValueUtil import CoordinateValueUtil

class Polyline3DImpl(BasePolyPointsImpl):
    """ implementation of the Polyline3D value type
    """

    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Polyline3D] | AllplanGeo.Polyline3D):
        """ get the 3D polyline from a string

        Args:
            value_str: 3D polyline string

        Returns:
            3D polyline(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Polyline3DImpl.__get_value_polyline3d, value_str)


    @staticmethod
    def __get_value_polyline3d(value_str: str) -> AllplanGeo.Polyline3D:
        """ get a 3D polyline from a value string

        Args:
            value_str: Value string

        Returns:
            3D polyline
        """

        if value_str.find("Point3D") == 0:      # Plate / created from Polyline
            property_string = StringToValueUtil.get_property_string(value_str, "Point3D", value_str.replace("Polyline3D", ""))

        elif value_str.find("Vector3D") == 0:   # Plate / Trapezoid
            property_string = StringToValueUtil.get_property_string(value_str, "Vector3D", value_str.replace("Polyline3D", ""))

        else:
            property_string = StringToValueUtil.get_property_string(value_str, "Points", value_str.replace("Polyline3D", ""))

        return CoordinateValueUtil.add_coordinates(AllplanGeo.Polyline3D(), property_string)

```

</details>