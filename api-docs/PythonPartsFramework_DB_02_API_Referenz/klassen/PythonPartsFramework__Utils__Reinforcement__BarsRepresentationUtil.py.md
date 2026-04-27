---
title: "BarsRepresentationUtil"
source: "PythonPartsFramework\Utils\Reinforcement\BarsRepresentationUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BarsRepresentationUtil

> **Pfad:** `PythonPartsFramework\Utils\Reinforcement\BarsRepresentationUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `utility`

## Übersicht

implementation of the bars representation utility class

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Reinforcement`

## Klassen

### `BarsRepresentationUtil`

implementation of the bars representation utility class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, bars_rep: AllplanReinf.BarsRepresentation` | `None` | initialize  Args:     bars_rep: representation element |
| `get_local_min_max_of_placement` | `self, placement_line: AllplanGeo.Line2D` | `AllplanGeo.MinMax2D` | get the min/max box of the placement  Args:     placement_line: placement line  Returns:     min/max box of the representation elements |
| `get_min_max_of_placements` | `bars_ref_elements: list[AllplanEleAdapter.BaseElementAdapter], direction_angle: AllplanGeo.Angle` | `AllplanGeo.MinMax2D` | get the min/max box of the placements defined by the representation elements local to the direction angle  Args:     bars_ref_elements: representation elements     direction_angle:   direction angle  Returns:     min/max box of the representation elements |
| `is_placement_labeling` | `self` | `tuple[bool, bool]` | check if the labeling is for the placement  Returns:     label is for the placement, line representation state |
| `are_all_bars_visible_in_representation` | `self` | `bool` | check if all bars are visible in the representation  Returns:     all bars are visible in the representation |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the bars representation utility class
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Reinforcement as AllplanReinf

class BarsRepresentationUtil:
    """ implementation of the bars representation utility class
    """

    def __init__(self,
                 bars_rep: AllplanReinf.BarsRepresentation):
        """ initialize

        Args:
            bars_rep: representation element
        """

        self.bars_rep         = bars_rep
        self.bars_rep_geo_ele = []

        for ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildModelElements(bars_rep.GetBaseElementAdapter(),
                                                                                                  True):
            if ele != AllplanEleAdapter.BarsRepresentationLine_TypeUUID:
                continue

            if (rep_geo := ele.GetGeometry()) is not None:
                self.bars_rep_geo_ele.append(rep_geo)


    def get_local_min_max_of_placement(self,
                                       placement_line: AllplanGeo.Line2D) -> AllplanGeo.MinMax2D:
        """ get the min/max box of the placement

        Args:
            placement_line: placement line

        Returns:
            min/max box of the representation elements
        """

        min_max = AllplanGeo.MinMax2D()

        for geo_ele in self.bars_rep_geo_ele:
            if isinstance(geo_ele, AllplanGeo.Point2D):
                min_max += AllplanGeo.TransformCoord.PointLocal(placement_line, geo_ele)

            elif isinstance(geo_ele, AllplanGeo.Line2D):
                min_max += AllplanGeo.TransformCoord.PointLocal(placement_line, geo_ele.StartPoint)
                min_max += AllplanGeo.TransformCoord.PointLocal(placement_line, geo_ele.EndPoint)

            elif isinstance(geo_ele, AllplanGeo.Polyline2D):
                for point in geo_ele.Points:
                    min_max += AllplanGeo.TransformCoord.PointLocal(placement_line, point)

        return min_max


    @staticmethod
    def get_min_max_of_placements(bars_ref_elements: list[AllplanEleAdapter.BaseElementAdapter],
                                  direction_angle  : AllplanGeo.Angle) -> AllplanGeo.MinMax2D:
        """ get the min/max box of the placements defined by the representation elements local to the direction angle

        Args:
            bars_ref_elements: representation elements
            direction_angle:   direction angle

        Returns:
            min/max box of the representation elements
        """

        min_max = AllplanGeo.MinMax2D()

        for rep_ele in bars_ref_elements:
            for ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildModelElements(rep_ele, True):
                if ele != AllplanEleAdapter.BarsRepresentationLine_TypeUUID:
                    continue

                trans_geo = AllplanGeo.Rotate(ele.GetGeometry(), direction_angle)

                min_max += AllplanGeo.CalcMinMax(trans_geo)[0]

        return min_max


    def is_placement_labeling(self) -> tuple[bool, bool]:
        """ check if the labeling is for the placement

        Returns:
            label is for the placement, line representation state
        """

        start_geo = None
        min_dist  = 10

        for rep_geo in self.bars_rep_geo_ele:
            if isinstance(rep_geo, AllplanGeo.Polyline2D) and rep_geo.Count() > 2:
                return False, False

            if start_geo is None:
                start_geo = rep_geo
                continue

            if isinstance(rep_geo, AllplanGeo.Point2D) and isinstance(start_geo, AllplanGeo.Point2D) and \
               AllplanGeo.Vector2D(start_geo, rep_geo).GetLength() > min_dist:
                return True, False

            if isinstance(rep_geo, AllplanGeo.Line2D) and isinstance(start_geo, AllplanGeo.Line2D) and \
               AllplanGeo.Vector2D(start_geo.StartPoint, rep_geo.StartPoint).GetLength() > min_dist:
                return True, True

            if isinstance(rep_geo, AllplanGeo.Polyline2D) and isinstance(start_geo, AllplanGeo.Polyline2D) and \
               AllplanGeo.Vector2D(start_geo.StartPoint, rep_geo.StartPoint).GetLength() > min_dist:
                return True, True

            return False, False

        return False, False


    def are_all_bars_visible_in_representation(self) -> bool:
        """ check if all bars are visible in the representation

        Returns:
            all bars are visible in the representation
        """

        return len(self.bars_rep_geo_ele) == self.bars_rep.GetBarPlacement().GetBarCount()

```

</details>