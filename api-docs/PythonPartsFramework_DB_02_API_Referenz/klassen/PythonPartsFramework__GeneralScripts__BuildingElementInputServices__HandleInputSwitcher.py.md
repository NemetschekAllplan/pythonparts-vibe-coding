---
title: "HandleInputSwitcher"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\HandleInputSwitcher.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandleInputSwitcher

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\HandleInputSwitcher.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implements the HandleInputSwitcher class

## Abhängigkeiten

- `BuildingElementInputServices.PythonScriptType`
- `BuildingElementPaletteService`
- `InputData`
- `InputMode`
- `InputService`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Utility`
- `ScriptObjectService`
- `ScriptService`
- `__future__`
- `typing`

## Klassen

### `HandleInputSwitcher`

HandleInputSwitcher class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `execute` | `input_data: InputData, palette_service: BuildingElementPaletteService | None` | `bool` | Execute the input switcher  Args:     input_data:      input data     palette_service: palette service  Returns:     True if the switcher is executed successfully |
| `__start_handle_select` | `input_data: InputData` | `None` | Start the handle selection  Args:     input_data: input data |
| `__start_handle_modification` | `input_data: InputData, palette_service: BuildingElementPaletteService | None` | `None` | Start the handle modification  Args:     input_data:      input data     palette_service: palette service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implements the HandleInputSwitcher class
"""

from __future__ import annotations

from typing import cast, TYPE_CHECKING

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Utility as AllplanUtil

from BuildingElementInputServices.PythonScriptType import PythonScriptType
from InputMode import InputMode

from .InputData import InputData
from .InputService import InputService
from .ScriptObjectService import ScriptObjectService
from .ScriptService import ScriptService

if TYPE_CHECKING:
    from BuildingElementPaletteService import BuildingElementPaletteService

SUB_ELEMENT_KEY = "__SubElementSelect__"

class HandleInputSwitcher:
    """ HandleInputSwitcher class
    """

    @staticmethod
    def execute(input_data     : InputData,
                palette_service: (BuildingElementPaletteService | None)) -> bool:
        """ Execute the input switcher

        Args:
            input_data:      input data
            palette_service: palette service

        Returns:
            True if the switcher is executed successfully
        """

        match input_data.input_mode:

            #----------------- Switch to handle selection

            case InputMode.HandleSelect | InputMode.HandleNext:
                HandleInputSwitcher.__start_handle_select(input_data)

                return True


            #----------------- Switch to handle modification

            case InputMode.HandleModify:
                HandleInputSwitcher.__start_handle_modification(input_data, palette_service)

                return True


        return False


    @staticmethod
    def __start_handle_select(input_data: InputData):
        """ Start the handle selection

        Args:
            input_data: input data
        """

        input_data.coord_input.StopHandleModification()

        if input_data.input_mode == InputMode.HandleNext:
            InputService.recalculate_and_draw_preview(input_data, True, False, False)

        input_data.input_mode = InputMode.HandleSelect

        input_data.handle_modi_service.start(input_data.create_ele_result.handles,input_data.insert_matrix,
                                             input_data.last_input_doc, input_data.last_view_proj, True)

        if input_data.handle_modi_service.handle_prop and input_data.palette_service:
            input_data.palette_service.update_palette(-1, True)

        str_tmp = input_data.str_table_service.get_string("e_SELECT_HANDLE", "Select the handle")

        if input_data.execution_event not in (AllplanSettings.ExecutionEvent.eHandles, AllplanSettings.ExecutionEvent.ePropertyPalette):
            input_data.coord_input.InitFirstPointValueInput(
                AllplanIFW.InputStringConvert(str_tmp),   \
                AllplanIFW.ValueInputControlData(AllplanIFW.eValueInputControlType.eANGLE_COMBOBOX, True, False))


    @staticmethod
    def __start_handle_modification(input_data     : InputData,
                                    palette_service: (BuildingElementPaletteService | None)):
        """ Start the handle modification

        Args:
            input_data:      input data
            palette_service: palette service
        """

        if (handle_prop := input_data.handle_modi_service.handle_prop) is None:
            return


        #---------------- click handle

        if handle_prop.click_state or AllplanUtil.KeyboardState.IsShiftKeyPressed() and handle_prop.parameter_data[0].delete_list_item:
            match input_data.python_script_type:
                case PythonScriptType.SCRIPT_OBJECT:
                    ScriptObjectService.move_handle(input_data, AllplanGeo.Point3D())

                case PythonScriptType.STANDARD:
                    ScriptService.move_handle(input_data, AllplanGeo.Point3D())

            input_data.input_mode = InputMode.HandleSelect

            InputService.recalculate_and_draw_preview(input_data, False, True, False)

            if palette_service is not None:
                palette_service.update_palette(-1, True)

            return


        #---------------- select a sub element

        if cast(str, handle_prop.handle_id) == SUB_ELEMENT_KEY and input_data.palette_service:
            input_data.palette_service.show_page_for_element(input_data.active_page, handle_prop.build_ele_index_list)

            input_data.input_mode = InputMode.HandleSelect

            InputService.recalculate_and_draw_preview(input_data, True, True, False)

            return


        #---------------- start the new handle point input

        input_data.handle_modi_service.start_new_handle_point_input(input_data.str_table_service,
                                                                    input_data.create_ele_result.handle_placement_geo)

```

</details>