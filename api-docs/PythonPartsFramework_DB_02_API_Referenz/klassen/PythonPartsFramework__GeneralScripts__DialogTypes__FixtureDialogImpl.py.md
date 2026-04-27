---
title: "FixtureDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\FixtureDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# FixtureDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\FixtureDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the fixture dialog

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `FileDialog`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Palette`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `_collections_abc`

## Klassen

### `FixtureDialogImpl`

implementation of the fixture dialog
    

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
""" implementation of the fixture dialog
"""

from _collections_abc import Callable

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Palette as AllplanPalette

from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from .FileDialog import FileDialog

class FixtureDialogImpl(FileDialog):
    """ implementation of the fixture dialog
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

        init_path = prop.value or AllplanPalette.FixtureProperties.GetLastFixturePath()

        row_name = ctrl_props.row_name or ctrl_props.text

        wpf_palette.AddButton(init_path, prop.name + GeneralConstants.DIALOG_BUTTON_KEY,
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

        path = prop.value if (index := FixtureDialogImpl.get_index(build_ele, value_ctrl_prop, name)) is None else \
               prop.value[index]


        #----------------- set the full path

        match path[:3]:
            case "ETC":
                path = path.replace("ETC\\", AllplanSettings.AllplanPaths.GetEtcPath())

            case "STD":
                path = path.replace("STD\\", AllplanSettings.AllplanPaths.GetStdPath())

            case "PRJ":
                path = path.replace("PRJ\\", AllplanSettings.AllplanPaths.GetCurPrjPath())

            case "USR":
                path = path.replace("USR\\", AllplanSettings.AllplanPaths.GetUsrPath())


        #----------------- select the path

        if not (path := AllplanPalette.FixtureProperties.OpenFixtureDialog(path)):
            return False


        #----------------- set the relative path

        match path:
            case _ if path.find(AllplanSettings.AllplanPaths.GetEtcPath()) > -1:
                path = path.replace(AllplanSettings.AllplanPaths.GetEtcPath(), "ETC\\")

            case _ if path.find(AllplanSettings.AllplanPaths.GetStdPath()) > -1:
                path = path.replace(AllplanSettings.AllplanPaths.GetStdPath(), "STD\\")

            case _ if path.find(AllplanSettings.AllplanPaths.GetCurPrjPath()) > -1:
                path = path.replace(AllplanSettings.AllplanPaths.GetCurPrjPath(), "PRJ\\")

            case _ if path.find(AllplanSettings.AllplanPaths.GetUsrPath()) > -1:
                path = path.replace(AllplanSettings.AllplanPaths.GetUsrPath(), "USR\\")

        if (index := FixtureDialogImpl.get_index(build_ele, value_ctrl_prop, name)) is None:
            prop.value = path
        else:
            prop.value[index] = path

        return False

```

</details>