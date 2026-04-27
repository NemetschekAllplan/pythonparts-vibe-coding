---
title: "PictureImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\PictureImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PictureImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\PictureImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Picture value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `FileNameService`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `os`
- `pathlib`
- `typing`

## Klassen

### `PictureImpl`

implementation of the Picture value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[str] | str` | get the picture from a string  Args:     value_str: value string  Returns:     value from string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the string edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `get_default_control_width` | `-` | `int` | get the default control width  Returns:     default control width |
| `get_default_control_height` | `-` | `int` | get the default control height  Returns:     default control height |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Picture value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import os
import pathlib

from ControlProperties import ControlProperties
from FileNameService import FileNameService
from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

from .BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PictureImpl(BaseStrImpl):
    """ implementation of the Picture value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[str] | str):
        """ get the picture from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        res = BaseStringToValueConverter.to_str(value_str)

        if isinstance(res, list):
            return res

        return res.lstrip()


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the string edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        value = prop.value

        if StringEvaluate.is_text_from_script(value):
            value = StringEvaluate.eval_text(value, prop_pal_ctrl_service.param_dict)

        if value.isnumeric():
            picture_path = ""
            file_name    = value

        elif "AllplanSettings" in value:       # pylint: disable=magic-value-comparison
            picture_path = ""
            file_name    = str(int(eval(value, StringEvaluate.get_allplan_api_param_dict())))  # pylint: disable=eval-used

        elif (file_name := FileNameService.get_global_standard_path(value)):
            picture_path = os.path.dirname(file_name)
            file_name    = os.path.basename(file_name)

        elif not pathlib.Path(value).drive:
            picture_path = prop_pal_ctrl_service.picture_path
            file_name    = value

        else:
            picture_path = os.path.dirname(value)
            file_name    = os.path.basename(value)

        wpf_palette.AddPicture(ctrl_props.text.replace("\\n", "\n"), prop.name, file_name, picture_path,
                               prop.selected_value, prop_pal_ctrl_service.page_index,
                               ctrl_props.expander_name + ctrl_props.expander_state_key,
                               ctrl_props.row_name + ctrl_props.row_state_key,
                               ctrl_props.height, ctrl_props.width)

    @staticmethod
    def get_default_control_width() -> int:
        """ get the default control width

        Returns:
            default control width
        """

        return 0

    @staticmethod
    def get_default_control_height() -> int:
        """ get the default control height

        Returns:
            default control height
        """

        return 0

```

</details>