---
title: "ViewCode"
source: "PythonPartsFramework\GeneralScripts\PythonPart\ViewCode.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# ViewCode

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPart\ViewCode.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the PythonPart

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `View`
- `__future__`

## Klassen

### `ViewCode`

Definition of a code view class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, hash_value: str` | `None` | Initialization of code view class  Args:     hash_value: hash value |
| `create` | `self` | `AllplanBasisEle.MacroSlideElement` | Create code view  Returns:     macro slide element |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart
"""
from __future__ import annotations

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle

from .View import View

class ViewCode(View):
    """ Definition of a code view class
    """

    def __init__(self, hash_value: str):
        """ Initialization of code view class

        Args:
            hash_value: hash value
        """

        self._hash_value = hash_value

        super().__init__(AllplanBasisEle.MacroSlideType.eCode,
                         False, False, 0, 9999, [])


    def create(self) -> AllplanBasisEle.MacroSlideElement:
        """ Create code view

        Returns:
            macro slide element
        """

        slide_props                 = AllplanBasisEle.MacroSlideProperties()
        slide_props.VisibilityGeo2D = super().visibility2d
        slide_props.VisibilityGeo3D = super().visibility3d
        slide_props.Type            = super().viewtype
        slide_props.StartScaleRange = super().start_scale
        slide_props.EndScaleRange   = super().end_scale

        hash_attr      = AllplanBaseEle.AttributeString(AllplanBaseEle.ATTRNR_HASH, self._hash_value)
        attr_set       = AllplanBaseEle.AttributeSet([hash_attr])
        attributes     = AllplanBaseEle.Attributes([attr_set])
        attr_container = AllplanBasisEle.AttributeContainer(attributes)

        return AllplanBasisEle.MacroSlideElement(slide_props, [attr_container])

```

</details>