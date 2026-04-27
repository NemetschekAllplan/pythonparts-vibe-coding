---
title: "AxisPlacement3DImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\AxisPlacement3DImpl.py"
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


# AxisPlacement3DImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\AxisPlacement3DImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the AxisPlacement3D value type

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

### `AxisPlacement3DImpl`

implementation of the AxisPlacement3D value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanGeo.AxisPlacement2D | AllplanGeo.AxisPlacement3D` | `str` | convert the axis placement to a string  Args:     value: axis placement value  Returns:     axis placement as string |
| `get_value` | `value_str: Any` | `list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D` | get the 3d axis placement from a string  Args:     value_str: 3D axis placement string  Returns:     3D axis placement(s) |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__visit_Origin` | `axis_placement: list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D, sep_count: int, name: str, value: Any` | `bool` | modify the center point  Args:     axis_placement: axis placement     sep_count:      sub value separator count     name:           name of the modified property     value:          new value  Returns:     palette update state |
| `__visit_XDirection` | `axis_placement: list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D, sep_count: int, name: str, value: Any` | `bool` | modify the x axis  Args:     axis_placement: axis placement     sep_count:      sub value separator count     name:           name of the modified property     value:          new value  Returns:     palette update state |
| `__visit_ZDirection` | `axis_placement: list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D, sep_count: int, name: str, value: Any` | `bool` | modify the z axis  Args:     axis_placement: axis placement     sep_count:      sub value separator count     name:           name of the modified property     value:          new value  Returns:     palette update state |
| `__set_axis` | `axis_placement: list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D, sep_count: int, name: str, value: Any, axis_fct: Callable[[Any, Any], None], axis_coord_fct: Callable[[Any, str, Any], None]` | `None` | modify the z axis  Args:     axis_placement: axis_placement(s)     sep_count:      sub value separator count     name:           name of the modified property     value:          new value     axis_fct:       axis function     axis_coord_fct: axis coordinate function |
| `__set_x_axis` | `axis_placement: AllplanGeo.AxisPlacement3D, value: AllplanGeo.Vector3D` | `None` | set the x axis  Args:     axis_placement:   axis_placement     value: x axis |
| `__set_x_axis_coord` | `axis_placement: AllplanGeo.AxisPlacement3D, name: str, value: AllplanGeo.Vector3D` | `None` | set the x axis  Args:     axis_placement:   axis_placement     name:  name of the modified property     value: x axis |
| `__set_z_axis` | `axis_placement: AllplanGeo.AxisPlacement3D, value: AllplanGeo.Vector3D` | `None` | set the z axis  Args:     axis_placement:   axis_placement     value: z axis |
| `__set_z_axis_coord` | `axis_placement: AllplanGeo.AxisPlacement3D, name: str, value: AllplanGeo.Vector3D` | `None` | set the z axis  Args:     axis_placement:   axis_placement     name:  name of the modified property     value: z axis |
| `__get_value_axisplacement3d` | `value_str: str` | `AllplanGeo.AxisPlacement3D` | get a 3D axis placement from a value string  Args:     value_str: Value string  Returns:     3D axis placement |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the AxisPlacement3D value type
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

class AxisPlacement3DImpl(ParameterPropertyValueType):
    """ implementation of the AxisPlacement3D value type
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

        visit_key = f"_AxisPlacement3DImpl__visit_{name.split('.', 2)[1]}"

        axis_placement = ParameterPropertyListUtil.get_item_value(prop, name)

        if (visitor := getattr(AxisPlacement3DImpl, visit_key, None)) is not None:
            return visitor(axis_placement, sep_count, name, value)                  # pylint: disable=not-callable

        return False


    @staticmethod
    def to_string(value: (AllplanGeo.AxisPlacement2D | AllplanGeo.AxisPlacement3D)) -> str:
        """ convert the axis placement to a string

        Args:
            value: axis placement value

        Returns:
            axis placement as string
        """

        return str(value).replace("\n", "").replace(" ", "")


    @staticmethod
    def get_value(value_str: Any) -> (list[AllplanGeo.AxisPlacement3D]| AllplanGeo.AxisPlacement3D):
        """ get the 3d axis placement from a string

        Args:
            value_str: 3D axis placement string

        Returns:
            3D axis placement(s)
        """

        return BaseStringToValueConverter.to_value_by_type_converter(AxisPlacement3DImpl.__get_value_axisplacement3d, value_str)


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

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Origin",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.Origin, "Origin",
                                                                     text_util.get_row_name_text(ctrl_props, "Origin", "e_CENTER_POINT"),
                                                                     True, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.XDirection",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_direction_vector_to_palette(
                                                                     wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.XDirection, "XDirection",
                                                                     text_util.get_row_name_text(ctrl_props, "XDirection", "e_X_AXIS"),
                                                                     True, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.ZDirection",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_direction_vector_to_palette(
                                                                     wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.ZDirection, "ZDirection",
                                                                     text_util.get_row_name_text(ctrl_props, "ZDirection", "e_Z_AXIS"),
                                                                     True, prop_pal_ctrl_service)


    @staticmethod
    def __visit_Origin(axis_placement: (list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D),
                       sep_count     : int,
                       name          : str,
                       value         : Any) -> bool:
        """ modify the center point

        Args:
            axis_placement: axis placement
            sep_count:      sub value separator count
            name:           name of the modified property
            value:          new value

        Returns:
            palette update state
        """

        if sep_count == 1:
            ParameterPropertyListUtil.set_sub_item_value(axis_placement, "Origin", value)

        else:
            CoordinateValueUtil.set_sub_item_coordinate_value(axis_placement, name, value)

        return False


    @staticmethod
    def __visit_XDirection(axis_placement: (list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D),
                           sep_count     : int,
                           name          : str,
                           value         : Any) -> bool:
        """ modify the x axis

        Args:
            axis_placement: axis placement
            sep_count:      sub value separator count
            name:           name of the modified property
            value:          new value

        Returns:
            palette update state
        """

        AxisPlacement3DImpl.__set_axis(axis_placement, sep_count, name, value,
                                       AxisPlacement3DImpl.__set_x_axis, AxisPlacement3DImpl.__set_x_axis_coord)

        return True


    @staticmethod
    def __visit_ZDirection(axis_placement: (list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D),
                           sep_count     : int,
                           name          : str,
                           value         : Any) -> bool:
        """ modify the z axis

        Args:
            axis_placement: axis placement
            sep_count:      sub value separator count
            name:           name of the modified property
            value:          new value

        Returns:
            palette update state
        """

        AxisPlacement3DImpl.__set_axis(axis_placement, sep_count, name, value,
                                       AxisPlacement3DImpl.__set_z_axis, AxisPlacement3DImpl.__set_z_axis_coord)

        return True


    @staticmethod
    def __set_axis(axis_placement: (list[AllplanGeo.AxisPlacement3D] | AllplanGeo.AxisPlacement3D),
                   sep_count     : int,
                   name          : str,
                   value         : Any,
                   axis_fct      : Callable[[Any, Any], None],
                   axis_coord_fct: Callable[[Any, str, Any], None]):
        """ modify the z axis

        Args:
            axis_placement: axis_placement(s)
            sep_count:      sub value separator count
            name:           name of the modified property
            value:          new value
            axis_fct:       axis function
            axis_coord_fct: axis coordinate function
        """

        #------------- vector value

        if sep_count == 1:
            if isinstance(axis_placement, list):
                for item in axis_placement:
                    axis_fct(item, value)
            else:
                axis_fct(axis_placement, value)


        #------------- coordinate part value

        elif isinstance(axis_placement, list):
            for item in axis_placement:
                axis_coord_fct(item, name, value)

        else:
            axis_coord_fct(axis_placement, name, value)


    @staticmethod
    def __set_x_axis(axis_placement  : AllplanGeo.AxisPlacement3D,
                     value: AllplanGeo.Vector3D):
        """ set the x axis

        Args:
            axis_placement:   axis_placement
            value: x axis
        """

        axis_placement.SetXDirection(value)


    @staticmethod
    def __set_x_axis_coord(axis_placement  : AllplanGeo.AxisPlacement3D,
                           name : str,
                           value: AllplanGeo.Vector3D):
        """ set the x axis

        Args:
            axis_placement:   axis_placement
            name:  name of the modified property
            value: x axis
        """

        axis_placement.XDirection = CoordinateValueUtil.set_coordinate_value(axis_placement.XDirection, name, value)


    @staticmethod
    def __set_z_axis(axis_placement  : AllplanGeo.AxisPlacement3D,
                     value: AllplanGeo.Vector3D):
        """ set the z axis

        Args:
            axis_placement:   axis_placement
            value: z axis
        """

        axis_placement.SetZDirection(value)


    @staticmethod
    def __set_z_axis_coord(axis_placement  : AllplanGeo.AxisPlacement3D,
                           name : str,
                           value: AllplanGeo.Vector3D):
        """ set the z axis

        Args:
            axis_placement:   axis_placement
            name:  name of the modified property
            value: z axis
        """

        axis_placement.ZDirection = CoordinateValueUtil.set_coordinate_value(axis_placement.ZDirection, name, value)


    @staticmethod
    def __get_value_axisplacement3d(value_str: str) -> AllplanGeo.AxisPlacement3D:
        """ get a 3D axis placement from a value string

        Args:
            value_str: Value string

        Returns:
            3D axis placement
        """

        if not value_str:
            return AllplanGeo.AxisPlacement3D()

        value_str = value_str.replace("AxisPlacement3D", "").replace(" ", "")

        return AllplanGeo.AxisPlacement3D(CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "Origin",
                                                                                                                    "(0,0,0)"),
                                                                              AllplanGeo.Point3D()),
                                          CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "XDirection",
                                                                                                                    "(1,0,0)"),
                                                                              AllplanGeo.Vector3D()),
                                          CoordinateValueUtil.get_xyz_element(StringToValueUtil.get_property_string(value_str, "ZDirection",
                                                                                                                    "(0,0,1)"),
                                                                              AllplanGeo.Vector3D()))

```

</details>