---
title: "DoubleImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\DoubleImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# DoubleImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\DoubleImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Double value type

## Abhängigkeiten

- `BaseFloatImpl`
- `BuildingElement`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `DoubleImpl`

implementation of the Double value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the double edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `update_by_constraint` | `build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties, _name: str` | `None` | update by a constraint  Args:     build_ele:  building element with the parameter properties     prop:       parameter property to update     ctrl_props: control properties     _name:      name of the modified value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Double value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from .BaseFloatImpl import BaseFloatImpl

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class DoubleImpl(BaseFloatImpl):
    """ implementation of the Double value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the double edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_pal_ctrl_service.add_edit_control(wpf_palette.AddDoubleValue, prop, ctrl_props, prop.value)


    @staticmethod
    def update_by_constraint(build_ele : BuildingElement,
                             prop      : ParameterProperty,
                             ctrl_props: ControlProperties,
                             _name     : str):
        """ update by a constraint

        Args:
            build_ele:  building element with the parameter properties
            prop:       parameter property to update
            ctrl_props: control properties
            _name:      name of the modified value
        """

        prop.value = StringEvaluate.eval(ctrl_props.constraint[0],
                                         StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0]))

```

</details>