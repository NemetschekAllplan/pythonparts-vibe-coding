---
title: "BaseScriptObject"
source: "PythonPartsFramework\GeneralScripts\BaseScriptObject.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BaseScriptObject

> **Pfad:** `PythonPartsFramework\GeneralScripts\BaseScriptObject.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the script object base class

## Abhängigkeiten

- `ControlPropertiesUtil`
- `CreateElementResult`
- `HandleProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `ScriptObjectInteractors.BaseScriptObjectInteractor`
- `ScriptObjectInteractors.OnCancelFunctionResult`
- `TypeCollections.ModelEleList`
- `TypeCollections.ModificationElementList`
- `__future__`
- `abc`
- `collections.abc`
- `dataclasses`
- `typing`

## Klassen

### `BaseScriptObjectData`

implementation of the data class for the script object interactor
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `BaseScriptObject`

implementation of the script object base class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, script_object_data: BaseScriptObjectData` | `None` | Initialization of class TextExample  Args:     script_object_data: script object data |
| `document` | `self` | `AllplanEleAdapter.DocumentAdapter` | get the document  Returns:     document |
| `script_object_interactor` | `self` | `BaseScriptObjectInteractor | None` | get the script object interactor  Returns:     script object interactor |
| `script_object_interactor` | `self, interactor: BaseScriptObjectInteractor | None` | `None` | set the script object interactor  Args:     interactor: script object interactor |
| `create_library_preview` | `self` | `CreateElementResult` | create the library preview  Returns:     created elements for the preview |
| `execute` | `self` | `CreateElementResult` | execute the script  Returns:     created result |
| `start_input` | `self` | `None` | start the input  Overload this member function in the case where a script object interactor (e. g. for an element selection) needs to be started before the script execution |
| `start_next_input` | `self` | `None` | start the next input  Overload this member function to execute the needed steps after the execution of a script object interactor (e. g. after an element selection) |
| `modify_element_property` | `self, _name: str, _value: Any` | `bool` | Modify property of element  Args:     _name:  the name of the property.     _value: new value for property.  Returns:     palette update state |
| `on_cancel_function` | `self` | `OnCancelFunctionResult` | Handles the cancel function event (e.g. by ESC, ...)  Returns:     True : cancel the input     False: continue the input     None : in case of not implemented |
| `on_control_event` | `self, _event_id: int` | `bool` | Handles the on control event  Called when an event is triggered by a palette control (ex. button).  Args:     _event_id: event id of the clicked button control  Returns:     True, when palette should be updated. False otherwise. |
| `on_value_input_control_enter` | `self` | `bool` | Process the enter inside the value input control  Returns:     message was processed: True/False |
| `on_shortcut_control_input` | `self, _value: int` | `bool` | Handles the input inside the shortcut control  Args:     _value: shortcut value  Returns:     True/False for success. |
| `on_input_undo` | `self` | `bool` | Process the input undo event  Returns:     message was processed: True/False |
| `set_text_for_palette_modification` | `self, text: str` | `None` | set an input text for a modification by palette  Args:     text: input text |
| `move_handle` | `self, _handle_prop: HandleProperties, _input_pnt: AllplanGeo.Point3D` | `None` | Modify the element geometry by handles  Args:     _handle_prop: handle properties     _input_pnt:   input point |
| `process_mouse_move` | `self, _input_pnt: AllplanGeo.Point3D` | `None` | Process the mouse move event  Args:     _input_pnt: input point |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the script object base class
"""

# pylint: disable=no-self-use

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from collections.abc import Callable
from dataclasses import dataclass

import abc

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Geometry as AllplanGeo

from CreateElementResult import CreateElementResult

from ScriptObjectInteractors.OnCancelFunctionResult import OnCancelFunctionResult

from TypeCollections.ModelEleList import ModelEleList
from TypeCollections.ModificationElementList import ModificationElementList

if TYPE_CHECKING:
    from ControlPropertiesUtil import ControlPropertiesUtil
    from HandleProperties import HandleProperties
    from ScriptObjectInteractors.BaseScriptObjectInteractor import BaseScriptObjectInteractor


@dataclass
class BaseScriptObjectData:
    """ implementation of the data class for the script object interactor
    """

    coord_input : AllplanIFW.CoordinateInput
    """ Object representing user's input in Allplan Viewport """

    modification_ele_list: ModificationElementList
    """ List with UUIDs of modified elements"""

    is_only_update : bool
    """ True, when the script execution was triggered by a PythonPart update """

    execution_event: AllplanSettings.ExecutionEvent
    """ execution event """

    modification_matrix: AllplanGeo.Matrix3D
    """ Modification matrix """

    control_props_util : ControlPropertiesUtil
    """ Utility for altering the properties of palette controls """

    exec_switch_pythonpart : (Callable[[str, bool], None] | None)
    """ Switch to PythonPart

        Args:
            file_name:            file name of the PythonPart
            add_current_to_stack: add the current pyp file to the stack
    """

    exec_palette_update : (Callable[[], None] | None)
    """ Execute the palette update """

    org_and_copy_ele_guids: dict[str, str]
    """ Map of GUIDs for original and copy elements, for the case when python part was called by copy function. """


class BaseScriptObject(abc.ABC, BaseScriptObjectData):
    """ implementation of the script object base class
    """

    def __init__(self,
                 script_object_data: BaseScriptObjectData):
        """ Initialization of class TextExample

        Args:
            script_object_data: script object data
        """

        super().__init__(script_object_data.coord_input,
                         script_object_data.modification_ele_list,
                         script_object_data.is_only_update,
                         script_object_data.execution_event,
                         script_object_data.modification_matrix,
                         script_object_data.control_props_util,
                         script_object_data.exec_switch_pythonpart,
                         script_object_data.exec_palette_update,
                         script_object_data.org_and_copy_ele_guids)

        self.__script_object_interactor : (BaseScriptObjectInteractor | None) = None


    @property
    def document(self) -> AllplanEleAdapter.DocumentAdapter:
        """ get the document

        Returns:
            document
        """

        return self.coord_input.GetInputViewDocument()


    @property
    def script_object_interactor(self) -> (BaseScriptObjectInteractor | None):
        """ get the script object interactor

        Returns:
            script object interactor
        """

        return self.__script_object_interactor


    @script_object_interactor.setter
    def script_object_interactor(self,
                                 interactor: (BaseScriptObjectInteractor | None)):
        """ set the script object interactor

        Args:
            interactor: script object interactor
        """

        self.__script_object_interactor = interactor


    def create_library_preview(self) -> CreateElementResult:
        """ create the library preview

        Returns:
            created elements for the preview
        """

        return CreateElementResult(ModelEleList())


    @abc.abstractmethod
    def execute(self) -> CreateElementResult:
        """  execute the script

        Returns:
            created result
        """


    def start_input(self):
        """ start the input

        Overload this member function in the case where a script object interactor
        (e. g. for an element selection) needs to be started before the script execution
        """


    def start_next_input(self):
        """ start the next input

        Overload this member function to execute the needed steps after the execution
        of a script object interactor (e. g. after an element selection)
        """


    def modify_element_property(self,
                                _name : str,
                                _value: Any) -> bool:
        """ Modify property of element

        Args:
            _name:  the name of the property.
            _value: new value for property.

        Returns:
            palette update state
        """

        return False


    def on_cancel_function(self) -> OnCancelFunctionResult:
        """ Handles the cancel function event (e.g. by ESC, ...)

        Returns:
            True : cancel the input
            False: continue the input
            None : in case of not implemented
        """

        return OnCancelFunctionResult.NOT_IMPLEMENTED


    def on_control_event(self,
                         _event_id: int) -> bool:
        """ Handles the on control event

        Called when an event is triggered by a palette control (ex. button).

        Args:
            _event_id: event id of the clicked button control

        Returns:
            True, when palette should be updated. False otherwise.
        """

        return True


    def on_value_input_control_enter(self) -> bool:
        """ Process the enter inside the value input control

        Returns:
            message was processed: True/False
        """

        return False


    def on_shortcut_control_input(self,                     # pylint: disable=no-self-use
                                  _value: int) -> bool:
        """ Handles the input inside the shortcut control

        Args:
            _value: shortcut value

        Returns:
            True/False for success.
        """

        print()
        print("Missing implementation of on_shortcut_control_input ---> see BaseScriptObject!!!")
        print()

        return False


    def on_input_undo(self) -> bool:                                 # pylint: disable=no-self-use
        """ Process the input undo event

        Returns:
            message was processed: True/False
        """

        print()
        print("Missing implementation of on_input_undo ---> see BaseScriptObject!!!")
        print()

        return False


    def set_text_for_palette_modification(self,
                                          text: str):
        """ set an input text for a modification by palette

        Args:
            text: input text
        """

        self.coord_input.InitFirstElementInput(AllplanIFW.InputStringConvert(text))


    def move_handle(self,
                    _handle_prop: HandleProperties,
                    _input_pnt  : AllplanGeo.Point3D):
        """ Modify the element geometry by handles

        Args:
            _handle_prop: handle properties
            _input_pnt:   input point
        """

        raise NotImplementedError


    def process_mouse_move(self,
                           _input_pnt: AllplanGeo.Point3D):
        """ Process the mouse move event

        Args:
            _input_pnt: input point
        """

```

</details>