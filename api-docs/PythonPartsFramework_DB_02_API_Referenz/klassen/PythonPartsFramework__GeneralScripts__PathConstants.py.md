---
title: "PathConstants"
source: "PythonPartsFramework\GeneralScripts\PathConstants.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PathConstants

> **Pfad:** `PythonPartsFramework\GeneralScripts\PathConstants.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the Allplan path constants

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`

## Klassen

### `PathConstants`

implementation of the Allplan path constants
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the Allplan path constants
"""

import NemAll_Python_AllplanSettings as AllplanSettings

class PathConstants(str):
    """ implementation of the Allplan path constants
    """

    ETC_PATH = "etc"
    STD_PATH = "std"
    USR_PATH = "usr"
    PRJ_PATH = "prj"

    PATH_KEYS_SEARCH_ORDER = (PRJ_PATH, STD_PATH, ETC_PATH, USR_PATH)

    PYP_SEARCH_PATHS = (AllplanSettings.AllplanPaths.GetCurPrjPath(),
                        AllplanSettings.AllplanPaths.GetStdPath(),
                        AllplanSettings.AllplanPaths.GetPythonPartsEtcPath(),
                        AllplanSettings.AllplanPaths.GetUsrPath())

    KEY_PATH_TUPLES = ((ETC_PATH, AllplanSettings.AllplanPaths.GetPythonPartsEtcPath()),
                       (STD_PATH, AllplanSettings.AllplanPaths.GetStdPath()),
                       (USR_PATH, AllplanSettings.AllplanPaths.GetUsrPath()),
                       (PRJ_PATH, AllplanSettings.AllplanPaths.GetCurPrjPath()))

```

</details>