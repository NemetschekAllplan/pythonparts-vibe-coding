---
title: "LengthComboBoxImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\LengthComboBoxImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# LengthComboBoxImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\LengthComboBoxImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the LengthComboBox value type

## Abhängigkeiten

- `BaseFloatImpl`
- `ComboBoxImpl`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Palette`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `LengthComboBoxImpl`

implementation of the LengthComboBox value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the length edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `value_to_unit_string` | `value: float` | `str` | convert the value to the current unit value  Args:     value: value  Returns:     unit value as string |
| `string_to_unit_value` | `cls, value_str: str` | `float` | convert the string to the unit value  Args:     value_str: value string  Returns:     unit value as string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the LengthComboBox value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Palette as AllplanPalette

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .BaseFloatImpl import BaseFloatImpl
from .ComboBoxImpl import ComboBoxImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class LengthComboBoxImpl(BaseFloatImpl, metaclass = ComboBoxImpl):
    """ implementation of the LengthComboBox value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the length edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if prop.value_list_util and not ctrl_props.row_name:
            ctrl_props.row_name = ctrl_props.text

        prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.LENGTH)

        if prop.value_list_util:
            ComboBoxImpl.add_del_button(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def value_to_unit_string(value: float) -> str:
        """ convert the value to the current unit value

        Args:
            value: value

        Returns:
            unit value as string
        """

        return AllplanSettings.UnitService.ToLengthUnitString(value)


    @classmethod
    def string_to_unit_value(cls,
                             value_str: str) -> float:
        """ convert the string to the unit value

        Args:
            value_str: value string

        Returns:
            unit value as string
        """

        error, value = AllplanSettings.UnitService.ConvertToMM(value_str)

        return 0 if error else value

```

</details>