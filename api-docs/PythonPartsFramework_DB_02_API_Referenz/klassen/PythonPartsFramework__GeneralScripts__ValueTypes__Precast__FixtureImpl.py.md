---
title: "FixtureImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Precast\FixtureImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# FixtureImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Precast\FixtureImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Fixture value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `NemAll_Python_Palette`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `typing`

## Klassen

### `FixtureImpl`

implementation of the Fixture value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanPalette.FixtureProperties` | `str` | convert the fixture to a string  Args:     value: new value  Returns:     length as string |
| `get_value` | `value_str: str` | `list[AllplanPalette.FixtureProperties] | AllplanPalette.FixtureProperties` | get the fixture from a string  Args:     value_str: value string  Returns:     fixture from string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the string combo box control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Fixture value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import NemAll_Python_Palette as AllplanPalette

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from ..BaseStrImpl import BaseStrImpl

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class FixtureImpl(BaseStrImpl):
    """ implementation of the Fixture value type
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

        #----------------- assign the new value in case of a full element

        sep_count = name.count(".")

        if GeneralConstants.SUB_NAME_SEPARATOR not in name and not sep_count:
            prop.value = value

            return True


        #----------------- part can't be an empty list

        if value == []:
            return False


        #----------------- set the new value

        fixture = ParameterPropertyListUtil.get_item_value(prop, name)

        match name.split('.', 1)[1]:
            case "PathShortcut":
                fixture.PathShortcut = value
                return True

            case "Group":
                fixture.Group = value
                return True

            case "Element":
                fixture.Element = value
                return True

        return False


    @staticmethod
    def to_string(value: AllplanPalette.FixtureProperties) -> str:
        """ convert the fixture to a string

        Args:
            value: new value

        Returns:
            length as string
        """

        return ValueToStringUtil.trim_value_string(str(value))


    @staticmethod
    def get_value(value_str: str) -> (list[AllplanPalette.FixtureProperties] |  AllplanPalette.FixtureProperties):
        """ get the fixture from a string

        Args:
            value_str: value string

        Returns:
            fixture from string
        """

        def convert(value_str: str) -> AllplanPalette.FixtureProperties:
            """ get the fixture from a string

            Args:
                value_str: value string

            Returns:
                fixture
            """

            if not value_str:
                return AllplanPalette.FixtureProperties()

            return AllplanPalette.FixtureProperties(StringToValueUtil.get_property_string(value_str, "PathShortcut", ""),
                                                    StringToValueUtil.get_property_string(value_str, "Group", ""),
                                                    StringToValueUtil.get_property_string(value_str, "Element", ""))

        return BaseStringToValueConverter.to_value_by_type_converter(convert, value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the string combo box control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        text = ctrl_props.text

        if prop_pal_ctrl_service.global_str_table is None:
            return

        wpf_palette.AddFixtureValues(f"{text} - {prop_pal_ctrl_service.global_str_table.get_entry('e_PATH')[0]}",
                                     f"{text} - {prop_pal_ctrl_service.global_str_table.get_entry('e_FILE')[0]}",
                                     f"{text} - {prop_pal_ctrl_service.global_str_table.get_entry('e_ENTRY')[0]}",
                                     prop.name, prop.value, prop_pal_ctrl_service.page_index,
                                     ctrl_props.expander_name + ctrl_props.expander_state_key,
                                     ctrl_props.row_name + ctrl_props.row_state_key,
                                     prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

```

</details>