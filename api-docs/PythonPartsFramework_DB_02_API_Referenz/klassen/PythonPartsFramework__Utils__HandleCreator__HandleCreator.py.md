---
title: "HandleCreator"
source: "PythonPartsFramework\Utils\HandleCreator\HandleCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - utility
related:
  -
last_updated: "2026-02-20"
---


# HandleCreator

> **Pfad:** `PythonPartsFramework\Utils\HandleCreator\HandleCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `utility`

## Übersicht

implementation of the handle creator

## Abhängigkeiten

- `HandleDirection`
- `HandleParameterData`
- `HandleParameterType`
- `HandleProperties`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `PointListHandlesCreator`
- `TestHelper`
- `TypeCollections.HandleList`
- `string`
- `typing`

## Klassen

### `HandleCreator`

implementation of the handle creator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `point_distance` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, has_input_field: bool=True, input_field_above: bool=True, show_handles: bool=True, list_index: int | None=None, center_point: AllplanGeo.Point3D | None=None, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a point distance handle  Args:     handle_list:             handle list     name:                    handle parameter name     handle_point:            handle point     ref_point:               reference point     has_input_field:         has input field state     input_field_above:       input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     center_point:            center point for arc     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `x_distance` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, has_input_field: bool=True, input_field_above: bool=True, show_handles: bool=True, list_index: int | None=None, distance_factor: float=1.0, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a x distance handle  Args:     handle_list:             handle list     name:                    handle parameter name     handle_point:            handle point     ref_point:               reference point     has_input_field:         has input field state     input_field_above:       input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     distance_factor:         distance factor     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `y_distance` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, has_input_field: bool=True, input_field_above: bool=True, show_handles: bool=True, list_index: int | None=None, distance_factor: float=1.0, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a y distance handle  Args:     handle_list:             handle list     name:                    handle parameter name     handle_point:            handle point     ref_point:               reference point     has_input_field:         has input field state     input_field_above:       input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     distance_factor:         distance factor     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `z_distance` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, has_input_field: bool=True, input_field_above: bool=True, show_handles: bool=True, list_index: int | None=None, distance_factor: float=1.0, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a z distance handle  Args:     handle_list:             handle list     name:                    handle parameter name     handle_point:            handle point     ref_point:               reference point     has_input_field:         has input field state     input_field_above:       input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     distance_factor:         distance factor     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `xy_distance` | `handle_list: HandleList, x_name: str, y_name: str, handle_point: AllplanGeo.Point3D | AllplanGeo.Point2D, ref_point: AllplanGeo.Point3D | AllplanGeo.Point2D, has_input_field: bool=True, input_field_above: bool=True, show_handles: bool=True, list_index: int | None=None, distance_factor: float=1.0, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a x/y distance handle  Args:     handle_list:             handle list     x_name:                  handle parameter name for x distance     y_name:                  handle parameter name for y distance     handle_point:            handle point     ref_point:               reference point     has_input_field:         has input field state     input_field_above:       input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     distance_factor:         distance factor     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `xyz_distance` | `handle_list: HandleList, x_name: str, y_name: str, z_name: str, handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, has_input_field: bool=True, input_field_above: bool=True, show_handles: bool=True, list_index: int | None=None, distance_factor: float=1.0, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a x/y/z distance handle  Args:     handle_list:             handle list     x_name:                  handle parameter name for x distance     y_name:                  handle parameter name for y distance     z_name:                  handle parameter name for z distance     handle_point:            handle point     ref_point:               reference point     has_input_field:         has input field state     input_field_above:       input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     distance_factor:         distance factor     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `vector_distance` | `handle_list: HandleList, dir_name: str, handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, dir_vector: AllplanGeo.Vector3D, has_input_field: bool=True, input_field_above: bool=True, show_handles: bool=True, list_index: int | None=None, distance_factor: float=1.0, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create vector distance handle  Args:     handle_list:             handle list     dir_name:                direction name     handle_point:            handle point     ref_point:               reference point     dir_vector:              direction vector     has_input_field:         has input field state     input_field_above:       input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     distance_factor:         distance factor     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `vector_distances` | `handle_list: HandleList, dir_names: list[str], handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, dir_vectors: list[AllplanGeo.Vector3D], has_input_fields: list[bool], input_fields_above: list[bool], show_handles: bool=True, list_index: int | None=None, distance_factor: float=1.0, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create vector distance handles  Args:     handle_list:             handle list     dir_names:               direction names     handle_point:            handle point     ref_point:               reference point     dir_vectors:             direction vectors     has_input_fields:        has input field state     input_fields_above:      input field above the dimension line state     show_handles:            show the handles state     list_index:              list index     distance_factor:         distance factor     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode)     disable_transform:       disable handle transformation with the matrix from the handle list |
| `point` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, index: int | None=None, info_text: str='', delete_point: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), handle_type: AllplanIFW.ElementHandleType=AllplanIFW.ElementHandleType.HANDLE_CIRCLE, handle_angle: AllplanGeo.Angle=AllplanGeo.Angle(), disable_transform: bool=False, plane: AllplanGeo.Plane3D | None=None` | `None` | create a point move handle  Args:     handle_list:       handle list     name:              handle parameter name     handle_point:      handle point     index:             point index     info_text:         info text     delete_point:      enable delete point state for list items     owner_element:     owner element of the handle (in element modification mode)     handle_type:       handle type     handle_angle:      handle angle     disable_transform: disable handle transformation with the matrix from the handle list     plane:             input plane for the handle_point movement |
| `angle` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, angle_placement: AllplanGeo.AxisPlacement3D, center_point: AllplanGeo.Point3D | None=None, info_text: str='', owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create an angle handle  Args:     handle_list:       handle list     name:              handle parameter name     handle_point:      handle point     ref_point:         reference point     angle_placement:   angle placement     center_point:      center point for arc angle handle     info_text:         info text     owner_element:     owner element of the handle (in element modification mode)     disable_transform: disable handle transformation with the matrix from the handle list |
| `split_point` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, handle_angle: AllplanGeo.Angle, index: int, info_text: str='', owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False, plane: AllplanGeo.Plane3D | None=None` | `None` | create a split point handle  Args:     handle_list:       handle list     name:              handle parameter name     handle_point:      handle point     handle_angle:      handle angle     index:             point index     info_text:         info text     owner_element:     owner element of the handle (in element modification mode)     disable_transform: disable handle transformation with the matrix from the handle list     plane:             input plane for the handle_point movement |
| `point_list_2d` | `handle_list: HandleList, name: str, handle_points: list[AllplanGeo.Point2D], info_text: str='', info_text_template: Template=Template(''), index_offset: int=0` | `None` | create 2d point move handles  Args:     handle_list:        handle list     name:               handle parameter name     handle_points:      handle points     info_text:          info text     info_text_template: info text template     index_offset:       index offset for the info text |
| `move_in_direction` | `handle_list: HandleList, name: str, placement_point: AllplanGeo.Point3D, angle: AllplanGeo.Angle, info_text: str='', move_by_click: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a handle for a move in the arrow direction  Args:     handle_list:       handle list     name:              handle parameter name     placement_point:   placement move handle     angle:             handle angle     info_text:         info text     move_by_click:     execute the move only by click state     owner_element:     owner element of the handle (in element modification mode)     disable_transform: disable handle transformation with the matrix from the handle list |
| `move` | `handle_list: HandleList, name: str, placement_point: AllplanGeo.Point3D, info_text: str='', move_by_click: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), disable_transform: bool=False` | `None` | create a handle for a move with a blue square  Args:     handle_list:       handle list     name:              handle parameter name     placement_point:   placement move handle     info_text:         info text     move_by_click:     execute the move only by click state     owner_element:     owner element of the handle (in element modification mode)     disable_transform: disable handle transformation with the matrix from the handle list |
| `click` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, handle_type: AllplanIFW.ElementHandleType, info_text: str='', handle_angle: AllplanGeo.Angle=AllplanGeo.Angle(), disable_transform: bool=False` | `None` | create a click handle  Args:     handle_list:       handle list     name:              handle parameter name     handle_point:      handle point     handle_type:       handle type     info_text:         info text     handle_angle:      handle angle     disable_transform: disable handle transformation with the matrix from the handle list |
| `checkbox` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, check_box_state: bool, info_text_checked: str='', info_text_uncheck: str='', disable_transform: bool=False` | `None` | create a checkbox  handle  Args:     handle_list:       handle list     name:              handle parameter name     handle_point:      handle point     check_box_state:   check box state     info_text_checked: info text checked     info_text_uncheck: info text unchecked     disable_transform: disable handle transformation with the matrix from the handle list |
| `increment` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, increment_value: Any, info_text: str='', disable_transform: bool=False` | `None` | create a increment handle  Args:     handle_list:       handle list     name:              handle parameter name     handle_point:      handle point     increment_value:   increment value     info_text:         info text     disable_transform: disable handle transformation with the matrix from the handle list |
| `decrement` | `handle_list: HandleList, name: str, handle_point: AllplanGeo.Point3D, decrement_value: Any, info_text: str='', disable_transform: bool=False` | `None` | create a decrement handle  Args:     handle_list:       handle list     name:              handle parameter name     handle_point:      handle point     decrement_value:   decrement value     info_text:         info text     disable_transform: disable handle transformation with the matrix from the handle list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the handle creator
"""

# pylint: disable=too-many-arguments

from typing import Any

from string import Template

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from HandleDirection import HandleDirection
from HandleParameterData import HandleParameterData
from HandleParameterType import HandleParameterType
from HandleProperties import HandleProperties

from TestHelper import PythonPartPylintDecorator

from TypeCollections.HandleList import HandleList

class HandleCreator():
    """ implementation of the handle creator
    """

    @staticmethod
    def point_distance(handle_list            : HandleList,
                       name                   : str,
                       handle_point           : AllplanGeo.Point3D,
                       ref_point              : AllplanGeo.Point3D,
                       has_input_field        : bool                                 = True,
                       input_field_above      : bool                                 = True,
                       show_handles           : bool                                 = True,
                       list_index             : (int | None)                         = None,
                       center_point           : (AllplanGeo.Point3D | None)          = None,
                       info_text              : str                                  = "",
                       show_input_field_always: bool                                 = False,
                       owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                       disable_transform      : bool                                 = False):
        """ create a point distance handle

        Args:
            handle_list:             handle list
            name:                    handle parameter name
            handle_point:            handle point
            ref_point:               reference point
            has_input_field:         has input field state
            input_field_above:       input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            center_point:            center point for arc
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, ref_point,
                                            [HandleParameterData(name, HandleParameterType.POINT_DISTANCE,
                                                                 has_input_field         = has_input_field,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above,
                                                                 list_index              = list_index)],
                                            HandleDirection.POINT_DIR,
                                            show_handles  = show_handles,
                                            center_point  = center_point,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def x_distance(handle_list            : HandleList,
                   name                   : str,
                   handle_point           : AllplanGeo.Point3D,
                   ref_point              : AllplanGeo.Point3D,
                   has_input_field        : bool                                 = True,
                   input_field_above      : bool                                 = True,
                   show_handles           : bool                                 = True,
                   list_index             : (int | None)                         = None,
                   distance_factor        : float                                = 1.0,
                   info_text              : str                                  = "",
                   show_input_field_always: bool                                 = False,
                   owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                   disable_transform      : bool                                 = False):
        """ create a x distance handle

        Args:
            handle_list:             handle list
            name:                    handle parameter name
            handle_point:            handle point
            ref_point:               reference point
            has_input_field:         has input field state
            input_field_above:       input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            distance_factor:         distance factor
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, ref_point,
                                            [HandleParameterData(name, HandleParameterType.X_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above)],
                                            HandleDirection.X_DIR,
                                            show_handles  = show_handles,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def y_distance(handle_list            : HandleList,
                   name                   : str,
                   handle_point           : AllplanGeo.Point3D,
                   ref_point              : AllplanGeo.Point3D,
                   has_input_field        : bool                                 = True,
                   input_field_above      : bool                                 = True,
                   show_handles           : bool                                 = True,
                   list_index             : (int | None)                         = None,
                   distance_factor        : float                                = 1.0,
                   info_text              : str                                  = "",
                   show_input_field_always: bool                                 = False,
                   owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                   disable_transform      : bool                                 = False):
        """ create a y distance handle

        Args:
            handle_list:             handle list
            name:                    handle parameter name
            handle_point:            handle point
            ref_point:               reference point
            has_input_field:         has input field state
            input_field_above:       input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            distance_factor:         distance factor
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, ref_point,
                                            [HandleParameterData(name, HandleParameterType.Y_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above)],
                                            HandleDirection.Y_DIR,
                                            show_handles  = show_handles,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def z_distance(handle_list            : HandleList,
                   name                   : str,
                   handle_point           : AllplanGeo.Point3D,
                   ref_point              : AllplanGeo.Point3D,
                   has_input_field        : bool                                 = True,
                   input_field_above      : bool                                 = True,
                   show_handles           : bool                                 = True,
                   list_index             : (int | None)                         = None,
                   distance_factor        : float                                = 1.0,
                   info_text              : str                                  = "",
                   show_input_field_always: bool                                 = False,
                   owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                   disable_transform      : bool                                 = False):
        """ create a z distance handle

        Args:
            handle_list:             handle list
            name:                    handle parameter name
            handle_point:            handle point
            ref_point:               reference point
            has_input_field:         has input field state
            input_field_above:       input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            distance_factor:         distance factor
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, ref_point,
                                            [HandleParameterData(name, HandleParameterType.Z_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above)],
                                            HandleDirection.Z_DIR,
                                            show_handles  = show_handles,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def xy_distance(handle_list            : HandleList,
                    x_name                 : str,
                    y_name                 : str,
                    handle_point           : (AllplanGeo.Point3D | AllplanGeo.Point2D),
                    ref_point              : (AllplanGeo.Point3D | AllplanGeo.Point2D),
                    has_input_field        : bool                                 = True,
                    input_field_above      : bool                                 = True,
                    show_handles           : bool                                 = True,
                    list_index             : (int | None)                         = None,
                    distance_factor        : float                                = 1.0,
                    info_text              : str                                  = "",
                    show_input_field_always: bool                                 = False,
                    owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                    disable_transform      : bool                                 = False):
        """ create a x/y distance handle

        Args:
            handle_list:             handle list
            x_name:                  handle parameter name for x distance
            y_name:                  handle parameter name for y distance
            handle_point:            handle point
            ref_point:               reference point
            has_input_field:         has input field state
            input_field_above:       input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            distance_factor:         distance factor
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(x_name, AllplanGeo.Point3D(handle_point), AllplanGeo.Point3D(ref_point),
                                            [HandleParameterData(x_name, HandleParameterType.X_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above),
                                             HandleParameterData(y_name, HandleParameterType.Y_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above)],
                                            HandleDirection.XY_DIR,
                                            show_handles  = show_handles,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def xyz_distance(handle_list            : HandleList,
                     x_name                 : str,
                     y_name                 : str,
                     z_name                 : str,
                     handle_point           : AllplanGeo.Point3D,
                     ref_point              : AllplanGeo.Point3D,
                     has_input_field        : bool                                 = True,
                     input_field_above      : bool                                 = True,
                     show_handles           : bool                                 = True,
                     list_index             : (int | None)                         = None,
                     distance_factor        : float                                = 1.0,
                     info_text              : str                                  = "",
                     show_input_field_always: bool                                 = False,
                     owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                     disable_transform      : bool                                 = False):
        """ create a x/y/z distance handle

        Args:
            handle_list:             handle list
            x_name:                  handle parameter name for x distance
            y_name:                  handle parameter name for y distance
            z_name:                  handle parameter name for z distance
            handle_point:            handle point
            ref_point:               reference point
            has_input_field:         has input field state
            input_field_above:       input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            distance_factor:         distance factor
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(x_name, handle_point, ref_point,
                                            [HandleParameterData(x_name, HandleParameterType.X_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above),
                                             HandleParameterData(y_name, HandleParameterType.Y_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above),
                                             HandleParameterData(z_name, HandleParameterType.Z_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above)],
                                            HandleDirection.XY_DIR,
                                            show_handles  = show_handles,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def vector_distance(handle_list            : HandleList,
                        dir_name               : str,
                        handle_point           : AllplanGeo.Point3D,
                        ref_point              : AllplanGeo.Point3D,
                        dir_vector             : AllplanGeo.Vector3D,
                        has_input_field        : bool                                 = True,
                        input_field_above      : bool                                 = True,
                        show_handles           : bool                                 = True,
                        list_index             : (int | None)                         = None,
                        distance_factor        : float                                = 1.0,
                        info_text              : str                                  = "",
                        show_input_field_always: bool                                 = False,
                        owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                        disable_transform      : bool                                 = False):
        """ create vector distance handle

        Args:
            handle_list:             handle list
            dir_name:                direction name
            handle_point:            handle point
            ref_point:               reference point
            dir_vector:              direction vector
            has_input_field:         has input field state
            input_field_above:       input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            distance_factor:         distance factor
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(dir_name, handle_point, ref_point,
                                            [HandleParameterData(dir_name, HandleParameterType.VECTOR_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above,
                                                                 dir_vector              = dir_vector)],
                                            HandleDirection.VECTOR_DIR,
                                            show_handles  = show_handles,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def vector_distances(handle_list            : HandleList,
                         dir_names              : list[str],
                         handle_point           : AllplanGeo.Point3D,
                         ref_point              : AllplanGeo.Point3D,
                         dir_vectors            : list[AllplanGeo.Vector3D],
                         has_input_fields       : list[bool],
                         input_fields_above     : list[bool],
                         show_handles           : bool                                 = True,
                         list_index             : (int | None)                         = None,
                         distance_factor        : float                                = 1.0,
                         info_text              : str                                  = "",
                         show_input_field_always: bool                                 = False,
                         owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                         disable_transform      : bool                                 = False):
        """ create vector distance handles

        Args:
            handle_list:             handle list
            dir_names:               direction names
            handle_point:            handle point
            ref_point:               reference point
            dir_vectors:             direction vectors
            has_input_fields:        has input field state
            input_fields_above:      input field above the dimension line state
            show_handles:            show the handles state
            list_index:              list index
            distance_factor:         distance factor
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
            disable_transform:       disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(dir_names[0], handle_point, ref_point,
                                            [HandleParameterData(name, HandleParameterType.VECTOR_DISTANCE,
                                                                 has_input_field,
                                                                 list_index              = list_index,
                                                                 distance_factor         = distance_factor,
                                                                 show_input_field_always = show_input_field_always,
                                                                 input_field_above       = input_field_above,
                                                                 dir_vector              = dir_vector)
                                                for name, dir_vector, has_input_field, input_field_above in zip(dir_names, dir_vectors,
                                                                                                                has_input_fields,
                                                                                                                input_fields_above)],
                                            HandleDirection.VECTOR_DIR,
                                            show_handles  = show_handles,
                                            info_text     = info_text,
                                            owner_element = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def point(handle_list      : HandleList,
              name             : str,
              handle_point     : AllplanGeo.Point3D,
              index            : (int | None)                         = None,
              info_text        : str                                  = "",
              delete_point     : bool                                 = False,
              owner_element    : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
              handle_type      : AllplanIFW.ElementHandleType         = AllplanIFW.ElementHandleType.HANDLE_CIRCLE,
              handle_angle     : AllplanGeo.Angle                     = AllplanGeo.Angle(),
              disable_transform: bool                                 = False,
              plane            : (AllplanGeo.Plane3D | None)          = None):
        """ create a point move handle

        Args:
            handle_list:       handle list
            name:              handle parameter name
            handle_point:      handle point
            index:             point index
            info_text:         info text
            delete_point:      enable delete point state for list items
            owner_element:     owner element of the handle (in element modification mode)
            handle_type:       handle type
            handle_angle:      handle angle
            disable_transform: disable handle transformation with the matrix from the handle list
            plane:             input plane for the handle_point movement
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, handle_point,
                                            [HandleParameterData(name, HandleParameterType.POINT, False,
                                                                 list_index = index, delete_list_item = delete_point)],
                                             HandleDirection.XYZ_DIR if plane is None else HandleDirection.PLANE_DIR,
                                             info_text     = info_text,
                                             owner_element = owner_element,
                                             plane         = plane))

        handle_list[-1].handle_type  = handle_type
        handle_list[-1].handle_angle = handle_angle

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def angle(handle_list      : HandleList,
              name             : str,
              handle_point     : AllplanGeo.Point3D,
              ref_point        : AllplanGeo.Point3D,
              angle_placement  : AllplanGeo.AxisPlacement3D,
              center_point     : (AllplanGeo.Point3D | None)          = None,
              info_text        : str                                  = "",
              owner_element    : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
              disable_transform: bool                                 = False):
        """ create an angle handle

        Args:
            handle_list:       handle list
            name:              handle parameter name
            handle_point:      handle point
            ref_point:         reference point
            angle_placement:   angle placement
            center_point:      center point for arc angle handle
            info_text:         info text
            owner_element:     owner element of the handle (in element modification mode)
            disable_transform: disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, ref_point,
                                            [HandleParameterData(name, HandleParameterType.ANGLE, False)],
                                            HandleDirection.ANGLE,
                                            angle_placement = angle_placement,
                                            info_text       = info_text,
                                            center_point    = center_point,
                                            owner_element   = owner_element))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def split_point(handle_list      : HandleList,
                    name             : str,
                    handle_point     : AllplanGeo.Point3D,
                    handle_angle     : AllplanGeo.Angle,
                    index            : int,
                    info_text        : str                                  = "",
                    owner_element    : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                    disable_transform: bool                                 = False,
                    plane            : (AllplanGeo.Plane3D | None)          = None):
        """ create a split point handle

        Args:
            handle_list:       handle list
            name:              handle parameter name
            handle_point:      handle point
            handle_angle:      handle angle
            index:             point index
            info_text:         info text
            owner_element:     owner element of the handle (in element modification mode)
            disable_transform: disable handle transformation with the matrix from the handle list
            plane:             input plane for the handle_point movement
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, handle_point,
                                            [HandleParameterData(name, HandleParameterType.SPLIT_POINT, False,
                                                                 list_index = index + 1)],
                                             HandleDirection.XYZ_DIR if plane is None else HandleDirection.PLANE_DIR,
                                             info_text     = info_text,
                                             owner_element = owner_element,
                                             plane         = plane))

        handle_list[-1].handle_type  = AllplanIFW.ElementHandleType.HANDLE_SQUARE_BLUE
        handle_list[-1].handle_angle = handle_angle

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @PythonPartPylintDecorator.deprecated(replace = "use PointListHandlesCreator.point_list(...)")
    @staticmethod
    def point_list_2d(handle_list       : HandleList,
                      name              : str,
                      handle_points     : list[AllplanGeo.Point2D],
                      info_text         : str      = "",
                      info_text_template: Template = Template(""),
                      index_offset      : int      = 0):
        """ create 2d point move handles

        Args:
            handle_list:        handle list
            name:               handle parameter name
            handle_points:      handle points
            info_text:          info text
            info_text_template: info text template
            index_offset:       index offset for the info text
        """

        from .PointListHandlesCreator import PointListHandlesCreator    # pylint: disable=import-outside-toplevel

        PointListHandlesCreator.point_list(handle_list, name, handle_points, info_text, info_text_template, index_offset)


    @staticmethod
    def move_in_direction(handle_list      : HandleList,
                          name             : str,
                          placement_point  : AllplanGeo.Point3D,
                          angle            : AllplanGeo.Angle,
                          info_text        : str                                  = "",
                          move_by_click    : bool                                 = False,
                          owner_element    : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                          disable_transform: bool                                 = False):
        """ create a handle for a move in the arrow direction

        Args:
            handle_list:       handle list
            name:              handle parameter name
            placement_point:   placement move handle
            angle:             handle angle
            info_text:         info text
            move_by_click:     execute the move only by click state
            owner_element:     owner element of the handle (in element modification mode)
            disable_transform: disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        move_handle = HandleProperties(name, placement_point, AllplanGeo.Point3D(),
                                       [HandleParameterData(name, HandleParameterType.POINT, False)],
                                        HandleDirection.CLICK if move_by_click else HandleDirection.XYZ_DIR,
                                        info_text     = info_text,
                                        owner_element = owner_element)

        move_handle.handle_type  = AllplanIFW.ElementHandleType.HANDLE_ARROW
        move_handle.handle_angle = angle

        handle_list.append(move_handle)

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def move(handle_list      : HandleList,
             name             : str,
             placement_point  : AllplanGeo.Point3D,
             info_text        : str                                  = "",
             move_by_click    : bool                                 = False,
             owner_element    : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
             disable_transform: bool                                 = False):
        """ create a handle for a move with a blue square

        Args:
            handle_list:       handle list
            name:              handle parameter name
            placement_point:   placement move handle
            info_text:         info text
            move_by_click:     execute the move only by click state
            owner_element:     owner element of the handle (in element modification mode)
            disable_transform: disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        move_handle = HandleProperties(name, placement_point, AllplanGeo.Point3D(),
                                       [HandleParameterData(name, HandleParameterType.POINT, False)],
                                        HandleDirection.CLICK if move_by_click else HandleDirection.XYZ_DIR,
                                        info_text     = info_text,
                                        owner_element = owner_element)

        move_handle.handle_type = AllplanIFW.ElementHandleType.HANDLE_SQUARE_RED

        handle_list.append(move_handle)

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def click(handle_list      : HandleList,
              name             : str,
              handle_point     : AllplanGeo.Point3D,
              handle_type      : AllplanIFW.ElementHandleType,
              info_text        : str              = "",
              handle_angle     : AllplanGeo.Angle = AllplanGeo.Angle(),
              disable_transform: bool             = False):
        """ create a click handle

        Args:
            handle_list:       handle list
            name:              handle parameter name
            handle_point:      handle point
            handle_type:       handle type
            info_text:         info text
            handle_angle:      handle angle
            disable_transform: disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        click_handle = HandleProperties(name, handle_point, AllplanGeo.Point3D(),
                                         [],
                                         HandleDirection.CLICK,
                                         info_text = info_text)

        click_handle.handle_angle = handle_angle
        click_handle.handle_type  = handle_type

        handle_list.append(click_handle)

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def checkbox(handle_list      : HandleList,
                 name             : str,
                 handle_point     : AllplanGeo.Point3D,
                 check_box_state  : bool,
                 info_text_checked: str  = "",
                 info_text_uncheck: str  = "",
                 disable_transform: bool = False):
        """ create a checkbox  handle

        Args:
            handle_list:       handle list
            name:              handle parameter name
            handle_point:      handle point
            check_box_state:   check box state
            info_text_checked: info text checked
            info_text_uncheck: info text unchecked
            disable_transform: disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, AllplanGeo.Point3D(),
                                            [HandleParameterData(name, HandleParameterType.CHECK_BOX,
                                                                 check_box_state = check_box_state)],
                                            HandleDirection.CLICK,
                                            info_text = info_text_checked if check_box_state else info_text_uncheck))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def increment(handle_list      : HandleList,
                  name             : str,
                  handle_point     : AllplanGeo.Point3D,
                  increment_value  : Any,
                  info_text        : str  = "",
                  disable_transform: bool = False):
        """ create a increment handle

        Args:
            handle_list:       handle list
            name:              handle parameter name
            handle_point:      handle point
            increment_value:   increment value
            info_text:         info text
            disable_transform: disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, AllplanGeo.Point3D(),
                                            [HandleParameterData(name, HandleParameterType.INCREMENT_BUTTON,
                                                                 in_decrement_value = increment_value)],
                                            HandleDirection.CLICK,
                                            info_text = info_text))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True


    @staticmethod
    def decrement(handle_list      : HandleList,
                  name             : str,
                  handle_point     : AllplanGeo.Point3D,
                  decrement_value  : Any,
                  info_text        : str  = "",
                  disable_transform: bool = False):
        """ create a decrement handle

        Args:
            handle_list:       handle list
            name:              handle parameter name
            handle_point:      handle point
            decrement_value:   decrement value
            info_text:         info text
            disable_transform: disable handle transformation with the matrix from the handle list
        """

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = not disable_transform

        handle_list.append(HandleProperties(name, handle_point, AllplanGeo.Point3D(),
                                            [HandleParameterData(name, HandleParameterType.DECREMENT_BUTTON,
                                                                 in_decrement_value = decrement_value)],
                                            HandleDirection.CLICK,
                                            info_text = info_text))

        if isinstance(handle_list, HandleList):
            handle_list.enable_transform = True

```

</details>