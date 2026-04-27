---
title: "CircleImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\CircleImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# CircleImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\CircleImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the base class for the circle value types

## Abhängigkeiten

- `ArcVisitors`
- `ControlProperties`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `Utilities.ConditionUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.PropertyPaletteGeometryControlService`
- `__future__`
- `typing`

## Klassen

### `CircleImpl`

implementation of the base class for the circle value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanGeo.Arc2D | AllplanGeo.Arc3D` | `str` | convert the circle to a string  Args:     value: circle value  Returns:     circle as string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base class for the circle value types
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil

from .ArcVisitors import ArcVisitors
from .CoordinateValueUtil import CoordinateValueUtil

from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextUtil
from ..ValueTypeUtils.PropertyPaletteGeometryControlService import PropertyPaletteGeometryControlService

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class CircleImpl(ParameterPropertyValueType):
    """ implementation of the base class for the circle value types
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

        if value is None:
            return False

        prop.is_modified = True


        #----------------- assign the new value in case of a full element

        sep_count = name.count(".")

        if CoordinateValueUtil.SUB_NAME_SEPARATOR not in name and not sep_count:
            prop.value = value

            return True


        #----------------- part can't be an empty list

        if value == []:
            return False


        #----------------- set the new value

        visit_key = f"visit_{name.split('.', 2)[1]}"

        arc = ParameterPropertyListUtil.get_item_value(prop, name)

        if (visitor := getattr(ArcVisitors, visit_key, None)) is not None:
            visitor(arc, sep_count, name, value)

        if visit_key == "visit_MajorRadius":                                            # pylint: disable=magic-value-comparison
            getattr(ArcVisitors, "visit_MinorRadius")(arc, sep_count, name, value)

        return False


    @staticmethod
    def to_string(value: (AllplanGeo.Arc2D | AllplanGeo.Arc3D)) -> str:
        """ convert the circle to a string

        Args:
            value: circle value

        Returns:
            circle as string
        """

        return str(value).replace("\n", "").replace(" ", "")


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the control to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        is_3d_arc = isinstance(prop.value, AllplanGeo.Arc3D)

        text_util = PropertyPaletteControlTextUtil(prop_pal_ctrl_service.global_str_table)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.CenterPoint",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.Center, "CenterPoint",
                                                                     text_util.get_row_name_text(ctrl_props, "CenterPoint",
                                                                                                 "e_CENTER_POINT"),
                                                                     is_3d_arc, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.MajorRadius",  prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.MajorRadius",  ctrl_props,  prop.value.MajorRadius,
                                                          ctrl_props.min_value, ctrl_props.max_value,
                                                          text_util.get_row_name_text(ctrl_props, "MajorRadius", "e_RADIUS"))

        if is_3d_arc and ParameterPropertyValueType.is_visible(f"{prop.name}.ZAxis",  prop_visible_dict):
            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, prop.name, ctrl_props,
                                                                     prop.value.GetZAxis() * 1000, "ZAxis",
                                                                     text_util.get_row_name_text(ctrl_props, "ZAxis", "e_Z_AXIS"),
                                                                     is_3d_arc, prop_pal_ctrl_service)

```

</details>