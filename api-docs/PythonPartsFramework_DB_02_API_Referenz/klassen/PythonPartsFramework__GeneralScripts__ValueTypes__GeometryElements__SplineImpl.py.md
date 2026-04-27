---
title: "SplineImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\SplineImpl.py"
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


# SplineImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\SplineImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Base class for the line value types

## Abhängigkeiten

- `BasePolyPointsImpl`
- `ControlProperties`
- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ParameterPropertyValueTypes`
- `Utilities.ConditionUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.PropertyPaletteGeometryControlService`
- `__future__`
- `typing`

## Klassen

### `SplineImpl`

implementation of the base class for the spline value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the controls to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `_visit_StartVector` | `prop: ParameterProperty, sep_count: int, name: str, value: Any` | `bool` | modify the start vector  Args:     prop:      parameter property     sep_count: sub value separator count     name:      name of the modified property     value:     new value  Returns:     palette update state |
| `_visit_EndVector` | `prop: ParameterProperty, sep_count: int, name: str, value: Any` | `bool` | modify the end vector  Args:     prop:      parameter property     sep_count: sub value separator count     name:      name of the modified property     value:     new value  Returns:     palette update state |
| `_visit_IsPeriodic` | `prop: ParameterProperty, _sep_count: int, name: str, value: Any` | `bool` | modify the periodic state  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Base class for the line value types
"""

# pylint: disable=invalid-name
# pylint: disable=unused-private-member

from __future__ import annotations

from typing import TYPE_CHECKING, cast, Any

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil

from .BasePolyPointsImpl import BasePolyPointsImpl
from .CoordinateValueUtil import CoordinateValueUtil

from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ..ValueTypeUtils.PropertyPaletteGeometryControlService import PropertyPaletteGeometryControlService

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class SplineImpl(BasePolyPointsImpl):
    """ implementation of the base class for the spline value types
    """

    ELEMENT_3D_KEY = "3d"

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the controls to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        if not ParameterPropertyValueType.is_visible(f"{prop.name}.Points",  prop_visible_dict):
            return

        is_coord_3d = SplineImpl.ELEMENT_3D_KEY in prop.value_type

        is_periodic = prop.value_type == ParameterPropertyValueTypes.SPLINE3D and cast(AllplanGeo.Spline3D, prop.value).IsPeriodic

        if prop.value_type == ParameterPropertyValueTypes.SPLINE3D:
            wpf_palette.AddCheckboxValue(prop_pal_ctrl_service.global_str_table.get_entry("e_PERIODIC")[0],
                                         f"{prop.name}.IsPeriodic",
                                         is_periodic, prop_pal_ctrl_service.page_index,
                                         ctrl_props.expander_name + ctrl_props.expander_state_key, "",
                                         prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                         ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)


        #----------------- add the spline vectors

        text_util = PropertyPaletteControlTextUtil(prop_pal_ctrl_service.global_str_table)

        text = ctrl_props.text

        ctrl_props.text = ""

        if ParameterPropertyValueType.is_visible(f"{prop.name}.StartVector",  prop_visible_dict) and not is_periodic:
            PropertyPaletteGeometryControlService.add_direction_vector_to_palette(
                                                                    wpf_palette, prop.name, ctrl_props,
                                                                    prop.value.StartVector, "StartVector",
                                                                    text_util.get_row_name_text(ctrl_props,
                                                                                                "StartVector", "e_START_VECTOR"),
                                                                    is_coord_3d, prop_pal_ctrl_service)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.EndVector",  prop_visible_dict) and not is_periodic:
            PropertyPaletteGeometryControlService.add_direction_vector_to_palette(
                                                                    wpf_palette, prop.name, ctrl_props,
                                                                    prop.value.EndVector, "EndVector",
                                                                    text_util.get_row_name_text(ctrl_props,
                                                                                                "EndVector", "e_END_VECTOR"),
                                                                    is_coord_3d, prop_pal_ctrl_service)

        ctrl_props.text = text

        BasePolyPointsImpl.add_to_palette(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def _visit_StartVector(prop     : ParameterProperty,
                           sep_count: int,
                           name     : str,
                           value    : Any) -> bool:
        """ modify the start vector

        Args:
            prop:      parameter property
            sep_count: sub value separator count
            name:      name of the modified property
            value:     new value

        Returns:
            palette update state
        """

        spline = ParameterPropertyListUtil.get_item_value(prop, name)

        if sep_count == 1:
            spline.StartVector = value

        else:
            CoordinateValueUtil.set_sub_item_coordinate_value(spline, name, value)

        vec = spline.StartVector

        vec.Normalize()

        spline.StartVector = vec

        return False


    @staticmethod
    def _visit_EndVector(prop     : ParameterProperty,
                         sep_count: int,
                         name     : str,
                         value    : Any) -> bool:
        """ modify the end vector

        Args:
            prop:      parameter property
            sep_count: sub value separator count
            name:      name of the modified property
            value:     new value

        Returns:
            palette update state
        """

        spline = ParameterPropertyListUtil.get_item_value(prop, name)

        if sep_count == 1:
            spline.EndVector = value

        else:
            CoordinateValueUtil.set_sub_item_coordinate_value(spline, name, value)

        vec = spline.EndVector

        vec.Normalize()

        spline.EndVector = vec

        return False


    @staticmethod
    def _visit_IsPeriodic(prop      : ParameterProperty,
                          _sep_count: int,
                          name      : str,
                          value     : Any) -> bool:
        """ modify the periodic state

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        spline = ParameterPropertyListUtil.get_item_value(prop, name)

        spline.IsPeriodic = value

        return True

```

</details>