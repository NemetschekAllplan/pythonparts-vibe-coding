---
title: "BuildingElementArchitectureUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementArchitectureUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementArchitectureUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementArchitectureUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

Script for BuildingElementArchitectureUtil

## Abhängigkeiten

- `ValueTypes.Resources.PlaneReferencesImpl`

## Klassen

### `BuildingElementArchitectureUtil`

Definition of class BuildingElementArchitectureUtil

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_value_planereferences` | `value_str` | `None` | Get the plane reference properties  Args:   value_str   Value string  Return: Plane reference properties |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Script for BuildingElementArchitectureUtil
"""

from ValueTypes.Resources.PlaneReferencesImpl import PlaneReferencesImpl

class BuildingElementArchitectureUtil():
    """
    Definition of class BuildingElementArchitectureUtil
    """

    @staticmethod
    def get_value_planereferences(value_str):
        """
        Get the plane reference properties

        Args:   value_str   Value string

        Return: Plane reference properties

        """

        return PlaneReferencesImpl.get_value(value_str)

```

</details>