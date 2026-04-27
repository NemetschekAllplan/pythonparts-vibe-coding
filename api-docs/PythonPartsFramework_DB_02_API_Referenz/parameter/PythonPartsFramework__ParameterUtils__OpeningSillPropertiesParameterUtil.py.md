---
title: "OpeningSillPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\OpeningSillPropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningSillPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\OpeningSillPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the opening sill properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_ArchElements`

## Klassen

### `OpeningSillPropertiesParameterUtil`

implementation of the opening sill properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_sill_properties` | `build_ele: BuildingElement, name_postfix: str, sill_prop: AllplanArchEle.VerticalOpeningSillProperties` | `None` | create the sill properties from the parameter values  Args:     build_ele:    building element with the parameter properties     name_postfix: postfix of the parameter names     sill_prop:    sill properties |
| `set_parameter_values` | `build_ele: BuildingElement, sill_prop: AllplanArchEle.VerticalOpeningSillProperties, name_postfix: str` | `None` | get the parameter values from the text properties  Args:     build_ele:    building element with the parameter properties     sill_prop:    sill properties     name_postfix: post fix of the parameter names |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening sill properties parameter utilities
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_ArchElements as AllplanArchEle

from BuildingElement import BuildingElement

class OpeningSillPropertiesParameterUtil():
    """ implementation of the opening sill properties parameter utilities
    """

    @staticmethod
    def create_sill_properties(build_ele   : BuildingElement,
                               name_postfix: str,
                               sill_prop   : AllplanArchEle.VerticalOpeningSillProperties):
        """ create the sill properties from the parameter values

        Args:
            build_ele:    building element with the parameter properties
            name_postfix: postfix of the parameter names
            sill_prop:    sill properties
        """

        sill_prop.Type =  build_ele.get_existing_property(f"Sill{name_postfix}").value

        com_prop = AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties()

        com_prop.Color  =  build_ele.get_existing_property(f"Color{name_postfix}").value
        com_prop.Pen    =  build_ele.get_existing_property(f"Pen{name_postfix}").value
        com_prop.Stroke =  build_ele.get_existing_property(f"Stroke{name_postfix}").value

        sill_prop.CommonProperties = com_prop


    @staticmethod
    def set_parameter_values(build_ele   : BuildingElement,
                             sill_prop   : AllplanArchEle.VerticalOpeningSillProperties,
                             name_postfix: str):
        """ get the parameter values from the text properties

        Args:
            build_ele:    building element with the parameter properties
            sill_prop:    sill properties
            name_postfix: post fix of the parameter names
        """

        build_ele.get_existing_property(f"Sill{name_postfix}").value   = sill_prop.Type
        build_ele.get_existing_property(f"Color{name_postfix}").value  = sill_prop.CommonProperties.Color
        build_ele.get_existing_property(f"Pen{name_postfix}").value    = sill_prop.CommonProperties.Pen
        build_ele.get_existing_property(f"Stroke{name_postfix}").value = sill_prop.CommonProperties.Stroke

```

</details>