---
title: "Plane3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Plane3DImpl.py"
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


# Plane3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\Plane3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Plane3D value type

## Abhängigkeiten

- `ControlProperties`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `Utilities.ConditionUtil`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.PropertyPaletteGeometryControlService`
- `ValueTypeUtils.StringToValueUtil`
- `collections.abc`
- `typing`

## Klassen

### `Plane3DImpl`

implementation of the Plane3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanGeo.AxisPlacement2D | AllplanGeo.Plane3D` | `str` | convert the plane to a string  Args:     value: plane value  Returns:     plane as string |
| `get_value` | `value_str: Any` | `list[AllplanGeo.Plane3D] | AllplanGeo.Plane3D` | get the 3d plane from a string  Args:     value_str: 3D plane string  Returns:     3D plane(s) |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__visit_Point` | `plane: list[AllplanGeo.Plane3D] | AllplanGeo.Plane3D, sep_count: int, name: str, value: Any` | `bool` | modify the center point  Args:     plane:     plane     sep_count: sub value separator count     name:      name of the modified property     value:     new value  Returns:     palette update state |
| `__visit_Vector` | `plane: list[AllplanGeo.Plane3D] | AllplanGeo.Plane3D, sep_count: int, name: str, value: Any` | `bool` | modify the vector  Args:     plane:     plane     sep_count: sub value separator count     name:      name of the modified property     value:     new value  Returns:     palette update state |
| `__set_vector` | `plane: list[AllplanGeo.Plane3D] | AllplanGeo.Plane3D, sep_count: int, name: str, value: Any, vector_fct: Callable[[Any, Any], None], vector_coord_fct: Callable[[Any, str, Any], None]` | `None` | modify the vector  Args:     plane:            plane(s)     sep_count:        sub value separator count     name:             name of the modified property     value:            new value     vector_fct:       vector function     vector_coord_fct: vector coordinate function |
| `__set_vector_value` | `plane: AllplanGeo.Plane3D, value: AllplanGeo.Vector3D` | `None` | set the vector  Args:     plane: plane     value: x axis |
| `__set_vector_coord` | `plane: AllplanGeo.Plane3D, name: str, value: AllplanGeo.Vector3D` | `None` | set the vector coordinate  Args:     plane: plane     name:  name of the modified property     value: x axis |
| `__get_value_plane3d` | `value_str: str` | `AllplanGeo.Plane3D` | get a 3D plane from a value string  Args:     value_str: Value string  Returns:     3D plane |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Plane3D value type
"""

# pylint: disable=invalid-name
# pylint: disable=unused-private-member

from typing import Any

from collections.abc import Callable

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil

from .CoordinateValueUtil import CoordinateValueUtil

from ..ParameterPropertyValueType import ParameterPropertyValueType

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextUtil
from ..ValueTypeUtils.PropertyPaletteGeometryControlService import PropertyPaletteGeometryControlService
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil

class Plane3DImpl(ParameterPropertyValueType):
    """ implementation of the Plane3D value type
    """

    @staticmethod
    def set_property_value(prop : ParameterProperty,
                           name : str,
                           value: Any) -> bool:
        """ Set the value of the property

        Args:
            prop:  property
            name:  name of the modified property
            value: new value

        Returns:
            update palette state
        """

        if value is None:
            return False

        prop.is_modified = True


        #----------------- assign the new value in case of a full element

        sep_count = name.count(".")

        if CoordinateValueUtil.SUB_NAME_SEPARATOR not in name and not sep_count:
            prop.value = value

            return True


        #----------------- part can't be an empty list

        if value == []:
            return False


        #----------------- set the new value

        visit_key = f"_Plane3DImpl__visit_{name.split('.', 2)[1]}"

        plane = ParameterPropertyListUtil.get_item_value(prop, name)

        if (visitor := getattr(Plane3DImpl, visit_key, None)) is not None:
            return visitor(plane, sep_count, name, value)                       # pylint: disable=not-callable

        return False


    @staticmethod
    def to_string(value: (AllplanGeo.AxisPlacement2D | AllplanGeo.Plane3D)) -> str:
        """ convert the plane to a string

        Args:
            value: plane value

        Returns:
            plane as string
        """

        return str(value).replace("\n", "").replace(" ", "")


    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.Plane3D]| AllplanGeo.Plane3D):
        """ get the 3d plane from a string

        Args:
            value_str: 3D plane string

        Returns:
            3D plane(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(Plane3DImpl.__get_value_plane3d, value_str)


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

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        text_util = PropertyPaletteControlTextUtil(prop_pal_ctrl_service.global_str_table)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Point",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.Point, "Point",
                                                                     text_util.get_row_name_text(ctrl_props, "Point", "e_CENTER_POINT"),
                                                                     True, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Vector",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_direction_vector_to_palette(
                                                                     wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.Vector, "Vector",
                                                                     text_util.get_row_name_text(ctrl_props, "Vector", "e_Z_AXIS"),
                                                                     True, prop_pal_ctrl_service)


    @staticmethod
    def __visit_Point(plane    : (list[AllplanGeo.Plane3D] | AllplanGeo.Plane3D),
                      sep_count: int,
                      name     : str,
                      value    : Any) -> bool:
        """ modify the center point

        Args:
            plane:     plane
            sep_count: sub value separator count
            name:      name of the modified property
            value:     new value

        Returns:
            palette update state
        """

        if sep_count == 1:
            ParameterPropertyListUtil.set_sub_item_value(plane, "Point", value)

        else:
            CoordinateValueUtil.set_sub_item_coordinate_value(plane, name, value)

        return False


    @staticmethod
    def __visit_Vector(plane    : (list[AllplanGeo.Plane3D] | AllplanGeo.Plane3D),
                       sep_count: int,
                       name     : str,
                       value    : Any) -> bool:
        """ modify the vector

        Args:
            plane:     plane
            sep_count: sub value separator count
            name:      name of the modified property
            value:     new value

        Returns:
            palette update state
        """

        Plane3DImpl.__set_vector(plane, sep_count, name, value,
                                 Plane3DImpl.__set_vector_value, Plane3DImpl.__set_vector_coord)

        return True


    @staticmethod
    def __set_vector(plane           : (list[AllplanGeo.Plane3D] | AllplanGeo.Plane3D),
                     sep_count       : int,
                     name            : str,
                     value           : Any,
                     vector_fct      : Callable[[Any, Any], None],
                     vector_coord_fct: Callable[[Any, str, Any], None]):
        """ modify the vector

        Args:
            plane:            plane(s)
            sep_count:        sub value separator count
            name:             name of the modified property
            value:            new value
            vector_fct:       vector function
            vector_coord_fct: vector coordinate function
        """

        #------------- vector value

        if sep_count == 1:
            if isinstance(plane, list):
                for item in plane:
                    vector_fct(item, value)
            else:
                vector_fct(plane, value)


        #------------- coordinate part value

        elif isinstance(plane, list):
            for item in plane:
                vector_coord_fct(item, name, value)

        else:
            vector_coord_fct(plane, name, value)


    @staticmethod
    def __set_vector_value(plane: AllplanGeo.Plane3D,
                           value: AllplanGeo.Vector3D):
        """ set the vector

        Args:
            plane: plane
            value: x axis
        """

        plane.Vector = value


    @staticmethod
    def __set_vector_coord(plane: AllplanGeo.Plane3D,
                           name : str,
                           value: AllplanGeo.Vector3D):
        """ set the vector coordinate

        Args:
            plane: plane
            name:  name of the modified property
            value: x axis
        """

        plane.Vector = CoordinateValueUtil.set_coordinate_value(plane.Vector, name, value)


    @staticmethod
    def __get_value_plane3d(value_str: str) -> AllplanGeo.Plane3D:
        """ get a 3D plane from a value string

        Args:
            value_str: Value string

        Returns:
            3D plane
        """

        if not value_str:
            return AllplanGeo.Plane3D()

        value_str = value_str.replace("Plane3D", "").replace("Normal", "Vector")

        return AllplanGeo.Plane3D(CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "Point", "(0,0,0)"),
                                                                      AllplanGeo.Point3D()),
                                  CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "Vector", "(0,0,0)"),
                                                                      AllplanGeo.Vector3D()))

```

</details>