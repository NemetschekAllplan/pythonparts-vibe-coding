---
title: "BuildingElementParameterListUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementParameterListUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementParameterListUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementParameterListUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `utility`

## Übersicht

Script for BuildingElementParameterListUtil

## Abhängigkeiten

- `BuildingElementListUtil`
- `NemAll_Python_Geometry`
- `NemAll_Python_Palette`
- `StringToValueConverter`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `functools`
- `typing`

## Klassen

### `BuildingElementParameterListUtil`

Definition of class BuildingElementParameterListUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value` | `params_list: list[str], value_name: str, value_type: str='string', default: Any=None` | `Any` | Get a value from the parameter list  Args:     params_list: parameter list     value_name:  name of the value     value_type:  value type of the value     default:     default value  Returns:     value |
| `get_value_index` | `params_list: list[str], value_name: str` | `list[int] | int | None` | Get a value index from the parameter list  Args:     params_list: parameter list     value_name:  value name  Returns:     index of the value |
| `set_value` | `params_list: list[str], value_name: str, value: Any` | `bool` | Set a value to the parameter list  Args:     params_list: parameter list     value_name:  description     value:       value  Returns:     value was set state |
| `print_values` | `params_list: list[str]` | `None` | print the parameter list  Args:     params_list: parameter list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementParameterListUtil
"""
from typing import Any

import functools

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Palette as AllplanPalette

from BuildingElementListUtil import BuildingElementListUtil
from StringToValueConverter import StringToValueConverter

from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

class BuildingElementParameterListUtil():
    """ Definition of class BuildingElementParameterListUtil
    """

    @staticmethod
    def get_value(params_list: list[str],
                  value_name : str,
                  value_type : str = "string",
                  default    : Any = None) -> Any:
        """ Get a value from the parameter list

        Args:
            params_list: parameter list
            value_name:  name of the value
            value_type:  value type of the value
            default:     default value

        Returns:
            value
        """

        value_name += "="

        if not (values := [parameter for parameter in params_list if parameter.startswith(value_name)]):
            return default

        value_str_list = [value[value.find("=") + 1:].rstrip("\n") for value in values]

        value_str = "" if value_str_list == [] else value_str_list[0]

        if value_str.startswith("["):
            return BuildingElementListUtil.get_list_element(value_str, ParameterPropertyValueTypesImpl.get_value_type_impl(value_type), None)

        return StringToValueConverter.get_value(ParameterPropertyValueTypesImpl.get_value_type_impl(value_type), value_str)


    #----------------- partial methods for special value types

    get_value_string     = functools.partialmethod(get_value, value_type = "string", default = "")
    get_value_double     = functools.partialmethod(get_value, value_type = "double", default = 0.0)
    get_value_integer    = functools.partialmethod(get_value, value_type = "integer", default = 0)
    get_value_checkbox   = functools.partialmethod(get_value, value_type = "checkbox", default = False)
    get_value_fixture    = functools.partialmethod(get_value, value_type = "fixture", default = AllplanPalette.FixtureProperties())
    get_value_point2d    = functools.partialmethod(get_value, value_type = "point2d", default = AllplanGeo.Point2D())
    get_value_point3d    = functools.partialmethod(get_value, value_type = "point3d", default = AllplanGeo.Point3D())
    get_value_polyline3d = functools.partialmethod(get_value, value_type = "polyline3d", default = AllplanGeo.Polyline3D())
    get_value_polygon3d  = functools.partialmethod(get_value, value_type = "polygon3d", default = AllplanGeo.Polygon3D())
    get_value_matrix3d   = functools.partialmethod(get_value, value_type = "matrix3d", default = AllplanGeo.Matrix3D())
    get_value_vector3d   = functools.partialmethod(get_value, value_type = "vector3d", default = AllplanGeo.Vector3D())


    @staticmethod
    def get_value_index(params_list: list[str],
                        value_name : str) -> (list[int] | int | None):
        """ Get a value index from the parameter list

        Args:
            params_list: parameter list
            value_name:  value name

        Returns:
            index of the value
        """

        value_name += "="

        if not (indexes := [index for index, parameter in enumerate(params_list) if parameter.startswith(value_name)]):
            return None

        return indexes if len(indexes) != 1 else indexes[0]


    @staticmethod
    def set_value(params_list: list[str],
                  value_name : str,
                  value      : Any) -> bool:
        """ Set a value to the parameter list

        Args:
            params_list: parameter list
            value_name:  description
            value:       value

        Returns:
            value was set state
        """

        value_index = BuildingElementParameterListUtil.get_value_index(params_list, value_name)

        if value_index is None or isinstance(value_index, list):
            return False

        if isinstance(value, list):
            value = f"[{';'.join([str(x) for x in value])}]"

        params_list[value_index] = value_name + "=" + str(value) + "\n"

        return True


    @staticmethod
    def print_values(params_list: list[str]):
        """ print the parameter list

        Args:
            params_list: parameter list
        """

        print()
        print("===========================================================================================================================")
        print("Parameter:")
        print()

        for param in params_list:
            print(param.rstrip("\n"))

        print()
        print("===========================================================================================================================")

```

</details>