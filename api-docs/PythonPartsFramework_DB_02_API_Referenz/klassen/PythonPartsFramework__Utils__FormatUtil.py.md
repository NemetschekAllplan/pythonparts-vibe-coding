---
title: "FormatUtil"
source: "PythonPartsFramework\Utils\FormatUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# FormatUtil

> **Pfad:** `PythonPartsFramework\Utils\FormatUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

Script for FormatUtil

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `__future__`
- `codecs`
- `os`
- `typing`

## Klassen

### `FormatUtil`

Implementation of the format utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `init_by_global_properties` | `build_ele: BuildingElement` | `None` | initialize the values by global properties  Args:     build_ele: building element with the parameter properties |
| `init_list_by_global_properties` | `build_ele: BuildingElement` | `None` | initialize the values by global properties  Args:     build_ele: building element with the parameter properties |
| `update_by_layer` | `color: int, color_by_layer: bool, pen: int, pen_by_layer: bool, stroke: int, stroke_by_layer: bool, layer: int` | `tuple[int, int, int]` | Update the common properties by layer  Args:     color:           color     color_by_layer:  color by layer state     pen:             pen     pen_by_layer:    pen by layer state     stroke:          stroke     stroke_by_layer: stroke by layer state     layer:           layer  Returns:     color, pen, stroke |
| `update_build_ele_single_values` | `build_ele: BuildingElement` | `None` | Update the single values inside the building element      return Property is updated: True/False  Args:     build_ele: building element with the parameter properties |
| `update_build_ele_list_values` | `build_ele: BuildingElement` | `None` | Update the list values inside the building element      return Property is updated: True/False  Args:     build_ele: building element with the parameter properties |
| `get_layer_pen_stroke_color` | `layer: int | str` | `tuple[bool, int, int, int]` | get the pen, stroke and color from the layer  Args:     layer: number of the layer  Returns:     tuple(pen, stroke, color) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for FormatUtil
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import codecs
import os

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_AllplanSettings as AllplanSettings

if TYPE_CHECKING:
    from BuildingElement import BuildingElement

class FormatUtil():
    """ Implementation of the format utilities
    """

    @staticmethod
    def init_by_global_properties(build_ele: BuildingElement):
        """ initialize the values by global properties

        Args:
            build_ele: building element with the parameter properties
        """

        com_prop = AllplanBaseEle.CommonProperties()

        com_prop.GetGlobalProperties()

        if build_ele.Layer.value == -2:
            build_ele.Layer.value = com_prop.Layer

        if build_ele.Pen.value == -2:
            build_ele.Pen.value = com_prop.Pen

            if not build_ele.PenByLayer.value:
                build_ele.PenByLayer.value = com_prop.PenByLayer

        if build_ele.Stroke.value == -2:
            build_ele.Stroke.value = com_prop.Stroke

            if not build_ele.StrokeByLayer.value:
                build_ele.StrokeByLayer.value = com_prop.StrokeByLayer

        if build_ele.Color.value == -2:
            build_ele.Color.value = com_prop.Color

            if not build_ele.ColorByLayer.value:
                build_ele.ColorByLayer.value = com_prop.ColorByLayer


        #----------------- check the by layer state

        props = FormatUtil.update_by_layer(build_ele.Color.value, build_ele.ColorByLayer.value,
                                           build_ele.Pen.value, build_ele.PenByLayer.value,
                                           build_ele.Stroke.value, build_ele.StrokeByLayer.value,
                                           build_ele.Layer.value)

        build_ele.Color.value  = props[0]
        build_ele.Pen.value    = props[1]
        build_ele.Stroke.value = props[2]


    @staticmethod
    def init_list_by_global_properties(build_ele: BuildingElement):
        """ initialize the values by global properties

        Args:
            build_ele: building element with the parameter properties
        """

        com_prop = AllplanBaseEle.CommonProperties()
        com_prop.GetGlobalProperties()

        for index, _ in enumerate(build_ele.Color.value):
            if build_ele.Layer.value[index] == -2:
                build_ele.Layer.value[index] = com_prop.Layer

            if build_ele.Pen.value[index] == -2:
                build_ele.Pen.value[index] = com_prop.Pen

                if not build_ele.PenByLayer.value[index]:
                    build_ele.PenByLayer.value[index] = com_prop.PenByLayer

            if build_ele.Stroke.value[index] == -2:
                build_ele.Stroke.value[index] = com_prop.Stroke

                if not build_ele.StrokeByLayer.value[index]:
                    build_ele.StrokeByLayer.value[index] = com_prop.StrokeByLayer

            if build_ele.Color.value[index] == -2:
                build_ele.Color.value[index] = com_prop.Color

                if not build_ele.ColorByLayer.value[index]:
                    build_ele.ColorByLayer.value[index] = com_prop.ColorByLayer


            #----------------- check the by layer state

            props = FormatUtil.update_by_layer(build_ele.Color.value[index], build_ele.ColorByLayer.value[index],
                                               build_ele.Pen.value[index], build_ele.PenByLayer.value[index],
                                               build_ele.Stroke.value[index], build_ele.StrokeByLayer.value[index],
                                               build_ele.Layer.value[index])

            build_ele.Color.value[index]  = props[0]
            build_ele.Pen.value[index]    = props[1]
            build_ele.Stroke.value[index] = props[2]


    @staticmethod
    def update_by_layer(color          : int,
                        color_by_layer : bool,
                        pen            : int,
                        pen_by_layer   : bool,
                        stroke         : int,
                        stroke_by_layer: bool,
                        layer          : int) -> tuple[int, int, int]:
        """ Update the common properties by layer

        Args:
            color:           color
            color_by_layer:  color by layer state
            pen:             pen
            pen_by_layer:    pen by layer state
            stroke:          stroke
            stroke_by_layer: stroke by layer state
            layer:           layer

        Returns:
            color, pen, stroke
        """

        if not pen_by_layer and not stroke_by_layer and not color_by_layer:
            return color, pen, stroke


        #----------------- get the format properties by layer

        exist, layer_pen, layer_stroke, layer_color = FormatUtil.get_layer_pen_stroke_color(str(layer))

        if not exist:
            return color, pen, stroke

        if pen_by_layer:
            pen = layer_pen

        if stroke_by_layer:
            stroke = layer_stroke

        if color_by_layer:
            color = layer_color

        return color, pen, stroke


    @staticmethod
    def update_build_ele_single_values(build_ele: BuildingElement):
        """ Update the single values inside the building element

            return Property is updated: True/False

        Args:
            build_ele: building element with the parameter properties
        """

        color, pen, stroke = FormatUtil.update_by_layer(build_ele.Color.value, build_ele.ColorByLayer.value,
                                                        build_ele.Pen.value, build_ele.PenByLayer.value,
                                                        build_ele.Stroke.value, build_ele.StrokeByLayer.value,
                                                        build_ele.Layer.value)

        is_update = build_ele.Color.value  != color or \
                    build_ele.Pen.value    != pen   or \
                    build_ele.Stroke.value != stroke

        build_ele.Color.value  = color
        build_ele.Pen.value    = pen
        build_ele.Stroke.value = stroke

        return is_update


    @staticmethod
    def update_build_ele_list_values(build_ele: BuildingElement):
        """ Update the list values inside the building element

            return Property is updated: True/False

        Args:
            build_ele: building element with the parameter properties
        """

        is_update = False

        min_len = min([len(build_ele.Color.value),
         		       len(build_ele.ColorByLayer.value),
         			   len(build_ele.Pen.value),
         			   len(build_ele.PenByLayer.value),
         			   len(build_ele.Stroke.value),
         			   len(build_ele.StrokeByLayer.value),
         			   len(build_ele.Layer.value)])

        com_prop = AllplanBaseEle.CommonProperties()
        com_prop.GetGlobalProperties()

        for index in range(min_len):
            layer  = build_ele.Layer.value[index]
            color  = build_ele.Color.value[index]
            pen    = build_ele.Pen.value[index]
            stroke = build_ele.Stroke.value[index]

            if layer == -2:
                layer = com_prop.Layer

            if pen == -2:
                pen = com_prop.Pen

            if stroke == -2:
                stroke = com_prop.Stroke

            if color == -2:
                color = com_prop.Color

            color, pen, stroke = FormatUtil.update_by_layer(color,  build_ele.ColorByLayer.value[index],
                                                            pen,    build_ele.PenByLayer.value[index],
                                                            stroke, build_ele.StrokeByLayer.value[index],
                                                            layer)

            if not is_update:
                is_update = build_ele.Color.value[index]  != color or \
                            build_ele.Pen.value[index]    != pen   or \
                            build_ele.Stroke.value[index] != stroke

            build_ele.Layer.value[index]  = layer
            build_ele.Color.value[index]  = color
            build_ele.Pen.value[index]    = pen
            build_ele.Stroke.value[index] = stroke

        return is_update


    @staticmethod
    def get_layer_pen_stroke_color(layer: (int | str)) -> tuple[bool, int, int, int]:
        """ get the pen, stroke and color from the layer

        Args:
            layer: number of the layer

        Returns:
            tuple(pen, stroke, color)
        """

        layer = str(layer)

        etc = AllplanSettings.AllplanPaths.GetEtcPath()
        std = AllplanSettings.AllplanPaths.GetStdPath()

        if etc[-1] != "\\":
            etc = etc + "\\"

        file_name = etc + "layerbas.nem"

        if not os.path.exists(file_name):
            return True, 11, 9, 11

        with codecs.open(file_name, "r", "utf-16") as layer_file:
            for line in layer_file.readlines():
                if layer in line:
                    values = line.split("@")

                    return True, int(values[4]), int(values[5]), int(values[6])

            return False, 1, 1, 1

```

</details>