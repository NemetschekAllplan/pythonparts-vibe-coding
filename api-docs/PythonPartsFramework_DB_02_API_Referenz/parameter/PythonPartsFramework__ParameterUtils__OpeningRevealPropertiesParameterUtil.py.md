---
title: "OpeningRevealPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\OpeningRevealPropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningRevealPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\OpeningRevealPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the opening reveal properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_ArchElements`

## Klassen

### `OpeningRevealPropertiesParameterUtil`

implementation of the opening reveal properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_reveal_properties` | `build_ele: BuildingElement, name_postfix: str, reveal_prop: AllplanArchEle.VerticalOpeningRevealProperties` | `None` | create the reveal properties from the parameter values  Args:     build_ele:    building element with the parameter properties     name_postfix: postfix of the parameter names     reveal_prop:  reveal properties |
| `set_parameter_values` | `build_ele: BuildingElement, reveal_prop: AllplanArchEle.VerticalOpeningRevealProperties, name_postfix: str` | `None` | get the parameter values from the text properties  Args:     build_ele:    building element with the parameter properties     reveal_prop:  reveal properties     name_postfix: post fix of the parameter names |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening reveal properties parameter utilities
"""

import NemAll_Python_ArchElements as AllplanArchEle

from BuildingElement import BuildingElement

class OpeningRevealPropertiesParameterUtil():
    """ implementation of the opening reveal properties parameter utilities
    """

    @staticmethod
    def create_reveal_properties(build_ele   : BuildingElement,
                                 name_postfix: str,
                                 reveal_prop : AllplanArchEle.VerticalOpeningRevealProperties):
        """ create the reveal properties from the parameter values

        Args:
            build_ele:    building element with the parameter properties
            name_postfix: postfix of the parameter names
            reveal_prop:  reveal properties
        """

        reveal_prop.Type = build_ele.get_existing_property(f"Reveal{name_postfix}").value

        if reveal_prop.Type != AllplanArchEle.VerticalOpeningRevealType.eNone:
            reveal_prop.Depth       = build_ele.get_existing_property(f"Depth{name_postfix}").value
            reveal_prop.OuterOffset = build_ele.get_existing_property(f"OuterOffset{name_postfix}").value
            reveal_prop.InnerOffset = build_ele.get_existing_property(f"InnerOffset{name_postfix}").value
            reveal_prop.SideOffset  = build_ele.get_existing_property(f"SideOffset{name_postfix}").value


    @staticmethod
    def set_parameter_values(build_ele   : BuildingElement,
                             reveal_prop : AllplanArchEle.VerticalOpeningRevealProperties,
                             name_postfix: str):
        """ get the parameter values from the text properties

        Args:
            build_ele:    building element with the parameter properties
            reveal_prop:  reveal properties
            name_postfix: post fix of the parameter names
        """

        build_ele.get_existing_property(f"Reveal{name_postfix}").value      = reveal_prop.Type
        build_ele.get_existing_property(f"Depth{name_postfix}").value       = reveal_prop.Depth
        build_ele.get_existing_property(f"OuterOffset{name_postfix}").value = reveal_prop.OuterOffset
        build_ele.get_existing_property(f"InnerOffset{name_postfix}").value = reveal_prop.InnerOffset
        build_ele.get_existing_property(f"SideOffset{name_postfix}").value  = reveal_prop.SideOffset

```

</details>