---
title: "SurfaceElementPropertiesImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\SurfaceElementPropertiesImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# SurfaceElementPropertiesImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\SurfaceElementPropertiesImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the SurfaceElementProperties value type

## Abhängigkeiten

- `ControlProperties`
- `NemAll_Python_ArchElements`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
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

### `SurfaceElementPropertiesImpl`

implementation of the SurfaceElementProperties value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanArchElements.SurfaceElementProperties` | `str` | convert the surface element properties to a string  Args:     value: SurfaceElementProperties  Returns:     surface element properties as string |
| `get_value` | `value_str: str` | `AllplanArchElements.SurfaceElementProperties` | get the surface element properties from a string  Args:     value_str: surface element properties string  Returns:     surface element properties from the string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the SurfaceElementProperties value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING, cast

import NemAll_Python_ArchElements as AllplanArchElements

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class SurfaceElementPropertiesImpl(ParameterPropertyValueType):
    """ implementation of the SurfaceElementProperties value type
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

        surface_elem_prop = cast(AllplanArchElements.SurfaceElementProperties, ParameterPropertyListUtil.get_item_value(prop, name))

        sub_name = name.split(".")[1]

        old_use_in_groundplan  = surface_elem_prop.UseAreaInGroundplan
        old_hatch_selected     = surface_elem_prop.HatchSelected
        old_pattern_selected   = surface_elem_prop.PatternSelected
        old_filling_selected   = surface_elem_prop.FillingSelected
        old_facestyle_selected = surface_elem_prop.FaceStyleSelected
        old_bitmap_selected    = surface_elem_prop.BitmapSelected

        setattr(surface_elem_prop, sub_name, value)

        update_palette = (
            old_use_in_groundplan  != surface_elem_prop.UseAreaInGroundplan or
            old_hatch_selected     != surface_elem_prop.HatchSelected  or
            old_pattern_selected   != surface_elem_prop.PatternSelected or
            old_filling_selected   != surface_elem_prop.FillingSelected or
            old_facestyle_selected != surface_elem_prop.FaceStyleSelected or
            old_bitmap_selected    != surface_elem_prop.BitmapSelected
        )

        return update_palette


    @staticmethod
    def to_string(value: AllplanArchElements.SurfaceElementProperties) -> str:
        """ convert the surface element properties to a string

        Args:
            value: SurfaceElementProperties

        Returns:
            surface element properties as string
        """

        return ValueToStringUtil.trim_value_string(str(value))


    @staticmethod
    def get_value(value_str: str) -> AllplanArchElements.SurfaceElementProperties:
        """ get the surface element properties from a string

        Args:
            value_str: surface element properties string

        Returns:
            surface element properties from the string
        """

        def get_surface_element_properties(value_str: str) -> AllplanArchElements.SurfaceElementProperties:
            """ get the surface element properties from the value string

            Args:
                value_str: value string

            Returns:
                surface element properties
            """

            surface_elem_prop = AllplanArchElements.SurfaceElementProperties()

            if not value_str:
                return surface_elem_prop

            surface_elem_prop.UseAreaInGroundplan = StringToValueUtil.get_property_bool(value_str, "UseAreaInGroundplan", False)

            surface_elem_prop.HatchSelected     = StringToValueUtil.get_property_bool(value_str, "HatchSelected", False)
            surface_elem_prop.PatternSelected   = StringToValueUtil.get_property_bool(value_str, "PatternSelected", False)
            surface_elem_prop.FillingSelected   = StringToValueUtil.get_property_bool(value_str, "FillingSelected", False)
            surface_elem_prop.BitmapSelected    = StringToValueUtil.get_property_bool(value_str, "BitmapSelected", False)
            surface_elem_prop.FaceStyleSelected = StringToValueUtil.get_property_bool(value_str, "FaceStyleSelected", False)

            surface_elem_prop.HatchID     = StringToValueUtil.get_property_int(value_str, "HatchID", 303)
            surface_elem_prop.PatternID   = StringToValueUtil.get_property_int(value_str, "PatternID", 301)
            surface_elem_prop.FillingID   = StringToValueUtil.get_property_int(value_str, "FillingID", 24)
            surface_elem_prop.FaceStyleID = StringToValueUtil.get_property_int(value_str, "FaceStyleID", 301)
            surface_elem_prop.BitmapID    = StringToValueUtil.get_property_string(value_str, "BitmapID", '')

            return surface_elem_prop

        return BaseStringToValueConverter.to_value_by_type_converter(get_surface_element_properties, value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder, # pylint: disable=too-complex
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

        control_enabled = prop_pal_ctrl_service.is_control_enabled(ctrl_props)

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        use_groundplan_str , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_DISPLAY_PLAN_VIEW")
        hatch_str          , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_HATCH")
        pattern_str        , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_PATTERN")
        filling_str        , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_FILLING")
        bitmap_str         , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_BITMAP_AREA")
        style_area_str     , _ = prop_pal_ctrl_service.global_str_table.get_entry("e_STYLE_AREA")

        if ParameterPropertyValueType.is_visible(f"{prop.name}.UseAreaInGroundplan",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "UseAreaInGroundplan",
                                                  text + use_groundplan_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.HatchSelected",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "HatchSelected",
                                                  text + hatch_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.HatchID",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddHatchValue, prop, ctrl_props, "HatchID",
                                                  text + hatch_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.PatternSelected",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "PatternSelected",
                                                  text + pattern_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.PatternID",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddPatternValue, prop, ctrl_props, "PatternID",
                                                  text + pattern_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.FillingSelected",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "FillingSelected",
                                                  text + filling_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.FillingID",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddColorValue, prop, ctrl_props, "FillingID",
                                                  text + filling_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.FaceStyleSelected",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "FaceStyleSelected",
                                                  text + style_area_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.FaceStyleID",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddFaceStyleValue, prop, ctrl_props, "FaceStyleID",
                                                  text + style_area_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.BitmapSelected",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "BitmapSelected",
                                                  text + bitmap_str + index_name, control_enabled)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.BitmapID",  prop_visible_dict):
            wpf_palette.AddButton(prop.value.BitmapID, prop.name + GeneralConstants.BITMAP_RESOURCE_DIALOG_BUTTON_KEY,
                              0, prop_pal_ctrl_service.page_index,
                              ctrl_props.expander_name, text + bitmap_str + index_name,
                              control_enabled,
                              ctrl_props.height, ctrl_props.width,
                              ctrl_props.font_style, ctrl_props.font_face_code)

```

</details>