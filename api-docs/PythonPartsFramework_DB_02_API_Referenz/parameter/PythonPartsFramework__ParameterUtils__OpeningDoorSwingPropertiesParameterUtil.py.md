---
title: "OpeningDoorSwingPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\OpeningDoorSwingPropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningDoorSwingPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\OpeningDoorSwingPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the opening door swing properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_ArchElements`
- `math`

## Klassen

### `OpeningDoorSwingPropertiesParameterUtil`

implementation of the opening door swing properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_door_swing_properties` | `build_ele: BuildingElement, name_postfix: str, door_swing_prop: AllplanArchEle.DoorSwingProperties` | `None` | create the door swing properties from the parameter values  Args:     build_ele:    building element with the parameter properties     name_postfix: postfix of the parameter names     door_swing_prop:  door_swing properties |
| `set_parameter_values` | `build_ele: BuildingElement, door_swing_prop: AllplanArchEle.DoorSwingProperties, name_postfix: str` | `None` | get the parameter values from the text properties  Args:     build_ele:       building element with the parameter properties     door_swing_prop: door_swing properties     name_postfix:    post fix of the parameter names |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening door swing properties parameter utilities
"""

import math

import NemAll_Python_ArchElements as AllplanArchEle

from BuildingElement import BuildingElement

class OpeningDoorSwingPropertiesParameterUtil():
    """ implementation of the opening door swing properties parameter utilities
    """

    @staticmethod
    def create_door_swing_properties(build_ele   : BuildingElement,
                                 name_postfix: str,
                                 door_swing_prop : AllplanArchEle.DoorSwingProperties):
        """ create the door swing properties from the parameter values

        Args:
            build_ele:    building element with the parameter properties
            name_postfix: postfix of the parameter names
            door_swing_prop:  door_swing properties
        """

        door_swing_prop.Type           = build_ele.get_existing_property(f"DoorSwingSymbol{name_postfix}").value
        door_swing_prop.BasePointIndex = build_ele.get_existing_property(f"DoorSwingBasePointIndex{name_postfix}").value
        door_swing_prop.Angle          = math.radians(build_ele.get_existing_property(f"OpeningSymbolAngle{name_postfix}").value)
        door_swing_prop.LeafThickness  = build_ele.get_existing_property(f"OpeningSymbolOffset{name_postfix}").value


    @staticmethod
    def set_parameter_values(build_ele      : BuildingElement,
                             door_swing_prop: AllplanArchEle.DoorSwingProperties,
                             name_postfix   : str):
        """ get the parameter values from the text properties

        Args:
            build_ele:       building element with the parameter properties
            door_swing_prop: door_swing properties
            name_postfix:    post fix of the parameter names
        """

        build_ele.get_existing_property(f"DoorSwingSymbol{name_postfix}").value         = door_swing_prop.Type
        build_ele.get_existing_property(f"DoorSwingBasePointIndex{name_postfix}").value = door_swing_prop.BasePointIndex
        build_ele.get_existing_property(f"OpeningSymbolAngle{name_postfix}").value      = door_swing_prop.Angle
        build_ele.get_existing_property(f"OpeningSymbolOffset{name_postfix}").value     = door_swing_prop.LeafThickness

```

</details>