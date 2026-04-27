---
title: "PaletteListGroup"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteListGroup.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PaletteListGroup

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteListGroup.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the palette list group creation

## Abhängigkeiten

- `ControlProperties`
- `PaletteControlByValueTypeCreator`
- `PaletteData`
- `ParameterProperty`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ValueTypeUtils.ControlMinMaxUtil`
- `WpfPaletteBuilder`
- `__future__`
- `collections.abc`
- `inspect`
- `typing`

## Klassen

### `PaletteListGroup`

implementation of the palette list group creation
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `check_list_group_creation` | `self, wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_prop: ControlProperties, palette_data: PaletteData` | `bool` | check for a list group creation  Args:     wpf_palette:  the palette to show.     prop:         property     ctrl_prop:    control properties     palette_data: palette data  Returns:     state for execute list group creation |
| `create_list_group_control` | `self, wpf_palette: WpfPaletteBuilder, palette_data: PaletteData` | `None` | create the list group control  Args:     wpf_palette:  the palette to show.     palette_data: palette data |
| `__create_list_group_control` | `self, wpf_palette: WpfPaletteBuilder, palette_data: PaletteData` | `None` | create the list group control  Args:     wpf_palette:  the palette to show.     palette_data: palette data |
| `__set_control_data` | `param_dict: dict[str, Any], row: int, prop: ParameterProperty, ctrl_props: ControlProperties, is_visual_script: bool` | `ControlProperties` | set the control data  Args:     param_dict:       parameter dictionary     row:              row     prop:             property     ctrl_props:       control properties     is_visual_script: is visual script state  Returns:     control properties of the row |
| `__set_prop_data` | `row: int, prop: ParameterProperty, ctrl_props_row: ControlProperties, param_dict: dict[str, Any]` | `ParameterProperty` | set the property data of the row  Args:     row:            row     prop:           property     ctrl_props_row: description     param_dict:     parameter dictionary  Returns:     property data of the row |
| `__get_max_item_count` | `self, param_dict: dict[str, Any]` | `int` | get the max value item count  Args:     param_dict: parameter dictionary  Returns:     max value item count |
| `__get_visible_fcts` | `self` | `list[Callable | None]` | get the visible functions  Returns:     visible functions |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the palette list group creation
"""

from __future__ import annotations

from typing import cast, Any

from collections.abc import Callable

import inspect

from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate

from ValueTypes.ValueTypeUtils.ControlMinMaxUtil import ControlMinMaxUtil
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from Utilities.GeneralConstants import GeneralConstants

from .PaletteControlByValueTypeCreator import PaletteControlByValueTypeCreator
from .PaletteData import PaletteData
from .WpfPaletteBuilder import WpfPaletteBuilder

class PaletteListGroup():
    """ implementation of the palette list group creation
    """

    def __init__(self):
        """ initialize
        """

        self.list_group_controls = []
        self.list_group_name     = "???"


    def check_list_group_creation(self,
                                  wpf_palette : WpfPaletteBuilder,
                                  prop        : ParameterProperty,
                                  ctrl_prop   : ControlProperties,
                                  palette_data: PaletteData) -> bool:
        """ check for a list group creation

        Args:
            wpf_palette:  the palette to show.
            prop:         property
            ctrl_prop:    control properties
            palette_data: palette data

        Returns:
            state for execute list group creation
        """

        if self.list_group_controls and self.list_group_name != ctrl_prop.list_group_name:
            self.list_group_name = "???"

            self.__create_list_group_control(wpf_palette, palette_data)

            self.list_group_controls = []

        if ctrl_prop.list_group_name:
            self.list_group_controls.append((prop, ctrl_prop))

            self.list_group_name = ctrl_prop.list_group_name

            return True

        return False


    def create_list_group_control(self,
                                  wpf_palette : WpfPaletteBuilder,
                                  palette_data: PaletteData):
        """ create the list group control

        Args:
            wpf_palette:  the palette to show.
            palette_data: palette data
        """

        if self.list_group_controls:
            self.__create_list_group_control(wpf_palette, palette_data)


    def __create_list_group_control(self,
                                    wpf_palette : WpfPaletteBuilder,
                                    palette_data: PaletteData):
        """ create the list group control

        Args:
            wpf_palette:  the palette to show.
            palette_data: palette data
        """

        #----------------- get the max list count

        max_count = self.__get_max_item_count(palette_data.param_dict)

        visible_fcts = self.__get_visible_fcts()


        #----------------- create the controls

        for row in range(max_count):
            palette_data.row = row

            for list_group_index, (prop, ctrl_props) in enumerate(self.list_group_controls):
                if not PaletteControlByValueTypeCreator.is_visible_row(visible_fcts[list_group_index], ctrl_props.visible_condition,
                                                                       row, "", palette_data.param_dict):
                    continue

                ctrl_props_row = self.__set_control_data(palette_data.param_dict, row, prop, ctrl_props,
                                                         palette_data.is_visual_script)

                prop_row = self.__set_prop_data(row, prop, ctrl_props_row, palette_data.param_dict)

                if isinstance(prop.value, list):
                    prop_row.name       = f"{prop.name}[{row + ctrl_props.list_index_offset}]"
                    prop_row.value      = prop.value[row + ctrl_props.list_index_offset]
                    prop_row.value_type = prop.value_type

                PaletteControlByValueTypeCreator.excecute(wpf_palette, prop_row, ctrl_props_row, prop.value_type, palette_data)


    @staticmethod
    def __set_control_data(param_dict      : dict[str, Any],
                           row             : int,
                           prop            : ParameterProperty,
                           ctrl_props      : ControlProperties,
                           is_visual_script: bool) -> ControlProperties:
        """ set the control data

        Args:
            param_dict:       parameter dictionary
            row:              row
            prop:             property
            ctrl_props:       control properties
            is_visual_script: is visual script state

        Returns:
            control properties of the row
        """

        ctrl_props_row = ctrl_props.deep_copy()

        ctrl_props_row.text              = StringEvaluate.eval_list_row(ctrl_props.text, row, param_dict)
        ctrl_props_row.expander_name     = StringEvaluate.eval_list_row(ctrl_props.expander_name, row, param_dict)
        ctrl_props_row.row_name          = StringEvaluate.eval_list_row(ctrl_props.row_name, row, param_dict)
        ctrl_props_row.visible_condition = StringEvaluate.eval_list_row(ctrl_props_row.visible_condition, row, param_dict)
        ctrl_props_row.enable_condition  = StringEvaluate.eval_list_row(ctrl_props_row.enable_condition, row, param_dict)

        if ParameterPropertyValueTypes.is_button_type(prop.value_type):
            PaletteControlByValueTypeCreator.set_row_button_event_id(ctrl_props_row, prop.value_type, ctrl_props.event_id, row,
                                                                     param_dict, is_visual_script)

        return ctrl_props_row


    @staticmethod
    def __set_prop_data(row           : int,
                        prop          : ParameterProperty,
                        ctrl_props_row: ControlProperties,
                        param_dict    : dict[str, Any]) -> ParameterProperty:
        """ set the property data of the row

        Args:
            row:            row
            prop:           property
            ctrl_props_row: description
            param_dict:     parameter dictionary

        Returns:
            property data of the row
        """

        prop_row = prop.deep_copy()

        prop_row.attribute_id_str = prop.attribute_id_str

        if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE and isinstance(prop_row.attribute_id, list):
            prop_row.attribute_id_str = str(prop_row.attribute_id[row] if row < len(prop_row.attribute_id) else prop_row.attribute_id[0])

        ControlMinMaxUtil.set_min_max_values(ctrl_props_row, prop.value_type, cast(int, prop_row.attribute_id),
                                             param_dict)

        if prop_row.value_type == ParameterPropertyValueTypes.PICTURE:
            prop_row.value = prop_row.value.replace(GeneralConstants.LIST_ROW_KEYWORD, str(row))

        return prop_row


    def __get_max_item_count(self,
                             param_dict: dict[str, Any]) -> int:
        """ get the max value item count

        Args:
            param_dict: parameter dictionary

        Returns:
            max value item count
        """

        max_count = 0

        for prop, _ in self.list_group_controls:
            if prop.dimensions:                                                                                     # pylint: disable = consider-ternary-expression
                max_count = max(max_count, StringEvaluate.eval_dimension(prop.dimensions, param_dict))
            else:
                max_count = max(max_count, len(prop.value) if isinstance(prop.value, list) else 1)

        return max_count


    def __get_visible_fcts(self) -> list[Callable | None]:
        """ get the visible functions

        Returns:
            visible functions
        """

        return [ctrl_props.visible_function if ctrl_props.visible_function and \
                                               inspect.getfullargspec(ctrl_props.visible_function).args else None \
                for _, ctrl_props in self.list_group_controls]

```

</details>