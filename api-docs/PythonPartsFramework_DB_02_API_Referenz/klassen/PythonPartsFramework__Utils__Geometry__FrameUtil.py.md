---
title: "FrameUtil"
source: "PythonPartsFramework\Utils\Geometry\FrameUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# FrameUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\FrameUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the frame utility

- create a frame with fixed or variable offset

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`

## Klassen

### `FrameUtil`

implementation of the frame utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `fixed_frame` | `offset: float, height: float, polygon: AllplanGeo.Polygon2D` | `AllplanGeo.Polyhedron3D | None` | create a frame with a fixed offset  Args:     offset:  offset value     height:  height of the frame     polygon: base polygon  Returns:     created frame polyhedron |
| `variable_frame` | `offset_bottom: float, offset_right: float, offset_top: float, offset_left: float, height: float, polygon: AllplanGeo.Polygon2D` | `AllplanGeo.Polyhedron3D | None` | create a frame with a variable offset  Args:     offset_bottom: offset at the bottom     offset_right:  offset at the right     offset_top:    offset at the top     offset_left:   offset at the left     height:        height     polygon:       base polygon  Returns:     created frame polyhedron |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the frame utility

    - create a frame with fixed or variable offset
"""

# pylint: disable=magic-value-comparison

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

class FrameUtil():
    """ implementation of the frame utility
    """

    @staticmethod
    def fixed_frame(offset : float,
                    height : float,
                    polygon: AllplanGeo.Polygon2D) -> (AllplanGeo.Polyhedron3D | None):
        """ create a frame with a fixed offset

        Args:
            offset:  offset value
            height:  height of the frame
            polygon: base polygon

        Returns:
            created frame polyhedron
        """

        return FrameUtil.variable_frame(offset, offset, offset, offset, height, polygon)


    @staticmethod
    def variable_frame(offset_bottom: float,
                       offset_right : float,
                       offset_top   : float,
                       offset_left  : float,
                       height       : float,
                       polygon      : AllplanGeo.Polygon2D) -> (AllplanGeo.Polyhedron3D | None):
        """ create a frame with a variable offset

        Args:
            offset_bottom: offset at the bottom
            offset_right:  offset at the right
            offset_top:    offset at the top
            offset_left:   offset at the left
            height:        height
            polygon:       base polygon

        Returns:
            created frame polyhedron
        """

        if polygon.Count() < 3:
            print("Error: Polygon must have at least 3 points.")
            return None

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()


        #----------------- create the final polygon

        if polygon.StartPoint != polygon.EndPoint:
            polygon += polygon.StartPoint

        scale_mat = AllplanGeo.Matrix2D()

        scale_mat.Scaling(length_fac, length_fac)

        polygon = AllplanGeo.Transform(polygon, scale_mat)

        _, orientation = AllplanGeo.CalcArea(polygon)

        if orientation == AllplanGeo.eServiceResult.NEGATIVE_ORIENTATION:
            polygon.Reverse()


        #----------------- get the min and max values

        min_max, _ = AllplanGeo.CalcMinMax(polygon)

        x_left  = min_max.Min.X + AllplanGeo.GetAbsoluteTolerance()
        x_right = min_max.Max.X - AllplanGeo.GetAbsoluteTolerance()


        #----------------- get the offsets

        _, poly_segments = polygon.GetSegments()

        segments = [poly_segments[0]]

        for item in poly_segments[1:]:
            unite, unite_segment = AllplanGeo.Unite(segments[-1], item)

            if unite:
                segments[-1] = unite_segment
            else:
                segments.append(item)

        offsets = []

        for segment in segments:
            if segment.StartPoint.X <= x_left and segment.EndPoint.X <= x_left:
                offsets.append(offset_left * length_fac)

            elif segment.StartPoint.X >= x_right and segment.EndPoint.X >= x_right:
                offsets.append(offset_right * length_fac)

            elif segment.EndPoint.X > segment.StartPoint.X:
                offsets.append(offset_bottom * length_fac)

            else:
                offsets.append(offset_top * length_fac)


        #----------------- calculate the offset polygon

        offset_polygon = AllplanGeo.Polygon2D()

        end_index = len(segments) - 1

        for index, segment in enumerate(segments):
            _, offset_seg_1 = AllplanGeo.Offset(-offsets[index], segment)
            _, offset_seg_2 = AllplanGeo.Offset(-offsets[end_index], segments[end_index]) if index == 0 else \
                              AllplanGeo.Offset(-offsets[index - 1], segments[index - 1])

            _, s_pnt = AllplanGeo.IntersectionCalculusEx(offset_seg_1, offset_seg_2)

            offset_polygon += s_pnt

        offset_polygon += offset_polygon.StartPoint


        #----------------- create the polyhedron

        profiles = []

        for poly in (polygon, offset_polygon):
            poly_3d = AllplanGeo.ConvertTo3D(poly)[1]

            path = AllplanGeo.Polyline3D([poly_3d.StartPoint,
                                          poly_3d.StartPoint + AllplanGeo.Vector3D(0, 0, height * length_fac)])

            profiles.append(AllplanGeo.CreatePolyhedron(poly_3d, path)[1])

        result, polyhed = AllplanGeo.MakeSubtraction(profiles[1], profiles[0]) if offset_bottom > 0 else \
                          AllplanGeo.MakeSubtraction(profiles[0], profiles[1])

        if result != AllplanGeo.eGeometryErrorCode.eOK:
            print()
            print(f"Error during frame_d creation: {result}")
            print()

        return polyhed if result == AllplanGeo.eGeometryErrorCode.eOK else None

```

</details>