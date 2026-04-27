---
title: "TextPointerPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\Reinforcement\TextPointerPropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TextPointerPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\Reinforcement\TextPointerPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `parameter`, `utility`

## Übersicht

implementation of the text pointer properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`

## Klassen

### `TextPointerPropertiesParameterUtil`

implementation of the text pointer properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_text_pointer_properties` | `build_ele: BuildingElement, label: AllplanReinf.ReinforcementLabel, name_postfix: str` | `None` | create the text pointer properties from the parameter values  Args:     build_ele:    building element with the parameter properties     label:        reinforcement label     name_postfix: postfix of the parameter names |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the text pointer properties parameter utilities
"""

import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_Utility as AllplanUtil

from BuildingElement import BuildingElement

class TextPointerPropertiesParameterUtil():
    """ implementation of the text pointer properties parameter utilities
    """

    @staticmethod
    def create_text_pointer_properties(build_ele   : BuildingElement,
                                       label       : AllplanReinf.ReinforcementLabel,
                                       name_postfix: str):
        """ create the text pointer properties from the parameter values

        Args:
            build_ele:    building element with the parameter properties
            label:        reinforcement label
            name_postfix: postfix of the parameter names
        """

        if build_ele.get_existing_property(f"SetPointerStartPoint{name_postfix}").value:
            label.SetPointerStartPoint(build_ele.get_existing_property(f"PointerStartPoint{name_postfix}").value)

        if build_ele.get_existing_property(f"SetAdditionalText{name_postfix}").value:
            label.SetAdditionalText(build_ele.get_existing_property(f"AdditionalText{name_postfix}").value)

        label.SetShowTextPointer(build_ele.get_existing_property(f"ShowTextPointer{name_postfix}").value)
        label.SetShowTextPointerEndSymbol(build_ele.get_existing_property(f"ShowTextPointerEndSymbol{name_postfix}").value)

```

</details>