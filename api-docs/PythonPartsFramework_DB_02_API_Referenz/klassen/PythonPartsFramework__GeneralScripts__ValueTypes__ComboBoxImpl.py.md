---
title: "ComboBoxImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ComboBoxImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ComboBoxImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ComboBoxImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the combo box meta class

## Abhängigkeiten

- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `ComboBoxImpl`

implementation of the combo box meta class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__new__` | `mcs: type[Self], name: str, bases: tuple[type, ...], attrs: dict[str, Any]` | `Self` | add the set_property_value to the combo box implementation  Args:     mcs:   meta class     name:  name of the class     bases: bases     attrs: attributes  Returns:     created meta class |
| `set_property_value` | `cls: type[Self], prop: ParameterProperty, name: str, value: list[float | int | str] | float | int | str` | `bool` | Set the value of the property  Args:     cls:   meta class     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `add_del_button` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the delete button  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the combo box meta class
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from .ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

Self = TypeVar("Self")

if TYPE_CHECKING:
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty

    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class ComboBoxImpl(type):
    """ implementation of the combo box meta class
    """

    def __new__(mcs  : type[Self],
                name : str,
                bases: tuple[type, ...],
                attrs: dict[str, Any]) -> Self:
        """ add the set_property_value to the combo box implementation

        Args:
            mcs:   meta class
            name:  name of the class
            bases: bases
            attrs: attributes

        Returns:
            created meta class
        """

        attrs['set_property_value'] = ComboBoxImpl.set_property_value
        attrs['base_class']         = bases[0]

        return super().__new__(mcs, name, bases, attrs)


    def set_property_value(cls  : type[Self],     # type: ignore
                           prop : ParameterProperty,
                           name : str,
                           value: (list[(float | int | str)] | float | int | str)) -> bool:
        """ Set the value of the property

        Args:
            cls:   meta class
            prop:  property
            name:  name of the modified property
            value: new value

        Returns:
            update palette state
        """

        ret      = False
        del_mode = False

        if  GeneralConstants.DIALOG_BUTTON_COMBO_DEL_ENTRY in name and prop.value_list_util:
            value = ParameterPropertyListUtil.get_item_value(prop, name.replace(GeneralConstants.DIALOG_BUTTON_COMBO_DEL_ENTRY, ""))

            prop.value_list_util.delete_item(value)

            ret      = True
            del_mode = True

            if (value := prop.value_list_util.get_first_item()) is None:    # type: ignore
                value = cls.base_class.get_value("")      # type: ignore

        ret |= cls.base_class.set_property_value(prop, name, value)      # type: ignore

        if prop.value_list_util and not del_mode:
            ret |= prop.value_list_util.update(prop.value)

        return ret


    @staticmethod
    def add_del_button(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the delete button

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        row_name = ctrl_props.row_name or ctrl_props.text

        wpf_palette.AddPictureResourceButton(prop_pal_ctrl_service.build_ele.get_string_tables()[1].get_string("e_DELETE_ITEM",
                                                                                                               "Delete item"),
                                                prop.name + GeneralConstants.DIALOG_BUTTON_COMBO_DEL_ENTRY, 10051,
                                                0, prop_pal_ctrl_service.page_index,
                                                ctrl_props.expander_name, row_name,
                                                prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                                ctrl_props.height, 10, ctrl_props.font_face_code)

```

</details>