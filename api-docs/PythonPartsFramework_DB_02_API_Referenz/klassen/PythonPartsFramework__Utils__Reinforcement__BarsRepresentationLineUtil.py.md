---
title: "BarsRepresentationLineUtil"
source: "PythonPartsFramework\Utils\Reinforcement\BarsRepresentationLineUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BarsRepresentationLineUtil

> **Pfad:** `PythonPartsFramework\Utils\Reinforcement\BarsRepresentationLineUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

implementation of the bars representation line utility class

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`

## Klassen

### `BarsRepresentationLineUtil`

implementation of the bars representation line utility class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `clear` | `self` | `None` | clear the center lines          |
| `get_visible_bars` | `self, visible_bars_ele: AllplanEleAdapter.BaseElementAdapterList, bars_rep: AllplanReinf.BarsRepresentation, visible_bars: str` | `AllplanUtil.VecIntList` | get the visible bar elements  Args:     visible_bars_ele: visible bar elements     bars_rep:         representation element     visible_bars:     visible bars  Returns:     visible bars string |
| `__get_center_index` | `self, center_index: int, bars_rep: AllplanReinf.BarsRepresentation, bars_rep_lines: list[AllplanEleAdapter.BaseElementAdapter]` | `int` | get the center index  Args:     center_index:   center index     bars_rep:       representation element     bars_rep_lines: bars representation lines  Returns:     center index |
| `get_dim_line_center_bar_intersection` | `self, dim_line: AllplanGeo.Line2D, bars_rep: AllplanReinf.BarsRepresentation` | `AllplanGeo.Point2D | None` | get the intersection point of the dimension line with the center bar  Args:     dim_line: dimension line     bars_rep: representation element  Returns:     intersection point |
| `__is_overlapped_bar_line` | `center_line: AllplanGeo.Line2D, bar_line: AllplanGeo.Line2D` | `bool` | check if the bar line is overlapped with the center line  Args:     center_line: center line     bar_line:    bar line  Returns:     overlapped state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the bars representation line utility class
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_Utility as AllplanUtil

class BarsRepresentationLineUtil:
    """ implementation of the bars representation line utility class
    """

    def __init__(self):
        """ initialize
        """

        self.center_lines = dict[AllplanEleAdapter.GUID, AllplanGeo.Line2D]()


    def clear(self):
        """ clear the center lines
        """

        self.center_lines.clear()


    def get_visible_bars(self,
                         visible_bars_ele: AllplanEleAdapter.BaseElementAdapterList,
                         bars_rep        : AllplanReinf.BarsRepresentation,
                         visible_bars    : str) -> AllplanUtil.VecIntList:
        """ get the visible bar elements

        Args:
            visible_bars_ele: visible bar elements
            bars_rep:         representation element
            visible_bars:     visible bars

        Returns:
            visible bars string
        """

        bars_rep_lines = [ele for ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildModelElements(bars_rep.GetBaseElementAdapter(),True)  # pylint: disable=line-too-long \
                          if ele == AllplanEleAdapter.BarsRepresentationLine_TypeUUID]

        bars_count = len(bars_rep_lines)

        visible_bars_new = AllplanUtil.VecIntList()
        center_index     = int(bars_count / 2) - 1

        for index in [int(item) for item in visible_bars.split(',')]:
            if 0 < index < bars_count or 0 > index > -bars_count:
                visible_bars_ele.append(bars_rep_lines[index])

                visible_bars_new.append(index)

            elif index == 0:
                center_index = self.__get_center_index(center_index, bars_rep, bars_rep_lines,)

                visible_bars_ele.append(bars_rep_lines[center_index])

                visible_bars_new.append(center_index + 1)

        return visible_bars_new


    def __get_center_index(self,
                           center_index  : int,
                           bars_rep      : AllplanReinf.BarsRepresentation,
                           bars_rep_lines: list[AllplanEleAdapter.BaseElementAdapter]) -> int:
        """ get the center index

        Args:
            center_index:   center index
            bars_rep:       representation element
            bars_rep_lines: bars representation lines

        Returns:
            center index
        """

        org_center_index = center_index

        end_index = len(bars_rep_lines) - 1

        while True:
            center_line = bars_rep_lines[center_index].GetGeometry()

            if next((True for line in self.center_lines.values() if self.__is_overlapped_bar_line(line, center_line)), False):
                if center_index == end_index:
                    self.center_lines[bars_rep.GetBaseElementAdapter().GetModelElementUUID()] = center_line

                    return org_center_index

                center_index += 1

                continue

            self.center_lines[bars_rep.GetBaseElementAdapter().GetModelElementUUID()] = center_line

            break

        return center_index


    def get_dim_line_center_bar_intersection(self,
                                             dim_line: AllplanGeo.Line2D,
                                             bars_rep: AllplanReinf.BarsRepresentation) -> (AllplanGeo.Point2D | None):
        """ get the intersection point of the dimension line with the center bar

        Args:
            dim_line: dimension line
            bars_rep: representation element

        Returns:
            intersection point
        """

        if (center_line := self.center_lines.get(bars_rep.GetBaseElementAdapter().GetModelElementUUID(), None)) is None:
            return None

        dim_line_poly = AllplanGeo.Polyline2D([dim_line.StartPoint, dim_line.EndPoint])

        found, intersection = AllplanGeo.IntersectionCalculus(center_line, dim_line_poly)

        return intersection[0] if found else None


    @staticmethod
    def __is_overlapped_bar_line(center_line: AllplanGeo.Line2D,
                                 bar_line   : AllplanGeo.Line2D) -> bool:
        """ check if the bar line is overlapped with the center line

        Args:
            center_line: center line
            bar_line:    bar line

        Returns:
            overlapped state
        """

        min_dist    = 100
        sloped_dist = 50

        pnt_loc_start = AllplanGeo.TransformCoord.PointLocal(center_line, bar_line.StartPoint)
        pnt_loc_end   = AllplanGeo.TransformCoord.PointLocal(center_line, bar_line.EndPoint)

        if abs(pnt_loc_start.Y) > min_dist or abs(pnt_loc_end.Y) > min_dist:
            return False

        if abs(pnt_loc_start.Y - pnt_loc_end.Y) > sloped_dist:
            return False

        length = AllplanGeo.CalcLength(center_line)

        return not (pnt_loc_start.X < 0 and pnt_loc_end.X < 0 or pnt_loc_start.X > length and pnt_loc_end.X > length)

```

</details>