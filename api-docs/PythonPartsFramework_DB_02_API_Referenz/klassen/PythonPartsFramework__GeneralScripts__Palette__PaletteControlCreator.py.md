---
title: "PaletteControlCreator"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteControlCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PaletteControlCreator

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteControlCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the palette control creator

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_Palette`
- `NemAll_Python_Utility`
- `PaletteControlByValueTypeCreator`
- `PaletteData`
- `PaletteRowControls`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypes.MultiIndex`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.ValueTypeUtils.ControlMinMaxUtil`
- `WpfPaletteBuilder`
- `__future__`
- `typing`

## Klassen

### `PaletteControlCreator`

implementation of the palette control creator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_control` | `wpf_palette: WpfPaletteBuilder, build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties, palette_data: PaletteData` | `None` | create the control  Args:     wpf_palette:  the palette to show.     build_ele:    building element with the parameter properties     prop:         parameter property     ctrl_props:   control properties     palette_data: palette data |
| `__set_selected_value` | `build_ele: BuildingElement, prop: ParameterProperty` | `None` | set the selected value  Args:     build_ele: building element with the parameter properties     prop:      parameter property |
| `get_value_index_name_values` | `build_ele: BuildingElement, ctrl_props: ControlProperties` | `tuple[bool, list[int | MultiIndex]]` | get the values of the value index names  Args:     build_ele:  building element with the parameter properties     ctrl_props: control properties  Returns:     result state, list with the values |
| `__is_valid_value_index` | `value_index: list[int] | int | MultiIndex, value_index_name: str` | `bool` | test the value index  Args:     value_index:      value index     value_index_name: value index name  Returns:     valid state |
| `create_full_row_text` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, palette_data: PaletteData` | `None` | create row text for a full row as normal text  Args:     wpf_palette:  the palette to show.     prop:         parameter property     ctrl_props:   control properties     palette_data: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the palette control creator
"""

from __future__ import annotations

from typing import cast

import NemAll_Python_Palette as AllplanPalette
import NemAll_Python_Utility as AllplanUtil

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate

from ValueTypes.ValueTypeUtils.ControlMinMaxUtil import ControlMinMaxUtil

from ValueTypes.MultiIndex import MultiIndex
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

from .PaletteControlByValueTypeCreator import PaletteControlByValueTypeCreator
from .PaletteData import PaletteData
from .PaletteRowControls import PaletteRowControls
from .WpfPaletteBuilder import WpfPaletteBuilder

class PaletteControlCreator():
    """ implementation of the palette control creator
    """

    TWO_DIM_LIST = 2

    @staticmethod
    def create_control(wpf_palette : WpfPaletteBuilder,
                       build_ele   : BuildingElement,
                       prop        : ParameterProperty,
                       ctrl_props  : ControlProperties,
                       palette_data: PaletteData):
        """ create the control

        Args:
            wpf_palette:  the palette to show.
            build_ele:    building element with the parameter properties
            prop:         parameter property
            ctrl_props:   control properties
            palette_data: palette data
        """

        ctrl_props.visible = True

        PaletteControlCreator.__set_selected_value(build_ele, prop)


        #----------------- add single value

        value_type = prop.value_type

        if not isinstance(prop.value, list) or not value_type.is_add_to_palette_for_single_list_item() or \
           value_type.startswith(ParameterPropertyValueTypes.DYNAMIC_LIST):
            ControlMinMaxUtil.set_min_max_values(ctrl_props, prop.value_type, cast(int, prop.attribute_id),
                                                 palette_data.param_dict)

            PaletteControlByValueTypeCreator.excecute(wpf_palette, prop, ctrl_props, value_type, palette_data)

            return


        #----------------- add list values (value is created as list with no list type)

        if not prop.value:
            return

        result, value_index_values = PaletteControlCreator.get_value_index_name_values(build_ele, ctrl_props)

        if not result:
            return

        list_ctrl_props = ctrl_props.deep_copy()

        is_text_from_script = StringEvaluate.is_text_from_script(ctrl_props.text)


        #----------------- create the a multi index row control

        if value_index_values and isinstance(value_index_values[0], MultiIndex):
            PaletteRowControls.create_multi_index_row_control(wpf_palette, prop, list_ctrl_props, value_index_values[0],
                                                              build_ele.get_string_tables()[1], palette_data)

            return


        #------------- show all rows

        value_index_values = cast(list, value_index_values)

        if not value_index_values or value_index_values and value_index_values[0] <= ctrl_props.value_index_name_base - 1:
            PaletteRowControls.create_all_row_controls(wpf_palette,  prop, ctrl_props, list_ctrl_props,
                                                       value_index_values, is_text_from_script, palette_data)

            return


        #------------- show only the row with the defined index

        if (row := value_index_values[0] - ctrl_props.value_index_name_base) < len(prop.value):
            column_count = len(prop.value[row]) if isinstance(prop.value[row], list) else 1

            palette_data.row = row

            PaletteRowControls.create_row_controls(wpf_palette, prop, ctrl_props, list_ctrl_props,
                                                   False, column_count, column_count > 1, is_text_from_script,
                                                   0 if len(value_index_values) < PaletteControlCreator.TWO_DIM_LIST else \
                                                   value_index_values[1],
                                                   palette_data)


    @staticmethod
    def __set_selected_value(build_ele: BuildingElement,
                             prop     : ParameterProperty):
        """ set the selected value

        Args:
            build_ele: building element with the parameter properties
            prop:      parameter property
        """


        if prop.value_type == ParameterPropertyValueTypes.RADIO_BUTTON:
            if (group_prop := build_ele.get_property(prop.group_name)) is not None and not isinstance(group_prop.value, list):
                prop.selected_value = group_prop.value


    @staticmethod
    def get_value_index_name_values(build_ele : BuildingElement,
                                    ctrl_props: ControlProperties) -> tuple[bool, list[(int | MultiIndex)]]:
        """ get the values of the value index names

        Args:
            build_ele:  building element with the parameter properties
            ctrl_props: control properties

        Returns:
            result state, list with the values
        """

        value_index_props = []

        for value_index_name in ctrl_props.value_index_name.split(","):
            if not value_index_name:
                continue

            if value_index_name.isnumeric():
                value_index_props.append(int(value_index_name))

                continue


            #------------- value index from a constraint

            value_index = None

            if (index_prop := build_ele.get_property(value_index_name)) is not None:
                value_index = index_prop.value

            elif (index_prop := build_ele.get_constant(value_index_name)) is not None:
                value_index = index_prop

            else:
                AllplanUtil.ShowMessageBox(f"ValueIndexName: {value_index_name} doesn't exist !!!", AllplanUtil.MB_OK)
                return False, []

            if not PaletteControlCreator.__is_valid_value_index(value_index, value_index_name):
                return False, []

            value_index_props.append(value_index)

        return True, value_index_props


    @staticmethod
    def __is_valid_value_index(value_index     : (list[int] | int | MultiIndex),
                               value_index_name: str) -> bool:
        """ test the value index

        Args:
            value_index:      value index
            value_index_name: value index name

        Returns:
            valid state
        """

        if isinstance(value_index, MultiIndex):
            for item in value_index:
                if item[0] < 0:
                    AllplanUtil.ShowMessageBox(f"ValueIndexName: {value_index_name} must have minimal value 1 !!!", AllplanUtil.MB_OK)
                    return False

        elif isinstance(value_index, list):
            for item in value_index:
                if item < 0:
                    AllplanUtil.ShowMessageBox(f"ValueIndexName: {value_index_name} must have minimal value 1 !!!", AllplanUtil.MB_OK)
                    return False

        elif value_index < 0:
            AllplanUtil.ShowMessageBox(f"ValueIndexName: {value_index_name} must have minimal value 1 !!!", AllplanUtil.MB_OK)
            return False

        return True


    @staticmethod
    def create_full_row_text(wpf_palette : WpfPaletteBuilder,
                             prop        : ParameterProperty,
                             ctrl_props  : ControlProperties,
                             palette_data: PaletteData):
        """ create row text for a full row as normal text

        Args:
            wpf_palette:  the palette to show.
            prop:         parameter property
            ctrl_props:   control properties
            palette_data: property palette control service
        """

        if not palette_data.row_full_text:
            return

        if prop.value_type == ParameterPropertyValueTypes.TEXT or not palette_data.row_full_text.strip():
            palette_data.row_full_text = ""

            return

        index_ctrl_props = ControlProperties("", f"___{ctrl_props.value_name}",  "",  "",  ctrl_props.page,
                                             ctrl_props.expander_name,
                                             palette_data.row_full_text,
                                             "", "", "", "", row_state_key = ctrl_props.row_state_key)

        text_prop = ParameterProperty()

        text_prop.value          = palette_data.row_full_text
        text_prop.selected_value = AllplanPalette.Orientation.eRight
        text_prop.value_type     = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.TEXT)

        PaletteControlByValueTypeCreator.excecute(wpf_palette, text_prop, index_ctrl_props, text_prop.value_type, palette_data)

        palette_data.row_full_text = ""

```

</details>