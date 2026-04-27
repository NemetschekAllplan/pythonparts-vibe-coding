---
title: "LabelingUtil"
source: "PythonPartsFramework\Utils\Reinforcement\LabelingUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# LabelingUtil

> **Pfad:** `PythonPartsFramework\Utils\Reinforcement\LabelingUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

implementation of the labeling utility functions

## Abhängigkeiten

- `BarsRepresentationUtil`
- `NemAll_Python_Geometry`

## Klassen

### `LabelingUtil`

implementation of the labeling utility functions
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_dim_line_placement_data` | `exclude_area_min_max: AllplanGeo.MinMax2D, bars_rep_util: BarsRepresentationUtil, placement_line: AllplanGeo.Line2D, bars_rep_line: AllplanGeo.Line2D, dist_from_exclude_area: float, swap_placement: bool` | `tuple[float, bool, float]` | get the placement data of the dimension line  Args:     exclude_area_min_max:   min/max box of the exclude area     bars_rep_util:          bars representation utility     placement_line:         placement line     bars_rep_line:          representation line     dist_from_exclude_area: distance from the exclude area     swap_placement:         swap the placement state  Returns:     dim line offset, at start or end, start offset |
| `__get_dim_line_offset_to_placement` | `bars_rep_util: BarsRepresentationUtil, placement_line: AllplanGeo.Line2D, dist_border: float, at_start: bool, dist_from_exclude_area: float, dim_line_extension: int` | `tuple[float, float]` | get the dimension line offset to the placement  Args:     bars_rep_util:          bars representation utility     placement_line:         placement line     dist_border:            border distance     at_start:               dimension line at start or end     dist_from_exclude_area: distance from the exclude area     dim_line_extension:     dimension line extension  Returns:     dimension line offset to the placement, start offset |
| `is_swap_text_angle` | `dim_line_angle: AllplanGeo.Angle` | `bool` | check if the text angle should be swapped  Args:     dim_line_angle: dimension line angle  Returns:     swap state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the labeling utility functions
"""

import NemAll_Python_Geometry as AllplanGeo

from .BarsRepresentationUtil import BarsRepresentationUtil

class LabelingUtil():
    """ implementation of the labeling utility functions
    """


    @staticmethod
    def get_dim_line_placement_data(exclude_area_min_max  : AllplanGeo.MinMax2D,
                                    bars_rep_util         : BarsRepresentationUtil,
                                    placement_line        : AllplanGeo.Line2D,
                                    bars_rep_line         : AllplanGeo.Line2D,
                                    dist_from_exclude_area: float,
                                    swap_placement        : bool) -> tuple[float, bool, float]:
        """ get the placement data of the dimension line

        Args:
            exclude_area_min_max:   min/max box of the exclude area
            bars_rep_util:          bars representation utility
            placement_line:         placement line
            bars_rep_line:          representation line
            dist_from_exclude_area: distance from the exclude area
            swap_placement:         swap the placement state

        Returns:
            dim line offset, at start or end, start offset
        """

        rot_angle  = AllplanGeo.Angle(-AllplanGeo.CalcAngle(placement_line)[0].Rad)

        start_point = AllplanGeo.Rotate(bars_rep_line.StartPoint, rot_angle)
        end_point   = AllplanGeo.Rotate(bars_rep_line.EndPoint, rot_angle)

        bottom_line = AllplanGeo.Line2D(exclude_area_min_max.Min.X, exclude_area_min_max.Min.Y,
                                        exclude_area_min_max.Max.X, exclude_area_min_max.Min.Y)

        top_line = AllplanGeo.Line2D(exclude_area_min_max.Min.X, exclude_area_min_max.Max.Y,
                                     exclude_area_min_max.Max.X, exclude_area_min_max.Max.Y)

        bottom_dist_start = abs(AllplanGeo.TransformCoord.PointLocal(bottom_line, start_point).Y)
        bottom_dist_end   = abs(AllplanGeo.TransformCoord.PointLocal(bottom_line, end_point).Y)
        top_dist_start    = abs(AllplanGeo.TransformCoord.PointLocal(top_line, start_point).Y)
        top_dist_end      = abs(AllplanGeo.TransformCoord.PointLocal(top_line, end_point).Y)

        bottom_dist = min(bottom_dist_start, bottom_dist_end)
        top_dist    = min(top_dist_start, top_dist_end)

        dist_border = bottom_dist if bottom_dist < top_dist else top_dist

        dim_line_extension = -1 if bottom_dist < top_dist else 1

        at_start = bottom_dist == bottom_dist_start if bottom_dist < top_dist else top_dist == top_dist_start

        if swap_placement:
            at_start           = not at_start
            dim_line_extension = -dim_line_extension
            dist_border        = top_dist if dist_border == bottom_dist else bottom_dist

        dim_line_offset, start_offset = LabelingUtil.__get_dim_line_offset_to_placement(bars_rep_util, placement_line,
                                                                                        dist_border, at_start,
                                                                                        dist_from_exclude_area, dim_line_extension)

        return dim_line_offset, at_start, start_offset


    @staticmethod
    def __get_dim_line_offset_to_placement(bars_rep_util         : BarsRepresentationUtil,
                                           placement_line        : AllplanGeo.Line2D,
                                           dist_border           : float,
                                           at_start              : bool,
                                           dist_from_exclude_area: float,
                                           dim_line_extension    : int) -> tuple[float, float]:
        """ get the dimension line offset to the placement

        Args:
            bars_rep_util:          bars representation utility
            placement_line:         placement line
            dist_border:            border distance
            at_start:               dimension line at start or end
            dist_from_exclude_area: distance from the exclude area
            dim_line_extension:     dimension line extension

        Returns:
            dimension line offset to the placement, start offset
        """

        local_min_max = bars_rep_util.get_local_min_max_of_placement(placement_line)

        dist = dist_border + dist_from_exclude_area

        start_offset = dist

        if at_start and dim_line_extension == 1 or not at_start and dim_line_extension == -1:
            dist = -dist + local_min_max.Min.Y

        if not at_start and dim_line_extension == -1:
            start_offset = -start_offset + local_min_max.Min.Y

        elif not at_start and dim_line_extension == 1:
            start_offset = start_offset + local_min_max.Max.Y

        elif at_start and dim_line_extension == -1:
            start_offset = -start_offset

        return dist, start_offset


    @staticmethod
    def is_swap_text_angle(dim_line_angle: AllplanGeo.Angle) -> bool:
        """ check if the text angle should be swapped

        Args:
            dim_line_angle: dimension line angle

        Returns:
            swap state
        """

        swap_text_angle_start = 93
        swap_text_angle_end   = 273

        return swap_text_angle_start <= dim_line_angle.Deg <= swap_text_angle_end

```

</details>