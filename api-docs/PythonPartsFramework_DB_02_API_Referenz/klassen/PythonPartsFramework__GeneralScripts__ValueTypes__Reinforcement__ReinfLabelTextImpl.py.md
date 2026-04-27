---
title: "ReinfLabelTextImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfLabelTextImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ReinfLabelTextImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfLabelTextImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `werte`

## Übersicht

implementation of ReinfLabelText value type

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `Resources.FontImpl`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `math`
- `typing`

## Klassen

### `ReinfLabelTextImpl`

implementation of the ReinfLabelText value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanReinf.ReinforcementLabelTextProperties` | `str` | convert the common properties to a string  Args:     value: common properties  Returns:     common properties as string |
| `get_value` | `value_str: str` | `AllplanReinf.ReinforcementLabelTextProperties` | get the common properties from a string  Args:     value_str: common properties string  Returns:     common properties from the string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of ReinfLabelText value type
"""

from __future__ import annotations

import math

from typing import Any, TYPE_CHECKING, cast

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..Resources.FontImpl import FontImpl
from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextData
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService


class ReinfLabelTextImpl(ParameterPropertyValueType):
    """ implementation of the ReinfLabelText value type
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

        text_prop = cast(AllplanReinf.ReinforcementLabelTextProperties, ParameterPropertyListUtil.get_item_value(prop, name))

        sub_name = name.split(".")[1]

        match sub_name:
            case "HasTransparentBackground":
                text_prop.HasTransparentBackground = not value

            case "Height":
                aspect = text_prop.Height / text_prop.Width if text_prop.Width != 0 else 1.0

                text_prop.Width  = value / aspect
                text_prop.Height = value

                return True

            case "Aspect":
                text_prop.Height = value * text_prop.Width

                return True

            case "FontAngle":
                text_prop.FontAngle = AllplanGeo.Angle.FromDeg(value)

                return True

            case _:
                setattr(text_prop, sub_name, value)

        return False


    @staticmethod
    def to_string(value: AllplanReinf.ReinforcementLabelTextProperties) -> str:
        """ convert the common properties to a string

        Args:
            value: common properties

        Returns:
            common properties as string
        """

        return ValueToStringUtil.trim_value_string(str(value))


    @staticmethod
    def get_value(value_str: str) -> AllplanReinf.ReinforcementLabelTextProperties:
        """ get the common properties from a string

        Args:
            value_str: common properties string

        Returns:
            common properties from the string
        """

        def get_text_properties(value_str: str) -> AllplanReinf.ReinforcementLabelTextProperties:
            """ get the pointer properties from the value string

            Args:
                value_str: value string

            Returns:
                common properties
            """

            text_prop = AllplanReinf.ReinforcementLabelTextProperties()

            if not value_str:
                return text_prop

            text_prop.MarkNumberPen                    = StringToValueUtil.get_property_int(value_str, "MarkNumberPen", 1)
            text_prop.MarkNumberColor                  = StringToValueUtil.get_property_int(value_str, "MarkNumberColor", 1)
            text_prop.MarkNumberBorderPen              = StringToValueUtil.get_property_int(value_str, "MarkNumberBorderPen", 1)
            text_prop.MarkNumberBorderColorFromElement = StringToValueUtil.get_property_bool(value_str, "MarkNumberBorderColorFromElement",
                                                                                             False)
            text_prop.MarkNumberBorderColor            = StringToValueUtil.get_property_int(value_str, "MarkNumberBorderColor", 1)
            text_prop.Font                             = StringToValueUtil.get_property_int(value_str, "Font", 1)
            text_prop.Height                           = StringToValueUtil.get_property_float(value_str, "Height", 2.5)
            text_prop.Width                            = StringToValueUtil.get_property_float(value_str, "Width", 2.5)
            text_prop.FontAngle                        = StringToValueUtil.get_property_geo_angle(value_str, "FontAngle", math.pi / 2.0)
            text_prop.TextPen                          = StringToValueUtil.get_property_int(value_str, "TextPen", 1)
            text_prop.TextColor                        = StringToValueUtil.get_property_int(value_str, "TextColor", 1)
            text_prop.HasTransparentBackground         = not StringToValueUtil.get_property_int(value_str, "TextColor", 1)

            return text_prop

        return BaseStringToValueConverter.to_value_by_type_converter(get_text_properties, value_str)


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

        enabled = prop_pal_ctrl_service.is_control_enabled(ctrl_props)

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)


        #----------------- add controls

        get_global_str_table_entry = prop_pal_ctrl_service.get_global_str_table_entry

        expander_name = ctrl_props.expander_name

        separator = GeneralConstants.TEXT_SEPARATOR if expander_name else ""


        #----------------- mark number properties

        ctrl_props.expander_name = expander_name + separator + get_global_str_table_entry("e_MARK_NUMBER")

        prop_pal_ctrl_service.add_sub_control(wpf_palette.AddPenValue, prop, ctrl_props, "MarkNumberPen",
                                                text + get_global_str_table_entry("e_PEN") + index_name, enabled, prop_visible_dict)

        prop_pal_ctrl_service.add_sub_control(wpf_palette.AddColorValue, prop, ctrl_props, "MarkNumberColor",
                                                text + get_global_str_table_entry("e_COLOR") + index_name, enabled, prop_visible_dict)

        prop_pal_ctrl_service.add_sub_control(wpf_palette.AddPenValue, prop, ctrl_props, "MarkNumberBorderPen",
                                                text + get_global_str_table_entry("e_FRAME_PEN") + index_name, enabled, prop_visible_dict)

        prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "MarkNumberBorderColorFromElement",
                                                text + get_global_str_table_entry("e_FRAME_COLOR_FROM_ELEMENT") + index_name, enabled,
                                                prop_visible_dict)

        if not prop.value.MarkNumberBorderColorFromElement:
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddColorValue, prop, ctrl_props, "MarkNumberBorderColor",
                                                 text + get_global_str_table_entry("e_FRAME_COLOR") + index_name, enabled,
                                                 prop_visible_dict)


        #----------------- text properties

        ctrl_props.expander_name = expander_name + separator + get_global_str_table_entry("e_MARK_TEXT")

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Font",  prop_visible_dict):
            font_prop       = prop.deep_copy()
            font_prop.name  = f"{prop.name}.Font"
            font_prop.value = prop.value.Font

            font_ctrl_props            = ctrl_props.deep_copy()
            font_ctrl_props.value_name = font_prop.name
            font_ctrl_props.row_name   = text + get_global_str_table_entry("e_FONT") + index_name

            FontImpl.add_to_palette(wpf_palette, font_prop, font_ctrl_props, prop_pal_ctrl_service)

        prop_pal_ctrl_service.add_num_edit_sub_control(wpf_palette.AddDoubleValue, prop, ctrl_props, "Height",
                                                        text + get_global_str_table_entry("e_TEXT_HEIGHT") + index_name, enabled,
                                                        prop_visible_dict)

        prop_pal_ctrl_service.add_num_edit_sub_control(wpf_palette.AddDoubleValue, prop, ctrl_props, "Width",
                                                        text + get_global_str_table_entry("e_TEXT_WIDTH") + index_name, enabled,
                                                        prop_visible_dict)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Aspect",  prop_visible_dict):
            aspect_ctrl_props = ctrl_props.deep_copy()

            value = prop.value.Height / prop.value.Width if prop.value.Width != 0 else 1.0

            prop_pal_ctrl_service.add_double_edit_control(wpf_palette, f"{prop.name}.Aspect", aspect_ctrl_props, value,
                                                          0.001, 100.0,
                                                          PropertyPaletteControlTextData(text + get_global_str_table_entry("e_ASPECT") + \
                                                                                         index_name, ""))

        prop_pal_ctrl_service.add_num_edit_sub_control(wpf_palette.AddAngleValue, prop, ctrl_props, "FontAngle",
                                                        text + get_global_str_table_entry("e_FONT_ANGLE") + index_name, enabled,
                                                        prop_visible_dict)

        prop_pal_ctrl_service.add_sub_control(wpf_palette.AddPenValue, prop, ctrl_props, "TextPen",
                                                text + get_global_str_table_entry("e_PEN") + index_name, enabled, prop_visible_dict)

        prop_pal_ctrl_service.add_sub_control(wpf_palette.AddColorValue, prop, ctrl_props, "TextColor",
                                                text + get_global_str_table_entry("e_COLOR") + index_name, enabled, prop_visible_dict)

        prop.value.HasTransparentBackground = not prop.value.HasTransparentBackground

        prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "HasTransparentBackground",
                                                text + get_global_str_table_entry("e_APPLY_BACKGROUND_FILL") + index_name, enabled,
                                                prop_visible_dict)

        prop.value.HasTransparentBackground = not prop.value.HasTransparentBackground

        ctrl_props.expander_name = expander_name

```

</details>