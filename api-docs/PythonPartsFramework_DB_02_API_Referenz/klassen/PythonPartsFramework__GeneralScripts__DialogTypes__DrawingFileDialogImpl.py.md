---
title: "DrawingFileDialogImpl"
source: "PythonPartsFramework\GeneralScripts\DialogTypes\DrawingFileDialogImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dialog
  - script
related:
  -
last_updated: "2026-02-20"
---


# DrawingFileDialogImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\DialogTypes\DrawingFileDialogImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dialog`, `script`

## Übersicht

implementation of the drawing file dialog

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `ParameterProperty`
- `ValueDialogType`

## Klassen

### `DrawingFileDialogImpl`

implementation of the drawing file dialog
    

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
""" implementation of the drawing file dialog
"""

import NemAll_Python_BaseElements as AllplanBase

from BuildingElement import BuildingElement
from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from .ValueDialogType import ValueDialogType

class DrawingFileDialogImpl(ValueDialogType):
    """ implementation of the drawing file dialog
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

        doc = DocumentManager.get_instance().document

        single_selection   = value_ctrl_prop.value_list   == "True"
        deactivate_derived = value_ctrl_prop.value_list_2 == "True"

        selected_drawing_files = AllplanBase.DrawingFileService.ShowDrawingFileDialog(doc, single_selection, deactivate_derived)

        prop.value = selected_drawing_files

        return True

```

</details>