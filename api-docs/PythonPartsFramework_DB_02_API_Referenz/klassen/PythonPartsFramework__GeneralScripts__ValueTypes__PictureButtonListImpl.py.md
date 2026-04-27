---
title: "PictureButtonListImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\PictureButtonListImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PictureButtonListImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\PictureButtonListImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the PictureButtonList value type

## Abhängigkeiten

- `BaseEnumListImpl`
- `ControlProperties`
- `FileNameService`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `TraceService`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `os`
- `typing`

## Klassen

### `PictureButtonListImpl`

implementation of the PictureButtonList value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a picture button list to palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `get_default_control_width` | `-` | `int` | get the default control width  Returns:     default control width |
| `validate_picture_list` | `dir_path: str, picture_list: str, property_name: str` | `None` | validate if the paths to files from picture_list are existing,     if not the information is written to trace  Args:     dir_path: path to the directory for pictures     picture_list: list of picture file paths relative to dir_path     property_name: name of the property |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PictureButtonList value type
"""

from __future__ import annotations

import os

from typing import TYPE_CHECKING

from FileNameService import FileNameService
from StringEvaluate import StringEvaluate
from TraceService import TraceService

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from .BaseEnumListImpl import BaseEnumListImpl

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PictureButtonListImpl(BaseEnumListImpl):
    """ implementation of the PictureButtonList value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add a picture button list to palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        value_list = ctrl_props.value_list if prop.enum_dict else \
                     StringEvaluate.eval_constants(ctrl_props.value_list, prop_pal_ctrl_service.param_dict, int)


        #----------------- get picture path and file names

        if (file_name := FileNameService.get_global_standard_path(ctrl_props.value_list_2.split(GeneralConstants.TEXT_SEPARATOR, 1)[0])):
            picture_path = os.path.dirname(file_name)

            file_names = GeneralConstants.TEXT_SEPARATOR.join(item.rsplit("\\", 1)[1] \
                            for item in ctrl_props.value_list_2.split(GeneralConstants.TEXT_SEPARATOR))
        else:
            picture_path = prop_pal_ctrl_service.picture_path
            file_names   = ctrl_props.value_list_2


        #----------------- use as row to get the correct sizes (sizes are internally row dependent)

        if not (row_name := ctrl_props.row_name + ctrl_props.row_state_key):
            row_name = ctrl_props.text

        PictureButtonListImpl.validate_picture_list (picture_path, file_names, prop.name)


        #----------------- add picture button list

        wpf_palette.AddPictureButtonList(ctrl_props.text, prop.name, prop.value, picture_path,
                                         file_names, value_list, ctrl_props.value_text_list,
                                         prop_pal_ctrl_service.page_index,
                                         ctrl_props.expander_name + ctrl_props.expander_state_key, row_name,
                                         prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                         ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)


    @staticmethod
    def get_default_control_width() -> int:
        """ get the default control width

        Returns:
            default control width
        """

        return 22

    @staticmethod
    def validate_picture_list(dir_path     : str,
                              picture_list : str,
                              property_name: str):
        """ validate if the paths to files from picture_list are existing,
            if not the information is written to trace

        Args:
            dir_path: path to the directory for pictures
            picture_list: list of picture file paths relative to dir_path
            property_name: name of the property
        """

        relative_paths = picture_list.split("|")

        nonexisting_files = ""

        for path in relative_paths:
            full_path = os.path.join(dir_path, path)

            if not os.path.isfile(full_path):
                nonexisting_files = f"{nonexisting_files}{path}, "

        if nonexisting_files:
            TraceService.trace_1(f"\nFollowing files are not found: {nonexisting_files}defined in PictureButtonList '{property_name}'\n")

```

</details>