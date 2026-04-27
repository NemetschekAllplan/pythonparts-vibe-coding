---
title: "HandlePropertiesService"
source: "PythonPartsFramework\GeneralScripts\HandlePropertiesService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandlePropertiesService

> **Pfad:** `PythonPartsFramework\GeneralScripts\HandlePropertiesService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the service for the handle properties

## Abhängigkeiten

- `BuildingElement`
- `HandleParameterType`
- `HandleProperties`
- `Handles.HandlePropUpdateData`
- `NemAll_Python_Geometry`
- `__future__`
- `typing`

## Klassen

### `HandlePropertiesService`

implementation of the service for the handle properties
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `update_property_value` | `build_ele: BuildingElement, handle_prop: HandleProperties, input_pnt: AllplanGeo.Point3D` | `bool` | Update the property value  Args:     build_ele:   building element with the parameter properties     handle_prop: handle property     input_pnt:   input point  Returns:     update palette state |
| `update_point` | `handle_prop: HandleProperties, name: str, value: float` | `bool` | Update the point  Args:     handle_prop: handle property     name:        name of the property     value:       input value  Returns:     update palette state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the service for the handle properties
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo

from HandleParameterType import HandleParameterType
from HandleProperties import HandleProperties

from Handles.HandlePropUpdateData import HandlePropUpdateData

if TYPE_CHECKING:
    from BuildingElement import BuildingElement

HANDLE_PROPERTIES_UPDATER: dict[HandleParameterType, HandlePropUpdateData] = \
    {HandleParameterType.X_DISTANCE       : HandlePropUpdateData("XDistance"),
     HandleParameterType.Y_DISTANCE       : HandlePropUpdateData("YDistance"),
     HandleParameterType.Z_DISTANCE       : HandlePropUpdateData("ZDistance"),
     HandleParameterType.POINT            : HandlePropUpdateData("Point"),
     HandleParameterType.POINT_DISTANCE   : HandlePropUpdateData("PointDistance"),
     HandleParameterType.ANGLE            : HandlePropUpdateData("Angle"),
     HandleParameterType.Z_COORD          : HandlePropUpdateData("ZCoord"),
     HandleParameterType.VECTOR_DISTANCE  : HandlePropUpdateData("VectorDistance"),
     HandleParameterType.CHECK_BOX        : HandlePropUpdateData("CheckBox"),
     HandleParameterType.INCREMENT_BUTTON : HandlePropUpdateData("IncrementButton"),
     HandleParameterType.DECREMENT_BUTTON : HandlePropUpdateData("DecrementButton"),
     HandleParameterType.SPLIT_POINT      : HandlePropUpdateData("SplitPoint"),
     HandleParameterType.CURVE_POINT      : HandlePropUpdateData("CurvePoint"),
     HandleParameterType.CURVE_SPLIT_POINT: HandlePropUpdateData("CurveSplitPoint")
    }


HANDLE_POINT_UPDATER: dict[HandleParameterType, HandlePropUpdateData] = \
    {HandleParameterType.X_POINT_DISTANCE       : HandlePropUpdateData("XPointDistance"),
     HandleParameterType.Y_POINT_DISTANCE       : HandlePropUpdateData("YPointDistance"),
     HandleParameterType.Z_POINT_DISTANCE       : HandlePropUpdateData("ZPointDistance"),
     HandleParameterType.LENGTH_POINT_DISTANCE  : HandlePropUpdateData("LengthPointDistance")
    }


class HandlePropertiesService():
    """ implementation of the service for the handle properties
    """

    @staticmethod
    def update_property_value(build_ele  : BuildingElement,
                              handle_prop: HandleProperties,
                              input_pnt  : AllplanGeo.Point3D) -> bool:
        """ Update the property value

        Args:
            build_ele:   building element with the parameter properties
            handle_prop: handle property
            input_pnt:   input point

        Returns:
            update palette state
        """

        update_palette = False

        for param_data in handle_prop.parameter_data:
            if (modify_data := HANDLE_PROPERTIES_UPDATER.get(param_data.param_type)) is None:
                continue

            update_class = modify_data.get_handle_prop_update()(build_ele, handle_prop, input_pnt, param_data)

            update_class()

            update_palette |= update_class.update_palette

        return update_palette


    @staticmethod
    def update_point(handle_prop: HandleProperties,
                     name       : str,
                     value      : float) -> bool:
        """ Update the point

        Args:
            handle_prop: handle property
            name:        name of the property
            value:       input value

        Returns:
            update palette state
        """

        for param_data in handle_prop.parameter_data:
            if param_data.param_prop_name != name or (modify_data := HANDLE_POINT_UPDATER.get(param_data.param_type)) is None:
                continue

            update_class = modify_data.get_handle_prop_update()(handle_prop, param_data, value)

            update_class()

            return True

        return False

```

</details>