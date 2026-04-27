---
title: "HandleParameterData"
source: "PythonPartsFramework\GeneralScripts\HandleParameterData.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - parameter
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandleParameterData

> **Pfad:** `PythonPartsFramework\GeneralScripts\HandleParameterData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `parameter`, `script`

## Übersicht

Implementation of the data class for the handle parameter data.

## Abhängigkeiten

- `HandleParameterType`
- `NemAll_Python_Geometry`
- `TypeCollections.GeometryTyping`
- `dataclasses`
- `typing`

## Klassen

### `HandleParameterData`

The parameter data are used to define the recalculation of the parameter property
assigned to the handle. The recalculation is performed depending on the defined
parameter type.

Args:
    param_prop_name        : Name of the parameter property
    parameter_type         : Type of the parameter
    has_input_field        : Add an input field for the value input
    show_negative_value    : Show a negative value in the input field
    check_box_state        : State of the checkbox
    in_decrement_value     : Value for the increment or decrement button, can be int, float, Point3D, ...
    list_index             : List index assigned to the handle, necessary if the parameter property is a list.
                             In case of an n-dimensional list the index must be defined as list like [1,2,3]
    distance_factor        : Factor for the distance
    dir_vector             : direction vector in case of VECTOR_DISTANCE
    show_input_field_always: show the input field always
    input_field_above      : input field above the dimension line
    geo_element            : geometry element
    delete_list_item       : enable delete list item state

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the data class for the handle parameter data.
"""

from typing import Any

from dataclasses import dataclass

import NemAll_Python_Geometry as AllplanGeo

from HandleParameterType import HandleParameterType

from TypeCollections.GeometryTyping import CURVES

@dataclass
class HandleParameterData():
    """ The parameter data are used to define the recalculation of the parameter property
    assigned to the handle. The recalculation is performed depending on the defined
    parameter type.

    Args:
        param_prop_name        : Name of the parameter property
        parameter_type         : Type of the parameter
        has_input_field        : Add an input field for the value input
        show_negative_value    : Show a negative value in the input field
        check_box_state        : State of the checkbox
        in_decrement_value     : Value for the increment or decrement button, can be int, float, Point3D, ...
        list_index             : List index assigned to the handle, necessary if the parameter property is a list.
                                 In case of an n-dimensional list the index must be defined as list like [1,2,3]
        distance_factor        : Factor for the distance
        dir_vector             : direction vector in case of VECTOR_DISTANCE
        show_input_field_always: show the input field always
        input_field_above      : input field above the dimension line
        geo_element            : geometry element
        delete_list_item       : enable delete list item state
    """

    param_prop_name        : str
    param_type             : HandleParameterType
    has_input_field        : bool                         = True
    show_negative_value    : bool                         = False
    check_box_state        : bool                         = True
    in_decrement_value     : Any                          = 1
    list_index             : (int | list[int] | None)     = None
    distance_factor        : (float | None)               = None
    dir_vector             : (AllplanGeo.Vector3D | None) = None
    show_input_field_always: bool                         = False
    input_field_above      : bool                         = True
    geo_element            : CURVES                       = None
    delete_list_item       : bool                         = False

```

</details>