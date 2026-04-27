---
title: "PictureComboBoxImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\PictureComboBoxImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PictureComboBoxImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\PictureComboBoxImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the PictureComboBoxImpl value type

## Abhängigkeiten

- `BaseEnumListImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypes.ValueTypeUtils.ValueListValidator`
- `__future__`
- `typing`

## Klassen

### `PictureComboBoxImpl`

implementation of the PictureComboBoxImpl value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a picture combo box to palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service  Raises:     ValueError: if the value_list, value_list_2 and value_text_list contain different number of entries |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PictureComboBoxImpl value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from StringEvaluate import StringEvaluate
from ValueTypes.ValueTypeUtils.ValueListValidator import ValueListValidator

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .BaseEnumListImpl import BaseEnumListImpl

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty

    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PictureComboBoxImpl(BaseEnumListImpl):
    """ implementation of the PictureComboBoxImpl value types
    """


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add a picture combo box to palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service

        Raises:
            ValueError: if the value_list, value_list_2 and value_text_list contain different number of entries
        """

        value_list = ctrl_props.value_list if prop.enum_dict else \
                     StringEvaluate.eval_constants(ctrl_props.value_list, prop_pal_ctrl_service.param_dict, int)

        try:
            ValueListValidator.check_length(ctrl_props.value_list_2, value_list, ctrl_props.value_text_list)

        except ValueError as err:
            raise ValueError(f"Invalid definition of the parameter {prop.name}.\n{err}") from err

        wpf_palette.AddPictureComboBox(ctrl_props.text, prop.name, prop.value, prop_pal_ctrl_service.picture_path,
                                       ctrl_props.value_list_2, value_list, ctrl_props.value_text_list,
                                       prop_pal_ctrl_service.page_index,
                                       ctrl_props.expander_name + ctrl_props.expander_state_key,
                                       ctrl_props.row_name + ctrl_props.row_state_key,
                                       prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                       ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

```

</details>