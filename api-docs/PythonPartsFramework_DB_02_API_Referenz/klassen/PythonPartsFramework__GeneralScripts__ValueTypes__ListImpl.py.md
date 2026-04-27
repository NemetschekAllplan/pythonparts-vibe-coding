---
title: "ListImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ListImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ListImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ListImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the list value type

## Abhängigkeiten

- `BuildingElementConverterUtil`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ParameterPropertyValueTypesImpl`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `typing`

## Klassen

### `ListImpl`

implementation of the list value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: Any` | `str` | convert the value to a string  Args:     value: new value  Returns:     list as string |
| `get_value` | `value_str: str` | `Any` | get the list from a string  Args:     value_str: value string  Returns:     value |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__get_value_type` | `value: Any` | `ParameterPropertyValueType | None` | get the value type of the object  Args:     value: geometry object  Returns:     value type |
| `is_add_to_palette_for_single_list_item` | `-` | `bool` | check, whether the add_to_palette function must be called for a single list item  Returns:     add control for single list item state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the list value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from BuildingElementConverterUtil import BuildingElementConverterUtil
from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from .ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from .ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService
from .ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

from .ParameterPropertyValueType import ParameterPropertyValueType
from .ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class ListImpl(ParameterPropertyValueType):
    """ implementation of the list value type
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

        #----------------- 2 dim. list

        if (index_2d := ParameterPropertyListUtil.get_list_index_2dim(name)) is not None:
            if isinstance(prop.value[index_2d[0]], list):
                prop_value = prop.value[index_2d[0]][index_2d[1]]
            else:
                prop_value = prop.value[index_2d[0]]

            if (value_type := ListImpl.__get_value_type(prop_value)) is None:
                return False

            return value_type.set_property_value(prop, name, value)


        #----------------- 1 dim. list

        if (list_index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            if isinstance(prop.value, list):
                if list_index - len(prop.value) >= 0:
                    return False

                prop_value = prop.value[list_index]
            else:
                prop_value = prop.value

            if (value_type := ListImpl.__get_value_type(prop_value)) is None:
                return False

            return value_type.set_property_value(prop, name, value)


        #----------------- normal value

        if not name.count(GeneralConstants.SUB_NAME_SEPARATOR):
            prop.value = value

            return True

        if (value_type := ListImpl.__get_value_type(prop.value)) is None:
            return False

        return value_type.set_property_value(prop, name, value)


    @staticmethod
    def to_string(value: Any) -> str:
        """ convert the value to a string

        Args:
            value: new value

        Returns:
            list as string
        """

        return ValueToStringUtil.check_to_string_strip(value)


    @staticmethod
    def get_value(value_str: str) -> Any:
        """ get the list from a string

        Args:
            value_str: value string

        Returns:
            value
        """

        def convert(item_value_str: str) -> Any:
            """ convert the value string

            Args:
                item_value_str: geometry value string

            Returns:
                object
            """

            if not (value_type := ListImpl.__get_value_type(item_value_str)):
                return eval(item_value_str) if item_value_str else item_value_str

            if not value_type.has_impl:
                if (converter := BuildingElementConverterUtil.get_string_to_value_converter(value_type)) is None:
                    return None

                return converter(value_str)

            return value_type.get_value(item_value_str)

        return BaseStringToValueConverter.to_value_by_type_converter(convert, value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the control to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if (value_type := ListImpl.__get_value_type(prop.value)) is None:
            return

        if ctrl_props.row_name.isnumeric() and int(ctrl_props.row_name) > ctrl_props.value_list_start_row:
            wpf_palette.AddSeparator(prop_pal_ctrl_service.page_index, ctrl_props.expander_name)

        value_type.add_to_palette(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def __get_value_type(value: Any) -> (ParameterPropertyValueType | None):
        """ get the value type of the object

        Args:
            value: geometry object

        Returns:
            value type
        """

        value_str = str(value)

        if (index := value_str.find("(")) == -1:
            return None

        value_type = value_str[:index]

        return ParameterPropertyValueTypesImpl.get_value_type_impl(value_type)


    @staticmethod
    def is_add_to_palette_for_single_list_item() -> bool:
        """ check, whether the add_to_palette function must be called for a single list item

        Returns:
            add control for single list item state
        """

        return False

```

</details>