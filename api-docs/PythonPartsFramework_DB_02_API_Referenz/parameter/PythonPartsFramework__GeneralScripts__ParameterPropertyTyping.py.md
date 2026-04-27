---
title: "ParameterPropertyTyping"
source: "PythonPartsFramework\GeneralScripts\ParameterPropertyTyping.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
related:
  -
last_updated: "2026-02-20"
---


# ParameterPropertyTyping

> **Pfad:** `PythonPartsFramework\GeneralScripts\ParameterPropertyTyping.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`

## Übersicht

implementation of the helper class for the ParameterProperty typing

## Abhängigkeiten

- `ParameterProperty`
- `typing`

## Klassen

### `ParameterPropertyTyping`

generic ParameterProperty for the typing

Args:
    Generic:           generic type
    ParameterProperty: base class

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
""" implementation of the helper class for the ParameterProperty typing
"""

from typing import Generic, TypeVar

from ParameterProperty import ParameterProperty

T = TypeVar("T")

class ParameterPropertyTyping(Generic[T], ParameterProperty):
    """ generic ParameterProperty for the typing

    Args:
        Generic:           generic type
        ParameterProperty: base class
    """

    value : T

```

</details>