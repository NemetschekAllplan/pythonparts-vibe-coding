---
title: "AllplanEnvironment"
source: "PythonPartsFramework\GeneralScripts\Utilities\AllplanEnvironment.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# AllplanEnvironment

> **Pfad:** `PythonPartsFramework\GeneralScripts\Utilities\AllplanEnvironment.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the Allplan environment utilities

## Abhängigkeiten

- `NemAll.Python.Palette.WPF.ViewModel`
- `NemAll_Python_AllplanSettings`
- `clr`

## Klassen

### `AllplanEnvironment`

implementation of the Allplan environment utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `is_dark_mode` | `-` | `bool` | checks if Allplan user interface is set to dark mode  Returns:     true if dark mode is set, false otherwise |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Allplan environment utilities
"""

import clr

import NemAll_Python_AllplanSettings as AllplanSettings

clr.AddReference(f"{AllplanSettings.AllplanPaths.GetPathOfApplication()}\\NemAll_Python_Palette_WPF.dll")
from NemAll.Python.Palette.WPF.ViewModel import PythonPaletteViewModel

class AllplanEnvironment():
    """ implementation of the Allplan environment utilities
    """


    @staticmethod
    def is_dark_mode() -> bool:
        """ checks if Allplan user interface is set to dark mode

        Returns:
            true if dark mode is set, false otherwise
        """

        return PythonPaletteViewModel.IsDarkTheme

```

</details>