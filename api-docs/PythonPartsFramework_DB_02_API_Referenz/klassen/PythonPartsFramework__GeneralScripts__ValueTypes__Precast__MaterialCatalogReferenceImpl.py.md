---
title: "MaterialCatalogReferenceImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Precast\MaterialCatalogReferenceImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# MaterialCatalogReferenceImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Precast\MaterialCatalogReferenceImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the MaterialCatalogReference value type

## Abhängigkeiten

- `BaseStrImpl`
- `ControlProperties`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `MaterialCatalogReferenceImpl`

implementation of the MaterialCatalogReference value type
    

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
""" implementation of the MaterialCatalogReference value type
"""

# pylint: disable=magic-value-comparison

from __future__ import annotations

from typing import TYPE_CHECKING

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class MaterialCatalogReferenceImpl(BaseStrImpl):
    """ implementation of the MaterialCatalogReference value type
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

        start = prop.value.find("(")
        end   = prop.value.find(")")
        val   = prop.value[start + 1:]

        if end > -1:
            val = prop.value[start + 1: end]

        if "ConcreteCat" in prop.value or "In-situ ConcreteCat" in prop.value:
            prop_pal_ctrl_service.add_control(wpf_palette.AddConcreteGradeCatalogRef, prop, ctrl_props, val)

        if "InsulationCat" in prop.value:
            prop_pal_ctrl_service.add_control(wpf_palette.AddInsulationCatalogRef, prop, ctrl_props, val)

        if "Brick/TileCat" in prop.value:
            prop_pal_ctrl_service.add_control(wpf_palette.AddBrickTileCatalogRef, prop, ctrl_props, val)

```

</details>