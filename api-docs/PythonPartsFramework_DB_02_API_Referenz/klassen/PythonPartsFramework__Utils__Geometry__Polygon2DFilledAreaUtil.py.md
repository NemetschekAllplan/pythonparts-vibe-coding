---
title: "Polygon2DFilledAreaUtil"
source: "PythonPartsFramework\Utils\Geometry\Polygon2DFilledAreaUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Polygon2DFilledAreaUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\Polygon2DFilledAreaUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the Polygon2DFilledAreaUtil

- add hatching, pattern, filling, face style or surface element properties
- create filled area with polygon2D

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_ArchElements`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `TypeCollections.ModelEleList`
- `Utils.General.FilledAreaUtil`

## Klassen

### `Polygon2DFilledAreaUtil`

implementation of the Polygon2DFilledAreaUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize the Polygon2DFilledAreaUtil          |
| `set_hatching` | `self, hatching_prop: AllplanBasisEle.HatchingProperties | None` | `None` | set the hatching properties  Args:     hatching_prop: hatching properties |
| `set_pattern` | `self, pattern_prop: AllplanBasisEle.PatternProperties | None` | `None` | set the pattern properties  Args:     pattern_prop: pattern properties |
| `set_filling` | `self, filling_prop: AllplanBasisEle.FillingProperties | None` | `None` | set the filling properties  Args:     filling_prop: filling properties |
| `set_face_style` | `self, face_style_prop: AllplanBasisEle.FaceStyleProperties | None` | `None` | set the face style properties  Args:     face_style_prop: face style properties |
| `set_surface_ele` | `self, surface_prop: AllplanArchEle.SurfaceElementProperties | None` | `None` | set the surface element properties  Args:     surface_prop: surface element properties |
| `set_common_properties` | `self, com_prop: AllplanBaseEle.CommonProperties | None` | `None` | set the common properties  Args:     com_prop: common properties |
| `execute` | `self, model_ele_list: ModelEleList, polygon: AllplanGeo.Polygon2D, visible_polygon: bool, visible_area: bool=True` | `None` | create the filled area depending on the current filled area properties     and add it to the model element list  Args:     model_ele_list:  model element list     polygon:         polygon (created with the common properties of the model element list)     visible_polygon: visible polygon state     visible_area:    visible area state |
| `__add_polygon` | `self, model_ele_list: ModelEleList, polygon: AllplanGeo.Polygon2D` | `None` | add a polygon  Args:     model_ele_list: model element list     polygon:        polygon |
| `__add_area_element` | `self, model_ele_list: ModelEleList, polygon: AllplanGeo.Polygon2D` | `None` | add the area element  Args:     model_ele_list: model element list     polygon:        polygon |
| `__create_prop_from_surface_element` | `self, com_prop: AllplanBaseEle.CommonProperties, polygon: AllplanGeo.Polygon2D` | `AllplanBasisEle.AllplanElement | None` | create the properties from the surface element  Args:     com_prop: common properties     polygon:  polygon  Returns:     created element |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Polygon2DFilledAreaUtil

    - add hatching, pattern, filling, face style or surface element properties
    - create filled area with polygon2D
"""

# pylint: disable=no-self-use

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Geometry as AllplanGeo

from TypeCollections.ModelEleList import ModelEleList

from Utils.General.FilledAreaUtil import FilledAreaUtil

class Polygon2DFilledAreaUtil():
    """ implementation of the Polygon2DFilledAreaUtil
    """

    def __init__(self):
        """ initialize the Polygon2DFilledAreaUtil
        """

        self.length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        self.__hatching_prop   : (AllplanBasisEle.HatchingProperties | None)      = None
        self.__pattern_prop    : (AllplanBasisEle.PatternProperties | None)       = None
        self.__filling_prop    : (AllplanBasisEle.FillingProperties | None)       = None
        self.__face_style_prop : (AllplanBasisEle.FaceStyleProperties | None)     = None
        self.__surface_prop    : (AllplanArchEle.SurfaceElementProperties | None) = None
        self.__area_com_prop   : (AllplanBaseEle.CommonProperties | None)         = None


    def set_hatching(self,
                     hatching_prop: (AllplanBasisEle.HatchingProperties | None)):
        """ set the hatching properties

        Args:
            hatching_prop: hatching properties
        """

        self.__hatching_prop = hatching_prop


    def set_pattern(self,
                    pattern_prop: (AllplanBasisEle.PatternProperties | None)):
        """ set the pattern properties

        Args:
            pattern_prop: pattern properties
        """

        self.__pattern_prop = pattern_prop


    def set_filling(self,
                    filling_prop: (AllplanBasisEle.FillingProperties | None)):
        """ set the filling properties

        Args:
            filling_prop: filling properties
        """

        self.__filling_prop = filling_prop


    def set_face_style(self,
                      face_style_prop: (AllplanBasisEle.FaceStyleProperties | None)):
        """ set the face style properties

        Args:
            face_style_prop: face style properties
        """

        self.__face_style_prop = face_style_prop


    def set_surface_ele(self,
                        surface_prop: (AllplanArchEle.SurfaceElementProperties | None)):
        """ set the surface element properties

        Args:
            surface_prop: surface element properties
        """

        self.__surface_prop = surface_prop


    def set_common_properties(self,
                              com_prop: (AllplanBaseEle.CommonProperties | None)):
        """ set the common properties

        Args:
            com_prop: common properties
        """

        self.__area_com_prop = com_prop


    def execute(self,
                model_ele_list : ModelEleList,
                polygon        : AllplanGeo.Polygon2D,
                visible_polygon: bool,
                visible_area   : bool = True):
        """ create the filled area depending on the current filled area properties
            and add it to the model element list

        Args:
            model_ele_list:  model element list
            polygon:         polygon (created with the common properties of the model element list)
            visible_polygon: visible polygon state
            visible_area:    visible area state
        """

        if not polygon.IsValid():
            return

        if visible_polygon:
            self.__add_polygon(model_ele_list, polygon)

        if visible_area:
            self.__add_area_element(model_ele_list, polygon)


    def __add_polygon(self,
                      model_ele_list : ModelEleList,
                      polygon        : AllplanGeo.Polygon2D):
        """ add a polygon

        Args:
            model_ele_list: model element list
            polygon:        polygon
        """

        if not polygon.IsValid():
            return

        model_ele_list.append_geometry_2d(polygon)


    def __add_area_element(self,
                           model_ele_list: ModelEleList,
                           polygon       : AllplanGeo.Polygon2D):
        """ add the area element

        Args:
            model_ele_list: model element list
            polygon:        polygon
        """

        com_prop = model_ele_list.get_common_properties() if self.__area_com_prop is None else self.__area_com_prop

        if self.__hatching_prop is not None:
            model_ele_list.append(AllplanBasisEle.HatchingElement(com_prop, self.__hatching_prop, polygon))

        elif self.__pattern_prop is not None:
            model_ele_list.append(AllplanBasisEle.PatternElement(com_prop, self.__pattern_prop, polygon))

        elif self.__filling_prop is not None:
            model_ele_list.append(AllplanBasisEle.FillingElement(com_prop, self.__filling_prop, polygon))

        elif self.__face_style_prop is not None:
            model_ele_list.append(AllplanBasisEle.FaceStyleElement(com_prop, self.__face_style_prop, polygon))

        elif (ele := self.__create_prop_from_surface_element(com_prop, polygon)) is not None:
            model_ele_list.append(ele)


    def __create_prop_from_surface_element(self,
                                           com_prop: AllplanBaseEle.CommonProperties,
                                           polygon : AllplanGeo.Polygon2D) -> (AllplanBasisEle.AllplanElement | None):
        """ create the properties from the surface element

        Args:
            com_prop: common properties
            polygon:  polygon

        Returns:
            created element
        """

        if self.__surface_prop is None:
            return None

        bg_color = self.__surface_prop.FillingID if self.__surface_prop.FillingSelected else None

        if self.__surface_prop.BitmapSelected:
            return AllplanBasisEle.BitmapAreaElement(com_prop,
                                                     FilledAreaUtil.create_default_bitmap(self.__surface_prop.BitmapID), polygon)

        if self.__surface_prop.FaceStyleSelected:
            return AllplanBasisEle.FaceStyleElement(com_prop,
                                                    FilledAreaUtil.create_default_face_style(self.__surface_prop.FaceStyleID), polygon)

        if self.__surface_prop.HatchSelected:
            return AllplanBasisEle.HatchingElement(com_prop,
                                                   FilledAreaUtil.create_default_hatching(self.__surface_prop.HatchID, bg_color), polygon)

        if self.__surface_prop.PatternSelected:
            return AllplanBasisEle.PatternElement(com_prop,
                                                  FilledAreaUtil.create_default_pattern(self.__surface_prop.PatternID, bg_color), polygon)

        if self.__surface_prop.FillingSelected:
            return AllplanBasisEle.FillingElement(com_prop,
                                                  FilledAreaUtil.create_no_transition_filling(self.__surface_prop.FillingID), polygon)

        return None

```

</details>