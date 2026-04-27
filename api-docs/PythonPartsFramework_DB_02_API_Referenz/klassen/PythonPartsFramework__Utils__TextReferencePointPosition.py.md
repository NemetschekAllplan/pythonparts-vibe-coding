---
title: "TextReferencePointPosition"
source: "PythonPartsFramework\Utils\TextReferencePointPosition.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TextReferencePointPosition

> **Pfad:** `PythonPartsFramework\Utils\TextReferencePointPosition.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

Implementation of the text reference points

## Abhängigkeiten

- `enum`

## Klassen

### `TextReferencePointPosition`

Definition of the text reference points
    

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
""" Implementation of the text reference points
"""

import enum

class TextReferencePointPosition(enum.IntEnum):
    """ Definition of the text reference points
    """

    BOTTOM_LEFT   = 1
    BOTTOM_CENTER = 2
    BOTTOM_RIGHT  = 3
    CENTER_LEFT   = 4
    CENTER_CENTER = 5
    CENTER_RIGHT  = 6
    TOP_LEFT      = 7
    TOP_CENTER    = 8
    TOP_RIGHT     = 9

```

</details>