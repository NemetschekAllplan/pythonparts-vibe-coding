---
title: "AttributeSelectionDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\AttributeSelectionDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# AttributeSelectionDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\AttributeSelectionDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the attribute selection dialog

## Abhängigkeiten

- `AttributeIdValue`
- `BuildingElement`
- `BuildingElementStringTable`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueDialogType`
- `ValueTypes.ParameterPropertyValueTypes`
- `_collections_abc`
- `typing`

## Klassen

### `AttributeSelectionDialogImpl`

implementation of the attribute selection dialog
    

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
""" implementation of the attribute selection dialog
"""

from typing import cast

from _collections_abc import Callable

import NemAll_Python_BaseElements as AllplanBaseEle

from AttributeIdValue import AttributeIdValue
from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from .ValueDialogType import ValueDialogType

NEW_ATTRIBUTE_RES_ID = 10213
DEL_ATTRIBUTE_RES_ID = 10205

class AttributeSelectionDialogImpl(ValueDialogType):
    """ implementation of the attribute selection dialog
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

        row_name = ctrl_props.row_name if ctrl_props.row_name else ctrl_props.text

        if prop.value_type in {ParameterPropertyValueTypes.ATTRIBUTE_ID,
                               ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE}:
            if GeneralConstants.LIST_SEPARATOR_START in prop.name:
                attribute_id = prop.value if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID else \
                               prop.value.attribute_id

                btn_res_id = NEW_ATTRIBUTE_RES_ID if not attribute_id else DEL_ATTRIBUTE_RES_ID
            else:
                btn_res_id = NEW_ATTRIBUTE_RES_ID

            text_id = "e_ADD_NEW_ATTRIBUTE" if btn_res_id == NEW_ATTRIBUTE_RES_ID else "e_DELETE_ATTRIBUTE"

            wpf_palette.AddPictureResourceButton(global_str_table.get_string(text_id, "Attribute"),
                                                 prop.name + GeneralConstants.DIALOG_BUTTON_KEY, btn_res_id,
                                                 0, page_index,
                                                 ctrl_props.expander_name, row_name,
                                                 is_control_enabled(ctrl_props),
                                                 ctrl_props.height, 10, ctrl_props.font_face_code)
            return True

        wpf_palette.AddButton(AllplanBaseEle.AttributeService.GetAttributeName(DocumentManager.get_instance().document, prop.value) \
                              if prop.value else " ",
                              prop.name + GeneralConstants.DIALOG_BUTTON_KEY, 0, page_index,
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

        index = AttributeSelectionDialogImpl.get_index(build_ele, value_ctrl_prop, name)


        #----------------- delete the attribute

        if index is not None and \
           (prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID       and prop.value[index] or \
            prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE and prop.value[index].attribute_id):
            del prop.value[index]

            return True


        #----------------- get the dialog type

        doc = DocumentManager.get_instance().document

        dialog = cast(ValueDialogType, value_ctrl_prop.value_dialog).lower()

        if dialog.endswith("insert"):
            dialog_type = AllplanBaseEle.AttributeService.AttributeSelectionDialogType.eInsertAttributes

        elif dialog.endswith("project"):
            dialog_type = AllplanBaseEle.AttributeService.AttributeSelectionDialogType.eProjectAttributes

        else:
            dialog_type = AllplanBaseEle.AttributeService.AttributeSelectionDialogType.eAllAttributes


        #----------------- open the attribute selection dialog

        attribute_id = AllplanBaseEle.AttributeService.OpenAttributeSelectionDialog(doc, dialog_type)


        #----------------- new value for single attribute

        if index is None:
            if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID:
                if prop.value != attribute_id:
                    prop.value = attribute_id

                return True

            if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE:
                if prop.value.attribute_id != attribute_id:
                    prop.value.attribute_id = attribute_id
                    prop.value.value        = AllplanBaseEle.AttributeService.GetDefaultValue(doc, attribute_id)

                return True

            prop.value = attribute_id

            return True


        #----------------- new value for attribute list

        if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID:
            if prop.value[index] != attribute_id:
                prop.value[index] = attribute_id
                prop.value.append(0)

            return True

        if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE:
            if prop.value[index].attribute_id != attribute_id:
                prop.value[index].attribute_id = attribute_id
                prop.value[index].value        = AllplanBaseEle.AttributeService.GetDefaultValue(doc, attribute_id)
                prop.value.append(AttributeIdValue(0, "0"))

            return True

        prop.value[index] = attribute_id

        return True

```

</details>