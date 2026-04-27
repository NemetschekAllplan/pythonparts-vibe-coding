---
title: "ParameterProperty"
source: "PythonPartsFramework\GeneralScripts\ParameterProperty.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
related:
  -
last_updated: "2026-02-20"
---


# ParameterProperty

> **Pfad:** `PythonPartsFramework\GeneralScripts\ParameterProperty.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`

## Übersicht

General script for parameter properties

## Abhängigkeiten

- `ValueTypes.ParameterPropertyValueType`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.ValueTypeUtils.ComboBoxValueListUtil`
- `ValueTypes.ValueTypeUtils.ValueType`
- `__future__`
- `collections`
- `copy`
- `enum`
- `os`
- `typing`

## Klassen

### `ParameterProperty`

Definition of class ParameterProperty
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize  |
| `__repr__` | `self` | `str` | Print class information  Returns:     parameter property as string |
| `name` | `self` | `str` | Get the name of the property  Returns:     name of the property. |
| `name` | `self, name: str` | `None` | Set the name of the property  Args:     name: name of the modified property |
| `group_name` | `self` | `str` | Get the group name of the property  Returns:     name of the property. |
| `group_name` | `self, name: str` | `None` | Set the group name of the property  Args:     name: name of the modified property |
| `value` | `self` | `Any` | Get the value of the property  Returns:     value of the property. |
| `value` | `self, value: Any` | `None` | Set the value of the property  Args:     value: new value |
| `__set_varied_value` | `self, value: Any` | `None` | Set the varied value of the property  Args:     value: new value |
| `get_unique_value` | `self, default_value: Any` | `Any` | Get the unique value of the property  Args:     default_value: default value  Returns:     value of the property if not varied, otherwise the default value. |
| `is_varied_value` | `self` | `bool | None` | Get the varied value state of the property  Returns:     varied value state of the property. |
| `selected_value` | `self` | `Any` | Get the selected value of the property  Returns:     value of the property. |
| `selected_value` | `self, value: Any` | `None` | Set the selected value of the property  Args:     value: new value |
| `attribute_id` | `self` | `int | list[int]` | Get the attribute id of the property  Returns:     attribute id of the property. |
| `attribute_id` | `self, attribute_id: int` | `None` | Set the attribute id of the property  Args:     attribute_id: attribute ID |
| `attribute_id_str` | `self` | `str` | Get the attribute id string of the property  Returns:     attribute id of the property. |
| `attribute_id_str` | `self, attribute_id_str: str` | `None` | Set the attribute id string of the property  Args:     attribute_id_str: new attribute id |
| `value_type` | `self` | `ParameterPropertyValueType` | Get the value type of the property  Returns:     value type. |
| `value_type` | `self, value_type: str` | `None` | Set the value type of the property  Args:     value_type: new value type. |
| `persistent` | `self` | `Persistent` | Get the persistent state of the property  Returns:     persistent state (save in the PythonPart data). |
| `persistent` | `self, persistent: Persistent` | `None` | Set the persistent state of the property  Args:     persistent: property is persistent (save in the PythonPart data). |
| `input_type` | `self` | `InputType` | Getter for input type parameter  Returns:     Input type of parameter property. |
| `input_type` | `self, input_type: InputType` | `None` | Setter to input type property  Args:     input_type (InputType): Type of input |
| `dimensions` | `self` | `str` | Get the dimensions of the property in case of a list  Returns:     dimensions. |
| `dimensions` | `self, dimensions: str` | `None` | Set the dimensions of the property in case of a list  Args:     dimensions: list dimensions. |
| `list_state` | `self` | `int` | Get the list as block state  Returns:     returns |
| `list_state` | `self, list_state: int` | `None` | Set the list as block state  Args:     list_state: description |
| `list_reverse` | `self` | `bool` | Get the list reverse state  Returns:     returns |
| `list_reverse` | `self, is_list_reverse: bool` | `None` | Set the list reverse state  Args:     is_list_reverse: description |
| `list_squeeze` | `self` | `bool` | Get the list squeeze state  Returns:     returns |
| `list_squeeze` | `self, is_list_squeeze: bool` | `None` | Set the list squeeze state  Args:     is_list_squeeze: description |
| `is_modified` | `self` | `bool` | Get the modified state  Returns:     returns |
| `is_modified` | `self, is_modified: bool` | `None` | Set the modified state  Args:     is_modified: description |
| `reset_modified` | `self` | `None` | Reset the is_modified state          |
| `reset` | `self` | `None` | reset the parameter property          |
| `exclude_identical` | `self` | `bool` | Get the exclude identical state  If True, the parameter is not used for checking identical PythonParts  Returns:     returns |
| `exclude_identical` | `self, exclude_identical: bool` | `None` | Set the exclude identical state  If True, the parameter is not used for checking identical PythonParts  Args:     exclude_identical: description |
| `named_tuple_def` | `self` | `NamedTupleDef | None` | Get the named tuple definition  Returns:     named tuple definition |
| `set_named_tuple_def` | `self, typename: str, field_names: list[str]` | `None` | Set the named tuple definition  Args:     typename:    description     field_names: description |
| `enum_dict` | `self` | `dict[int, IntEnum]` | Get the enumeration list for the input values  Returns:     enumeration list |
| `enum_dict` | `self, enum_dict: dict[int, IntEnum]` | `None` | Set the enumeration list for the input values  Args:     enum_dict: enumeration list for the input values |
| `value_list_util` | `self` | `ComboBoxValueListUtil | None` | Get the combo box value list utility  Returns:     combo box value list utility |
| `value_list_util` | `self, value_list_util: ComboBoxValueListUtil | None` | `None` | Set the combo box value list utility  Args:     value_list_util: combo box value list utility |
| `deep_copy` | `self` | `ParameterProperty` | deep copy of the parameter values  Returns:     copied parameter property |
| `copy_value` | `self, value: Any` | `Any` | copy the value  Args:     value: new value  Returns:     copied value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" General script for parameter properties
"""

# pylint: disable="too-many-instance-attributes"

from __future__ import annotations

from enum import IntEnum

from typing import Any

import copy
import enum
import os

from collections import namedtuple

from ValueTypes.ParameterPropertyValueType import ParameterPropertyValueType
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl
from ValueTypes.ValueTypeUtils.ComboBoxValueListUtil import ComboBoxValueListUtil
from ValueTypes.ValueTypeUtils.ValueType import ValueType

NamedTupleDef = namedtuple("NamedTupleDef", ["typename" ,"field_names"])

class ParameterProperty:
    """ Definition of class ParameterProperty
    """

    class Persistent(enum.IntEnum):
        """ Definition of class PersistentType
        """

        NO                 = 0
        MODEL_AND_FAVORITE = 1
        MODEL              = 2
        FAVORITE           = 3


    class InputType(enum.IntEnum):
        """ Class used to define the type of inputs
        """

        MANDATORY = 0
        OPTIONAL  = 1


    def __init__(self):
        """ initialize """

        self.__name              : str                            = ''
        self.__group_name        : str                            = ""
        self.__value_type        : ParameterPropertyValueType     = ParameterPropertyValueType(ValueType("", "", False, False))
        self.__value             : Any                            = 0.
        self.__selected_value    : Any                            = 0
        self.__attribute_id_str  : str                            = "0"
        self.__persistent        : ParameterProperty.Persistent   = ParameterProperty.Persistent.NO
        self.__input_type        : ParameterProperty.InputType    = ParameterProperty.InputType.OPTIONAL
        self.__dimensions        : str                            = ""
        self.__list_state        : int                            = 0
        self.__list_reverse      : bool                           = False
        self.__list_squeeze      : bool                           = True
        self.__is_modified       : bool                           = False
        self.__exclude_identical : bool                           = False
        self.__named_tuple_def   : (NamedTupleDef | None)         = None
        self.__enum_dict         : dict[int, IntEnum]             = {}
        self.__value_list_util   : (ComboBoxValueListUtil | None) = None
        self.__is_varied_value   : (bool | None)                  = None

    def __repr__(self) -> str:
        """ Print class information

        Returns:
            parameter property as string
        """
        return f"<{self.__class__.__name__}>\n" \
               f"name:              {self.__name}\n" \
               f"group_name:        {self.__group_name}\n" \
               f"value_type:        {self.__value_type}\n" \
               f"value:             {self.__value}\n" \
               f"selected_value:    {self.__selected_value}\n" \
               f"attribute_id_str:  {self.__attribute_id_str}\n" \
               f"persistent:        Persistent.{str(self.__persistent.name)}\n" \
               f"input_type:        InputType.{str(self.__input_type.name)}\n" \
               f"dimension:         {self.__dimensions}\n" \
               f"list state:        {self.__list_state}\n" \
               f"list reverse:      {self.__list_reverse}\n" \
               f"list squeeze:      {self.__list_squeeze}\n" \
               f"is_modified:       {self.__is_modified}\n" \
               f"exclude_identical: {self.__exclude_identical}\n" \
               f"named_tuple_def:   {self.__named_tuple_def}\n" \
               f"enum_dict:         {self.__enum_dict}\n" \
               f"value_list_util:   {str(self.__value_list_util)}\n"

    @property
    def name(self) -> str:
        """ Get the name of the property

        Returns:
            name of the property.
        """
        return self.__name

    @name.setter
    def name(self,
             name: str):
        """ Set the name of the property

        Args:
            name: name of the modified property
        """
        self.__name = name

    @property
    def group_name(self) -> str:
        """ Get the group name of the property

        Returns:
            name of the property.
        """
        return self.__group_name

    @group_name.setter
    def group_name(self,
                   name: str):
        """ Set the group name of the property

        Args:
            name: name of the modified property
        """
        self.__group_name = name

    @property
    def value(self) -> Any:
        """ Get the value of the property

        Returns:
            value of the property.
        """
        return self.__value

    @value.setter
    def value(self,
              value: Any):
        """ Set the value of the property

        Args:
            value: new value
        """

        if not self.is_modified:
            self.__is_modified = value != self.__value

        self.__value           = value
        self.__is_varied_value = False

    def __set_varied_value(self,
                           value: Any):
        """ Set the varied value of the property

        Args:
            value: new value
        """

        if self.__is_varied_value is None:
            self.__is_varied_value = False

        elif not self.__is_varied_value and self.__value != value:
            self.__is_varied_value = True

            return

        self.__value = value

    varied_value = property(fset = __set_varied_value)

    def get_unique_value(self,
                         default_value: Any) -> Any:
        """ Get the unique value of the property

        Args:
            default_value: default value

        Returns:
            value of the property if not varied, otherwise the default value.
        """

        return default_value if self.is_varied_value else self.value

    @property
    def is_varied_value(self) -> (bool | None):
        """ Get the varied value state of the property

        Returns:
            varied value state of the property.
        """
        return self.__is_varied_value

    @property
    def selected_value(self) -> Any:
        """ Get the selected value of the property

        Returns:
            value of the property.
        """
        return self.__selected_value

    @selected_value.setter
    def selected_value(self,
                       value: Any):
        """ Set the selected value of the property

        Args:
            value: new value
        """
        self.__selected_value = value

    @property
    def attribute_id(self) -> (int | list[int]):
        """ Get the attribute id of the property

        Returns:
            attribute id of the property.
        """

        if self.__attribute_id_str == "0":          # pylint: disable=magic-value-comparison
            return 0

        return eval(self.__attribute_id_str)        # pylint: disable=eval-used

    @attribute_id.setter
    def attribute_id(self,
                     attribute_id: int):
        """ Set the attribute id of the property

        Args:
            attribute_id: attribute ID
        """

        self.__attribute_id_str = str(attribute_id)


    @property
    def attribute_id_str(self) -> str:
        """ Get the attribute id string of the property

        Returns:
            attribute id of the property.
        """
        return self.__attribute_id_str

    @attribute_id_str.setter
    def attribute_id_str(self,
                         attribute_id_str: str):
        """ Set the attribute id string of the property

        Args:
            attribute_id_str: new attribute id
        """
        self.__attribute_id_str = attribute_id_str

    @property
    def value_type(self) -> ParameterPropertyValueType:
        """ Get the value type of the property

        Returns:
            value type.
        """
        return self.__value_type

    @value_type.setter
    def value_type(self,
                   value_type: str):
        """ Set the value type of the property

        Args:
            value_type: new value type.
        """
        self.__value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(value_type)

    @property
    def persistent(self) -> Persistent:
        """ Get the persistent state of the property

        Returns:
            persistent state (save in the PythonPart data).
        """
        return self.__persistent

    @persistent.setter
    def persistent(self,
                   persistent: Persistent):
        """ Set the persistent state of the property

        Args:
            persistent: property is persistent (save in the PythonPart data).
        """
        self.__persistent = persistent

    @property
    def input_type(self) -> InputType:
        """  Getter for input type parameter

        Returns:
            Input type of parameter property.
        """
        return self.__input_type

    @input_type.setter
    def input_type(self,
                   input_type: InputType):
        """Setter to input type property

        Args:
            input_type (InputType): Type of input
        """
        self.__input_type = input_type

    @property
    def dimensions(self) -> str:
        """ Get the dimensions of the property in case of a list

        Returns:
            dimensions.
        """
        return self.__dimensions

    @dimensions.setter
    def dimensions(self,
                   dimensions: str):
        """ Set the dimensions of the property in case of a list

        Args:
            dimensions: list dimensions.
        """
        self.__dimensions = dimensions

    @property
    def list_state(self) -> int:
        """ Get the list as block state

        Returns:
            returns
        """

        return self.__list_state

    @list_state.setter
    def list_state(self,
                   list_state: int):
        """ Set the list as block state

        Args:
            list_state: description
        """

        self.__list_state = list_state

    @property
    def list_reverse(self) -> bool:
        """ Get the list reverse state

        Returns:
            returns
        """

        return self.__list_reverse

    @list_reverse.setter
    def list_reverse(self,
                     is_list_reverse: bool):
        """ Set the list reverse state

        Args:
            is_list_reverse: description
        """

        self.__list_reverse = is_list_reverse

    @property
    def list_squeeze(self) -> bool:
        """ Get the list squeeze state

        Returns:
            returns
        """

        return self.__list_squeeze

    @list_squeeze.setter
    def list_squeeze(self,
                     is_list_squeeze: bool):
        """ Set the list squeeze state

        Args:
            is_list_squeeze: description
        """

        self.__list_squeeze = is_list_squeeze

    @property
    def is_modified(self) -> bool:
        """ Get the modified state

        Returns:
            returns
        """

        return self.__is_modified

    @is_modified.setter
    def is_modified(self,
                    is_modified: bool):
        """ Set the modified state

        Args:
            is_modified: description
        """

        self.__is_modified = is_modified

    def reset_modified(self):
        """ Reset the is_modified state
        """

        self.__is_modified = False

    def reset(self):
        """ reset the parameter property
        """

        self.__is_modified     = False
        self.__is_varied_value = None

    @property
    def exclude_identical(self) -> bool:
        """ Get the exclude identical state

        If True, the parameter is not used for checking identical PythonParts

        Returns:
            returns
        """

        return self.__exclude_identical

    @exclude_identical.setter
    def exclude_identical(self,
                          exclude_identical: bool):
        """ Set the exclude identical state

        If True, the parameter is not used for checking identical PythonParts

        Args:
            exclude_identical: description
        """

        self.__exclude_identical = exclude_identical

    @property
    def named_tuple_def(self) -> (NamedTupleDef | None):
        """ Get the named tuple definition

        Returns:
            named tuple definition
        """

        return self.__named_tuple_def

    def set_named_tuple_def(self,
                            typename   : str,
                            field_names: list[str]):
        """ Set the named tuple definition

        Args:
            typename:    description
            field_names: description
        """

        self.__named_tuple_def = NamedTupleDef(typename, field_names)

    @property
    def enum_dict(self) -> dict[int, IntEnum]:
        """ Get the enumeration list for the input values

        Returns:
            enumeration list
        """

        return self.__enum_dict

    @enum_dict.setter
    def enum_dict(self,
                  enum_dict: dict[int, IntEnum]):
        """ Set the enumeration list for the input values

        Args:
            enum_dict: enumeration list for the input values
        """

        self.__enum_dict = enum_dict

    @property
    def value_list_util(self) -> (ComboBoxValueListUtil | None):
        """ Get the combo box value list utility

        Returns:
            combo box value list utility
        """

        return self.__value_list_util

    @value_list_util.setter
    def value_list_util(self,
                        value_list_util: (ComboBoxValueListUtil | None)):
        """ Set the combo box value list utility

        Args:
            value_list_util: combo box value list utility
        """

        self.__value_list_util = value_list_util

    def deep_copy(self) -> ParameterProperty:
        """ deep copy of the parameter values

        Returns:
            copied parameter property
        """

        prop = ParameterProperty()

        prop.name              = self.name
        prop.group_name        = self.group_name
        prop.value_type        = self.value_type
        prop.selected_value    = self.selected_value
        prop.persistent        = self.persistent
        prop.dimensions        = self.dimensions
        prop.list_state        = self.list_state
        prop.list_reverse      = self.list_reverse
        prop.list_squeeze      = self.list_squeeze
        prop.is_modified       = self.is_modified
        prop.exclude_identical = self.exclude_identical
        prop.enum_dict         = dict(self.enum_dict)
        prop.value_list_util   = self.value_list_util

        if self.named_tuple_def is not None:
            prop.set_named_tuple_def(*self.named_tuple_def)

        prop.value = self.copy_value(self.value)

        return prop


    def copy_value(self,
                   value: Any) -> Any:
        """ copy the value

        Args:
            value: new value

        Returns:
            copied value
        """

        if value is None:
            return value

        if isinstance(value, list):
            return [self.copy_value(item) for item in value]

        if ParameterPropertyValueTypes.NAMED_TUPLE in self.value_type:
            if self.__named_tuple_def is not None:
                field_names = [field_name.split("(")[0] for field_name in self.__named_tuple_def.field_names]

                return namedtuple(self.__named_tuple_def.typename, field_names)(*value)

            return None

        match self.value_type:
            case ParameterPropertyValueTypes.ATTRIBUTE | \
                 ParameterPropertyValueTypes.DATE:
                return value

            case ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE:
                return copy.deepcopy(value)

            case _ if (deep_copy := getattr(value, "deep_copy", None)) is not None:
                return deep_copy()

            case _:
                try:
                    return type(value)(value)

                except:
                    os.system("color")

                    print("\033[91m")
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print()
                    print(f"Cannot create a copy of value {value} of type {type(value)}")
                    print()
                    print(f"The defined value type is: {self.value_type}")
                    print()
                    print(f"Please check the value assigned to the parameter {self.name}.")
                    print("Maybe a conversion of the value is missing.")
                    print()
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("\033[00m")
                    return value

```

</details>