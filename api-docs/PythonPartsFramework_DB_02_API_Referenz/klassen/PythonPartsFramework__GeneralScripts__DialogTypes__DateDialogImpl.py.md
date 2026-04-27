---
title: "DateDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\DateDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# DateDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\DateDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the date dialog

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `NemAll_Python_Utility`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueDialogType`
- `ValueTypes.ValueTypeUtils.BaseStringToValueConverter`
- `__future__`
- `_collections_abc`
- `datetime`
- `typing`

## Klassen

### `DateDialogImpl`

implementation of the date dialog
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_controls` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, page_index: int, global_str_table: BuildingElementStringTable, is_control_enabled: Callable[[ControlProperties], bool]` | `bool` | Add the controls  Args:     wpf_palette:        palette builder     prop:               parameter property     ctrl_props:         control properties     page_index:         page index     global_str_table:   global string table     is_control_enabled: function for getting the enabled state  Returns:     True |
| `show` | `build_ele: BuildingElement, prop: ParameterProperty, value_ctrl_prop: ControlProperties, name: str` | `bool` | show the dialog  Args:     build_ele:       building element with the parameter properties     prop:            parameter property     value_ctrl_prop: value control property     name:            parameter name  Returns:     update palette state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the date dialog
"""

from __future__ import annotations

from typing import cast, TYPE_CHECKING

from datetime import date

from _collections_abc import Callable

import NemAll_Python_Utility as AllplanUtil

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter

from .ValueDialogType import ValueDialogType

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from BuildingElementStringTable import BuildingElementStringTable
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty

class DateDialogImpl(ValueDialogType):
    """ implementation of the date dialog
    """

    @staticmethod
    def create_controls(wpf_palette       : WpfPaletteBuilder,
                        prop              : ParameterProperty,
                        ctrl_props        : ControlProperties,
                        page_index        : int,
                        global_str_table  : BuildingElementStringTable,
                        is_control_enabled: Callable[[ControlProperties], bool]) -> bool:
        """ Add the controls

        Args:
            wpf_palette:        palette builder
            prop:               parameter property
            ctrl_props:         control properties
            page_index:         page index
            global_str_table:   global string table
            is_control_enabled: function for getting the enabled state

        Returns:
            True
        """

        row_name = ctrl_props.row_name or ctrl_props.text

        wpf_palette.AddPictureResourceButton(global_str_table.get_string("e_DATE_DIALOG", "Select date"),
                                             prop.name + GeneralConstants.DATE_DIALOG_BUTTON_KEY, 19353, 0, page_index,
                                             ctrl_props.expander_name, row_name,
                                             is_control_enabled(ctrl_props),
                                             ctrl_props.height, 10, ctrl_props.font_face_code)

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

        if (index := DateDialogImpl.get_index(build_ele, value_ctrl_prop, name)) is None:
            prop.value = BaseStringToValueConverter.string_to_date(AllplanUtil.DateDialog.GetDate( \
                                                                   BaseStringToValueConverter.date_to_string(cast(date, prop.value)),
                                                                                                             value_ctrl_prop.text), False)

            return True

        prop.value[index] = \
            BaseStringToValueConverter.string_to_date(AllplanUtil.DateDialog.GetDate( \
                                                      BaseStringToValueConverter.date_to_string(cast(date, prop.value[index])),
                                                                                                value_ctrl_prop.text), False)

        return True

```

</details>