---
title: "BottomPlaneReferencesDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\BottomPlaneReferencesDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# BottomPlaneReferencesDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\BottomPlaneReferencesDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the bottom plane references dialog

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_ArchElements`
- `ParameterProperty`
- `ValueDialogType`

## Klassen

### `BottomPlaneReferencesDialogImpl`

implementation of the bottom plane references dialog
    

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
""" implementation of the bottom plane references dialog
"""

import NemAll_Python_ArchElements as AllplanArch

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from .ValueDialogType import ValueDialogType

class BottomPlaneReferencesDialogImpl(ValueDialogType):
    """ implementation of the bottom plane references dialog
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

        index = BottomPlaneReferencesDialogImpl.get_index(build_ele, value_ctrl_prop, name)

        doc        = DocumentManager.get_instance().document
        pythonpart = DocumentManager.get_instance().pythonpart_element

        if index is None:
            AllplanArch.PropertyDialogs.OpenBottomPlaneReferenceDialog(pythonpart, doc, prop.value)
        else:
            AllplanArch.PropertyDialogs.OpenBottomPlaneReferenceDialog(pythonpart, doc, prop.value[index])

        return True

```

</details>