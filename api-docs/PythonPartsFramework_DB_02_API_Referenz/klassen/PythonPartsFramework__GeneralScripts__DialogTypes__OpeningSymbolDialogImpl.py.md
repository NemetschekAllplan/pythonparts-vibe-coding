---
title: "OpeningSymbolDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\OpeningSymbolDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# OpeningSymbolDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\OpeningSymbolDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the opening symbol dialog

## Abhängigkeiten

- `BaseSymbolDialogImpl`
- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_ArchElements`
- `ParameterProperty`

## Klassen

### `OpeningSymbolDialogImpl`

implementation of the opening dialog
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `show` | `build_ele: BuildingElement, prop: ParameterProperty, value_ctrl_prop: ControlProperties, name: str` | `bool` | show the dialog  Args:     build_ele:       building element with the parameter properties     prop:            parameter property     value_ctrl_prop: value control property     name:            parameter name  Returns:     update palette state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the opening symbol dialog
"""

import NemAll_Python_ArchElements as AllplanArch

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from .BaseSymbolDialogImpl import BaseSymbolDialogImpl

class OpeningSymbolDialogImpl(BaseSymbolDialogImpl):
    """ implementation of the opening dialog
    """

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

        default_value = OpeningSymbolDialogImpl.get_default_value(build_ele, prop, value_ctrl_prop, name)

        prop_value = AllplanArch.PropertyDialogs.OpenSmartSymbolPartDialog(default_value, True, True)

        prop.value_type.set_property_value(prop, name, prop_value)

        return True

```

</details>