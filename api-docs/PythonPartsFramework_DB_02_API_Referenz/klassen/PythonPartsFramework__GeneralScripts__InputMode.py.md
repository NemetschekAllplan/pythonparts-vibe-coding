---
title: "InputMode"
source: "PythonPartsFramework\GeneralScripts\InputMode.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# InputMode

> **Pfad:** `PythonPartsFramework\GeneralScripts\InputMode.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the input mode enumeration

## Abhängigkeiten

- `enum`

## Klassen

### `InputMode`

Definition of class InputMode

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
"""
Implementation of the input mode enumeration
"""

import enum

class InputMode(enum.IntEnum):
    """
    Definition of class InputMode
    """
    GeoExpand    = 1
    RefPoint     = 2
    HandleSelect = 3
    HandleModify = 4
    HandleNext   = 5
    Interactor   = 6
    WriteToDB    = 7



```

</details>