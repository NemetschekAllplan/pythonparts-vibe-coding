---
title: "PropertyPaletteControlService"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\PropertyPaletteControlService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PropertyPaletteControlService

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\PropertyPaletteControlService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the property palette control service

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_Palette`
- `Palette.PaletteData`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `PropertyPaletteControlTextUtil`
- `StringEvaluate`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `ValueListValidator`
- `__future__`
- `typing`

## Klassen

### `PropertyPaletteControlService`

implementation of the property palette control service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, palette_data: PaletteData` | `None` | initialize  Args:     palette_data: palette data |
| `is_control_enabled` | `self, ctrl_props: ControlProperties` | `bool` | Get the enable condition  Args:     ctrl_props: control properties  Returns:     control enabled state |
| `is_sub_control_enabled` | `self, ctrl_props: ControlProperties, sub_name: str` | `bool` | Get the enable condition  Args:     ctrl_props: control properties     sub_name:   name of the sub control  Returns:     control enabled state |
| `add_edit_control` | `self, wpf_palette_function: Any, prop: ParameterProperty, ctrl_props: ControlProperties, value: Any` | `None` | Add an float/integer edit control to palette  Args:     wpf_palette_function: WPF palette function for the control creation     prop:                 parameter property     ctrl_props:           control properties     value:                new value |
| `add_string_edit_control` | `self, wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, value: Any` | `None` | Add a string edit controls to palette  Args:     wpf_palette: WPF palette     prop:        parameter property     ctrl_props:  control properties     value:       new value |
| `add_length_edit_control` | `self, wpf_palette: WpfPaletteBuilder, prop_name: str, ctrl_props: ControlProperties, value: Any, min_value: Any, max_value: Any, text_data: PropertyPaletteControlTextData` | `None` | Add a length edit field to palette  Args:     wpf_palette: WPF palette     prop_name:   name of the property     ctrl_props:  control properties     value:       new value     min_value:   min value     max_value:   max value     text_data:   text data |
| `add_double_edit_control` | `self, wpf_palette: WpfPaletteBuilder, prop_name: str, ctrl_props: ControlProperties, value: Any, min_value: Any, max_value: Any, text_data: PropertyPaletteControlTextData` | `None` | Add a length edit field to palette  Args:     wpf_palette: WPF palette     prop_name:   name of the property     ctrl_props:  control properties     value:       new value     min_value:   min value     max_value:   max value     text_data:   text data |
| `add_int_edit_control` | `self, wpf_palette: WpfPaletteBuilder, prop_name: str, ctrl_props: ControlProperties, value: Any, min_value: int, max_value: int, row_name: str, text: str` | `None` | Add an integer edit field to palette  Args:     wpf_palette: WPF palette     prop_name:   name of the property     ctrl_props:  control properties     value:       new value     min_value:   min value     max_value:   max value     row_name:    name of the row     text:        text |
| `add_radio_button_control` | `self, wpf_palette: WpfPaletteBuilder, group_name: str, ctrl_props: ControlProperties, value: Any, selected_value: Any` | `None` | Add a radio button controls to palette  Args:     wpf_palette:    WPF palette     group_name:     group name     ctrl_props:     control properties     value:          new value     selected_value: description |
| `add_angle_edit_control` | `self, wpf_palette: WpfPaletteBuilder, prop_name: str, ctrl_props: ControlProperties, value: Any, text_data: PropertyPaletteControlTextData` | `None` | Add a length edit field to palette  Args:     wpf_palette: WPF palette     prop_name:   name of the property     ctrl_props:  control properties     value:       new value     text_data:   text data |
| `add_combo_box` | `self, wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, palette_value_type: AllplanPalette.PaletteValueType` | `None` | Add a combo box edit field to palette  Args:     wpf_palette:        WPF palette     prop:               parameter property     ctrl_props:         control properties     palette_value_type: value type of the control inside the palette |
| `add_string` | `self, wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties` | `None` | Add a string edit control to palette  Args:     wpf_palette: WPF palette     prop:        parameter property     ctrl_props:  control properties |
| `add_text` | `self, wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties` | `None` | Add a text to palette  Args:     wpf_palette: WPF palette     prop:        parameter property     ctrl_props:  control properties |
| `add_control` | `self, wpf_palette_function: Any, prop: ParameterProperty, ctrl_props: ControlProperties, value: Any` | `None` | Add a control to palette  Args:     wpf_palette_function: palette function for the control creation     prop:                 parameter property     ctrl_props:           control properties     value:                new value |
| `__add_edit_control` | `self, wpf_palette_function: Any, prop_name: str, ctrl_props: ControlProperties, value: Any, min_value: Any, max_value: Any, row_name: str, text: str` | `None` | Add a edit field to palette  Args:     wpf_palette_function: palette function for the control creation     prop_name:            name of the property     ctrl_props:           control properties     value:                new value     min_value:            min value     max_value:            max value     row_name:             name of the row     text:                 text |
| `add_sub_control` | `self, wpf_palette_function: Any, prop: ParameterProperty, ctrl_props: ControlProperties, sub_name: str, row_name: str, enabled: bool, prop_visible_dict: dict[str, bool] | None=None` | `None` | Add a sub control to palette  Args:     wpf_palette_function: palette function for the control creation     prop:                 parameter property     ctrl_props:           control properties     sub_name:             name of the sub control     row_name:             name of the row     enabled:              enabled state     prop_visible_dict:    visible dictionary for the property |
| `add_num_edit_sub_control` | `self, wpf_palette_function: Any, prop: ParameterProperty, ctrl_props: ControlProperties, sub_name: str, row_name: str, enabled: bool, prop_visible_dict: dict[str, bool] | None=None` | `None` | Add an sub control with numerical edit to palette  Args:     wpf_palette_function: palette function for the control creation     prop:                 parameter property     ctrl_props:           control properties     sub_name:             name of the sub control     row_name:             name of the row     enabled:              enabled state     prop_visible_dict:    visible dictionary for the property |
| `get_global_str_table_entry` | `self, text_id: str` | `str` | get an entry from the global string table  Args:     text_id: id of the text  Returns:     text entry from the global string table |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the property palette control service
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import NemAll_Python_Palette as AllplanPalette

from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from Palette.PaletteData import PaletteData
from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..ParameterPropertyValueType import ParameterPropertyValueType

from .PropertyPaletteControlTextUtil import PropertyPaletteControlTextData
from .ValueListValidator import ValueListValidator

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty

class PropertyPaletteControlService(PaletteData):
    """ implementation of the property palette control service
    """

    def __init__(self,
                 palette_data: PaletteData):
        """ initialize

        Args:
            palette_data: palette data
        """

        super().__init__(palette_data.page_enable_cond,
                         palette_data.param_dict,
                         palette_data.page_index,
                         palette_data.picture_path,
                         palette_data.global_str_table,
                         palette_data.build_ele,
                         palette_data.row,
                         palette_data.is_visual_script,
                         palette_data.expander_name,
                         palette_data.expander_visible,
                         palette_data.row_name,
                         palette_data.row_visible,
                         palette_data.row_full_text)


    def is_control_enabled(self,
                           ctrl_props: ControlProperties) -> bool:
        """ Get the enable condition

        Args:
            ctrl_props: control properties

        Returns:
            control enabled state
        """

        if ctrl_props.enable_function:
            return ctrl_props.enable_function()

        condition = self.page_enable_cond or ctrl_props.enable_condition

        ctrl_props.enable = StringEvaluate.eval_condition(condition, self.param_dict)

        return ctrl_props.enable


    def is_sub_control_enabled(self,
                               ctrl_props: ControlProperties,
                               sub_name  : str) -> bool:
        """ Get the enable condition

        Args:
            ctrl_props: control properties
            sub_name:   name of the sub control

        Returns:
            control enabled state
        """

        if ctrl_props.enable_function:
            return ctrl_props.enable_function()

        condition =  self.page_enable_cond or ctrl_props.enable_condition

        if GeneralConstants.TEXT_SEPARATOR not in condition:
            ctrl_props.enable = StringEvaluate.eval_condition(condition, self.param_dict)

        else:
            enable_dict = ConditionUtil.get_condition_dict(condition, ctrl_props.value_name, self.param_dict)

            ctrl_props.enable = enable_dict.get(f"{ctrl_props.value_name}.{sub_name}",  True)

        return ctrl_props.enable


    def add_edit_control(self,
                         wpf_palette_function: Any,
                         prop                : ParameterProperty,
                         ctrl_props          : ControlProperties,
                         value               : Any):
        """ Add an float/integer edit control to palette

        Args:
            wpf_palette_function: WPF palette function for the control creation
            prop:                 parameter property
            ctrl_props:           control properties
            value:                new value
        """

        self.__add_edit_control(wpf_palette_function,
                                prop.name, ctrl_props, value,
                                ctrl_props.min_value, ctrl_props.max_value,
                                ctrl_props.row_name + ctrl_props.row_state_key, ctrl_props.text)


    def add_string_edit_control(self,
                                wpf_palette: WpfPaletteBuilder,
                                prop       : ParameterProperty,
                                ctrl_props : ControlProperties,
                                value      : Any):
        """ Add a string edit controls to palette

        Args:
            wpf_palette: WPF palette
            prop:        parameter property
            ctrl_props:  control properties
            value:       new value
        """

        background_color = StringEvaluate.eval_color(ctrl_props.background_color, self.param_dict)

        wpf_palette.AddStringValue(ctrl_props.text, prop.name, value, self.page_index,
                                   ctrl_props.expander_name + ctrl_props.expander_state_key,
                                   ctrl_props.row_name + ctrl_props.row_state_key,
                                   self.is_control_enabled(ctrl_props),
                                   ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code,
                                   background_color)


    def add_length_edit_control(self,
                                wpf_palette: WpfPaletteBuilder,
                                prop_name  : str,
                                ctrl_props : ControlProperties,
                                value      : Any,
                                min_value  : Any,
                                max_value  : Any,
                                text_data  : PropertyPaletteControlTextData):
        """ Add a length edit field to palette

        Args:
            wpf_palette: WPF palette
            prop_name:   name of the property
            ctrl_props:  control properties
            value:       new value
            min_value:   min value
            max_value:   max value
            text_data:   text data
        """

        self.__add_edit_control(wpf_palette.AddLengthValue,
                                prop_name, ctrl_props, value, min_value, max_value,
                                text_data.row_name, text_data.text)


    def add_double_edit_control(self,
                                wpf_palette: WpfPaletteBuilder,
                                prop_name  : str,
                                ctrl_props : ControlProperties,
                                value      : Any,
                                min_value  : Any,
                                max_value  : Any,
                                text_data  : PropertyPaletteControlTextData):
        """ Add a length edit field to palette

        Args:
            wpf_palette: WPF palette
            prop_name:   name of the property
            ctrl_props:  control properties
            value:       new value
            min_value:   min value
            max_value:   max value
            text_data:   text data
        """

        self.__add_edit_control(wpf_palette.AddDoubleValue,
                                prop_name, ctrl_props, value, min_value, max_value,
                                text_data.row_name, text_data.text)


    def add_int_edit_control(self,
                             wpf_palette: WpfPaletteBuilder,
                             prop_name  : str,
                             ctrl_props : ControlProperties,
                             value      : Any,
                             min_value  : int,
                             max_value  : int,
                             row_name   : str,
                             text       : str):
        """ Add an integer edit field to palette

        Args:
            wpf_palette: WPF palette
            prop_name:   name of the property
            ctrl_props:  control properties
            value:       new value
            min_value:   min value
            max_value:   max value
            row_name:    name of the row
            text:        text
        """

        self.__add_edit_control(wpf_palette.AddIntValue, prop_name, ctrl_props, value,
                                min_value, max_value, row_name, text)


    def add_radio_button_control(self,
                                 wpf_palette   : WpfPaletteBuilder,
                                 group_name    : str,
                                 ctrl_props    : ControlProperties,
                                 value         : Any,
                                 selected_value: Any):
        """ Add a radio button controls to palette

        Args:
            wpf_palette:    WPF palette
            group_name:     group name
            ctrl_props:     control properties
            value:          new value
            selected_value: description
        """

        value = StringEvaluate.eval_constant(value, self.param_dict)

        wpf_palette.AddRadioButton(ctrl_props.group_text, group_name, ctrl_props.text,
                                   value, selected_value, self.page_index,
                                   ctrl_props.expander_name + ctrl_props.expander_state_key,
                                   ctrl_props.row_name + ctrl_props.row_state_key,
                                   self.is_control_enabled(ctrl_props),
                                   ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)


    def add_angle_edit_control(self,
                               wpf_palette: WpfPaletteBuilder,
                               prop_name  : str,
                               ctrl_props : ControlProperties,
                               value      : Any,
                               text_data  : PropertyPaletteControlTextData):
        """ Add a length edit field to palette

        Args:
            wpf_palette: WPF palette
            prop_name:   name of the property
            ctrl_props:  control properties
            value:       new value
            text_data:   text data
        """

        self.__add_edit_control(wpf_palette.AddAngleValue,
                                prop_name, ctrl_props, value,
                                ctrl_props.min_value, ctrl_props.max_value,
                                text_data.row_name, text_data.text)


    def add_combo_box(self,
                      wpf_palette       : WpfPaletteBuilder,
                      prop              : ParameterProperty,
                      ctrl_props        : ControlProperties,
                      palette_value_type: AllplanPalette.PaletteValueType):
        """ Add a combo box edit field to palette

        Args:
            wpf_palette:        WPF palette
            prop:               parameter property
            ctrl_props:         control properties
            palette_value_type: value type of the control inside the palette
        """

        value_list = ctrl_props.value_list

        if (value_list_util := prop.value_list_util) is not None:
            value_list = value_list_util.get_value_list()

        value, value_list = ValueListValidator.eval_value_list_formula(value_list, str(prop.value), self.param_dict)

        if value != str(prop.value):
            if palette_value_type in [AllplanPalette.PaletteValueType.ANGLE,
                                      AllplanPalette.PaletteValueType.DOUBLE,
                                      AllplanPalette.PaletteValueType.LENGTH]:
                prop.value = float(value)

            elif palette_value_type == AllplanPalette.PaletteValueType.INTEGER:
                prop.value = int(value)

            else:
                prop.value = value

            self.param_dict[prop.name] = prop.value

        background_color = StringEvaluate.eval_color(ctrl_props.background_color, self.param_dict)

        wpf_palette.AddComboBoxValue(ctrl_props.text, prop.name, value, # current value is stored only in building element
                                     value_list, palette_value_type,
                                     self.page_index,
                                     ctrl_props.expander_name + ctrl_props.expander_state_key,
                                     ctrl_props.row_name + ctrl_props.row_state_key,
                                     self.is_control_enabled(ctrl_props),
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code,
                                     background_color,
                                     prop.value_list_util is not None)


    def add_string(self,
                   wpf_palette: WpfPaletteBuilder,
                   prop       : ParameterProperty,
                   ctrl_props : ControlProperties):
        """ Add a string edit control to palette

        Args:
            wpf_palette: WPF palette
            prop:        parameter property
            ctrl_props:  control properties
        """

        background_color = StringEvaluate.eval_color(ctrl_props.background_color, self.param_dict)

        wpf_palette.AddStringValue(ctrl_props.text, prop.name, prop.value, self.page_index,
                                   ctrl_props.expander_name + ctrl_props.expander_state_key,
                                   ctrl_props.row_name + ctrl_props.row_state_key,
                                   self.is_control_enabled(ctrl_props),
                                   ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code,
                                   background_color)


    def add_text(self,
                 wpf_palette: WpfPaletteBuilder,
                 prop       : ParameterProperty,
                 ctrl_props : ControlProperties):
        """ Add a text to palette

        Args:
            wpf_palette: WPF palette
            prop:        parameter property
            ctrl_props:  control properties
        """

        value = StringEvaluate.eval_text(prop.value, self.param_dict)

        orientation = prop.selected_value if isinstance(prop.selected_value, AllplanPalette.Orientation) else \
                      AllplanPalette.Orientation.eLeft

        wpf_palette.AddText(ctrl_props.text, value, orientation, self.page_index,
                            ctrl_props.expander_name + ctrl_props.expander_state_key,
                            ctrl_props.row_name + ctrl_props.row_state_key,
                            self.is_control_enabled(ctrl_props),
                            ctrl_props.height, ctrl_props.width,
                            ctrl_props.font_style, ctrl_props.font_face_code)

    def add_control(self,
                    wpf_palette_function: Any,
                    prop                : ParameterProperty,
                    ctrl_props          : ControlProperties,
                    value               : Any):
        """ Add a control to palette

        Args:
            wpf_palette_function: palette function for the control creation
            prop:                 parameter property
            ctrl_props:           control properties
            value:                new value
        """

        wpf_palette_function(ctrl_props.text, prop.name, value, self.page_index,
                             ctrl_props.expander_name + ctrl_props.expander_state_key,
                             ctrl_props.row_name + ctrl_props.row_state_key,
                             self.is_control_enabled(ctrl_props),
                             ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)


    def __add_edit_control(self,
                           wpf_palette_function: Any,
                           prop_name           : str,
                           ctrl_props          : ControlProperties,
                           value               : Any,
                           min_value           : Any,
                           max_value           : Any,
                           row_name            : str,
                           text                : str):
        """ Add a edit field to palette

        Args:
            wpf_palette_function: palette function for the control creation
            prop_name:            name of the property
            ctrl_props:           control properties
            value:                new value
            min_value:            min value
            max_value:            max value
            row_name:             name of the row
            text:                 text
        """

        interval_value = eval(ctrl_props.interval_value, self.param_dict) if ctrl_props.interval_value else 0       # pylint: disable=eval-used

        background_color = StringEvaluate.eval_color(ctrl_props.background_color, self.param_dict)

        wpf_palette_function(text, prop_name, value, self.page_index,
                             ctrl_props.expander_name + ctrl_props.expander_state_key,
                             row_name,self.is_control_enabled(ctrl_props),
                             min_value, max_value, interval_value, ctrl_props.as_slider,
                             ctrl_props.height, ctrl_props.width,
                             ctrl_props.font_face_code, background_color)


    def add_sub_control(self,
                        wpf_palette_function: Any,
                        prop                : ParameterProperty,
                        ctrl_props          : ControlProperties,
                        sub_name            : str,
                        row_name            : str,
                        enabled             : bool,
                        prop_visible_dict   : dict[str, bool] | None = None):
        """ Add a sub control to palette

        Args:
            wpf_palette_function: palette function for the control creation
            prop:                 parameter property
            ctrl_props:           control properties
            sub_name:             name of the sub control
            row_name:             name of the row
            enabled:              enabled state
            prop_visible_dict:    visible dictionary for the property
        """

        if prop_visible_dict is not None and not ParameterPropertyValueType.is_visible(f"{prop.name}.{sub_name}",  prop_visible_dict):
            return

        wpf_palette_function(ctrl_props.text, f"{prop.name}.{sub_name}",
                             getattr(prop.value, sub_name), self.page_index,
                             ctrl_props.expander_name + ctrl_props.expander_state_key,
                             row_name, enabled,
                             ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)


    def add_num_edit_sub_control(self,
                                 wpf_palette_function: Any,
                                 prop                : ParameterProperty,
                                 ctrl_props          : ControlProperties,
                                 sub_name            : str,
                                 row_name            : str,
                                 enabled             : bool,
                                 prop_visible_dict   : dict[str, bool] | None = None):
        """ Add an sub control with numerical edit to palette

        Args:
            wpf_palette_function: palette function for the control creation
            prop:                 parameter property
            ctrl_props:           control properties
            sub_name:             name of the sub control
            row_name:             name of the row
            enabled:              enabled state
            prop_visible_dict:    visible dictionary for the property
        """

        if prop_visible_dict is not None and not ParameterPropertyValueType.is_visible(f"{prop.name}.{sub_name}",  prop_visible_dict):
            return

        interval_value = eval(ctrl_props.interval_value, self.param_dict) if ctrl_props.interval_value else 0       # pylint: disable=eval-used

        background_color = StringEvaluate.eval_color(ctrl_props.background_color, self.param_dict)

        wpf_palette_function(ctrl_props.text, f"{prop.name}.{sub_name}",
                             getattr(prop.value, sub_name), self.page_index,
                             ctrl_props.expander_name + ctrl_props.expander_state_key,
                             row_name, enabled, ctrl_props.min_value, ctrl_props.max_value,
                             interval_value, ctrl_props.as_slider,
                             ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code, background_color)


    def get_global_str_table_entry(self,
                                   text_id: str) -> str:
        """ get an entry from the global string table

        Args:
            text_id: id of the text

        Returns:
            text entry from the global string table
        """

        return self.global_str_table.get_entry(text_id)[0]

```

</details>