---
title: "RefPointButtonImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\RefPointButtonImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# RefPointButtonImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\RefPointButtonImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the RefPointButton value type

## Abhängigkeiten

- `BaseIntImpl`
- `ControlProperties`
- `NemAll_Python_Palette`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.BaseValueToStringConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `RefPointButtonImpl`

implementation of the RefPointButton value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `get_value` | `value_str: str` | `AllplanPalette.RefPointPosition | list[AllplanPalette.RefPointPosition]` | get the reference point position from a string  Args:     value_str: value string  Returns:     value from string |
| `to_string` | `value: Any` | `str` | convert the value to a string  Args:     value: new value  Returns:     value as string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add a ref point button to palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `get_default_control_width` | `-` | `int` | get the default control width  Returns:     default control width |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the RefPointButton value type
"""
from __future__ import annotations

from typing import TYPE_CHECKING, cast, Any

import NemAll_Python_Palette as AllplanPalette

from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..BaseIntImpl import BaseIntImpl
from ..ValueTypeUtils.BaseValueToStringConverter import BaseValueToStringConverter
from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class RefPointButtonImpl(BaseIntImpl):
    """ implementation of the RefPointButton value type
    """

    @staticmethod
    def set_property_value(prop : ParameterProperty,
                           name : str,
                           value: Any) -> bool:
        """ Set the value of the property

        Args:
            prop:  property
            name:  name of the modified property
            value: new value

        Returns:
            update palette state
        """

        prop.is_modified = True

        return ParameterPropertyListUtil.set_item_value(prop, name, AllplanPalette.RefPointPosition.values[value])


    @staticmethod
    def get_value(value_str: str) -> (AllplanPalette.RefPointPosition | list[AllplanPalette.RefPointPosition]):
        """ get the reference point position from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        if "AllplanPalette" in value_str:   # pylint: disable=magic-value-comparison
            return eval(value_str, StringEvaluate.get_allplan_api_param_dict())

        return BaseStringToValueConverter.to_value_by_type_converter(
            lambda x: AllplanPalette.RefPointPosition.values[cast(int, BaseIntImpl.get_value(x))],
            value_str)


    @staticmethod
    def to_string(value: Any) -> str:
        """ convert the value to a string

        Args:
            value: new value

        Returns:
            value as string
        """

        if isinstance(value, int):
            value = AllplanPalette.RefPointPosition.values[value]

        return BaseValueToStringConverter.enum_to_string(value)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add a ref point button to palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if ctrl_props.width == ControlProperties.DEFAULT_WIDTH:
            ctrl_props.width = 70

        ref_pnt_type = ctrl_props.value_list_2 or "AllplanPalette.RefPointButtonType.eAllNinePositions"

        ref_pnt_type = eval(ref_pnt_type, prop_pal_ctrl_service.param_dict)

        row_name = ctrl_props.row_name or ctrl_props.text

        if isinstance(prop.value, int):
            prop.value = AllplanPalette.RefPointPosition.values[prop.value]

        wpf_palette.AddRefPointButton(ctrl_props.text, prop.name, prop.value, ref_pnt_type, prop_pal_ctrl_service.page_index,
                                      ctrl_props.expander_name + ctrl_props.expander_state_key,
                                      row_name + ctrl_props.row_state_key,
                                      prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                      ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)


    @staticmethod
    def get_default_control_width() -> int:
        """ get the default control width

        Returns:
            default control width
        """

        return 40

```

</details>