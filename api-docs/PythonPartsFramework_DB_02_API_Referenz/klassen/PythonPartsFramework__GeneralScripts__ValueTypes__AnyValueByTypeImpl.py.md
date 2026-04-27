---
title: "AnyValueByTypeImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\AnyValueByTypeImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# AnyValueByTypeImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\AnyValueByTypeImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the AnyValueByType value type

## Abhängigkeiten

- `AnyValueByType`
- `BaseFloatImpl`
- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `Palette.PaletteControlByValueTypeCreator`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueTypes`
- `ParameterPropertyValueTypesImpl`
- `StringEvaluate`
- `StringToValueConverter`
- `ValueToStringConverter`
- `ValueTypeUtil`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ControlMinMaxUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypes.ValueTypeUtils.MinMaxValidator`
- `__future__`
- `ast`
- `dataclasses`
- `typing`

## Klassen

### `AnyValueByTypeImpl`

implementation of the AnyValueByType value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AnyValueByType` | `str` | convert the data to a string  Args:     value: new value  Returns:     values as string |
| `get_value` | `value_str: str` | `AnyValueByType | list[AnyValueByType]` | get the value from a string  Args:     value_str: value string  Returns:     value from the string |
| `__string_to_any_value_by_type` | `value_str: str` | `AnyValueByType` | convert a string to an AnyValueByType object  Args:     value_str: value string  Returns:     AnyValueByType object |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the any value by type control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `update_by_constraint` | `build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties, _name: str` | `None` | update by a constraint  Args:     build_ele:  building element with the parameter properties     prop:       parameter property to update     ctrl_props: control properties     _name:      name of the modified value |
| `validate_minimal_value` | `ctrl_prop: ControlProperties, parameter_dict: dict[str, Any]` | `ValidateMinValueResult` | validate, whether the minimal value of the control property has changed  Args:     ctrl_prop:      control property     parameter_dict: parameter dictionary for the range command  Returns:     min value validation result |
| `validate_maximal_value` | `ctrl_prop: ControlProperties, parameter_dict: dict[str, Any]` | `ValidateMaxValueResult` | validate, whether the maximal value of the control property has changed  Args:     ctrl_prop:      control property     parameter_dict: parameter dictionary for the range command  Returns:     min value validation result |
| `validate_for_min_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, min_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the minimal value  Args:     prop:             property     ctrl_prop:        control properties     min_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `validate_for_max_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, max_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the maximal value  Args:     prop:             property     ctrl_prop:        control properties     max_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `__get_value_for_type` | `value_type: str, value: Any` | `Any` | get the value for the value type  Args:     value_type: value type     value:      new value  Returns:     value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the AnyValueByType value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ast import literal_eval
from dataclasses import asdict

from AnyValueByType import AnyValueByType
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate
from StringToValueConverter import StringToValueConverter
from ValueToStringConverter import ValueToStringConverter
from ValueTypeUtil import ValueTypeUtil

from Palette.PaletteControlByValueTypeCreator import PaletteControlByValueTypeCreator
from Palette.WpfPaletteBuilder import WpfPaletteBuilder

import ValueTypes.ValueTypeUtils.MinMaxValidator

from .BaseFloatImpl import BaseFloatImpl
from .ParameterPropertyValueTypes import ParameterPropertyValueTypes
from .ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

from .ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from .ValueTypeUtils.ControlMinMaxUtil import ControlMinMaxUtil
from .ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class AnyValueByTypeImpl(BaseFloatImpl):
    """ implementation of the AnyValueByType value type
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

        item_value : AnyValueByType = ParameterPropertyListUtil.get_item_value(prop, name)


        #----------------- set all data

        if isinstance(value, AnyValueByType):
            item_value.value_type = value.value_type
            item_value.text       = value.text
            item_value.value      = value.value
            item_value.value_list = value.value_list
            item_value.max_value  = value.max_value
            item_value.min_value  = value.min_value

            return False


        #----------------- set only the value

        value_prop = prop.deep_copy()

        value_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(item_value.value_type)
        value_prop.value      = item_value.value

        left, sep, right = name.partition(".")

        name = left.split("[", 1)[0] + sep + right

        ret = ParameterPropertyValueTypesImpl.get_value_type_impl(item_value.value_type).set_property_value(value_prop, name, value)

        item_value.value = value_prop.value

        return ret


    @staticmethod
    def to_string(value: AnyValueByType) -> str:
        """ convert the data to a string

        Args:
            value: new value

        Returns:
            values as string
        """

        value_dict = asdict(value)

        value_dict["value"] = \
            ValueToStringConverter.to_string_from_value(value.value,
                                                        ParameterPropertyValueTypesImpl.get_value_type_impl(value.value_type), None)

        return str(value_dict)


    @staticmethod
    def get_value(value_str: str) -> AnyValueByType | list[AnyValueByType]:
        """ get the value from a string

        Args:
            value_str: value string

        Returns:
            value from the string
        """

        if not value_str or value_str == StringToValueConverter.convert_to_empty_list:
            return []

        return BaseStringToValueConverter.to_value_by_type_converter(AnyValueByTypeImpl.__string_to_any_value_by_type, value_str)


    @staticmethod
    def __string_to_any_value_by_type(value_str: str) -> AnyValueByType:
        """ convert a string to an AnyValueByType object

        Args:
            value_str: value string

        Returns:
            AnyValueByType object
        """

        data_dict = literal_eval(value_str)

        value_type = data_dict["value_type"].lower()

        value = AnyValueByType(value_type,
                               data_dict["text"],
                               StringToValueConverter.get_value(ParameterPropertyValueTypesImpl.get_value_type_impl(value_type),
                                                                str(data_dict["value"])),
                               data_dict["value_list"],
                               data_dict["min_value"],
                               data_dict["max_value"],)

        return value


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the any value by type control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop        = prop.deep_copy()
        ctrl_props = ctrl_props.deep_copy()

        value : AnyValueByType = prop.value

        if value.text:
            ctrl_props.text = value.text

        ctrl_props.value_list          = value.value_list
        ctrl_props.min_value_condition = value.min_value
        ctrl_props.max_value_condition = value.max_value

        if value.text:
            ctrl_props.row_name = value.text

        prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(value.value_type)
        prop.value      = value.value

        ControlMinMaxUtil.set_min_max_values(ctrl_props, prop.value_type, 0, prop_pal_ctrl_service.param_dict)

        PaletteControlByValueTypeCreator.excecute(wpf_palette, prop, ctrl_props, prop.value_type, prop_pal_ctrl_service)


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

        param_dict = build_ele.get_parameter_dict()

        for constraint in ctrl_props.constraint:
            name, _, value_name = constraint.partition("=")

            match name:
                case "value_type":
                    prop.value.value_type = StringEvaluate.eval(value_name, param_dict, False).lower()

                    if prop.value_type == ParameterPropertyValueTypes.STRING:
                        prop.value.value = str(prop.value.value)

                        continue

                    prop.value.value = AnyValueByTypeImpl.__get_value_for_type(prop.value.value_type, prop.value)

                case "min_value":
                    min_value = build_ele.get_existing_property(value_name).value

                    prop.value.min_value = str(AnyValueByTypeImpl.__get_value_for_type(prop.value.value_type, min_value))

                case "max_value":
                    max_value = build_ele.get_existing_property(value_name).value

                    prop.value.max_value = str(AnyValueByTypeImpl.__get_value_for_type(prop.value.value_type, max_value))


    class ValidateMinValueResult():
        """ result of the min value validation
        """

        def __init__(self,
                     ctrl_prop     : ControlProperties,
                     parameter_dict: dict[str, Any]):
            """ initialize

            Args:
                ctrl_prop:      control properties
                parameter_dict: parameter dictionary for the range command
            """

            self.has_minimal_cond = True
            self.ctrl_prop        = ctrl_prop
            self.parameter_dict   = parameter_dict


        def get_min_value_state(self) -> tuple[bool, (bool | None)]:
            """ get the min value state

            Returns:
                has minimal condition, minimal value changed
            """

            return self.has_minimal_cond, None


        def get_value(self,
                      prop: ParameterProperty,
                      name: str) -> Any:
            """ get the value

            Args:
                prop: property
                name: name of the value, including the name of the sub value (tuple field name, geometry .X, ...)

            Returns:
                value
            """

            value = ParameterPropertyListUtil.get_item_value(prop, name)

            if ValueTypeUtil.is_string_input(value.value_type):
                return None

            if value.min_value == "":
                return None

            return StringEvaluate.eval(value.min_value, self.parameter_dict)


    class ValidateMaxValueResult():
        """ result of the max value validation
        """


        def __init__(self,
                     ctrl_prop     : ControlProperties,
                     parameter_dict: dict[str, Any]):
            """ initialize

            Args:
                ctrl_prop:      control properties
                parameter_dict: parameter dictionary for the range command
            """

            self.has_maximal_cond = True
            self.ctrl_prop        = ctrl_prop
            self.parameter_dict   = parameter_dict


        def get_max_value_state(self) -> tuple[bool, (bool | None)]:
            """ get the max value state

            Returns:
                has maximal condition, maximal value changed
            """

            return self.has_maximal_cond, None


        def get_value(self,
                      prop: ParameterProperty,
                      name: str) -> Any:
            """ get the value

            Args:
                prop: property
                name: name of the value, including the name of the sub value (tuple field name, geometry .X, ...)

            Returns:
                value
            """

            value = ParameterPropertyListUtil.get_item_value(prop, name)

            if ValueTypeUtil.is_string_input(value.value_type):
                return None

            if value.max_value == "":
                return None

            return StringEvaluate.eval(value.max_value, self.parameter_dict)


    @staticmethod
    def validate_minimal_value(ctrl_prop     : ControlProperties,
                               parameter_dict: dict[str, Any]) -> ValidateMinValueResult:
        """ validate, whether the minimal value of the control property has changed

        Args:
            ctrl_prop:      control property
            parameter_dict: parameter dictionary for the range command

        Returns:
            min value validation result
        """

        return AnyValueByTypeImpl.ValidateMinValueResult(ctrl_prop, parameter_dict)


    @staticmethod
    def validate_maximal_value(ctrl_prop     : ControlProperties,
                               parameter_dict: dict[str, Any]) -> ValidateMaxValueResult:
        """ validate, whether the maximal value of the control property has changed

        Args:
            ctrl_prop:      control property
            parameter_dict: parameter dictionary for the range command

        Returns:
            min value validation result
        """

        return AnyValueByTypeImpl.ValidateMaxValueResult(ctrl_prop, parameter_dict)


    @staticmethod
    def validate_for_min_value(prop            : ParameterProperty,
                               ctrl_prop       : ControlProperties,
                               min_value       : Any,
                               global_str_table: BuildingElementStringTable) -> bool:
        """ validate for the minimal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            min_value:        min value
            global_str_table: global string table

        Returns:
            palette update state
        """

        def test_min(value    : AnyValueByType,
                     min_value: Any) -> tuple[bool, Any]:
            """ test for the min value

            Args:
                value:     value
                min_value: min value

            Returns:
                min value assigned state, min value
            """

            if ValueTypeUtil.is_string_input(value.value_type) or not value.min_value:
                return False, value

            if value.value < min_value:
                new_value       = value.deep_copy()
                new_value.value = min_value

                return True, new_value

            return False, value

        return ValueTypes.ValueTypeUtils.MinMaxValidator.MinMaxValidator.validate_for_min_value(prop, ctrl_prop, min_value,
                                                                                                global_str_table, test_min)


    @staticmethod
    def validate_for_max_value(prop            : ParameterProperty,
                               ctrl_prop       : ControlProperties,
                               max_value       : Any,
                               global_str_table: BuildingElementStringTable) -> bool:
        """ validate for the maximal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            max_value:        min value
            global_str_table: global string table

        Returns:
            palette update state
        """

        def test_max(value    : AnyValueByType,
                     max_value: Any) -> tuple[bool, Any]:
            """ test for the max value

            Args:
                value:     value
                max_value: max value

            Returns:
                max value assigned state, max value
            """

            if ValueTypeUtil.is_string_input(value.value_type) or not value.max_value:
                return False, value

            if value.value > max_value:
                new_value       = value.deep_copy()
                new_value.value = max_value

                return True, new_value

            return False, value

        return ValueTypes.ValueTypeUtils.MinMaxValidator.MinMaxValidator.validate_for_max_value(prop, ctrl_prop, max_value,
                                                                                                global_str_table, test_max)


    @staticmethod
    def __get_value_for_type(value_type: str,
                             value     : Any) -> Any:
        """ get the value for the value type

        Args:
            value_type: value type
            value:      new value

        Returns:
            value
        """

        if isinstance(value, AnyValueByType):
            value = value.value

        value_str = str(value)

        if value_type == ParameterPropertyValueTypes.INTEGER:
            value_str = value_str.split(".", 1)[0]

        value_type_impl = ParameterPropertyValueTypesImpl.get_value_type_impl(value_type)

        return value_type_impl.get_value(value_str)

```

</details>