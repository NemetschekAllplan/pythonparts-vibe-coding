---
title: "RadioButtonImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\RadioButtonImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# RadioButtonImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\RadioButtonImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the RadioButton value type

## Abhängigkeiten

- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `RadioButtonImpl`

implementation of the RadioButton value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `to_string` | `value: int` | `str` | convert the radio button id to a string  Args:     value: new value  Returns:     radio button id as string |
| `get_value` | `value_str: str` | `Any` | get the radio button id from a string  Args:     value_str: value string  Returns:     value from string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the integer edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the RadioButton value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

from .ParameterPropertyValueType import ParameterPropertyValueType

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class RadioButtonImpl(ParameterPropertyValueType):
    """ implementation of the RadioButton value type
    """

    @staticmethod
    def to_string(value: int) -> str:
        """ convert the radio button id to a string

        Args:
            value: new value

        Returns:
            radio button id as string
        """

        return str(value)


    @staticmethod
    def get_value(value_str: str) -> Any:
        """ get the radio button id from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        return BaseStringToValueConverter.to_auto(value_str)


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

        prop_pal_ctrl_service.add_radio_button_control(wpf_palette, prop.group_name, ctrl_props, prop.value, prop.selected_value)

```

</details>