---
title: "FaceSelectInteractor"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\FaceSelectInteractor.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# FaceSelectInteractor

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\FaceSelectInteractor.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

Module containing interactor and result data class implementation for an interaction,
where the user selects a face on a polyhedron element

## Abhängigkeiten

- `BaseFilterObject`
- `BaseScriptObjectInteractor`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `collections.abc`
- `dataclasses`
- `re`
- `typing`

## Klassen

### `FaceSelectResult`

implementation of the single element selection result
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `FaceSelectInteractor`

implementation of the interactor handling the face selection on a polyhedron element

This interactor handles the interaction, where the user selects a face of any
model element. The element geometry must be a polyhedron with closed faces. It is
possible to allow the user to select faces inside a UVS.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, interactor_result: FaceSelectResult, ele_filter: list[AllplanEleAdapter.GUID] | BaseFilterObject | AllplanIFW.SelectionQuery | None=None, prompt_msg: str='Select the face', allow_uvs: bool=False, preview_function: Callable[[], None] | None=None` | `None` | initialize  Args:     interactor_result: data class for saving the result of the interaction     ele_filter:        element filter as a list of accepted element type GUIDs or a callable or a selection query                        returning True, when the element is valid for selection     prompt_msg:        prompt message shown to the user in the dialog line     allow_uvs:         whether to allow the selection inside a UVS     preview_function:  function for drawing a preview, called with each mouse move event during the selection |
| `is_face_polyhedron` | `ele: AllplanEleAdapter.BaseElementAdapter` | `bool` | Checks, if the base element adapter has a polyhedron geometry with faces  Args:     ele: element adapter  Returns:     True, if the given element adapter has a polyhedron type geometry with faces |
| `start_input` | `self, coord_input: AllplanIFW.CoordinateInput` | `None` | start the input  Args:     coord_input: API object for the coordinate input, element selection, ... in the Allplan view |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool` | Handles the process mouse message event  Args:     mouse_msg: mouse message ID     pnt:       input point in Allplan view coordinates     msg_info:  additional mouse message info  Returns:     True/False for success. |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Module containing interactor and result data class implementation for an interaction,
where the user selects a face on a polyhedron element
"""

import re
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from .BaseFilterObject import BaseFilterObject
from .BaseScriptObjectInteractor import BaseScriptObjectInteractor


@dataclass
class FaceSelectResult:
    """ implementation of the single element selection result
    """

    sel_element : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()
    """Selected element"""

    sel_geo_ele : Any                                       = None
    """Geometry of the selected element"""

    input_point : AllplanGeo.Point3D                        = AllplanGeo.Point3D()
    """Input point on the face"""

    face_polygon: AllplanGeo.Polygon3D                      = AllplanGeo.Polygon3D()
    """Outline polygon of the selected face"""

    face_plane  : AllplanGeo.Plane3D                        = AllplanGeo.Plane3D()
    """Plane of the selected face"""

    assoc_view  : AllplanEleAdapter.AssocViewElementAdapter = AllplanEleAdapter.AssocViewElementAdapter()
    """The UVS, in which the element was selected"""



class FaceSelectInteractor(BaseScriptObjectInteractor):
    """ implementation of the interactor handling the face selection on a polyhedron element

    This interactor handles the interaction, where the user selects a face of any
    model element. The element geometry must be a polyhedron with closed faces. It is
    possible to allow the user to select faces inside a UVS.
    """

    def __init__(self,
                 interactor_result: FaceSelectResult,
                 ele_filter       : (list[AllplanEleAdapter.GUID] | BaseFilterObject | AllplanIFW.SelectionQuery | None)  = None,
                 prompt_msg       : str = "Select the face",
                 allow_uvs        : bool = False,
                 preview_function : Callable[[], None] | None = None):
        """ initialize

        Args:
            interactor_result: data class for saving the result of the interaction
            ele_filter:        element filter as a list of accepted element type GUIDs or a callable or a selection query
                               returning True, when the element is valid for selection
            prompt_msg:        prompt message shown to the user in the dialog line
            allow_uvs:         whether to allow the selection inside a UVS
            preview_function:  function for drawing a preview, called with each mouse move event during the selection
        """

        self.interactor_result  = interactor_result
        self.__coord_input      = None
        self.__prompt_msg       = prompt_msg
        self.__allow_uvs        = allow_uvs
        self.__selection_filter = None
        self.__preview_func     = preview_function


        #----------------- set up selection filter

        if (sel_query := self.create_selection_query(ele_filter)) is not None:
            element_filter = lambda ele: self.is_face_polyhedron(ele) and sel_query(ele)
        else:
            element_filter = self.is_face_polyhedron

        self.__selection_filter = AllplanIFW.ElementSelectFilterSetting(AllplanIFW.SelectionQuery(element_filter))

    @staticmethod
    def is_face_polyhedron(ele: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """Checks, if the base element adapter has a polyhedron geometry with faces

        Args:
            ele: element adapter

        Returns:
            True, if the given element adapter has a polyhedron type geometry with faces
        """
        if not isinstance(geo := ele.GetGeometry(), AllplanGeo.Polyhedron3D):
            return False

        return geo.GetType() in (AllplanGeo.PolyhedronType.tVolume, AllplanGeo.PolyhedronType.tFaces)

    def start_input(self,
                    coord_input: AllplanIFW.CoordinateInput):
        """ start the input

        Args:
            coord_input: API object for the coordinate input, element selection, ... in the Allplan view
        """

        self.__coord_input = coord_input

        self.__coord_input.InitFirstElementInput(AllplanIFW.InputStringConvert(self.__prompt_msg))


    def process_mouse_msg(self,
                          mouse_msg: int,
                          pnt      : AllplanGeo.Point2D,
                          msg_info : AllplanIFW.AddMsgInfo) -> bool:
        """ Handles the process mouse message event

        Args:
            mouse_msg: mouse message ID
            pnt:       input point in Allplan view coordinates
            msg_info:  additional mouse message info

        Returns:
            True/False for success.
        """

        if not self.__coord_input:
            return True

        if self.__selection_filter is None:
            self.__coord_input.SelectElement(mouse_msg, pnt, msg_info, True, False, False)
        else:
            self.__coord_input.SelectElement(mouse_msg, pnt, msg_info, True, False, False, self.__selection_filter)

        sel_ele = self.__coord_input.GetSelectedElement()

        if sel_ele.IsNull():
            return True

        is_selected, face_polygon, intersect_result = \
            AllplanBaseEle.FaceSelectService.SelectPolyhedronFace(
                sel_ele, pnt, True,
                self.__coord_input.GetViewWorldProjection(),
                self.__coord_input.GetInputViewDocument(),
                self.__allow_uvs)

        if not is_selected:
            return True

        # save the result
        self.interactor_result.sel_element  = sel_ele
        self.interactor_result.sel_geo_ele  = sel_ele.GetGeometry()
        self.interactor_result.input_point  = intersect_result.IntersectionPoint
        self.interactor_result.face_polygon = face_polygon
        self.interactor_result.assoc_view   = self.__coord_input.GetSelectedElementAssocView()

        self.interactor_result.face_plane.SetPoint(intersect_result.IntersectionPoint)
        self.interactor_result.face_plane.SetVector(intersect_result.FaceNv)

        if self.__preview_func is not None:
            self.__preview_func()

        return self.__coord_input.IsMouseMove(mouse_msg)

```

</details>