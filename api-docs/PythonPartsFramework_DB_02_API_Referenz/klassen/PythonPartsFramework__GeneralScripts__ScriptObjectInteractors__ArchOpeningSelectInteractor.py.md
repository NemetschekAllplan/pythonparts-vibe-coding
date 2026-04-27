---
title: "ArchOpeningSelectInteractor"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\ArchOpeningSelectInteractor.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# ArchOpeningSelectInteractor

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\ArchOpeningSelectInteractor.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

implementation of the interactor for the wall opening selection

## Abhängigkeiten

- `BaseScriptObjectInteractor`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `OnCancelFunctionResult`
- `StartFunctionResult`
- `Utils.Architecture.OpeningGeometryUtil`
- `Utils.ElementFilter.ArchitectureElementsQueryUtil`
- `collections.abc`
- `dataclasses`
- `enum`

## Klassen

### `ArchOpeningSelectType`

Enum for wall opening selection type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ArchOpeningSelectResult`

implementation of the wall opening selection result
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ArchOpeningSelectInteractor`

implementation of the interactor for the wall opening selection
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, interactor_result: ArchOpeningSelectResult, opening_sel_type: ArchOpeningSelectType=ArchOpeningSelectType.DOOR_WINDOW_OPENING, preview_function: Callable[[], None] | None=None` | `None` | initialize  Args:     interactor_result: result of the interactor     opening_sel_type:  opening selection type     preview_function:  preview function |
| `start_input` | `self, coord_input: AllplanIFW.CoordinateInput` | `StartFunctionResult` | start the input  Args:     coord_input: API object for the coordinate input, element selection, ... in the Allplan view  Returns:     start function result |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool` | Handles the process mouse message event  Args:     mouse_msg: mouse message ID     pnt:       input point in Allplan view coordinates     msg_info:  additional mouse message info  Returns:     True/False for success. |
| `get_opening_data` | `self, sel_ele: AllplanEleAdapter.BaseElementAdapter, input_pnt: AllplanGeo.Point3D` | `None` | Get the opening data from the selected element  Args:     sel_ele:   selected element     input_pnt: input point |
| `on_cancel_function` | `self` | `OnCancelFunctionResult` | Handles the cancel function event (e.g. by ESC, ...)  Returns:     cancel function result |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the interactor for the wall opening selection
"""

from dataclasses import dataclass

from collections.abc import Callable
from enum import IntEnum

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from Utils.Architecture.OpeningGeometryUtil import OpeningGeometryUtil, OpeningGeometry
from Utils.ElementFilter.ArchitectureElementsQueryUtil import ArchitectureElementsQueryUtil

from .BaseScriptObjectInteractor import BaseScriptObjectInteractor
from .OnCancelFunctionResult import OnCancelFunctionResult
from .StartFunctionResult import StartFunctionResult

class ArchOpeningSelectType(IntEnum):
    """Enum for wall opening selection type
    """

    DOOR_WINDOW_OPENING = 0
    DOOR_OPENING        = 1
    WINDOW_OPENING      = 2
    SLAB_OPENING        = 3


@dataclass
class ArchOpeningSelectResult:
    """ implementation of the wall opening selection result
    """

    sel_element : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()
    """Selected element"""

    opening_geometry = OpeningGeometry()


class ArchOpeningSelectInteractor(BaseScriptObjectInteractor):
    """ implementation of the interactor for the wall opening selection
    """

    def __init__(self,
                 interactor_result: ArchOpeningSelectResult,
                 opening_sel_type : ArchOpeningSelectType    = ArchOpeningSelectType.DOOR_WINDOW_OPENING,
                 preview_function : (Callable[[], None] | None) = None):
        """ initialize

        Args:
            interactor_result: result of the interactor
            opening_sel_type:  opening selection type
            preview_function:  preview function
        """

        self.__result           = interactor_result
        self.__preview_function = preview_function

        self.__coord_input   = None
        self.__prompt_msg    = "Select the opening"
        self.__sel_query     = AllplanIFW.SelectionQuery()
        self.__pre_selection = False


        #----------------- set up selection filter

        match opening_sel_type:
            case ArchOpeningSelectType.DOOR_WINDOW_OPENING:
                self.__sel_query = ArchitectureElementsQueryUtil.create_vertical_arch_opening_query()

            case ArchOpeningSelectType.DOOR_OPENING:
                self.__sel_query = AllplanIFW.SelectionQuery(AllplanIFW.QueryTypeID(AllplanEleAdapter.DoorTier_TypeUUID))

            case ArchOpeningSelectType.WINDOW_OPENING:
                self.__sel_query = AllplanIFW.SelectionQuery(AllplanIFW.QueryTypeID(AllplanEleAdapter.WindowTier_TypeUUID))

            case ArchOpeningSelectType.SLAB_OPENING:
                self.__sel_query = AllplanIFW.SelectionQuery(AllplanIFW.QueryTypeID(AllplanEleAdapter.SlabOpening_TypeUUID))

        self.__selection_filter = AllplanIFW.ElementSelectFilterSetting(self.__sel_query)


    def start_input(self,
                    coord_input: AllplanIFW.CoordinateInput) -> StartFunctionResult:
        """ start the input

        Args:
            coord_input: API object for the coordinate input, element selection, ... in the Allplan view

        Returns:
            start function result
        """

        pre_sel_ele = AllplanIFW.SelectElementsService.GetPreSelectedElements(coord_input.GetInputViewDocument(),
                                                                              self.__sel_query)

        if len(pre_sel_ele):
            self.__result.sel_element = pre_sel_ele[0]
            self.__pre_selection      = True

            return StartFunctionResult.PRE_SELECTED_ELEMENTS

        self.__coord_input = coord_input

        self.__coord_input.InitFirstElementInput(AllplanIFW.InputStringConvert(self.__prompt_msg))

        return StartFunctionResult.CONTINUE_INPUT


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

        if not self.__coord_input or self.__pre_selection:
            return True

        if self.__selection_filter is None:
            self.__coord_input.SelectElement(mouse_msg, pnt, msg_info, True, True, False)
        else:
            self.__coord_input.SelectElement(mouse_msg, pnt, msg_info, True, True, False, self.__selection_filter)

        sel_ele = self.__coord_input.GetSelectedElement()

        input_pnt = self.__coord_input.GetInputPoint(mouse_msg, pnt, msg_info).GetPoint()

        self.get_opening_data(sel_ele, input_pnt)

        if self.__preview_function is not None:
            self.__preview_function()

        return self.__coord_input.IsMouseMove(mouse_msg)


    def get_opening_data(self,
                         sel_ele  : AllplanEleAdapter.BaseElementAdapter,
                         input_pnt: AllplanGeo.Point3D):
        """ Get the opening data from the selected element

        Args:
            sel_ele:   selected element
            input_pnt: input point
        """

        if self.__coord_input is None:
            return

        self.__result.sel_element = sel_ele


        #----------------- free placement

        if sel_ele.IsNull():
            self.__result.sel_element      = sel_ele
            self.__result.opening_geometry = OpeningGeometry()

            self.__result.opening_geometry.placement_point = input_pnt

            return

        self.__result.opening_geometry = OpeningGeometryUtil.get_arch_opening_geometry_by_sel_point(sel_ele, input_pnt.To2D)


    def on_cancel_function(self) -> OnCancelFunctionResult:             # pylint: disable=no-self-use
        """ Handles the cancel function event (e.g. by ESC, ...)

        Returns:
            cancel function result
        """

        return OnCancelFunctionResult.CANCEL_INPUT

```

</details>