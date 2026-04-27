---
title: "TextAlignmentUtil"
source: "PythonPartsFramework\Utils\TextAlignmentUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TextAlignmentUtil

> **Pfad:** `PythonPartsFramework\Utils\TextAlignmentUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

Implementation of the text alignment utilities

## Abhängigkeiten

- `NemAll_Python_BasisElements`
- `NemAll_Python_Palette`
- `TextReferencePointPosition`
- `__future__`
- `typing`

## Klassen

### `TextAlignmentUtil`

Implementation of the text alignment utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_text_alignment_from_text_point_position` | `ref_point_position: TextReferencePointPosition` | `AllplanBasisEle.TextAlignment` | get the text alignment from the text point position  Args:     ref_point_position: ref point position  Returns:     text alignment |
| `get_text_alignment_from_ref_point_button_index` | `ref_point_button_index: AllplanPalette.RefPointPosition` | `AllplanBasisEle.TextAlignment` | get the text alignment from the text point position  Args:     ref_point_button_index: ref point button index  Returns:     text alignment |
| `get_ref_point_button_index_from_text_alignment` | `text_align: AllplanBasisEle.TextAlignment` | `int` | get the text point position from the text alignment  Args:     text_align: text alignment  Returns:     reference point button index |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the text alignment utilities
"""

from __future__ import annotations

from typing import cast

import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Palette as AllplanPalette

from .TextReferencePointPosition import TextReferencePointPosition

class TextAlignmentUtil():
    """ Implementation of the text alignment utilities
    """

    @staticmethod
    def get_text_alignment_from_text_point_position(ref_point_position: TextReferencePointPosition) -> AllplanBasisEle.TextAlignment:
        """ get the text alignment from the text point position

        Args:
            ref_point_position: ref point position

        Returns:
            text alignment
        """

        return {TextReferencePointPosition.BOTTOM_LEFT : AllplanBasisEle.TextAlignment.eLeftBottom,
                TextReferencePointPosition.BOTTOM_CENTER : AllplanBasisEle.TextAlignment.eMiddleBottom,
                TextReferencePointPosition.BOTTOM_RIGHT : AllplanBasisEle.TextAlignment.eRightBottom,
                TextReferencePointPosition.CENTER_LEFT : AllplanBasisEle.TextAlignment.eLeftMiddle,
                TextReferencePointPosition.CENTER_CENTER : AllplanBasisEle.TextAlignment.eMiddleMiddle,
                TextReferencePointPosition.CENTER_RIGHT : AllplanBasisEle.TextAlignment.eRightMiddle,
                TextReferencePointPosition.TOP_LEFT : AllplanBasisEle.TextAlignment.eLeftTop,
                TextReferencePointPosition.TOP_CENTER : AllplanBasisEle.TextAlignment.eMiddleTop,
                TextReferencePointPosition.TOP_RIGHT : AllplanBasisEle.TextAlignment.eRightTop} \
               [cast(TextReferencePointPosition, ref_point_position)]


    @staticmethod
    def get_text_alignment_from_ref_point_button_index(ref_point_button_index: AllplanPalette.RefPointPosition) \
                                                       -> AllplanBasisEle.TextAlignment:
        """ get the text alignment from the text point position

        Args:
            ref_point_button_index: ref point button index

        Returns:
            text alignment
        """

        return {AllplanPalette.RefPointPosition.eBottomLeft  : AllplanBasisEle.TextAlignment.eLeftBottom,
                AllplanPalette.RefPointPosition.eBottomCenter: AllplanBasisEle.TextAlignment.eMiddleBottom,
                AllplanPalette.RefPointPosition.eBottomRight : AllplanBasisEle.TextAlignment.eRightBottom,
                AllplanPalette.RefPointPosition.eCenterLeft  : AllplanBasisEle.TextAlignment.eLeftMiddle,
                AllplanPalette.RefPointPosition.eCenterCenter: AllplanBasisEle.TextAlignment.eMiddleMiddle,
                AllplanPalette.RefPointPosition.eCenterRight : AllplanBasisEle.TextAlignment.eRightMiddle,
                AllplanPalette.RefPointPosition.eTopLeft     : AllplanBasisEle.TextAlignment.eLeftTop,
                AllplanPalette.RefPointPosition.eTopCenter   : AllplanBasisEle.TextAlignment.eMiddleTop,
                AllplanPalette.RefPointPosition.eTopRight    : AllplanBasisEle.TextAlignment.eRightTop} [ref_point_button_index]


    @staticmethod
    def get_ref_point_button_index_from_text_alignment(text_align: AllplanBasisEle.TextAlignment) -> int:
        """ get the text point position from the text alignment

        Args:
            text_align: text alignment

        Returns:
            reference point button index
        """

        return {AllplanBasisEle.TextAlignment.eLeftBottom: 7,
                AllplanBasisEle.TextAlignment.eMiddleBottom: 8,
                AllplanBasisEle.TextAlignment.eRightBottom: 9,
                AllplanBasisEle.TextAlignment.eLeftMiddle: 4,
                AllplanBasisEle.TextAlignment.eMiddleMiddle: 5,
                AllplanBasisEle.TextAlignment.eRightMiddle: 6,
                AllplanBasisEle.TextAlignment.eLeftTop: 1,
                AllplanBasisEle.TextAlignment.eMiddleTop: 2,
                AllplanBasisEle.TextAlignment.eRightTop: 3} [text_align]

```

</details>