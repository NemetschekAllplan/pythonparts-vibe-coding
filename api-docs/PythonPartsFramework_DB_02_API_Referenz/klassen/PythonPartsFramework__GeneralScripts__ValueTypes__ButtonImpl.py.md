---
title: "ButtonImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ButtonImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ButtonImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ButtonImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Button value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `ButtonImpl`

implementation of the Button value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a button to palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Button value type
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from StringEvaluate import StringEvaluate

from .BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ButtonImpl(BaseStrImpl):
    """ implementation of the Button value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add a button to palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        event_id = StringEvaluate.eval_constants(ctrl_props.event_id, prop_pal_ctrl_service.param_dict)

        wpf_palette.AddButton(ctrl_props.text, prop.name, int(event_id), prop_pal_ctrl_service.page_index,
                              ctrl_props.expander_name + ctrl_props.expander_state_key,
                              ctrl_props.row_name + ctrl_props.row_state_key,
                              prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                              ctrl_props.height, ctrl_props.width,
                              ctrl_props.font_style, ctrl_props.font_face_code)

```

</details>