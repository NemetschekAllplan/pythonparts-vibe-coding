---
title: "IncludeData"
source: "PythonPartsFramework\GeneralScripts\XMLReader\IncludeData.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# IncludeData

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\IncludeData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `xml`

## Übersicht

implementation of the include data

## Abhängigkeiten

- `dataclasses`

## Klassen

### `IncludeData`

implementation of the include data
    

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
""" implementation of the include data
"""

from dataclasses import dataclass, field

@dataclass
class IncludeData:
    """ implementation of the include data
    """

    is_include  : bool           = False
    incl_visible: dict[str, str] = field(default_factory = dict)
    name_postfix: str            = ""
    text_postfix: str            = ""

```

</details>