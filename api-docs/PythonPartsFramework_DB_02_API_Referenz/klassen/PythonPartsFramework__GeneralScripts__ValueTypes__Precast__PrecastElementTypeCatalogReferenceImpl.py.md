---
title: "PrecastElementTypeCatalogReferenceImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Precast\PrecastElementTypeCatalogReferenceImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PrecastElementTypeCatalogReferenceImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Precast\PrecastElementTypeCatalogReferenceImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the PrecastElementTypeCatalogReference value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `PrecastElementTypeCatalogReferenceImpl`

implementation of the PrecastElementTypeCatalogReference value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the string combo box control  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PrecastElementTypeCatalogReference value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PrecastElementTypeCatalogReferenceImpl(BaseStrImpl):
    """ implementation of the PrecastElementTypeCatalogReference value type
    """

    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the string combo box control

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if isinstance(prop.value, int) and prop.value > 0:
            value_str = str(prop.value)

        elif isinstance(prop.value, str):
            value_str = prop.value

        else:
            value_str = ""

        prop.selected_value = \
            wpf_palette.AddPrecastElementTypeCatalogRef(ctrl_props.text, prop.name, value_str, prop_pal_ctrl_service.page_index,
                                                        ctrl_props.expander_name + ctrl_props.expander_state_key,
                                                        ctrl_props.row_name + ctrl_props.row_state_key,
                                                        prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                                        ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code)

```

</details>