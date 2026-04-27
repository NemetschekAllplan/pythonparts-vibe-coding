---
title: "OpeningModificationUtil"
source: "PythonPartsFramework\Utils\Architecture\OpeningModificationUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningModificationUtil

> **Pfad:** `PythonPartsFramework\Utils\Architecture\OpeningModificationUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the opening modification utilities

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`

## Klassen

### `OpeningModificationUtil`

implementation of the opening modification utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_opening_element` | `selected_ele: AllplanEleAdapter.BaseElementAdapter` | `AllplanEleAdapter.BaseElementAdapter` | get the opening element from the selected element  Args:     selected_ele: selected element  Returns:     opening element |
| `get_placement_element` | `opening_ele: AllplanEleAdapter.BaseElementAdapter, opening_start_pnt: AllplanGeo.Point2D` | `tuple[AllplanEleAdapter.BaseElementAdapter, AllplanGeo.Polygon2D, AllplanGeo.Line2D, AllplanGeo.Line2D | AllplanGeo.Arc2D]` | get the placement element data of the opening  Args:     opening_ele:       opening element     opening_start_pnt: opening start point  Returns:     placement element, placement element geometry, placement line, placement element axis |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening modification utilities
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

class OpeningModificationUtil():
    """ implementation of the opening modification utilities
    """

    @staticmethod
    def get_opening_element(selected_ele: AllplanEleAdapter.BaseElementAdapter) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the opening element from the selected element

        Args:
            selected_ele: selected element

        Returns:
            opening element
        """

        opening_ele = selected_ele

        if opening_ele.GetElementAdapterType().GetGuid() in {AllplanEleAdapter.NicheTier_TypeUUID,
                                                             AllplanEleAdapter.RecessTier_TypeUUID,
                                                             AllplanEleAdapter.PolygonalNicheTier_TypeUUID,
                                                             AllplanEleAdapter.PolygonalRecessTier_TypeUUID,
                                                             AllplanEleAdapter.DoorTier_TypeUUID,
                                                             AllplanEleAdapter.WindowTier_TypeUUID,
                                                             AllplanEleAdapter.WindowDoorTier_TypeUUID}:
            opening_ele = AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(opening_ele)

        return opening_ele


    @staticmethod
    def get_placement_element(opening_ele      : AllplanEleAdapter.BaseElementAdapter,
                              opening_start_pnt: AllplanGeo.Point2D) -> tuple[AllplanEleAdapter.BaseElementAdapter,
                                                                              AllplanGeo.Polygon2D, AllplanGeo.Line2D,
                                                                              (AllplanGeo.Line2D | AllplanGeo.Arc2D)]:
        """ get the placement element data of the opening

        Args:
            opening_ele:       opening element
            opening_start_pnt: opening start point

        Returns:
            placement element, placement element geometry, placement line, placement element axis
        """

        placement_ele = AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(opening_ele)

        min_dist = 1.0e10


        #----------------- get the placement line located at the opening start point

        placement_ele_geo : AllplanGeo.Polygon2D = AllplanGeo.Polygon2D()

        if placement_ele.GetElementAdapterType().IsTypeGroup(AllplanEleAdapter.ElementAdapterTypeGroup.eHYPERELEMENT_GROUP):
            for tier_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetTierElements(placement_ele):
                tier_geo = tier_ele.GetGeometry()

                if (dist := abs(AllplanGeo.TransformCoord.PointLocal(AllplanGeo.Polyline2D(tier_geo), opening_start_pnt).Y)) < min_dist:
                    min_dist = dist

                    placement_ele_geo = tier_geo
        else:
            placement_ele_geo = placement_ele.GetGeometry()

        _, placement_line = AllplanGeo.Polyline2DUtil.GetPolyline2DSegment(AllplanGeo.Polyline2D(placement_ele_geo),
                                                                           opening_start_pnt)

        if (placement_ele_axis := AllplanEleAdapter.AxisElementAdapter(placement_ele).GetAxis()) is None:
            placement_ele_axis = placement_line

        return placement_ele, placement_ele_geo, placement_line, placement_ele_axis

```

</details>