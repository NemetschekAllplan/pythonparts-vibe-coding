---
title: "GeometryExpandService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\GeometryExpandService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - script
related:
  -
last_updated: "2026-02-20"
---


# GeometryExpandService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\GeometryExpandService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`

## Übersicht

implementation of the geometry expand service

## Abhängigkeiten

- `InputData`
- `InputMode`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`
- `ScriptService`
- `__future__`
- `traceback`
- `typing`

## Klassen

### `GeometryExpandService`

implementation of the geometry expand service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `init` | `input_data: InputData, msg_info: AllplanIFW.AddMsgInfo` | `None` | initialize the geometry expand  Args:     input_data: input data     msg_info:   additional mouse message info |
| `process_mouse_msg` | `mouse_msg: int, pnt: AllplanGeo.Point2D, msg_info: AllplanIFW.AddMsgInfo, input_data: InputData, script_service: ScriptService` | `tuple[bool, bool]` | process the mouse message  Args:     mouse_msg:      mouse message ID     pnt:            input point in Allplan view coordinates     msg_info:       additional mouse message info     input_data:     input data     script_service: script service  Returns:     has expand function state, executed state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the geometry expand service
"""

# pylint: disable=global-statement

from __future__ import annotations

from typing import TYPE_CHECKING

import traceback

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_Utility as AllplanUtil

from InputMode import InputMode


if TYPE_CHECKING:
    from .InputData import InputData
    from .ScriptService import ScriptService

ASK_3D_KEY = "DO_NOT_ASK_3D_REINFORCEMENT"
USE_3D_KEY = "USE_3D_REINFORCEMENT"

if ASK_3D_KEY not in globals():
    globals()[ASK_3D_KEY] = False
    globals()[USE_3D_KEY] = False

DO_NOT_ASK_3D_REINFORCEMENT = globals()[ASK_3D_KEY]
USE_3D_REINFORCEMENT        = globals()[USE_3D_KEY]

class GeometryExpandService():
    """ implementation of the geometry expand service
    """

    @staticmethod
    def init(input_data: InputData,
             msg_info  : AllplanIFW.AddMsgInfo):
        """ initialize the geometry expand

        Args:
            input_data: input data
            msg_info:   additional mouse message info
        """

        if input_data.last_input_doc is not None:
            AllplanBaseEle.GetViewMatrices(input_data.last_input_doc)

        is_3d_reinf = AllplanReinf.ReinforcementSettings.Is3DReinforcement()

        global DO_NOT_ASK_3D_REINFORCEMENT
        global USE_3D_REINFORCEMENT

        if not DO_NOT_ASK_3D_REINFORCEMENT and not is_3d_reinf:
            msg = input_data.str_table_service.get_string("e_USE_3D_REINFORCEMENT",
                                                          "'Reinforce with 3D-Model' ist disabled: Enable for the PythonPart?")

            result = AllplanUtil.ShowMessageBox(msg, AllplanUtil.MB_YESNO | AllplanUtil.MB_DONOTASKAGAIN)

            DO_NOT_ASK_3D_REINFORCEMENT = result & AllplanUtil.MB_DONOTASKAGAIN

            result -= DO_NOT_ASK_3D_REINFORCEMENT

            USE_3D_REINFORCEMENT = result == AllplanUtil.IDYES

        input_data.expand_util = AllplanReinf.GeometryExpansionUtil(msg_info, is_3d_reinf | USE_3D_REINFORCEMENT)
        input_data.input_mode  = InputMode.GeoExpand


    @staticmethod
    def process_mouse_msg(mouse_msg     : int,
                          pnt           : AllplanGeo.Point2D,
                          msg_info      : AllplanIFW.AddMsgInfo,
                          input_data    : InputData,
                          script_service: ScriptService) -> tuple[bool, bool]:
        """ process the mouse message

        Args:
            mouse_msg:      mouse message ID
            pnt:            input point in Allplan view coordinates
            msg_info:       additional mouse message info
            input_data:     input data
            script_service: script service

        Returns:
            has expand function state, executed state
        """

        world_pnt2d = AllplanGeo.Point2D(input_data.coord_input.GetViewWorldProjection().ViewToWorldBaseZ0(pnt))

        AllplanGeo.Point2D(input_data.coord_input.GetViewWorldProjection().ViewToWorldBaseZ0(pnt))

        input_data.last_input_doc = input_data.coord_input.GetInputViewDocument()
        input_data.last_view_proj = input_data.coord_input.GetViewWorldProjection()

        place_pnt = AllplanGeo.Point3D()

        try:                                            # pylint: disable=too-many-try-statements
            if len(input_data.build_ele_list) == 1:
                expand, _, place_pnt, input_data.asso_ref_ele, create_ele_result =   \
                    input_data.build_ele_script.expand_create_element(input_data.build_ele_list[0], input_data.expand_util,
                                                                world_pnt2d,
                                                                input_data.coord_input.GetViewWorldProjection(),
                                                                input_data.last_input_doc, input_data.last_expanded)
            else:
                expand, _, place_pnt, input_data.asso_ref_ele, create_ele_result =   \
                    input_data.build_ele_script.expand_create_element(input_data.build_ele_list, input_data.build_ele_composite,
                                                                input_data.expand_util, world_pnt2d,
                                                                input_data.coord_input.GetViewWorldProjection(),
                                                                input_data.last_input_doc, input_data.last_expanded)

        except:                         # pylint: disable=bare-except
            traceback.print_exc()

            AllplanUtil.ShowMessageBox(f"Function 'expand_create_element' must be implemented in script"
                                        f" {input_data.build_ele_list[0].script_name}",
                                        AllplanUtil.MB_OK)

            return False, False

        script_service.set_element_result_data(input_data, create_ele_result)

        if expand is False:
            place_pnt = input_data.coord_input.GetInputPoint(mouse_msg, pnt, msg_info).GetPoint()

        input_data.set_insert_matrix_from_point(AllplanGeo.Point3D(place_pnt))

        input_data.last_expanded = expand

        return True, expand

```

</details>