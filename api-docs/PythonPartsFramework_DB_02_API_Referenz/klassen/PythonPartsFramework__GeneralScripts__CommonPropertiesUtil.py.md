---
title: "CommonPropertiesUtil"
source: "PythonPartsFramework\GeneralScripts\CommonPropertiesUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# CommonPropertiesUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\CommonPropertiesUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the common properties utilities

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `ParameterProperty`
- `Utils`
- `__future__`
- `typing`

## Klassen

### `CommonPropertiesUtil`

implementation of the common properties utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `assing_by_layer_check` | `com_prop: AllplanBaseEle.CommonProperties, color: ParameterProperty, color_by_layer: ParameterProperty, pen: ParameterProperty, pen_by_layer: ParameterProperty, stroke: ParameterProperty, stroke_by_layer: ParameterProperty, layer: ParameterProperty` | `None` | assign the values by from layer check  Args:     com_prop:        common properties     color:           color     color_by_layer:  color by layer     pen:             pen     pen_by_layer:    pen by layer     stroke:          stroke     stroke_by_layer: stroke by layer     layer:           layer |
| `update_by_layer` | `com_prop: AllplanBaseEle.CommonProperties` | `bool` | Update the common properties by the layer flag  Args:     com_prop: common properties  Returns:     update state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the common properties utilities
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import NemAll_Python_BaseElements as AllplanBaseEle

from Utils import FormatUtil

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty

class CommonPropertiesUtil():
    """ implementation of the common properties utilities
    """

    @staticmethod
    def assing_by_layer_check(com_prop       : AllplanBaseEle.CommonProperties,
                              color          : ParameterProperty,
                              color_by_layer : ParameterProperty,
                              pen            : ParameterProperty,
                              pen_by_layer   : ParameterProperty,
                              stroke         : ParameterProperty,
                              stroke_by_layer: ParameterProperty,
                              layer          : ParameterProperty):
        """ assign the values by from layer check

        Args:
            com_prop:        common properties
            color:           color
            color_by_layer:  color by layer
            pen:             pen
            pen_by_layer:    pen by layer
            stroke:          stroke
            stroke_by_layer: stroke by layer
            layer:           layer
        """

        com_prop.Color         = color.value
        com_prop.Pen           = pen.value
        com_prop.Stroke        = stroke.value
        com_prop.ColorByLayer  = color_by_layer.value
        com_prop.PenByLayer    = pen_by_layer.value
        com_prop.StrokeByLayer = stroke_by_layer.value
        com_prop.Layer         = layer.value

        CommonPropertiesUtil.update_by_layer(com_prop)

        color.value  = com_prop.Color
        pen.value    = com_prop.Pen
        stroke.value = com_prop.Stroke


    @staticmethod
    def update_by_layer(com_prop: AllplanBaseEle.CommonProperties) -> bool:
        """ Update the common properties by the layer flag

        Args:
            com_prop: common properties

        Returns:
            update state
        """

        if com_prop.Layer == 0:
            return False

        color  = com_prop.Color
        pen    = com_prop.Pen
        stroke = com_prop.Stroke

        com_prop.Color, com_prop.Pen, com_prop.Stroke = \
            FormatUtil.update_by_layer(com_prop.Color, com_prop.ColorByLayer,
                                       com_prop.Pen, com_prop.PenByLayer,
                                       com_prop.Stroke, com_prop.StrokeByLayer,
                                       com_prop.Layer)

        return color  != com_prop.Color   or \
               pen    != com_prop.Pen     or \
               stroke != com_prop.Stroke

```

</details>