---
title: "TextElementUtil"
source: "PythonPartsFramework\Utils\General\TextElementUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TextElementUtil

> **Pfad:** `PythonPartsFramework\Utils\General\TextElementUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the TextElementUtil class

- create text properties
- set text properties
- add text element to the model element list

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `TypeCollections.ModelEleList`

## Klassen

### `TextElementUtil`

implementation of the TextElementUtil class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `create_text_properties` | `self, font_name: str | int, font_size: float, alignment: AllplanBasisEle.TextAlignment` | `None` | create text properties  Args:     font_name: font name     font_size: font size     alignment: alignment of the text |
| `set_properties` | `self, text_prop: AllplanBasisEle.TextProperties` | `None` | set the text properties  Args:     text_prop: text properties to set |
| `add_text` | `self, model_ele_list: ModelEleList, x_ref_pnt: float, y_ref_pnt: float, text: str` | `None` | add a text element to the model element list  Args:     model_ele_list: model element list     x_ref_pnt:      x coordinate reference point     y_ref_pnt:      y coordinate reference point     text:           text |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the TextElementUtil class

    - create text properties
    - set text properties
    - add text element to the model element list
"""

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Geometry as AllplanGeo

from TypeCollections.ModelEleList import ModelEleList

class TextElementUtil():
    """ implementation of the TextElementUtil class
    """

    def __init__(self):
        """ initialize
        """

        self.text_prop = AllplanBasisEle.TextProperties()


    def create_text_properties(self,
                               font_name: (str | int),
                               font_size: float,
                               alignment: AllplanBasisEle.TextAlignment):
        """ create text properties

        Args:
            font_name: font name
            font_size: font size
            alignment: alignment of the text
        """

        self.text_prop = AllplanBasisEle.TextProperties()

        self.text_prop.Font      = AllplanSettings.FontProvider.Instance().GetFontID(font_name, True) if isinstance(font_name, str) else \
                                   font_name
        self.text_prop.Height    = font_size
        self.text_prop.Width     = font_size
        self.text_prop.Alignment = alignment


    def set_properties(self,
                       text_prop: AllplanBasisEle.TextProperties):
        """ set the text properties

        Args:
            text_prop: text properties to set
        """

        self.text_prop = text_prop


    def add_text(self,
                 model_ele_list: ModelEleList,
                 x_ref_pnt     : float,
                 y_ref_pnt     : float,
                 text          : str):
        """ add a text element to the model element list

        Args:
            model_ele_list: model element list
            x_ref_pnt:      x coordinate reference point
            y_ref_pnt:      y coordinate reference point
            text:           text
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        ref_pnt = AllplanGeo.Point2D(x_ref_pnt * length_fac, y_ref_pnt * length_fac)

        model_ele_list.append(AllplanBasisEle.TextElement(model_ele_list.get_common_properties(), self.text_prop, text, ref_pnt))

```

</details>