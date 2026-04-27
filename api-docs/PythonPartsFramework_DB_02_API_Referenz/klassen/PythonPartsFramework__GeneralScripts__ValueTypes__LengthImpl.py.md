---
title: "LengthImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\LengthImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# LengthImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\LengthImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the Length value type

## Abhängigkeiten

- `BaseFloatImpl`
- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueTypes`
- `StringEvaluate`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `LengthImpl`

implementation of the Length value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty.ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty.ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the length edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `update_by_constraint` | `build_ele: BuildingElement, prop: ParameterProperty.ParameterProperty, ctrl_props: ControlProperties, _name: str` | `None` | update by a constraint  Args:     build_ele:  building element with the parameter properties     prop:       parameter property to update     ctrl_props: control properties     _name:      name of the modified value |
| `is_default_init_by_constraint` | `build_ele: BuildingElement, ctrl_props: ControlProperties` | `bool` | check, whether the default value must be initialized by the constraint  Args:     build_ele:  building element with the parameter properties     ctrl_props: control properties  Returns:     default init by the constraint state |
| `value_to_unit_string` | `value: float` | `str` | convert the value to the current unit value  Args:     value: value  Returns:     unit value as string |
| `string_to_unit_value` | `cls, value_str: str` | `float` | convert the string to the unit value  Args:     value_str: value string  Returns:     unit value as string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Length value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import NemAll_Python_AllplanSettings as AllplanSettings

from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

import ParameterProperty

from .ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

from .ParameterPropertyValueTypes import ParameterPropertyValueTypes

from .BaseFloatImpl import BaseFloatImpl

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class LengthImpl(BaseFloatImpl):
    """ implementation of the Length value type
    """

    @staticmethod
    def set_property_value(prop : ParameterProperty.ParameterProperty,
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

        if (ParameterPropertyListUtil.get_multiple_list_index(name)) is not None and isinstance(value, str):
            error, value = AllplanSettings.UnitService.ConvertToMM(value)

            if error:
                return True

        if prop.is_varied_value and isinstance(value, str):
            value = LengthImpl.string_to_unit_value(value)

        return BaseFloatImpl.set_property_value(prop, name, value)

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty.ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the length edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if prop.is_varied_value:
            value = prop_pal_ctrl_service.global_str_table.get_string("e_VARIED", "*varied*")

            prop_pal_ctrl_service.add_string_edit_control(wpf_palette, prop, ctrl_props, value)

            return

        prop_pal_ctrl_service.add_edit_control(wpf_palette.AddLengthValue, prop, ctrl_props, prop.value)


    @staticmethod
    def update_by_constraint(build_ele : BuildingElement,
                             prop      : ParameterProperty.ParameterProperty,
                             ctrl_props: ControlProperties,
                             _name     : str):
        """ update by a constraint

        Args:
            build_ele:  building element with the parameter properties
            prop:       parameter property to update
            ctrl_props: control properties
            _name:      name of the modified value
        """

        prop.value = StringEvaluate.eval(ctrl_props.constraint[0],
                                         StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0]))


    @staticmethod
    def is_default_init_by_constraint(build_ele : BuildingElement,
                                      ctrl_props: ControlProperties) -> bool:
        """ check, whether the default value must be initialized by the constraint

        Args:
            build_ele:  building element with the parameter properties
            ctrl_props: control properties

        Returns:
            default init by the constraint state
        """

        prop = build_ele.get_existing_property(ctrl_props.value_name)

        if prop.persistent == ParameterProperty.ParameterProperty.Persistent.NO:
            return True

        constraint_name = ctrl_props.constraint[0].split(".")[0]

        if (prop := build_ele.get_property(constraint_name)) is None:
            return False

        return prop.value_type == ParameterPropertyValueTypes.PLANE_REFERENCES


    @staticmethod
    def value_to_unit_string(value: float) -> str:
        """ convert the value to the current unit value

        Args:
            value: value

        Returns:
            unit value as string
        """

        return AllplanSettings.UnitService.ToLengthUnitString(value)


    @classmethod
    def string_to_unit_value(cls,
                             value_str: str) -> float:
        """ convert the string to the unit value

        Args:
            value_str: value string

        Returns:
            unit value as string
        """

        error, value = AllplanSettings.UnitService.ConvertToMM(value_str)

        return 0 if error else value

```

</details>