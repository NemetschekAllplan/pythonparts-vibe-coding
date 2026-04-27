---
title: "BaseElementAdapterFilter"
source: "PythonPartsFramework\Utils\BaseElementAdapterFilter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BaseElementAdapterFilter

> **Pfad:** `PythonPartsFramework\Utils\BaseElementAdapterFilter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the base element adapter filter

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`

## Klassen

### `BaseElementAdapterFilter`

implementation of the base element adapter filter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_python_part` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `AllplanEleAdapter.BaseElementAdapter` | get PythonPart  Args:     elements: elements to filter  Returns:     filtered element |
| `get_bar_definitions` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for all type of bar definitions  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_mesh_definitions` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for all type of mesh definitions  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_bar_placements` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for all type of bar definitions  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_wall_tiers` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for all type of wall tiers definitions  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_opening_tiers` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for all type of opening tiers definitions  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_slab_tiers` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for all type of wall tiers definitions  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_slab_foundation_tiers` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for all type of slab foundation tiers definitions  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_facing` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for facing  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_door_swing` | `elements: AllplanEleAdapter.BaseElementAdapterList` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for door swing  Args:     elements: elements to filter  Returns:     filtered elements |
| `get_elements_by_type` | `elements: AllplanEleAdapter.BaseElementAdapterList, type_uuid: AllplanEleAdapter.GUID` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements for the type  Args:     elements:  elements to filter     type_uuid: element type  Returns:     filtered elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base element adapter filter
"""

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

class BaseElementAdapterFilter():
    """ implementation of the base element adapter filter
    """

    @staticmethod
    def get_python_part(elements: AllplanEleAdapter.BaseElementAdapterList) -> AllplanEleAdapter.BaseElementAdapter:
        """ get PythonPart

        Args:
            elements: elements to filter

        Returns:
            filtered element
        """

        return next((element for element in elements if AllplanBaseEle.PythonPartService.IsPythonPartElement(element)),
                    AllplanEleAdapter.BaseElementAdapter())


    @staticmethod
    def get_bar_definitions(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for all type of bar definitions

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        bar_def_type_uuids = {AllplanEleAdapter.BarsDefinition_TypeUUID,
                              AllplanEleAdapter.BarsAreaDefinition_TypeUUID}

        return [element for element in elements if element.GetElementAdapterType().GetGuid() in bar_def_type_uuids]


    @staticmethod
    def get_mesh_definitions(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for all type of mesh definitions

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        bar_def_type_uuids = {AllplanEleAdapter.MeshDefinition_TypeUUID,
                              AllplanEleAdapter.BendedMeshDefinition_TypeUUID,
                              AllplanEleAdapter.MeshPlacementDefinition_TypeUUID}

        return [element for element in elements if element.GetElementAdapterType().GetGuid() in bar_def_type_uuids]


    @staticmethod
    def get_bar_placements(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for all type of bar definitions

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        placement_uuids = {AllplanEleAdapter.BarsLinearPlacement_TypeUUID,
                           AllplanEleAdapter.BarsLinearMultiPlacement_TypeUUID,
                           AllplanEleAdapter.BarsAreaPlacement_TypeUUID,
                           AllplanEleAdapter.BarsSpiralPlacement_TypeUUID,
                           AllplanEleAdapter.BarsCircularPlacement_TypeUUID,
                           AllplanEleAdapter.BarsRotationalSolidPlacement_TypeUUID,
                           AllplanEleAdapter.BarsRotationalPlacement_TypeUUID,
                           AllplanEleAdapter.BarsTangentionalPlacement_TypeUUID,
                           AllplanEleAdapter.BarsEndBendingPlacement_TypeUUID}

        return [element for element in elements if element.GetElementAdapterType().GetGuid() in placement_uuids]


    @staticmethod
    def get_wall_tiers(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for all type of wall tiers definitions

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        wall_tier_uuids = {AllplanEleAdapter.WallTier_TypeUUID,
                           AllplanEleAdapter.ElementWallTier_TypeUUID,
                           AllplanEleAdapter.PolygonWallTier_TypeUUID,
                           AllplanEleAdapter.ProfileWallTier_TypeUUID,
                           AllplanEleAdapter.CircularWallTier_TypeUUID}

        return [element for element in elements if element.GetElementAdapterType().GetGuid() in wall_tier_uuids]


    @staticmethod
    def get_opening_tiers(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for all type of opening tiers definitions

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        wall_tier_uuids = {AllplanEleAdapter.DoorTier_TypeUUID,
                           AllplanEleAdapter.WindowTier_TypeUUID,
                           AllplanEleAdapter.WindowDoorTier_TypeUUID,
                           AllplanEleAdapter.NicheTier_TypeUUID,
                           AllplanEleAdapter.RecessTier_TypeUUID,
                           AllplanEleAdapter.PolygonalNicheTier_TypeUUID,
                           AllplanEleAdapter.PolygonalRecessTier_TypeUUID,
                           AllplanEleAdapter.JointTier_TypeUUID,
                           AllplanEleAdapter.FlushPierTier_TypeUUID}
        

        return [element for element in elements if element.GetElementAdapterType().GetGuid() in wall_tier_uuids]


    @staticmethod
    def get_slab_tiers(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for all type of wall tiers definitions

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        return [element for element in elements if element.GetElementAdapterType() == AllplanEleAdapter.Slab_TypeUUID]
    

    @staticmethod
    def get_slab_foundation_tiers(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for all type of slab foundation tiers definitions

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        return [element for element in elements if element.GetElementAdapterType() == AllplanEleAdapter.SlabFoundationTier_TypeUUID]


    @staticmethod
    def get_facing(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for facing

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        return [element for element in elements if element.GetElementAdapterType() == AllplanEleAdapter.Facing_TypeUUID]


    @staticmethod
    def get_door_swing(elements: AllplanEleAdapter.BaseElementAdapterList) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for door swing

        Args:
            elements: elements to filter

        Returns:
            filtered elements
        """

        elements_by_type = BaseElementAdapterFilter.get_elements_by_type(elements, AllplanEleAdapter.DoorSwing_TypeUUID)

        door_swing_elements = []

        for element in elements_by_type:
            door_swing_elements += list(AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(element, False))

        return door_swing_elements



    @staticmethod
    def get_elements_by_type(elements : AllplanEleAdapter.BaseElementAdapterList,
                            type_uuid: AllplanEleAdapter.GUID) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements for the type

        Args:
            elements:  elements to filter
            type_uuid: element type

        Returns:
            filtered elements
        """

        return [element for element in elements if element == type_uuid]

```

</details>