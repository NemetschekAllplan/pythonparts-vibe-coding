---
title: "BuildingElementValueTypeUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementValueTypeUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementValueTypeUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementValueTypeUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

Implementation of the value type utilities

## Abhängigkeiten

- Keine

## Klassen

### `BuildingElementValueTypeUtil`

Implementation of the value type utilities

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `is_float_type` | `value_type` | `None` | Check for a float value type |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Implementation of the value type utilities
"""

class BuildingElementValueTypeUtil():
    """
    Implementation of the value type utilities
    """

    @staticmethod
    def is_float_type(value_type):
        """
        Check for a float value type
        """

        return value_type in ("angle",
                              "anglecombobox",
                              "double",
                              "doublecombobox",
                              "length",
                              "lengthcombobox",
                              "area",
                              "volume",
                              "weight",
                              "reinfbendingroller",
                              "reinfconcretecover",
                              "reinfbardiameter",
                              "reinfhooklength")

```

</details>