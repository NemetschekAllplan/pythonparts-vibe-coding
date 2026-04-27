---
title: "LineVisitors"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\LineVisitors.py"
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


# LineVisitors

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\LineVisitors.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the line visitors for the property modification

## Abhängigkeiten

- `CoordinateValueUtil`
- `NemAll_Python_Geometry`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `collections.abc`
- `typing`

## Klassen

### `LineVisitors`

implementation of the line visitors for the property modification
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `visit_StartPoint` | `line: LINE_TYPES, sep_count: int, name: str, value: Any` | `None` | modify the start point  Args:     line:      line     sep_count: separator count     name:      name of the modified property     value:     new value |
| `visit_EndPoint` | `line: LINE_TYPES, sep_count: int, name: str, value: Any` | `None` | modify the end point  Args:     line:      line     sep_count: separator count     name:      name of the modified property     value:     new value |
| `visit_Length` | `line: LINE_TYPES, _sep_count: int, _name: str, value: Any` | `None` | modify the end point by the length  Args:     line:       line     _sep_count: separator count     _name:      name of the modified property     value:      new value |
| `visit_DeltaX` | `line: LINE_TYPES, _sep_count: int, _name: str, value: Any` | `None` | modify the end point by the delta x  Args:     line:       line     _sep_count: separator count     _name:      name of the modified property     value:      new value |
| `visit_DeltaY` | `line: LINE_TYPES, _sep_count: int, _name: str, value: Any` | `None` | modify the end point by the delta y  Args:     line:       line     _sep_count: separator count     _name:      name of the modified property     value:      new value |
| `visit_DeltaZ` | `line: LINE_TYPES, _sep_count: int, _name: str, value: Any` | `None` | modify the end point by the delta z  Args:     line:       line     _sep_count: separator count     _name:      name of the modified property     value:      new value |
| `visit_Angle` | `line: LINE_TYPES, _sep_count: int, _name: str, value: Any` | `None` | modify the end point by the angle  Args:     line:       line     _sep_count: separator count     _name:      name of the modified property     value:      new value |
| `__set_end_point` | `line: LINE_TYPES, value: float, end_pnt_fct: Callable[[AllplanGeo.Line2D | AllplanGeo.Line3D, float], None]` | `None` | modify the end point  Args:     line:        line(s)     value:       new value     end_pnt_fct: end point function |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the line visitors for the property modification
"""

# pylint: disable=invalid-name

from typing import Any, cast

from collections.abc import Callable

import NemAll_Python_Geometry as AllplanGeo

from .CoordinateValueUtil import CoordinateValueUtil
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

LINE_TYPES = AllplanGeo.Line2D | AllplanGeo.Line3D | list[AllplanGeo.Line2D] | list[AllplanGeo.Line3D]

class LineVisitors():
    """ implementation of the line visitors for the property modification
    """

    @staticmethod
    def visit_StartPoint(line     : LINE_TYPES,
                         sep_count: int,
                         name     : str,
                         value    : Any):
        """ modify the start point

        Args:
            line:      line
            sep_count: separator count
            name:      name of the modified property
            value:     new value
        """

        if sep_count == 1:
            ParameterPropertyListUtil.set_sub_item_value(line, "StartPoint", value)

        else:
            CoordinateValueUtil.set_sub_item_coordinate_value(line, name, value)


    @staticmethod
    def visit_EndPoint(line     : LINE_TYPES,
                       sep_count: int,
                       name     : str,
                       value    : Any):
        """ modify the end point

        Args:
            line:      line
            sep_count: separator count
            name:      name of the modified property
            value:     new value
        """

        if sep_count == 1:
            ParameterPropertyListUtil.set_sub_item_value(line, "EndPoint", value)

        else:
            CoordinateValueUtil.set_sub_item_coordinate_value(line, name, value)


    @staticmethod
    def visit_Length(line      : LINE_TYPES,
                     _sep_count: int,
                     _name     : str,
                     value     : Any):
        """ modify the end point by the length

        Args:
            line:       line
            _sep_count: separator count
            _name:      name of the modified property
            value:      new value
        """

        def modify_length(line: (AllplanGeo.Line2D | AllplanGeo.Line3D),
                          length: float):
            if isinstance(line, AllplanGeo.Line2D):
                line.Extend(length - AllplanGeo.CalcLength(line))
            else:
                line.TrimEnd(AllplanGeo.CalcLength(line) - length)

        LineVisitors.__set_end_point(line, cast(float, value), modify_length)


    @staticmethod
    def visit_DeltaX(line      : LINE_TYPES,
                     _sep_count: int,
                     _name     : str,
                     value     : Any):
        """ modify the end point by the delta x

        Args:
            line:       line
            _sep_count: separator count
            _name:      name of the modified property
            value:      new value
        """

        def modify_x(line: (AllplanGeo.Line2D | AllplanGeo.Line3D),
                     length: float):
            if isinstance(line, AllplanGeo.Line2D):
                line.EndPoint = AllplanGeo.Point2D(line.StartPoint.X + length, line.EndPoint.Y)
            else:
                line.EndPoint = AllplanGeo.Point3D(line.StartPoint.X + length, line.EndPoint.Y, line.EndPoint.Z)

        LineVisitors.__set_end_point(line, cast(float, value), modify_x)


    @staticmethod
    def visit_DeltaY(line      : LINE_TYPES,
                     _sep_count: int,
                     _name     : str,
                     value     : Any):
        """ modify the end point by the delta y

        Args:
            line:       line
            _sep_count: separator count
            _name:      name of the modified property
            value:      new value
        """

        def modify_y(line: (AllplanGeo.Line2D | AllplanGeo.Line3D),
                     length: float):
            if isinstance(line, AllplanGeo.Line2D):
                line.EndPoint = AllplanGeo.Point2D(line.EndPoint.X, line.StartPoint.Y + length)
            else:
                line.EndPoint = AllplanGeo.Point3D(line.EndPoint.X, line.StartPoint.Y + length, line.EndPoint.Z)

        LineVisitors.__set_end_point(line, cast(float, value), modify_y)


    @staticmethod
    def visit_DeltaZ(line      : LINE_TYPES,
                     _sep_count: int,
                     _name     : str,
                     value     : Any):
        """ modify the end point by the delta z

        Args:
            line:       line
            _sep_count: separator count
            _name:      name of the modified property
            value:      new value
        """

        def modify_z(line: AllplanGeo.Line3D,
                     length: float):
            line.EndPoint = AllplanGeo.Point3D(line.EndPoint.X, line.EndPoint.Y, line.StartPoint.Z + length)

        LineVisitors.__set_end_point(line, cast(float, value), modify_z)    # type: ignore


    @staticmethod
    def visit_Angle(line      : LINE_TYPES,
                    _sep_count: int,
                    _name     : str,
                    value     : Any):
        """ modify the end point by the angle

        Args:
            line:       line
            _sep_count: separator count
            _name:      name of the modified property
            value:      new value
        """

        def modify_angle(line: AllplanGeo.Line2D,
                          angle: float):
            vec = AllplanGeo.Vector2D(line.StartPoint, line.EndPoint)

            vec = AllplanGeo.Rotate(vec, AllplanGeo.Angle.FromDeg(angle) - vec.GetAngle())

            line.EndPoint = AllplanGeo.Point2D(line.StartPoint + vec)

        LineVisitors.__set_end_point(line, cast(float, value), modify_angle)    # type: ignore


    @staticmethod
    def __set_end_point(line       : LINE_TYPES,
                        value      : float,
                        end_pnt_fct: Callable[[(AllplanGeo.Line2D | AllplanGeo.Line3D), float], None]):
        """ modify the end point

        Args:
            line:        line(s)
            value:       new value
            end_pnt_fct: end point function
        """

        if isinstance(line, list):
            for item in line:
                end_pnt_fct(item, value)
        else:
            end_pnt_fct(line, value)

```

</details>