---
title: "IntegerComboBoxImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\IntegerComboBoxImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# IntegerComboBoxImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\IntegerComboBoxImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the IntegerComboBox value type

## Abhängigkeiten

- `BaseIntImpl`
- `ComboBoxImpl`
- `ControlProperties`
- `NemAll_Python_Palette`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `IntegerComboBoxImpl`

implementation of the IntegerComboBox value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the integer edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the IntegerComboBox value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_Palette as AllplanPalette

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .BaseIntImpl import BaseIntImpl
from .ComboBoxImpl import ComboBoxImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class IntegerComboBoxImpl(BaseIntImpl, metaclass = ComboBoxImpl):
    """ implementation of the IntegerComboBox value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the integer edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if prop.value_list_util and not ctrl_props.row_name:
            ctrl_props.row_name = ctrl_props.text

        prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.INTEGER)

        if prop.value_list_util:
            ComboBoxImpl.add_del_button(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)

```

</details>