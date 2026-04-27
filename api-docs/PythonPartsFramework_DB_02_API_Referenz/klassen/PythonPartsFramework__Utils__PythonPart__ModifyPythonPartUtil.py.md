---
title: "ModifyPythonPartUtil"
source: "PythonPartsFramework\Utils\PythonPart\ModifyPythonPartUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ModifyPythonPartUtil

> **Pfad:** `PythonPartsFramework\Utils\PythonPart\ModifyPythonPartUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the utility class for the PythonPart modification

## Abhängigkeiten

- `BaseInteractor`
- `BuildingElementInput`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `ScriptObjectInteractors.BaseScriptObjectInteractor`
- `TypeCollections.ModificationElementList`
- `Utils.HideElementsService`
- `typing`

## Klassen

### `ModifyPythonPartUtil`

implementation of the utility class for the PythonPart modification
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, python_part: AllplanEleAdapter.BaseElementAdapter` | `None` | initialize  Args:     python_part: PythonPart to modify |
| `start_input` | `self, coord_input: AllplanIFWInput.CoordinateInput` | `None` | start the modification  Args:     coord_input: API object for the coordinate input, element selection, ... in the Allplan view |
| `on_control_event` | `self, event_id: int` | `None` | Handles the on control event.  Called when an event is triggered by a palette control (ex. button).  Args:     event_id: event id of the clicked button control |
| `on_cancel_function` | `self` | `bool` | Handles the cancel function event  This event is triggered when the ESC button is hit during the runtime of the PythonPart.  Returns:     True when the PythonPart framework should terminate the PythonPart, False otherwise. |
| `on_preview_draw` | `self` | `None` | Handles the preview draw event.  This event is triggered, when an input in the dialog line is done (e.g. input of a coordinate). |
| `on_mouse_leave` | `self` | `None` | Handles the mouse leave event.  This event is triggered, when the mouse leaves the viewport. |
| `on_value_input_control_enter` | `self` | `bool` | Handles the value input control enter event.  This event is triggered, when enter key is hit during the input inside the input control located in the dialog line.  Returns:     True/False for success. |
| `modify_element_property` | `self, page: int, name: str, value: Any` | `None` | Handles the modify element property event.  This event is triggered with each modification of the element property done in the property palette or by using a handle.  Args:     page:   Page of the modified property     name:   Name of the modified property.     value:  New value of the modified property. |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: Any` | `bool` | Handles the process mouse message event.  This event is triggered with each message sent by the mouse, which can be a mouse move, mouse click, zoom out, etc. The message is sent only during mouse actions inside a viewport.  Args:     mouse_msg:  The mouse message.     pnt:        The input point in view coordinates. The origin is the mid point of the viewport     msg_info:   additional message info.  Returns:     True/False for success. |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the utility class for the PythonPart modification
"""

from typing import Any

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFWInput

from BaseInteractor import BaseInteractor
from BuildingElementInput import BuildingElementInput

from ScriptObjectInteractors.BaseScriptObjectInteractor import BaseScriptObjectInteractor

from TypeCollections.ModificationElementList import ModificationElementList

from Utils.HideElementsService import HideElementsService

class ModifyPythonPartUtil(BaseScriptObjectInteractor, BaseInteractor):
    """ implementation of the utility class for the PythonPart modification
    """

    def __init__(self,
                 python_part: AllplanEleAdapter.BaseElementAdapter):
        """ initialize

        Args:
            python_part: PythonPart to modify
        """

        self.python_part = python_part

        self.build_ele_input : BuildingElementInput

        self.hide_elements = HideElementsService()
        self.hide_elements.hide_element_and_linked(python_part)


    def start_input(self,
                    coord_input: AllplanIFWInput.CoordinateInput):
        """ start the modification

        Args:
            coord_input: API object for the coordinate input, element selection, ... in the Allplan view
        """

        py_path = fr"{AllplanSettings.AllplanPaths.GetPythonPartsEtcPath()}PythonPartsFramework\GeneralScripts"

        self.build_ele_input = BuildingElementInput(coord_input, py_path)


        #----------------- start the modification

        _, pyp_path, parameter = AllplanBaseEle.PythonPartService.GetParameter(self.python_part)

        _, placement_matrix = AllplanBaseEle.PythonPartService.GetPlacementMatrix(self.python_part)

        self.build_ele_input.start_input(pyp_path, parameter, None, ModificationElementList([self.python_part]),
                                         placement_matrix, AllplanGeo.Matrix3D(), AllplanEleAdapter.BaseElementAdapter(),
                                         AllplanSettings.ExecutionEvent.eProperties)


    def on_control_event(self,
                         event_id: int):
        """ Handles the on control event.

        Called when an event is triggered by a palette control (ex. button).

        Args:
            event_id: event id of the clicked button control
        """

        self.build_ele_input.on_control_event(event_id)


    def on_cancel_function(self) -> bool:
        """ Handles the cancel function event

        This event is triggered when the ESC button is hit during the runtime of the PythonPart.

        Returns:
            True when the PythonPart framework should terminate the PythonPart, False otherwise.
        """

        self.hide_elements.show_elements()

        if (ret := self.build_ele_input.on_cancel_function()):
            self.build_ele_input.close_palette()

        return ret


    def on_preview_draw(self):
        """ Handles the preview draw event.

        This event is triggered, when an input in the dialog line is done (e.g. input of a coordinate).
        """

        self.build_ele_input.on_preview_draw()


    def on_mouse_leave(self):
        """ Handles the mouse leave event.

        This event is triggered, when the mouse leaves the viewport.
        """

        self.build_ele_input.on_mouse_leave()


    def on_value_input_control_enter(self) -> bool:
        """ Handles the value input control enter event.

        This event is triggered, when enter key is hit during the input inside the input control
        located in the dialog line.

        Returns:
            True/False for success.
        """

        return self.build_ele_input.on_value_input_control_enter()


    def modify_element_property(self,
                                page : int,
                                name : str,
                                value: Any):
        """ Handles the modify element property event.

        This event is triggered with each modification of the element property done in the property
        palette or by using a handle.

        Args:
            page:   Page of the modified property
            name:   Name of the modified property.
            value:  New value of the modified property.
        """

        self.build_ele_input.modify_element_property(page, name, value)


    def process_mouse_msg(self,
                          mouse_msg: int,
                          pnt      : AllplanGeo.Point2D,
                          msg_info : Any) -> bool:
        """ Handles the process mouse message event.

        This event is triggered with each message sent by the mouse, which can be a mouse move,
        mouse click, zoom out, etc. The message is sent only during mouse actions inside a viewport.

        Args:
            mouse_msg:  The mouse message.
            pnt:        The input point in view coordinates. The origin is the mid point of the viewport
            msg_info:   additional message info.

        Returns:
            True/False for success.
        """

        return self.build_ele_input.process_mouse_msg(mouse_msg, pnt, msg_info)

```

</details>