---
title: "SeparatorImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\SeparatorImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# SeparatorImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\SeparatorImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Separator value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `SeparatorImpl`

implementation of the Separator value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, _prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the string edit control  Args:     wpf_palette:           WPf palette     _prop:                 parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Separator value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class SeparatorImpl(BaseStrImpl):
    """ implementation of the Separator value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       _prop                : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the string edit control

        Args:
            wpf_palette:           WPf palette
            _prop:                 parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        wpf_palette.AddSeparator(prop_pal_ctrl_service.page_index, ctrl_props.expander_name + ctrl_props.expander_state_key)

```

</details>