---
title: "BSplineImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BSplineImpl.py"
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


# BSplineImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BSplineImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the Base class for the line value types

## Abhängigkeiten

- `BasePolyPointsImpl`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `ValueListUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `__future__`
- `typing`

## Klassen

### `BSplineImpl`

implementation of the base class for the b-spline value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `_visit_IsPeriodic` | `prop: ParameterProperty, _sep_count: int, name: str, value: bool` | `bool` | modify the periodic state  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `_visit_Degree` | `prop: ParameterProperty, _sep_count: int, name: str, value: int` | `bool` | modify the degree  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `_visit_KnotsCount` | `prop: ParameterProperty, _sep_count: int, name: str, value: int` | `bool` | modify the knots count  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `_visit_ShowKnots` | `prop: ParameterProperty, _sep_count: int, name: str, _value: Any` | `bool` | modify the ShowKnots state  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     _value:     new value  Returns:     palette update state |
| `_visit_Knots` | `prop: ParameterProperty, _sep_count: int, name: str, value: Any` | `bool` | modify the knots  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `_visit_WeightsCount` | `prop: ParameterProperty, _sep_count: int, name: str, value: int` | `bool` | modify the weights count  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `_visit_ShowWeights` | `prop: ParameterProperty, _sep_count: int, name: str, _value: Any` | `bool` | modify the ShowWeights state  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     _value:     new value  Returns:     palette update state |
| `_visit_Weights` | `prop: ParameterProperty, _sep_count: int, name: str, value: Any` | `bool` | modify the weights  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `__set_item_value` | `prop: ParameterProperty, name: str, value: Any, sub_item_name: str` | `bool` | Set the value of the item defined in the name  Args:     prop:          property     name:          name of the modified property     value:         new value     sub_item_name: sub item name  Returns:     update palette state |
| `_set_point_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the point defined in the name  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |

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

from typing import TYPE_CHECKING, Any

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties
from ValueListUtil import ValueListUtil

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextData
from .BasePolyPointsImpl import BasePolyPointsImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class BSplineImpl(BasePolyPointsImpl):
    """ implementation of the base class for the b-spline value types
    """

    ELEMENT_3D_KEY = "3d"

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

        if not ParameterPropertyValueType.is_visible(f"{prop.name}.Points",  prop_visible_dict):
            return

        wpf_palette.AddCheckboxValue(prop_pal_ctrl_service.global_str_table.get_entry("e_PERIODIC")[0],
                                     f"{prop.name}.IsPeriodic",
                                     prop.value.IsPeriodic, prop_pal_ctrl_service.page_index,
                                     ctrl_props.expander_name + ctrl_props.expander_state_key, "",
                                     prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        prop_pal_ctrl_service.add_int_edit_control(wpf_palette, f"{prop.name}.Degree", ctrl_props,
                                                   prop.value.Degree, 1, 3, "",
                                                   prop_pal_ctrl_service.global_str_table.get_entry("e_DEGREE")[0])


        #----------------- knots

        count_row_name = prop_pal_ctrl_service.global_str_table.get_entry("e_KNOTS_COUNT")[0]

        if ctrl_props.row_name.isnumeric():
            count_row_name = " " * int(ctrl_props.row_name) + count_row_name

        prop_pal_ctrl_service.add_int_edit_control(wpf_palette, f"{prop.name}.KnotsCount", ctrl_props,
                                                   len(prop.value.Knots), 0, 32000, count_row_name, "")

        if (visible_knots := getattr(prop.value, "ShowKnots", None)) is None:
            prop.value.ShowKnots = False

        file_name = "arrowup.png" if prop.value.ShowKnots else "arrowdown.png"

        wpf_palette.AddPictureButton("", f"{prop.name}.{GeneralConstants.PALETTE_BUTTON_SHOW_KNOTS_KEY}",
                                     AllplanSettings.AllplanPaths.GetPythonPartsEtcPath() + \
                                     "\\PythonPartsFramework\\GeneralScripts\\Bitmaps\\" + file_name,
                                     0, prop_pal_ctrl_service.page_index, ctrl_props.expander_name, count_row_name, True,
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        if visible_knots:
            for index, knot in enumerate(prop.value.Knots):
                prop_pal_ctrl_service.add_double_edit_control(wpf_palette, f"{prop.name}.Knots[{index}]",
                                                            ctrl_props, knot,  ctrl_props.min_value, ctrl_props.max_value,
                                                            PropertyPaletteControlTextData("", str(index + 1)))

        #----------------- weights

        count_row_name = prop_pal_ctrl_service.global_str_table.get_entry("e_WEIGHTS_COUNT")[0]

        if ctrl_props.row_name.isnumeric():
            count_row_name = " " * int(ctrl_props.row_name) + count_row_name

        prop_pal_ctrl_service.add_int_edit_control(wpf_palette, f"{prop.name}.{GeneralConstants.PALETTE_BUTTON_SHOW_WEIGHTS_KEY}",
                                                   ctrl_props, len(prop.value.Weights), 0, 32000, count_row_name, "")

        if (visible_weights := getattr(prop.value, "ShowWeights", None)) is None:
            prop.value.ShowWeights = False

        file_name = "arrowup.png" if prop.value.ShowWeights else "arrowdown.png"

        wpf_palette.AddPictureButton("", f"{prop.name}.ShowWeights",
                                     AllplanSettings.AllplanPaths.GetPythonPartsEtcPath() + \
                                     "\\PythonPartsFramework\\GeneralScripts\\Bitmaps\\" + file_name,
                                     0, prop_pal_ctrl_service.page_index, ctrl_props.expander_name, count_row_name, True,
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        if visible_weights:
            for index, weight in enumerate(prop.value.Weights):
                prop_pal_ctrl_service.add_double_edit_control(wpf_palette, f"{prop.name}.Weights[{index}]",
                                                            ctrl_props, weight, ctrl_props.min_value, ctrl_props.max_value,
                                                            PropertyPaletteControlTextData("", str(index + 1)))

        BasePolyPointsImpl.add_to_palette(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def _visit_IsPeriodic(prop      : ParameterProperty,
                          _sep_count: int,
                          name      : str,
                          value     : bool) -> bool:
        """ modify the periodic state

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        bspline = ParameterPropertyListUtil.get_item_value(prop, name)

        service = AllplanGeo.BSpline3DService(bspline)

        service.SetPeriodic(value)

        return True


    @staticmethod
    def _visit_Degree(prop      : ParameterProperty,
                          _sep_count: int,
                          name      : str,
                          value     : int) -> bool:
        """ modify the degree

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        bspline = ParameterPropertyListUtil.get_item_value(prop, name)

        service = AllplanGeo.BSpline3DService(bspline)

        service.SetDegree(value)

        return True


    @staticmethod
    def _visit_KnotsCount(prop      : ParameterProperty,
                          _sep_count: int,
                          name      : str,
                          value     : int) -> bool:
        """ modify the knots count

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        bspline = ParameterPropertyListUtil.get_item_value(prop, name)

        knots = bspline.Knots

        ValueListUtil.resize_1_dim_list(knots, value, 0.)

        bspline.Knots = knots

        return True


    @staticmethod
    def _visit_ShowKnots(prop      : ParameterProperty,
                          _sep_count: int,
                          name      : str,
                          _value    : Any) -> bool:
        """ modify the ShowKnots state

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            _value:     new value

        Returns:
            palette update state
        """

        bspline = ParameterPropertyListUtil.get_item_value(prop, name)

        bspline.ShowKnots = not bspline.ShowKnots

        return True


    @staticmethod
    def _visit_Knots(prop      : ParameterProperty,
                     _sep_count: int,
                     name      : str,
                     value     : Any) -> bool:
        """ modify the knots

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        return BSplineImpl.__set_item_value(prop, name, value, "Knots")


    @staticmethod
    def _visit_WeightsCount(prop      : ParameterProperty,
                            _sep_count: int,
                            name      : str,
                            value     : int) -> bool:
        """ modify the weights count

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        bspline = ParameterPropertyListUtil.get_item_value(prop, name)

        weights = bspline.Weights

        ValueListUtil.resize_1_dim_list(weights, value, 0.)

        bspline.Weights = weights

        return True


    @staticmethod
    def _visit_ShowWeights(prop      : ParameterProperty,
                           _sep_count: int,
                           name      : str,
                           _value    : Any) -> bool:
        """ modify the ShowWeights state

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            _value:     new value

        Returns:
            palette update state
        """

        bspline = ParameterPropertyListUtil.get_item_value(prop, name)

        bspline.ShowWeights = not bspline.ShowWeights

        return True


    @staticmethod
    def _visit_Weights(prop      : ParameterProperty,
                       _sep_count: int,
                       name      : str,
                       value     : Any) -> bool:
        """ modify the weights

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        return BSplineImpl.__set_item_value(prop, name, value, "Weights")


    @staticmethod
    def __set_item_value(prop         : ParameterProperty,
                         name         : str,
                         value        : Any,
                         sub_item_name: str) -> bool:
        """ Set the value of the item defined in the name

        Args:
            prop:          property
            name:          name of the modified property
            value:         new value
            sub_item_name: sub item name

        Returns:
            update palette state
        """

        if (list_index := ParameterPropertyListUtil.get_list_index_2dim(name)) is not None:
            bspline = prop.value[list_index[0]]
            items   = getattr(bspline, sub_item_name)

            items[list_index[1]] = value

            setattr(bspline, sub_item_name, items)

            return False

        if (index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            items = getattr(prop.value, sub_item_name)

            items[index] = value

            setattr(prop.value, sub_item_name, items)

            return False

        prop.value = value

        return False


    @staticmethod
    def _set_point_value(prop : ParameterProperty,
                         name : str,
                         value: Any) -> bool:
        """ Set the value of the point defined in the name

        Args:
            prop:  property
            name:  name of the modified property
            value: new value

        Returns:
            update palette state
        """

        if (list_index := ParameterPropertyListUtil.get_list_index_2dim(name)) is not None:
            item_value = prop.value[list_index[0]]

            service = AllplanGeo.BSpline3DService(item_value)

            service.SetControlPoint(list_index[1], value)

            return False

        if (index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            service = AllplanGeo.BSpline3DService(prop.value)

            service.SetControlPoint(index, value)

            return False

        prop.value = value

        return False

```

</details>