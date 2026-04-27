---
title: "RGBColorDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\RGBColorDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# RGBColorDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\RGBColorDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the RGB color dialog

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_BasisElements`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `Utils.WriteOneColorPng`
- `ValueDialogType`
- `_collections_abc`
- `os`

## Klassen

### `RGBColorDialogImpl`

implementation of the RGB color dialog
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_controls` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, page_index: int, _global_str_table: BuildingElementStringTable, is_control_enabled: Callable[[ControlProperties], bool]` | `bool` | Add the controls  Args:     wpf_palette:        palette builder     prop:               parameter property     ctrl_props:         control properties     page_index:         page index     _global_str_table:  global string table     is_control_enabled: function for getting the enabled state  Returns:     True |
| `show` | `build_ele: BuildingElement, prop: ParameterProperty, value_ctrl_prop: ControlProperties, name: str` | `bool` | show the dialog  Args:     build_ele:       building element with the parameter properties     prop:            parameter property     value_ctrl_prop: value control property     name:            parameter name  Returns:     update palette state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the RGB color dialog
"""

import os

from _collections_abc import Callable

import NemAll_Python_BasisElements as AllplanBasisEle

from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from Utils.WriteOneColorPng import WriteOneColorPngFile

from .ValueDialogType import ValueDialogType

class RGBColorDialogImpl(ValueDialogType):
    """ implementation of the RGB color dialog
    """

    @staticmethod
    def create_controls(wpf_palette       : WpfPaletteBuilder,
                        prop              : ParameterProperty,
                        ctrl_props        : ControlProperties,
                        page_index        : int,
                        _global_str_table : BuildingElementStringTable,
                        is_control_enabled: Callable[[ControlProperties], bool]) -> bool:
        """ Add the controls

        Args:
            wpf_palette:        palette builder
            prop:               parameter property
            ctrl_props:         control properties
            page_index:         page index
            _global_str_table:  global string table
            is_control_enabled: function for getting the enabled state

        Returns:
            True
        """

        png_path = os.path.dirname(__file__) + "\\ColorButton"

        if not os.path.exists(png_path):
            os.makedirs(png_path)

        png_path += "\\" + str(prop.value) + ".png"

        if not os.path.exists(png_path):
            png_writer = WriteOneColorPngFile(16, 16, prop.value)

            with open(png_path, "wb") as file:
                png_writer.write(file)

        row_name = ctrl_props.row_name if ctrl_props.row_name else ctrl_props.text

        wpf_palette.AddPictureButton(ctrl_props.text,
                                     prop.name + GeneralConstants.DIALOG_BUTTON_KEY, png_path,
                                     0, page_index,
                                     ctrl_props.expander_name, row_name,
                                     is_control_enabled(ctrl_props),
                                     ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

        return True


    @staticmethod
    def show(build_ele      : BuildingElement,
             prop           : ParameterProperty,
             value_ctrl_prop: ControlProperties,
             name           : str) -> bool:
        """ show the dialog

        Args:
            build_ele:       building element with the parameter properties
            prop:            parameter property
            value_ctrl_prop: value control property
            name:            parameter name

        Returns:
            update palette state
        """

        index = RGBColorDialogImpl.get_index(build_ele, value_ctrl_prop, name)

        doc = DocumentManager.get_instance().document

        if index is None:
            prop.value = AllplanBasisEle.BasisPropertyDialogs.OpenRGBColorDialog(doc, prop.value + 0x1000000) - 0x1000000
        else:
            prop.value[index] = \
                AllplanBasisEle.BasisPropertyDialogs.OpenRGBColorDialog(doc, prop.value[index] + 0x1000000) - 0x1000000

        return False

```

</details>