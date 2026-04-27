---
title: "ArcVisitors"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\ArcVisitors.py"
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


# ArcVisitors

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\ArcVisitors.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the arc visitors for the property modification

## Abhängigkeiten

- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `collections.abc`
- `typing`

## Klassen

### `ArcVisitors`

implementation of the arc visitors for the property modification
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `visit_CenterPoint` | `arc: ArcTypes, sep_count: int, name: str, value: Any` | `None` | modify the center point  Args:     arc:       arc(s)     sep_count: sub value separator count     name:      name of the modified property     value:     new value |
| `visit_MinorRadius` | `arc: ArcTypes, _sep_count: int, _name: str, value: Any` | `None` | modify the minor radius  Args:     arc:        arc(s)     _sep_count: sub value separator count     _name:      name of the modified property     value:      new value |
| `visit_MajorRadius` | `arc: ArcTypes, _sep_count: int, _name: str, value: Any` | `None` | modify the major radius  Args:     arc:        arc(s)     _sep_count: sub value separator count     _name:      name of the modified property     value:      new value |
| `visit_AxisAngle` | `arc: AllplanGeo.Arc2D | list[AllplanGeo.Arc2D], _sep_count: int, _name: str, value: Any` | `None` | modify the axis angle  Args:     arc:        arc(s)     _sep_count: sub value separator count     _name:      name of the modified property     value:      new value |
| `visit_StartAngle` | `arc: ArcTypes, _sep_count: int, _name: str, value: Any` | `None` | modify the start angle  Args:     arc:        arc(s)     _sep_count: sub value separator count     _name:      name of the modified property     value:      new value |
| `visit_EndAngle` | `arc: ArcTypes, _sep_count: int, _name: str, value: Any` | `None` | modify the end angle  Args:     arc:        arc(s)     _sep_count: sub value separator count     _name:      name of the modified property     value:      new value |
| `visit_ArcLength` | `arc: AllplanGeo.Arc2D, _sep_count: int, _name: str, value: Any` | `None` | modify the end angle by arc length  Args:     arc:        arc(s)     _sep_count: sub value separator count     _name:      name of the modified property     value:      new value |
| `visit_XDirection` | `arc: AllplanGeo.Arc3D | list[AllplanGeo.Arc3D], sep_count: int, name: str, value: Any` | `None` | modify the x axis  Args:     arc:       arc(s)     sep_count: sub value separator count     name:      name of the modified property     value:     new value |
| `visit_ZAxis` | `arc: AllplanGeo.Arc3D | list[AllplanGeo.Arc3D], sep_count: int, name: str, value: Any` | `None` | modify the z axis  Args:     arc:       arc(s)     sep_count: sub value separator count     name:      name of the modified property     value:     new value |
| `__set_axis` | `arc: AllplanGeo.Arc3D | list[AllplanGeo.Arc3D], sep_count: int, name: str, value: Any, axis_fct: Callable[[Any, Any], None], axis_coord_fct: Callable[[Any, str, Any], None]` | `None` | modify the z axis  Args:     arc:            arc(s)     sep_count:      sub value separator count     name:           name of the modified property     value:          new value     axis_fct:       axis function     axis_coord_fct: axis coordinate function |
| `__set_x_axis` | `arc: AllplanGeo.Arc3D, value: AllplanGeo.Vector3D` | `None` | set the x axis  Args:     arc:   arc     value: x axis |
| `__set_x_axis_coord` | `arc: AllplanGeo.Arc3D, name: str, value: AllplanGeo.Vector3D` | `None` | set the x axis  Args:     arc:   arc     name:  name of the modified property     value: x axis |
| `__set_z_axis` | `arc: AllplanGeo.Arc3D, value: AllplanGeo.Vector3D` | `None` | set the z axis  Args:     arc:   arc     value: z axis |
| `__set_z_axis_coord` | `arc: AllplanGeo.Arc3D, name: str, value: AllplanGeo.Vector3D` | `None` | set the z axis  Args:     arc:   arc     name:  name of the modified property     value: z axis |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the arc visitors for the property modification
"""

# pylint: disable=invalid-name

from typing import Any

from collections.abc import Callable

import NemAll_Python_Geometry as AllplanGeo

from .CoordinateValueUtil import CoordinateValueUtil
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

ArcTypes = AllplanGeo.Arc2D | AllplanGeo.Arc3D | list[AllplanGeo.Arc2D] | list[AllplanGeo.Arc3D]

class ArcVisitors():
    """ implementation of the arc visitors for the property modification
    """

    @staticmethod
    def visit_CenterPoint(arc      : ArcTypes,
                          sep_count: int,
                          name     : str,
                          value    : Any):
        """ modify the center point

        Args:
            arc:       arc(s)
            sep_count: sub value separator count
            name:      name of the modified property
            value:     new value
        """

        if sep_count == 1:
            ParameterPropertyListUtil.set_sub_item_value(arc, "Center", value)

        else:
            CoordinateValueUtil.set_sub_item_coordinate_value(arc, name.replace("CenterPoint", "Center"), value)


    @staticmethod
    def visit_MinorRadius(arc       : ArcTypes,
                          _sep_count: int,
                          _name     : str,
                          value     : Any):
        """ modify the minor radius

        Args:
            arc:        arc(s)
            _sep_count: sub value separator count
            _name:      name of the modified property
            value:      new value
        """

        ParameterPropertyListUtil.set_sub_item_value(arc, "MinorRadius", value)


    @staticmethod
    def visit_MajorRadius(arc       : ArcTypes,
                          _sep_count: int,
                          _name     : str,
                          value     : Any):
        """ modify the major radius

        Args:
            arc:        arc(s)
            _sep_count: sub value separator count
            _name:      name of the modified property
            value:      new value
        """

        ParameterPropertyListUtil.set_sub_item_value(arc, "MajorRadius", value)


    @staticmethod
    def visit_AxisAngle(arc       : (AllplanGeo.Arc2D | list[AllplanGeo.Arc2D]),
                        _sep_count: int,
                        _name     : str,
                        value     : Any):
        """ modify the axis angle

        Args:
            arc:        arc(s)
            _sep_count: sub value separator count
            _name:      name of the modified property
            value:      new value
        """

        ParameterPropertyListUtil.set_sub_item_angle_value(arc, "AxisAngle", value)


    @staticmethod
    def visit_StartAngle(arc       : ArcTypes,
                         _sep_count: int,
                         _name     : str,
                         value     : Any):
        """ modify the start angle

        Args:
            arc:        arc(s)
            _sep_count: sub value separator count
            _name:      name of the modified property
            value:      new value
        """

        ParameterPropertyListUtil.set_sub_item_angle_value(arc, "StartAngle", value)


    @staticmethod
    def visit_EndAngle(arc       : ArcTypes,
                       _sep_count: int,
                       _name     : str,
                       value     : Any):
        """ modify the end angle

        Args:
            arc:        arc(s)
            _sep_count: sub value separator count
            _name:      name of the modified property
            value:      new value
        """

        ParameterPropertyListUtil.set_sub_item_angle_value(arc, "EndAngle", value)


    @staticmethod
    def visit_ArcLength(arc       : AllplanGeo.Arc2D,
                        _sep_count: int,
                        _name     : str,
                        value     : Any):
        """ modify the end angle by arc length

        Args:
            arc:        arc(s)
            _sep_count: sub value separator count
            _name:      name of the modified property
            value:      new value
        """

        end_angle = arc.StartAngle + value / arc.MajorRadius

        ParameterPropertyListUtil.set_sub_item_angle_value(arc, "EndAngle", end_angle)


    @staticmethod
    def visit_XDirection(arc      : (AllplanGeo.Arc3D | list[AllplanGeo.Arc3D]),
                         sep_count: int,
                         name     : str,
                         value    : Any):
        """ modify the x axis

        Args:
            arc:       arc(s)
            sep_count: sub value separator count
            name:      name of the modified property
            value:     new value
        """

        ArcVisitors.__set_axis(arc, sep_count, name, value, ArcVisitors.__set_x_axis, ArcVisitors.__set_x_axis_coord)


    @staticmethod
    def visit_ZAxis(arc      : (AllplanGeo.Arc3D | list[AllplanGeo.Arc3D]),
                    sep_count: int,
                    name     : str,
                    value    : Any):
        """ modify the z axis

        Args:
            arc:       arc(s)
            sep_count: sub value separator count
            name:      name of the modified property
            value:     new value
        """

        ArcVisitors.__set_axis(arc, sep_count, name, value, ArcVisitors.__set_z_axis, ArcVisitors.__set_z_axis_coord)


    @staticmethod
    def __set_axis(arc           : (AllplanGeo.Arc3D | list[AllplanGeo.Arc3D]),
                   sep_count     : int,
                   name          : str,
                   value         : Any,
                   axis_fct      : Callable[[Any, Any], None],
                   axis_coord_fct: Callable[[Any, str, Any], None]):
        """ modify the z axis

        Args:
            arc:            arc(s)
            sep_count:      sub value separator count
            name:           name of the modified property
            value:          new value
            axis_fct:       axis function
            axis_coord_fct: axis coordinate function
        """

        #------------- vector value

        if sep_count == 1:
            if isinstance(arc, list):
                for item in arc:
                    axis_fct(item, value)
            else:
                axis_fct(arc, value)


        #------------- coordinate part value

        elif isinstance(arc, list):
            for item in arc:
                axis_coord_fct(item, name, value)

        else:
            axis_coord_fct(arc, name, value)


    @staticmethod
    def __set_x_axis(arc  : AllplanGeo.Arc3D,
                     value: AllplanGeo.Vector3D):
        """ set the x axis

        Args:
            arc:   arc
            value: x axis
        """

        placement            = arc.GetRefPlacement()
        placement.XDirection = value

        placement.XDirection.Normalize()

        arc.SetRefPlacement(placement)


    @staticmethod
    def __set_x_axis_coord(arc  : AllplanGeo.Arc3D,
                           name : str,
                           value: AllplanGeo.Vector3D):
        """ set the x axis

        Args:
            arc:   arc
            name:  name of the modified property
            value: x axis
        """

        placement            = arc.GetRefPlacement()
        placement.XDirection = CoordinateValueUtil.set_coordinate_value(placement.XDirection, name, value)

        placement.XDirection.Normalize()

        arc.SetRefPlacement(placement)


    @staticmethod
    def __set_z_axis(arc  : AllplanGeo.Arc3D,
                     value: AllplanGeo.Vector3D):
        """ set the z axis

        Args:
            arc:   arc
            value: z axis
        """

        placement            = arc.GetRefPlacement()
        placement.ZDirection = value

        placement.ZDirection.Normalize()

        arc.SetRefPlacement(placement)


    @staticmethod
    def __set_z_axis_coord(arc  : AllplanGeo.Arc3D,
                           name : str,
                           value: AllplanGeo.Vector3D):
        """ set the z axis

        Args:
            arc:   arc
            name:  name of the modified property
            value: z axis
        """

        placement            = arc.GetRefPlacement()
        placement.ZDirection = CoordinateValueUtil.set_coordinate_value(placement.ZDirection, name, value)

        placement.ZDirection.Normalize()

        arc.SetRefPlacement(placement)

```

</details>