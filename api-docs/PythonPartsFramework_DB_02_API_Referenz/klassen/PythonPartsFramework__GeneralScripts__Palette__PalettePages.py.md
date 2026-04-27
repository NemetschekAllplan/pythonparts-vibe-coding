---
title: "PalettePages"
source: "PythonPartsFramework\GeneralScripts\Palette\PalettePages.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PalettePages

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PalettePages.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

" implementation for the palette pages

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `BuildingElementControlService`
- `BuildingElementParameterPropertyUtil`
- `BuildingElementStringTable`
- `ControlProperties`
- `PaletteControlCreator`
- `PaletteControlVisibility`
- `PaletteData`
- `PaletteListGroup`
- `PaletteRadioButtonGroup`
- `ParameterProperty`
- `StringEvaluate`
- `WpfPaletteBuilder`

## Klassen

### `PalettePages`

implementation for the palette pages
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele: BuildingElement, local_str_table: BuildingElementStringTable, is_visual_script: bool, picture_path: str` | `None` | initialize  Args:     build_ele:        building element with the parameter properties     local_str_table:  local string table     is_visual_script: is visual script state     picture_path:     picture path |
| `show_controls_for_pages` | `self, wpf_palette: WpfPaletteBuilder, page_building_ele: list[list[int]], page_index: int, page_index_dict: dict[str, int], build_ele_index: int, build_ele: BuildingElement, page_control_props: list[BuildingElementControlProperties]` | `int` | function description  Args:     wpf_palette:        the palette to show.     page_building_ele:  page building element indexes     page_index:         page index of the controls     page_index_dict:    page index dict     build_ele_index:    building element index     build_ele:          building element with the parameter properties     page_control_props: control properties for the pages  Returns:     next page index |
| `__is_new_page` | `page_index_dict: dict[str, int], page_index: int, page_data: BuildingElement.PageData` | `tuple[int, bool]` | check for new page  Args:     page_index_dict: page index dict     page_index:      page index of the controls     page_data:       page data  Returns:     page index, new page state |
| `__show_page_controls` | `self, build_ele: BuildingElement, control_props: BuildingElementControlProperties, wpf_palette: WpfPaletteBuilder` | `None` | show the controls for a page  Args:     build_ele:     building element with the parameter properties     control_props: control properties     wpf_palette:   WPF palette |
| `__get_visible_condition` | `ctrl_prop: ControlProperties` | `str` | get the visible condition  Args:     ctrl_prop: control properties  Returns:     visible condition |
| `__is_hidden_control` | `self, prop: ParameterProperty, ctrl_prop: ControlProperties, visible_condition: str` | `bool` | test for a hidden control  Args:     prop:              parameter property     ctrl_prop:         control properties     visible_condition: visible condition  Returns:     hidden control state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""" implementation for the palette pages
"""

import BuildingElementParameterPropertyUtil

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementControlService import BuildingElementControlService
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate

from .PaletteControlCreator import PaletteControlCreator
from .PaletteControlVisibility import PaletteControlVisibility
from .PaletteData import PaletteData
from .PaletteListGroup import PaletteListGroup
from .PaletteRadioButtonGroup import PaletteRadioButtonGroup
from .WpfPaletteBuilder import WpfPaletteBuilder

class PalettePages(PaletteData):
    """ implementation for the palette pages
    """

    def __init__(self,
                 build_ele       : BuildingElement,
                 local_str_table : BuildingElementStringTable,
                 is_visual_script: bool,
                 picture_path    : str):
        """ initialize

        Args:
            build_ele:        building element with the parameter properties
            local_str_table:  local string table
            is_visual_script: is visual script state
            picture_path:     picture path
        """

        self.param_dict = StringEvaluate.get_string_eval_param_dict(build_ele, local_str_table) | \
                          StringEvaluate.get_allplan_geometry_dict()

        _, global_str_table = build_ele.get_string_tables()

        self.palette_data = PaletteData("", self.param_dict, -1, picture_path, global_str_table, build_ele, -1,
                                        is_visual_script)

    def show_controls_for_pages(self,
                                wpf_palette       : WpfPaletteBuilder,
                                page_building_ele : list[list[int]],
                                page_index        : int,
                                page_index_dict   : dict[str, int],
                                build_ele_index   : int,
                                build_ele         : BuildingElement,
                                page_control_props: list[BuildingElementControlProperties]) -> int:
        """ function description

        Args:
            wpf_palette:        the palette to show.
            page_building_ele:  page building element indexes
            page_index:         page index of the controls
            page_index_dict:    page index dict
            build_ele_index:    building element index
            build_ele:          building element with the parameter properties
            page_control_props: control properties for the pages

        Returns:
            next page index
        """

        build_ele_index_list = list[int]([build_ele_index])

        for control_props, page_data in zip(page_control_props, build_ele.get_pages()):
            if not control_props:
                continue


            #--------- check for a hidden page, reduce the start index to get the correct next page index

            if page_data.visible_condition and not StringEvaluate.eval_condition(page_data.visible_condition, self.param_dict):
                continue


            #--------- check for a parent page use

            page_index, is_new_page = self.__is_new_page(page_index_dict, page_index, page_data)


            #------------ show the page controls

            if is_new_page:
                wpf_palette.AddPage(page_data.name, page_data.text)

                page_building_ele.append(build_ele_index_list)
            else:
                page_building_ele[page_index].append(build_ele_index)

            BuildingElementControlService.add_check_state_functions(self.param_dict, control_props)

            self.palette_data.page_enable_cond = page_data.enable_condition

            self.palette_data.page_index = page_index

            self.__show_page_controls(build_ele, control_props, wpf_palette)

            if is_new_page:
                page_index_dict[page_data.name] = page_index

                page_index += 1

        return page_index


    @staticmethod
    def __is_new_page(page_index_dict: dict[str, int],
                      page_index     : int,
                      page_data      : BuildingElement.PageData) -> tuple[int, bool]:
        """ check for new page

        Args:
            page_index_dict: page index dict
            page_index:      page index of the controls
            page_data:       page data

        Returns:
            page index, new page state
        """

        is_new_page = True

        if page_data.name.startswith("Parent:"):
            _, _, name = page_data.name.partition(":")

            if (index := page_index_dict.get(name, None)) is not None:
                page_index  = index
                is_new_page = False

        return page_index, is_new_page


    def __show_page_controls(self,
                             build_ele    : BuildingElement,
                             control_props: BuildingElementControlProperties,
                             wpf_palette  : WpfPaletteBuilder):
        """ show the controls for a page

        Args:
            build_ele:     building element with the parameter properties
            control_props: control properties
            wpf_palette:   WPF palette
        """

        radio_group = PaletteRadioButtonGroup()
        list_group  = PaletteListGroup()


        #----------------- show the page controls

        for ctrl_prop in control_props:
            visible_condition = self.__get_visible_condition(ctrl_prop)


            #---------------- check visible expander and row first

            if not PaletteControlVisibility.is_visible_expander_or_row(self.palette_data, ctrl_prop, visible_condition):
                continue


            #---------------- get and check the parameter property

            value_name = BuildingElementParameterPropertyUtil.get_property_value_name(ctrl_prop.value_name)

            if (prop := build_ele.get_property(value_name)) is None:
                print(f"Parameter property with name {value_name} not found!")
                continue


            #---------------- create the radio button group control

            if radio_group.check_radio_button_group(wpf_palette, build_ele,
                                                    prop, ctrl_prop, visible_condition, self.palette_data):
                continue


            #---------------- visibility

            if self.__is_hidden_control(prop, ctrl_prop, visible_condition):
                continue


            #------------- check the groups

            if list_group.check_list_group_creation(wpf_palette, prop, ctrl_prop, self.palette_data):
                continue

            if radio_group.check_radio_button(prop, ctrl_prop):
                continue


            #---------------- create the control

            PaletteControlCreator.create_full_row_text(wpf_palette, prop, ctrl_prop, self.palette_data)

            PaletteControlCreator.create_control(wpf_palette, build_ele, prop, ctrl_prop, self.palette_data)

        list_group.create_list_group_control(wpf_palette,self.palette_data)

        radio_group.create_radio_button_group_control(wpf_palette, build_ele, self.palette_data)


    @staticmethod
    def __get_visible_condition(ctrl_prop: ControlProperties) -> str:
        """ get the visible condition

        Args:
            ctrl_prop: control properties

        Returns:
            visible condition
        """

        visible_condition = ctrl_prop.visible_condition

        if (ip_sep := visible_condition.find("|")) != -1:
            visible_condition = visible_condition[:ip_sep]

        return visible_condition


    def __is_hidden_control(self,
                            prop             : ParameterProperty,
                            ctrl_prop        : ControlProperties,
                            visible_condition: str) -> bool:
        """ test for a hidden control

        Args:
            prop:              parameter property
            ctrl_prop:         control properties
            visible_condition: visible condition

        Returns:
            hidden control state
        """

        if visible_condition and prop.value_type.is_tuple_type():
            PaletteControlVisibility.set_tuple_visibilty(ctrl_prop, visible_condition, self.param_dict)

            return False

        if not PaletteControlVisibility.is_visible_control(self.palette_data, ctrl_prop, visible_condition):
            return True

        return False

```

</details>