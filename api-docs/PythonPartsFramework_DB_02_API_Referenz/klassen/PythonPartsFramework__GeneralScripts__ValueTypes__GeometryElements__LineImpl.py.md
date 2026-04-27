---
title: "LineImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\LineImpl.py"
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


# LineImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\LineImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Base class for the line value types

## Abhängigkeiten

- `ControlProperties`
- `CoordinateValueUtil`
- `LineVisitors`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `Utilities.ConditionUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.PropertyPaletteGeometryControlService`
- `__future__`
- `typing`

## Klassen

### `LineImpl`

implementation of the Base class for the line value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanGeo.Line2D | AllplanGeo.Line3D` | `str` | convert the line to a string  Args:     value: line value  Returns:     line as string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Base class for the line value types
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil

from .LineVisitors import LineVisitors
from .CoordinateValueUtil import CoordinateValueUtil

from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextUtil
from ..ValueTypeUtils.PropertyPaletteGeometryControlService import PropertyPaletteGeometryControlService

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class LineImpl(ParameterPropertyValueType):
    """ implementation of the Base class for the line value types
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

        visit_key = f"visit_{name.split('.', 2)[1]}"

        line = ParameterPropertyListUtil.get_item_value(prop, name)

        if (visitor := getattr(LineVisitors, visit_key, None)) is not None:
            visitor(line, sep_count, name, value)

        return False


    @staticmethod
    def to_string(value: (AllplanGeo.Line2D | AllplanGeo.Line3D)) -> str:
        """ convert the line to a string

        Args:
            value: line value

        Returns:
            line as string
        """

        return str(value).replace("\n", "").replace(" ", "")


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

        is_3d_line = isinstance(prop.value, AllplanGeo.Line3D)

        text_util = PropertyPaletteControlTextUtil(prop_pal_ctrl_service.global_str_table)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.StartPoint", prop_visible_dict):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.StartPoint, "StartPoint",
                                                                     text_util.get_row_name_text(ctrl_props, "StartPoint", "e_START_POINT"),
                                                                     is_3d_line, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.EndPoint", prop_visible_dict):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.EndPoint, "EndPoint",
                                                                     text_util.get_row_name_text(ctrl_props, "EndPoint", "e_END_POINT"),
                                                                     is_3d_line, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Length", prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.Length", ctrl_props,
                                                          AllplanGeo.CalcLength(prop.value),
                                                          ctrl_props.min_value, ctrl_props.max_value,
                                                          text_util.get_row_name_text(ctrl_props, "Length", "e_LENGTH"))

        if ParameterPropertyValueType.is_visible(f"{prop.name}.DeltaX", prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.DeltaX", ctrl_props,
                                                          prop.value.EndPoint.X - prop.value.StartPoint.X,
                                                          ctrl_props.min_value, ctrl_props.max_value,
                                                          text_util.get_row_name_text(ctrl_props, "DeltaX", "e_DELTA_X"))

        if ParameterPropertyValueType.is_visible(f"{prop.name}.DeltaY", prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.DeltaY", ctrl_props,
                                                          prop.value.EndPoint.Y - prop.value.StartPoint.Y,
                                                          ctrl_props.min_value, ctrl_props.max_value,
                                                          text_util.get_row_name_text(ctrl_props, "DeltaY", "e_DELTA_Y"))

        if is_3d_line and ParameterPropertyValueType.is_visible(f"{prop.name}.DeltaZ", prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.DeltaZ", ctrl_props,
                                                          prop.value.EndPoint.Z - prop.value.StartPoint.Z,
                                                          ctrl_props.min_value, ctrl_props.max_value,
                                                          text_util.get_row_name_text(ctrl_props, "DeltaZ", "e_DELTA_Z"))

        if not is_3d_line and ParameterPropertyValueType.is_visible(f"{prop.name}.Angle", prop_visible_dict):
            prop_pal_ctrl_service.add_angle_edit_control(wpf_palette, f"{prop.name}.Angle", ctrl_props,
                                                         AllplanGeo.CalcAngle(prop.value)[0].GetDeg(),
                                                         text_util.get_row_name_text(ctrl_props, "Angle", "e_ANGLE"))

```

</details>