---
title: "PaletteRowControls"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteRowControls.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PaletteRowControls

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteRowControls.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the functions for the creation on the controls in a row

## Abhängigkeiten

- `BuildingElementStringTable`
- `ControlProperties`
- `PaletteControlByValueTypeCreator`
- `PaletteControlVisibility`
- `PaletteData`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `Utilities.MultiIndexListUtil`
- `ValueTypes.MultiIndex`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.ValueTypeUtils.ControlMinMaxUtil`
- `WpfPaletteBuilder`
- `__future__`
- `typing`

## Klassen

### `PaletteRowControls`

implementation of the functions for the creation on the controls in a row
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_all_row_controls` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, list_ctrl_props: ControlProperties, value_index_values: list[int | MultiIndex], is_text_from_script: bool, palette_data: PaletteData` | `None` | create all row controls  Args:     wpf_palette:         the palette to show.     prop:                parameter property     ctrl_props:          control properties     list_ctrl_props:     control properties for the list element     value_index_values:  value index values     is_text_from_script: create a dynamic text from a script state     palette_data:        palette data |
| `create_row_controls` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, list_ctrl_props: ControlProperties, set_row_name: bool, column_count: int, use_row: bool, is_text_from_script: bool, visible_column: int, palette_data: PaletteData` | `None` | create the row controls  Args:     wpf_palette:         the palette to show.     prop:                parameter property     ctrl_props:          control properties     list_ctrl_props:     control properties for the list element     set_row_name:        set the row name     column_count:        column count     use_row:             use a row for the controls     is_text_from_script: create a dynamic text from a script state     visible_column:      visible column     palette_data:        property palette control service |
| `create_multi_index_row_control` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, list_ctrl_props: ControlProperties, multi_index: MultiIndex, global_str_table: BuildingElementStringTable, palette_data: PaletteData` | `None` | create the multi index row controls  Args:     wpf_palette:      the palette to show.     prop:             parameter property     list_ctrl_props:  control properties for the list element     multi_index:      multi index     global_str_table: global string table     palette_data:     palette data |
| `__set_item_prop` | `prop: ParameterProperty, row: int, col: int, column_count: int, item_prop: ParameterProperty` | `None` | set the properties for the item  Args:     prop:         parameter property     row:          row index     col:          column index     column_count: column count     item_prop:    item properties |
| `__set_row_name` | `ctrl_props: ControlProperties, list_ctrl_props: ControlProperties, row: int, set_row_name: bool, column_count: int, use_row: bool, start_row: int, current_row: int, item_prop: ParameterProperty, row_name_len: int, col: int` | `None` | set the row name  Args:     ctrl_props:      control properties     list_ctrl_props: control properties for the list element     row:             row index     set_row_name:    set the row name state     column_count:    column count     use_row:         use a row for the controls     start_row:       start row     current_row:     current row     item_prop:       item properties     row_name_len:    length of the row name     col:             column index |
| `__create_row_control_by_value_type` | `wpf_palette: WpfPaletteBuilder, ctrl_props: ControlProperties, list_ctrl_props: ControlProperties, item_prop: ParameterProperty, palette_data: PaletteData` | `None` | create the control by the value type  Args:     wpf_palette:     the palette to show.     ctrl_props:      control properties     list_ctrl_props: control properties for the list element     item_prop:       item properties     palette_data:    palette data |
| `__create_row_index_control` | `wpf_palette: WpfPaletteBuilder, ctrl_props: ControlProperties, list_ctrl_props: ControlProperties, palette_data: PaletteData` | `None` | create the control for the row index  Args:     wpf_palette:     the palette to show.     ctrl_props:      control properties     list_ctrl_props: control properties for the list element     palette_data:    palette data |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the functions for the creation on the controls in a row
"""

from __future__ import annotations

from typing import cast

from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from Utilities.GeneralConstants import GeneralConstants
from Utilities.MultiIndexListUtil import MultiIndexListUtil

from ValueTypes.ValueTypeUtils.ControlMinMaxUtil import ControlMinMaxUtil

from ValueTypes.MultiIndex import MultiIndex
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

from .PaletteControlVisibility import PaletteControlVisibility
from .PaletteControlByValueTypeCreator import PaletteControlByValueTypeCreator
from .PaletteData import PaletteData
from .WpfPaletteBuilder import WpfPaletteBuilder

class PaletteRowControls():
    """ implementation of the functions for the creation on the controls in a row
    """

    GEO_LIB_NAME         = "NemAll_Python_Geometry"
    ROW_NAME_WIDTH_LIMIT = 4
    TWO_DIM_LIST         = 2

    @staticmethod
    def create_all_row_controls(wpf_palette        : WpfPaletteBuilder,
                                prop               : ParameterProperty,
                                ctrl_props         : ControlProperties,
                                list_ctrl_props    : ControlProperties,
                                value_index_values : list[(int | MultiIndex)],
                                is_text_from_script: bool,
                                palette_data       : PaletteData):
        """ create all row controls

        Args:
            wpf_palette:         the palette to show.
            prop:                parameter property
            ctrl_props:          control properties
            list_ctrl_props:     control properties for the list element
            value_index_values:  value index values
            is_text_from_script: create a dynamic text from a script state
            palette_data:        palette data
        """

        visible_column = cast(int, 0 if len(value_index_values) < PaletteRowControls.TWO_DIM_LIST else value_index_values[1])

        for row, obj_value in enumerate(prop.value):
            column_count = len(obj_value) if isinstance(obj_value, list) else 1

            if is_text_from_script:
                list_ctrl_props.row_name = ctrl_props.text

            palette_data.row = row

            PaletteRowControls.create_row_controls(wpf_palette, prop, ctrl_props, list_ctrl_props,
                                                   True, column_count, column_count > 1,
                                                   is_text_from_script, visible_column, palette_data)


    @staticmethod
    def create_row_controls(wpf_palette        : WpfPaletteBuilder,
                            prop               : ParameterProperty,
                            ctrl_props         : ControlProperties,
                            list_ctrl_props    : ControlProperties,
                            set_row_name       : bool,
                            column_count       : int,
                            use_row            : bool,
                            is_text_from_script: bool,
                            visible_column     : int,
                            palette_data       : PaletteData):
        """ create the row controls

        Args:
            wpf_palette:         the palette to show.
            prop:                parameter property
            ctrl_props:          control properties
            list_ctrl_props:     control properties for the list element
            set_row_name:        set the row name
            column_count:        column count
            use_row:             use a row for the controls
            is_text_from_script: create a dynamic text from a script state
            visible_column:      visible column
            palette_data:        property palette control service
        """

        row = palette_data.row

        start_row    = ctrl_props.value_list_start_row
        current_row  = start_row + row
        item_prop    = ParameterProperty()
        row_name_len = len(ctrl_props.row_name)

        if is_text_from_script:
            list_ctrl_props.row_name = ctrl_props.text.replace(GeneralConstants.LIST_ROW_KEYWORD, str(row))


        #------------- check the visibility of the row

        if not prop.value_type.is_tuple_type() and \
            not PaletteControlVisibility.is_visible_list_row(list_ctrl_props, row, palette_data.param_dict):
            return


        #------------- loop over all column

        for col in range(column_count):
            if visible_column and visible_column -1 != col:
                continue

            PaletteRowControls.__set_item_prop(prop, row, col, column_count, item_prop)


            #--------- set the row name

            if not is_text_from_script:
                PaletteRowControls.__set_row_name(ctrl_props, list_ctrl_props, row, set_row_name, column_count, use_row,
                                                  start_row, current_row, item_prop, row_name_len, col)


            #--------- index must be added as text control in case of using the entire row

            if not col and list_ctrl_props.row_state_key:
                PaletteRowControls.__create_row_index_control(wpf_palette, ctrl_props, list_ctrl_props, palette_data)


            #--------- create the control

            list_ctrl_props.text             = ctrl_props.text.replace(GeneralConstants.LIST_ROW_KEYWORD, str(row))
            list_ctrl_props.enable_condition = ctrl_props.enable_condition.replace(GeneralConstants.LIST_ROW_KEYWORD, str(row))

            PaletteRowControls.__create_row_control_by_value_type(wpf_palette, ctrl_props, list_ctrl_props,
                                                                  item_prop, palette_data)


    @staticmethod
    def create_multi_index_row_control(wpf_palette     : WpfPaletteBuilder,
                                       prop            : ParameterProperty,
                                       list_ctrl_props : ControlProperties,
                                       multi_index     : MultiIndex,
                                       global_str_table: BuildingElementStringTable,
                                       palette_data    : PaletteData):
        """ create the multi index row controls

        Args:
            wpf_palette:      the palette to show.
            prop:             parameter property
            list_ctrl_props:  control properties for the list element
            multi_index:      multi index
            global_str_table: global string table
            palette_data:     palette data
        """

        item_prop = ParameterProperty()

        item_prop.value, varied = MultiIndexListUtil.get_value(prop, multi_index, global_str_table)


        #----------------- create the control for varied values

        if varied:
            if GeneralConstants.COMBOBOX_KEY in prop.value_type:
                if prop.value_type == ParameterPropertyValueTypes.LENGTH_COMBO_BOX:
                    value_list = [prop.value_type.get_value(item) for item in list_ctrl_props.value_list.split("|")]

                    list_ctrl_props.value_list = "|".join(prop.value_type.value_to_unit_string(cast(int, item)) for item in value_list)

                item_prop.value_type = ParameterPropertyValueTypes.STRING_COMBO_BOX
            else:
                item_prop.value_type = ParameterPropertyValueTypes.STRING
        else:
            item_prop.value_type = prop.value_type

        item_prop.name = f"{prop.name}[{multi_index.get_indexes(True)}]"

        ControlMinMaxUtil.set_min_max_values(list_ctrl_props, item_prop.value_type, cast(int, item_prop.attribute_id),
                                             palette_data.param_dict)

        PaletteControlByValueTypeCreator.excecute(wpf_palette, item_prop, list_ctrl_props, item_prop.value_type, palette_data)


    @staticmethod
    def __set_item_prop(prop        : ParameterProperty,
                        row         : int,
                        col         : int,
                        column_count: int,
                        item_prop   : ParameterProperty):
        """ set the properties for the item

        Args:
            prop:         parameter property
            row:          row index
            col:          column index
            column_count: column count
            item_prop:    item properties
        """

        item_prop.value = prop.value[row] if column_count == 1 and not isinstance(prop.value[row], list) else prop.value[row][col]


        #------------- set the selected value for the item

        if isinstance(prop.selected_value, list):
            item_prop.selected_value = prop.selected_value[row] \
                                       if column_count == 1 and not isinstance(prop.selected_value[row], list) else \
                                       prop.selected_value[row][col]
        else:
            item_prop.selected_value = prop.selected_value

        item_prop.name             = f"{prop.name}[{row}]"
        item_prop.value_type       = prop.value_type
        item_prop.group_name       = prop.group_name
        item_prop.attribute_id_str = prop.attribute_id_str

        if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE and isinstance(item_prop.attribute_id, list):
            item_prop.attribute_id_str = str(item_prop.attribute_id[row] if row < len(item_prop.attribute_id) else \
                                            item_prop.attribute_id[0])

        if prop.named_tuple_def:
            item_prop.set_named_tuple_def(prop.named_tuple_def.typename, prop.named_tuple_def.field_names)

        if column_count > 1 or isinstance(prop.value[row], list):
            item_prop.name += f"[{col}]"


    @staticmethod
    def __set_row_name(ctrl_props     : ControlProperties,
                       list_ctrl_props: ControlProperties,
                       row            : int,
                       set_row_name   : bool,
                       column_count   : int,
                       use_row        : bool,
                       start_row      : int,
                       current_row    : int,
                       item_prop      : ParameterProperty,
                       row_name_len   : int,
                       col            : int):
        """ set the row name

        Args:
            ctrl_props:      control properties
            list_ctrl_props: control properties for the list element
            row:             row index
            set_row_name:    set the row name state
            column_count:    column count
            use_row:         use a row for the controls
            start_row:       start row
            current_row:     current row
            item_prop:       item properties
            row_name_len:    length of the row name
            col:             column index
        """

        if use_row and not ctrl_props.row_name:
            list_ctrl_props.row_name = str(current_row)

        elif not use_row and PaletteRowControls.GEO_LIB_NAME in str(type(item_prop.value)):
            list_ctrl_props.row_name = list_ctrl_props.text

        if set_row_name and not row_name_len:
            if start_row == -1:
                list_ctrl_props.row_name = " " * (row + 1)
            else:
                list_ctrl_props.row_name = str(current_row)

        if not use_row and set_row_name and column_count > 1:
            list_ctrl_props.row_name = str(start_row + col)


    @staticmethod
    def __create_row_control_by_value_type(wpf_palette    : WpfPaletteBuilder,
                                           ctrl_props     : ControlProperties,
                                           list_ctrl_props: ControlProperties,
                                           item_prop      : ParameterProperty,
                                           palette_data   : PaletteData):
        """ create the control by the value type

        Args:
            wpf_palette:     the palette to show.
            ctrl_props:      control properties
            list_ctrl_props: control properties for the list element
            item_prop:       item properties
            palette_data:    palette data
        """

        if ctrl_props.row_name:
            list_ctrl_props.row_name = ctrl_props.row_name.replace(GeneralConstants.LIST_ROW_KEYWORD, str(palette_data.row))

        list_ctrl_props.enable_function  = None

        if ctrl_props.enable_function and not item_prop.value_type.is_tuple_type():
            list_ctrl_props.enable_condition = str(ctrl_props.enable_function(palette_data.row))

        ControlMinMaxUtil.set_min_max_values(list_ctrl_props, item_prop.value_type, cast(int, item_prop.attribute_id),
                                             palette_data.param_dict)

        PaletteControlByValueTypeCreator.excecute(wpf_palette, item_prop, list_ctrl_props, item_prop.value_type, palette_data)


    @staticmethod
    def __create_row_index_control(wpf_palette    : WpfPaletteBuilder,
                                   ctrl_props     : ControlProperties,
                                   list_ctrl_props: ControlProperties,
                                   palette_data   : PaletteData):
        """ create the control for the row index

        Args:
            wpf_palette:     the palette to show.
            ctrl_props:      control properties
            list_ctrl_props: control properties for the list element
            palette_data:    palette data
        """

        index_ctrl_props = ControlProperties("", f"___{ctrl_props.value_name}", "", "", ctrl_props.page,
                                                     ctrl_props.expander_name, list_ctrl_props.row_name,
                                                     "", "", "", "", row_state_key = ctrl_props.row_state_key)

        if len(list_ctrl_props.row_name) < PaletteRowControls.ROW_NAME_WIDTH_LIMIT:
            index_ctrl_props.width = 10

        index_data = ParameterProperty()

        index_data.value      = list_ctrl_props.row_name
        index_data.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.TEXT)

        PaletteControlByValueTypeCreator.excecute(wpf_palette, index_data, index_ctrl_props, index_data.value_type, palette_data)

```

</details>