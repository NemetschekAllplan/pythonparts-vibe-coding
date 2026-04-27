---
title: "PythonPartViewModelEleList"
source: "PythonPartsFramework\TypeCollections\PythonPartViewModelEleList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# PythonPartViewModelEleList

> **Pfad:** `PythonPartsFramework\TypeCollections\PythonPartViewModelEleList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dokumentation`

## Übersicht

implementation of the PythonPartViewModelEleList class

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementAttributeList`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `PythonPartUtil`
- `PythonPartViewData`
- `TypeCollections.ModelEleList`
- `Utils.Geometry.TransformationStack`

## Klassen

### `PythonPartViewModelEleList`

PythonPartViewModelEleList class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, trans_stack: TransformationStack=TransformationStack()` | `None` | initialize  Args:     trans_stack: transformation stack |
| `add_view` | `self, name: str, visible_in_2d: bool=True, visible_in_3d: bool=True, start_scale: float=0, end_scale: float=9999, ref_pnt1_x: float=0, ref_pnt1_y: float=0, ref_pnt1_z: float=0, ref_pnt2_x: float=0, ref_pnt2_y: float=0, ref_pnt2_z: float=0, visibility_layer_a: bool=True, visibility_layer_b: bool=True, visibility_layer_c: bool=True, scale_x: int=1, scale_y: int=2, scale_z: int=3, all_drawing_types: bool=True, drawing_types: list[int | AllplanBaseEle.DrawingTypeService.DefaultDrawingTypes] | None=None` | `None` | add a view to the view model element list  Args:     name:               name of the modified property     visible_in_2d:      2D visible state     visible_in_3d:      3D visible state     start_scale:        start scale     end_scale:          end scale     ref_pnt1_x:         x coordinate of the first reference point     ref_pnt1_y:         y coordinate of the first reference point     ref_pnt1_z:         z coordinate of the first reference point     ref_pnt2_x:         x coordinate of the second reference point     ref_pnt2_y:         y coordinate of the second reference point     ref_pnt2_z:         z coordinate of the second reference point     visibility_layer_a: visible state for layer a     visibility_layer_b: visible state for layer b     visibility_layer_c: visible state for layer cS     scale_x:            x scaling factor     scale_y:            y scaling factor     scale_z:            z scaling factor     all_drawing_types:  description     drawing_types:      description |
| `get_default_3d_view_model_ele_list` | `self` | `ModelEleList` | get the model element list of the 3D default view  Returns:     model element list of the 3D default view |
| `get_view_model_ele_list` | `self, name: str` | `ModelEleList` | get the model element list for the view defined by name  Args:     name: name of the view  Returns:     get the model element list for the current view |
| `create_pythonpart` | `self, build_ele: BuildingElement, build_ele_attr_list: BuildingElementAttributeList, local_placement_matrix: AllplanGeo.Matrix3D=AllplanGeo.Matrix3D()` | `ModelEleList` | create the PythonPart  Args:     build_ele:              building element with the parameter properties     build_ele_attr_list:    building element attribute list     local_placement_matrix: local placement matrix for the PythonPart  Returns:     PythonPart elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPartViewModelEleList class
"""

# pylint: disable=too-many-arguments

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo

from BuildingElement import BuildingElement
from BuildingElementAttributeList import BuildingElementAttributeList
from PythonPartUtil import PythonPartUtil
from PythonPartViewData import PythonPartViewData

from TypeCollections.ModelEleList import ModelEleList

from Utils.Geometry.TransformationStack import TransformationStack

class PythonPartViewModelEleList():
    """ PythonPartViewModelEleList class
    """

    def __init__(self,
                 trans_stack: TransformationStack = TransformationStack()):
        """ initialize

        Args:
            trans_stack: transformation stack
        """

        self.__trans_stack = trans_stack

        self.__view_model_ele_list :dict[str, tuple[PythonPartViewData, ModelEleList]] = {}

        self.__view_model_ele_list["0_2D_3D"] = (PythonPartViewData(True, True), ModelEleList(trans_stack = trans_stack))
        self.__view_model_ele_list["0_2D"]    = (PythonPartViewData(True, False), ModelEleList(trans_stack = trans_stack))
        self.__view_model_ele_list["0_3D"]    = (PythonPartViewData(False, True), ModelEleList(trans_stack = trans_stack))

        self.__model_ele_list : (ModelEleList | None) = None


    def add_view(self,
                 name              : str,
                 visible_in_2d     : bool                                                                       = True,
                 visible_in_3d     : bool                                                                       = True,
                 start_scale       : float                                                                      = 0,
                 end_scale         : float                                                                      = 9999,
                 ref_pnt1_x        : float                                                                      = 0,
                 ref_pnt1_y        : float                                                                      = 0,
                 ref_pnt1_z        : float                                                                      = 0,
                 ref_pnt2_x        : float                                                                      = 0,
                 ref_pnt2_y        : float                                                                      = 0,
                 ref_pnt2_z        : float                                                                      = 0,
                 visibility_layer_a: bool                                                                       = True,
                 visibility_layer_b: bool                                                                       = True,
                 visibility_layer_c: bool                                                                       = True,
                 scale_x           : int                                                                        = 1,
                 scale_y           : int                                                                        = 2,
                 scale_z           : int                                                                        = 3,
                 all_drawing_types : bool                                                                       = True,
                 drawing_types     : (list[int | AllplanBaseEle.DrawingTypeService.DefaultDrawingTypes] | None) = None):
        """ add a view to the view model element list

        Args:
            name:               name of the modified property
            visible_in_2d:      2D visible state
            visible_in_3d:      3D visible state
            start_scale:        start scale
            end_scale:          end scale
            ref_pnt1_x:         x coordinate of the first reference point
            ref_pnt1_y:         y coordinate of the first reference point
            ref_pnt1_z:         z coordinate of the first reference point
            ref_pnt2_x:         x coordinate of the second reference point
            ref_pnt2_y:         y coordinate of the second reference point
            ref_pnt2_z:         z coordinate of the second reference point
            visibility_layer_a: visible state for layer a
            visibility_layer_b: visible state for layer b
            visibility_layer_c: visible state for layer cS
            scale_x:            x scaling factor
            scale_y:            y scaling factor
            scale_z:            z scaling factor
            all_drawing_types:  description
            drawing_types:      description
        """

        self.__view_model_ele_list[name] = (PythonPartViewData(visible_in_2d, visible_in_3d,
                                                                start_scale, end_scale,
                                                                ref_pnt1_x, ref_pnt1_y, ref_pnt1_z,
                                                                ref_pnt2_x, ref_pnt2_y, ref_pnt2_z,
                                                                visibility_layer_a, visibility_layer_b, visibility_layer_c,
                                                                scale_x, scale_y, scale_z,
                                                                all_drawing_types, drawing_types),
                                            ModelEleList(trans_stack = self.__trans_stack))


    def get_default_3d_view_model_ele_list(self) -> ModelEleList:
        """ get the model element list of the 3D default view

        Returns:
            model element list of the 3D default view
        """

        return self.get_view_model_ele_list("0_3D")


    def get_view_model_ele_list(self,
                                name: str) -> ModelEleList:
        """ get the model element list for the view defined by name

        Args:
            name: name of the view

        Returns:
            get the model element list for the current view
        """

        model_ele_list = self.__view_model_ele_list[name][1]

        if self.__model_ele_list is not None:
            model_ele_list.set_common_properties(self.__model_ele_list.get_common_properties())
            model_ele_list.set_texture(self.__model_ele_list.get_texture())
            model_ele_list.set_texture_mapping(self.__model_ele_list.get_texture_mapping())

        self.__model_ele_list = model_ele_list

        return self.__model_ele_list


    def create_pythonpart(self,
                          build_ele             : BuildingElement,
                          build_ele_attr_list   : BuildingElementAttributeList,
                          local_placement_matrix: AllplanGeo.Matrix3D = AllplanGeo.Matrix3D()) -> ModelEleList:
        """ create the PythonPart

        Args:
            build_ele:              building element with the parameter properties
            build_ele_attr_list:    building element attribute list
            local_placement_matrix: local placement matrix for the PythonPart

        Returns:
            PythonPart elements
        """

        pyp_util = PythonPartUtil()
        pyp_util.add_attribute_list(build_ele_attr_list)

        for view_data, elements in self.__view_model_ele_list.values():
            if not elements:
                continue

            if view_data.visible_in_2d and view_data.visible_in_3d:
                pyp_util.add_pythonpart_view_2d3d(elements, view_data)

            elif view_data.visible_in_2d and not view_data.visible_in_3d:
                pyp_util.add_pythonpart_view_2d(elements, view_data)

            else:
                pyp_util.add_pythonpart_view_3d(elements, view_data)

        return pyp_util.create_pythonpart(build_ele,
                                          local_placement_matrix = local_placement_matrix,)

```

</details>