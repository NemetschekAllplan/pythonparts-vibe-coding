---
title: "PaletteControlByValueTypeCreator"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteControlByValueTypeCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PaletteControlByValueTypeCreator

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteControlByValueTypeCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the control by value type creator

## Abhängigkeiten

- `ControlProperties`
- `NemAll_Python_Utility`
- `PaletteData`
- `ParameterProperty`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueType`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ValueTypeUtils.PropertyPaletteControlService`
- `WpfPaletteBuilder`
- `typing`

## Klassen

### `PaletteControlByValueTypeCreator`

implementation of the control by value type creator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `excecute` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, value_type: ParameterPropertyValueType, palette_data: PaletteData` | `None` | execute the control by the value type creation  Args:     wpf_palette:  WPF palette     prop:         parameter property     ctrl_props:   control properties     value_type:   vale type     palette_data: palette data |
| `is_visible_row` | `visible_fct: Any, visible_condition: str, row: int, field_name: str, param_dict: dict[str, Any]` | `bool` | test for visible row  Args:     visible_fct:       visible function     visible_condition: visible condition     row:               row index     field_name:        field name in case of named tuple. Defaults to "".     param_dict:        parameter dict  Returns:     row visibility state |
| `set_row_button_event_id` | `ctrl_props: ControlProperties, value_type: ParameterPropertyValueType, event_id_str: str, row: int, param_dict: dict[str, Any], is_visual_script: bool` | `None` | set the event id for a row button  Args:     ctrl_props:       control properties     value_type:       value type     event_id_str:     event id string     row:              row index     param_dict:       parameter dict     is_visual_script: visual script state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the control by value type creator
"""

# pylint: disable=unused-private-member

from typing import Any

import NemAll_Python_Utility as AllplanUtil

from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

from ValueTypes.ParameterPropertyValueType import ParameterPropertyValueType
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from .PaletteData import PaletteData
from .WpfPaletteBuilder import WpfPaletteBuilder

class PaletteControlByValueTypeCreator():
    """ implementation of the control by value type creator
    """

    @staticmethod
    def excecute(wpf_palette : WpfPaletteBuilder,
                 prop        : ParameterProperty,
                 ctrl_props  : ControlProperties,
                 value_type  : ParameterPropertyValueType,
                 palette_data: PaletteData):
        """ execute the control by the value type creation

        Args:
            wpf_palette:  WPF palette
            prop:         parameter property
            ctrl_props:   control properties
            value_type:   vale type
            palette_data: palette data
        """

        if not value_type.has_impl:
            AllplanUtil.ShowMessageBox(f"PaletteControlByValueTypeCreator.py - control type '{prop.value_type}" \
                                       f"for {ctrl_props.value_name}' could not be created",
                                       AllplanUtil.MB_OK)

            return

        prop_pal_ctrl_service  = PropertyPaletteControlService(palette_data)


        #----------------- evaluate the text

        if StringEvaluate.is_text_from_script(ctrl_props.row_name) or       \
           StringEvaluate.is_text_from_script(ctrl_props.expander_name) or  \
           StringEvaluate.is_text_from_script(ctrl_props.text) or           \
           StringEvaluate.is_text_from_script(ctrl_props.group_text):
            ctrl_props = ctrl_props.deep_copy()

            ctrl_props.row_name      = StringEvaluate.eval_text(ctrl_props.row_name, palette_data.param_dict)
            ctrl_props.expander_name = StringEvaluate.eval_text(ctrl_props.expander_name, palette_data.param_dict)
            ctrl_props.text          = StringEvaluate.eval_text(ctrl_props.text, palette_data.param_dict)
            ctrl_props.group_text    = StringEvaluate.eval_text(ctrl_props.group_text, palette_data.param_dict)


        #----------------- use dialog controls from attribute ID and value

        is_dynamic_list = ParameterPropertyValueTypes.DYNAMIC_LIST in prop.value_type

        if not is_dynamic_list and \
           ctrl_props.value_dialog and not ctrl_props.value_dialog.has_input_controls(prop.value_type) and \
            ctrl_props.value_dialog.create_controls(wpf_palette, prop, ctrl_props,
                                                    palette_data.page_index, palette_data.global_str_table,
                                                    prop_pal_ctrl_service.is_control_enabled):
            return


        #----------------- create the controls by value type

        value_type.add_to_palette(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)

        if not is_dynamic_list and ctrl_props.value_dialog:
            ctrl_props.value_dialog.create_controls(wpf_palette, prop, ctrl_props, palette_data.page_index,
                                                    palette_data.global_str_table,
                                                    prop_pal_ctrl_service.is_control_enabled)

    @staticmethod
    def is_visible_row(visible_fct      : Any,
                       visible_condition: str,
                       row              : int,
                       field_name       : str,
                       param_dict       : dict[str, Any]) -> bool:
        """ test for visible row

        Args:
            visible_fct:       visible function
            visible_condition: visible condition
            row:               row index
            field_name:        field name in case of named tuple. Defaults to "".
            param_dict:        parameter dict

        Returns:
            row visibility state
        """

        if visible_fct:
            if field_name:
                if row != -1:
                    return visible_fct(row, field_name)

                return visible_fct(field_name)

            return visible_fct(row)

        if visible_condition:
            visible_condition = visible_condition.split(GeneralConstants.TEXT_SEPARATOR, 1)[0]. \
                                                  replace(GeneralConstants.LIST_ROW_KEYWORD, str(row))

            return StringEvaluate.eval_condition(visible_condition, param_dict)

        return True


    @staticmethod
    def set_row_button_event_id(ctrl_props      : ControlProperties,
                                value_type      : ParameterPropertyValueType,
                                event_id_str    : str,
                                row             : int,
                                param_dict      : dict[str, Any],
                                is_visual_script: bool):
        """ set the event id for a row button

        Args:
            ctrl_props:       control properties
            value_type:       value type
            event_id_str:     event id string
            row:              row index
            param_dict:       parameter dict
            is_visual_script: visual script state
        """

        event_id = int(StringEvaluate.eval_constants(event_id_str, param_dict))

        if is_visual_script:
            node_event_id = event_id >> 16
            node_index    = event_id - (node_event_id << 16)

            event_id = (((max(row, 0) * 10) + node_event_id) << 16) + node_index
        else:
            event_id =  (row << 16) + event_id

        ctrl_props.event_id = str(event_id)

        if value_type == ParameterPropertyValueTypes.BUTTON and not ctrl_props.row_name:
            ctrl_props.row_name, _, ctrl_props.text = ctrl_props.text.partition(GeneralConstants.TEXT_SEPARATOR)

            ctrl_props.text     = StringEvaluate.eval_list_row(ctrl_props.text, row, param_dict)
            ctrl_props.row_name = StringEvaluate.eval_list_row(ctrl_props.row_name, row, param_dict)

```

</details>