---
title: "PaletteData"
source: "PythonPartsFramework\GeneralScripts\Palette\PaletteData.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PaletteData

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\PaletteData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the palette data

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `__future__`
- `dataclasses`
- `typing`

## Klassen

### `PaletteData`

implementation of the palette data
    

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
""" implementation of the palette data
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from dataclasses import dataclass, field

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from BuildingElementStringTable import BuildingElementStringTable

@dataclass
class PaletteData:
    """ implementation of the palette data
    """

    page_enable_cond : str
    param_dict       : dict[str, Any]
    page_index       : int
    picture_path     : str
    global_str_table : BuildingElementStringTable
    build_ele        : BuildingElement
    row              : int
    is_visual_script : bool

    expander_name      : str  = "???"
    expander_visible   : bool = True

    row_name      : str  = ""
    row_visible   : bool = True
    row_full_text : str  = ""

    expander_visibility_dict : dict[str, bool] = field(default_factory=dict)

```

</details>