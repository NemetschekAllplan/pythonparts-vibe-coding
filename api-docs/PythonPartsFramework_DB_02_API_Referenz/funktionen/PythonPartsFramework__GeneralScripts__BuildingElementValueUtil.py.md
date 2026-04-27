---
title: "BuildingElementValueUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementValueUtil.py"
type: "module"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementValueUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementValueUtil.py`  
> **Typ:** Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

Implementation of the building element value utilities

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `BuildingElementParameterPropertyUtil`
- `BuildingElementValueConstraint`
- `ControlProperties`
- `ControlPropertiesMinMaxUtil`
- `ControlPropertiesValueListUtil`
- `DialogTypes.ValueDialogTypes`
- `Palette.PaletteUpdateValidation`
- `ParameterProperty`
- `StringEvaluate`
- `StringToValueConverter`
- `Utilities.GeneralConstants`
- `ValueListUtil`
- `ValueTypeUtil`
- `ValueTypes.ParameterPropertyValueTypes`
- `itertools`
- `typing`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `update_list_size(name: str, new_count: Union[int, Dict[str, Any]], build_ele: BuildingElement, build_ele_ctrl_props: Optional[BuildingElementControlProperties]=None)`

Update the size of the lists

Args:
    name:                 name of the modified property
    new_count:            New_count
    build_ele:            building element with the parameter properties
    build_ele_ctrl_props: control properties of the building element

Returns:
    update palette state

**Parameter:**
- `name: str`
- `new_count: Union[int`
- `Dict[str`
- `Any]]`
- `build_ele: BuildingElement`
- `build_ele_ctrl_props: Optional[BuildingElementControlProperties]=None`

**Rückgabe:** `bool`

**Beispiel:**
```python
result = update_list_size(..., ..., ..., ..., ..., ...)
```

### `update_value(name: str, value: Any, build_ele: BuildingElement, build_ele_ctrl_props: BuildingElementControlProperties)`

Update the value of the building element

Args:
    name:                 name of the modified property
    value:                new value
    build_ele:            building element with the parameter properties
    build_ele_ctrl_props: control properties of the building element

Returns:
    tuple(refresh the palette, modified property)

**Parameter:**
- `name: str`
- `value: Any`
- `build_ele: BuildingElement`
- `build_ele_ctrl_props: BuildingElementControlProperties`

**Rückgabe:** `Tuple[bool, Optional[ParameterProperty]]`

**Beispiel:**
```python
result = update_value(..., ..., ..., ...)
```

### `__process_dialog_button(value_ctrl_prop: ControlProperties, prop: ParameterProperty, button_name: str, name: str, value: Any, build_ele: BuildingElement)`

process the dialog button click

Args:
    value_ctrl_prop: control properties
    prop:            parameter property
    button_name:     button name
    name:            property name
    value:           new value
    build_ele:       building element with the parameter properties

Returns:
    returns

**Parameter:**
- `value_ctrl_prop: ControlProperties`
- `prop: ParameterProperty`
- `button_name: str`
- `name: str`
- `value: Any`
- `build_ele: BuildingElement`

**Rückgabe:** `bool`

**Beispiel:**
```python
result = __process_dialog_button(..., ..., ..., ..., ..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the building element value utilities
"""

from typing import Any, Tuple, Optional, Union, Dict

from itertools import zip_longest

import BuildingElementParameterPropertyUtil

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementValueConstraint import BuildingElementValueConstraint
from ControlProperties import ControlProperties
from ControlPropertiesMinMaxUtil import ControlPropertiesMinMaxUtil
from ControlPropertiesValueListUtil import ControlPropertiesValueListUtil
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate
from StringToValueConverter import StringToValueConverter
from ValueListUtil import ValueListUtil
from ValueTypeUtil import ValueTypeUtil

from DialogTypes.ValueDialogTypes import ValueDialogTypes

from Palette.PaletteUpdateValidation import PaletteUpdateValidation

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

def update_list_size(name                : str,
                     new_count           : Union[int, Dict[str, Any]],
                     build_ele           : BuildingElement,
                     build_ele_ctrl_props: Optional[BuildingElementControlProperties] = None) -> bool:
    """ Update the size of the lists

    Args:
        name:                 name of the modified property
        new_count:            New_count
        build_ele:            building element with the parameter properties
        build_ele_ctrl_props: control properties of the building element

    Returns:
        update palette state
    """

    refresh_palette = False

    list_parameter : list[tuple[ParameterProperty, ControlProperties]]= []

    for prop in build_ele.get_properties():
        if not isinstance(prop.value, list):
            continue

        dimensions = prop.dimensions.split(",")

        dimensions_len = len(dimensions)

        two_dim_count = 1

        if dimensions_len > 1:
            two_dim_count = StringEvaluate.eval_dimension(dimensions[-1], build_ele.get_parameter_dict())

        ctrl_prop = build_ele_ctrl_props.get_property(prop.name) if build_ele_ctrl_props else None

        value_str = ""


        #--------------- use the first combo box list entry, min value for default

        if ctrl_prop:
            value_types = prop.value_type.rstrip(")").split("(")
            value_types = value_types[-1].split(",")

            for index, (value_type, min_value, value_list) in enumerate(zip_longest(value_types,
                                                                                    ctrl_prop.min_value_condition.split(","),
                                                                                    ctrl_prop.value_list.split(","),
                                                                                    fillvalue = "")):
                if index:
                    value_str += "|"

                if value_type.find("combobox") != -1:
                    if (combo_list := value_list.split("|")):
                        value_str += combo_list[0] if two_dim_count == 1 else "'" + combo_list[0] + "'"

                elif ValueTypeUtil.is_string_input(value_type) and two_dim_count > 1:
                    value_str += "'" + min_value + "'"
                else:
                    value_str += min_value


        #---------------- default value for the row of a 2-dim list

        if two_dim_count > 1:
            if not value_str:
                value_str = "''"

            value_str = "[" + (value_str + ",") * (two_dim_count - 1) + value_str + "]"

        if ValueListUtil.update_value_list(prop, name, new_count,
                                           StringToValueConverter.get_default_value(prop, value_str) if not prop.value else None):
            refresh_palette = True

            if ctrl_prop:
                list_parameter.append((prop, ctrl_prop))


    #--------------------- update the enable state by constraints

    for prop, ctrl_prop in list_parameter:
        if ctrl_prop.constraint:
            prop.value_type.update_enable_by_constraint(build_ele, prop, ctrl_prop)

    return refresh_palette


def update_value(name                : str,
                 value               : Any,
                 build_ele           : BuildingElement,
                 build_ele_ctrl_props: BuildingElementControlProperties) -> Tuple[bool, Optional[ParameterProperty]]:
    """ Update the value of the building element

    Args:
        name:                 name of the modified property
        value:                new value
        build_ele:            building element with the parameter properties
        build_ele_ctrl_props: control properties of the building element

    Returns:
        tuple(refresh the palette, modified property)
    """

    update_name = name

    parameter_dict = StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0])

    if (value_dialog_button := GeneralConstants.DIALOG_BUTTON_KEY in name):
        name = name.split(GeneralConstants.DIALOG_BUTTON_KEY)[0]

    parent_name = BuildingElementParameterPropertyUtil.get_property_value_name(name)

    if (prop := build_ele.get_property(parent_name)):
        prop.is_modified = True

    refresh_palette = False

    palette_update_validation = PaletteUpdateValidation(build_ele, build_ele_ctrl_props, parameter_dict)


    #----------------- check the min/max and the value list of the value

    value_ctrl_prop = build_ele_ctrl_props.get_property(parent_name)

    if prop and value_ctrl_prop:
        valid_value = ControlPropertiesMinMaxUtil.validate_value(value_ctrl_prop, prop, value, name, parameter_dict)

        if (valid_value := ControlPropertiesValueListUtil.validate_value(value_ctrl_prop, prop, valid_value, parameter_dict)[1]) != value:
            value           = valid_value
            refresh_palette = True


    #----------------- update the property and check the value constraint

    if prop:
        if value_ctrl_prop and value_dialog_button:
            refresh_palette |= __process_dialog_button(value_ctrl_prop, prop, update_name, name, value, build_ele)

        elif BuildingElementParameterPropertyUtil.set_property_value(prop, name, value):
            refresh_palette = True

        if BuildingElementValueConstraint.check_property_constraint(name, build_ele, build_ele_ctrl_props):
            refresh_palette = True

        if not refresh_palette and prop.value_type in (ParameterPropertyValueTypes.REINF_MESH_GROUP,
                                                       ParameterPropertyValueTypes.REINF_STEEL_GRADE):
            refresh_palette = True

        if not refresh_palette:
            parameter_dict = StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0])

            refresh_palette = palette_update_validation.check_palette_update(name, parameter_dict)


    #----------------- update the list dimension

    if isinstance(value, int) and update_list_size(name, build_ele.get_parameter_dict(), build_ele, build_ele_ctrl_props):
        refresh_palette = True

    return refresh_palette, prop


def __process_dialog_button(value_ctrl_prop: ControlProperties,
                            prop           : ParameterProperty,
                            button_name    : str,
                            name           : str,
                            value          : Any,
                            build_ele      : BuildingElement) -> bool:
    """ process the dialog button click

    Args:
        value_ctrl_prop: control properties
        prop:            parameter property
        button_name:     button name
        name:            property name
        value:           new value
        build_ele:       building element with the parameter properties

    Returns:
        returns
    """

    if value_ctrl_prop.value_dialog:
        return value_ctrl_prop.value_dialog.show(build_ele, prop, value_ctrl_prop, name)

    if GeneralConstants.DIALOG_BUTTON_KEY in button_name:
        name, _, value_dialog = button_name.partition(GeneralConstants.DIALOG_BUTTON_KEY)

        if (dialog_impl := ValueDialogTypes.get_value_dialog_type_impl(value_dialog)) is not None:
            return dialog_impl.show(build_ele, prop, value_ctrl_prop, name)

    if GeneralConstants.DIALOG_BUTTON_COMBO_DEL_ENTRY in button_name:
        return BuildingElementParameterPropertyUtil.set_property_value(prop, button_name, value)

    return BuildingElementParameterPropertyUtil.set_property_value(prop, name, value)

```

</details>