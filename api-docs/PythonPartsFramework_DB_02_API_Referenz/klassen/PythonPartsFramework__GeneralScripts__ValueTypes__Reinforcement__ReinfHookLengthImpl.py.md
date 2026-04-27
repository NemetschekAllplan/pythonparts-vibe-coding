---
title: "ReinfHookLengthImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfHookLengthImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ReinfHookLengthImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfHookLengthImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `werte`

## Übersicht

implementation of the ReinfHookLength value type

## Abhängigkeiten

- `BaseFloatImpl`
- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `ReinfHookLengthImpl`

implementation of the ReinfHookLength value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty.ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the ReinfHookLength edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `value_to_unit_string` | `value: float` | `str` | convert the value to the current unit value  Args:     value: value  Returns:     unit value as string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the ReinfHookLength value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_AllplanSettings as AllplanSettings

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

import ParameterProperty

from ..BaseFloatImpl import BaseFloatImpl

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ReinfHookLengthImpl(BaseFloatImpl):
    """ implementation of the ReinfHookLength value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty.ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the ReinfHookLength edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_pal_ctrl_service.add_edit_control(wpf_palette.AddLengthValue, prop, ctrl_props, prop.value)


    @staticmethod
    def value_to_unit_string(value: float) -> str:
        """ convert the value to the current unit value

        Args:
            value: value

        Returns:
            unit value as string
        """

        return AllplanSettings.UnitService.ToLengthUnitString(value)

```

</details>