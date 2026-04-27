---
title: "PaletteUpdateValidation"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteUpdateValidation.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PaletteUpdateValidation

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteUpdateValidation.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the palette update validation

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `ControlProperties`
- `ParameterProperty`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ValueTypeUtils.ValueListValidator`
- `dataclasses`
- `typing`

## Klassen

### `DynamicDates`

data class with the dynamic control data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `PaletteUpdateValidation`

implementation of the palette update validation
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele: BuildingElement, build_ele_ctrl_props: BuildingElementControlProperties, parameter_dict: dict[str, Any]` | `None` | initialize  Args:     build_ele:            building element with the parameter properties     build_ele_ctrl_props: list with the building element control properties     parameter_dict:       parameter dict |
| `__get_dynamic_data_state` | `self, parameter_dict: dict[str, Any]` | `list[DynamicDates]` | get the current state of the dynamic palette data  Args:     parameter_dict: parameter dictionary  Returns:     dynamic dates |
| `check_palette_update` | `self, name: str, parameter_dict: dict[str, Any]` | `bool` | check for a palette update  Args:     name:           name of the modified property     parameter_dict: parameter dictionary  Returns:     palette update state |
| `__check_dynamic_data_state` | `self, parameter_dict: dict[str, Any]` | `bool` | get the current state of the dynamic palette data  Args:     parameter_dict: parameter dictionary  Returns:     palette update state |
| `__compare_text` | `ctrl_props: ControlProperties, max_list_count: int, parameter_dict: dict[str, Any], old_text: str, new_text: str` | `bool` | compare text  Args:     ctrl_props:     control properties     max_list_count: max list count     parameter_dict: parameter dictionary     old_text:       old text     new_text:       new text  Returns:     text compare state |
| `__get_max_list_count_from_group` | `self, list_group_name: str` | `int` | get the max list count in a list group  Args:     list_group_name: list group name  Returns:     list group count |
| `__eval_text` | `ctrl_props: ControlProperties, eval_text: str, max_list_count: int, parameter_dict: dict[str, Any]` | `str` | eval the dynamic text  Args:     ctrl_props:     control properties     eval_text:      text to evaluate     max_list_count: max list count     parameter_dict: parameter dictionary  Returns:     evaluated text |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the palette update validation
"""

from typing import Any

from dataclasses import dataclass

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ValueTypeUtils.ValueListValidator import ValueListValidator

@dataclass
class DynamicDates():
    """ data class with the dynamic control data
    """

    value_list   : tuple[str, str] = ("", "")
    expander_name: str              = ""
    row_name     : str             = ""
    text         : str             = ""
    value_text   : str             = ""


class PaletteUpdateValidation():
    """ implementation of the palette update validation
    """

    def __init__(self,
                 build_ele           : BuildingElement,
                 build_ele_ctrl_props: BuildingElementControlProperties,
                 parameter_dict      : dict[str, Any]):
        """ initialize

        Args:
            build_ele:            building element with the parameter properties
            build_ele_ctrl_props: list with the building element control properties
            parameter_dict:       parameter dict
        """

        self.build_ele            = build_ele
        self.build_ele_ctrl_props = build_ele_ctrl_props

        self.dynamic_dates = self.__get_dynamic_data_state(parameter_dict)

        self.values = [prop.copy_value(prop.value) for prop in build_ele.get_properties() \
                                                       if prop.persistent != ParameterProperty.Persistent.NO]


    def __get_dynamic_data_state(self,
                                 parameter_dict: dict[str, Any]) -> list[DynamicDates]:
        """ get the current state of the dynamic palette data

        Args:
            parameter_dict: parameter dictionary

        Returns:
            dynamic dates
        """

        dynamic_dates: list[DynamicDates] = []

        build_ele = self.build_ele

        for ctrl_props in self.build_ele_ctrl_props:
            dyn_data = DynamicDates()

            if (prop := build_ele.get_property(ctrl_props.value_name)) is not None and \
                not prop.value_type.is_tuple_type() and prop.value_type.is_combobox_type():
                dyn_data.value_list = ValueListValidator.eval_value_list_formula(ctrl_props.value_list,
                                                                                 str(prop.value), parameter_dict)

            max_list_count = self.__get_max_list_count_from_group(ctrl_props.list_group_name)

            dyn_data.text          = self.__eval_text(ctrl_props, ctrl_props.text, max_list_count, parameter_dict)
            dyn_data.expander_name = self.__eval_text(ctrl_props, ctrl_props.expander_name, max_list_count, parameter_dict)
            dyn_data.row_name      = self.__eval_text(ctrl_props, ctrl_props.row_name, max_list_count, parameter_dict)

            if prop is not None and prop.value_type == ParameterPropertyValueTypes.TEXT:
                dyn_data.value_text = self.__eval_text(ctrl_props, prop.value, max_list_count, parameter_dict)

            dynamic_dates.append(dyn_data)

        return dynamic_dates


    def check_palette_update(self,
                             name          : str,
                             parameter_dict: dict[str, Any]) -> bool:
        """ check for a palette update

        Args:
            name:           name of the modified property
            parameter_dict: parameter dictionary

        Returns:
            palette update state
        """

        for prop, value in zip(self.build_ele.get_properties(), self.values):
            if prop.name != name and prop.persistent != ParameterProperty.Persistent.NO and value != prop.value:
                return True

        if any(name in ctrl_props.value_index_name for ctrl_props in self.build_ele_ctrl_props):
            return True

        if any(name in ctrl_props.value_list_2 for ctrl_props in self.build_ele_ctrl_props):
            return True

        return self.__check_dynamic_data_state(parameter_dict)



    def __check_dynamic_data_state(self,
                                   parameter_dict: dict[str, Any]) -> bool:
        """ get the current state of the dynamic palette data

        Args:
            parameter_dict: parameter dictionary

        Returns:
            palette update state
        """

        build_ele = self.build_ele

        for ctrl_props, dyn_data in zip(self.build_ele_ctrl_props, self.dynamic_dates):
            if (prop := build_ele.get_property(ctrl_props.value_name)) is not None and \
                not prop.value_type.is_tuple_type() and \
                prop.value_type.is_combobox_type() and  \
                ValueListValidator.eval_value_list_formula(ctrl_props.value_list,
                                                           str(prop.value), parameter_dict) != dyn_data:
                return True

            max_list_count = self.__get_max_list_count_from_group(ctrl_props.list_group_name)

            if self.__compare_text(ctrl_props, max_list_count, parameter_dict, ctrl_props.text, dyn_data.text):
                return True

            if self.__compare_text(ctrl_props, max_list_count, parameter_dict, ctrl_props.expander_name, dyn_data.expander_name):
                return True

            if self.__compare_text(ctrl_props, max_list_count, parameter_dict, ctrl_props.row_name, dyn_data.row_name):
                return True

            if prop is not None and prop.value_type == ParameterPropertyValueTypes.TEXT and \
               self.__compare_text(ctrl_props, max_list_count, parameter_dict, prop.value, dyn_data.value_text):
                return True

        return False


    @staticmethod
    def __compare_text(ctrl_props    : ControlProperties,
                       max_list_count: int,
                       parameter_dict: dict[str, Any],
                       old_text      : str,
                       new_text      : str) -> bool:
        """ compare text

        Args:
            ctrl_props:     control properties
            max_list_count: max list count
            parameter_dict: parameter dictionary
            old_text:       old text
            new_text:       new text

        Returns:
            text compare state
        """

        return StringEvaluate.is_text_from_script(old_text) and \
               PaletteUpdateValidation.__eval_text(ctrl_props, old_text, max_list_count, parameter_dict) != new_text


    def __get_max_list_count_from_group(self,
                                        list_group_name: str) -> int:
        """ get the max list count in a list group

        Args:
            list_group_name: list group name

        Returns:
            list group count
        """

        if not list_group_name:
            return 1

        build_ele = self.build_ele
        max_count = 1

        for ctrl_props in self.build_ele_ctrl_props:
            if ctrl_props.list_group_name == list_group_name:
                if (prop := build_ele.get_property(ctrl_props.value_name)) is not None and isinstance(prop.value, list):
                    max_count = max(max_count, len(prop.value))

        return max_count


    @staticmethod
    def __eval_text(ctrl_props    : ControlProperties,
                    eval_text     : str,
                    max_list_count: int,
                    parameter_dict: dict[str, Any]) -> str:
        """ eval the dynamic text

        Args:
            ctrl_props:     control properties
            eval_text:      text to evaluate
            max_list_count: max list count
            parameter_dict: parameter dictionary

        Returns:
            evaluated text
        """

        if not StringEvaluate.is_text_from_script(eval_text):
            return eval_text

        text = ""

        for index in range(max_list_count):
            if (visible_fct := ctrl_props.visible_function) is not None:
                if not visible_fct(index):
                    continue

            if (visible_condition := ctrl_props.visible_condition):
                visible_condition = visible_condition.replace(GeneralConstants.LIST_ROW_KEYWORD, str(index))

                if not StringEvaluate.eval_condition(visible_condition, parameter_dict):
                    continue

            text += StringEvaluate.eval_text(eval_text.replace("$list_row", str(index)).replace("$list_col", "0"), parameter_dict)

        return text

```

</details>