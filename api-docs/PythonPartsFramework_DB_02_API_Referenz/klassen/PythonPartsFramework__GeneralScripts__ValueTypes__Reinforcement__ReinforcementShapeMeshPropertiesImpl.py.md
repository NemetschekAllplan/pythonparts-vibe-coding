---
title: "ReinforcementShapeMeshPropertiesImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinforcementShapeMeshPropertiesImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ReinforcementShapeMeshPropertiesImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Reinforcement\ReinforcementShapeMeshPropertiesImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `werte`

## Übersicht

implementation of the ReinforcementShapeMeshProperties value type

## Abhängigkeiten

- `BaseIntImpl`
- `ControlProperties`
- `NemAll_Python_Reinforcement`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `StdReinfShapeBuilder.ReinforcementShapeProperties`
- `Utilities.ConditionUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `typing`

## Klassen

### `ReinforcementShapeMeshPropertiesImpl`

implementation of the ReinforcementShapeMeshProperties value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: ReinforcementShapeProperties` | `str` | convert the shape mesh properties to a string  Args:     value: new value  Returns:     shape mesh properties as string |
| `get_value` | `value_str: str` | `ReinforcementShapeProperties` | get the shape mesh properties from a string  Args:     value_str: value string  Returns:     value from string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the ReinforcementShapeMeshProperties edit control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the ReinforcementShapeMeshProperties value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import NemAll_Python_Reinforcement as AllplanReinf

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil

from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties

from ..BaseIntImpl import BaseIntImpl
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ReinforcementShapeMeshPropertiesImpl(BaseIntImpl):
    """ implementation of the ReinforcementShapeMeshProperties value type
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

        match name.split(".", 1)[-1]:
            case "ConcreteGrade":
                prop.value.concrete_grade = value

            case "BendingRoller":
                prop.value.bending_roller = float(value)

            case "MeshType":
                prop.value.mesh_type = value

            case "MeshBendingDirection":
                prop.value.mesh_bending_direction = value

        return False


    @staticmethod
    def to_string(value: ReinforcementShapeProperties) -> str:
        """ convert the shape mesh properties to a string

        Args:
            value: new value

        Returns:
            shape mesh properties as string
        """

        return ValueToStringUtil.trim_value_string(value.to_reinforcementshapemeshproperties_string())


    @staticmethod
    def get_value(value_str: str) -> ReinforcementShapeProperties:
        """ get the shape mesh properties from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        bending_direction = StringToValueUtil.get_property_string(value_str, "MeshBendingDirection", "LongitudinalBars")

        mesh_type              = StringToValueUtil.get_property_string(value_str, "MeshType", "BT11")
        bending_roller         = StringToValueUtil.get_property_float(value_str, "BendingRoller", "4.0")
        mesh_bending_direction = AllplanReinf.MeshBendingDirection.LongitudinalBars if bending_direction == "LongitudinalBars" else \
                                 AllplanReinf.MeshBendingDirection.CrossBars
        concrete_grade         = StringToValueUtil.get_property_int(value_str, "ConcreteGrade", 4)

        return ReinforcementShapeProperties.mesh(mesh_type, mesh_bending_direction, bending_roller, concrete_grade,
                                                 AllplanReinf.BendingShapeType.LongitudinalBar)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the ReinforcementShapeMeshProperties edit control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        value      = prop.value
        value_name = ctrl_props.value_name
        str_table  = prop_pal_ctrl_service.global_str_table
        page_index = prop_pal_ctrl_service.page_index

        if ParameterPropertyValueType.is_visible(f"{value_name}.ConcreteGrade",  prop_visible_dict):
            wpf_palette.AddConcreteGrade(str_table.get_entry("e_CONCRETE_GRADE")[0],
                                         f"{value_name}.ConcreteGrade", value.concrete_grade,
                                         page_index, ctrl_props.expander_name, "",
                                         prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                         ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        if ParameterPropertyValueType.is_visible(f"{value_name}.MeshType",  prop_visible_dict):
            mesh_group = prop_pal_ctrl_service.build_ele.get_existing_property(ctrl_props.constraint[0]).value \
                         if ctrl_props.constraint else -1

            wpf_palette.AddMeshType(str_table.get_entry("e_MESH_TYPE")[0],
                                    f"{value_name}.MeshType", value.mesh_type,
                                    page_index, ctrl_props.expander_name, "",
                                    prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                    mesh_group, ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        if ParameterPropertyValueType.is_visible(f"{value_name}.MeshBendingDirection",  prop_visible_dict):
            wpf_palette.AddRadioButton("Bending direction",
                                       f"{value_name}.MeshBendingDirection", "Bending direction longitudinal",
                                       0, int(value.mesh_bending_direction),
                                       page_index, ctrl_props.expander_name, "",
                                       prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                       ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

            wpf_palette.AddRadioButton("Bending direction",
                                       f"{value_name}.MeshBendingDirection", "Bending direction cross",
                                       1, int(value.mesh_bending_direction),
                                       page_index, ctrl_props.expander_name, "",
                                       prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                       ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        if ParameterPropertyValueType.is_visible(f"{value_name}.BendingRoller",  prop_visible_dict):
            wpf_palette.AddBendingRollerValue(str_table.get_entry("e_BENDING_ROLLER")[0],
                                              f"{value_name}.BendingRoller", value.bending_roller,
                                              page_index, ctrl_props.expander_name, "",
                                              prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                              ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

```

</details>