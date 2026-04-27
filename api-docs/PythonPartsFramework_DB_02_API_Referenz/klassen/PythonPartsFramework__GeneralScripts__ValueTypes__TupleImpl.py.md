---
title: "TupleImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\TupleImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# TupleImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\TupleImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the tuple value type

## Abhängigkeiten

- `BuildingElementStringTable`
- `ControlProperties`
- `GeometryElements.CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `NemAll_Python_Palette`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`
- `Palette.PaletteControlByValueTypeCreator`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ParameterPropertyValueTypes`
- `ParameterPropertyValueTypesImpl`
- `StdReinfShapeBuilder.ReinforcementShapeProperties`
- `StringEvaluate`
- `StringToValueConverter`
- `Utilities.GeneralConstants`
- `Utilities.SplitUtil`
- `ValueTypeUtils.ControlMinMaxUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.ValueToStringUtil`
- `ValueTypes.ValueTypeUtils.MinMaxValidator`
- `__future__`
- `inspect`
- `typing`

## Klassen

### `TupleImpl`

implementation of the tuple value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `__insert_tuple_value` | `index: int, index_list: list[int], tuple_value: tuple[Any], name: str, value: Any` | `Any` | insert a value in a tuple  Args:     index:       index     index_list:  index list     tuple_value: tuple value     name:        name of the modified property     value:       property value  Returns:     new tuple value |
| `to_string` | `value: tuple[Any]` | `str` | convert the tuple to a string  Args:     value: new value  Returns:     tuple as string |
| `get_value` | `value_str: Any` | `tuple[Any]` | get the attribute from a string  Args:     value_str: value string  Returns:     tuple value |
| `get_value_extend` | `self, value_str: str, attribute_id: int | list[int], build_ele_str_table: BuildingElementStringTable` | `Any` | get the value from a string  Args:     value_str:           value from string     attribute_id:        attribute IDs     build_ele_str_table: string table  Returns:     attribute value |
| `get_value_types` | `value_types_str: str, remove_layout_value_types: bool` | `tuple[list[ParameterPropertyValueType], bool]` | Get the value types  Args:     value_types_str:           value types     remove_layout_value_types: remove the layout value types  Returns:     value types, tuple in tuple state |
| `get_tuple_values` | `value_str: str, tuple_in_tuple: bool` | `list[Any]` | get the tuples values  Args:     value_str:      value from string     tuple_in_tuple: tuple in tuple state  Returns:     tuple value |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, tuple_ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the area edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     tuple_ctrl_props:      tuple control properties     prop_pal_ctrl_service: property palette control service |
| `is_tuple_type` | `self, is_named_tuple: bool=False` | `bool` | test for tuple value type  Args:     is_named_tuple: test from named tuple  Returns:     tuple type state |
| `validate_minimal_value` | `ctrl_prop: ControlProperties, parameter_dict: dict[str, Any]` | `ValidateMinValueResult` | validate, whether the minimal value of the control property has changed  Args:     ctrl_prop:      control property     parameter_dict: parameter dictionary for the range command  Returns:     min value validation result |
| `validate_maximal_value` | `ctrl_prop: ControlProperties, parameter_dict: dict[str, Any]` | `ValidateMaxValueResult` | validate, whether the maximal value of the control property has changed  Args:     ctrl_prop:      control property     parameter_dict: parameter dictionary for the range command  Returns:     min value validation result |
| `validate_for_min_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, min_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the minimal value  Args:     prop:             property     ctrl_prop:        control properties     min_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `validate_for_max_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, max_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the maximal value  Args:     prop:             property     ctrl_prop:        control properties     max_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `__check_row_name` | `ctrl_props: ControlProperties, texts: list[str]` | `None` | check the row name  Args:     ctrl_props: control properties     texts:      control text |
| `__set_expander_row_name` | `value_type: ParameterPropertyValueType, prop: ParameterProperty, ctrl_props: ControlProperties, value_index: int, texts: list[str], index: int` | `tuple[bool, int]` | set the expander or row name  Args:     value_type:  value type     prop:        parameter property     ctrl_props:  control properties     value_index: value index     texts:       control text     index:       index  Returns:     name was set state, new value index |
| `__assign_by_index` | `items: list[Any], index: int, default: Any, replace_list_row: None | int=None` | `Any` | assign the indexed of the default value  Args:     items:            list items     index:            index     default:          default value     replace_list_row: replace $list_row with the defined row, None = nothing to replace  Returns:     value to assign |
| `__set_fixture` | `ele: Any, name: str, value: Any` | `bool` | Set the fixture value  Args:     ele:   element     name:  name of the modified property     value: property value  Returns:     set fixture state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the tuple value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING, cast

import inspect

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Palette as AllplanPalette
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_Utility as AllplanUtil

from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate
from StringToValueConverter import StringToValueConverter

from Utilities.GeneralConstants import GeneralConstants
from Utilities.SplitUtil import SplitUtil

from Palette.PaletteControlByValueTypeCreator import PaletteControlByValueTypeCreator
from Palette.WpfPaletteBuilder import WpfPaletteBuilder

import ValueTypes.ValueTypeUtils.MinMaxValidator

from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties

from .ValueTypeUtils.ControlMinMaxUtil import ControlMinMaxUtil
from .ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from .ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

from .GeometryElements.CoordinateValueUtil import CoordinateValueUtil

from .ParameterPropertyValueType import ParameterPropertyValueType
from .ParameterPropertyValueTypes import ParameterPropertyValueTypes
from .ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

if TYPE_CHECKING:
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService


class TupleImpl(ParameterPropertyValueType):
    """ implementation of the tuple value type
    """

    TUPLE = "tuple"

    GEOMETRY_DICT = {"Point2D"                     : AllplanGeo.Point2D,
                     "Point3D"                     : AllplanGeo.Point3D,
                     "Vector2D"                    : AllplanGeo.Vector2D,
                     "Vector3D"                    : AllplanGeo.Vector3D,
                     "FixtureProperties"           : AllplanPalette.FixtureProperties,
                     "BendingShapeType"            : AllplanReinf.BendingShapeType,
                     "MeshBendingDirection"        : AllplanReinf.MeshBendingDirection,
                     "ReinforcementShapeProperties": ReinforcementShapeProperties,}

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

        list_index, tuple_indexes = ParameterPropertyListUtil.get_tuple_list_indexes(name)


        #----------------- tuple

        if list_index == -1:
            prop.value = TupleImpl.__insert_tuple_value(0, tuple_indexes, prop.value, name, value)

            return False


        #----------------- tuple list

        prop.value[list_index] = TupleImpl.__insert_tuple_value(0, tuple_indexes, prop.value[list_index], name, value)

        return False


    @staticmethod
    def __insert_tuple_value(index      : int,
                             index_list : list[int],
                             tuple_value: tuple[Any],
                             name       : str,
                             value      : Any) -> Any:
        """ insert a value in a tuple

        Args:
            index:       index
            index_list:  index list
            tuple_value: tuple value
            name:        name of the modified property
            value:       property value

        Returns:
            new tuple value
        """

        tuple_index = index_list[index]

        part_value = tuple_value[tuple_index]

        if index == len(index_list) - 1:
            if name[-2: -1] == GeneralConstants.SUB_NAME_SEPARATOR:
                CoordinateValueUtil.set_coordinate_value(part_value, name, value)

                return tuple_value

            if GeneralConstants.SUB_NAME_SEPARATOR in name:
                TupleImpl.__set_fixture(part_value, name, value)

                return tuple_value

            return tuple_value[:tuple_index] + (value, ) + tuple_value[tuple_index + 1:]

        return tuple_value[:tuple_index] + (TupleImpl.__insert_tuple_value(index + 1, index_list,
                                                                           tuple_value[tuple_index], name, value), ) + \
               tuple_value[tuple_index + 1:]

    @staticmethod
    def to_string(value: tuple[Any]) -> str:
        """ convert the tuple to a string

        Args:
            value: new value

        Returns:
            tuple as string
        """

        return ValueToStringUtil.check_to_string_strip(value)


    @staticmethod
    def get_value(value_str: Any) -> tuple[Any]:
        """ get the attribute from a string

        Args:
            value_str: value string

        Returns:
            tuple value
        """

        res = eval(value_str, TupleImpl.GEOMETRY_DICT)

        return res


    def get_value_extend(self,
                         value_str          : str,
                         attribute_id       : (int | list[int]),
                         build_ele_str_table: BuildingElementStringTable) -> Any:
        """ get the value from a string

        Args:
            value_str:           value from string
            attribute_id:        attribute IDs
            build_ele_str_table: string table

        Returns:
            attribute value
        """

        tuple_types, tuple_in_tuple = TupleImpl.get_value_types(self, True)

        tuple_str_values = TupleImpl.get_tuple_values(value_str, tuple_in_tuple)

        tuple_str_values += [""] * (len(tuple_types) - len(tuple_str_values))

        value = tuple()

        for tuple_type, tuple_str_value in zip(tuple_types, tuple_str_values):
            if tuple_type.startswith("$"):
                value = value +  (None, )

                continue

            if not tuple_type:
                AllplanUtil.ShowMessageBox(f"TupleImple: Value type {tuple_type} doesn't exist!!!",  AllplanUtil.MB_OK)

                value = value +  (None, )

                continue

            value_str = tuple_str_value.replace("&#124", "|")

            data = SplitUtil.split_string_with_bracket_parts(value_str, "=")

            value_str = data[-1] if data else ""

            if tuple_type.is_tuple_type():
                value = value + (tuple_type.get_value_extend(value_str, attribute_id, build_ele_str_table),)
            else:
                value += (StringToValueConverter.get_value(tuple_type, value_str, build_ele_str_table, attribute_id),)

        return value


    @staticmethod
    def get_value_types(value_types_str          : str,
                        remove_layout_value_types: bool) -> tuple[list[ParameterPropertyValueType], bool]:
        """ Get the value types

        Args:
            value_types_str:           value types
            remove_layout_value_types: remove the layout value types

        Returns:
            value types, tuple in tuple state
        """

        value_types = value_types_str[value_types_str.find("(") + 1:].rstrip(")").replace(" ", "")

        if remove_layout_value_types:
            value_types = value_types.replace("separator,", "").replace("expander,", "").replace(",separator", "")

        tuple_in_tuple = value_types.startswith(f"{TupleImpl.TUPLE}(") or f",{TupleImpl.TUPLE}(" in value_types

        value_types = SplitUtil.split_string_with_bracket_parts(value_types, ",") if TupleImpl.TUPLE in value_types else \
                      value_types.split(",")

        return [ParameterPropertyValueTypesImpl.get_value_type_impl(value_type) for value_type in value_types], tuple_in_tuple


    @staticmethod
    def get_tuple_values(value_str     : str,
                         tuple_in_tuple: bool) -> list[Any]:
        """ get the tuples values

        Args:
            value_str:      value from string
            tuple_in_tuple: tuple in tuple state

        Returns:
            tuple value
        """

        if tuple_in_tuple:
            return SplitUtil.split_string_with_bracket_parts(value_str[1:-1], "|")

        if value_str.startswith("("):
            return value_str[1: -1].split("|")

        return value_str.lstrip("(").rstrip(")").split("|")


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,   #NOSONAR
                       prop                 : ParameterProperty,
                       tuple_ctrl_props     : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the area edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            tuple_ctrl_props:      tuple control properties
            prop_pal_ctrl_service: property palette control service
        """

        ctrl_props = tuple_ctrl_props.deep_copy()

        value_types, _ = TupleImpl.get_value_types(prop.value_type, False)

        value_lists     = ctrl_props.value_list.split(",")
        texts           = ctrl_props.text.split(GeneralConstants.TEXT_SEPARATOR)
        min_value_conds = ctrl_props.min_value_condition.split(",")
        max_value_conds = ctrl_props.max_value_condition.split(",")
        enable_conds    = ctrl_props.enable_condition.split(",")
        visible_conds   = ctrl_props.visible_condition.split(",")
        event_ids       = ctrl_props.event_id if isinstance(ctrl_props.event_id, list) else ctrl_props.event_id.split(",")
        attribute_ids   = prop.attribute_id_str.split(",")

        visible_fct = ctrl_props.visible_function if ctrl_props.visible_function and \
                                                     inspect.getfullargspec(ctrl_props.visible_function).args else None
        enable_fct  = ctrl_props.enable_function

        field_names = prop.named_tuple_def.field_names if prop.named_tuple_def else [""] * len(value_types)


        #----------------- check the row name

        TupleImpl.__check_row_name(ctrl_props, texts)


        #----------------- check the value list

        if len(value_lists) == 1 and value_lists[0].startswith("@"):
            value_lists = getattr(prop.value, value_lists[0][1:], "").split(",")

        value_index = 0

        no_value_types = ["separator", "expander"]

        row = prop_pal_ctrl_service.row


        #----------------- create the control for each tuple element

        for index, _value_type in enumerate(value_types):
            field_name        = _value_type if _value_type in no_value_types else field_names[value_index]
            value_type        = ParameterPropertyValueTypesImpl.get_value_type_impl(_value_type.replace(" ", ""))
            visible_condition = TupleImpl.__assign_by_index(visible_conds, index, "")

            set_name, value_index = TupleImpl.__set_expander_row_name(value_type, prop, ctrl_props, value_index, texts, index)

            if set_name:
                continue

            if not PaletteControlByValueTypeCreator.is_visible_row(visible_fct, visible_condition, row, field_name,
                                                                   prop_pal_ctrl_service.param_dict):
                value_index += 1
                continue

            data = ParameterProperty()

            data.name             = f"{prop.name}({value_index})"
            data.value_type       = value_type
            data.selected_value   = prop.selected_value
            data.attribute_id_str = TupleImpl.__assign_by_index(attribute_ids, value_index, "0")
            data.group_name       = prop.group_name


            #------------- set the value

            min_value_condition = ""
            max_value_condition = ""

            if value_type not in no_value_types:
                data.value          = prop.value[value_index]
                min_value_condition = TupleImpl.__assign_by_index(min_value_conds, value_index, "", row)
                max_value_condition = TupleImpl.__assign_by_index(max_value_conds, value_index, "", row)
                value_index += 1

            if value_type in {"stringcombobox", "text"} and str(data.value).isnumeric() and \
               (local_str_table := prop_pal_ctrl_service.build_ele.get_string_tables()[0]):
                data.value = local_str_table.get_entry(data.value)[0]


            #------------- set the control properties

            ctrl_props.value_list          = TupleImpl.__assign_by_index(value_lists, index, "")
            ctrl_props.min_value_condition = min_value_condition
            ctrl_props.max_value_condition = max_value_condition
            ctrl_props.text                = TupleImpl.__assign_by_index(texts, index, "")
            ctrl_props.enable_condition    = TupleImpl.__assign_by_index(enable_conds ,index, "", row)
            ctrl_props.enable_function     = None
            ctrl_props.visible_function    = None
            ctrl_props.visible_condition   = visible_condition


            #------------- set the event id

            if ParameterPropertyValueTypes.is_button_type(value_type):
                PaletteControlByValueTypeCreator.set_row_button_event_id(ctrl_props, value_type, event_ids[index], row,
                                                                         prop_pal_ctrl_service.param_dict,
                                                                         prop_pal_ctrl_service.is_visual_script)


            #------------- create the control

            data.selected_value = prop.selected_value

            if enable_fct:
                ctrl_props.enable_condition = str(enable_fct(row, field_name)) if row != -1 else str(enable_fct(field_name))

            ControlMinMaxUtil.set_min_max_values(ctrl_props, value_type, cast(int, data.attribute_id),
                                                 prop_pal_ctrl_service.param_dict)

            PaletteControlByValueTypeCreator.excecute(wpf_palette, data, ctrl_props, value_type, prop_pal_ctrl_service)


    def is_tuple_type(self,
                      is_named_tuple: bool = False) -> bool:
        """ test for tuple value type

        Args:
            is_named_tuple: test from named tuple

        Returns:
            tuple type state
        """

        return not (is_named_tuple and not self.startswith("namedtuple"))


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
                      _prop: ParameterProperty,
                      name : str) ->  ((Any | None) | list[(Any | None)]):
            """ get the value

            Args:
                _prop: property
                name:  name of the value, including the name of the sub value (tuple field name, geometry .X, ...)

            Returns:
                max value(s), None in case of empty condition
            """

            if not self.ctrl_prop.min_value_condition:
                return None

            if GeneralConstants.BRACKET_OPEN in name:
                row_index, tuple_indexes = ParameterPropertyListUtil.get_tuple_list_indexes(name)

                tuple_index = tuple_indexes[0]

                min_value_conditions = self.ctrl_prop.min_value_condition.split(",")

                if tuple_index >= len(min_value_conditions) or not min_value_conditions[tuple_index]:
                    return None

                min_value = StringEvaluate.eval(min_value_conditions[tuple_index].replace(GeneralConstants.LIST_ROW_KEYWORD,
                                                                                          str(row_index)), self.parameter_dict)

                if min_value == "":
                    return None

                return min_value


            #------------- get all max values

            row_index = ParameterPropertyListUtil.get_list_index(name)

            min_values = []

            for min_value_condition in self.ctrl_prop.min_value_condition.split(","):
                if (min_value := StringEvaluate.eval(min_value_condition.replace(GeneralConstants.LIST_ROW_KEYWORD,
                                                                                 str(row_index)), self.parameter_dict)) == "":
                    min_values.append(None)
                else:
                    min_values.append(min_value)

            return min_values


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
                      _prop: ParameterProperty,
                      name : str) -> ((Any | None) | list[(Any | None)]):
            """ get the value

            Args:
                _prop: property
                name:  name of the value, including the name of the sub value (tuple field name, geometry .X, ...)

            Returns:
                max value(s), None in case of empty condition
            """

            if not self.ctrl_prop.max_value_condition:
                return None


            #------------- get the min value for the sub item

            if GeneralConstants.BRACKET_OPEN in name:
                row_index, tuple_indexes = ParameterPropertyListUtil.get_tuple_list_indexes(name)

                tuple_index = tuple_indexes[0]

                max_value_conditions = self.ctrl_prop.max_value_condition.split(",")

                if tuple_index >= len(max_value_conditions) or not max_value_conditions[tuple_index]:
                    return None

                max_value = StringEvaluate.eval(max_value_conditions[tuple_index].replace("$list_row", str(row_index)), self.parameter_dict)

                if max_value == "":
                    return None

                return max_value


            #------------- get all max values

            row_index = ParameterPropertyListUtil.get_list_index(name)

            max_values = []

            for max_value_condition in self.ctrl_prop.max_value_condition.split(","):
                if (max_value := StringEvaluate.eval(max_value_condition.replace("$list_row", str(row_index)), self.parameter_dict)) == "":
                    max_values.append(None)
                else:
                    max_values.append(max_value)

            return max_values


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

        return TupleImpl.ValidateMinValueResult(ctrl_prop, parameter_dict)


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

        return TupleImpl.ValidateMaxValueResult(ctrl_prop, parameter_dict)


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

        def test_min(value     : Any,
                     min_values: Any) -> tuple[bool, Any]:
            """ test for the min value

            Args:
                value:      value
                min_values: minimal values for the tuple parts

            Returns:
                min value assigned state, min value
            """

            if min_values is None:
                return False, value

            use_min = False

            for index, min_value in enumerate(min_values):
                if min_value is None:
                    continue

                if value[index] < min_value:
                    value = value[:index] + (min_value, ) + value[index + 1:]

                    use_min = True

            return use_min, value

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

        def test_max(value    : Any,
                     max_values: Any) -> tuple[bool, Any]:
            """ test for the max value

            Args:
                value:     value
                max_values: max values for the tuple parts

            Returns:
                max value assigned state, max value
            """

            if max_values is None:
                return False, value

            use_max = False

            for index, max_value in enumerate(max_values):
                if max_value is None:
                    continue

                if value[index] > max_value:
                    value = value[:index] + (max_value, ) + value[index + 1:]

                    use_max = True

            return use_max, value

        return ValueTypes.ValueTypeUtils.MinMaxValidator.MinMaxValidator.validate_for_max_value(prop, ctrl_prop, max_value,
                                                                                                global_str_table, test_max)



    @staticmethod
    def __check_row_name(ctrl_props: ControlProperties,
                         texts     : list[str]):
        """ check the row name

        Args:
            ctrl_props: control properties
            texts:      control text
        """
        if len(texts) == 1:
            if not ctrl_props.row_name:
                ctrl_props.row_name = ctrl_props.text

            texts = []

        elif ctrl_props.text:
            ctrl_props.row_name = ""


    @staticmethod
    def __set_expander_row_name(value_type : ParameterPropertyValueType,
                                prop       : ParameterProperty,
                                ctrl_props : ControlProperties,
                                value_index: int,
                                texts      : list[str],
                                index      : int) -> tuple[bool, int]:
        """ set the expander or row name

        Args:
            value_type:  value type
            prop:        parameter property
            ctrl_props:  control properties
            value_index: value index
            texts:       control text
            index:       index

        Returns:
            name was set state, new value index
        """

        match value_type:
            case ParameterPropertyValueTypes.EXPANDER:
                ctrl_props.expander_name = TupleImpl.__assign_by_index(texts, index, "")

                return True, value_index

            case ParameterPropertyValueTypes.DISPLAY_TEXT:
                ctrl_props.row_name = prop.value[value_index]

                return True, value_index + 1

        return False, value_index


    @staticmethod
    def __assign_by_index(items           : list[Any],
                          index           : int,
                          default         : Any,
                          replace_list_row: (None | int) = None) -> Any:
        """ assign the indexed of the default value

        Args:
            items:            list items
            index:            index
            default:          default value
            replace_list_row: replace $list_row with the defined row, None = nothing to replace

        Returns:
            value to assign
        """

        item = items[index] if index < len(items) else default

        if replace_list_row is None:
            return  item

        return item.replace(GeneralConstants.LIST_ROW_KEYWORD, str(replace_list_row))


    @staticmethod
    def __set_fixture(ele  : Any,
                      name : str,
                      value: Any) -> bool:
        """ Set the fixture value

        Args:
            ele:   element
            name:  name of the modified property
            value: property value

        Returns:
            set fixture state
        """

        if name.endswith(".PathShortcut"):
            ele.PathShortcut = value
            return True

        if name.endswith(".Group"):
            ele.Group = value
            return True

        if name.endswith(".Element"):
            ele.Element = value
            return True

        return False

```

</details>