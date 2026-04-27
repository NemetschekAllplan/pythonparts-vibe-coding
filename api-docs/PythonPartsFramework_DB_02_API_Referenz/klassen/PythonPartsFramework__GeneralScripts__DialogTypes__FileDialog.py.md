---
title: "FileDialog"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\FileDialog.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# FileDialog

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\FileDialog.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the file dialog

## Abhängigkeiten

- `BuildingElementStringTable`
- `ControlProperties`
- `FileNameService`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Utility`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `PathConstants`
- `Utilities.GeneralConstants`
- `ValueDialogType`
- `ValueTypes.ParameterPropertyValueTypes`
- `_collections_abc`

## Klassen

### `FileDialog`

implementation of the file dialog
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_controls` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, page_index: int, global_str_table: BuildingElementStringTable, is_control_enabled: Callable[[ControlProperties], bool]` | `bool` | Add the controls  Args:     wpf_palette:        palette builder     prop:               parameter property     ctrl_props:         control properties     page_index:         page index     global_str_table:   global string table     is_control_enabled: function for getting the enabled state  Returns:     True |
| `get_default_directories` | `value_ctrl_prop: ControlProperties` | `AllplanUtil.DefaultDirectories` | get the default directories  Args:     value_ctrl_prop: value control property  Returns:     default directories |
| `expand_value_string` | `value: str | list[str]` | `str | list[str]` | expand the value string  Args:     value: value  Returns:     expanded value string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the file dialog
"""

from _collections_abc import Callable

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Utility as AllplanUtil

from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from FileNameService import FileNameService
from ParameterProperty import ParameterProperty
from PathConstants import PathConstants

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from Utilities.GeneralConstants import GeneralConstants

from .ValueDialogType import ValueDialogType

class FileDialog(ValueDialogType):
    """ implementation of the file dialog
    """

    @staticmethod
    def create_controls(wpf_palette       : WpfPaletteBuilder,
                        prop              : ParameterProperty,
                        ctrl_props        : ControlProperties,
                        page_index        : int,
                        global_str_table  : BuildingElementStringTable,
                        is_control_enabled: Callable[[ControlProperties], bool]) -> bool:
        """ Add the controls

        Args:
            wpf_palette:        palette builder
            prop:               parameter property
            ctrl_props:         control properties
            page_index:         page index
            global_str_table:   global string table
            is_control_enabled: function for getting the enabled state

        Returns:
            True
        """

        row_name = ctrl_props.row_name or ctrl_props.text

        if prop.value_type == ParameterPropertyValueTypes.PICTURE_BUTTON:
            wpf_palette.AddPictureButton(prop.value,
                                         prop.name + GeneralConstants.DIALOG_BUTTON_KEY, prop.value, 0, page_index,
                                         ctrl_props.expander_name, row_name,
                                         is_control_enabled(ctrl_props),
                                         ctrl_props.height, ctrl_props.width,
                                         ctrl_props.font_face_code)
        else:
            value = prop.value or global_str_table.get_string("e_FILE_DIALOG_DEFAULT", "...")

            wpf_palette.AddButton(value,
                                  prop.name + GeneralConstants.DIALOG_BUTTON_KEY, 0, page_index,
                                  ctrl_props.expander_name, row_name,
                                  is_control_enabled(ctrl_props),
                                  ctrl_props.height, ctrl_props.width,
                                  ctrl_props.font_style, ctrl_props.font_face_code)

        return True


    @staticmethod
    def get_default_directories(value_ctrl_prop: ControlProperties) -> AllplanUtil.DefaultDirectories:
        """ get the default directories

        Args:
            value_ctrl_prop: value control property

        Returns:
            default directories
        """

        default_dir_names = value_ctrl_prop.value_list_2.split("|")[1:]
        default_dir       = AllplanUtil.DefaultDirectories()

        if PathConstants.ETC_PATH in default_dir_names:
            default_dir.AddDirectory(AllplanSettings.AllplanPaths.GetEtcPath())

        if PathConstants.STD_PATH in default_dir_names:
            default_dir.AddDirectory(AllplanSettings.AllplanPaths.GetStdPath())

        if PathConstants.USR_PATH in default_dir_names:
            default_dir.AddDirectory(AllplanSettings.AllplanPaths.GetUsrPath())

        if PathConstants.PRJ_PATH in default_dir_names:
            default_dir.AddDirectory(AllplanSettings.AllplanPaths.GetCurPrjPath())

        return default_dir

    @staticmethod
    def expand_value_string(value: (str | list[str])) -> (str | list[str]):
        """ expand the value string

        Args:
            value: value

        Returns:
            expanded value string
        """

        if isinstance(value, list):
            return [FileNameService.get_global_standard_path(item) for item in value]

        if (expand_path := FileNameService.get_global_standard_path("" if value is None else value)):
            return expand_path

        return value

```

</details>