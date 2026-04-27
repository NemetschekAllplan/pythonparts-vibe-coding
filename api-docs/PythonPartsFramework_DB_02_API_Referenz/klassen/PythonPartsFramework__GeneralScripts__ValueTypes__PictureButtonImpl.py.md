---
title: "PictureButtonImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\PictureButtonImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PictureButtonImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\PictureButtonImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the PictureButton value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `pathlib`
- `typing`

## Klassen

### `PictureButtonImpl`

implementation of the PictureButton value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a picture button list to palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `get_default_control_width` | `-` | `int` | get the default control width  Returns:     default control width |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PictureButton value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pathlib

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from StringEvaluate import StringEvaluate

from .BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PictureButtonImpl(BaseStrImpl):
    """ implementation of the PictureButton value type
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

        picture_path = prop.value if pathlib.Path(prop.value).drive else f"{prop_pal_ctrl_service.picture_path}\\{prop.value}"

        event_id = StringEvaluate.eval_constants(ctrl_props.event_id, prop_pal_ctrl_service.param_dict)

        wpf_palette.AddPictureButton(ctrl_props.text, prop.name, picture_path,
                                     int(event_id), prop_pal_ctrl_service.page_index,
                                     ctrl_props.expander_name + ctrl_props.expander_state_key,
                                     ctrl_props.row_name + ctrl_props.row_state_key,
                                     prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)


    @staticmethod
    def get_default_control_width() -> int:
        """ get the default control width

        Returns:
            default control width
        """

        return 22

```

</details>