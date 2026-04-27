---
title: "BuildingElementTupleUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementTupleUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementTupleUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementTupleUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

Script for BuildingElementTupleUtil

## Abhängigkeiten

- `BuildingElementStringTable`
- `NemAll_Python_Utility`
- `ParameterProperty`
- `StringToValueConverter`
- `Utilities.SplitUtil`
- `ValueToStringConverter`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.TupleImpl`
- `collections`
- `collections.abc`

## Klassen

### `BuildingElementTupleUtil`

Implementation of the tuple utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_tuple_element_list` | `value_str: str, value_type: str, named_tuple_def: NamedTupleDef | None` | `list[tuple | None]` | Convert a tuple list string to a list of tuple elements  Args:     value_str       String with the values like                     "[(1.1|1);(2.2|2);(3.3|3)]"     value_type      Value type like                     "double,integer"     named_tuple_def Definition for the named tuple  Return:     list with the tuples from the string |
| `get_tuple_element` | `value_str: str, value_type: str, named_tuple_def: NamedTupleDef | None` | `tuple | None` | Convert a tuple string to a tuple element  Args:     value_str       String with the values like                     "(Point2D(100,200)|Point3D(300,400,500)|True|This is a string)"                     ((4|True)|3.5|(Text|False))     value_type      Value type like                     "tuple(point2d,point3d,checkbox,string)"                     namedtuple(tuple(integer,checkbox), double, tuple(string,checkbox))     named_tuple_def Definition for the named tuple  Returns:     tuple from the string |
| `__get_named_tuple_element` | `value_str: str, value_type: str, named_tuple_def: NamedTupleDef` | `tuple | None` | get the values for a named tuple element  Args:     value_str:       String with the values like     value_type:      Value type like     named_tuple_def: definition for the named tuple  Returns:     named tuple |
| `get_tuple_params` | `tuple_ele: tuple, str_table: BuildingElementStringTable` | `str` | Get the tuple parameter string from a tuple element  Args:     tuple_ele   tuple element     str_table   string table  Returns:     tuple as string with delimiter | like "(3|3.5|Point3D(100,200,300))" |
| `get_namedtuple_params_list` | `tuple_ele: NamedTupleDef` | `list[str]` | Get the tuple parameter string list from a named tuple element  Args:     tuple_ele   tuple element  Returns:     tuple as string list |
| `create_namedtuple_from_definition` | `param_prop: ParameterProperty` | `Callable | None` | create a named tuple from the definition  Args:     param_prop: parameter property  Returns:     named tuple function |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementTupleUtil
"""

from collections import namedtuple
from collections.abc import Callable

import NemAll_Python_Utility as AllplanUtil

from BuildingElementStringTable import BuildingElementStringTable
from ParameterProperty import ParameterProperty, NamedTupleDef
from StringToValueConverter import StringToValueConverter
from ValueToStringConverter import ValueToStringConverter

from Utilities.SplitUtil import SplitUtil

from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl
from ValueTypes.TupleImpl import TupleImpl

class BuildingElementTupleUtil():
    """ Implementation of the tuple utilities
    """

    @staticmethod
    def get_tuple_element_list(value_str      : str,
                               value_type     : str,
                               named_tuple_def: (NamedTupleDef | None)) -> list[(tuple | None)]:
        """ Convert a tuple list string to a list of tuple elements

        Args:
            value_str       String with the values like
                            "[(1.1|1);(2.2|2);(3.3|3)]"
            value_type      Value type like
                            "double,integer"
            named_tuple_def Definition for the named tuple

        Return:
            list with the tuples from the string
        """

        if value_str in {"[]", "[_]"}:
            return []

        value_str  = value_str.replace("[", "[\"").replace("]", "\"]").replace(";", "\",\"")
        value_list = eval(value_str)

        return [BuildingElementTupleUtil.get_tuple_element(value_str, value_type, named_tuple_def) for value_str in value_list]


    @staticmethod
    def get_tuple_element(value_str      : str,
                          value_type     : str,
                          named_tuple_def: (NamedTupleDef | None)) -> (tuple | None):
        """ Convert a tuple string to a tuple element

        Args:
            value_str       String with the values like
                            "(Point2D(100,200)|Point3D(300,400,500)|True|This is a string)"
                            ((4|True)|3.5|(Text|False))
            value_type      Value type like
                            "tuple(point2d,point3d,checkbox,string)"
                            namedtuple(tuple(integer,checkbox), double, tuple(string,checkbox))
            named_tuple_def Definition for the named tuple

        Returns:
            tuple from the string
        """

        value_str = value_str.strip()

        if named_tuple_def and named_tuple_def.field_names and value_str.find("=") != -1:
            return BuildingElementTupleUtil.__get_named_tuple_element(value_str, value_type, named_tuple_def)


        #----------------- get the values for the tuple

        ele_tuple = value_type.get_value_extend(value_str, 0, None)

        if not named_tuple_def:
            return ele_tuple


        #----------------- convert to named tuple

        if len(ele_tuple) < len(named_tuple_def.field_names):
            AllplanUtil.ShowMessageBox("Missing tuple value: " + value_str + " != " +
                                       ",".join(named_tuple_def.field_names), AllplanUtil.MB_OK)

            return None

        if len(ele_tuple) > len(named_tuple_def.field_names):
            AllplanUtil.ShowMessageBox("Missing tuple field name: " + value_str + " != " +
                                       ",".join(named_tuple_def.field_names), AllplanUtil.MB_OK)

            return None

        field_names     = []
        tuple_tuple_ele = ()

        for field_name, value in zip(named_tuple_def.field_names, ele_tuple):
            if field_name.find("(") != -1:
                tuple_data = field_name.rstrip(")").split("(")

                tuple_tuple_ele += (namedtuple(tuple_data[0], tuple_data[1].split(","))(*value), )

                field_names.append(tuple_data[0])
            else:
                field_names.append(field_name)
                tuple_tuple_ele += (value, )

        return namedtuple(named_tuple_def.typename, field_names)(*tuple_tuple_ele)


    @staticmethod
    def __get_named_tuple_element(value_str      : str,
                                  value_type     : str,
                                  named_tuple_def: NamedTupleDef) -> (tuple | None):
        """ get the values for a named tuple element

        Args:
            value_str:       String with the values like
            value_type:      Value type like
            named_tuple_def: definition for the named tuple

        Returns:
            named tuple
        """

        tuple_types, tuple_in_tuple = TupleImpl.get_value_types(value_type, True)

        tuple_str_values = TupleImpl.get_tuple_values(value_str, tuple_in_tuple)

        if len(tuple_types) < len(named_tuple_def.field_names):
            AllplanUtil.ShowMessageBox("Number of tuple value types and field names is different", AllplanUtil.MB_OK)

            return None


        #----------------- set the default values

        def init_tuple_values(tuple_type, tuple_def):
            def_tuple_values = []

            for tuple_value_type in TupleImpl.get_value_types(tuple_type, True)[0]:
                def_tuple_values.append(StringToValueConverter.get_value(ParameterPropertyValueTypesImpl.get_value_type_impl(tuple_value_type), ""))

            if tuple_def.find("(") == -1:
                return tuple(def_tuple_values)

            sub_data = tuple_def.split("(")

            sub_field_names = sub_data[1].rstrip(")").split(",")

            return namedtuple(sub_data[0], sub_field_names)(*def_tuple_values)

        tuple_values = [init_tuple_values(tuple_type, tuple_def) \
                        if tuple_type.startswith("tuple(") else StringToValueConverter.get_value(ParameterPropertyValueTypesImpl.get_value_type_impl(tuple_type), "")
                            for tuple_type, tuple_def in zip(tuple_types, named_tuple_def.field_names)]


        #----------------- get the values

        field_names = [field_name.split("(")[0] for field_name in named_tuple_def.field_names]

        for tuple_str_value in tuple_str_values if isinstance(tuple_str_values, list) else [tuple_str_values]:
            tuple_str_value = tuple_str_value.replace("&#124", "|")

            data = SplitUtil.split_string_with_bracket_parts(tuple_str_value, "=")

            if data[0] not in field_names:
                continue

            index = field_names.index(data[0])

            if tuple_types[index].startswith("tuple("):
                if named_tuple_def.field_names[index].find("(") == -1:
                    tuple_values[index] = BuildingElementTupleUtil.get_tuple_element(data[1], tuple_types[index], None)
                else:
                    sub_data = named_tuple_def.field_names[index].split("(")

                    sub_field_names = sub_data[1].rstrip(")").split(",")

                    tuple_values[index] = BuildingElementTupleUtil.get_tuple_element(data[1], tuple_types[index],
                                                                                     NamedTupleDef(sub_data[0], sub_field_names))
            else:
                tuple_values[index] = StringToValueConverter.get_value(ParameterPropertyValueTypesImpl.get_value_type_impl(tuple_types[index]),
                                                                       data[1])

        return namedtuple(named_tuple_def.typename, field_names)(*tuple_values)


    @staticmethod
    def get_tuple_params(tuple_ele: tuple,
                         str_table: BuildingElementStringTable) -> str:
        """
        Get the tuple parameter string from a tuple element

        Args:
            tuple_ele   tuple element
            str_table   string table

        Returns:
            tuple as string with delimiter | like "(3|3.5|Point3D(100,200,300))"
        """

        tuple_str = "("

        fields = getattr(tuple_ele, "_fields", None)

        for index, ele in enumerate(tuple_ele):
            if len(tuple_str) > 1:
                tuple_str += "|"

            if fields:
                tuple_str += fields[index] + "="

            tuple_ele_str = ValueToStringConverter.to_string_from_value(ele, ParameterPropertyValueTypesImpl.get_value_type_impl("tuple"), str_table)

            if isinstance(ele, tuple):
                tuple_str += BuildingElementTupleUtil.get_tuple_params(ele, str_table)
            else:
                tuple_str += tuple_ele_str.replace("|", "&#124")

        return tuple_str + ")"


    @staticmethod
    def get_namedtuple_params_list(tuple_ele: NamedTupleDef) -> list[str]:
        """
        Get the tuple parameter string list from a named tuple element

        Args:
            tuple_ele   tuple element

        Returns:
            tuple as string list
        """

        tuple_str_list = []

        for ele, name in zip(tuple_ele, tuple_ele._fields):
            tuple_ele_str = ValueToStringConverter.to_string_from_value(ele, ParameterPropertyValueTypesImpl.get_value_type_impl("tuple"), None)

            tuple_str_list.append(name + "=" + tuple_ele_str)

        return tuple_str_list


    @staticmethod
    def create_namedtuple_from_definition(param_prop: ParameterProperty) -> (Callable | None):
        """ create a named tuple from the definition

        Args:
            param_prop: parameter property

        Returns:
            named tuple function
        """

        named_tuple_def = param_prop.named_tuple_def

        if named_tuple_def is None:
            return None

        field_names = [field_name if field_name.find("(") == -1 else field_name.split("(")[0] for field_name in named_tuple_def.field_names]

        return namedtuple(named_tuple_def.typename, field_names)

```

</details>