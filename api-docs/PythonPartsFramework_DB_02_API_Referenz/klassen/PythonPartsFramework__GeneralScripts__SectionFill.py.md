---
title: "SectionFill"
source: "PythonPartsFramework\GeneralScripts\SectionFill.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# SectionFill

> **Pfad:** `PythonPartsFramework\GeneralScripts\SectionFill.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the SectionFill class

The SectionFill class represents a surface element, shown when an element is cut through in a section view.

## Abhängigkeiten

- `NemAll_Python_ArchElements`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `TestHelper.PythonPartPylintDecorator`
- `TypeCollections.ModelEleList`
- `__future__`
- `enum`
- `ntpath`
- `os`

## Klassen

### `SectionFillType`

Enumeration with possible section element types

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `SectionFill`

Representation of a surface element, shown when an element is cut through in a section view

This class can be used to apply a filling, hatching, pattern, face style or bitmap to a ModelElement3D,
as in this case these properties are managed through ALLPLAN attributes.

Examples:
    To assign a hatching with ALLPLAN internal ID of 303 (reinforced concrete) to `model_ele_list` containing
    3d solids represented by ModelElement3D, use the following code:
    >>> hatching = SectionFill.as_hatching(303)
    >>> hatching.apply_on_model_elements(model_ele_list)

    To assign a bitmap to the same `model_ele_list`, use the following code:
    >>> bitmap = SectionFill.as_bitmap('C:/path/to/bitmap.jpg')
    >>> bitmap.apply_on_model_elements(model_ele_list)

    To create a SectionFill object from a parameter with ValueType of SurfaceElementProperties,
    use the following code:
    >>> surface_ele_props = build_ele.NameOfYourSurfaceElementPropertiesParameter.value
    >>> section_fill = SectionFill.from_surface_ele_properties(surface_ele_props)

    To change the type of the surface element, first set the type, then the number or bitmap path:
    >>> section_fill.type = SectionFillType.HATCHING
    >>> section_fill.number = 303

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, section_type: SectionFillType, number: int, bitmap_path: str='', background_color: int | None=None` | `None` | Initialize the surface element  Use dedicated methods like `as_hatching()`, `as_pattern()`, etc. rather than this constructor.  Args:     section_type:       Type of the surface element (filling, hatching, pattern, etc.)     number:             ALLPLAN Resource ID of the pattern/hatch/etc.     bitmap_path:        Absolute path to the file with a bitmap (image files like .jpg or .png are allowed)     background_color:   Color of the background (only for pattern or hatching) |
| `as_bitmap` | `cls, bitmap_path: str` | `SectionFill` | Initialize the surface element as a bitmap  Args:     bitmap_path: Path to the bitmap  Returns:     SectionFill object with bitmap type  Raises:     FileNotFoundError: If the bitmap file is not found |
| `as_hatching` | `cls, hatching_id: int, background_color: int | None=None` | `SectionFill` | Initialize the surface element as hatching  Args:     hatching_id: ID of the hatching     background_color: Optional background filling color  Returns:     SectionFill object with hatching type |
| `as_pattern` | `cls, pattern_id: int, background_color: int | None=None` | `SectionFill` | Initialize the surface element as pattern  Args:     pattern_id: ID of the pattern     background_color: Optional background filling color  Returns:     SectionFill object with pattern type |
| `as_filling` | `cls, filling_id: int` | `SectionFill` | Initialize the surface element as filling  Args:     filling_id: ID of the filling  Returns:     SectionFill object with filling type |
| `as_face_style` | `cls, face_style_id: int` | `SectionFill` | Initialize the surface element as face style  Args:     face_style_id: ID of the face style  Returns:     SectionFill object with face style type |
| `from_surface_ele_properties` | `cls, surface_ele_props: AllplanArchEle.SurfaceElementProperties` | `SectionFill` | Create a SectionFill object from SurfaceElementProperties  Args:     surface_ele_props: SurfaceElementProperties object  Returns:     SectionFill object |
| `__repr__` | `self` | `str` | Return a string representation of the object  Returns:     string representation |
| `type` | `self` | `SectionFillType` | Type of the surface element |
| `type` | `self, section_type: SectionFillType` | `None` | - |
| `number` | `self` | `int` | ALLPLAN Resource ID of the pattern/hatch/etc.  In case of FILLING, the ID of the ALLPLAN standard color.  Raises:     ValueError: If the fill type is BITMAP |
| `number` | `self, number: int` | `None` | - |
| `bitmap` | `self` | `str` | Absolute path to the file with a bitmap (image files like .jpg or .png are allowed)  Raises:     ValueError: If the type is other than BITMAP |
| `bitmap` | `self, bitmap_path: str` | `None` | - |
| `background_color` | `self` | `int | None` | Color of the background (only for pattern or hatching)  Raises:     ValueError: If the type is other than HATCHING or PATTERN |
| `background_color` | `self, color: int | None` | `None` | - |
| `set_type` | `self, section_type: SectionFillType` | `None` | Set the type of the surface element  Args:     section_type: filling type |
| `get_type` | `self` | `SectionFillType` | Get type  Returns:     type of section_fill |
| `set_number` | `self, number: int` | `None` | Set the ALLPLAN Resource ID of the pattern/hatch/etc.  Args:     number: ALLPLAN Resource ID of the pattern/hatch/etc. |
| `get_number` | `self` | `int` | Get ALLPLAN Resource ID of the pattern/hatch/etc.  Returns:     ALLPLAN Resource ID of the pattern/hatch/etc. |
| `set_bitmap` | `self, bitmap: str` | `None` | Set the absolute path to the file with a bitmap  Args:     bitmap: Absolute path to the file with a bitmap |
| `get_bitmap` | `self` | `str` | Get the bitmap  Returns:     Absolute path to the file with a bitmap |
| `apply_on_model_elements` | `self, elements: AllplanBasisEle.ModelElement3D | list[AllplanBasisEle.ModelElement3D] | ModelEleList` | `None` | Apply the section fill to the given ModelElement3D or list of them  Args:     elements: ModelElement3D or list of them to apply the section fill to |
| `_apply_on_model_element` | `self, elem: AllplanBasisEle.ModelElement3D` | `None` | Apply the section fill to the given element  Args:     elem: Element to apply the section fill to |
| `add_section_filling` | `elem: AllplanBasisEle.ModelElement3D, section_fill: SectionFill` | `None` | Add section filling to element  Args:     elem:         element to add section fill     section_fill: section fill |
| `add_section_filling_attribute` | `elem, section_fill, attr_list` | `None` | Add section filling and attributes to element  Args:     elem:         element to add section fill     section_fill: section fill     attr_list:    attribute list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the SectionFill class

The SectionFill class represents a surface element, shown when an element is cut through in a section view.
"""
from __future__ import annotations

import ntpath
import os

from enum import IntEnum

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle

from TestHelper.PythonPartPylintDecorator import PythonPartPylintDecorator
from TypeCollections.ModelEleList import ModelEleList

class SectionFillType(IntEnum):
    """Enumeration with possible section element types"""

    EMPTY = 0
    """No section element"""
    FILLING = 1
    """Single-color fill"""
    HATCHING = 2
    """Hatching"""
    PATTERN = 3
    """Pattern"""
    FACESTYLE = 4
    """Face style (aka style area)"""
    BITMAP = 5
    """Bitmap"""


class SectionFill():
    """Representation of a surface element, shown when an element is cut through in a section view

    This class can be used to apply a filling, hatching, pattern, face style or bitmap to a ModelElement3D,
    as in this case these properties are managed through ALLPLAN attributes.

    Examples:
        To assign a hatching with ALLPLAN internal ID of 303 (reinforced concrete) to `model_ele_list` containing
        3d solids represented by ModelElement3D, use the following code:
        >>> hatching = SectionFill.as_hatching(303)
        >>> hatching.apply_on_model_elements(model_ele_list)

        To assign a bitmap to the same `model_ele_list`, use the following code:
        >>> bitmap = SectionFill.as_bitmap('C:/path/to/bitmap.jpg')
        >>> bitmap.apply_on_model_elements(model_ele_list)

        To create a SectionFill object from a parameter with ValueType of SurfaceElementProperties,
        use the following code:
        >>> surface_ele_props = build_ele.NameOfYourSurfaceElementPropertiesParameter.value
        >>> section_fill = SectionFill.from_surface_ele_properties(surface_ele_props)

        To change the type of the surface element, first set the type, then the number or bitmap path:
        >>> section_fill.type = SectionFillType.HATCHING
        >>> section_fill.number = 303
    """

    def __init__(self,
                 section_type    : SectionFillType,
                 number          : int,
                 bitmap_path     : str = '',
                 background_color: int|None = None):
        """Initialize the surface element

        Use dedicated methods like `as_hatching()`, `as_pattern()`, etc. rather than this constructor.

        Args:
            section_type:       Type of the surface element (filling, hatching, pattern, etc.)
            number:             ALLPLAN Resource ID of the pattern/hatch/etc.
            bitmap_path:        Absolute path to the file with a bitmap (image files like .jpg or .png are allowed)
            background_color:   Color of the background (only for pattern or hatching)
        """

        self._type             = section_type
        self._number           = number if section_type != SectionFillType.BITMAP else 0
        self._bitmap           = bitmap_path if section_type == SectionFillType.BITMAP else ''
        self._background_color = background_color if section_type in [SectionFillType.HATCHING, SectionFillType.PATTERN] else None


    @classmethod
    def as_bitmap(cls,
                  bitmap_path: str) -> SectionFill:
        """Initialize the surface element as a bitmap

        Args:
            bitmap_path: Path to the bitmap

        Returns:
            SectionFill object with bitmap type

        Raises:
            FileNotFoundError: If the bitmap file is not found
        """

        if not os.path.exists(bitmap_path):
            raise FileNotFoundError(f"Bitmap file not found: {bitmap_path}")

        return cls(SectionFillType.BITMAP, 0, bitmap_path)


    @classmethod
    def as_hatching(cls,
                    hatching_id     : int,
                    background_color: int|None = None) -> SectionFill:
        """Initialize the surface element as hatching

        Args:
            hatching_id: ID of the hatching
            background_color: Optional background filling color

        Returns:
            SectionFill object with hatching type
        """
        return cls(SectionFillType.HATCHING, hatching_id, background_color=background_color)


    @classmethod
    def as_pattern(cls,
                   pattern_id      : int,
                   background_color: int|None = None) -> SectionFill:
        """Initialize the surface element as pattern

        Args:
            pattern_id: ID of the pattern
            background_color: Optional background filling color

        Returns:
            SectionFill object with pattern type
        """
        return cls(SectionFillType.PATTERN, pattern_id, background_color=background_color)


    @classmethod
    def as_filling(cls,
                   filling_id: int) -> SectionFill:
        """Initialize the surface element as filling

        Args:
            filling_id: ID of the filling

        Returns:
            SectionFill object with filling type
        """
        return cls(SectionFillType.FILLING, filling_id)


    @classmethod
    def as_face_style(cls,
                      face_style_id: int) -> SectionFill:
        """Initialize the surface element as face style

        Args:
            face_style_id: ID of the face style

        Returns:
            SectionFill object with face style type
        """
        return cls(SectionFillType.FACESTYLE, face_style_id)


    @classmethod
    def from_surface_ele_properties(cls,
                                    surface_ele_props: AllplanArchEle.SurfaceElementProperties) -> SectionFill:
        """Create a SectionFill object from SurfaceElementProperties

        Args:
            surface_ele_props: SurfaceElementProperties object

        Returns:
            SectionFill object
        """

        selected_types = [surface_ele_props.FillingSelected,
                          surface_ele_props.HatchSelected,
                          surface_ele_props.PatternSelected,
                          surface_ele_props.FaceStyleSelected,
                          surface_ele_props.BitmapSelected]

        resource_ids = [surface_ele_props.FillingID,
                        surface_ele_props.HatchID,
                        surface_ele_props.PatternID,
                        surface_ele_props.FaceStyleID,
                        0]

        selected_indices = [i for i, val in enumerate(selected_types) if val]

        if len(selected_indices) == 2:
            type_idx = selected_indices[-1]
            return cls(SectionFillType(type_idx + 1), resource_ids[type_idx], background_color=surface_ele_props.FillingID)

        if len(selected_indices) == 1:
            type_idx = selected_indices[0]
            return cls(SectionFillType(type_idx + 1), resource_ids[type_idx], surface_ele_props.BitmapID)

        return cls(SectionFillType.EMPTY, 0)


    def __repr__(self) -> str:
        """Return a string representation of the object

        Returns:
            string representation
        """
        return (
            f"{self.__class__.__name__}("
            f"type={self._type!r}, "
            f"number={self._number!r}, "
            f"bitmap={self._bitmap!r}, "
            f"background_color={self._background_color!r})"
        )


    @property
    def type(self) -> SectionFillType:
        """Type of the surface element"""
        return self._type


    @type.setter
    def type(self, section_type: SectionFillType):
        if not isinstance(section_type, SectionFillType):
            raise ValueError("Invalid type")
        self._type = section_type

        # Reset the properties irrelevant for the new type
        if section_type != SectionFillType.BITMAP:
            self._bitmap = ''

        if section_type not in [SectionFillType.HATCHING, SectionFillType.PATTERN]:
            self._background_color = None

        if section_type in [SectionFillType.BITMAP, SectionFillType.EMPTY]:
            self._number = 0


    @property
    def number(self) -> int:
        """ALLPLAN Resource ID of the pattern/hatch/etc.

        In case of FILLING, the ID of the ALLPLAN standard color.

        Raises:
            ValueError: If the fill type is BITMAP
        """
        return self._number


    @number.setter
    def number(self, number: int):
        if self.type == SectionFillType.BITMAP:
            raise ValueError('This object is of BITMAP type. First change the type to something else than BITMAP.')
        self._number = number


    @property
    def bitmap(self) -> str:
        """Absolute path to the file with a bitmap (image files like .jpg or .png are allowed)

        Raises:
            ValueError: If the type is other than BITMAP
        """
        return self._bitmap


    @bitmap.setter
    def bitmap(self, bitmap_path: str):
        self._type = SectionFillType.BITMAP
        self._number = 0
        self._bitmap = bitmap_path


    @property
    def background_color(self) -> int|None:
        """Color of the background (only for pattern or hatching)

        Raises:
            ValueError: If the type is other than HATCHING or PATTERN
        """
        return self._background_color


    @background_color.setter
    def background_color(self, color: int|None):
        if self.type not in [SectionFillType.HATCHING, SectionFillType.PATTERN]:
            raise ValueError('Background color can be set only for HATCHING or PATTERN type.')
        self._background_color = color


    def set_type(self, section_type: SectionFillType):
        """Set the type of the surface element

        Args:
            section_type: filling type
        """
        self.type = section_type


    def get_type(self) -> SectionFillType:
        """Get type

        Returns:
            type of section_fill
        """
        return self.type


    def set_number(self, number: int):
        """Set the ALLPLAN Resource ID of the pattern/hatch/etc.

        Args:
            number: ALLPLAN Resource ID of the pattern/hatch/etc.
        """
        self.number = number


    def get_number(self) -> int:
        """Get ALLPLAN Resource ID of the pattern/hatch/etc.

        Returns:
            ALLPLAN Resource ID of the pattern/hatch/etc.
        """
        return self.number


    def set_bitmap(self, bitmap: str):
        """Set the absolute path to the file with a bitmap

        Args:
            bitmap: Absolute path to the file with a bitmap
        """
        self.bitmap = bitmap


    def get_bitmap(self) -> str:
        """Get the bitmap

        Returns:
            Absolute path to the file with a bitmap
        """
        return self.bitmap


    def apply_on_model_elements(self, elements: AllplanBasisEle.ModelElement3D | list[AllplanBasisEle.ModelElement3D] | ModelEleList):
        """Apply the section fill to the given ModelElement3D or list of them

        Args:
            elements: ModelElement3D or list of them to apply the section fill to
        """

        if isinstance(elements, list):
            for elem in elements:
                self._apply_on_model_element(elem)
        else:
            self._apply_on_model_element(elements)


    def _apply_on_model_element(self, elem: AllplanBasisEle.ModelElement3D):
        """Apply the section fill to the given element

        Args:
            elem: Element to apply the section fill to
        """

        if not isinstance(elem, AllplanBasisEle.ModelElement3D):
            return

        try:
            attr_list = elem.Attributes.AttributeSets[0].Attributes # type: ignore
        except (AttributeError, KeyError):
            attr_list = []

        match self.type:
            case SectionFillType.EMPTY:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 0))

            case SectionFillType.FILLING:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 3))
                attr_list.append(AllplanBaseEle.AttributeInteger(252, self.number))

            case SectionFillType.HATCHING:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 2))
                attr_list.append(AllplanBaseEle.AttributeInteger(124, self.number))

                if self.background_color is not None:
                    attr_list.append(AllplanBaseEle.AttributeInteger(252, self.background_color))

            case SectionFillType.PATTERN:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 1))
                attr_list.append(AllplanBaseEle.AttributeInteger(126, self.number))
                if self.background_color is not None:
                    attr_list.append(AllplanBaseEle.AttributeInteger(252, self.background_color))

            case SectionFillType.FACESTYLE:
                attr_list.append(AllplanBaseEle.AttributeInteger(125, self.number))

            case SectionFillType.BITMAP:
                path, file = ntpath.split(self.bitmap)
                attr_list.append(AllplanBaseEle.AttributeString(333, path))
                attr_list.append(AllplanBaseEle.AttributeString(336, file))

        elem.SetAttributes(AllplanBaseEle.Attributes([AllplanBaseEle.AttributeSet(attr_list)]))


    @PythonPartPylintDecorator.deprecated(replace = " use apply_on_model_elements(...)")
    @staticmethod
    def add_section_filling(elem:         AllplanBasisEle.ModelElement3D,
                            section_fill: SectionFill):
        """Add section filling to element

        Args:
            elem:         element to add section fill
            section_fill: section fill
        """

        attr_list = []

        match section_fill.type:
            case SectionFillType.FILLING:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 3))
                attr_list.append(AllplanBaseEle.AttributeInteger(252, section_fill.number))

            case SectionFillType.HATCHING:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 2))
                attr_list.append(AllplanBaseEle.AttributeInteger(124, section_fill.number))

            case SectionFillType.PATTERN:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 1))
                attr_list.append(AllplanBaseEle.AttributeInteger(126, section_fill.number))

            case SectionFillType.FACESTYLE:
                attr_list.append(AllplanBaseEle.AttributeInteger(125, section_fill.number))

            case SectionFillType.BITMAP:
                path, file = ntpath.split(section_fill.bitmap)
                attr_list.append(AllplanBaseEle.AttributeString(333, path))
                attr_list.append(AllplanBaseEle.AttributeString(336, file))

        if len(attr_list)!= 0:
            attr_set_list = []
            attr_set_list.append(AllplanBaseEle.AttributeSet(attr_list))
            attributes = AllplanBaseEle.Attributes(attr_set_list)
            elem.SetAttributes(attributes)

    @PythonPartPylintDecorator.deprecated(replace = " use apply_on_model_elements(...)")
    @staticmethod
    def add_section_filling_attribute(elem, section_fill, attr_list):
        """Add section filling and attributes to element

        Args:
            elem:         element to add section fill
            section_fill: section fill
            attr_list:    attribute list
        """

        if section_fill:
            match section_fill.type:
                case SectionFillType.FILLING:
                    attr_list.append(AllplanBaseEle.AttributeInteger(118, 3))
                    attr_list.append(AllplanBaseEle.AttributeInteger(252, section_fill.number))

                case SectionFillType.HATCHING:
                    attr_list.append(AllplanBaseEle.AttributeInteger(118, 2))
                    attr_list.append(AllplanBaseEle.AttributeInteger(124, section_fill.number))

                case SectionFillType.PATTERN:
                    attr_list.append(AllplanBaseEle.AttributeInteger(118, 1))
                    attr_list.append(AllplanBaseEle.AttributeInteger(126, section_fill.number))

                case SectionFillType.FACESTYLE:
                    attr_list.append(AllplanBaseEle.AttributeInteger(125, section_fill.number))

                case SectionFillType.BITMAP:
                    path, file = ntpath.split(section_fill.bitmap)
                    attr_list.append(AllplanBaseEle.AttributeString(333, path))
                    attr_list.append(AllplanBaseEle.AttributeString(336, file))

        if len(attr_list)!= 0:
            attr_set_list = []
            attr_set_list.append(AllplanBaseEle.AttributeSet(attr_list))
            attributes = AllplanBaseEle.Attributes(attr_set_list)
            elem.SetAttributes(attributes)

```

</details>