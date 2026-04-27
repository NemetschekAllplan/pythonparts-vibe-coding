---
title: "BRep3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BRep3DImpl.py"
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


# BRep3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BRep3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the BRep3D value type

## Abhängigkeiten

- `ControlProperties`
- `GeometryValidate`
- `Matrix3DImpl`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.PropertyPaletteGeometryControlService`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `typing`

## Klassen

### `BRep3DImpl`

implementation of the BRep3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, _name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     _name: name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanGeo.BRep3D` | `str` | convert the BRep3D to a string  Args:     value: arc value  Returns:     arc as string |
| `get_value` | `value_str: Any` | `list[AllplanGeo.BRep3D] | AllplanGeo.BRep3D` | get the 3D Polyhedron from a string  Args:     value_str: 3D Polyhedron string  Returns:     3D Polyhedron(s) |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__get_value_brep3d` | `value_str: str` | `AllplanGeo.BRep3D` | get a 3D brep from a value string  Args:     value_str: Value string  Returns:     3D brep |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the BRep3D value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING, cast

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

import GeometryValidate

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.PropertyPaletteGeometryControlService import PropertyPaletteGeometryControlService
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextData
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

from .Matrix3DImpl import Matrix3DImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class BRep3DImpl(ParameterPropertyValueType):
    """ implementation of the BRep3D value type
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
    def to_string(value: AllplanGeo.BRep3D) -> str:
        """ convert the BRep3D to a string

        Args:
            value: arc value

        Returns:
            arc as string
        """

        if value is None:
            return ""

        _, res, trans_mat = value.WriteToStream()

        return f"BRep3D(Body({res}),{ValueToStringUtil.to_string_strip(trans_mat)})"


    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.BRep3D] | AllplanGeo.BRep3D):
        """ get the 3D Polyhedron from a string

        Args:
            value_str: 3D Polyhedron string

        Returns:
            3D Polyhedron(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(BRep3DImpl.__get_value_brep3d, value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the control to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if prop.value == []:
            return

        value = cast(AllplanGeo.BRep3D, prop.value)

        error, vertices = value.GetVertices()

        if not GeometryValidate.element_method(error):
            return

        for i, pnt in enumerate(vertices):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     pnt, "",
                                                                     PropertyPaletteControlTextData(ctrl_props.text + str(i), ""),
                                                                     True, prop_pal_ctrl_service)


    @staticmethod
    def __get_value_brep3d(value_str: str) -> AllplanGeo.BRep3D:
        """ get a 3D brep from a value string

        Args:
            value_str: Value string

        Returns:
            3D brep
        """

        brep = AllplanGeo.BRep3D()

        if not value_str:
            return brep

        value_str = value_str.split("(", 1)[1][:-1]

        if not value_str or "RefPoint" in value_str:        # pylint: disable=magic-value-comparison
            return brep

        body_str, _, matrix_str = value_str.partition(",")

        trans_mat = Matrix3DImpl.get_value_matrix3d(matrix_str)

        brep.ReadFromStream(body_str.split("(")[1].rstrip(")"), trans_mat)

        return brep

```

</details>