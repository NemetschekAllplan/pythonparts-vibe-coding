---
title: "PlaneReferencesDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\PlaneReferencesDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# PlaneReferencesDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\PlaneReferencesDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the plane references dialog

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_ArchElements`
- `ParameterProperty`
- `ValueDialogType`

## Klassen

### `PlaneReferencesDialogImpl`

implementation of the plane references dialog
    

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
""" implementation of the plane references dialog
"""

import NemAll_Python_ArchElements as AllplanArch

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from .ValueDialogType import ValueDialogType

class PlaneReferencesDialogImpl(ValueDialogType):
    """ implementation of the plane references dialog
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

        index = PlaneReferencesDialogImpl.get_index(build_ele, value_ctrl_prop, name)

        doc        = DocumentManager.get_instance().document
        pythonpart = DocumentManager.get_instance().pythonpart_element

        if index is None:
            AllplanArch.PropertyDialogs.OpenPlaneReferencesDialog(pythonpart, doc, prop.value)
        else:
            AllplanArch.PropertyDialogs.OpenPlaneReferencesDialog(pythonpart, doc, prop.value[index])

        return True

```

</details>