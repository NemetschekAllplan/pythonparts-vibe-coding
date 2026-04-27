---
title: "FactoryCatalogReferenceImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Precast\FactoryCatalogReferenceImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# FactoryCatalogReferenceImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Precast\FactoryCatalogReferenceImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the FactoryCatalogReference value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `FactoryCatalogReferenceImpl`

implementation of the FactoryCatalogReference value type
    

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
""" implementation of the FactoryCatalogReference value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class FactoryCatalogReferenceImpl(BaseStrImpl):
    """ implementation of the FactoryCatalogReference value type
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

        prop_pal_ctrl_service.add_control(wpf_palette.AddFactoryCatalogRef, prop, ctrl_props, prop.value)

```

</details>