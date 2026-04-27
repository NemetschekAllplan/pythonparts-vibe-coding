---
title: "ValueListUtil"
source: "PythonPartsFramework\GeneralScripts\ValueListUtil.py"
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


# ValueListUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueListUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

Implementation of the functions for a value list

## Abhängigkeiten

- `ParameterProperty`
- `StringEvaluate`
- `__future__`
- `typing`

## Klassen

### `ValueListUtil`

Implementation of class ValueListUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `_copy_object` | `obj: Any` | `Any` | Copy an object  Args:     obj: object  Returns:     object copy |
| `resize_1_dim_list` | `elements: list[Any], new_count: int, new_value: Any` | `None` | Resize a one dimensional list  Args:     elements:  list elements to resize     new_count: new element count     new_value: new value |
| `resize_2_dim_list` | `source_list: list[Any], target_list: list[Any]` | `None` | Resize a two dimensional list  Args:     source_list: source list     target_list: target list |
| `resize_list` | `elements: list[Any], new_count: int, default_obj: Any=None` | `bool` | Resize a list  Args:     elements:    list elements to resize     new_count:   new element count     default_obj: default object  Returns:     resize state |
| `update_value_list` | `prop: ParameterProperty, dim_name: str, new_count: int | dict[str, Any], default_obj: Any | None=None` | `bool` | Update the size of a value list  Args:     prop:        Property     dim_name:    Name of the dimension     new_count:   New count of the list or dict with the new value     default_obj: Default for new object  Returns:     update state |
| `create_value_list` | `prop: ParameterProperty, value_list: list[Any]` | `list[Any]` | Create a new list by the size of an existing list  Args:     prop:       Property     value_list: existing list  Returns:     new list |
| `replace_sub_values` | `source_list: list[Any], target_list: list[Any], sub_name: str` | `None` | Replace the sub values from the value inside a list  Args:     source_list: source list     target_list: target list     sub_name:    name of the sub element |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the functions for a value list
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from StringEvaluate import StringEvaluate

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class ValueListUtil():
    """ Implementation of class ValueListUtil
    """

    @staticmethod
    def _copy_object(obj: Any) -> Any:
        """ Copy an object

        Args:
            obj: object

        Returns:
            object copy
        """

        if isinstance(obj, tuple):
            if getattr(obj, "_fields", None) is None:
                return tuple(type(value)(value) for value in obj)

            return type(obj)(**obj._asdict())

        if isinstance(obj, list):
            return [type(value)(value) for value in obj]

        if isinstance(obj, (int, float, str)):
            return obj

        return type(obj)(obj)


    @staticmethod
    def resize_1_dim_list(elements : list[Any],
                          new_count: int,
                          new_value: Any):
        """ Resize a one dimensional list

        Args:
            elements:  list elements to resize
            new_count: new element count
            new_value: new value
        """

        old_count = len(elements)

        if new_count < old_count:
            del elements[new_count:]

            return

        for _ in range(old_count, new_count):
            elements.append(ValueListUtil._copy_object(new_value))


    @staticmethod
    def resize_2_dim_list(source_list: list[Any],
                          target_list: list[Any]):
        """ Resize a two dimensional list

        Args:
            source_list: source list
            target_list: target list
        """

        ValueListUtil.resize_list(target_list, len(source_list))

        for index, (source, target) in enumerate(zip(source_list, target_list)):
            is_source_list = isinstance(source, list)
            is_target_list = isinstance(target, list)

            if is_source_list and is_target_list:
                ValueListUtil.resize_list(target, len(source))

            elif not is_source_list and is_target_list:
                target_list[index] = target[0]

            elif is_source_list and not is_target_list:
                target_list[index] = [target]

                ValueListUtil.resize_list(target_list[index], len(source))


    @staticmethod
    def resize_list(elements   : list[Any],
                    new_count  : int,
                    default_obj: Any = None) -> bool:
        """ Resize a list

        Args:
            elements:    list elements to resize
            new_count:   new element count
            default_obj: default object

        Returns:
            resize state
        """

        if (old_count := len(elements)) == new_count:
            return False

        if new_count < old_count:
            del elements[new_count:]

            return True

        if elements:
            default_obj = elements[-1]

        for _ in range(old_count, new_count):
            elements.append(ValueListUtil._copy_object(default_obj))

        return True


    @staticmethod
    def update_value_list(prop       : ParameterProperty,
                          dim_name   : str,
                          new_count  : (int | dict[str, Any]),
                          default_obj: (Any | None) = None) -> bool:
        """ Update the size of a value list

        Args:
            prop:        Property
            dim_name:    Name of the dimension
            new_count:   New count of the list or dict with the new value
            default_obj: Default for new object

        Returns:
            update state
        """

        dimensions = prop.dimensions.split(",")

        index = -1

        elements = prop.value

        is_update = False

        for dimension in dimensions:
            index += 1

            if StringEvaluate.is_string_in_formula(dim_name, dimension):
                count = new_count if isinstance(new_count, int) else StringEvaluate.eval_dimension(dimension, new_count)

                if index == 0:
                    ValueListUtil.resize_list(elements, count, default_obj)

                    is_update = True

                elif index == 1:
                    for ele in elements:
                        ValueListUtil.resize_list(ele, count, default_obj)

                    is_update = True

        if is_update:
            prop.is_modified = True

        return is_update


    @staticmethod
    def create_value_list(prop      : ParameterProperty,
                          value_list: list[Any]) -> list[Any]:
        """ Create a new list by the size of an existing list

        Args:
            prop:       Property
            value_list: existing list

        Returns:
            new list
        """

        prop_value_type = type(prop.value)

        new_list = []

        for value in value_list:
            if isinstance(value, list):
                new_list.append(ValueListUtil.create_value_list(prop, value))
            else:
                new_list.append(prop_value_type(prop.value))

        return new_list


    @staticmethod
    def replace_sub_values(source_list: list[Any],
                           target_list: list[Any],
                           sub_name   : str):
        """ Replace the sub values from the value inside a list

        Args:
            source_list: source list
            target_list: target list
            sub_name:    name of the sub element
        """

        for i, target in enumerate(target_list):
            source = source_list[i]

            if isinstance(source, list):
                for j, source_val in enumerate(source):
                    setattr(target[j], sub_name, source_val)
            else:
                setattr(target, sub_name, source)

```

</details>