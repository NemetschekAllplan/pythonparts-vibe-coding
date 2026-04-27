---
title: "Text3DUtil"
source: "PythonPartsFramework\Utils\Text3DUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# Text3DUtil

> **Pfad:** `PythonPartsFramework\Utils\Text3DUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

Implementation of the functions for the 3D text

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `Utils.TextReferencePointPosition`
- `collections`
- `typing`

## Klassen

### `Text3DUtil`

Implementation of the functions for the 3D text

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | - |
| `__getattr__` | `self, name` | `None` | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Implementation of the functions for the 3D text
"""

# pylint: disable=invalid-name

from typing import List

from collections import namedtuple

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_AllplanSettings as AllplanSettings

from Utils.TextReferencePointPosition import TextReferencePointPosition

class Text3DUtil:
    """
    Implementation of the functions for the 3D text
    """

    CharData = namedtuple("CharData", ["width", "height", "bsplines"])


    class __Text3DUtil:
        """
        Implementation of the functions for the 3D text
        """

        def __init__(self):
            """ read the data """

            file_name = AllplanSettings.AllplanPaths.GetPythonPartsEtcPath() + r"PythonPartsFramework\GeneralScripts\Fonts\Arial.dat"

            self.chr_dict = {}

            with open(file_name, 'r', encoding = "utf-8") as file:
                for line in file.readlines():
                    char, width, height, polylines = eval("(" + line + ")")

                    bspline_list = []

                    for polyline in polylines:
                        bspline_pnt = AllplanGeo.Point3DList()

                        for pnt in polyline:
                            bspline_pnt.append(AllplanGeo.Point3D(pnt[0], pnt[1], 0))

                        bspline_list.append(AllplanGeo.BSpline3D.CreateBSpline(bspline_pnt, 2, False))

                    self.chr_dict[char] = Text3DUtil.CharData(width, height, bspline_list)


        def get_bsplines(self,
                         pnt        : AllplanGeo.Point3D,
                         text       : str,
                         ref_pnt_pos: TextReferencePointPosition,
                         height     : float,
                         angle      : AllplanGeo.Angle) -> List[AllplanGeo.BSpline3D] :
            """ get the BSplines of the text

            Args:
                pnt:              reference point
                text:             text
                ref_pnt_pos:      point position of the reference point
                height:           height
                angle:            rotation angle

            Returns:
                list with the created BSpline3D
            """

            #----------------- get the width and height

            text_height = 0
            text_width  = 0

            for char in text:
                data = self.chr_dict[char]

                text_height = max(text_height, data.height)
                text_width += data.width


            #----------------- get the transformation matrix

            move_vec = AllplanGeo.Vector3D(pnt)

            bsplines = []

            trans_mat = AllplanGeo.Matrix3D()

            fac = height / text_height if height > 0 else 1 / abs(height)

            trans_mat.SetScaling(fac, fac, 0)

            x_refpnt = 0
            y_refpnt = 0

            if ref_pnt_pos in [TextReferencePointPosition.BOTTOM_CENTER, TextReferencePointPosition.CENTER_CENTER,
                               TextReferencePointPosition.TOP_CENTER]:
                x_refpnt = -text_width / 2

            elif ref_pnt_pos in [TextReferencePointPosition.BOTTOM_RIGHT, TextReferencePointPosition.CENTER_RIGHT,
                                 TextReferencePointPosition.TOP_RIGHT]:
                x_refpnt = -text_width

            if ref_pnt_pos in [TextReferencePointPosition.CENTER_CENTER, TextReferencePointPosition.CENTER_CENTER,
                               TextReferencePointPosition.CENTER_RIGHT]:
                y_refpnt = -text_height / 2

            elif ref_pnt_pos in [TextReferencePointPosition.TOP_LEFT, TextReferencePointPosition.TOP_CENTER,
                                 TextReferencePointPosition.TOP_RIGHT]:
                y_refpnt = -text_height

            trans_mat.Translate(AllplanGeo.Vector3D(x_refpnt * fac, y_refpnt * fac, 0))
            trans_mat.Rotation(AllplanGeo.Line3D(0, 0, 0, 0, 0, 1000), angle)


            #----------------- get the transformed BSplines

            for char in text:
                data = self.chr_dict[char]

                for bspline in data[2]:
                    bsplines.append(AllplanGeo.Move(AllplanGeo.Transform(bspline, trans_mat), move_vec))

                trans_mat.Translate(AllplanGeo.Transform(AllplanGeo.Vector3D(data.width, 0, 0), trans_mat))

            return bsplines


    #----------------- access to the internal implementation

    instance = None

    def __init__(self):
        if not Text3DUtil.instance:
            Text3DUtil.instance = Text3DUtil.__Text3DUtil()

    def __getattr__(self, name):
        return getattr(self.instance, name)

```

</details>