---
title: "NamedTupleImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\NamedTupleImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# NamedTupleImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\NamedTupleImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the named tuple value type

## Abhängigkeiten

- `BuildingElementStringTable`
- `ControlProperties`
- `GeometryElements.CoordinateValueUtil`
- `ParameterProperty`
- `StringToValueConverter`
- `TupleImpl`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypes.ValueTypeUtils.MinMaxValidator`
- `__future__`
- `typing`

## Klassen

### `NamedTupleImpl`

implementation of the named tuple value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `validate_for_min_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, min_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the minimal value  Args:     prop:             property     ctrl_prop:        control properties     min_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `validate_for_max_value` | `prop: ParameterProperty, ctrl_prop: ControlProperties, max_value: Any, global_str_table: BuildingElementStringTable` | `bool` | validate for the maximal value  Args:     prop:             property     ctrl_prop:        control properties     max_value:        min value     global_str_table: global string table  Returns:     palette update state |
| `__insert_tuple_value` | `index: int, index_list: list[int], tuple_value: Any, name: str, value: Any` | `Any` | insert a value in a tuple  Args:     index:       index     index_list:  index list     tuple_value: tuple value     name:        name of the modified property     value:       property value  Returns:     new tuple value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the named tuple value type
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from Utilities.GeneralConstants import GeneralConstants

import ValueTypes.ValueTypeUtils.MinMaxValidator

from .ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

from .GeometryElements.CoordinateValueUtil import CoordinateValueUtil
from .TupleImpl import TupleImpl

if TYPE_CHECKING:
    from StringToValueConverter import StringToValueConverter

    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService


class NamedTupleImpl(TupleImpl):
    """ implementation of the named tuple value type
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

        prop.is_modified = True

        list_index, tuple_indexes = ParameterPropertyListUtil.get_tuple_list_indexes(name)


        #----------------- new value

        if list_index == -1 and not tuple_indexes:
            prop.value = value

            return False


        #----------------- tuple

        if list_index == -1:
            prop.value = NamedTupleImpl.__insert_tuple_value(0, tuple_indexes, prop.value, name, value)

            return False


        #----------------- tuple list

        prop.value[list_index] = NamedTupleImpl.__insert_tuple_value(0, tuple_indexes, prop.value[list_index], name, value)

        return False


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
                    field_name  = value._fields[index]

                    value = value._replace(**{field_name : min_value})

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
                    field_name  = value._fields[index]

                    value = value._replace(**{field_name : max_value})

                    use_max = True

            return use_max, value

        return ValueTypes.ValueTypeUtils.MinMaxValidator.MinMaxValidator.validate_for_max_value(prop, ctrl_prop, max_value,
                                                                                                global_str_table, test_max)


    @staticmethod
    def __insert_tuple_value(index      : int,
                             index_list : list[int],
                             tuple_value: Any,
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

        field_name  = tuple_value._fields[tuple_index]

        if index == len(index_list) - 1:
            if name[-2: -1] == GeneralConstants.SUB_NAME_SEPARATOR:
                CoordinateValueUtil.set_coordinate_value(part_value, name, value)

                return tuple_value

            if GeneralConstants.SUB_NAME_SEPARATOR in name:
                TupleImpl.__set_fixture(part_value, name, value)

                return tuple_value

            return tuple_value._replace(**{field_name : value})

        return tuple_value._replace(**{field_name : NamedTupleImpl.__insert_tuple_value(index + 1, index_list,
                                                                                        tuple_value[tuple_index], name, value)})

```

</details>