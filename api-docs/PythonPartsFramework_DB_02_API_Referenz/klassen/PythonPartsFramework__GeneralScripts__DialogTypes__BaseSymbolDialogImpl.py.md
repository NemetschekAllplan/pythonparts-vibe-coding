---
title: "BaseSymbolDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\BaseSymbolDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# BaseSymbolDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\BaseSymbolDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the symbol dialog

## Abhängigkeiten

- `BuildingElementStringTable`
- `ControlProperties`
- `FileDialog`
- `NemAll_Python_ArchElements`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `_collections_abc`

## Klassen

### `BaseSymbolDialogImpl`

implementation of the symbol dialog
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_controls` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, page_index: int, _global_str_table: BuildingElementStringTable, is_control_enabled: Callable[[ControlProperties], bool]` | `bool` | Add the controls  Args:     wpf_palette:        palette builder     prop:               parameter property     ctrl_props:         control properties     page_index:         page index     _global_str_table:  global string table     is_control_enabled: function for getting the enabled state  Returns:     True |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the symbol dialog
"""

from _collections_abc import Callable

import NemAll_Python_ArchElements as AllplanArch

from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from Palette.WpfPaletteBuilder import WpfPaletteBuilder
from Utilities.GeneralConstants import GeneralConstants

from .FileDialog import FileDialog

class BaseSymbolDialogImpl(FileDialog):
    """ implementation of the symbol dialog
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

        init_path = prop.value or AllplanArch.PropertyDialogs.GetLastSymbolPath()

        row_name = ctrl_props.row_name or ctrl_props.text

        wpf_palette.AddButton(init_path, prop.name + GeneralConstants.DIALOG_BUTTON_KEY,
                              0, page_index,
                              ctrl_props.expander_name, row_name,
                              is_control_enabled(ctrl_props),
                              ctrl_props.height, ctrl_props.width,
                              ctrl_props.font_style, ctrl_props.font_face_code)

        return True

```

</details>