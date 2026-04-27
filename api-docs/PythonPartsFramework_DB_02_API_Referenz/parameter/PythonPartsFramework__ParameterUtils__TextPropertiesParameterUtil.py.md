---
title: "TextPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\TextPropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TextPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\TextPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the text properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `Utils.TextAlignmentUtil`

## Klassen

### `TextPropertiesParameterUtil`

implementation of the text properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_text_properties` | `build_ele: BuildingElement, name_postfix: str` | `AllplanBasisEle.TextProperties` | create the text properties from the parameter values  Args:     build_ele:    building element with the parameter properties     name_postfix: postfix of the parameter names  Returns:     created text properties |
| `set_parameter_values` | `build_ele: BuildingElement, text_prop: AllplanBasisEle.TextProperties, name_postfix: str` | `None` | get the parameter values from the text properties  Args:     build_ele:    building element with the parameter properties     text_prop:    text properties     name_postfix: post fix of the parameter names |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the text properties parameter utilities
"""

import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Geometry as AllplanGeo

from BuildingElement import BuildingElement

from Utils.TextAlignmentUtil import TextAlignmentUtil

class TextPropertiesParameterUtil():
    """ implementation of the text properties parameter utilities
    """

    @staticmethod
    def create_text_properties(build_ele   : BuildingElement,
                               name_postfix: str) -> AllplanBasisEle.TextProperties:
        """ create the text properties from the parameter values

        Args:
            build_ele:    building element with the parameter properties
            name_postfix: postfix of the parameter names

        Returns:
            created text properties
        """

        text_prop = AllplanBasisEle.TextProperties()

        text_prop.HasTextFrame = build_ele.get_existing_property(f"HasTextFrame{name_postfix}").value

        if build_ele.get_existing_property(f"HasTextFrame{name_postfix}").value:
            text_prop.TextFramePen    = build_ele.get_existing_property(f"FramePen{name_postfix}").value
            text_prop.TextFrameStroke = build_ele.get_existing_property(f"FrameStroke{name_postfix}").value
            text_prop.TextFrameColor  = build_ele.get_existing_property(f"FrameColor{name_postfix}").value

        text_prop.Height           = build_ele.get_existing_property(f"TextHeight{name_postfix}").value
        text_prop.Width            = build_ele.get_existing_property(f"TextWidth{name_postfix}").value
        text_prop.Font             = build_ele.get_existing_property(f"Font{name_postfix}").value
        text_prop.FontStyles       = build_ele.get_existing_property(f"FontStyles{name_postfix}").value
        text_prop.FontAngle        = AllplanGeo.Angle.FromDeg(build_ele.get_existing_property(f"FontAngle{name_postfix}").value)
        text_prop.ColumnSlopeAngle = AllplanGeo.Angle.FromDeg(build_ele.get_existing_property(f"ColumnSlopeAngle{name_postfix}").value)
        text_prop.TextAngle        = AllplanGeo.Angle.FromDeg(build_ele.get_existing_property(f"TextAngle{name_postfix}").value)
        text_prop.Alignment        = TextAlignmentUtil.get_text_alignment_from_ref_point_button_index( \
                                                       build_ele.get_existing_property(f"Alignment{name_postfix}").value)

        text_prop.HasTransparentBackground = not build_ele.get_existing_property(f"BackgroundFillOfViewport{name_postfix}").value
        text_prop.HasBackgroundColor       = build_ele.get_existing_property(f"HasBackgroundColor{name_postfix}").value

        if build_ele.get_existing_property(f"HasBackgroundColor{name_postfix}").value:
            text_prop.BackgroundColor = build_ele.get_existing_property(f"BackgroundColor{name_postfix}").value

        text_prop.LineFeed         = build_ele.get_existing_property(f"LineFeed{name_postfix}").value
        text_prop.WrappedText      = build_ele.get_existing_property(f"WrappedText{name_postfix}").value
        text_prop.IsScaleDependent = build_ele.get_existing_property(f"IsScaleDependent{name_postfix}").value

        text_prop.Type      = AllplanBasisEle.TextType.eNormalText
        text_prop.Expansion = 1

        return text_prop

    @staticmethod
    def set_parameter_values(build_ele   : BuildingElement,
                             text_prop   : AllplanBasisEle.TextProperties,
                             name_postfix: str):
        """ get the parameter values from the text properties

        Args:
            build_ele:    building element with the parameter properties
            text_prop:    text properties
            name_postfix: post fix of the parameter names
        """

        build_ele.get_existing_property(f"HasTextFrame{name_postfix}").value = text_prop.HasTextFrame

        build_ele.get_existing_property(f"FramePen{name_postfix}").value    = text_prop.TextFramePen
        build_ele.get_existing_property(f"FrameStroke{name_postfix}").value = text_prop.TextFrameStroke
        build_ele.get_existing_property(f"FrameColor{name_postfix}").value  = text_prop.TextFrameColor

        build_ele.get_existing_property(f"TextHeight{name_postfix}").value = text_prop.Height
        build_ele.get_existing_property(f"TextWidth{name_postfix}").value  = text_prop.Width
        build_ele.get_existing_property(f"Font{name_postfix}").value       = text_prop.Font
        build_ele.get_existing_property(f"FontStyles{name_postfix}").value = text_prop.FontStyles

        build_ele.get_existing_property(f"FontAngle{name_postfix}").value = text_prop.FontAngle.Deg
        build_ele.get_existing_property(f"ColumnSlopeAngle{name_postfix}").value = text_prop.ColumnSlopeAngle.Deg
        build_ele.get_existing_property(f"TextAngle{name_postfix}").value = text_prop.TextAngle.Deg
        build_ele.get_existing_property(f"Alignment{name_postfix}").value = \
                                        TextAlignmentUtil.get_ref_point_button_index_from_text_alignment(text_prop.Alignment)

        build_ele.get_existing_property(f"BackgroundFillOfViewport{name_postfix}").value = not text_prop.HasTransparentBackground
        build_ele.get_existing_property(f"HasBackgroundColor{name_postfix}").value       = text_prop.HasBackgroundColor

        build_ele.get_existing_property(f"HasBackgroundColor{name_postfix}").value = text_prop.HasBackgroundColor
        build_ele.get_existing_property(f"BackgroundColor{name_postfix}").value    = text_prop.BackgroundColor

        build_ele.get_existing_property(f"LineFeed{name_postfix}").value         = text_prop.LineFeed
        build_ele.get_existing_property(f"WrappedText{name_postfix}").value      = text_prop.WrappedText
        build_ele.get_existing_property(f"IsScaleDependent{name_postfix}").value = text_prop.IsScaleDependent

```

</details>