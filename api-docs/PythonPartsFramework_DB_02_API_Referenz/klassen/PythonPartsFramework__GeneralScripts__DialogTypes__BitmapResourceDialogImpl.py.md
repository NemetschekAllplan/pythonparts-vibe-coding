---
title: "BitmapResourceDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\BitmapResourceDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# BitmapResourceDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\BitmapResourceDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the bitmap resource dialog

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `DocumentManager`
- `FileDialog`
- `NemAll_Python_BasisElements`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueTypes`
- `_collections_abc`

## Klassen

### `BitmapResourceDialogImpl`

implementation of the bitmap resource dialog
    

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
""" implementation of the bitmap resource dialog
"""

from _collections_abc import Callable

import NemAll_Python_BasisElements as AllplanBasisEle

from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from .FileDialog import FileDialog

class BitmapResourceDialogImpl(FileDialog):
    """ implementation of the bitmap resource dialog
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

        row_name = ctrl_props.row_name or ctrl_props.text

        wpf_palette.AddButton(prop.value, prop.name + GeneralConstants.DIALOG_BUTTON_KEY,
                              0, page_index,
                              ctrl_props.expander_name, row_name,
                              is_control_enabled(ctrl_props),
                              ctrl_props.height, ctrl_props.width,
                              ctrl_props.font_style, ctrl_props.font_face_code)

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

        index = BitmapResourceDialogImpl.get_index(build_ele, value_ctrl_prop, name)

        doc = DocumentManager.get_instance().document

        if index is None:

            if prop.value_type == ParameterPropertyValueTypes.SURFACE_ELEMENT_PROPERTIES:
                prop.value.BitmapID = AllplanBasisEle.BasisPropertyDialogs.OpenBitmapResourceDialog(doc, prop.value.BitmapID)
            else:
                prop.value = AllplanBasisEle.BasisPropertyDialogs.OpenBitmapResourceDialog(doc, prop.value)

            return True

        if prop.value_type == ParameterPropertyValueTypes.SURFACE_ELEMENT_PROPERTIES:
            prop.value[index].BitmapID = AllplanBasisEle.BasisPropertyDialogs.OpenBitmapResourceDialog(doc, prop.value[index].BitmapID)
        else:
            prop.value[index] = AllplanBasisEle.BasisPropertyDialogs.OpenBitmapResourceDialog(doc, prop.value[index])

        return True

```

</details>