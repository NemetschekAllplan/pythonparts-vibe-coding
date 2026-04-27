---
title: "BarsDimLinePlacement"
source: "PythonPartsFramework\Utils\Reinforcement\BarsDimLinePlacement.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BarsDimLinePlacement

> **Pfad:** `PythonPartsFramework\Utils\Reinforcement\BarsDimLinePlacement.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

implementation of the BarsDimLinePlacement class

## Abhängigkeiten

- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Reinforcement`
- `Utils.Reinforcement.BarsRepresentationLineUtil`
- `Utils.Reinforcement.BarsRepresentationUtil`
- `Utils.Reinforcement.LabelingUtil`
- `math`

## Klassen

### `BarsDimLinePlacement`

implementation of the BarsDimLinePlacement class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, bars_rep_elements: list[AllplanReinf.BarsRepresentation]` | `None` | initialize  Args:     bars_rep_elements: representation elements |
| `reset` | `self` | `None` | reset the data          |
| `swap_dim_line_position` | `self, bars_rep_ele_guid: AllplanEleAdapter.GUID` | `None` | swap the dimension line position  Args:     bars_rep_ele_guid: guid of the representation element |
| `set_dim_line_position` | `self, bars_rep_ele_guid: AllplanEleAdapter.GUID, dim_line_offset: float, dim_line: AllplanGeo.Line2D` | `None` | set the dimension line position  Args:     bars_rep_ele_guid: guid of the representation element     dim_line_offset:   dimension line offset     dim_line:          dimension line |
| `get_dim_line_position` | `self, bars_representation: AllplanReinf.BarsRepresentation, bars_rep_util: BarsRepresentationUtil, offset_from_placement: float, dim_line_distance: float, dim_line_angle_from: float, dim_line_angle_to: float, text_dist: float` | `tuple[bool, bool, float, AllplanBasisEle.TextAlignment, AllplanGeo.Line2D]` | get the dimension line position  Args:     bars_representation:   representation element     bars_rep_util:         bars representation utility     offset_from_placement: offset from the placement     dim_line_distance:     dimension line distance     dim_line_angle_from:   dimension line angle from     dim_line_angle_to:     dimension line angle to     text_dist:             text distance from the dimension line  Returns:     location at start, distance from the placement, text alignment, handle point |
| `select_dim_line_bars_rep` | `self, input_pnt: AllplanGeo.Point3D, min_dist: float, text_dist: float` | `AllplanEleAdapter.GUID | None` | select the dimension line bars representation  Args:     input_pnt: input point     min_dist:  minimum distance     text_dist: text distance from the dimension line  Returns:     selected bars representation element |
| `get_label_offset` | `self, bars_rep: AllplanReinf.BarsRepresentation, dim_line: AllplanGeo.Line2D, bars_ref_line_util: BarsRepresentationLineUtil, text_dist: float` | `AllplanGeo.Vector2D` | get the label offset in case of intersection with the center bar  Args:     bars_rep:           bars representation     dim_line:           dimension line     bars_ref_line_util: bars representation line utility     text_dist:          text distance from the dimension line  Returns:     offset |
| `__search_empty_label_position` | `self, dim_line_distance: float, placement_line_dist: float, dim_line_offset: float, placement_line: AllplanGeo.Line2D, bars_rep_ele: AllplanEleAdapter.BaseElementAdapter` | `tuple[float, AllplanGeo.Line2D]` | search an empty label position  Args:     dim_line_distance:   dimension line distance     placement_line_dist: placement line distance     dim_line_offset:     dimension line offset     placement_line:      placement line     bars_rep_ele:        representation element  Returns:     dimension line offset, dimension line |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the BarsDimLinePlacement class
"""

import math

import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

from Utils.Reinforcement.BarsRepresentationLineUtil import BarsRepresentationLineUtil
from Utils.Reinforcement.BarsRepresentationUtil import BarsRepresentationUtil
from Utils.Reinforcement.LabelingUtil import LabelingUtil

class BarsDimLinePlacement():
    """ implementation of the BarsDimLinePlacement class
    """

    def __init__(self,
                 bars_rep_elements: list[AllplanReinf.BarsRepresentation]):
        """ initialize

        Args:
            bars_rep_elements: representation elements
        """

        self.bars_rep_elements = [item.GetBaseElementAdapter() for item in bars_rep_elements]

        self.labeling_lines: list[tuple[AllplanGeo.Line2D, float, AllplanEleAdapter.GUID]] = []

        self.bars_rep_min_max  = dict[float, AllplanGeo.MinMax2D]()
        self.swap_position     = set[AllplanEleAdapter.GUID]()
        self.dim_line_position = dict[AllplanEleAdapter.GUID, tuple[float, AllplanGeo.Line2D]]()
        self.label_size        = (AllplanEleAdapter.GUID(), 0.0)


    def reset(self):
        """ reset the data
        """

        self.labeling_lines.clear()

        self.bars_rep_min_max.clear()


    def swap_dim_line_position(self,
                               bars_rep_ele_guid: AllplanEleAdapter.GUID):
        """ swap the dimension line position

        Args:
            bars_rep_ele_guid: guid of the representation element
        """

        if bars_rep_ele_guid in self.swap_position:
            self.swap_position.remove(bars_rep_ele_guid)

            return

        self.swap_position.add(bars_rep_ele_guid)

        if bars_rep_ele_guid in self.dim_line_position:
            self.dim_line_position.pop(bars_rep_ele_guid)


    def set_dim_line_position(self,
                              bars_rep_ele_guid: AllplanEleAdapter.GUID,
                              dim_line_offset  : float,
                              dim_line         : AllplanGeo.Line2D):
        """ set the dimension line position

        Args:
            bars_rep_ele_guid: guid of the representation element
            dim_line_offset:   dimension line offset
            dim_line:          dimension line
        """

        self.dim_line_position[bars_rep_ele_guid] = (dim_line_offset, dim_line)


    def get_dim_line_position(self,
                              bars_representation  : AllplanReinf.BarsRepresentation,
                              bars_rep_util        : BarsRepresentationUtil,
                              offset_from_placement: float,
                              dim_line_distance    : float,
                              dim_line_angle_from  : float,
                              dim_line_angle_to    : float,
                              text_dist            : float) -> tuple[bool, bool, float, AllplanBasisEle.TextAlignment, AllplanGeo.Line2D]:
        """ get the dimension line position

        Args:
            bars_representation:   representation element
            bars_rep_util:         bars representation utility
            offset_from_placement: offset from the placement
            dim_line_distance:     dimension line distance
            dim_line_angle_from:   dimension line angle from
            dim_line_angle_to:     dimension line angle to
            text_dist:             text distance from the dimension line

        Returns:
            location at start, distance from the placement, text alignment, handle point
        """

        bars_placement_line = bars_representation.GetPlacementLine()
        bars_rep_line       = bars_representation.GetirstRepresentationLine()

        dim_line_angle = AllplanGeo.CalcAngle(bars_placement_line)[0]

        text_align = AllplanBasisEle.TextAlignment.eMiddleTop if LabelingUtil.is_swap_text_angle(dim_line_angle) else \
                     AllplanBasisEle.TextAlignment.eMiddleBottom


        #----------------- check if the dimension line should be created

        create_dim_line = False

        for norm_angle in (0, 180, 360):
            if dim_line_angle_from <= dim_line_angle.Deg - norm_angle <= dim_line_angle_to:
                create_dim_line = True
                break

        if not create_dim_line:
            return False, False, 0, AllplanBasisEle.TextAlignment.eLeftBottom, AllplanGeo.Line2D()

        rot_angle = AllplanGeo.Angle(-dim_line_angle.Rad)


        #----------------- get the min/max of the bars representation defined by the direction angle

        eps = math.pi / 180

        if (rep_min_max := next((value for angle, value in self.bars_rep_min_max.items() \
                                 if abs(angle - rot_angle.Rad) < eps), None)) is None:
            rep_min_max = bars_rep_util.get_min_max_of_placements(self.bars_rep_elements, rot_angle)

            self.bars_rep_min_max[rot_angle.Rad] = rep_min_max


        #----------------- get the dimension line placement data

        bars_rep_ele = bars_representation.GetBaseElementAdapter()

        dim_line_offset, at_start, placement_line_dist = \
            LabelingUtil.get_dim_line_placement_data(rep_min_max, bars_rep_util, bars_placement_line,
                                                     bars_rep_line, offset_from_placement,
                                                     bars_rep_ele.GetModelElementUUID() in self.swap_position)

        if (dim_line_position := self.dim_line_position.get(bars_rep_ele.GetModelElementUUID(), None)) is not None:
            dim_line_offset, dim_line = dim_line_position

            self.labeling_lines.append((dim_line, AllplanGeo.CalcLength(dim_line), bars_rep_ele.GetModelElementUUID()))

        else:
            dim_line_offset, dim_line = self.__search_empty_label_position(dim_line_distance, placement_line_dist, dim_line_offset,
                                                                           bars_placement_line,
                                                                           bars_representation.GetBaseElementAdapter())

            if text_align == AllplanBasisEle.TextAlignment.eMiddleTop:
                dim_line_offset += text_dist if at_start else -text_dist

        return True, at_start, dim_line_offset, text_align, dim_line


    def select_dim_line_bars_rep(self,
                                 input_pnt: AllplanGeo.Point3D,
                                 min_dist : float,
                                 text_dist: float) -> (AllplanEleAdapter.GUID | None):
        """ select the dimension line bars representation

        Args:
            input_pnt: input point
            min_dist:  minimum distance
            text_dist: text distance from the dimension line

        Returns:
            selected bars representation element
        """

        sel_bars_rep_ele = None

        for line, length, bars_rep_ele in self.labeling_lines:
            if (dim_line_position := self.dim_line_position.get(bars_rep_ele, None)) is not None:
                _, dim_line = dim_line_position
            else:
                dim_line = line

            loc_pnt = AllplanGeo.TransformCoord.PointLocal(dim_line, input_pnt)

            if loc_pnt.X < 0 or loc_pnt.X > length:
                continue

            dim_line_angle = AllplanGeo.CalcAngle(dim_line)[0]

            diff = text_dist if LabelingUtil.is_swap_text_angle(dim_line_angle) else -text_dist

            if abs(loc_pnt.Y - diff) < min_dist:
                min_dist         = abs(loc_pnt.Y)
                sel_bars_rep_ele = bars_rep_ele

        return sel_bars_rep_ele


    def get_label_offset(self,
                        bars_rep          : AllplanReinf.BarsRepresentation,
                        dim_line          : AllplanGeo.Line2D,
                        bars_ref_line_util: BarsRepresentationLineUtil,
                        text_dist         : float) -> AllplanGeo.Vector2D:
        """ get the label offset in case of intersection with the center bar

        Args:
            bars_rep:           bars representation
            dim_line:           dimension line
            bars_ref_line_util: bars representation line utility
            text_dist:          text distance from the dimension line

        Returns:
            offset
        """

        bars_rep_ele_guid = bars_rep.GetBaseElementAdapter().GetModelElementUUID()

        if self.label_size[0] != bars_rep_ele_guid:
            self.label_size = (bars_rep_ele_guid, bars_rep.GetLabelTextLength())

        dim_line_angle = AllplanGeo.CalcAngle(dim_line)[0]

        if not LabelingUtil.is_swap_text_angle(dim_line_angle):
            text_dist *= -1

        dim_line = AllplanGeo.Offset(dim_line, text_dist)[1]

        if (pnt := bars_ref_line_util.get_dim_line_center_bar_intersection(dim_line, bars_rep)) is None:
            return AllplanGeo.Vector2D()

        local_dist = AllplanGeo.Vector2D((AllplanGeo.TransformCoord.PointLocal(dim_line, pnt) - \
                                          AllplanGeo.TransformCoord.PointLocal(dim_line, dim_line.GetCenterPoint())).X, 0)

        offset = AllplanGeo.Vector2D(self.label_size[1] / 2, 0)

        offset = (local_dist + offset) if LabelingUtil.is_swap_text_angle(dim_line_angle) else (local_dist * -1 + offset) * -1

        return offset


    def __search_empty_label_position(self,
                                      dim_line_distance  : float,
                                      placement_line_dist: float,
                                      dim_line_offset    : float,
                                      placement_line     : AllplanGeo.Line2D,
                                      bars_rep_ele       : AllplanEleAdapter.BaseElementAdapter) -> tuple[float, AllplanGeo.Line2D]:
        """ search an empty label position

        Args:
            dim_line_distance:   dimension line distance
            placement_line_dist: placement line distance
            dim_line_offset:     dimension line offset
            placement_line:      placement line
            bars_rep_ele:        representation element

        Returns:
            dimension line offset, dimension line
        """

        _, label_dim_line = AllplanGeo.Offset(placement_line, placement_line_dist)

        dim_line_offset_dist = dim_line_distance if dim_line_offset > 0 else -dim_line_distance
        dim_line_dist        = dim_line_distance if placement_line_dist > 0 else -dim_line_distance

        eps = dim_line_distance / 2

        while True:
            is_modified = False

            for line, length, _ in self.labeling_lines:
                start_pnt_loc = AllplanGeo.TransformCoord.PointLocal(line, label_dim_line.StartPoint)

                if abs(start_pnt_loc.Y) > eps:
                    continue

                end_pnt_loc = AllplanGeo.TransformCoord.PointLocal(line, label_dim_line.EndPoint)

                if start_pnt_loc.X < 0 and end_pnt_loc.X < 0 or start_pnt_loc.X > length and end_pnt_loc.X > length:
                    continue

                dim_line_offset += dim_line_offset_dist

                _, label_dim_line = AllplanGeo.Offset(label_dim_line, dim_line_dist)

                is_modified = True

                break

            if not is_modified:
                break

        self.labeling_lines.append((label_dim_line, AllplanGeo.CalcLength(label_dim_line), bars_rep_ele.GetModelElementUUID()))

        return dim_line_offset, label_dim_line

```

</details>