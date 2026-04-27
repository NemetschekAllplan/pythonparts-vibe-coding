---
title: "PythonScriptType"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\PythonScriptType.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PythonScriptType

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\PythonScriptType.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

definition of the Python script types

## Abhängigkeiten

- `enum`

## Klassen

### `PythonScriptType`

definition of the Python script types
    

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
""" definition of the Python script types
"""

import enum

class PythonScriptType(enum.IntEnum):
    """ definition of the Python script types
    """

    STANDARD      = 0
    INTERACTOR    = 1
    SCRIPT_OBJECT = 2

```

</details>