---
title: "AttributeImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\AttributeImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# AttributeImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\AttributeImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Attribute value type

## Abhängigkeiten

- `BuildingElementStringTable`
- `ControlProperties`
- `DateImpl`
- `DialogTypes.DateDialogImpl`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Palette`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `datetime`
- `typing`

## Klassen

### `AttributeImpl`

implementation of the Attribute value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `_value: Any` | `None` | convert the attribute to a string  Args:     _value: new value |
| `get_value` | `_value_str: Any` | `None` | get the attribute from a string  Args:     _value_str: value string |
| `to_string_extend` | `self, value: Any, attribute_id: int, _build_ele_str_table: BuildingElementStringTable | None` | `str | None` | convert the data to a string by an extended functionality  Args:     value:                new value     attribute_id:         attribute id     _build_ele_str_table: string table of the building element  Returns:     values as string |
| `get_value_extend` | `self, value_str: str, attribute_ids: int | list[int], _build_ele_str_table: BuildingElementStringTable` | `int | float | str | date | list[int | float | str | date]` | get the attribute from a string  Args:     value_str:            value from string     attribute_ids:        attribute IDs     _build_ele_str_table: description  Returns:     attribute value |
| `__convert_string_to_attribute_value` | `value_str: str, attribute_id: int` | `int | float | str | date` | convert a string to an attribute value  Args:     value_str:    value string     attribute_id: attribute ID  Returns:     attribute value |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Attribute value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING, cast
from datetime import date

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Palette as AllplanPalette

from ControlProperties import ControlProperties
from DocumentManager import DocumentManager

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

import DialogTypes.DateDialogImpl

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..DateImpl import DateImpl
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType

if TYPE_CHECKING:
    from BuildingElementStringTable import BuildingElementStringTable
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class AttributeImpl(ParameterPropertyValueType):
    """ implementation of the Attribute value type
    """

    ATTRIBUTE_NAME = "$Attribute_Name"

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

        if isinstance(ParameterPropertyListUtil.get_item_value(prop, name), date):
            return DateImpl.set_property_value(prop, name, value)

        ParameterPropertyListUtil.set_item_value(prop, name, value)

        return False


    @staticmethod
    def to_string(_value: Any):
        """ convert the attribute to a string

        Args:
            _value: new value
        """

        assert False, "not possible to call 'to_string' for value type 'Attribute'"


    @staticmethod
    def get_value(_value_str: Any):
        """ get the attribute from a string

        Args:
            _value_str: value string
        """

        assert False, "not possible to call 'get_value' for value type 'Attribute'"


    def to_string_extend(self,                          # pylint: disable=no-self-use
                         value               : Any,
                         attribute_id        : int,
                         _build_ele_str_table: (BuildingElementStringTable | None)) -> (str | None):
        """ convert the data to a string by an extended functionality

        Args:
            value:                new value
            attribute_id:         attribute id
            _build_ele_str_table: string table of the building element

        Returns:
            values as string
        """

        assert attribute_id

        doc = DocumentManager.get_instance().document

        attributel_type_enum = AllplanBaseEle.AttributeService.AttributeType

        attrib_type = AllplanBaseEle.AttributeService.GetAttributeType(doc, attribute_id)

        match attrib_type:
            case attributel_type_enum.Enum:
                return str(AllplanBaseEle.AttributeService.GetEnumIDFromValueString(attribute_id, str(value)))

            case attributel_type_enum.Date:
                return DateImpl.to_string(cast(date, value))

            case attributel_type_enum.String | attributel_type_enum.WString:
                control_type_enum = AllplanBaseEle.AttributeService.AttributeControlType

                ctrl_type = AllplanBaseEle.AttributeService.GetAttributeControlType(doc, attribute_id)

                if ctrl_type in (control_type_enum.ComboBoxFixed, control_type_enum.ComboBox):
                    input_list = AllplanBaseEle.AttributeService.GetInputListValues(doc, attribute_id)

                    if value in input_list:
                        return str(input_list.index(value))     # type: ignore

        return str(value)


    def get_value_extend(self,                              # pylint: disable=no-self-use
                         value_str           : str,
                         attribute_ids       : (int | list[int]),
                         _build_ele_str_table: BuildingElementStringTable) -> (int | float | str | date | list[int | float | str | date]):
        """ get the attribute from a string

        Args:
            value_str:            value from string
            attribute_ids:        attribute IDs
            _build_ele_str_table: description

        Returns:
            attribute value
        """

        if not isinstance(attribute_ids, list):
            return AttributeImpl.__convert_string_to_attribute_value(value_str, attribute_ids)

        if not (value_str := value_str.strip("[]").replace("\"", "")):
            return ""

        values = value_str.split(",")

        if (attr_fac := len(values) - len(attribute_ids)) > 0:
            attribute_ids += [attribute_ids[0]] * attr_fac

        return [AttributeImpl.__convert_string_to_attribute_value(value, attribute_id) \
               for attribute_id, value in zip(attribute_ids, values)]


    @staticmethod
    def __convert_string_to_attribute_value(value_str   : str,
                                            attribute_id: int) -> (int | float | str | date):
        """ convert a string to an attribute value

        Args:
            value_str:    value string
            attribute_id: attribute ID

        Returns:
            attribute value
        """

        assert attribute_id

        doc = DocumentManager.get_instance().document

        attributel_type_enum = AllplanBaseEle.AttributeService.AttributeType

        match AllplanBaseEle.AttributeService.GetAttributeType(doc, attribute_id):
            case attributel_type_enum.Integer:
                return cast(int, BaseStringToValueConverter.to_int(value_str))

            case attributel_type_enum.Double:
                return cast(float, BaseStringToValueConverter.to_float(value_str))

            case attributel_type_enum.Enum:
                value_str = AllplanBaseEle.AttributeService.GetEnumValueStringFromID(attribute_id, int(value_str))

                return value_str if value_str else AllplanBaseEle.AttributeService.GetEnumValues(doc, attribute_id)[0]

            case attributel_type_enum.String | attributel_type_enum.WString:
                control_type_enum = AllplanBaseEle.AttributeService.AttributeControlType

                ctrl_type = AllplanBaseEle.AttributeService.GetAttributeControlType(doc, attribute_id)

                if ctrl_type in (control_type_enum.ComboBoxFixed, control_type_enum.ComboBox) and value_str.isdigit():
                    input_list = AllplanBaseEle.AttributeService.GetInputListValues(doc, attribute_id)

                    if (index := int(value_str)) < len(input_list):
                        return input_list[index]

                    return input_list[0]

            case attributel_type_enum.Date:
                return cast(date, DateImpl.get_value(value_str))

        return value_str


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

        doc          = DocumentManager.get_instance().document
        attribute_id = cast(int, prop.attribute_id)

        attributel_type_enum = AllplanBaseEle.AttributeService.AttributeType


        #----------------- get the value list

        if (attrib_type := AllplanBaseEle.AttributeService.GetAttributeType(doc, attribute_id)) == attributel_type_enum.Enum:   # pylint: disable=consider-ternary-expression
            value_list = [str(value) for value in AllplanBaseEle.AttributeService.GetEnumValues(doc, attribute_id)]
        else:
            value_list = [str(value) for value in AllplanBaseEle.AttributeService.GetInputListValues(doc, attribute_id)]

        value_list = "|".join(value_list)

        ctrl_props.value_list = value_list

        if AttributeImpl.ATTRIBUTE_NAME in ctrl_props.text:
            ctrl_props.text = ctrl_props.text.replace(AttributeImpl.ATTRIBUTE_NAME,
                                                      AllplanBaseEle.AttributeService.GetAttributeName(doc, attribute_id))

        if AttributeImpl.ATTRIBUTE_NAME in ctrl_props.row_name:
            ctrl_props.row_name = ctrl_props.row_name.replace(AttributeImpl.ATTRIBUTE_NAME,
                                                              AllplanBaseEle.AttributeService.GetAttributeName(doc, attribute_id))


        #----------------- create the control

        control_type_enum = AllplanBaseEle.AttributeService.AttributeControlType

        ctrl_type = AllplanBaseEle.AttributeService.GetAttributeControlType(doc, attribute_id)

        match attrib_type:
            case attributel_type_enum.Integer:
                match ctrl_type:
                    case control_type_enum.ComboBoxFixed | control_type_enum.ComboBox:
                        match AllplanBaseEle.AttributeService.GetAttributeType(doc, attribute_id):
                            case attributel_type_enum.Integer:
                                prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.INTEGER)

                            case attributel_type_enum.Double:
                                prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.DOUBLE)

                            case attributel_type_enum.Enum:
                                prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.STRING)

                            case attributel_type_enum.String | attributel_type_enum.WString:
                                prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.STRING)

                    case control_type_enum.Edit:
                        prop_pal_ctrl_service.add_edit_control(wpf_palette.AddIntValue, prop, ctrl_props, int(prop.value))

                    case control_type_enum.CheckBox:
                        if isinstance(prop.value, str):
                            prop_pal_ctrl_service.add_string_edit_control(wpf_palette, prop, ctrl_props, prop.value)
                        else:
                            prop_pal_ctrl_service.add_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, int(prop.value))

                    case control_type_enum.ComboBoxHatch:
                        prop_pal_ctrl_service.add_control(wpf_palette.AddHatchValue, prop, ctrl_props, int(prop.value))

                    case control_type_enum.ComboBoxPattern:
                        prop_pal_ctrl_service.add_control(wpf_palette.AddPatternValue, prop, ctrl_props, int(prop.value))

                    case control_type_enum.ComboBoxFilling:
                        prop_pal_ctrl_service.add_control(wpf_palette.AddColorValue, prop, ctrl_props, int(prop.value))

            case attributel_type_enum.Double:
                if ctrl_type in (control_type_enum.ComboBoxFixed, control_type_enum.ComboBox):
                    prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.DOUBLE)
                else:
                    prop_pal_ctrl_service.add_edit_control(wpf_palette.AddDoubleValue, prop, ctrl_props, float(prop.value))

            case attributel_type_enum.Enum:
                prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.STRING)

            case attributel_type_enum.String |  attributel_type_enum.WString:
                if ctrl_type in (control_type_enum.ComboBoxFixed, control_type_enum.ComboBox):
                    prop_pal_ctrl_service.add_combo_box(wpf_palette, prop, ctrl_props, AllplanPalette.PaletteValueType.STRING)

                else:
                    prop_pal_ctrl_service.add_string(wpf_palette, prop, ctrl_props)

            case attributel_type_enum.Date:
                date_ctrl_props = ctrl_props.deep_copy()

                date_ctrl_props.row_name = ctrl_props.row_name or ctrl_props.text

                DateImpl.add_to_palette(wpf_palette, prop, date_ctrl_props, prop_pal_ctrl_service)

                DialogTypes.DateDialogImpl.DateDialogImpl.create_controls(wpf_palette, prop, date_ctrl_props,
                                                                          prop_pal_ctrl_service.page_index,
                                                                          prop_pal_ctrl_service.global_str_table,
                                                                          prop_pal_ctrl_service.is_control_enabled)

            case _ if not attributel_type_enum.Undef:
                assert False, f"Attribute type {attrib_type} has no input control for the palette!"

```

</details>