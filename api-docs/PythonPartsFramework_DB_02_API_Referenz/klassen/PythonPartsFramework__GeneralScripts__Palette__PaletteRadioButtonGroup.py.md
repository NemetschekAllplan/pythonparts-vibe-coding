---
title: "PaletteRadioButtonGroup"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteRadioButtonGroup.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PaletteRadioButtonGroup

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteRadioButtonGroup.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the palette radio button group creation

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `PaletteControlByValueTypeCreator`
- `PaletteControlCreator`
- `PaletteControlVisibility`
- `PaletteData`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `WpfPaletteBuilder`
- `__future__`
- `typing`

## Klassen

### `PaletteRadioButtonGroup`

implementation of the palette radio button group creation
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `check_radio_button_group` | `self, wpf_palette: WpfPaletteBuilder, build_ele: BuildingElement, prop: ParameterProperty, ctrl_prop: ControlProperties, visible_condition: str, palette_data: PaletteData` | `bool` | check for a radio button group creation  Args:     wpf_palette:       the palette to show.     build_ele:         building element with the parameter properties     prop:              property     ctrl_prop:         control properties     visible_condition: visible condition     palette_data:      palette data  Returns:     state for execute radio button group |
| `check_radio_button` | `self, prop: ParameterProperty, ctrl_prop: ControlProperties` | `bool` | check for a radio button  Args:     prop:      property     ctrl_prop: control properties  Returns:     state for executed radio button |
| `create_radio_button_group_control` | `self, wpf_palette: WpfPaletteBuilder, build_ele: BuildingElement, palette_data: PaletteData` | `None` | create the radio button group control  Args:     wpf_palette:  the palette to show.     build_ele:    building element with the parameter properties     palette_data: palette data |
| `__create_radio_button_group_control` | `self, wpf_palette: WpfPaletteBuilder, build_ele: BuildingElement, palette_data: PaletteData` | `None` | create the radio button group control  Args:     wpf_palette:  the palette to show.     build_ele:    building element with the parameter properties     palette_data: palette data |
| `__add_row_index` | `wpf_palette: WpfPaletteBuilder, radio_button_group_controls: list[tuple[ParameterProperty, ControlProperties]], column: int, palette_data: PaletteData` | `None` | index must be added as text control in case of using the entire row  Args:     wpf_palette:                 the palette to show.     radio_button_group_controls: radio button group controls     column:                      column index     palette_data:                palette data |
| `__create_group_controls_in_row` | `wpf_palette: WpfPaletteBuilder, build_ele: BuildingElement, radio_button_group_controls: list[tuple[ParameterProperty, ControlProperties]], column: int, col_sel_value: int, has_column: bool, palette_data: PaletteData` | `None` | create the controls for one row  Args:     wpf_palette:                 the palette to show.     build_ele:                   building element with the parameter properties     radio_button_group_controls: _description_     column:                      column index     col_sel_value:               selected value of the column     has_column:                  has column state     palette_data:                palette data |
| `replace_row_col_keywords` | `text: str, row: int, col: int` | `str` | replace the row and column keyword by the row and column  Args:     text: text     row:  row index     col:  column index  Returns:     adapted text |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the palette radio button group creation
"""


from __future__ import annotations

from typing import cast

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

from .PaletteControlCreator import PaletteControlCreator
from .PaletteData import PaletteData
from .PaletteControlVisibility import PaletteControlVisibility
from .PaletteControlByValueTypeCreator import PaletteControlByValueTypeCreator
from .WpfPaletteBuilder import WpfPaletteBuilder

class PaletteRadioButtonGroup():
    """ implementation of the palette radio button group creation
    """

    ROW_NAME_WIDTH_LIMIT = 4
    TWO_DIM_LIST         = 2

    def __init__(self):
        """ initialize
        """

        self.radio_button_group_controls = []
        self.radio_button_group_ctrl     = None
        self.radio_button_group_name     = ""
        self.radio_button_group_visible  = ""


    def check_radio_button_group(self,
                                 wpf_palette      : WpfPaletteBuilder,
                                 build_ele        : BuildingElement,
                                 prop             : ParameterProperty,
                                 ctrl_prop        : ControlProperties,
                                 visible_condition: str,
                                 palette_data     : PaletteData) -> bool:
        """ check for a radio button group creation

        Args:
            wpf_palette:       the palette to show.
            build_ele:         building element with the parameter properties
            prop:              property
            ctrl_prop:         control properties
            visible_condition: visible condition
            palette_data:      palette data

        Returns:
            state for execute radio button group
        """

        if prop.value_type != ParameterPropertyValueTypes.RADIO_BUTTON and \
           self.radio_button_group_controls and self.radio_button_group_ctrl is not None:
            self.__create_radio_button_group_control(wpf_palette, build_ele, palette_data)

            self.radio_button_group_controls = []

        if prop.value_type == ParameterPropertyValueTypes.RADIO_BUTTON_GROUP:
            self.radio_button_group_name    = ctrl_prop.value_name
            self.radio_button_group_ctrl    = ctrl_prop
            self.radio_button_group_visible = PaletteControlVisibility.is_visible_control(palette_data, ctrl_prop, visible_condition)

            return True

        if prop.value_type == ParameterPropertyValueTypes.RADIO_BUTTON:
            if not self.radio_button_group_visible and self.radio_button_group_name == prop.group_name:
                ctrl_prop.visible = False

                return True

        return False


    def check_radio_button(self,
                           prop     : ParameterProperty,
                           ctrl_prop: ControlProperties) -> bool:
        """ check for a radio button

        Args:
            prop:      property
            ctrl_prop: control properties

        Returns:
            state for executed radio button
        """

        if prop.value_type == ParameterPropertyValueTypes.RADIO_BUTTON and self.radio_button_group_name == prop.group_name and \
           isinstance(prop.selected_value, list):
            self.radio_button_group_controls.append((prop, ctrl_prop))

            return True

        return False


    def create_radio_button_group_control(self,
                                          wpf_palette : WpfPaletteBuilder,
                                          build_ele   : BuildingElement,
                                          palette_data: PaletteData):
        """ create the radio button group control

        Args:
            wpf_palette:  the palette to show.
            build_ele:    building element with the parameter properties
            palette_data: palette data
        """

        if self.radio_button_group_controls and self.radio_button_group_ctrl is not None:
            self.__create_radio_button_group_control(wpf_palette, build_ele, palette_data)

        self.radio_button_group_controls = []


    def __create_radio_button_group_control(self,
                                            wpf_palette : WpfPaletteBuilder,
                                            build_ele   : BuildingElement,
                                            palette_data: PaletteData):
        """ create the radio button group control

        Args:
            wpf_palette:  the palette to show.
            build_ele:    building element with the parameter properties
            palette_data: palette data
        """


        #------------- get the visible state

        if self.radio_button_group_ctrl is None:
            return

        result, value_index_values = PaletteControlCreator.get_value_index_name_values(build_ele, self.radio_button_group_ctrl)

        if not result:
            return

        value_index_values = cast(list, value_index_values)

        radio_button_group_prop = build_ele.get_existing_property(self.radio_button_group_ctrl.value_name)


        #------------- show the rows

        for row, sel_value in enumerate(radio_button_group_prop.value):
            if value_index_values and value_index_values[0] > 0 and row != value_index_values[0] - 1:
                continue

            palette_data.row = row

            has_column = isinstance(sel_value, list)

            col_sel_values = sel_value if has_column else [sel_value]

            for column, col_sel_value in enumerate(col_sel_values):
                if value_index_values and len(value_index_values) == PaletteRadioButtonGroup.TWO_DIM_LIST and \
                   value_index_values[1] > 0 and column != value_index_values[1] - 1:
                    continue

                PaletteRadioButtonGroup.__add_row_index(wpf_palette, self.radio_button_group_controls, column, palette_data)

                PaletteRadioButtonGroup.__create_group_controls_in_row(wpf_palette, build_ele, self.radio_button_group_controls,
                                                                       column, col_sel_value, has_column, palette_data)


    @staticmethod
    def __add_row_index(wpf_palette                : WpfPaletteBuilder,
                        radio_button_group_controls: list[tuple[ParameterProperty, ControlProperties]],
                        column                     : int,
                        palette_data               : PaletteData):
        """ index must be added as text control in case of using the entire row

        Args:
            wpf_palette:                 the palette to show.
            radio_button_group_controls: radio button group controls
            column:                      column index
            palette_data:                palette data
        """

        ctrl_props = radio_button_group_controls[0][1]

        if not ctrl_props.row_state_key:
            return

        index_ctrl_props = ControlProperties("", f"___{ctrl_props.value_name}",  "",  "",  ctrl_props.page,
                                                ctrl_props.expander_name,
                                                PaletteRadioButtonGroup.replace_row_col_keywords(ctrl_props.row_name,
                                                                                                 palette_data.row, column),
                                                "", "", "", "", row_state_key = ctrl_props.row_state_key)

        if len(ctrl_props.row_name) < PaletteRadioButtonGroup.ROW_NAME_WIDTH_LIMIT:
            index_ctrl_props.width = 10

        index_data = ParameterProperty()

        index_data.value      = PaletteRadioButtonGroup.replace_row_col_keywords(ctrl_props.row_name, palette_data.row, column)
        index_data.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.TEXT)

        PaletteControlByValueTypeCreator.excecute(wpf_palette, index_data, index_ctrl_props, index_data.value_type,
                                                  palette_data)

    @staticmethod
    def __create_group_controls_in_row(wpf_palette                : WpfPaletteBuilder,
                                       build_ele                  : BuildingElement,
                                       radio_button_group_controls: list[tuple[ParameterProperty, ControlProperties]],
                                       column                     : int,
                                       col_sel_value              : int,
                                       has_column                 : bool,
                                       palette_data               : PaletteData):
        """ create the controls for one row

        Args:
            wpf_palette:                 the palette to show.
            build_ele:                   building element with the parameter properties
            radio_button_group_controls: _description_
            column:                      column index
            col_sel_value:               selected value of the column
            has_column:                  has column state
            palette_data:                palette data
        """

        row = palette_data.row

        for prop, ctrl in radio_button_group_controls:
            radio_ctrl = ctrl.deep_copy()
            radio_prop = prop.deep_copy()

            radio_prop.group_name     = f"{prop.group_name}[{row}]" + (f"[{column}]" if has_column else "")
            radio_prop.selected_value = col_sel_value

            radio_ctrl.group_text    = PaletteRadioButtonGroup.replace_row_col_keywords(ctrl.group_text, row, column)
            radio_ctrl.row_name      = PaletteRadioButtonGroup.replace_row_col_keywords(ctrl.row_name, row, column)
            radio_ctrl.row_state_key = ctrl.row_state_key

            PaletteControlCreator.create_control(wpf_palette, build_ele, radio_prop, radio_ctrl, palette_data)


    @staticmethod
    def replace_row_col_keywords(text: str,
                                 row : int,
                                 col : int) -> str:
        """ replace the row and column keyword by the row and column

        Args:
            text: text
            row:  row index
            col:  column index

        Returns:
            adapted text
        """

        return text.replace(GeneralConstants.LIST_ROW_KEYWORD, str(row)).replace(GeneralConstants.LIST_COL_KEYWORD, str(col))

```

</details>