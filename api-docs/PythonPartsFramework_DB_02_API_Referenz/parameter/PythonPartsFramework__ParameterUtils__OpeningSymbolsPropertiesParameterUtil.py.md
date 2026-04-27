---
title: "OpeningSymbolsPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\OpeningSymbolsPropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# OpeningSymbolsPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\OpeningSymbolsPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the opening symbols properties parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_ArchElements`
- `NemAll_Python_Palette`

## Klassen

### `OpeningSymbolsPropertiesParameterUtil`

implementation of the opening symbols properties parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `create_opening_symbols_properties` | `build_ele: BuildingElement, name_postfix: str, opening_sym_prop: AllplanArchEle.OpeningSymbolsProperties` | `None` | create the opening symbols properties from the parameter values  Args:     build_ele:        building element with the parameter properties     name_postfix:     postfix of the parameter names     opening_sym_prop: opening symbols properties |
| `set_parameter_values` | `build_ele: BuildingElement, opening_sym_prop: AllplanArchEle.OpeningSymbolsProperties, name_postfix: str` | `None` | get the parameter values from the text properties  Args:     build_ele:        building element with the parameter properties     opening_sym_prop: opening symbols properties     name_postfix:     post fix of the parameter names |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening symbols properties parameter utilities
"""

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_Palette as AllplanPalette

from BuildingElement import BuildingElement

class OpeningSymbolsPropertiesParameterUtil():
    """ implementation of the opening symbols properties parameter utilities
    """

    @staticmethod
    def create_opening_symbols_properties(build_ele       : BuildingElement,
                                          name_postfix    : str,
                                          opening_sym_prop: AllplanArchEle.OpeningSymbolsProperties):
        """ create the opening symbols properties from the parameter values

        Args:
            build_ele:        building element with the parameter properties
            name_postfix:     postfix of the parameter names
            opening_sym_prop: opening symbols properties
        """

        opening_sym_prop.SymbolNames = build_ele.get_existing_property(f"SmartSymbolGroup{name_postfix}").value

        opening_symbol_tier_index = f"OpeningSymbolTierIndex{name_postfix}"

        if (prop := build_ele.get_property(opening_symbol_tier_index)) is None:
            opening_sym_prop.OpeningTierIndex = 1
        else:
            opening_sym_prop.OpeningTierIndex = prop.value

        match build_ele.get_existing_property(f"OpeningSymbolRefPntIndex{name_postfix}").value:
            case AllplanPalette.RefPointPosition.eTopLeft:
                opening_sym_prop.OpeningRefPntIndex = 4

            case AllplanPalette.RefPointPosition.eTopRight:
                opening_sym_prop.OpeningRefPntIndex = 3

            case AllplanPalette.RefPointPosition.eBottomLeft:
                opening_sym_prop.OpeningRefPntIndex = 1

            case AllplanPalette.RefPointPosition.eBottomRight:
                opening_sym_prop.OpeningRefPntIndex = 2


    @staticmethod
    def set_parameter_values(build_ele       : BuildingElement,
                             opening_sym_prop: AllplanArchEle.OpeningSymbolsProperties,
                             name_postfix    : str):
        """ get the parameter values from the text properties

        Args:
            build_ele:        building element with the parameter properties
            opening_sym_prop: opening symbols properties
            name_postfix:     post fix of the parameter names
        """

        build_ele.get_existing_property(f"SmartSymbolGroup{name_postfix}").value = opening_sym_prop.SymbolNames

        opening_symbol_tier_index = f"OpeningSymbolTierIndex{name_postfix}"

        if (prop := build_ele.get_property(opening_symbol_tier_index)) is not None:
            prop.value = opening_sym_prop.OpeningTierIndex

        match opening_sym_prop.OpeningRefPntIndex:
            case 4:
                build_ele.get_existing_property(f"OpeningSymbolRefPntIndex{name_postfix}").value = AllplanPalette.RefPointPosition.eTopLeft

            case 3:
                build_ele.get_existing_property(f"OpeningSymbolRefPntIndex{name_postfix}").value = AllplanPalette.RefPointPosition.eTopRight

            case 1:
                build_ele.get_existing_property(f"OpeningSymbolRefPntIndex{name_postfix}").value = AllplanPalette.RefPointPosition.eBottomLeft      # pylint: disable=line-too-long

            case 2:
                build_ele.get_existing_property(f"OpeningSymbolRefPntIndex{name_postfix}").value = AllplanPalette.RefPointPosition.eBottomRight     # pylint: disable=line-too-long

```

</details>