---
title: "View"
source: "PythonPartsFramework\GeneralScripts\PythonPart\View.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# View

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPart\View.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the View

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `__future__`

## Klassen

### `View`

Definition of a view class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, viewtype: AllplanBasisEle.MacroSlideType=AllplanBasisEle.MacroSlideType.eGeometry, visibility2d: bool=True, visibility3d: bool=True, start_scale: float=0.0, end_scale: float=9999.0, elements: list[AllplanBasisEle.AllplanElement] | None=None` | `None` | initialization of view class  Args:     viewtype:     view type. Defaults to AllplanBasisElements.MacroSlideType.eGeometry.     visibility2d: visible in 2D. Defaults to True.     visibility3d: visible in 3D. Defaults to True.     start_scale:  start scale. Defaults to 0.     end_scale:    end scale. Defaults to 9999.     elements:     elements. Defaults to None. |
| `__repr__` | `self` | `str` | create the element string  Returns:     element string |
| `viewtype` | `self` | `AllplanBasisEle.MacroSlideType` | Get the type  Returns:     macros slide type |
| `visibility2d` | `self` | `bool` | Get the 2D visibility flag  Returns:     2D visibility flag |
| `visibility3d` | `self` | `bool` | Get the 3D visibility flag  Returns:     3D visibility flag |
| `visibility_layer_a` | `self` | `bool` | Get the Layer A visibility flag  Returns:     Layer A visibility flag |
| `visibility_layer_a` | `self, value: bool` | `None` | Set the Layer A visibility  Args:     value: New value for Layer A flag |
| `visibility_layer_b` | `self` | `bool` | Get the Layer B visibility flag  Returns:     Layer B visibility flag |
| `visibility_layer_b` | `self, value: bool` | `None` | Set the Layer B visibility  Args:     value: New value for Layer B flag |
| `visibility_layer_c` | `self` | `bool` | Get the Layer C visibility flag  Returns:     Layer C visibility flag |
| `visibility_layer_c` | `self, value: bool` | `None` | Set the Layer C visibility  Args:     value: New value for Layer C flag |
| `start_scale` | `self` | `float` | Get the reference start scale  Returns:     start scale |
| `end_scale` | `self` | `float` | Get the reference end scale  Returns:     end scale |
| `all_drawing_types` | `self` | `bool` | Get the all drawing types flag  Returns:     all drawing types flag |
| `all_drawing_types` | `self, value: bool` | `None` | Set the all drawing types flag  Args:     value: New value for all drawing types flag |
| `drawing_types` | `self` | `list[AllplanBaseEle.DrawingTypeService.DefaultDrawingTypes | int]` | Get the drawing types  Returns:     drawing types |
| `drawing_types` | `self, value: list[AllplanBaseEle.DrawingTypeService.DefaultDrawingTypes | int]` | `None` | Set the drawing types  Args:     value: New value for drawing types |
| `elements` | `self` | `list[AllplanBasisEle.AllplanElement]` | Get all elements  Returns:     elements |
| `add` | `self, element: AllplanBasisEle.AllplanElement` | `None` | add one element  Args:     element: element |
| `reset` | `self, elements: list[AllplanBasisEle.AllplanElement]` | `None` | Reset elements  Args:     elements: elements |
| `create` | `self` | `AllplanBasisEle.MacroSlideElement` | Create view  Returns:     macro slide element |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the View
"""
from __future__ import annotations

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle


class View():
    """ Definition of a view class
    """

    def __init__(self,
                 viewtype     : AllplanBasisEle.MacroSlideType                = AllplanBasisEle.MacroSlideType.eGeometry,
                 visibility2d: bool                                           = True,
                 visibility3d: bool                                           = True,
                 start_scale  : float                                         = 0.,
                 end_scale    : float                                         = 9999.,
                 elements     : (list[AllplanBasisEle.AllplanElement] | None) = None):
        """ initialization of view class

        Args:
            viewtype:     view type. Defaults to AllplanBasisElements.MacroSlideType.eGeometry.
            visibility2d: visible in 2D. Defaults to True.
            visibility3d: visible in 3D. Defaults to True.
            start_scale:  start scale. Defaults to 0.
            end_scale:    end scale. Defaults to 9999.
            elements:     elements. Defaults to None.
        """
        self._start_scale        = start_scale
        self._end_scale          = end_scale
        self._visibility2d       = visibility2d
        self._visibility3d       = visibility3d
        self._visibility_layer_a = True
        self._visibility_layer_b = True
        self._visibility_layer_c = True
        self._viewtype           = viewtype
        self._elements           = elements if elements is not None else []
        self._all_drawing_types  = True
        self._drawing_types      = []

    def __repr__(self) ->str:
        """ create the element string

        Returns:
            element string
        """

        return f"View(_start_scale  ={self._start_scale}, " \
               f"_end_scale         ={self._end_scale}, " \
               f"_visibility2d      ={self._visibility2d}, " \
               f"_visibility3d      ={self._visibility3d}," \
               f"_visibility_layer_a={self._visibility_layer_a}, " \
               f"_visibility_layer_b={self._visibility_layer_b}, " \
               f"_visibility_layer_c={self._visibility_layer_c}, " \
               f"_viewtype          ={self._viewtype}\n" + \
            str(self._elements)

    @property
    def viewtype(self) -> AllplanBasisEle.MacroSlideType:
        """ Get the type

        Returns:
            macros slide type
        """
        return self._viewtype


    @property
    def visibility2d(self) -> bool:
        """ Get the 2D visibility flag

        Returns:
            2D visibility flag
        """
        return self._visibility2d

    @property
    def visibility3d(self) -> bool:
        """ Get the 3D visibility flag

        Returns:
            3D visibility flag
        """
        return self._visibility3d

    @property
    def visibility_layer_a(self) -> bool:
        """ Get the Layer A visibility flag

        Returns:
            Layer A visibility flag
        """
        return self._visibility_layer_a

    @visibility_layer_a.setter
    def visibility_layer_a(self,
                           value: bool):
        """ Set the Layer A visibility

        Args:
            value: New value for Layer A flag
        """
        self._visibility_layer_a = value

    @property
    def visibility_layer_b(self) -> bool:
        """ Get the Layer B visibility flag

        Returns:
            Layer B visibility flag
        """
        return self._visibility_layer_b

    @visibility_layer_b.setter
    def visibility_layer_b(self,
                           value: bool):
        """ Set the Layer B visibility

        Args:
            value: New value for Layer B flag
        """
        self._visibility_layer_b = value

    @property
    def visibility_layer_c(self) -> bool:
        """ Get the Layer C visibility flag

        Returns:
            Layer C visibility flag
        """
        return self._visibility_layer_c

    @visibility_layer_c.setter
    def visibility_layer_c(self,
                           value: bool):
        """ Set the Layer C visibility

        Args:
            value: New value for Layer C flag
        """
        self._visibility_layer_c = value

    @property
    def start_scale(self) -> float:
        """ Get the reference start scale

        Returns:
            start scale
        """
        return self._start_scale

    @property
    def end_scale(self) -> float:
        """ Get the reference end scale

        Returns:
            end scale
        """
        return self._end_scale

    @property
    def all_drawing_types(self) -> bool:
        """ Get the all drawing types flag

        Returns:
            all drawing types flag
        """
        return self._all_drawing_types

    @all_drawing_types.setter
    def all_drawing_types(self,
                          value: bool):
        """ Set the all drawing types flag

        Args:
            value: New value for all drawing types flag
        """
        self._all_drawing_types = value

    @property
    def drawing_types(self) -> list[AllplanBaseEle.DrawingTypeService.DefaultDrawingTypes | int]:
        """ Get the drawing types

        Returns:
            drawing types
        """
        return self._drawing_types

    @drawing_types.setter
    def drawing_types(self, value: list[AllplanBaseEle.DrawingTypeService.DefaultDrawingTypes | int]):
        """ Set the drawing types

        Args:
            value: New value for drawing types
        """
        self._drawing_types = value

    @property
    def elements(self) -> list[AllplanBasisEle.AllplanElement]:
        """ Get all elements

        Returns:
            elements
        """
        return self._elements

    def add(self, element: AllplanBasisEle.AllplanElement):
        """ add one element

        Args:
            element: element
        """
        self._elements.append(element)

    def reset(self, elements: list[AllplanBasisEle.AllplanElement]):
        """ Reset elements

        Args:
            elements: elements
        """
        self._elements = elements

    def create(self) -> AllplanBasisEle.MacroSlideElement:
        """ Create view

        Returns:
            macro slide element
        """

        slide_props                  = AllplanBasisEle.MacroSlideProperties()
        slide_props.VisibilityGeo2D  = self.visibility2d
        slide_props.VisibilityGeo3D  = self.visibility3d
        slide_props.VisibilityLayerA = self.visibility_layer_a
        slide_props.VisibilityLayerB = self.visibility_layer_b
        slide_props.VisibilityLayerC = self.visibility_layer_c
        slide_props.Type             = self.viewtype
        slide_props.StartScaleRange  = self.start_scale
        slide_props.EndScaleRange    = self.end_scale
        slide_props.AllDrawingTypes  = self.all_drawing_types
        slide_props.DrawingTypes     = self.drawing_types

        return AllplanBasisEle.MacroSlideElement(slide_props, self._elements)

```

</details>