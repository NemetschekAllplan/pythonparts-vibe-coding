---
title: "Matrix3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Matrix3DImpl.py"
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


# Matrix3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Matrix3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Matrix3D value type

## Abhängigkeiten

- `ControlProperties`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `typing`

## Klassen

### `Matrix3DImpl`

implementation of the Matrix3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, _name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     _name: name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanGeo.Matrix3D` | `str` | convert the matrix to a string  Args:     value: arc value  Returns:     arc as string |
| `get_value` | `value_str: Any` | `list[AllplanGeo.Matrix3D] | AllplanGeo.Matrix3D` | get the matrix from a string  Args:     value_str: matrix string  Returns:     matrix |
| `add_to_palette` | `_wpf_palette: WpfPaletteBuilder, _prop: ParameterProperty, _ctrl_props: ControlProperties, _prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     _wpf_palette:           WPf palette     _prop:                  parameter property     _ctrl_props:            control properties     _prop_pal_ctrl_service: property palette control service |
| `get_value_matrix3d` | `value_str: str` | `AllplanGeo.Matrix3D` | get a 3D matrix from a value string  Args:     value_str: Value string  Returns:     3D matrix |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Matrix3D value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..ParameterPropertyValueType import ParameterPropertyValueType

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

from .CoordinateValueUtil import CoordinateValueUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class Matrix3DImpl(ParameterPropertyValueType):
    """ implementation of the Matrix3D value type
    """

    @staticmethod
    def set_property_value(prop : ParameterProperty,
                           _name: str,
                           value: Any) -> bool:
        """ Set the value of the property

        Args:
            prop:  property
            _name: name of the modified property
            value: new value

        Returns:
            update palette state
        """

        if value is None:
            return False

        prop.is_modified = True

        prop.value = value

        return True


    @staticmethod
    def to_string(value: AllplanGeo.Matrix3D) -> str:
        """ convert the matrix to a string

        Args:
            value: arc value

        Returns:
            arc as string
        """

        return ValueToStringUtil.to_string_strip(value)


    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Matrix3D] | AllplanGeo.Matrix3D):
        """ get the matrix from a string

        Args:
            value_str: matrix string

        Returns:
            matrix
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Matrix3DImpl.get_value_matrix3d, value_str)


    @staticmethod
    def add_to_palette(_wpf_palette          : WpfPaletteBuilder,
                       _prop                 : ParameterProperty,
                       _ctrl_props           : ControlProperties,
                       _prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the control to the palette

        Args:
            _wpf_palette:           WPf palette
            _prop:                  parameter property
            _ctrl_props:            control properties
            _prop_pal_ctrl_service: property palette control service
        """


    @staticmethod
    def get_value_matrix3d(value_str: str) -> AllplanGeo.Matrix3D:
        """ get a 3D matrix from a value string

        Args:
            value_str: Value string

        Returns:
            3D matrix
        """

        if not value_str:
            return AllplanGeo.Matrix3D()

        value_list = CoordinateValueUtil.get_coordinates_list(StringToValueUtil.get_property_string(value_str, "Matrix3D",
                                                                                                    value_str.replace("Matrix3D", "")))

        if not value_list:
            return AllplanGeo.Matrix3D()

        value_list = value_list[0]

        return AllplanGeo.Matrix3D(value_list[0], value_list[1], value_list[2], value_list[3],
                                   value_list[4], value_list[5], value_list[6], value_list[7],
                                   value_list[8], value_list[9], value_list[10], value_list[11],
                                   value_list[12], value_list[13], value_list[14], value_list[15])

```

</details>