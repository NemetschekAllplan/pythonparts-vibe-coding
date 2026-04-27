---
title: "Polygon2DOffsetUtil"
source: "PythonPartsFramework\Utils\Geometry\Polygon2DOffsetUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Polygon2DOffsetUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\Polygon2DOffsetUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the polygon offset algorithm for 2D polygons

- add offset to individual segments of a polygon
- calculate the resulting offset polygon

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `Polygon2DOffsetUtil`

implementation of the polygon offset algorithm for 2D polygons
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, polygon: AllplanGeo.Polygon2D` | `None` | initialize the polygon offset util  Args:     polygon: polygon to offset |
| `set_offset` | `self, segment_index: int, offset: float` | `None` | set the offset value  Args:     segment_index: segment index to offset     offset:        offset value |
| `execute` | `self` | `AllplanGeo.Polygon2D` | execute the offset algorithm  Returns:     offset polygon |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the polygon offset algorithm for 2D polygons

    - add offset to individual segments of a polygon
    - calculate the resulting offset polygon
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class Polygon2DOffsetUtil():
    """ implementation of the polygon offset algorithm for 2D polygons
    """

    def __init__(self,
                 polygon: AllplanGeo.Polygon2D):
        """ initialize the polygon offset util

        Args:
            polygon: polygon to offset
        """

        self.length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        scale_mat = AllplanGeo.Matrix2D()
        scale_mat.Scaling(self.length_fac, self.length_fac)

        self.__polygon = AllplanGeo.Transform(polygon, scale_mat)

        self.__offsets = dict[int, float]()


    def set_offset(self,
                   segment_index: int,
                   offset       : float):
        """ set the offset value

        Args:
            segment_index: segment index to offset
            offset:        offset value
        """

        self.__offsets[segment_index - 1] = offset * self.length_fac


    def execute(self) -> AllplanGeo.Polygon2D:
        """ execute the offset algorithm

        Returns:
            offset polygon
        """

        offset_segments = []

        for index, segment in enumerate(self.__polygon.GetSegments()[1]):
            result, offset_seg = AllplanGeo.Offset(-self.__offsets.get(index, 0), segment)

            if result == AllplanGeo.eGeometryErrorCode.eOK:
                if offset_segments:
                    unite, unite_segment = AllplanGeo.Unite(offset_segments[-1], offset_seg)

                    if unite:
                        offset_segments[-1] = unite_segment
                    else:
                        offset_segments.append(offset_seg)
                else:
                    offset_segments.append(offset_seg)


        #------------- calculate the offset polygon

        end_index = len(offset_segments) - 1

        res_polygon = AllplanGeo.Polygon2D()

        for index, segment in enumerate(offset_segments):
            left_segment = offset_segments[end_index] if index == 0 else offset_segments[index - 1]

            result, s_pnt = AllplanGeo.IntersectionCalculusEx(left_segment, segment)

            if result:
                res_polygon += AllplanGeo.Point2D(s_pnt.X, s_pnt.Y)
            else:
                res_polygon += AllplanGeo.Point2D(left_segment.EndPoint.X, left_segment.EndPoint.Y)
                res_polygon += AllplanGeo.Point2D(segment.StartPoint.X, segment.StartPoint.Y)


        res_polygon += res_polygon[0]

        return res_polygon

```

</details>