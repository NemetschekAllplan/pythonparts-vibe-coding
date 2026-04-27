---
title: "ReinfSteelGradeImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfSteelGradeImpl.py"
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


# ReinfSteelGradeImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfSteelGradeImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `werte`

## Übersicht

implementation of the ReinfSteelGrade value type

## Abhängigkeiten

- `BaseIntImpl`
- `ControlProperties`
- `NemAll_Python_Reinforcement`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `ReinfSteelGradeImpl`

implementation of the ReinfSteelGrade value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[int] | int` | get the steel grade from a string  Args:     value_str: value string  Returns:     value from string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the ReinfSteelGrade edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the ReinfSteelGrade value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_Reinforcement as AllplanReinf

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from ..BaseIntImpl import BaseIntImpl
from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ReinfSteelGradeImpl(BaseIntImpl):
    """ implementation of the ReinfSteelGrade value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[int] | int):
        """ get the steel grade from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        if value_str == GeneralConstants.USE_CURRENT_RESOURCE_VALUE:
            return AllplanReinf.ReinforcementSettings.GetSteelGrade()

        return BaseStringToValueConverter.to_int(value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the ReinfSteelGrade edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_pal_ctrl_service.add_control(wpf_palette.AddSteelGrade, prop, ctrl_props, prop.value)

```

</details>