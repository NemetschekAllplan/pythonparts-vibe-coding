---
title: "FontImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\FontImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# FontImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\FontImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Font combobox value type

## Abhängigkeiten

- `BaseIntImpl`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `FontImpl`

implementation of the Font combobox value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the string edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Font combobox value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_AllplanSettings as AllplanSettings

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..BaseIntImpl import BaseIntImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class FontImpl(BaseIntImpl):
    """ implementation of the Font combobox value type
    """

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

        fonts    = AllplanSettings.FontProvider.Instance().GetNemFonts()[1]   + \
                   AllplanSettings.FontProvider.Instance().GetSystemFonts()[1]
        font_ids = AllplanSettings.FontProvider.Instance().GetNemFontIDs()[1] +  \
                   AllplanSettings.FontProvider.Instance().GetSystemFontIDs()[1]

        value_list    = "|".join([str(item) for item in font_ids])
        pictture_list = f'{"|".join(["8554"] * len(AllplanSettings.FontProvider.Instance().GetNemFontIDs()[1]))}|' \
                        f'{"|".join(["8556"] * len(AllplanSettings.FontProvider.Instance().GetSystemFontIDs()[1]))}'

        wpf_palette.AddPictureResourceComboBox(ctrl_props.text, prop.name, prop.value,
                                               pictture_list, value_list, "|".join(fonts),
                                               prop_pal_ctrl_service.page_index,
                                               ctrl_props.expander_name + ctrl_props.expander_state_key,
                                               ctrl_props.row_name + ctrl_props.row_state_key,
                                               prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                               ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

```

</details>