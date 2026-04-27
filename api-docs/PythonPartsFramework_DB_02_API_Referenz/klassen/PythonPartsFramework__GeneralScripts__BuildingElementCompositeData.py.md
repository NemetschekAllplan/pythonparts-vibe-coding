---
title: "BuildingElementCompositeData"
source: "PythonPartsFramework\GeneralScripts\BuildingElementCompositeData.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementCompositeData

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementCompositeData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the build element composite data

## Abhängigkeiten

- `collections`
- `dataclasses`

## Klassen

### `Constraint`

implementation of the constraint data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `BuildingElementCompositeData`

Implementation of class BuildingElementCompositeData
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__repr__` | `self` | `str` | create a data string  Returns:     data string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the build element composite data
"""

from dataclasses import dataclass, field
from collections import namedtuple

DefaultValues = namedtuple("DefaultValues", "name, value, visible, text, list_state, list_reverse, list_squeeze")

PaletteData = namedtuple("PaletteData", "PageIndex, ControlIndex, PageText, PageTextId, ExpanderText, ExpanderTextId")

@dataclass
class Constraint:
    """ implementation of the constraint data
    """

    name        : str
    value       : str
    value_type  : str
    condition   : str
    visible     : str
    list_state  : int | None
    list_reverse: int | None

@dataclass
class BuildingElementCompositeData:
    """ Implementation of class BuildingElementCompositeData
    """

    sub_ele_script       : list[object]              = field(default_factory = list)
    sub_ele_script_name  : list[str]                 = field(default_factory = list)
    sub_ele_script_uuid  : list[str]                 = field(default_factory = list)
    sub_ele_defaults     : list[list[DefaultValues]] = field(default_factory = list)
    sub_ele_constraints  : list[list[Constraint]]    = field(default_factory = list)
    sub_ele_page_index   : list[int]                 = field(default_factory = list)
    sub_ele_id           : list[str]                 = field(default_factory = list)
    sub_ele_visible      : list[str]                 = field(default_factory = list)
    sub_ele_composite    : list[list[str]]           = field(default_factory = list)
    sub_ele_name         : list[str]                 = field(default_factory = list)
    sub_ele_palette_data : dict[str,PaletteData]     = field(default_factory = dict)


    def __repr__(self) -> str:
        """ create a data string

        Returns:
            data string
        """
        return f"<{self.__class__.__name__}>\n" \
               f"  sub_ele_script         = {self.sub_ele_script}\n" \
               f"  sub_ele_script_name    = {self.sub_ele_script_name}\n" \
               f"  sub_ele_script_uuid    = {self.sub_ele_script_uuid}\n" \
               f"  sub_ele_defaults       = {self.sub_ele_defaults}\n" \
               f"  sub_ele_constraints    = {self.sub_ele_constraints}\n" \
               f"  sub_ele_page_index     = {self.sub_ele_page_index}\n" \
               f"  sub_ele_id             = {self.sub_ele_id}\n" \
               f"  sub_ele_visible        = {self.sub_ele_visible}\n" \
               f"  sub_ele_composite      = {self.sub_ele_composite}\n"

```

</details>