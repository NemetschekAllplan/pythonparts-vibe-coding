---
title: "TopPlaneReferencesDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\TopPlaneReferencesDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# TopPlaneReferencesDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\TopPlaneReferencesDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the top plane references dialog

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_ArchElements`
- `ParameterProperty`
- `ValueDialogType`

## Klassen

### `TopPlaneReferencesDialogImpl`

implementation of the top plane references dialog
    

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
""" implementation of the top plane references dialog
"""

import NemAll_Python_ArchElements as AllplanArch

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from .ValueDialogType import ValueDialogType

class TopPlaneReferencesDialogImpl(ValueDialogType):
    """ implementation of the top plane references dialog
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

        index = TopPlaneReferencesDialogImpl.get_index(build_ele, value_ctrl_prop, name)

        doc        = DocumentManager.get_instance().document
        pythonpart = DocumentManager.get_instance().pythonpart_element

        if index is None:
            AllplanArch.PropertyDialogs.OpenTopPlaneReferenceDialog(pythonpart, doc, prop.value)
        else:
            AllplanArch.PropertyDialogs.OpenTopPlaneReferenceDialog(pythonpart, doc, prop.value[index])

        return True

```

</details>