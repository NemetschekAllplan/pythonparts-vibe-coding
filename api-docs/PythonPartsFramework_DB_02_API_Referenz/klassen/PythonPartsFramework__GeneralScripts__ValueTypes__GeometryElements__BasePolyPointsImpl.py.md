---
title: "BasePolyPointsImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BasePolyPointsImpl.py"
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


# BasePolyPointsImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\BasePolyPointsImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the base class for the poly points element value types

## Abhängigkeiten

- `ControlProperties`
- `CoordinateValueUtil`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ParameterPropertyValueTypes`
- `TypeCollections.GeometryTyping`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `ValueListUtil`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.PropertyPaletteGeometryControlService`
- `__future__`
- `typing`

## Klassen

### `BasePolyPointsImpl`

implementation of the base class for the poly points element value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `cls, prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `__set_points_value` | `cls: type, prop: ParameterProperty, name: str, value: Any` | `bool` | se the points value  Args:     prop:  parameter property     name:  name of the modified property     value: line value  Returns:     update palette state |
| `_set_point_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the point defined in the name  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `__adapt_polygon_end_point` | `prop: ParameterProperty` | `None` | adapt the end points of the polygons to the start point  Args:     prop: parameter property |
| `_visit_ShowPoints` | `prop: ParameterProperty, _sep_count: int, name: str, _value: Any` | `bool` | modify the ShowPoints state  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     _value:     new value  Returns:     palette update state |
| `_visit_Count` | `prop: ParameterProperty, _sep_count: int, name: str, value: Any` | `bool` | modify the point count  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `_visit_Points` | `prop: ParameterProperty, _sep_count: int, name: str, value: Any` | `bool` | modify the Points  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `_visit_SegmentLength` | `prop: ParameterProperty, _sep_count: int, name: str, value: Any` | `bool` | modify the segment length  Args:     prop:       parameter property     _sep_count: sub value separator count     name:       name of the modified property     value:      new value  Returns:     palette update state |
| `to_string` | `value: AllplanGeo.Line2D | AllplanGeo.Line3D` | `str` | convert the line to a string  Args:     value: line value  Returns:     line as string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__add_points` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService, is_coord_3d: bool, count: int` | `None` | add the points to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service     is_coord_3d:           3D coordinate state     count:                 point count |
| `get_min_value` | `-` | `float` | get the minimal value  Returns:     get the minimal value |
| `get_max_value` | `-` | `float` | get the maximal value  Returns:     get the maximal value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base class for the poly points element value types
"""

# pylint: disable=invalid-name
# pylint: disable=unused-private-member

from __future__ import annotations

from typing import Any, TYPE_CHECKING

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties
from ValueListUtil import ValueListUtil

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from TypeCollections.GeometryTyping import POLY_CURVES_2D

from .CoordinateValueUtil import CoordinateValueUtil
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextData
from ..ValueTypeUtils.PropertyPaletteGeometryControlService import PropertyPaletteGeometryControlService

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class BasePolyPointsImpl(ParameterPropertyValueType):
    """ implementation of the base class for the poly points element value types
    """

    ELEMENT_3D_KEY = "3d"

    @classmethod
    def set_property_value(cls,
                           prop : ParameterProperty,
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

        if CoordinateValueUtil.SUB_NAME_SEPARATOR not in name and not sep_count and GeneralConstants.LIST_SEPARATOR_START not in name:
            prop.value = value

            return True


        #----------------- part can't be an empty list

        if value == []:
            return False


        #----------------- set the new value

        if sep_count:
            visit_key = f"_visit_{name.split('.', 2)[1].replace(GeneralConstants.PALETTE_BUTTON_KEY, '')}"

            visit_key = visit_key.split("[", 1)[0]

            if (visitor := getattr(cls, visit_key, None)) is not None:
                return visitor(prop, sep_count, name, value)

        return cls.__set_points_value(prop, name, value)


    @classmethod
    def __set_points_value(cls  : type,
                           prop : ParameterProperty,
                           name : str,
                           value: Any) -> bool:
        """ se the points value

        Args:
            prop:  parameter property
            name:  name of the modified property
            value: line value

        Returns:
            update palette state
        """

        #----------------- resize a list

        if isinstance(value, list):
            if isinstance(prop.value, list):
                ValueListUtil.resize_2_dim_list(value, prop.value)
            else:
                prop.value = ValueListUtil.create_value_list(prop, value)


        #----------------- assign the new value

        coord = ParameterPropertyListUtil.get_item_value(prop, name)

        getattr(cls, "_set_point_value")(prop, name, CoordinateValueUtil.set_coordinate_value(coord, name, value))

        if prop.value_type in (ParameterPropertyValueTypes.POLYGON2D, ParameterPropertyValueTypes.POLYGON3D):
            BasePolyPointsImpl.__adapt_polygon_end_point(prop)

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

            item_value.SetPoint(value, list_index[1])

            return False

        if (index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            prop.value.SetPoint(value, index)

            return False

        prop.value = value

        return False


    @staticmethod
    def __adapt_polygon_end_point(prop: ParameterProperty):
        """ adapt the end points of the polygons to the start point

        Args:
            prop: parameter property
        """

        if isinstance(prop.value, list):
            for polygon in prop.value:
                polygon.EndPoint = polygon.StartPoint
        else:
            prop.value.EndPoint = prop.value.StartPoint


    @staticmethod
    def _visit_ShowPoints(prop      : ParameterProperty,
                          _sep_count: int,
                          name      : str,
                          _value    : Any) -> bool:
        """ modify the ShowPoints state

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            _value:     new value

        Returns:
            palette update state
        """

        poly = ParameterPropertyListUtil.get_item_value(prop, name)

        poly.ShowPoints = not poly.ShowPoints

        return True


    @staticmethod
    def _visit_Count(prop      : ParameterProperty,
                     _sep_count: int,
                     name      : str,
                     value     : Any) -> bool:
        """ modify the point count

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        poly = ParameterPropertyListUtil.get_item_value(prop, name)

        if prop.value_type in (ParameterPropertyValueTypes.POLYGON2D, ParameterPropertyValueTypes.POLYGON3D):
            value += 1

        if poly.Count() == value:
            return False

        if poly.Count() > value:
            poly.Resize(value)

            if prop.value_type in (ParameterPropertyValueTypes.POLYGON2D, ParameterPropertyValueTypes.POLYGON3D):
                poly.EndPoint = poly.StartPoint

            return True


        #----------------- get the point to add

        if poly.Count():                # pylint: disable=consider-ternary-expression
            point = poly.EndPoint
        else:
            point = AllplanGeo.Point3D() if BasePolyPointsImpl.ELEMENT_3D_KEY in prop.value_type else AllplanGeo.Point2D()

        for _ in range(poly.Count(), value):
            poly += point

        if prop.value_type in (ParameterPropertyValueTypes.POLYGON2D, ParameterPropertyValueTypes.POLYGON3D):
            poly.EndPoint = poly.StartPoint

        return True


    @staticmethod
    def _visit_Points(prop      : ParameterProperty,
                      _sep_count: int,
                      name      : str,
                      value     : Any) -> bool:
        """ modify the Points

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        poly = ParameterPropertyListUtil.get_item_value(prop, name)

        poly.Clear()

        for item in value:
            if isinstance(item, list):
                for pnt in item:
                    poly += pnt
            else:
                poly += item

        if prop.value_type not in (ParameterPropertyValueTypes.POLYGON2D, ParameterPropertyValueTypes.POLYGON3D):
            return True

        if poly.StartPoint != poly.EndPoint:
            poly += poly.StartPoint

        return True


    @staticmethod
    def _visit_SegmentLength(prop      : ParameterProperty,
                             _sep_count: int,
                             name      : str,
                             value     : Any) -> bool:
        """ modify the segment length

        Args:
            prop:       parameter property
            _sep_count: sub value separator count
            name:       name of the modified property
            value:      new value

        Returns:
            palette update state
        """

        poly = prop.value

        if (index := ParameterPropertyListUtil.get_list_index(name)) is None:
            return False

        start_pnt = poly[index]
        end_pnt   = poly[index + 1]

        if isinstance(poly, POLY_CURVES_2D):
            line = AllplanGeo.Line2D(start_pnt, end_pnt)

            line.Extend(value - AllplanGeo.CalcLength(line))

            poly[index + 1] = line.EndPoint

        else:
            line = AllplanGeo.Line3D(start_pnt, end_pnt)

            line.TrimEnd(AllplanGeo.CalcLength(line) - value)

            poly[index + 1] = line.EndPoint

        return True


    @staticmethod
    def to_string(value: (AllplanGeo.Line2D | AllplanGeo.Line3D)) -> str:
        """ convert the line to a string

        Args:
            value: line value

        Returns:
            line as string
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

        if not ParameterPropertyValueType.is_visible(f"{prop.name}.Points",  prop_visible_dict):
            return

        is_coord_3d = BasePolyPointsImpl.ELEMENT_3D_KEY in prop.value_type


        #----------------- add the control for the point count

        count_row_name = prop_pal_ctrl_service.global_str_table.get_entry("e_POINT_COUNT")[0]

        if ctrl_props.row_name.isnumeric():
            count_row_name = " " * int(ctrl_props.row_name) + count_row_name

        min_value = ctrl_props.min_value

        is_polygon = prop.value_type in (ParameterPropertyValueTypes.POLYGON2D, ParameterPropertyValueTypes.POLYGON3D)

        ctrl_props.min_value = 3 if is_polygon else 2
        ctrl_props.min_value = 32000

        count = prop.value.Count() - 1 if is_polygon else prop.value.Count()

        prop_pal_ctrl_service.add_int_edit_control(wpf_palette, f"{prop.name}.Count", ctrl_props,
                                                   count, 1, 32000, count_row_name, "")

        ctrl_props.min_value = min_value


        #----------------- add the "show points" button

        if (visible_points := getattr(prop.value, "ShowPoints", None)) is None:
            prop.value.ShowPoints = False

        file_name = "arrowup.png" if prop.value.ShowPoints else "arrowdown.png"

        wpf_palette.AddPictureButton("", f"{prop.name}.{GeneralConstants.PALETTE_BUTTON_SHOW_POINT_KEY}",
                                     AllplanSettings.AllplanPaths.GetPythonPartsEtcPath() + \
                                     "\\PythonPartsFramework\\GeneralScripts\\Bitmaps\\" + file_name,
                                     0, prop_pal_ctrl_service.page_index, ctrl_props.expander_name, count_row_name, True,
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        if visible_points:
            BasePolyPointsImpl.__add_points(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service, is_coord_3d, count)


    @staticmethod
    def __add_points(wpf_palette          : WpfPaletteBuilder,
                     prop                 : ParameterProperty,
                     ctrl_props           : ControlProperties,
                     prop_pal_ctrl_service: PropertyPaletteControlService,
                     is_coord_3d          : bool,
                     count                : int):
        """ add the points to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
            is_coord_3d:           3D coordinate state
            count:                 point count
        """

        row_name = ctrl_props.row_name

        for index in range(0, count):
            text = f"{ctrl_props.text} {index + 1}"

            if row_name:
                row_name = text if ctrl_props.text else str(index + 1)

            PropertyPaletteGeometryControlService.add_xyz_to_palette(wpf_palette, f"{prop.name}[{index}]",
                                                                     ctrl_props,  prop.value[index],  "",
                                                                     PropertyPaletteControlTextData(row_name, text),
                                                                     is_coord_3d, prop_pal_ctrl_service)


    @staticmethod
    def get_min_value() -> float:
        """ get the minimal value

        Returns:
            get the minimal value
        """

        return -1.7976931348623157e+300


    @staticmethod
    def get_max_value() -> float:
        """ get the maximal value

        Returns:
            get the maximal value
        """

        return 1.7976931348623157e+300

```

</details>