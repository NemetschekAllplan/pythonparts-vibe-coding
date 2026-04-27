---
title: "ArcImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\ArcImpl.py"
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


# ArcImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\ArcImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Base class for the arc value types

## Abhängigkeiten

- `ArcVisitors`
- `BuildingElement`
- `ControlProperties`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `StringEvaluate`
- `Utilities.ConditionUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.PropertyPaletteGeometryControlService`
- `__future__`
- `typing`

## Klassen

### `ArcImpl`

implementation of the Base class for the arc value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanGeo.Arc2D | AllplanGeo.Arc3D` | `str` | convert the arc to a string  Args:     value: arc value  Returns:     arc as string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `update_by_constraint` | `build_ele: BuildingElement, _prop: ParameterProperty, ctrl_props: ControlProperties, _name: str` | `None` | update by a constraint  Args:     build_ele:  building element with the parameter properties     _prop:      parameter property to update     ctrl_props: control properties     _name:      name of the modified value |
| `is_default_init_by_constraint` | `_build_ele: BuildingElement, _ctrl_props: ControlProperties` | `bool` | check, whether the default value must be initialized by the constraint  Args:     _build_ele:  building element with the parameter properties     _ctrl_props: control properties  Returns:     default init by the constraint state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Base class for the arc value types
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil

from .ArcVisitors import ArcVisitors
from .CoordinateValueUtil import CoordinateValueUtil
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextUtil
from ..ValueTypeUtils.PropertyPaletteGeometryControlService import PropertyPaletteGeometryControlService

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ArcImpl(ParameterPropertyValueType):
    """ implementation of the Base class for the arc value types
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

        arc = ParameterPropertyListUtil.get_item_value(prop, name)

        if (visitor := getattr(ArcVisitors, visit_key, None)) is not None:
            visitor(arc, sep_count, name, value)

        return False


    @staticmethod
    def to_string(value: (AllplanGeo.Arc2D | AllplanGeo.Arc3D)) -> str:
        """ convert the arc to a string

        Args:
            value: arc value

        Returns:
            arc as string
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

        is_3d_arc = isinstance(prop.value, AllplanGeo.Arc3D)

        text_util = PropertyPaletteControlTextUtil(prop_pal_ctrl_service.global_str_table)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.CenterPoint",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.Center, "CenterPoint",
                                                                     text_util.get_row_name_text(ctrl_props, "CenterPoint",
                                                                                                 "e_CENTER_POINT"),
                                                                     is_3d_arc, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.MinorRadius",  prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.MinorRadius",  ctrl_props,  prop.value.MinorRadius,
                                                          ctrl_props.min_value, ctrl_props.max_value,
                                                          text_util.get_row_name_text(ctrl_props, "MinorRadius", "e_MINOR"))

        if ParameterPropertyValueType.is_visible(f"{prop.name}.MajorRadius",  prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.MajorRadius",  ctrl_props,  prop.value.MajorRadius,
                                                          ctrl_props.min_value, ctrl_props.max_value,
                                                          text_util.get_row_name_text(ctrl_props, "MajorRadius", "e_MAJOR"))

        if not is_3d_arc and ParameterPropertyValueType.is_visible(f"{prop.name}.AxisAngle",  prop_visible_dict):
            prop_pal_ctrl_service.add_angle_edit_control(wpf_palette, f"{prop.name}.AxisAngle",  ctrl_props,  prop.value.AxisAngle.Deg,
                                                         text_util.get_row_name_text(ctrl_props, "AxisAngle", "e_ANGLE"))

        if ParameterPropertyValueType.is_visible(f"{prop.name}.StartAngle",  prop_visible_dict):
            prop_pal_ctrl_service.add_angle_edit_control(wpf_palette, f"{prop.name}.StartAngle",  ctrl_props,  prop.value.StartAngle.Deg,
                                                         text_util.get_row_name_text(ctrl_props, "StartAngle", "e_START_ANGLE"))

        if ParameterPropertyValueType.is_visible(f"{prop.name}.EndAngle",  prop_visible_dict):
            prop_pal_ctrl_service.add_angle_edit_control(wpf_palette, f"{prop.name}.EndAngle",  ctrl_props,  prop.value.EndAngle.Deg,
                                                         text_util.get_row_name_text(ctrl_props, "EndAngle", "e_END_ANGLE"))

        if is_3d_arc and ParameterPropertyValueType.is_visible(f"{prop.name}.XDirection",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_direction_vector_to_palette(
                                                                     wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.GetXAxis(), "XDirection",
                                                                     text_util.get_row_name_text(ctrl_props, "XDirection", "e_X_AXIS"),
                                                                     is_3d_arc, prop_pal_ctrl_service)

        if is_3d_arc and ParameterPropertyValueType.is_visible(f"{prop.name}.ZAxis",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_direction_vector_to_palette(
                                                                     wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.GetZAxis(), "ZAxis",
                                                                     text_util.get_row_name_text(ctrl_props, "ZAxis", "e_Z_AXIS"),
                                                                     is_3d_arc, prop_pal_ctrl_service)


    @staticmethod
    def update_by_constraint(build_ele : BuildingElement,
                             _prop     : ParameterProperty,
                             ctrl_props: ControlProperties,
                             _name     : str):
        """ update by a constraint

        Args:
            build_ele:  building element with the parameter properties
            _prop:      parameter property to update
            ctrl_props: control properties
            _name:      name of the modified value
        """

        StringEvaluate.exec_function_string(ctrl_props.constraint[0],
                                            StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0]))


    @staticmethod
    def is_default_init_by_constraint(_build_ele : BuildingElement,
                                      _ctrl_props: ControlProperties) -> bool:
        """ check, whether the default value must be initialized by the constraint

        Args:
            _build_ele:  building element with the parameter properties
            _ctrl_props: control properties

        Returns:
            default init by the constraint state
        """

        return True

```

</details>