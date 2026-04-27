---
title: "GeometryStringValueConverter"
source: "PythonPartsFramework\Utils\GeometryStringValueConverter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# GeometryStringValueConverter

> **Pfad:** `PythonPartsFramework\Utils\GeometryStringValueConverter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`, `werte`

## Übersicht

implementation of the geometry string and value converter

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `StringToValueConverter`
- `ValueToStringConverter`
- `ValueTypes.ParameterPropertyValueTypes`
- `typing`

## Klassen

### `GeometryStringValueConverter`

implementation of the geometry string and value converter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_element` | `geometry_ele_str: str` | `Any` | get the elements from a string  Args:     geometry_ele_str: geometry element string  Returns:     value of the geometry element |
| `get_elements` | `geometry_ele_str_list: List[str], convert_to_3d: bool` | `List[Any]` | get the elements from a string  Args:     geometry_ele_str_list: list with the geometry element strings     convert_to_3d:         convert the elements to 3D elements state  Returns:     value of the geometry element |
| `to_string` | `geometry_ele: Any` | `str` | convert the geometry_ele to a string  Args:     geometry_ele: geometry element  Returns:     string from geometry element |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the geometry string and value converter
"""

from typing import Any, List

import NemAll_Python_Geometry as AllplanGeo

from StringToValueConverter import StringToValueConverter
from ValueToStringConverter import ValueToStringConverter

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

class GeometryStringValueConverter():
    """ implementation of the geometry string and value converter
    """

    @staticmethod
    def get_element(geometry_ele_str: str) -> Any:
        """ get the elements from a string

        Args:
            geometry_ele_str: geometry element string

        Returns:
            value of the geometry element
        """

        return StringToValueConverter.get_value(ParameterPropertyValueTypes.GEOMETRY_OBJECT, geometry_ele_str)


    @staticmethod
    def get_elements(geometry_ele_str_list: List[str],
                     convert_to_3d        : bool) -> List[Any]:
        """ get the elements from a string

        Args:
            geometry_ele_str_list: list with the geometry element strings
            convert_to_3d:         convert the elements to 3D elements state

        Returns:
            value of the geometry element
        """

        if convert_to_3d:
            return [AllplanGeo.ConvertTo3D(GeometryStringValueConverter.get_element(geo_ele_string))[1] \
                    for geo_ele_string in geometry_ele_str_list]

        return [GeometryStringValueConverter.get_element(geo_ele_string) for geo_ele_string in geometry_ele_str_list]


    @staticmethod
    def to_string(geometry_ele: Any) -> str:
        """ convert the geometry_ele to a string

        Args:
            geometry_ele: geometry element

        Returns:
            string from geometry element
        """

        return ValueToStringConverter.to_string_from_value(geometry_ele, ParameterPropertyValueTypes.GEOMETRY_OBJECT, None)

```

</details>