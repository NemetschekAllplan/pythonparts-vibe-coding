---
title: "DynamicListImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\DynamicListImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# DynamicListImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\DynamicListImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the DynamicList value type

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ParameterPropertyValueTypes`
- `ParameterPropertyValueTypesImpl`
- `Utilities.GeneralConstants`
- `Utilities.MultiIndexListUtil`
- `ValueTypeUtils.ControlMinMaxUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `DynamicListImpl`

implementation of the DynamicList value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value_extend` | `self, value_str: str, attribute_id: int | list[int], build_ele_str_table: BuildingElementStringTable` | `Any` | get the value from a string by an extended functionality  Args:     value_str:           value string     attribute_id:        attribute id     build_ele_str_table: string table of the building element  Returns:     value from the string |
| `to_string_extend` | `self, value: Any, _attribute_id: int | list[int], _build_ele_str_table: BuildingElementStringTable | None` | `str` | convert the data to a string by an extended functionality  Args:     value:                new value     _attribute_id:        attribute id     _build_ele_str_table: string table of the building element  Returns:     values as string |
| `set_property_value` | `prop: ParameterProperty.ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty.ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the dynamiclist edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `string_to_unit_value` | `self, value_str: str` | `Any` | convert the string to the unit value  Args:     value_str: value string  Returns:     unit value as string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the DynamicList value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import NemAll_Python_AllplanSettings as AllplanSettings

from ControlProperties import ControlProperties

import ParameterProperty

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants
from Utilities.MultiIndexListUtil import MultiIndexListUtil

from .ValueTypeUtils.ControlMinMaxUtil import ControlMinMaxUtil
from .ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from .ParameterPropertyValueType import ParameterPropertyValueType
from .ParameterPropertyValueTypes import ParameterPropertyValueTypes
from .ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from BuildingElementStringTable import BuildingElementStringTable
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class DynamicListImpl(ParameterPropertyValueType):
    """ implementation of the DynamicList value type
    """

    def get_value_extend(self,
                         value_str          : str,
                         attribute_id       : (int | list[int]),
                         build_ele_str_table: BuildingElementStringTable) -> Any:
        """ get the value from a string by an extended functionality

        Args:
            value_str:           value string
            attribute_id:        attribute id
            build_ele_str_table: string table of the building element

        Returns:
            value from the string
        """

        list_value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(self.split("(", 1)[-1].rstrip(")"))

        return list_value_type.get_value_extend(value_str, attribute_id, build_ele_str_table)


    def to_string_extend(self,
                         value               : Any,
                         _attribute_id       : (int | list[int]),
                         _build_ele_str_table: (BuildingElementStringTable | None)) -> str:
        """ convert the data to a string by an extended functionality

        Args:
            value:                new value
            _attribute_id:        attribute id
            _build_ele_str_table: string table of the building element

        Returns:
            values as string
        """

        list_value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(self.split("(", 1)[-1].rstrip(")"))

        return list_value_type.to_string(value)


    @staticmethod
    def set_property_value(prop : ParameterProperty.ParameterProperty,
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

        multi_index = ParameterPropertyListUtil.get_multiple_list_index(name)

        #----------------- delete the items

        if name.endswith(GeneralConstants.PALETTE_BUTTON_DELETE_KEY):
            if multi_index is not None:
                MultiIndexListUtil.delete_values(prop, multi_index)

            elif (index := ParameterPropertyListUtil.get_list_index(name)) is not None and index < len(prop.value):
                del prop.value[index]

            return True


        #----------------- set the value

        list_value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(prop.value_type.split("(", 1)[-1].rstrip(")"))

        if (ParameterPropertyListUtil.get_list_index(name) if multi_index is None else multi_index[-1][-1]) == len(prop.value):
            prop.value.append(list_value_type.get_value(""))

        if isinstance(value, str):
            value = list_value_type.string_to_unit_value(value)

        list_value_type.set_property_value(prop, name, value)

        return True


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty.ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the dynamiclist edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        item_prop       = prop.deep_copy()
        item_ctrl_props = ctrl_props.deep_copy()

        multi_index = prop_pal_ctrl_service.build_ele.get_existing_property(ctrl_props.value_index_name).value

        item_prop.value, varied = MultiIndexListUtil.get_value(prop, multi_index, prop_pal_ctrl_service.global_str_table)


        #----------------- create the control

        if varied or isinstance(item_prop.value, str):
            item_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.STRING)
        else:
            item_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(prop.value_type.split("(", 1)[-1].rstrip(")"))

        item_ctrl_props.value_name = f"{prop.name}[{multi_index.get_indexes(True)}]"
        item_prop.name             = item_ctrl_props.value_name

        item_ctrl_props.row_name = item_ctrl_props.text

        if ctrl_props.value_dialog:
            if not item_prop.value:
                item_prop.value = prop_pal_ctrl_service.global_str_table.get_string("e_EMPTY", "Empty")

            ctrl_props.value_dialog.create_controls(wpf_palette, item_prop, item_ctrl_props, prop_pal_ctrl_service.page_index,
                                                    prop_pal_ctrl_service.global_str_table, prop_pal_ctrl_service.is_control_enabled)

            item_ctrl_props.value_dialog = None

        else:
            ControlMinMaxUtil.set_min_max_values(item_ctrl_props, item_prop.value_type, cast(int, item_prop.attribute_id),
                                                 prop_pal_ctrl_service.param_dict)

            item_prop.value_type.add_to_palette(wpf_palette, item_prop, item_ctrl_props, prop_pal_ctrl_service)

        wpf_palette.AddPictureResourceButton("", f"{item_prop.name}{GeneralConstants.PALETTE_BUTTON_DELETE_KEY}",
                                                cast(int, AllplanSettings.PictResPalette.eClear), 0,
                                                prop_pal_ctrl_service.page_index,
                                                item_ctrl_props.expander_name, item_ctrl_props.row_name + item_ctrl_props.row_state_key,
                                                prop_pal_ctrl_service.is_control_enabled(item_ctrl_props),
                                                item_ctrl_props.height, 8, item_ctrl_props.font_face_code)


    def string_to_unit_value(self,
                             value_str: str) -> Any:
        """ convert the string to the unit value

        Args:
            value_str: value string

        Returns:
            unit value as string
        """

        list_value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(self.split("(", 1)[-1].rstrip(")"))

        return list_value_type.string_to_unit_value(value_str)

```

</details>