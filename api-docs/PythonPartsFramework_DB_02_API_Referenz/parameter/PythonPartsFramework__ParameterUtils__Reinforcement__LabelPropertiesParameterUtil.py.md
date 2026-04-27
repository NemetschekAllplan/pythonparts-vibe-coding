---
title: "LabelPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\Reinforcement\LabelPropertiesParameterUtil.py"
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


# LabelPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\Reinforcement\LabelPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `parameter`, `utility`

## Übersicht

implementation of the label properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_Reinforcement`

## Klassen

### `LabelPropertiesParameterUtil`

implementation of the label properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_label_properties` | `build_ele: BuildingElement, name_postfix: str` | `AllplanReinf.ReinforcementLabelProperties` | create the label properties from the parameter values  Args:     build_ele:    building element with the parameter properties     name_postfix: postfix of the parameter names  Returns:     created label properties |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the label properties parameter utilities
"""

import NemAll_Python_Reinforcement as AllplanReinf

from BuildingElement import BuildingElement

class LabelPropertiesParameterUtil():
    """ implementation of the label properties parameter utilities
    """

    @staticmethod
    def create_label_properties(build_ele   : BuildingElement,
                                name_postfix: str) -> AllplanReinf.ReinforcementLabelProperties:
        """ create the label properties from the parameter values

        Args:
            build_ele:    building element with the parameter properties
            name_postfix: postfix of the parameter names

        Returns:
            created label properties
        """

        label_props = AllplanReinf.ReinforcementLabelProperties()

        label_props.ShowPositionNumber = build_ele.get_existing_property(f"ShowPositionNumber{name_postfix}").value
        label_props.ShowBarDiameter    = build_ele.get_existing_property(f"ShowBarDiameter{name_postfix}").value
        label_props.ShowBarDistance    = build_ele.get_existing_property(f"ShowBarDistance{name_postfix}").value
        label_props.ShowBarCount       = build_ele.get_existing_property(f"ShowBarCount{name_postfix}").value
        label_props.ShowBendingShape   = build_ele.get_existing_property(f"ShowBendingShape{name_postfix}").value
        label_props.ShowBarPlace       = build_ele.get_existing_property(f"ShowBarPlace{name_postfix}").value
        label_props.ShowBarLength      = build_ele.get_existing_property(f"ShowBarLength{name_postfix}").value
        label_props.ShowSteelGrade     = build_ele.get_existing_property(f"ShowSteelGrade{name_postfix}").value
        label_props.ShowPositionAtEnd  = build_ele.get_existing_property(f"ShowPositionAtEnd{name_postfix}").value
        label_props.ShowTwoLineText    = build_ele.get_existing_property(f"ShowTwoLineText{name_postfix}").value

        return label_props

```

</details>