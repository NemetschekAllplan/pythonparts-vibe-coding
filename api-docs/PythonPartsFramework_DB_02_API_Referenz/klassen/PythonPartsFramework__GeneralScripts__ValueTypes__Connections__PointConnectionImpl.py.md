---
title: "PointConnectionImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Connections\PointConnectionImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PointConnectionImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Connections\PointConnectionImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the point connection value type

## Abhängigkeiten

- `ControlProperties`
- `Data.PointConnection`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_IFW_Input`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `PointConnectionImpl`

implementation of the point connection value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, _name: str, _value: str` | `bool` | Set the value of the property  Args:     prop:   property     _name:  name of the modified property     _value: new value  Returns:     update palette state |
| `to_string` | `value: PointConnection` | `str` | convert the value to a string  Args:     value: new value  Returns:     list as string |
| `get_value` | `value_str: str` | `PointConnection | list[PointConnection]` | get the value from a string  Args:     value_str: value string  Returns:     value |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the CheckBox control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the point connection value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_IFW_Input as AllplanIFW

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from ..Data.PointConnection import PointConnection

from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class PointConnectionImpl(ParameterPropertyValueType):
    """ implementation of the point connection value type
    """

    @staticmethod
    def set_property_value(prop  : ParameterProperty,
                           _name : str,
                           _value: str) -> bool:
        """ Set the value of the property

        Args:
            prop:   property
            _name:  name of the modified property
            _value: new value

        Returns:
            update palette state
        """

        prop.value = PointConnection(AllplanIFW.DockingPoint())

        return False


    @staticmethod
    def to_string(value: PointConnection) -> str:
        """ convert the value to a string

        Args:
            value: new value

        Returns:
            list as string
        """

        return value.to_string()


    @staticmethod
    def get_value(value_str: str) -> (PointConnection | list[PointConnection]):
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        return PointConnection.get_value(value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the CheckBox control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        row_name = ctrl_props.text

        value = prop.value.is_valid()

        wpf_palette.AddCheckboxValue(ctrl_props.text, prop.name, value, prop_pal_ctrl_service.page_index,
                                     ctrl_props.expander_name + ctrl_props.expander_state_key,
                                     row_name + ctrl_props.row_state_key,
                                     prop_pal_ctrl_service.is_control_enabled(ctrl_props) and value,
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        wpf_palette.AddPictureButton("Property match", prop.name + GeneralConstants.PALETTE_BUTTON_POINT_TAKE_OVER_KEY,
                                      str(int(AllplanSettings.PictResPalette.ePropertyTakeOver)),                             # type: ignore
                                      0, prop_pal_ctrl_service.page_index,
                                      ctrl_props.expander_name, row_name,
                                      prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                      ctrl_props.height, 10,
                                      ctrl_props.font_face_code)

```

</details>