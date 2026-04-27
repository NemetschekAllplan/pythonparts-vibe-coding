---
title: "ReinfBarDiameterImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfBarDiameterImpl.py"
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


# ReinfBarDiameterImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinfBarDiameterImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `werte`

## Übersicht

implementation of the ReinfBarDiameter value type

## Abhängigkeiten

- `BaseFloatImpl`
- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Reinforcement`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `ReinfBarDiameterImpl`

implementation of the ReinfBarDiameter value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `value_str: str` | `list[float] | float` | get the diameter from a string  Args:     value_str: value string  Returns:     value from string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty.ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the ReinfBarDiameter edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `value_to_unit_string` | `value: float` | `str` | convert the value to the current unit value  Args:     value: value  Returns:     unit value as string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the ReinfBarDiameter value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Reinforcement as AllplanReinf

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

import ParameterProperty

from Utilities.GeneralConstants import GeneralConstants

from ..BaseFloatImpl import BaseFloatImpl
from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ReinfBarDiameterImpl(BaseFloatImpl):
    """ implementation of the ReinfBarDiameter value type
    """

    @staticmethod
    def get_value(value_str: str) -> (list[float] | float):
        """ get the diameter from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        if value_str == GeneralConstants.USE_CURRENT_RESOURCE_VALUE:
            return AllplanReinf.ReinforcementSettings.GetBarDiameter()

        diameter = BaseStringToValueConverter.to_float(value_str)

        if not isinstance(diameter, list):
            return AllplanReinf.ReinforcementSettings.CheckBarDiameter(diameter)

        return [AllplanReinf.ReinforcementSettings.CheckBarDiameter(diameter[i]) for i in range(0, len(diameter))]


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty.ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the ReinfBarDiameter edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_pal_ctrl_service.add_control(wpf_palette.AddBarDiameter, prop, ctrl_props, float(prop.value))


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