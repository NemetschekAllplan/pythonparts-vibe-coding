---
title: "MaterialButtonImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\MaterialButtonImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# MaterialButtonImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\MaterialButtonImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the MaterialButton value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `MaterialButtonImpl`

implementation of the MaterialButton value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a material button to palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the MaterialButton value type
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class MaterialButtonImpl(BaseStrImpl):
    """ implementation of the MaterialButton value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add a material button to palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        wpf_palette.AddMaterialButton(ctrl_props.text, prop.name, prop.value, prop.selected_value,
                                      prop_pal_ctrl_service.page_index, ctrl_props.expander_name + ctrl_props.expander_state_key,
                                      ctrl_props.row_name + ctrl_props.row_state_key,
                                      prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                      ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

```

</details>