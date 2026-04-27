---
title: "PictureResourceButtonListImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\PictureResourceButtonListImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PictureResourceButtonListImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\PictureResourceButtonListImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the PictureResourceButtonList value type

## Abhängigkeiten

- `BaseEnumListImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `PictureResourceButtonListImpl`

implementation of the PictureResourceButtonList value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a picture resource button list to palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `get_default_control_width` | `-` | `int` | get the default control width  Returns:     default control width |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PictureResourceButtonList value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .BaseEnumListImpl import BaseEnumListImpl

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PictureResourceButtonListImpl(BaseEnumListImpl):
    """ implementation of the PictureResourceButtonList value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add a picture resource button list to palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        value_list = ctrl_props.value_list if prop.enum_dict else \
                     StringEvaluate.eval_constants(ctrl_props.value_list, prop_pal_ctrl_service.param_dict, int)

        value = -1 if prop.is_varied_value else int(prop.value)

        wpf_palette.AddPictureResourceButtonList(ctrl_props.text, prop.name, value,
                                                 ctrl_props.value_list_2, value_list, ctrl_props.value_text_list,
                                                 prop_pal_ctrl_service.page_index,
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