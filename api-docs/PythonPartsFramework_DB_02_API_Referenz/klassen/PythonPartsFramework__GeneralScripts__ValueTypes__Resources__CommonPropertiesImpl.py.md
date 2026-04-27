---
title: "CommonPropertiesImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\CommonPropertiesImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# CommonPropertiesImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\CommonPropertiesImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the CommonProperties value type

## Abhängigkeiten

- `BuildingElement`
- `CommonPropertiesUtil`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `StringEvaluate`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `typing`

## Klassen

### `CommonPropertiesImpl`

implementation of the CommonProperties value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanBaseEle.CommonProperties` | `str` | convert the common properties to a string  Args:     value: common properties  Returns:     common properties as string |
| `get_value` | `value_str: str` | `AllplanBaseEle.CommonProperties` | get the common properties from a string  Args:     value_str: common properties string  Returns:     common properties from the string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `update_by_constraint` | `build_ele: BuildingElement, _prop: ParameterProperty, ctrl_props: ControlProperties, _name: str` | `None` | update by a constraint  Args:     build_ele:  building element with the parameter properties     _prop:      parameter property to update     ctrl_props: control properties     _name:      name of the modified value |
| `is_default_init_by_constraint` | `_build_ele: BuildingElement, _ctrl_props: ControlProperties` | `bool` | check, whether the default value must be initialized by the constraint  Args:     _build_ele:  building element with the parameter properties     _ctrl_props: control properties  Returns:     default init by the constraint state |
| `__add_sub_control` | `wpf_palette_function: Any, name: str, value: int, ctrl_props: ControlProperties, sub_name: str, row_name: str, enabled: bool, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a sub control to palette  Args:     wpf_palette_function:  palette function for the control creation     name:                  name of the property     value:                 value of the sub property     ctrl_props:            control properties     sub_name:              name of the sub control     row_name:              name of the row     enabled:               enabled state     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the CommonProperties value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING, cast

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle

from ControlProperties import ControlProperties
from CommonPropertiesUtil import CommonPropertiesUtil
from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class CommonPropertiesImpl(ParameterPropertyValueType):
    """ implementation of the CommonProperties value type
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

        prop.is_modified = True

        if GeneralConstants.SUB_NAME_SEPARATOR not in name:
            return ParameterPropertyListUtil.set_item_value(prop, name, value)

        com_prop = cast(AllplanBaseEle.CommonProperties, ParameterPropertyListUtil.get_item_value(prop, name))

        sub_name = name.split(".")[1]

        color_by_layer  = com_prop.ColorByLayer
        pen_by_layer    = com_prop.PenByLayer
        stroke_by_layer = com_prop.StrokeByLayer
        help_constr     = com_prop.HelpConstruction
        layer           = com_prop.Layer

        setattr(com_prop, sub_name, value)

        com_prop_by_layer  = AllplanBaseEle.CommonProperties(com_prop)

        if not (update_palette := CommonPropertiesUtil.update_by_layer(com_prop_by_layer)):
            update_palette = color_by_layer  != com_prop_by_layer.ColorByLayer  or \
                             pen_by_layer    != com_prop_by_layer.PenByLayer    or \
                             stroke_by_layer != com_prop_by_layer.StrokeByLayer or \
                             layer           != com_prop_by_layer.Layer and layer == 0 or com_prop_by_layer.Layer == 0


        #----------------- check for constraint property update

        if help_constr != com_prop.HelpConstruction:
            return True

        return update_palette


    @staticmethod
    def to_string(value: AllplanBaseEle.CommonProperties) -> str:
        """ convert the common properties to a string

        Args:
            value: common properties

        Returns:
            common properties as string
        """

        return ValueToStringUtil.trim_value_string(str(value))


    @staticmethod
    def get_value(value_str: str) -> AllplanBaseEle.CommonProperties:
        """ get the common properties from a string

        Args:
            value_str: common properties string

        Returns:
            common properties from the string
        """

        def get_common_properties(value_str: str) -> AllplanBaseEle.CommonProperties:
            """ get the common properties from the value string

            Args:
                value_str: value string

            Returns:
                common properties
            """

            com_prop = AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties()

            if not value_str:
                return com_prop

            com_prop.Pen    = StringToValueUtil.get_property_int(value_str, "Pen", 1)
            com_prop.Stroke = StringToValueUtil.get_property_int(value_str, "Stroke", 1)
            com_prop.Color  = StringToValueUtil.get_property_int(value_str, "Color", 1)
            com_prop.Layer  = StringToValueUtil.get_property_int(value_str, "Layer", 0)

            com_prop.PenByLayer       = StringToValueUtil.get_property_bool(value_str, "PenByLayer", False)
            com_prop.StrokeByLayer    = StringToValueUtil.get_property_bool(value_str, "StrokeByLayer", False)
            com_prop.ColorByLayer     = StringToValueUtil.get_property_bool(value_str, "ColorByLayer", False)
            com_prop.HelpConstruction = StringToValueUtil.get_property_bool(value_str, "HelpConstruction", False)
            com_prop.DrawOrder        = StringToValueUtil.get_property_int(value_str, "DrawOrder", 0)

            return com_prop

        return BaseStringToValueConverter.to_value_by_type_converter(get_common_properties, value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,            # NOSONAR
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

        text = f"{ctrl_props.text} " if ctrl_props.text else ""

        index_name = f" {ctrl_props.row_name}" if ctrl_props.row_name and not text else ""


        #----------------- get strings

        pen_str         , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_PEN")
        stroke_str      , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_LINETYPE")
        color_str       , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_COLOR")
        layer_str       , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_LAYER")
        help_constr_str , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_HELPCONSTRUCTION")
        draw_order_str  , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_DRAW_ORDER")


        #----------------- get the property text

        prop_text_dict = {"Pen"             : pen_str + index_name,
                          "Stroke"          : stroke_str + index_name,
                          "Color"           : color_str + index_name,
                          "Layer"           : layer_str + index_name,
                          "HelpConstruction": help_constr_str + index_name,
                          "DrawOrder"       : draw_order_str + index_name}

        for item in text.split(GeneralConstants.TEXT_SEPARATOR):
            key, _, sub_text = item.partition(":")

            if key in prop_text_dict:
                prop_text_dict[key] = sub_text.strip() + index_name

                text = text.replace(f"{key}:{sub_text}", ""). \
                            replace(GeneralConstants.TEXT_SEPARATOR * 2, "").strip(GeneralConstants.TEXT_SEPARATOR)

        if not text.strip():
            text = ""


        #----------------- get common properties and properties state

        com_prop = AllplanBaseEle.CommonProperties(cast(AllplanBaseEle.CommonProperties, prop.value))

        enabled = prop_pal_ctrl_service.is_control_enabled(ctrl_props)

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)


        #----------------- update by layer

        CommonPropertiesUtil.update_by_layer(com_prop)


        #----------------- add controls

        layer = com_prop.Layer

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Pen",  prop_visible_dict):
            if ParameterPropertyValueType.is_visible(f"{prop.name}.PenByLayer",  prop_visible_dict):
                prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "PenByLayer",
                                                      text + prop_text_dict["Pen"],
                                                      enabled and not com_prop.HelpConstruction and layer != 0)

            CommonPropertiesImpl.__add_sub_control(wpf_palette.AddPenValue, prop.name, com_prop.Pen, ctrl_props, "Pen",
                                                   text + prop_text_dict["Pen"],
                                                   enabled and not com_prop.PenByLayer and not com_prop.HelpConstruction,
                                                   prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Stroke",  prop_visible_dict):
            if ParameterPropertyValueType.is_visible(f"{prop.name}.StrokeByLayer",  prop_visible_dict):
                prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "StrokeByLayer",
                                                      text + prop_text_dict["Stroke"],
                                                      enabled and not com_prop.HelpConstruction and layer != 0)

            CommonPropertiesImpl.__add_sub_control(wpf_palette.AddStroke, prop.name, com_prop.Stroke, ctrl_props, "Stroke",
                                                   text + prop_text_dict["Stroke"],
                                                   enabled and not com_prop.StrokeByLayer and not com_prop.HelpConstruction,
                                                   prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Color",  prop_visible_dict):
            if ParameterPropertyValueType.is_visible(f"{prop.name}.ColorByLayer",  prop_visible_dict):
                prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "ColorByLayer",
                                                      text + prop_text_dict["Color"],
                                                      enabled and not com_prop.HelpConstruction and layer != 0)

            CommonPropertiesImpl.__add_sub_control(wpf_palette.AddColorValue, prop.name, com_prop.Color, ctrl_props, "Color",
                                                   text + prop_text_dict["Color"],
                                                   enabled and not com_prop.ColorByLayer and not com_prop.HelpConstruction,
                                                   prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Layer",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddLayer, prop, ctrl_props, "Layer",
                                                  text + prop_text_dict["Layer"], True)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.HelpConstruction",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "HelpConstruction",
                                                  text + prop_text_dict["HelpConstruction"], True)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.DrawOrder",  prop_visible_dict):
            draw_order_ctrl_props = ctrl_props.deep_copy()
            draw_order_ctrl_props.as_slider = True

            prop_pal_ctrl_service.add_int_edit_control(wpf_palette, f"{prop.name}.DrawOrder",  draw_order_ctrl_props,
                                                       prop.value.DrawOrder, -15, 15, "", text + prop_text_dict["DrawOrder"])


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


    @staticmethod
    def __add_sub_control(wpf_palette_function : Any,
                          name                 : str,
                          value                : int,
                          ctrl_props           : ControlProperties,
                          sub_name             : str,
                          row_name             : str,
                          enabled              : bool,
                          prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add a sub control to palette

        Args:
            wpf_palette_function:  palette function for the control creation
            name:                  name of the property
            value:                 value of the sub property
            ctrl_props:            control properties
            sub_name:              name of the sub control
            row_name:              name of the row
            enabled:               enabled state
            prop_pal_ctrl_service: property palette control service
        """

        wpf_palette_function(ctrl_props.text, f"{name}.{sub_name}",
                             value, prop_pal_ctrl_service.page_index,
                             ctrl_props.expander_name + ctrl_props.expander_state_key,
                             row_name, enabled,
                             ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

```

</details>