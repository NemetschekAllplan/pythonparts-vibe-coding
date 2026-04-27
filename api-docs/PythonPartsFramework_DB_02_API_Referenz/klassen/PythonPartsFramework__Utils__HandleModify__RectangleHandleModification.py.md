---
title: "RectangleHandleModification"
source: "PythonPartsFramework\Utils\HandleModify\RectangleHandleModification.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - utility
related:
  -
last_updated: "2026-02-20"
---


# RectangleHandleModification

> **Pfad:** `PythonPartsFramework\Utils\HandleModify\RectangleHandleModification.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `utility`

## Übersicht

implementation of the rectangle handle modification

## Abhängigkeiten

- `HandleProperties`
- `NemAll_Python_Geometry`
- `Utils.Geometry.Rectangle2DUtil`

## Klassen

### `RectangleHandleModification`

implementation of the rectangle handle modification
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_center_and_sizes` | `handle_prop: HandleProperties, input_pnt: AllplanGeo.Point2D, center_point: AllplanGeo.Point2D, rotation_angle: AllplanGeo.Angle, width: float, depth: float` | `tuple[AllplanGeo.Point2D, float, float]` | create rectangle handles  Args:     handle_prop:    handle properties     input_pnt:      input point     center_point:   center point     rotation_angle: rotation angle     width:          width     depth:          depth  Returns:     center point, width and depth |
| `is_rect_handle` | `handle_prop: HandleProperties` | `bool` | check if the handle is a rectangle handle  Args:     handle_prop: handle properties  Returns:     get the rectangle handle state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the rectangle handle modification
"""

import NemAll_Python_Geometry as AllplanGeo

from HandleProperties import HandleProperties

from Utils.Geometry.Rectangle2DUtil import Rectangle2DUtil

class RectangleHandleModification():
    """ implementation of the rectangle handle modification
    """

    @staticmethod
    def get_center_and_sizes(handle_prop   : HandleProperties,
                             input_pnt     : AllplanGeo.Point2D,
                             center_point  : AllplanGeo.Point2D,
                             rotation_angle: AllplanGeo.Angle,
                             width         : float,
                             depth         : float) -> tuple[AllplanGeo.Point2D, float, float]:
        """ create rectangle handles

        Args:
            handle_prop:    handle properties
            input_pnt:      input point
            center_point:   center point
            rotation_angle: rotation angle
            width:          width
            depth:          depth

        Returns:
            center point, width and depth
        """

        rect_poly = Rectangle2DUtil.polygon_by_center(center_point, rotation_angle, width, depth)

        dir_vec = AllplanGeo.Vector2D(rotation_angle, 1000)

        match handle_prop.handle_id:
            case "BottomLeft":
                center_pnt = (rect_poly[2] + input_pnt) / 2

                base_line = AllplanGeo.Line2D(rect_poly[2], rect_poly[2] + dir_vec)

            case "BottomRight":
                center_pnt = (rect_poly[3] + input_pnt) / 2

                base_line = AllplanGeo.Line2D(rect_poly[3], rect_poly[3] + dir_vec)

            case "TopRight":
                center_pnt = (rect_poly[0] + input_pnt) / 2

                base_line = AllplanGeo.Line2D(rect_poly[0], rect_poly[0] + dir_vec)

            case "TopLeft":
                center_pnt = (rect_poly[1] + input_pnt) / 2

                base_line = AllplanGeo.Line2D(rect_poly[1], rect_poly[1] + dir_vec)


        #----------------- calculate the sizes

        loc_pnt = AllplanGeo.TransformCoord.PointLocal(base_line, input_pnt)

        width = abs(loc_pnt.X)
        depth = abs(loc_pnt.Y)

        return center_pnt, width, depth


    @staticmethod
    def is_rect_handle(handle_prop: HandleProperties) -> bool:
        """ check if the handle is a rectangle handle

        Args:
            handle_prop: handle properties

        Returns:
            get the rectangle handle state
        """

        return handle_prop.handle_id in {"BottomLeft", "BottomRight", "TopRight", "TopLeft"}

```

</details>