---
title: "BuildingElementFixtureUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementFixtureUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementFixtureUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementFixtureUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

Script for BuildingElementFixtureUtil

## Abhängigkeiten

- `NemAll_Python_Palette`

## Klassen

### `BuildingElementFixtureUtil`

Definition of class BuildingElementFixtureUtil

Create the fixture properties from a value string

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `get_fixtureprpoperties_from_libraryelement` | `library_ele` | `None` | Get the fixture properties from the library element  |
| `get_fixturesinglepath_from_libraryelement` | `library_ele` | `None` | Get the fixture properties from the library element  |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Script for BuildingElementFixtureUtil
"""

import NemAll_Python_Palette as AllplanPalette

class BuildingElementFixtureUtil():
    """
    Definition of class BuildingElementFixtureUtil

    Create the fixture properties from a value string
    """


    @staticmethod
    def get_fixtureprpoperties_from_libraryelement(library_ele):
        """ Get the fixture properties from the library element """

        if library_ele == None:
            return AllplanPalette.FixtureProperties("", "", "")

        props = library_ele.GetProperties()

        return AllplanPalette.FixtureProperties(props.GetPath(), props.GetGroup(), props.GetElement())

    @staticmethod
    def get_fixturesinglepath_from_libraryelement(library_ele):
        """ Get the fixture properties from the library element """

        if library_ele == None:
            return ""

        props = library_ele.GetProperties()

        return props.GetSingleFilePath()

```

</details>