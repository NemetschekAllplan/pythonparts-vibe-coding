---
title: "PolyhedronTypesList"
source: "PythonPartsFramework\TypeCollections\PolyhedronTypesList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# PolyhedronTypesList

> **Pfad:** `PythonPartsFramework\TypeCollections\PolyhedronTypesList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dokumentation`

## Übersicht

implementation of the list for the polyhedron types

## Abhängigkeiten

- `NemAll_Python_Geometry`

## Klassen

### `PolyhedronTypesList`

implementation of the list for the polyhedron types
    

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
""" implementation of the list for the polyhedron types
"""

import NemAll_Python_Geometry as AllplanGeo

class PolyhedronTypesList(list[(AllplanGeo.Polyhedron3D | AllplanGeo.Cylinder3D | AllplanGeo.ExtrudedAreaSolid3D |
                                AllplanGeo.Polygon3D | AllplanGeo.Line3D | AllplanGeo.Polyline3D | AllplanGeo.ClippedSweptSolid3D)]):
    """implementation of the list for the polyhedron types
    """

```

</details>