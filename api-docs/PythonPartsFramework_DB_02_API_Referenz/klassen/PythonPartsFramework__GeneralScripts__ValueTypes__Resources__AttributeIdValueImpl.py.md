---
title: "AttributeIdValueImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\AttributeIdValueImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# AttributeIdValueImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\AttributeIdValueImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the AttributeIdValue value type

## Abhängigkeiten

- `AttributeIdValue`
- `AttributeImpl`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ParameterPropertyValueTypes`
- `ParameterPropertyValueTypesImpl`
- `Utilities.AttributeIdEnums`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `AttributeIdValueImpl`

implementation of the AttributeIdValue value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AttributeIdValue` | `str` | convert the attribute ID and value to a string  Args:     value: attribute ID and value  Returns:     ID and value as string |
| `get_value` | `value_str: str` | `list[AttributeIdValue] | AttributeIdValue` | get the attribute ID and value from a string  Args:     value_str: attribute ID and value string  Returns:     ID and value from the string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the AttributeIdValue value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import NemAll_Python_BaseElements as AllplanBaseEle

from AttributeIdValue import AttributeIdValue
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.AttributeIdEnums import AttributeIdEnums

from ..ParameterPropertyValueType import ParameterPropertyValueType

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

from ..ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ..ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

from .AttributeImpl import AttributeImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class AttributeIdValueImpl(ParameterPropertyValueType):
    """ implementation of the AttributeIdValue value type
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

        if (list_index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            if list_index == len(prop.value):
                prop.value.append(value)

            elif isinstance(value, AttributeIdValue):
                prop.value[list_index] = value

                if value.attribute_id == 0:
                    del prop.value[list_index + 1:]

            else:
                prop.value[list_index].value = value

        elif isinstance(value, (AttributeIdValue, list)):
            prop.value = value

        else:
            prop.value.value = value

        return False


    @staticmethod
    def to_string(value: AttributeIdValue) -> str:
        """ convert the attribute ID and value to a string

        Args:
            value: attribute ID and value

        Returns:
            ID and value as string
        """

        doc = DocumentManager.get_instance().document

        AttributeType = AllplanBaseEle.AttributeService.AttributeType

        if AllplanBaseEle.AttributeService.GetAttributeType(doc, value.attribute_id) == AttributeType.Enum:
            return f"({value.attribute_id}," \
                   f"{AllplanBaseEle.AttributeService.GetEnumIDFromValueString(value.attribute_id, str(value.value))})"

        return f"({value.attribute_id},{value.value})"


    @staticmethod
    def get_value(value_str: str) -> (list[AttributeIdValue] | AttributeIdValue):
        """ get the attribute ID and value from a string

        Args:
            value_str: attribute ID and value string

        Returns:
            ID and value from the string
        """

        attribute_impl = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.ATTRIBUTE)

        def get_value_from_str(attr_value_str: str) -> AttributeIdValue:
            """ get the value from the string

            Args:
                attr_value_str: str

            Returns:
                value fro the string
            """

            value_str = attr_value_str.strip("()")

            attribute_id_str, _, value_str = value_str.partition(",")

            attribute_id = int(eval(attribute_id_str, {"AttributeIdEnums": AttributeIdEnums})) if attribute_id_str else 0

            return AttributeIdValue(attribute_id,
                                    attribute_impl.get_value_extend(value_str, attribute_id, None) if attribute_id else "")


        #----------------- convert to the ID and value

        if not BaseStringToValueConverter.is_list_value_string(value_str):
            return get_value_from_str(value_str)

        return [get_value_from_str(item) for item in value_str.strip("[]").split(");")]


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

        old_value = prop.value


        #----------------- get the attribute ID

        attribute_id = prop.value.attribute_id

        prop.attribute_id_str = str(attribute_id)
        prop.value    = prop.value.value

        if attribute_id:
            ctrl_props.row_name = AllplanBaseEle.AttributeService.GetAttributeName(DocumentManager.get_instance().document,
                                                                                        attribute_id)

        elif not ctrl_props.row_name:
            ctrl_props.row_name = ctrl_props.text


        #----------------- create a string edit control with an undefined value

        if not attribute_id:
            enable_cond                 = ctrl_props.enable_condition
            prop.value                  = prop_pal_ctrl_service.global_str_table.get_string("e_UNDEFINED", "undefined")
            ctrl_props.row_name         = " " * ParameterPropertyValueType.get_empty_row_counter()
            ctrl_props.enable_condition = "False"

            prop_pal_ctrl_service.add_string(wpf_palette, prop, ctrl_props)

            prop.value                  = old_value
            prop.attribute_id_str       = "0"
            ctrl_props.enable_condition = enable_cond
            return


        #----------------- create the control

        AttributeImpl.add_to_palette(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)

        prop.value            = old_value
        prop.attribute_id_str = "0"

```

</details>