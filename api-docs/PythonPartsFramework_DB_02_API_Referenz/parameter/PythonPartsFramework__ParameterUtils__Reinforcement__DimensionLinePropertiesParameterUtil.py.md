---
title: "DimensionLinePropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\Reinforcement\DimensionLinePropertiesParameterUtil.py"
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


# DimensionLinePropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\Reinforcement\DimensionLinePropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `parameter`, `utility`

## Übersicht

implementation of the dimension line properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`

## Klassen

### `DimensionLinePropertiesParameterUtil`

implementation of the dimension line properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_dim_line_properties` | `build_ele: BuildingElement, label: AllplanReinf.ReinforcementLabel, name_postfix: str` | `None` | create the dimension line properties from the parameter values  Args:     build_ele:    building element with the parameter properties     label:        reinforcement label     name_postfix: postfix of the parameter names |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the dimension line properties parameter utilities
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_Utility as AllplanUtil

from BuildingElement import BuildingElement

class DimensionLinePropertiesParameterUtil():
    """ implementation of the dimension line properties parameter utilities
    """

    @staticmethod
    def create_dim_line_properties(build_ele   : BuildingElement,
                                   label       : AllplanReinf.ReinforcementLabel,
                                   name_postfix: str):
        """ create the dimension line properties from the parameter values

        Args:
            build_ele:    building element with the parameter properties
            label:        reinforcement label
            name_postfix: postfix of the parameter names
        """

        if build_ele.get_existing_property(f"SetVisibleBars{name_postfix}").value:
            visible_bars = build_ele.get_existing_property(f"VisibleBars{name_postfix}").value

            label.VisibleBars = AllplanUtil.VecIntList([int(item) for item in visible_bars.split(',')])

        if build_ele.get_existing_property(f"SetLabelOffset{name_postfix}").value:
            label.LabelOffset = build_ele.get_existing_property(f"LabelOffset{name_postfix}").value
        else:
            label.LabelOffset = AllplanGeo.Vector2D()

        if build_ele.get_existing_property(f"SetAdditionalText{name_postfix}").value:
            label.AdditionalText = build_ele.get_existing_property(f"AdditionalText{name_postfix}").value
        else:
            label.AdditionalText = ""

        label.ShowAllBars(build_ele.get_existing_property(f"ShowAllBars{name_postfix}").value)

        if build_ele.get_existing_property(f"ShowTextPointer{name_postfix}").value:
            label.ShowTextPointer          = build_ele.get_existing_property(f"ShowTextPointer{name_postfix}").value
            label.ShowTextPointerEndSymbol = build_ele.get_existing_property(f"ShowTextPointerEndSymbol{name_postfix}").value
        else:
            label.ShowTextPointer = False

```

</details>