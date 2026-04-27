---
title: "BuildingElementComposite"
source: "PythonPartsFramework\GeneralScripts\BuildingElementComposite.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementComposite

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementComposite.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the build element composite

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementCompositeData`
- `BuildingElementCompositeReader`
- `BuildingElementParameterPropertyUtil`
- `BuildingElementValueUtil`
- `NemAll_Python_Geometry`
- `NemAll_Python_Utility`
- `ParameterProperty`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `re`
- `sys`
- `traceback`
- `typing`

## Klassen

### `BuildingElementComposite`

Implementation of class BuildingElementComposite
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_build_ele_index` | `self, build_ele_id: str` | `int` | get the index of the building element by the ID  Args:     build_ele_id: id fo find  Returns:     index of the ID |
| `get_values_from_list` | `value_list: list[Any], sub_name: str` | `list[Any]` | get the values from a list  Args:     value_list: value list     sub_name:   sub value name  Returns:     value |
| `connect_building_element_values` | `self, build_ele_list: list[BuildingElement], end_index: int=-1, check_modified: bool=True` | `bool` | Connect the values of the building element from the element data  Return: the connection is modified: True/False  Args:     build_ele_list: Building element list     end_index:      end index     check_modified: check modified state  Returns:     modified state |
| `set_connection_persistence` | `self, build_ele_list: list[BuildingElement]` | `None` | Set the persistence for the connected parameter  Args:     build_ele_list: building element list |
| `set_element_visible` | `self, ele_index: int, value: str` | `None` | Set the visible state for the element  Args:     ele_index: element index     value:     value |
| `is_element_visible` | `self, ele_index: int, build_ele_list: list[BuildingElement]` | `bool` | Check for a visible element  Return: the element is visible: True/False  Args:     ele_index:      element index     build_ele_list: Building element list  Returns:     element visible state |
| `get_element_palette_data` | `self, element_id: str` | `PaletteData` | Set the palette data for the element (control index, page text, expander text)  Args:     element_id: element ID  Returns:     palette data |
| `get_script` | `self, sub_ele_index: int` | `object` | Get the script of the sub element  Return: script  Args:     sub_ele_index: Index of the sub element  Returns:     script name |
| `get_sub_element_name` | `self, sub_ele_index: int` | `str` | Get the name of the sub element  Return: name  Args:     sub_ele_index: Index of the sub element  Returns:     sub element name |
| `get_composite_build_ele_list` | `self, sub_ele_index: int, build_ele_list: list[BuildingElement]` | `tuple[list[BuildingElement], list[int]]` | Get a tuple with the       - list with the sub building elements       - list with the indices of the sub building elements  Args:     sub_ele_index:  Index of the sub element     build_ele_list: list with the building elements  Returns:     tuple with the lists |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the build element composite
"""

# pylint: disable=bare-except

from typing import Any

import sys
import re
import traceback

from BuildingElementCompositeReader import PaletteData

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Utility as AllplanUtil

import BuildingElementParameterPropertyUtil as PropertyUtil
import BuildingElementValueUtil as ValueUtil

from BuildingElement import BuildingElement
from BuildingElementCompositeData import BuildingElementCompositeData
from ParameterProperty import ParameterProperty

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl


class BuildingElementComposite(BuildingElementCompositeData):
    """ Implementation of class BuildingElementComposite
    """

    def get_build_ele_index(self,
                            build_ele_id: str) -> int:
        """ get the index of the building element by the ID

        Args:
            build_ele_id: id fo find

        Returns:
            index of the ID
        """

        return next((i + 1 for i, sub_ele_id in enumerate(self.sub_ele_id) if sub_ele_id == build_ele_id), -1)


    @staticmethod
    def get_values_from_list(value_list: list[Any],
                             sub_name  : str) -> list[Any]:
        """ get the values from a list

        Args:
            value_list: value list
            sub_name:   sub value name

        Returns:
            value
        """

        result_values = []

        for row_value in value_list:
            if isinstance(row_value, list):
                result_values.append(BuildingElementComposite.get_values_from_list(row_value, sub_name))
            else:
                result_values.append(getattr(row_value, sub_name, None))

        return result_values


    def connect_building_element_values(self,
                                        build_ele_list: list[BuildingElement],
                                        end_index     : int = -1,
                                        check_modified: bool = True) -> bool:
        """ Connect the values of the building element from the element data

        Return: the connection is modified: True/False

        Args:
            build_ele_list: Building element list
            end_index:      end index
            check_modified: check modified state

        Returns:
            modified state
        """


        #----------------- create the parameter dictionary for the evaluation of the connections

        param_dict = {"build_ele_list" : build_ele_list,
                      "AllplanGeo" : AllplanGeo,
                      "get_values_from_list" : BuildingElementComposite.get_values_from_list}

        modified = False

        if end_index == -1:
            start_index = 0
            end_index   = len(self.sub_ele_constraints)
        else:
            start_index = end_index - 1

        for index in range(start_index, end_index):
            for constraint in self.sub_ele_constraints[index]:
                if constraint.value  and  (constraint.condition == "True"  or  eval(constraint.condition, param_dict)):
                    value_name = PropertyUtil.get_property_value_name(constraint.name)

                    if not (prop := build_ele_list[index + 1].get_property(value_name)):
                        msg_text = "Constraint with name " + value_name + " not found!!!"

                        print()
                        print(msg_text)

                        AllplanUtil.ShowMessageBox(msg_text, AllplanUtil.MB_OK)

                        continue

                    current_build_ele = build_ele_list[index + 1]

                    try:                                                    # pylint: disable=too-many-try-statements
                        new_val = eval(constraint.value, param_dict)

                        if constraint.value_type == ParameterPropertyValueTypes.ANY_VALUE_BY_TYPE:
                            new_val = new_val.value

                        input_build_ele_list = re.findall(r"build_ele_list\[\d*\]", constraint.value)

                        for input_build_ele in input_build_ele_list:
                            current_build_ele.skip_eval = current_build_ele.skip_eval or eval(input_build_ele).skip_eval

                    except:
                        msg_text = "Exception during connection of the building elements, eval: " + constraint.value + "\n\n" + \
                                   str(sys.exc_info()[1])

                        print()
                        print(msg_text)
                        print()
                        traceback.print_exc()

                        AllplanUtil.ShowMessageBox(msg_text, AllplanUtil.MB_OK)

                        continue

                    if hasattr(current_build_ele, "connected_params"):
                        current_build_ele.connected_params[prop.name] = True

                    #----- convert a tuple value to a geometry value

                    if isinstance(new_val, tuple) and not prop.value_type.is_tuple_type() and \
                       prop.value_type != ParameterPropertyValueTypes.LIST:
                        value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(prop.value_type)

                        if value_type.has_impl:
                            new_val = value_type.get_value(str(new_val))

                    if check_modified  and  prop.value != new_val:
                        modified = True

                    try:
                        PropertyUtil.set_property_value(prop, constraint.name, new_val)

                        if isinstance(new_val, int):
                            ValueUtil.update_list_size(constraint.name, new_val, build_ele_list[index + 1])

                    except:
                        msg_text = "Exception during connection of the building elements, assign to value: " + constraint.name + "\n\n" + \
                                   str(sys.exc_info()[1])

                        print()
                        print(msg_text)
                        print()
                        traceback.print_exc()

                        AllplanUtil.ShowMessageBox(msg_text, AllplanUtil.MB_OK)

                        continue

                    if constraint.name.find(".") == -1:
                        prop.persistent = ParameterProperty.Persistent.NO


                    #----------------- set the value type when $dynamic

                    if constraint.value_type:
                        value_types = eval(constraint.value_type)

                        if isinstance(value_types, list):
                            prop.value_type = value_types[0]
                        else:
                            prop.value_type = value_types

        return modified


    def set_connection_persistence(self,
                                   build_ele_list: list[BuildingElement]):
        """ Set the persistence for the connected parameter

        Args:
            build_ele_list: building element list
        """

        param_dict = {"build_ele_list" : build_ele_list,
                      "AllplanGeo" : AllplanGeo,
                      "get_values_from_list" : BuildingElementComposite.get_values_from_list}

        for index, constraints in enumerate(self.sub_ele_constraints):
            for constraint in constraints:
                if constraint.value  and  (constraint.condition == "True"  or  eval(constraint.condition, param_dict)):
                    value_name = PropertyUtil.get_property_value_name(constraint.name)

                    prop = build_ele_list[index + 1].get_property(value_name)

                    if constraint.name.find(".") == -1 and prop:
                        prop.persistent = ParameterProperty.Persistent.NO


    def set_element_visible(self,
                            ele_index: int,
                            value    : str):
        """ Set the visible state for the element

        Args:
            ele_index: element index
            value:     value
        """

        self.sub_ele_visible[ele_index] = value


    def is_element_visible(self,
                           ele_index     : int,
                           build_ele_list: list[BuildingElement]) -> bool:
        """ Check for a visible element

        Return: the element is visible: True/False

        Args:
            ele_index:      element index
            build_ele_list: Building element list

        Returns:
            element visible state
        """

        if ele_index >= len(self.sub_ele_visible):
            return True

        if self.sub_ele_visible[ele_index] == "True":
            return True

        if self.sub_ele_visible[ele_index] == "False":
            return False

        param_dict = {"build_ele_list" : build_ele_list}

        return eval(self.sub_ele_visible[ele_index],param_dict)


    def get_element_palette_data(self,
                                 element_id: str) -> PaletteData:
        """ Set the palette data for the element (control index, page text, expander text)

        Args:
            element_id: element ID

        Returns:
            palette data
        """

        if not element_id in self.sub_ele_palette_data:
            return PaletteData(0, -1, "", 0, "", 0)

        return self.sub_ele_palette_data[element_id]


    def get_script(self,
                   sub_ele_index: int) -> object:
        """ Get the script of the sub element

        Return: script

        Args:
            sub_ele_index: Index of the sub element

        Returns:
            script name
        """

        return self.sub_ele_script[sub_ele_index]


    def get_sub_element_name(self,
                             sub_ele_index: int) -> str:
        """ Get the name of the sub element

        Return: name

        Args:
            sub_ele_index: Index of the sub element

        Returns:
            sub element name
        """

        return self.sub_ele_name[sub_ele_index]


    def get_composite_build_ele_list(self,
                                     sub_ele_index : int,
                                     build_ele_list: list[BuildingElement]) -> tuple[list[BuildingElement], list[int]]:
        """ Get a tuple with the
              - list with the sub building elements
              - list with the indices of the sub building elements

        Args:
            sub_ele_index:  Index of the sub element
            build_ele_list: list with the building elements

        Returns:
            tuple with the lists
        """

        composite_list = []
        index_list     = []

        for composite in self.sub_ele_composite[sub_ele_index]:
            index = self.get_build_ele_index(composite)

            composite_list.append(build_ele_list[index])
            index_list.append(index)

        return (composite_list, index_list)

```

</details>