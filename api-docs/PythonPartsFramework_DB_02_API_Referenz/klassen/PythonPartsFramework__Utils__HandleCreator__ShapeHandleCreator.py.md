---
title: "ShapeHandleCreator"
source: "PythonPartsFramework\Utils\HandleCreator\ShapeHandleCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ShapeHandleCreator

> **Pfad:** `PythonPartsFramework\Utils\HandleCreator\ShapeHandleCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `utility`

## Übersicht

implementation of the shape handle creator

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `TypeCollections.HandleList`
- `Utils.Geometry.Rectangle2DUtil`
- `Utils.HandleCreator.HandleCreator`

## Klassen

### `ShapeHandleCreator`

implementation of the shape handle creator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `rect_by_center` | `handle_list: HandleList, center_point: AllplanGeo.Point3D, rotation_angle: AllplanGeo.Angle, width: float, depth: float, width_name: str='', depth_name: str='', owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter()` | `None` | create rectangle handles  Args:     handle_list:    handle list     center_point:   center point     rotation_angle: rotation angle     width:          width     depth:          depth     width_name:     width parameter name     depth_name:     depth parameter name     owner_element:  owner element of the handle (in element modification mode) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the shape handle creator
"""

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Geometry as AllplanGeo

from TypeCollections.HandleList import HandleList

from Utils.HandleCreator.HandleCreator import HandleCreator
from Utils.Geometry.Rectangle2DUtil import Rectangle2DUtil

class ShapeHandleCreator():
    """ implementation of the shape handle creator
    """

    @staticmethod
    def rect_by_center(handle_list   : HandleList,
                       center_point  : AllplanGeo.Point3D,
                       rotation_angle: AllplanGeo.Angle,
                       width         : float,
                       depth         : float,
                       width_name    : str                                  = "",
                       depth_name    : str                                  = "",
                       owner_element : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()):
        """ create rectangle handles

        Args:
            handle_list:    handle list
            center_point:   center point
            rotation_angle: rotation angle
            width:          width
            depth:          depth
            width_name:     width parameter name
            depth_name:     depth parameter name
            owner_element:  owner element of the handle (in element modification mode)
        """

        _, rect_poly = AllplanGeo.ConvertTo3D(Rectangle2DUtil.polygon_by_center(center_point.To2D, rotation_angle, width, depth))

        HandleCreator.vector_distances(handle_list, [width_name, depth_name], rect_poly[2], rect_poly[0],
                                       [AllplanGeo.Vector3D(rect_poly[0], rect_poly[1]),
                                        AllplanGeo.Vector3D(rect_poly[0], rect_poly[3])],
                                       [True, True], [False, True],
                                       show_handles  = False,
                                       owner_element = owner_element)

        HandleCreator.point(handle_list, "BottomLeft", rect_poly[0],
                            owner_element = owner_element,
                            handle_type   = AllplanIFW.ElementHandleType.HANDLE_SQUARE_BLUE,
                            handle_angle  = rotation_angle)
        HandleCreator.point(handle_list, "BottomRight", rect_poly[1],
                            owner_element = owner_element,
                            handle_type   = AllplanIFW.ElementHandleType.HANDLE_SQUARE_BLUE,
                            handle_angle  = rotation_angle)
        HandleCreator.point(handle_list, "TopRight", rect_poly[2],
                            owner_element = owner_element,
                            handle_type   = AllplanIFW.ElementHandleType.HANDLE_SQUARE_BLUE,
                            handle_angle  = rotation_angle)
        HandleCreator.point(handle_list, "TopLeft", rect_poly[3],
                            owner_element = owner_element,
                            handle_type   = AllplanIFW.ElementHandleType.HANDLE_SQUARE_BLUE,
                            handle_angle  = rotation_angle)

```

</details>