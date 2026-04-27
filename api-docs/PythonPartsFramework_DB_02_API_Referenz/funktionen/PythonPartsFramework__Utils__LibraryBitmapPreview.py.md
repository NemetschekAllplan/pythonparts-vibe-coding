---
title: "LibraryBitmapPreview"
source: "PythonPartsFramework\Utils\LibraryBitmapPreview.py"
type: "module"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# LibraryBitmapPreview

> **Pfad:** `PythonPartsFramework\Utils\LibraryBitmapPreview.py`  
> **Typ:** Modul  
> **Tags:** `utility`

## Übersicht

Implementation of the library bitmap preview 

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `TestHelper`
- `TypeCollections`
- `Utilities.AllplanEnvironment`
- `os`
- `struct`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `create_libary_bitmap_preview(png_file_name: str)`

deprecated function with typo

Args:
    png_file_name: pnt file name

Returns:
    list with the model elements for the preview

**Parameter:**
- `png_file_name: str`

**Rückgabe:** `ModelEleList`

**Beispiel:**
```python
result = create_libary_bitmap_preview(...)
```

### `create_library_bitmap_preview(png_file_name: str)`

This function creates the preview objects, which are needed to draw
a bitmap inside the preview window of the library

Args:
    png_file_name: full name of the png file

Returns:
    list with the model elements for the preview

**Parameter:**
- `png_file_name: str`

**Rückgabe:** `ModelEleList`

**Beispiel:**
```python
result = create_library_bitmap_preview(...)
```

### `get_file_name_for_active_gui_theme(png_file_name: str)`

Returns a file name for active gui theme using '_dark' suffix for dark mode

Args:
    png_file_name: Full name of the png file.

Returns:
    Modified file name with '_dark' suffix if the dark mode is active and the file exists,
    otherwise the original file name.

**Parameter:**
- `png_file_name: str`

**Rückgabe:** `str`

**Beispiel:**
```python
result = get_file_name_for_active_gui_theme(...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the library bitmap preview """

import os
import struct

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_BasisElements as AllplanBasisEle

from Utilities.AllplanEnvironment import AllplanEnvironment

from TestHelper import PythonPartPylintDecorator

from TypeCollections import ModelEleList

UNPACK_CODE = 0x0d0a1a0a

@PythonPartPylintDecorator.deprecated(replace = "use create_library_bitmap_preview(...)")
def create_libary_bitmap_preview(png_file_name: str) -> ModelEleList:
    """ deprecated function with typo

    Args:
        png_file_name: pnt file name

    Returns:
        list with the model elements for the preview
    """

    return create_library_bitmap_preview(png_file_name)


def create_library_bitmap_preview(png_file_name: str) -> ModelEleList:
    """ This function creates the preview objects, which are needed to draw
    a bitmap inside the preview window of the library

    Args:
        png_file_name: full name of the png file

    Returns:
        list with the model elements for the preview
    """

    if not os.path.isfile(png_file_name):
        print("")
        print("")
        print(f"file {png_file_name} not found for the library preview!!!")
        print("")
        print("")
        return ModelEleList()

    png_file_name = get_file_name_for_active_gui_theme(png_file_name)

    #----------------- read the size

    width  = 1000
    height = 1000

    with open(png_file_name, 'rb') as fhandle:
        head = fhandle.read(24)

        if struct.unpack('>i', head[4:8])[0] == UNPACK_CODE:
            width, height = struct.unpack('>ii', head[16:24])

        fhandle.close()


    #------------------ Define the polygon

    polygon = AllplanGeo.Polygon2D()
    polygon += AllplanGeo.Point2D(0,0)
    polygon += AllplanGeo.Point2D(width,0)
    polygon += AllplanGeo.Point2D(width,height)
    polygon += AllplanGeo.Point2D(0,height)
    polygon += AllplanGeo.Point2D(0,0)


    #------------------ Define common properties, take global Allplan settings

    com_prop = AllplanBaseEle.CommonProperties()
    com_prop.GetGlobalProperties()


    #------------------ Define BitmapArea properties

    bitmaparea_prop            = AllplanBasisEle.BitmapAreaProperties()
    bitmaparea_prop.BitmapName = png_file_name


    #------------------ Append for creation as new Allplan elements

    model_ele_list = ModelEleList()

    model_ele_list.append(AllplanBasisEle.BitmapAreaElement(com_prop, bitmaparea_prop, polygon))

    return model_ele_list

def get_file_name_for_active_gui_theme(png_file_name: str) -> str:
    """Returns a file name for active gui theme using '_dark' suffix for dark mode

    Args:
        png_file_name: Full name of the png file.

    Returns:
        Modified file name with '_dark' suffix if the dark mode is active and the file exists,
        otherwise the original file name.
    """

    if not AllplanEnvironment.is_dark_mode():
        return png_file_name

    directory, file_name = os.path.split(png_file_name)
    file_name_without_extension, extension = os.path.splitext(file_name)
    dark_file_name = f"{file_name_without_extension}_dark{extension}"
    dark_file_path = os.path.join(directory, dark_file_name)

    if os.path.isfile(dark_file_path):
        return dark_file_path

    return png_file_name

```

</details>