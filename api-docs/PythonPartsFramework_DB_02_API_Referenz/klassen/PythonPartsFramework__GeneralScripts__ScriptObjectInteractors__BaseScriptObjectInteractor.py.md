---
title: "BaseScriptObjectInteractor"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\BaseScriptObjectInteractor.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# BaseScriptObjectInteractor

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\BaseScriptObjectInteractor.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

implementation of the base script object interactor

## Abhängigkeiten

- `BaseFilterObject`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `ScriptObjectInteractors.OnCancelFunctionResult`
- `StartFunctionResult`
- `__future__`
- `abc`

## Klassen

### `BaseScriptObjectInteractor`

implementation of the base script object interactor
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `start_input` | `self, coord_input: AllplanIFW.CoordinateInput` | `StartFunctionResult` | start the input  Args:     coord_input: API object for the coordinate input, element selection, ... in the Allplan view  Returns:     start function result |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool` | Handles the process mouse message event  Args:     mouse_msg: mouse message ID     pnt:       input point in Allplan view coordinates     msg_info:  additional mouse message info  Returns:     True/False for success. |
| `on_preview_draw` | `self` | `None` | Handles the preview draw event          |
| `on_mouse_leave` | `self` | `None` | Handles the mouse leave event          |
| `on_cancel_function` | `self` | `OnCancelFunctionResult` | Handles the cancel function event (e.g. by ESC, ...)  Returns:     cancel function result |
| `create_selection_query` | `ele_filter: list[AllplanEleAdapter.GUID] | BaseFilterObject | AllplanIFW.SelectionQuery | None` | `AllplanIFW.SelectionQuery` | create the selection query  Args:     ele_filter: element filter as a list of accepted element type GUIDs or a callable or a selection query  Returns:     selection query or None |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base script object interactor
"""

# pylint: disable=no-self-use

from __future__ import annotations

import abc

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from ScriptObjectInteractors.OnCancelFunctionResult import OnCancelFunctionResult

from .BaseFilterObject import BaseFilterObject
from .StartFunctionResult import StartFunctionResult

class BaseScriptObjectInteractor(abc.ABC):
    """ implementation of the base script object interactor
    """

    @abc.abstractmethod
    def start_input(self,
                    coord_input: AllplanIFW.CoordinateInput) -> StartFunctionResult:
        """ start the input

        Args:
            coord_input: API object for the coordinate input, element selection, ... in the Allplan view

        Returns:
            start function result
        """

        return StartFunctionResult.NOT_IMPLEMENTED


    @abc.abstractmethod
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

    def on_preview_draw(self):
        """ Handles the preview draw event
        """

    def on_mouse_leave(self):
        """ Handles the mouse leave event
        """

    def on_cancel_function(self) -> OnCancelFunctionResult:
        """ Handles the cancel function event (e.g. by ESC, ...)

        Returns:
            cancel function result
        """

        return OnCancelFunctionResult.NOT_IMPLEMENTED


    @staticmethod
    def create_selection_query(ele_filter: (list[AllplanEleAdapter.GUID] | \
                               BaseFilterObject | AllplanIFW.SelectionQuery | None)) -> AllplanIFW.SelectionQuery:
        """ create the selection query

        Args:
            ele_filter: element filter as a list of accepted element type GUIDs or a callable or a selection query

        Returns:
            selection query or None
        """

        if isinstance(ele_filter, list):
            type_queries = [AllplanIFW.QueryTypeID(ele_guid) for ele_guid in ele_filter]

            return AllplanIFW.SelectionQuery(type_queries)

        if callable(ele_filter):
            return AllplanIFW.SelectionQuery(ele_filter)

        return ele_filter

```

</details>