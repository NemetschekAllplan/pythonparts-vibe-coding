---
title: "BuildingElementCounter"
source: "PythonPartsFramework\GeneralScripts\BuildingElementCounter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementCounter

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementCounter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the building element counter

## Abhängigkeiten

- `collections`

## Klassen

### `BuildingElementCounter`

Definition of class BuildingElementCounter

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | Initialisation of class BuildingElementConunter |
| `__repr__` | `self` | `None` | - |
| `check_index` | `self, build_ele` | `None` | Checks, whether the current element has the index from the palette  Args:     build_ele:  building element  Returns:     element has the palette index |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Implementation of the building element counter
"""

from collections import Counter

class BuildingElementCounter():
    """
    Definition of class BuildingElementCounter
    """

    def __init__(self):
        """
        Initialisation of class BuildingElementConunter
        """
        self.m_ele_count = Counter()

    def __repr__(self):
        return "%s(\n"     \
               "   %s\n"   \
               ")\n"       \
               % (self.__class__.__name__,
                  self.m_ele_count)

    def check_index(self, build_ele):
        """
        Checks, whether the current element has the index from the palette

        Args:
            build_ele:  building element

        Returns:
            element has the palette index
        """

        script_name = build_ele.script_name

        self.m_ele_count.update((script_name,))

        prop = getattr(build_ele, "__ElementIndex__", None)

        if prop is None:
            return True

        index = prop.value

        return index == self.m_ele_count[script_name]

```

</details>