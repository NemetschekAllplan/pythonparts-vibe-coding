---
title: "DockingPointInteractor"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\DockingPointInteractor.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# DockingPointInteractor

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\DockingPointInteractor.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

implementation of the interactor for the point takeover

## Abhängigkeiten

- `BaseScriptObjectInteractor`
- `BuildingElement`
- `BuildingElementControlProperties`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `ParameterProperty`
- `ValueTypes.Data.PointConnection`
- `collections.abc`

## Klassen

### `DockingPointInteractor`

implementation of the interactor for the point takeover
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, parameter: ParameterProperty, preview_function: Callable[[], None] | None=None` | `None` | initialize  Args:     parameter:        parameter for the docking point     preview_function: preview function |
| `start_input` | `self, coord_input: AllplanIFW.CoordinateInput` | `None` | start the input  Args:     coord_input: API object for the coordinate input, element selection, ... in the Allplan view |
| `process_mouse_msg` | `self, mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo` | `bool` | Handles the process mouse message event  Args:     mouse_msg: mouse message ID     pnt:       input point in Allplan view coordinates     msg_info:  additional mouse message info  Returns:     True/False for success. |
| `assign_selected_value` | `self` | `None` | assign the selected value to the take over parameter          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the interactor for the point takeover
"""

from collections.abc import Callable

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from ParameterProperty import ParameterProperty

from ValueTypes.Data.PointConnection import PointConnection

from .BaseScriptObjectInteractor import BaseScriptObjectInteractor

class DockingPointInteractor(BaseScriptObjectInteractor):
    """ implementation of the interactor for the point takeover
    """

    def __init__(self,
                 parameter       : ParameterProperty,
                 preview_function: (Callable[[], None] | None) = None):
        """ initialize

        Args:
            parameter:        parameter for the docking point
            preview_function: preview function
        """

        self.parameter        = parameter
        self.preview_function = preview_function

        self.__coord_input        = None
        self.build_ele            = BuildingElement()
        self.build_ele_ctrl_props = BuildingElementControlProperties()
        self.input_pnt            = AllplanGeo.Point3D()
        self.docking_point        = AllplanIFW.DockingPoint()


    def start_input(self,
                    coord_input: AllplanIFW.CoordinateInput):
        """ start the input

        Args:
            coord_input: API object for the coordinate input, element selection, ... in the Allplan view
        """

        self.__coord_input = coord_input


        #----------------- start the input

        self.__coord_input.InitFirstElementInput(AllplanIFW.InputStringConvert("Select the element and point"),
                                                 AllplanIFW.CoordinateInputMode(AllplanIFW.eIdentificationMode.eIDENT_DOCKINGPOINT))


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


        #----------------- select the connection element and point

        self.docking_point = self.__coord_input.GetInputDockingPoint(mouse_msg, pnt, msg_info)

        self.parameter.value = PointConnection(self.docking_point)

        if self.preview_function:
            self.preview_function()

        return not self.docking_point.IsValid() or self.__coord_input.IsMouseMove(mouse_msg)


    def assign_selected_value(self):
        """ assign the selected value to the take over parameter
        """

        if self.docking_point.IsValid():
            self.parameter.value = PointConnection(self.docking_point)

```

</details>