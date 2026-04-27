---
title: "PreviewSymbols"
source: "PythonPartsFramework\GeneralScripts\PreviewSymbols.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PreviewSymbols

> **Pfad:** `PythonPartsFramework\GeneralScripts\PreviewSymbols.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the preview symbols

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `Utilities.SystemAngleUtil`
- `Utils.Text3DUtil`
- `Utils.TextReferencePointPosition`
- `enum`
- `typing`

## Klassen

### `PreviewSymbols`

implementation of the preview symbols 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize  |
| `add_circle` | `self, reference_point: AllplanGeo.Point3D, radius_pixel: int, color: Union[AllplanBasisEle.ARGB, int]` | `None` | add a circle symbol  Args:     reference_point: reference point     radius_pixel:    radius in pixel     color:           color as ARGB value or color ID |
| `add_polyline` | `self, reference_point: AllplanGeo.Point3D, polyline: AllplanGeo.Polyline2D, color: Union[AllplanBasisEle.ARGB, int], line_pattern: int=4095` | `None` | add a polyline symbol  Args:     reference_point: reference point     polyline:        polyline     color:           color as ARGB value or color ID     line_pattern:    line pattern as 0/1 patten |
| `add_cross` | `self, reference_point: AllplanGeo.Point3D, width: float, color: Union[AllplanBasisEle.ARGB, int]` | `None` | add a cross symbol  Args:     reference_point: reference point     width:           width     color:           color as ARGB value or color ID |
| `add_mark` | `self, reference_point: AllplanGeo.Point3D, width: float, color: Union[AllplanBasisEle.ARGB, int]` | `None` | add mark symbol  Args:     reference_point: reference point     width:           width     color:           color as ARGB value or color ID |
| `add_coord_cross` | `self, plane: Union[AllplanGeo.Plane3D, AllplanGeo.AxisPlacement3D], arm_length: float` | `None` | add a coordinate cross symbol  Args:     plane:          plane of the coordinate cross     arm_length:     length of the arms |
| `add_text` | `self, text: str, reference_point: AllplanGeo.Point3D, ref_pnt_pos: TextReferencePointPosition, height: float, color: Union[AllplanBasisEle.ARGB, int], rotation_angle: AllplanGeo.Angle` | `None` | add a text symbol  Args:     text:            text     reference_point: reference point     ref_pnt_pos:     point position of the reference point     height:          height     color:           color as ARGB value or color ID     rotation_angle:  rotation angle |
| `add_arrow` | `self, reference_point: AllplanGeo.Point3D, width: float, color: Union[AllplanBasisEle.ARGB, int], rotation_angle: AllplanGeo.Angle` | `None` | add an arrow symbol  Args:     reference_point: reference point     width:           width     color:           color as ARGB value or color ID     rotation_angle:  rotation angle |
| `add_filled_rectangle` | `self, reference_point: AllplanGeo.Point3D, width: float, color: Union[AllplanBasisEle.ARGB, int], rotation_angle: AllplanGeo.Angle` | `None` | add a filled rectangle symbol  Args:     reference_point: reference point     width:           width     color:           color as ARGB value or color ID     rotation_angle:  rotation angle |
| `draw` | `self, insert_matrix: AllplanGeo.Matrix3D, view_projection: AllplanIFW.ViewWorldProjection, use_system_angle: bool=True` | `None` | draw the symbols  Args:     insert_matrix:    insert matrix     view_projection:  view world projection     use_system_angle: use the system angle state |
| `__get_color` | `color: Union[AllplanBasisEle.ARGB, int]` | `AllplanBasisEle.ARGB` | get the color as ARGB value  Args:     color: color as ARGB or color ID  Returns:     _color as ARGB value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
implementation of the preview symbols
"""

from typing import Union

from enum import IntEnum

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_BaseElements as AllplanBaseEle

from Utilities.SystemAngleUtil import SystemAngleUtil

from Utils.Text3DUtil import Text3DUtil
from Utils.TextReferencePointPosition import TextReferencePointPosition


class PreviewSymbols():
    """ implementation of the preview symbols """

    class PreviewSymbolType(IntEnum):
        """ definition of the preview symbol types"""

        CIRCLE           = 1
        POLYLINE         = 2
        CROSS            = 3
        MARK             = 4
        COORD_CROSS      = 5
        TEXT             = 6
        ARROW            = 7
        FILLED_RECTANGLE = 8


    def __init__(self):
        """ initialize """

        self.symbols = []

    def add_circle(self,
                   reference_point: AllplanGeo.Point3D,
                   radius_pixel   : int,
                   color          : Union[AllplanBasisEle.ARGB, int]):
        """ add a circle symbol

        Args:
            reference_point: reference point
            radius_pixel:    radius in pixel
            color:           color as ARGB value or color ID
        """

        self.symbols.append((PreviewSymbols.PreviewSymbolType.CIRCLE, reference_point, radius_pixel,
                             PreviewSymbols.__get_color(color)))

    def add_polyline(self,
                     reference_point: AllplanGeo.Point3D,
                     polyline       : AllplanGeo.Polyline2D,
                     color          : Union[AllplanBasisEle.ARGB, int],
                     line_pattern   : int = 0xfff):
        """ add a polyline symbol

        Args:
            reference_point: reference point
            polyline:        polyline
            color:           color as ARGB value or color ID
            line_pattern:    line pattern as 0/1 patten
        """

        self.symbols.append((PreviewSymbols.PreviewSymbolType.POLYLINE, reference_point, polyline,
                             PreviewSymbols.__get_color(color), line_pattern))

    def add_cross(self,
                  reference_point: AllplanGeo.Point3D,
                  width          : float,
                  color          : Union[AllplanBasisEle.ARGB, int]):
        """ add a cross symbol

        Args:
            reference_point: reference point
            width:           width
            color:           color as ARGB value or color ID
        """

        self.symbols.append((PreviewSymbols.PreviewSymbolType.CROSS, reference_point, width,
                             PreviewSymbols.__get_color(color)))

    def add_mark(self,
                 reference_point: AllplanGeo.Point3D,
                 width          : float,
                 color          : Union[AllplanBasisEle.ARGB, int]):
        """ add mark symbol

        Args:
            reference_point: reference point
            width:           width
            color:           color as ARGB value or color ID
        """

        self.symbols.append((PreviewSymbols.PreviewSymbolType.MARK, reference_point, width,
                             PreviewSymbols.__get_color(color)))

    def add_coord_cross(self,
                        plane          : Union[AllplanGeo.Plane3D, AllplanGeo.AxisPlacement3D],
                        arm_length     : float):
        """ add a coordinate cross symbol

        Args:
            plane:          plane of the coordinate cross
            arm_length:     length of the arms
        """

        self.symbols.append((PreviewSymbols.PreviewSymbolType.COORD_CROSS, plane, arm_length))

    def add_text(self,
                 text           : str,
                 reference_point: AllplanGeo.Point3D,
                 ref_pnt_pos    : TextReferencePointPosition,
                 height         : float,
                 color          : Union[AllplanBasisEle.ARGB, int],
                 rotation_angle : AllplanGeo.Angle):
        """ add a text symbol

        Args:
            text:            text
            reference_point: reference point
            ref_pnt_pos:     point position of the reference point
            height:          height
            color:           color as ARGB value or color ID
            rotation_angle:  rotation angle
        """

        text_3d = Text3DUtil()

        if text_3d is None:
            return

        bsplines = text_3d.get_bsplines(AllplanGeo.Point3D(), text,
                                        TextReferencePointPosition.BOTTOM_LEFT, height, rotation_angle)

        axis = AllplanGeo.Axis2D(AllplanGeo.Point2D(), AllplanGeo.Vector2D(100, 0))

        bsplines = [AllplanGeo.Mirror(bspline, axis) for bspline in bsplines]

        min_max = sum([AllplanGeo.CalcMinMax(bspline)[0] for bspline in bsplines], AllplanGeo.MinMax3D())

        text_width  = min_max.GetSizeX()
        text_height = min_max.GetSizeY()

        ref_vec = AllplanGeo.Vector2D(-min_max.Min.X, -min_max.Min.Y)

        if ref_pnt_pos in [TextReferencePointPosition.BOTTOM_CENTER, TextReferencePointPosition.CENTER_CENTER,
                           TextReferencePointPosition.TOP_CENTER]:
            ref_vec.X = ref_vec.X - text_width / 2

        elif ref_pnt_pos in [TextReferencePointPosition.BOTTOM_RIGHT, TextReferencePointPosition.CENTER_RIGHT,
                             TextReferencePointPosition.TOP_RIGHT]:
            ref_vec.X -= text_width

        if ref_pnt_pos in [TextReferencePointPosition.CENTER_CENTER, TextReferencePointPosition.CENTER_CENTER,
                           TextReferencePointPosition.CENTER_RIGHT]:
            ref_vec.Y -= text_height / 2

        elif ref_pnt_pos in [TextReferencePointPosition.TOP_LEFT, TextReferencePointPosition.TOP_CENTER,
                             TextReferencePointPosition.TOP_RIGHT]:
            ref_vec.Y -= text_height

        for bspline in bsplines:
            result, polyline3d = AllplanGeo.Polygonize(bspline, 4, 0, 0, 0)

            if result:
                result, polyline = AllplanGeo.ConvertTo2D(polyline3d)

                if result:
                    polyline = AllplanGeo.Move(polyline, ref_vec)

                    self.symbols.append((PreviewSymbols.PreviewSymbolType.POLYLINE, reference_point, polyline,
                                         PreviewSymbols.__get_color(color), 0xffff))

    def add_arrow(self,
                  reference_point: AllplanGeo.Point3D,
                  width          : float,
                  color          : Union[AllplanBasisEle.ARGB, int],
                  rotation_angle : AllplanGeo.Angle):
        """ add an arrow symbol

        Args:
            reference_point: reference point
            width:           width
            color:           color as ARGB value or color ID
            rotation_angle:  rotation angle
        """

        self.symbols.append((PreviewSymbols.PreviewSymbolType.ARROW, reference_point, width,
                             PreviewSymbols.__get_color(color), rotation_angle))

    def add_filled_rectangle(self,
                             reference_point: AllplanGeo.Point3D,
                             width          : float,
                             color          : Union[AllplanBasisEle.ARGB, int],
                             rotation_angle : AllplanGeo.Angle):
        """ add a filled rectangle symbol

        Args:
            reference_point: reference point
            width:           width
            color:           color as ARGB value or color ID
            rotation_angle:  rotation angle
        """

        self.symbols.append((PreviewSymbols.PreviewSymbolType.FILLED_RECTANGLE, reference_point, width,
                             PreviewSymbols.__get_color(color), rotation_angle))

    def draw(self,
             insert_matrix   : AllplanGeo.Matrix3D,
             view_projection : AllplanIFW.ViewWorldProjection,
             use_system_angle: bool = True):
        """ draw the symbols

        Args:
            insert_matrix:    insert matrix
            view_projection:  view world projection
            use_system_angle: use the system angle state
        """

        #----------------- final transformation in case of rotated crosshair

        if use_system_angle:
            insert_matrix = SystemAngleUtil.execute_rotation(insert_matrix)


        #----------------- draw the symbols

        for symbol in self.symbols:
            if symbol[0] == PreviewSymbols.PreviewSymbolType.CIRCLE:
                AllplanIFW.PreviewSymbolBuilder.CircleSymbol(AllplanGeo.Transform(symbol[1], insert_matrix),
                                                             True, view_projection, symbol[3], symbol[2])

            elif symbol[0] == PreviewSymbols.PreviewSymbolType.POLYLINE:
                AllplanIFW.PreviewSymbolBuilder.Polyline2DSymbol(AllplanGeo.Transform(symbol[1], insert_matrix),
                                                                 symbol[2], view_projection, symbol[3], 0xffff)

            elif symbol[0] == PreviewSymbols.PreviewSymbolType.CROSS:
                AllplanIFW.PreviewSymbolBuilder.CrossSymbol(AllplanGeo.Transform(symbol[1], insert_matrix),
                                                            True, view_projection, symbol[3], symbol[2])

            elif symbol[0] == PreviewSymbols.PreviewSymbolType.MARK:
                AllplanIFW.PreviewSymbolBuilder.MarkSymbol(AllplanGeo.Transform(symbol[1], insert_matrix),
                                                           True, view_projection, symbol[3], symbol[2])

            elif symbol[0] == PreviewSymbols.PreviewSymbolType.COORD_CROSS:
                if isinstance(symbol[1], AllplanGeo.AxisPlacement3D):
                    axis_placement : AllplanGeo.AxisPlacement3D = symbol[1]

                    axis_placement = AllplanGeo.AxisPlacement3D(AllplanGeo.Transform(axis_placement.GetOrigin(), insert_matrix),
                                                                AllplanGeo.Transform(axis_placement.GetXDirection(), insert_matrix),
                                                                AllplanGeo.Transform(axis_placement.GetZDirection(), insert_matrix))

                    AllplanIFW.PreviewSymbolBuilder.CoordCrossSymbol(axis_placement, symbol[2], view_projection)
                else:
                    plane : AllplanGeo.Plane3D = symbol[1]

                    AllplanIFW.PreviewSymbolBuilder.CoordCrossSymbol(AllplanGeo.Transform(plane, insert_matrix),
                                                                    symbol[2], view_projection)

            elif symbol[0] == PreviewSymbols.PreviewSymbolType.ARROW:
                AllplanIFW.PreviewSymbolBuilder.ArrowSymbol(AllplanGeo.Transform(symbol[1], insert_matrix),
                                                            True, view_projection, symbol[3], symbol[2], symbol[4].Rad)

            elif symbol[0] == PreviewSymbols.PreviewSymbolType.FILLED_RECTANGLE:
                AllplanIFW.PreviewSymbolBuilder.FilledRectangleSymbol(AllplanGeo.Transform(symbol[1], insert_matrix),
                                                                      True, view_projection, symbol[3], symbol[2], symbol[4].Rad)

    @staticmethod
    def __get_color(color: Union[AllplanBasisEle.ARGB, int]) -> AllplanBasisEle.ARGB:
        """ get the color as ARGB value

        Args:
            color: color as ARGB or color ID

        Returns:
            _color as ARGB value
        """

        if isinstance(color, int):
            return AllplanBasisEle.ARGB(AllplanBaseEle.GetColorById(color))

        return color

```

</details>