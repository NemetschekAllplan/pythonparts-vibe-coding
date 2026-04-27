---
title: "HideElementsService"
source: "PythonPartsFramework\Utils\HideElementsService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# HideElementsService

> **Pfad:** `PythonPartsFramework\Utils\HideElementsService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the hide elements service

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `typing`

## Klassen

### `HideElementsService`

implementation of the hide elements service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `hide_arch_ground_view_elements` | `self, arch_ele: AllplanEleAdapter.BaseElementAdapter` | `None` | hide the architecture ground view elements  Args:     arch_ele: architecture element |
| `hide_opening_parent_element` | `self, opening_parent_ele: AllplanEleAdapter.BaseElementAdapter, has_independent_2d_interaction: bool` | `None` | hide the parent element of an opening  Args:     opening_parent_ele:             parent element of the opening     has_independent_2d_interaction: has independent 2d interaction state |
| `hide_element` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `None` | hide the element and the children  Args:     element: element to hide |
| `hide_elements` | `self, elements: list[AllplanEleAdapter.BaseElementAdapter] | AllplanEleAdapter.BaseElementAdapterList` | `None` | hide the elements and the children  Args:     elements: elements to hide |
| `hide_element_and_linked` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `None` | hide the element, the children and the linked elements  Args:     element: element to hide |
| `show_elements` | `self` | `None` | show the hidden elements          |
| `__show_elements` | `self, show: bool` | `None` | show/hide the elements  Args:     show: show state |
| `__remove_from_reset_hidden` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `None` | remove the elements from the reset hidden elements  Args:     element: element to hide |
| `clear` | `self` | `None` | clear the elements          |
| `get_hidden_geo_elements` | `self` | `list[Any]` | get the geometry of the hidden elements  Returns:     elements |
| `hidden_elements` | `self` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the elements  Returns:     elements |
| `__get_symbol_elements` | `parent_ele: AllplanEleAdapter.BaseElementAdapter` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the symbol elements  Args:     parent_ele: parent element  Returns:     symbol elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the hide elements service
"""

from typing import Any

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW

class HideElementsService():
    """ implementation of the hide elements service
    """

    def __init__(self):
        """ initialize
        """

        self.__hidden_elements       : list[AllplanEleAdapter.BaseElementAdapter] = []
        self.__reset_hidden_elements : list[AllplanEleAdapter.BaseElementAdapter] = []


    def hide_arch_ground_view_elements(self,
                                       arch_ele: AllplanEleAdapter.BaseElementAdapter):
        """ hide the architecture ground view elements

        Args:
            arch_ele: architecture element
        """

        reset_hidden_types = {AllplanEleAdapter.NicheTier_TypeUUID,
                              AllplanEleAdapter.RecessTier_TypeUUID}

        if arch_ele.GetElementAdapterType().GetGuid() in {AllplanEleAdapter.PolygonWall_TypeUUID,
                                                          AllplanEleAdapter.PolygonWallTier_TypeUUID} or \
           not arch_ele.GetElementAdapterType().IsTypeGroup(AllplanEleAdapter.ElementAdapterTypeGroup.eHYPERELEMENT_GROUP):
            if arch_ele == AllplanEleAdapter.PolygonWall_TypeUUID:
                arch_ele = AllplanEleAdapter.BaseElementAdapterChildElementsService.GetTierElements(arch_ele)[0]

            for element in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(arch_ele, False):
                if not isinstance(element.GetGeometry(), AllplanGeo.Polyhedron3D):
                    self.__hidden_elements.append(element)

                if element.GetElementAdapterType().GetGuid() in reset_hidden_types:
                    self.__reset_hidden_elements.append(element)

        else:
            for tier in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetTierElements(arch_ele):
                for element in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(tier, False):
                    if not isinstance(element.GetGeometry(), AllplanGeo.Polyhedron3D):
                        self.__hidden_elements.append(element)

                    self.__reset_hidden_elements += self.__get_symbol_elements(element)

        self.__show_elements(False)


    def hide_opening_parent_element(self,
                                    opening_parent_ele            : AllplanEleAdapter.BaseElementAdapter,
                                    has_independent_2d_interaction: bool):
        """ hide the parent element of an opening

        Args:
            opening_parent_ele:             parent element of the opening
            has_independent_2d_interaction: has independent 2d interaction state
        """

        if not has_independent_2d_interaction and not self.hidden_elements:
            self.hide_arch_ground_view_elements(opening_parent_ele)

        elif has_independent_2d_interaction and self.hidden_elements:
            ele_list = AllplanEleAdapter.BaseElementAdapterList([opening_parent_ele])

            AllplanIFW.VisibleService.ShowElements(ele_list, True)

            self.clear()


    def hide_element(self,
                     element: AllplanEleAdapter.BaseElementAdapter):
        """ hide the element and the children

        Args:
            element: element to hide
        """

        self.__hidden_elements.append(element)

        self.__hidden_elements += AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildModelElementsFromTree(element)

        self.__remove_from_reset_hidden(element)

        self.__show_elements(False)


    def hide_elements(self,
                      elements: (list[AllplanEleAdapter.BaseElementAdapter] | AllplanEleAdapter.BaseElementAdapterList)):
        """ hide the elements and the children

        Args:
            elements: elements to hide
        """

        for element in elements:
            self.__hidden_elements.append(element)

            self.__hidden_elements += AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildModelElementsFromTree(element)

            self.__remove_from_reset_hidden(element)

        self.__show_elements(False)


    def hide_element_and_linked(self,
                                element: AllplanEleAdapter.BaseElementAdapter):
        """ hide the element, the children and the linked elements

        Args:
            element: element to hide
        """

        self.__hidden_elements.append(element)

        self.__hidden_elements += AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(element, True)

        def get_child_elements(ele: AllplanEleAdapter.BaseElementAdapter):
            self.__hidden_elements.append(ele)

            for child_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(ele, True):
                get_child_elements(child_ele)

        for linked_ele in AllplanEleAdapter.BaseElementAdapterService.GetLinkedElements(element):
            get_child_elements(linked_ele)

        self.__show_elements(False)


    def show_elements(self):
        """ show the hidden elements
        """

        if not self.hidden_elements:
            return

        self.__show_elements(True)

        self.clear()


    def __show_elements(self,
                        show: bool):
        """ show/hide the elements

        Args:
            show: show state
        """

        AllplanIFW.VisibleService.ShowElements(AllplanEleAdapter.BaseElementAdapterList(self.__hidden_elements), show)

        AllplanIFW.VisibleService.ShowElements(AllplanEleAdapter.BaseElementAdapterList(self.__reset_hidden_elements), True)


    def __remove_from_reset_hidden(self,
                                   element: AllplanEleAdapter.BaseElementAdapter):
        """ remove the elements from the reset hidden elements

        Args:
            element: element to hide
        """

        if not self.__reset_hidden_elements:
            return

        if element in self.__reset_hidden_elements:
            self.__reset_hidden_elements.remove(element)

        for child_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(element, False):
            if child_ele in self.__reset_hidden_elements:
                self.__reset_hidden_elements.remove(child_ele)

            for symbol_ele in self.__get_symbol_elements(child_ele):
                self.__reset_hidden_elements.remove(symbol_ele)


    def clear(self):
        """ clear the elements
        """

        self.__hidden_elements.clear()
        self.__reset_hidden_elements.clear()


    @property
    def get_hidden_geo_elements(self) -> list[Any]:
        """ get the geometry of the hidden elements

        Returns:
            elements
        """

        return [geo for ele in self.__hidden_elements if (geo := ele.GetGeometry()) is not None]


    @property
    def hidden_elements(self) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the elements

        Returns:
            elements
        """

        return self.__hidden_elements


    @staticmethod
    def __get_symbol_elements(parent_ele: AllplanEleAdapter.BaseElementAdapter) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the symbol elements

        Args:
            parent_ele: parent element

        Returns:
            symbol elements
        """

        symbol_types = {AllplanEleAdapter.OpeningPart_TypeUUID,
                        AllplanEleAdapter.OpeningPartDoor_TypeUUID,
                        AllplanEleAdapter.OpeningPartWindow_TypeUUID,
                        AllplanEleAdapter.SmartPart_TypeUUID,
                        AllplanEleAdapter.DoorOpeningSmartPart_TypeUUID,
                        AllplanEleAdapter.WindowOpeningSmartPart_TypeUUID,
                        AllplanEleAdapter.DoorOpeningSmartSymbol_TypeUUID,
                        AllplanEleAdapter.WindowOpeningSmartSymbol_TypeUUID,
                        AllplanEleAdapter.NicheSmartSymbol_TypeUUID,
                        AllplanEleAdapter.RecessSmartSymbol_TypeUUID}

        return [child_ele for child_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(parent_ele, False) \
                if child_ele.GetElementAdapterType().GetGuid() in symbol_types]

```

</details>