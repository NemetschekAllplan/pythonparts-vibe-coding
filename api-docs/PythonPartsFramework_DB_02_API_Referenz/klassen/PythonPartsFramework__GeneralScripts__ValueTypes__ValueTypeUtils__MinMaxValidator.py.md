---
title: "MinMaxValidator"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\MinMaxValidator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# MinMaxValidator

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\MinMaxValidator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the min/max validator

## Abhängigkeiten

- `AnyValueByType`
- `BuildingElementStringTable`
- `ControlProperties`
- `NemAll_Python_Utility`
- `ParameterProperty`
- `__future__`
- `collections.abc`
- `typing`

## Klassen

### `MinMaxValidator`

implementation of the min/max validator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_lock_update_message` | `lock: bool` | `None` | set the lock state for the update message  Args:     lock: lock state |
| `validate_for_min_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, min_value: Any, global_str_table: BuildingElementStringTable, test_min_fct: Callable[[Any, Any], tuple[bool, Any]]` | `bool` | validate for the minimal value  Args:     prop:             property     ctrl_prop:        control properties     min_value:        min value     global_str_table: global string table     test_min_fct:     function for the min test  Returns:     palette update state |
| `validate_for_max_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, max_value: Any, global_str_table: BuildingElementStringTable, test_max_fct: Callable[[Any, Any], tuple[bool, Any]]` | `bool` | validate for the maximal value  Args:     prop:             property     ctrl_prop:        control properties     max_value:        min value     global_str_table: global string table     test_max_fct:     function for the max test  Returns:     palette update state |
| `__check_min_value_for_list` | `prop: ParameterProperty, ctrl_prop: ControlProperties, min_value: Any, global_str_table: BuildingElementStringTable, test_min_fct: Callable[[Any, Any], tuple[bool, Any]]` | `bool` | check the minimal value  Args:     prop:             property     ctrl_prop:        control properties     min_value:        min value     global_str_table: global string table     test_min_fct:     function for the min test  Returns:     update state |
| `__check_max_value_for_list` | `prop: ParameterProperty, ctrl_prop: ControlProperties, max_value: Any, global_str_table: BuildingElementStringTable, test_max_fct: Callable[[Any, Any], tuple[bool, Any]]` | `bool` | check the minimal value  Args:     prop:             property     ctrl_prop:        control properties     max_value:        max value     global_str_table: global string table     test_max_fct:     function for the max test  Returns:     update state |
| `__show_update_message` | `text_id: str, default_text: str, value: Any, new_value: Any, ctrl_prop: ControlProperties, prop: ParameterProperty, global_str_table: BuildingElementStringTable` | `bool` | show the update message  Args:     text_id:          text id of the message string     default_text:     default text     value:            value     new_value:        new value     ctrl_prop:        control properties     prop:             property     global_str_table: global string table  Returns:     show message state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the min/max validator
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from collections.abc import Callable

import NemAll_Python_Utility as AllplanUtil

from AnyValueByType import AnyValueByType

if TYPE_CHECKING:
    from BuildingElementStringTable import BuildingElementStringTable
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty

MIN_VALUE_MSG = "The value for \"%s\" is adapted to the minimal value %s"
MAX_VALUE_MSG = "The value for \"%s\" is adapted to the maximal value %s"

class MinMaxValidator():
    """ implementation of the min/max validator
    """

    LOCK_UPDATE_MESSAGE = False

    @staticmethod
    def set_lock_update_message(lock: bool):
        """ set the lock state for the update message

        Args:
            lock: lock state
        """

        MinMaxValidator.LOCK_UPDATE_MESSAGE = lock


    @staticmethod
    def validate_for_min_value(prop            : ParameterProperty,
                               ctrl_prop       : ControlProperties,
                               min_value       : Any,
                               global_str_table: BuildingElementStringTable,
                               test_min_fct    : Callable[[Any, Any], tuple[bool, Any]]) -> bool:
        """ validate for the minimal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            min_value:        min value
            global_str_table: global string table
            test_min_fct:     function for the min test

        Returns:
            palette update state
        """

        #------------- check the values from a list against the min value

        if isinstance(prop.value, list):
            return MinMaxValidator.__check_min_value_for_list(prop, ctrl_prop, min_value, global_str_table, test_min_fct)


        #------------- check a single value against the min value

        use_min, new_value = test_min_fct(prop.value, min_value.get_value(prop, prop.name))

        if not use_min:
            return False

        is_update = MinMaxValidator.__show_update_message("e_VALUE_UPDATE_BY_MIN", MIN_VALUE_MSG,
                                                          prop.value, new_value, ctrl_prop, prop, global_str_table)
        prop.value = new_value

        return is_update


    @staticmethod
    def validate_for_max_value(prop            : ParameterProperty,
                               ctrl_prop       : ControlProperties,
                               max_value       : Any,
                               global_str_table: BuildingElementStringTable,
                               test_max_fct    : Callable[[Any, Any], tuple[bool, Any]]) -> bool:
        """ validate for the maximal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            max_value:        min value
            global_str_table: global string table
            test_max_fct:     function for the max test

        Returns:
            palette update state
        """

        #------------- check the values from a list against the max value

        if isinstance(prop.value, list):
            return MinMaxValidator.__check_max_value_for_list(prop, ctrl_prop, max_value, global_str_table, test_max_fct)


        #------------- check a single value against the max value

        use_min, new_value = test_max_fct(prop.value, max_value.get_value(prop, prop.name))

        if not use_min:
            return False

        is_update = MinMaxValidator.__show_update_message("e_VALUE_UPDATE_BY_MAX", MAX_VALUE_MSG,
                                                          prop.value, new_value, ctrl_prop, prop, global_str_table)

        prop.value = new_value

        return is_update


    @staticmethod
    def __check_min_value_for_list(prop            : ParameterProperty,
                                   ctrl_prop       : ControlProperties,
                                   min_value       : Any,
                                   global_str_table: BuildingElementStringTable,
                                   test_min_fct    : Callable[[Any, Any], tuple[bool, Any]]) -> bool:
        """ check the minimal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            min_value:        min value
            global_str_table: global string table
            test_min_fct:     function for the min test

        Returns:
            update state
        """

        is_update = False

        for index, value in enumerate(prop.value):
            if isinstance(value, list):
                for col_index, col_value in enumerate(value):
                    use_min, new_value = test_min_fct(col_value, min_value.get_value(prop, f"{prop.name}[{index}][{col_index}]"))

                    if use_min:
                        prop.value[index][col_index] = new_value

                        is_update |= MinMaxValidator.__show_update_message("e_VALUE_UPDATE_BY_MIN", MIN_VALUE_MSG,
                                                                           col_value, new_value, ctrl_prop, prop, global_str_table)

            else:
                use_min, new_value = test_min_fct(value, min_value.get_value(prop, f"{prop.name}[{index}]"))

                if use_min:
                    prop.value[index] = new_value

                    is_update |= MinMaxValidator.__show_update_message("e_VALUE_UPDATE_BY_MIN", MIN_VALUE_MSG,
                                                                       value, new_value, ctrl_prop, prop, global_str_table)

        return is_update


    @staticmethod
    def __check_max_value_for_list(prop            : ParameterProperty,
                                   ctrl_prop       : ControlProperties,
                                   max_value       : Any,
                                   global_str_table: BuildingElementStringTable,
                                   test_max_fct    : Callable[[Any, Any], tuple[bool, Any]]) -> bool:
        """ check the minimal value

        Args:
            prop:             property
            ctrl_prop:        control properties
            max_value:        max value
            global_str_table: global string table
            test_max_fct:     function for the max test

        Returns:
            update state
        """

        is_update = False

        for index, value in enumerate(prop.value):
            if isinstance(value, list):
                for col_index, col_value in enumerate(value):
                    use_max, new_value = test_max_fct(col_value, max_value.get_value(prop, f"{prop.name}[{index}][{col_index}]"))

                    if use_max:
                        prop.value[index][col_index] = new_value

                        is_update |= MinMaxValidator.__show_update_message("e_VALUE_UPDATE_BY_MIN", MAX_VALUE_MSG,
                                                                           col_value, new_value, ctrl_prop, prop, global_str_table)

            else:
                use_max, new_value = test_max_fct(value, max_value.get_value(prop, f"{prop.name}[{index}]"))

                if use_max:
                    prop.value[index] = new_value

                    is_update |= MinMaxValidator.__show_update_message("e_VALUE_UPDATE_BY_MAX", MAX_VALUE_MSG,
                                                                       value, new_value, ctrl_prop, prop, global_str_table)

        return is_update


    @staticmethod
    def __show_update_message(text_id         : str,
                              default_text    : str,
                              value           : Any,
                              new_value       : Any,
                              ctrl_prop       : ControlProperties,
                              prop            : ParameterProperty,
                              global_str_table: BuildingElementStringTable) -> bool:
        """ show the update message

        Args:
            text_id:          text id of the message string
            default_text:     default text
            value:            value
            new_value:        new value
            ctrl_prop:        control properties
            prop:             property
            global_str_table: global string table

        Returns:
            show message state
        """

        if not ctrl_prop.visible or MinMaxValidator.LOCK_UPDATE_MESSAGE:
            return False

        text = ctrl_prop.text

        if isinstance(value, AnyValueByType):
            if not text:
                text = value.text

            value = value.value

        if isinstance(new_value, AnyValueByType):
            new_value = new_value.value

        msg_str = global_str_table.get_string(text_id, default_text)

        text = f"{ctrl_prop.expander_name} - {text}" if ctrl_prop.expander_name else text

        value     = prop.value_type.value_to_unit_string(value)
        new_value = prop.value_type.value_to_unit_string(new_value)

        text += f" ({value})"

        msg_str = msg_str % (text, new_value)

        AllplanUtil.ShowMessageBox(msg_str, AllplanUtil.MB_OK)

        return True

```

</details>