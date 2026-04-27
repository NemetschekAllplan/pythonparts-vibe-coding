---
title: "DrawingFileImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\DrawingFileImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# DrawingFileImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\DrawingFileImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the drawing file value type

## Abhängigkeiten

- `BaseIntImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `DrawingFileImpl`

implementation of the drawing file value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `is_add_to_palette_for_single_list_item` | `-` | `bool` | check, whether the add_to_palette function must be called for a single list item                  Returns: add control for single list item state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the drawing file value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ControlProperties import ControlProperties
from Palette.WpfPaletteBuilder import WpfPaletteBuilder
from Utilities.GeneralConstants import GeneralConstants

from .BaseIntImpl import BaseIntImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class DrawingFileImpl(BaseIntImpl):
    """ implementation of the drawing file value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the control to the palette

            Args:
                wpf_palette:           WPf palette
                prop:                  parameter property
                ctrl_props:            control properties
                prop_pal_ctrl_service: property palette control service
        """
        row_name = ctrl_props.row_name or ctrl_props.text

        value = str()

        if prop.value == 0:
            value = ""
        else:
            value = ",".join(map(str,prop.value))

        wpf_palette.AddButton(value, prop.name + GeneralConstants.DIALOG_BUTTON_KEY + "DrawingFileDialog",
                              0, prop_pal_ctrl_service.page_index,
                              ctrl_props.expander_name, row_name,
                              prop_pal_ctrl_service.is_sub_control_enabled(ctrl_props, ""),
                              ctrl_props.height, ctrl_props.width,
                              ctrl_props.font_style, ctrl_props.font_face_code)

    @staticmethod
    def is_add_to_palette_for_single_list_item() -> bool:
        """ check, whether the add_to_palette function must be called for a single list item
                        
        Returns:
        add control for single list item state
        """

        return False

```

</details>