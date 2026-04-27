---
title: "BuildingElementPaletteService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementPaletteService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementPaletteService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementPaletteService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the building element palette service

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementComposite`
- `BuildingElementControlProperties`
- `BuildingElementPalette`
- `BuildingElementServices.BuildingElementIndexUtil`
- `BuildingElementServices.BuildingElementModification`
- `DocumentManager`
- `NemAll_Python_Palette`
- `Palette.WpfPaletteBuilder`
- `inspect`
- `typing`

## Klassen

### `BuildingElementPaletteService`

Definition of class BuildingElementPaletteService
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele_list: list[BuildingElement], build_ele_composite: BuildingElementComposite, build_ele_script: Any, build_ele_ctrl_props_list: list[BuildingElementControlProperties], picture_path: str` | `None` | Initialize the data  Args:     build_ele_list:            list with the building elements     build_ele_composite:       building element composite with the building element constraints     build_ele_script:          Building element script     build_ele_ctrl_props_list: list with the building element control properties     picture_path:              Picture path |
| `switch_pythonpart` | `self, build_ele_list: list[BuildingElement], build_ele_composite: BuildingElementComposite, build_ele_script: Any, build_ele_ctrl_props_list: list[BuildingElementControlProperties], picture_path: str` | `None` | Switch the PythonPart  Args:     build_ele_list:            list with the building elements     build_ele_composite:       building element composite with the building element constraints     build_ele_script:          Building element script     build_ele_ctrl_props_list: list with the building element control properties     picture_path:              Picture path |
| `set_palette_lock` | `palette_lock: bool` | `None` | set the palette lock state  Args:     palette_lock: palette lock state |
| `set_update_lock` | `update_lock: bool` | `None` | set the palette lock state  Args:     update_lock: palette lock state |
| `show_palette` | `self, part_name: str, show_close_button: bool=True, open_palette: bool=True, active_page_text: str='', is_visual_script: bool=False` | `None` | Show the palette  Args:     part_name:         Name of the PythonPart     show_close_button: Show close button in palette     open_palette:      open the palette     active_page_text:  active page text     is_visual_script:  execution for VisualScripting |
| `get_control_text` | `self` | `str` | Get the control data as text  Returns:     Controls data as text |
| `show_page_for_element` | `self, act_page: int, build_ele_index_list: list[int]` | `None` | Show the page for the element_index  Args:     act_page:             active page index     build_ele_index_list: index list with the connected building elements (geometry, reinforcement, ...) of a sub element |
| `on_control_event` | `self, event_id: int` | `bool` | On control event  Args:     event_id: event id of control.  Returns:     event was processed state |
| `modify_element_property` | `self, page: int, name: str, value: Any` | `bool` | Modify property of element  Args:     page:  page index of the modified property     name:  the name of the property.     value: new value for property.  Returns:     palette refresh state |
| `close_palette` | `self` | `str` | Close the palette  Returns:     text of the active page |
| `update_palette` | `self, page_index: int, update_dialog_data: bool, _show_palette_close_btn=True` | `None` | Update the palette  Args:     page_index:              page index to show, -1 = use current     update_dialog_data:      update the dialog data: True/False     _show_palette_close_btn: show close button in palette: True/False |
| `refresh_palette` | `self, build_ele_list: list[BuildingElement], build_ele_ctrl_props_list: list[BuildingElementControlProperties]` | `None` | refresh the palette  Args:     build_ele_list:     Building element list     build_ele_ctrl_props_list: Control properties list |
| `reset_palette` | `self, clear_only_pages: bool` | `None` | Reset the palette for a full refresh  Args:     clear_only_pages: Reset only pages |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the building element palette service
"""

from typing import Any

import inspect

import NemAll_Python_Palette as AllplanPalette

from BuildingElement import BuildingElement
from BuildingElementComposite import BuildingElementComposite
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementPalette import BuildingElementPalette
from DocumentManager import DocumentManager

from BuildingElementServices.BuildingElementIndexUtil import BuildingElementIndexUtil
from BuildingElementServices.BuildingElementModification import BuildingElementModification

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

class BuildingElementPaletteService:
    """ Definition of class BuildingElementPaletteService
    """

    __palette_lock = False
    __update_lock  = False

    def __init__(self,
                 build_ele_list           : list[BuildingElement],
                 build_ele_composite      : BuildingElementComposite,
                 build_ele_script         : Any,
                 build_ele_ctrl_props_list: list[BuildingElementControlProperties],
                 picture_path             : str):
        """ Initialize the data

        Args:
            build_ele_list:            list with the building elements
            build_ele_composite:       building element composite with the building element constraints
            build_ele_script:          Building element script
            build_ele_ctrl_props_list: list with the building element control properties
            picture_path:              Picture path
        """

        self.build_ele_pal   : (BuildingElementPalette | None)          = None
        self.palette         : (AllplanPalette.PythonWpfPalette | None) = None
        self.palette_builder : (WpfPaletteBuilder | None)               = None

        self.build_ele_list            = build_ele_list
        self.build_ele_composite       = build_ele_composite
        self.build_ele_script          = build_ele_script
        self.build_ele_ctrl_props_list = build_ele_ctrl_props_list
        self.picture_path              = picture_path

        self.page_building_ele: list[list[int]] = []

        self.build_ele_modify = BuildingElementModification(build_ele_list, build_ele_composite,
                                                            build_ele_script, build_ele_ctrl_props_list)


    def switch_pythonpart(self,
                          build_ele_list           : list[BuildingElement],
                          build_ele_composite      : BuildingElementComposite,
                          build_ele_script         : Any,
                          build_ele_ctrl_props_list: list[BuildingElementControlProperties],
                          picture_path             : str):
        """ Switch the PythonPart

        Args:
            build_ele_list:            list with the building elements
            build_ele_composite:       building element composite with the building element constraints
            build_ele_script:          Building element script
            build_ele_ctrl_props_list: list with the building element control properties
            picture_path:              Picture path
        """

        self.build_ele_list            = build_ele_list
        self.build_ele_composite       = build_ele_composite
        self.build_ele_script          = build_ele_script
        self.build_ele_ctrl_props_list = build_ele_ctrl_props_list
        self.picture_path              = picture_path

        self.page_building_ele: list[list[int]] = []

        self.build_ele_modify = BuildingElementModification(build_ele_list, build_ele_composite,
                                                            build_ele_script, build_ele_ctrl_props_list)


    @staticmethod
    def set_palette_lock(palette_lock: bool):
        """ set the palette lock state

        Args:
            palette_lock: palette lock state
        """

        BuildingElementPaletteService.__palette_lock = palette_lock


    @staticmethod
    def set_update_lock(update_lock: bool):
        """ set the palette lock state

        Args:
            update_lock: palette lock state
        """

        BuildingElementPaletteService.__update_lock = update_lock


    def show_palette(self,
                     part_name        : str,
                     show_close_button: bool = True,
                     open_palette     : bool = True,
                     active_page_text : str  = "",
                     is_visual_script : bool = False):
        """ Show the palette

        Args:
            part_name:         Name of the PythonPart
            show_close_button: Show close button in palette
            open_palette:      open the palette
            active_page_text:  active page text
            is_visual_script:  execution for VisualScripting
        """

        self.build_ele_pal = BuildingElementPalette(is_visual_script)

        if not self.__palette_lock:
            self.palette = AllplanPalette.PythonWpfPalette()

            self.palette_builder = WpfPaletteBuilder(self.palette.GetPythonWpfPaletteBuilder())

            self.page_building_ele = self.build_ele_pal.show(self.build_ele_list,
                                                             self.build_ele_ctrl_props_list,
                                                             self.palette_builder,
                                                             self.picture_path, self.build_ele_composite)

        if open_palette and self.palette is not None:
            self.palette.Open(self.build_ele_list[0].title, part_name, self.build_ele_list[0].data_column_width,
                              show_close_button, self.build_ele_list[0].show_favorite_buttons,
                              DocumentManager.get_instance().document, active_page_text)


    def get_control_text(self) -> str:
        """ Get the control data as text

        Returns:
            Controls data as text
        """

        control_text = str(self.palette)

        if self.palette:
            self.reset_palette(False)

        return control_text


    def show_page_for_element(self,
                              act_page            : int,
                              build_ele_index_list: list [int]):
        """ Show the page for the element_index

        Args:
            act_page:             active page index
            build_ele_index_list: index list with the connected building elements (geometry, reinforcement, ...) of a sub element
        """

        set_new_page    = True
        page_type_index = -1

        for build_ele_index in build_ele_index_list:
            script_name = self.build_ele_list[build_ele_index].script_name

            index = 0

            page_type_dict = {}

            add_to_page_type_dict = True


            #----------------- get the index of the last "script_name" building element
            #                  don't count hidden elements to get the real index

            for i in range(0, build_ele_index + 1):
                if i == 0  or  self.build_ele_composite.is_element_visible(i - 1, self.build_ele_list):
                    ele_script_name = self.build_ele_list[i].script_name


                    #----------------- count same names before the first "script_name"

                    if add_to_page_type_dict  and  self.build_ele_ctrl_props_list[i]:
                        page_type_dict[ele_script_name] = 1


                    #----------------- first "script_name" closes the name counting

                    if script_name == ele_script_name:
                        add_to_page_type_dict  = False
                        index                 += 1

            BuildingElementIndexUtil.set_building_element_index(index, script_name, self.build_ele_list, self.build_ele_composite)


            #----------------- get the index of the page type

            if page_type_index == -1:
                page_type_index = len(page_type_dict) - 1

            if len(page_type_dict) - 1 == act_page:
                set_new_page = False

        if set_new_page:
            self.update_palette(page_type_index, True)
        else:
            self.update_palette(-1, True)

        BuildingElementIndexUtil.check_building_element_index(self.build_ele_list, self.build_ele_composite)


    def on_control_event(self,
                         event_id: int) -> bool:
        """ On control event

        Args:
            event_id: event id of control.

        Returns:
            event was processed state
        """

        if not self.build_ele_script or self.palette is None or self.build_ele_pal is None:
            return False


        #----------------- get the on_control_event function

        if (on_control_event_fct := getattr(self.build_ele_script, "on_control_event", None)) is None:
            print("BuildingElementInput.py (on_control_event not overloaded in script ",
                  self.build_ele_list[0].script_name, ")")

            return False


        #----------------- execute the control event

        arg_spec = inspect.getfullargspec(on_control_event_fct)

        func_param_count = len(arg_spec.args)

        doc = DocumentManager.get_instance().document

        if len(self.build_ele_list) == 1:
            if func_param_count == 2:
                refresh_palette = on_control_event_fct(self.build_ele_list[0], event_id)
            else:
                refresh_palette = on_control_event_fct(self.build_ele_list[0], event_id, doc)

        elif func_param_count == 3:
            refresh_palette = on_control_event_fct(self.build_ele_list, self.build_ele_composite, event_id)

        else:
            refresh_palette = on_control_event_fct(self.build_ele_list, self.build_ele_composite, event_id, doc)


        #----------------- refresh the palette if necessary

        if refresh_palette:
            self.reset_palette(True)

            if self.palette_builder:
                self.page_building_ele = self.build_ele_pal.show(self.build_ele_list,
                                                                 self.build_ele_ctrl_props_list,
                                                                 self.palette_builder,
                                                                 self.picture_path, self.build_ele_composite)

        return True


    def modify_element_property(self,
                                page : int,
                                name : str,
                                value: Any) -> bool:
        """ Modify property of element

        Args:
            page:  page index of the modified property
            name:  the name of the property.
            value: new value for property.

        Returns:
            palette refresh state
        """

        return self.build_ele_modify.modify_element_property(page, name, value, self.page_building_ele,
                                                             self.palette_builder, None)


    def close_palette(self) -> str:
        """ Close the palette

        Returns:
            text of the active page
        """

        if not self.palette:
            return ""

        # the palette builder needs to be reset to clear all the event handlers and view models

        if self.palette_builder:
            self.palette_builder.Reset()
            self.palette_builder = None

        ret = self.palette.Close()

        self.palette = None

        return ret


    def update_palette(self,
                       page_index             : int,
                       update_dialog_data     : bool,
                       _show_palette_close_btn= True):
        """ Update the palette

        Args:
            page_index:              page index to show, -1 = use current
            update_dialog_data:      update the dialog data: True/False
            _show_palette_close_btn: show close button in palette: True/False
        """

        if self.palette is None or self.palette_builder is None or self.build_ele_pal is None:
            return

        self.reset_palette(True)

        self.page_building_ele = self.build_ele_pal.show(self.build_ele_list, self.build_ele_ctrl_props_list,
                                                         self.palette_builder,
                                                         self.picture_path, self.build_ele_composite)

        if update_dialog_data and not BuildingElementPaletteService.__update_lock:
            self.palette.UpdateDialogData(page_index)


    def refresh_palette(self,
                        build_ele_list           : list[BuildingElement],
                        build_ele_ctrl_props_list: list[BuildingElementControlProperties]):
        """ refresh the palette

        Args:
            build_ele_list:     Building element list
            build_ele_ctrl_props_list: Control properties list
        """

        self.build_ele_list            = build_ele_list
        self.build_ele_ctrl_props_list = build_ele_ctrl_props_list

        self.update_palette(0, True)

    def reset_palette(self,
                      clear_only_pages: bool):
        """Reset the palette for a full refresh

        Args:
            clear_only_pages: Reset only pages
        """

        if self.palette_builder:
            self.palette_builder.Reset()

        if self.palette:
            self.palette.Reset(clear_only_pages)

```

</details>