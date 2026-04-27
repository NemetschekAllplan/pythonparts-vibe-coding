---
title: "ValueDialogType"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\ValueDialogType.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ValueDialogType

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\ValueDialogType.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`, `werte`

## Übersicht

implementation of the value dialog type

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.MultiIndexListUtil`
- `ValueTypes.MultiIndex`
- `ValueTypes.ParameterPropertyValueTypes`
- `__future__`
- `_collections_abc`
- `abc`
- `typing`

## Klassen

### `ValueDialogType`

implementation of the value dialog type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__new__` | `cls, dialog_type: str` | `ValueDialogType` | initialize  Args:     dialog_type: dialog type  Returns:     created object |
| `has_input_controls` | `value_type: ParamPropValueTypesModule.ParameterPropertyValueType` | `bool` | get the has input controls left of the button state  Args:     value_type: value type  Returns:     has input controls left of the button state |
| `create_controls` | `_wpf_palette: WpfPaletteBuilder, _prop: ParameterProperty, _ctrl_props: ControlProperties, _page_index: int, _global_str_table: BuildingElementStringTable, _is_control_enabled: Callable[[ControlProperties], bool]` | `bool` | Add the dialog controls to the palette  Args:     _wpf_palette:        palette builder     _prop:               parameter property     _ctrl_props:         control properties     _page_index:         page index     _global_str_table:   global string table     _is_control_enabled: function for getting the enabled state  Returns:     False (non controls created) |
| `show` | `build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties, name: str` | `bool` | show the symbol dialog  Args:     build_ele:       building element with the parameter properties     prop:            parameter property     ctrl_props: value control property     name:            parameter name |
| `expand_value_string` | `value_str: str` | `str` | expand the value string  Args:     value_str: value string  Returns:     expanded value string |
| `get_index` | `build_ele: BuildingElement, ctrl_props: ControlProperties, name: str` | `int | MultiIndex | None` | get the current index  Args:     build_ele:  building element with the parameter properties     ctrl_props: value control property     name:       parameter name)  Returns:     list index or None if not exist |
| `get_default_value` | `build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties, name: str` | `Any` | get the default value  Args:     build_ele:  building element with the parameter properties     prop:       parameter property     ctrl_props: value control property     name:       parameter name)  Returns:     default value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the value dialog type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import abc

from _collections_abc import Callable

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.MultiIndexListUtil import MultiIndexListUtil

import ValueTypes.ParameterPropertyValueTypes as ParamPropValueTypesModule

from ValueTypes.MultiIndex import MultiIndex

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from BuildingElementStringTable import BuildingElementStringTable
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty

class ValueDialogType(str):
    """ implementation of the value dialog type
    """

    def __new__(cls,
                dialog_type: str) -> ValueDialogType:
        """ initialize

        Args:
            dialog_type: dialog type

        Returns:
            created object
        """

        instance = super().__new__(cls, dialog_type)

        return instance


    @staticmethod
    def has_input_controls(value_type: ParamPropValueTypesModule.ParameterPropertyValueType) -> bool:
        """ get the has input controls left of the button state

        Args:
            value_type: value type

        Returns:
            has input controls left of the button state
        """

        return value_type in {ParamPropValueTypesModule.ParameterPropertyValueTypes.ATTRIBUTE_ID,
                              ParamPropValueTypesModule.ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE,
                              ParamPropValueTypesModule.ParameterPropertyValueTypes.DATE}


    @staticmethod
    def create_controls(_wpf_palette       : WpfPaletteBuilder,
                        _prop              : ParameterProperty,
                        _ctrl_props        : ControlProperties,
                        _page_index        : int,
                        _global_str_table  : BuildingElementStringTable,
                        _is_control_enabled: Callable[[ControlProperties], bool]) -> bool:
        """ Add the dialog controls to the palette

        Args:
            _wpf_palette:        palette builder
            _prop:               parameter property
            _ctrl_props:         control properties
            _page_index:         page index
            _global_str_table:   global string table
            _is_control_enabled: function for getting the enabled state

        Returns:
            False (non controls created)
        """

        return False


    @staticmethod
    @abc.abstractmethod
    def show(build_ele      : BuildingElement,
             prop           : ParameterProperty,
             ctrl_props: ControlProperties,
             name           : str) -> bool:
        """ show the symbol dialog

        Args:
            build_ele:       building element with the parameter properties
            prop:            parameter property
            ctrl_props: value control property
            name:            parameter name
        """


    @staticmethod
    def expand_value_string(value_str: str) -> str:
        """ expand the value string

        Args:
            value_str: value string

        Returns:
            expanded value string
        """

        return value_str


    @staticmethod
    def get_index(build_ele : BuildingElement,
                  ctrl_props: ControlProperties,
                  name      : str) -> (int | MultiIndex | None):
        """ get the current index

        Args:
            build_ele:  building element with the parameter properties
            ctrl_props: value control property
            name:       parameter name)

        Returns:
            list index or None if not exist
        """

        if ctrl_props.value_index_name:
            if isinstance((index := build_ele.get_existing_property(ctrl_props.value_index_name).value), int):
                return index - 1

            return index

        if (ipb := name.find("[")) == -1:
            return None

        return int(name[ipb + 1:].split("]")[0])


    @staticmethod
    def get_default_value(build_ele : BuildingElement,
                          prop      : ParameterProperty,
                          ctrl_props: ControlProperties,
                          name      : str) -> Any:
        """ get the default value

        Args:
            build_ele:  building element with the parameter properties
            prop:       parameter property
            ctrl_props: value control property
            name:       parameter name)

        Returns:
            default value
        """

        if (value_index := ValueDialogType.get_index(build_ele, ctrl_props, name)) is None:
            return prop.value

        if isinstance(value_index, int):
            return prop.value[value_index]

        return MultiIndexListUtil.get_value(prop, value_index, build_ele.get_string_tables()[1])[0]

```

</details>