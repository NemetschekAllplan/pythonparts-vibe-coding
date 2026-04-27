---
title: "FilledAreaUtil"
source: "PythonPartsFramework\Utils\General\FilledAreaUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# FilledAreaUtil

> **Pfad:** `PythonPartsFramework\Utils\General\FilledAreaUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of FilledAreaUtil

- create default hatching, pattern, filling, face style, bitmap
- add hatching, pattern, filling, face style properties to the corresponding dictionary
- get hatching, pattern, filling, face style properties from the corresponding dictionary

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`

## Klassen

### `FilledAreaUtil`

implementation of FilledAreaUtil
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialization          |
| `add_hatching` | `self, hatching_id: str, hatching_prop: AllplanBasisEle.HatchingProperties` | `None` | add a hatching  Args:     hatching_id:   hatching ID     hatching_prop: hatching properties |
| `add_pattern` | `self, pattern_id: str, pattern_prop: AllplanBasisEle.PatternProperties` | `None` | add a pattern  Args:     pattern_id:   pattern ID     pattern_prop: pattern properties |
| `add_filling` | `self, filling_id: str, filling_prop: AllplanBasisEle.FillingProperties` | `None` | add a filling  Args:     filling_id:   filling ID     filling_prop: filling properties |
| `add_no_transition_filling` | `self, filling_id: str, color: AllplanBasisEle.ARGB | int, alpha: int=0` | `None` | create a no transition filling and add it to the filling dictionary  Args:     filling_id: filling ID     color:      color object or color ID     alpha:      alpha |
| `add_face_style` | `self, face_style_id: str, face_style_prop: AllplanBasisEle.FaceStyleProperties` | `None` | add a face style  Args:     face_style_id:   face style ID     face_style_prop: face style properties |
| `create_no_transition_filling` | `color: AllplanBasisEle.ARGB | int, alpha: int=0` | `AllplanBasisEle.FillingProperties` | create a no transition filling  Args:     color: color object or color ID     alpha: alpha  Returns:     filling properties with no transition |
| `create_default_bitmap` | `bitmap_name: str` | `AllplanBasisEle.BitmapAreaProperties` | create a default bitmap  Args:     bitmap_name: name of the bitmap file  Returns:     bitmap properties with default values |
| `create_default_hatching` | `hatching_id: int, bg_color: AllplanBasisEle.ARGB | int | None=None` | `AllplanBasisEle.HatchingProperties` | create a default hatching  Args:     hatching_id: hatching ID     bg_color:    background color object or color ID  Returns:     hatching properties with default values |
| `create_default_pattern` | `pattern_id: int, bg_color: AllplanBasisEle.ARGB | int | None=None` | `AllplanBasisEle.PatternProperties` | create a default pattern  Args:     pattern_id: pattern ID     bg_color:   background color object or color ID  Returns:     pattern properties with default values |
| `create_default_face_style` | `face_style_id: int` | `AllplanBasisEle.FaceStyleProperties` | create a default face style  Args:     face_style_id: face style ID  Returns:     face style properties with default values |
| `get_hatching` | `self, hatching_id: str` | `AllplanBasisEle.HatchingProperties | None` | get a hatching  Args:     hatching_id: hatching ID  Returns:     hatching properties or None |
| `get_pattern` | `self, pattern_id: str` | `AllplanBasisEle.PatternProperties | None` | get a pattern  Args:     pattern_id: pattern ID  Returns:     pattern properties or None |
| `get_filling` | `self, filling_id: str` | `AllplanBasisEle.FillingProperties | None` | get a filling  Args:     filling_id: filling ID  Returns:     filling properties or None |
| `get_face_style` | `self, face_style_id: str` | `AllplanBasisEle.FaceStyleProperties | None` | get a face style  Args:     face_style_id: face style ID  Returns:     face style properties or None |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of FilledAreaUtil

    - create default hatching, pattern, filling, face style, bitmap
    - add hatching, pattern, filling, face style properties to the corresponding dictionary
    - get hatching, pattern, filling, face style properties from the corresponding dictionary
"""

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle

class FilledAreaUtil():
    """ implementation of FilledAreaUtil
    """

    def __init__(self):
        """ initialization
        """

        self.hatching_dict   = dict[str, AllplanBasisEle.HatchingProperties]()
        self.pattern_dict    = dict[str, AllplanBasisEle.PatternProperties]()
        self.filling_dict    = dict[str, AllplanBasisEle.FillingProperties]()
        self.face_style_dict = dict[str, AllplanBasisEle.FaceStyleProperties]()


    def add_hatching(self,
                     hatching_id: str,
                     hatching_prop: AllplanBasisEle.HatchingProperties):
        """ add a hatching

        Args:
            hatching_id:   hatching ID
            hatching_prop: hatching properties
        """

        self.hatching_dict[hatching_id] = hatching_prop


    def add_pattern(self,
                    pattern_id: str,
                    pattern_prop: AllplanBasisEle.PatternProperties):
        """ add a pattern

        Args:
            pattern_id:   pattern ID
            pattern_prop: pattern properties
        """

        self.pattern_dict[pattern_id] = pattern_prop


    def add_filling(self,
                    filling_id: str,
                    filling_prop: AllplanBasisEle.FillingProperties):
        """ add a filling

        Args:
            filling_id:   filling ID
            filling_prop: filling properties
        """

        self.filling_dict[filling_id] = filling_prop


    def add_no_transition_filling(self,
                                  filling_id: str,
                                  color     : (AllplanBasisEle.ARGB | int),
                                  alpha     : int = 0):
        """ create a no transition filling and add it to the filling dictionary

        Args:
            filling_id: filling ID
            color:      color object or color ID
            alpha:      alpha
        """

        self.filling_dict[filling_id] = self.create_no_transition_filling(color, alpha)


    def add_face_style(self,
                       face_style_id: str,
                       face_style_prop: AllplanBasisEle.FaceStyleProperties):
        """ add a face style

        Args:
            face_style_id:   face style ID
            face_style_prop: face style properties
        """

        self.face_style_dict[face_style_id] = face_style_prop


    @staticmethod
    def create_no_transition_filling(color: (AllplanBasisEle.ARGB | int),
                                     alpha: int = 0) -> AllplanBasisEle.FillingProperties:
        """ create a no transition filling

        Args:
            color: color object or color ID
            alpha: alpha

        Returns:
            filling properties with no transition
        """

        filling_prop = AllplanBasisEle.FillingProperties()

        filling_prop.TranslationType  = AllplanBasisEle.TransitionType.eNoTransition
        filling_prop.FirstColor       = color if isinstance(color, AllplanBasisEle.ARGB) else AllplanBaseEle.GetColorById(color)
        filling_prop.FirstColor.Alpha = alpha

        return filling_prop


    @staticmethod
    def create_default_bitmap(bitmap_name: str) -> AllplanBasisEle.BitmapAreaProperties:
        """ create a default bitmap

        Args:
            bitmap_name: name of the bitmap file

        Returns:
            bitmap properties with default values
        """

        bitmap = AllplanBasisEle.BitmapAreaProperties()

        bitmap.BitmapName = bitmap_name

        return bitmap


    @staticmethod
    def create_default_hatching(hatching_id: int,
                                bg_color: (AllplanBasisEle.ARGB | int| None) = None) -> AllplanBasisEle.HatchingProperties:
        """ create a default hatching

        Args:
            hatching_id: hatching ID
            bg_color:    background color object or color ID

        Returns:
            hatching properties with default values
        """

        hatching = AllplanBasisEle.HatchingProperties()

        hatching.HatchID = hatching_id

        if bg_color is not None:
            hatching.BackgroundColor    = bg_color if isinstance(bg_color, AllplanBasisEle.ARGB) else AllplanBaseEle.GetColorById(bg_color)
            hatching.UseBackgroundColor = True

        return hatching


    @staticmethod
    def create_default_pattern(pattern_id: int,
                               bg_color: (AllplanBasisEle.ARGB | int| None) = None) -> AllplanBasisEle.PatternProperties:
        """ create a default pattern

        Args:
            pattern_id: pattern ID
            bg_color:   background color object or color ID

        Returns:
            pattern properties with default values
        """

        pattern = AllplanBasisEle.PatternProperties()

        pattern.PatternID = pattern_id

        if bg_color is not None:
            pattern.BackgroundColor    = bg_color if isinstance(bg_color, AllplanBasisEle.ARGB) else AllplanBaseEle.GetColorById(bg_color)
            pattern.UseBackgroundColor = True

        return pattern


    @staticmethod
    def create_default_face_style(face_style_id: int) -> AllplanBasisEle.FaceStyleProperties:
        """ create a default face style

        Args:
            face_style_id: face style ID

        Returns:
            face style properties with default values
        """

        face_style = AllplanBasisEle.FaceStyleProperties()

        face_style.FaceStyleID = face_style_id

        return face_style


    def get_hatching(self,
                     hatching_id: str) -> AllplanBasisEle.HatchingProperties | None:
        """ get a hatching

        Args:
            hatching_id: hatching ID

        Returns:
            hatching properties or None
        """

        return self.hatching_dict.get(hatching_id, None)


    def get_pattern(self,
                    pattern_id: str) -> AllplanBasisEle.PatternProperties | None:
        """ get a pattern

        Args:
            pattern_id: pattern ID

        Returns:
            pattern properties or None
        """

        return self.pattern_dict.get(pattern_id, None)


    def get_filling(self,
                    filling_id: str) -> AllplanBasisEle.FillingProperties | None:
        """ get a filling

        Args:
            filling_id: filling ID

        Returns:
            filling properties or None
        """

        return self.filling_dict.get(filling_id, None)


    def get_face_style(self,
                       face_style_id: str) -> AllplanBasisEle.FaceStyleProperties | None:
        """ get a face style

        Args:
            face_style_id: face style ID

        Returns:
            face style properties or None
        """

        return self.face_style_dict.get(face_style_id, None)

```

</details>