---
title: "DisplayTextImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\DisplayTextImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# DisplayTextImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\DisplayTextImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the DisplayText value type

## Abhängigkeiten

- `BaseStrImpl`
- `ParameterProperty`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `DisplayTextImpl`

implementation of the DisplayText value type
    

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
""" implementation of the DisplayText value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .BaseStrImpl import BaseStrImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from .ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class DisplayTextImpl(BaseStrImpl):                 # pylint: disable=too-few-public-methods
    """ implementation of the DisplayText value type
    """

```

</details>