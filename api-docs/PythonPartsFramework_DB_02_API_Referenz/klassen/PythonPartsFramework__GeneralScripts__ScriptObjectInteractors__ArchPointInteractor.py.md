---
title: "ArchPointInteractor"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\ArchPointInteractor.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# ArchPointInteractor

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\ArchPointInteractor.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

Implementation of the interactor for the architecture point input

## Abhängigkeiten

- `BaseFilterObject`
- `BaseScriptObjectInteractor`
- `NemAll_Python_ArchElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `collections.abc`
- `dataclasses`
- `typing`

## Klassen

### `ArchPointInteractorResult`

Implementation of the result of a point input on an architectural element
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ArchPointInteractor`

Implementation of the interactor for point input on an architectural element

Only vertical architectural elements (i.e. walls, beams, columns, foundation) are valid
for this interactor. The input result can be used e.g. for creation of openings in these elements.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, interactor_result: ArchPointInteractorResult, ele_filter: list[AllplanEleAdapter.GUID] | BaseFilterObject | AllplanIFW.SelectionQuery | None=None, request_text: str='Select the element', preview_function: Callable[[], None] | None=None` | `None` | initialize  Args:     interactor_result: result of the interactor     ele_filter:        element filter as a list of accepted element type GUIDs or a callable or a selection query                        returning True, when the element is valid for selection     request_text:      request text     preview_function:  preview function |
| `start_input` | `self, coord_input: AllplanIFW.CoordinateInput` | `None` | start the input  Args:     coord_input: API object for the coordinate input, element selection, ... in the Allplan view |
| `on_preview_draw` | `self` | `None` | Handles the preview draw event          |
| `on_mouse_leave` | `self` | `None` | Handles the mouse leave event          |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool` | Handles the process mouse message event  Args:     mouse_msg: mouse message ID     pnt:       input point in Allplan view coordinates     msg_info:  additional mouse message info  Returns:     True/False for success. |
| `get_outline_segment_and_point` | `self, sel_ele: AllplanEleAdapter.BaseElementAdapter, input_pnt: AllplanGeo.Point3D` | `None` | get the outline segment and point related to the input point (maybe an inner tier segment was selected)  Args:     sel_ele:   selected element     input_pnt: input point |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the interactor for the architecture point input
"""

from collections.abc import Callable
from dataclasses import dataclass
from typing import cast

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from .BaseScriptObjectInteractor import BaseScriptObjectInteractor
from .BaseFilterObject import BaseFilterObject

@dataclass
class ArchPointInteractorResult:
    """ Implementation of the result of a point input on an architectural element
    """

    sel_model_ele    : AllplanEleAdapter.BaseElementAdapter           = AllplanEleAdapter.BaseElementAdapter()
    """Selected model element"""

    sel_model_ele_geo: (AllplanGeo.Polygon2D | AllplanGeo.Polyline2D) = AllplanGeo.Polygon2D()
    """Geometry of the selected model element"""

    sel_geo_ele      : (AllplanGeo.Line2D  | None)                    = None
    """Selected geometry element"""

    input_point      : AllplanGeo.Point3D                             = AllplanGeo.Point3D()
    """input point"""


class ArchPointInteractor(BaseScriptObjectInteractor):
    """ Implementation of the interactor for point input on an architectural element

    Only vertical architectural elements (i.e. walls, beams, columns, foundation) are valid
    for this interactor. The input result can be used e.g. for creation of openings in these elements.
    """

    def __init__(self,
                 interactor_result: ArchPointInteractorResult,
                 ele_filter       : (list[AllplanEleAdapter.GUID] | BaseFilterObject | AllplanIFW.SelectionQuery | None)  = None,
                 request_text     : str = "Select the element",
                 preview_function : (Callable[[], None] | None) = None):
        """ initialize

        Args:
            interactor_result: result of the interactor
            ele_filter:        element filter as a list of accepted element type GUIDs or a callable or a selection query
                               returning True, when the element is valid for selection
            request_text:      request text
            preview_function:  preview function
        """

        self.interactor_result  = interactor_result
        self.__request_text     = request_text
        self.__preview_function = preview_function

        self.__coord_input = None


        #----------------- set up selection filter

        if (sel_query := self.create_selection_query(ele_filter)) is not None:
            self.__selection_filter = AllplanIFW.ElementSelectFilterSetting(sel_query)
        else:
            assert False, "Filter is missing"


    def start_input(self,
                    coord_input: AllplanIFW.CoordinateInput):
        """ start the input

        Args:
            coord_input: API object for the coordinate input, element selection, ... in the Allplan view
        """

        self.__coord_input = coord_input

        self.__coord_input.InitFirstPointInput(AllplanIFW.InputStringConvert(self.__request_text),
                                               AllplanIFW.CoordinateInputMode(AllplanIFW.eIdentificationMode.eIDENT_ARCHPOINT))

        self.__coord_input.SetElementFilter(self.__selection_filter)


    def on_preview_draw(self):
        """ Handles the preview draw event
        """

        if self.__coord_input is None:
            return

        self.interactor_result.input_point = self.__coord_input.GetCurrentPoint().GetPoint()

        if self.__preview_function:
            self.__preview_function()


    def on_mouse_leave(self):
        """ Handles the mouse leave event
        """

        self.on_preview_draw()


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

        input_pnt = self.__coord_input.GetInputPoint(mouse_msg, pnt, msg_info).GetPoint()


        #----------------- set the selected element and point

        sel_ele = self.__coord_input.GetSelectedElement()

        self.interactor_result.input_point = input_pnt

        if sel_ele.IsNull() or self.__coord_input.GetSelectedGeometryElement() is None:
            self.interactor_result.sel_geo_ele   = None
            self.interactor_result.sel_model_ele = AllplanEleAdapter.BaseElementAdapter()

            if self.__preview_function:
                self.__preview_function()

            return True


        #------------- set the general element and the geometry element

        if sel_ele.GetElementAdapterType().IsTypeGroup(AllplanEleAdapter.ElementAdapterTypeGroup.eAXIS_ELEMENT_GROUP) and \
           sel_ele.GetElementAdapterType().GetGuid() not in {AllplanEleAdapter.Beam_TypeUUID, AllplanEleAdapter.StripFoundation_TypeUUID}:
            self.get_outline_segment_and_point(sel_ele, input_pnt)

        else:
            self.interactor_result.sel_model_ele     = sel_ele
            self.interactor_result.sel_model_ele_geo = sel_ele.GetGroundViewArchitectureElementGeometry()
            self.interactor_result.sel_geo_ele       = cast(AllplanGeo.Line2D, self.__coord_input.GetSelectedGeometryElement())


        #----------------- draw the preview

        if self.__preview_function:
            self.__preview_function()

        return self.__coord_input.IsMouseMove(mouse_msg)


    def get_outline_segment_and_point(self,
                                      sel_ele  : AllplanEleAdapter.BaseElementAdapter,
                                      input_pnt: AllplanGeo.Point3D):
        """ get the outline segment and point related to the input point (maybe an inner tier segment was selected)

        Args:
            sel_ele:   selected element
            input_pnt: input point
        """

        if not self.__coord_input:
            return

        segment, pnt, ele = AllplanArchEle.ArchitectureElementsGeometryService.GetOutlineSegmentAndPoint(sel_ele, input_pnt.To2D)

        self.interactor_result.sel_model_ele     = AllplanEleAdapter.BaseElementAdapterParentElementService.GetParentElement(sel_ele)
        self.interactor_result.sel_model_ele_geo = ele.GetGeometry()
        self.interactor_result.sel_geo_ele       = segment
        self.interactor_result.input_point       = pnt.To3D

```

</details>