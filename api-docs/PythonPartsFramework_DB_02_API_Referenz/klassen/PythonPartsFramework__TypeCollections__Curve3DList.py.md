---
title: "Curve3DList"
source: "PythonPartsFramework\TypeCollections\Curve3DList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# Curve3DList

> **Pfad:** `PythonPartsFramework\TypeCollections\Curve3DList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dokumentation`

## Übersicht

implementation of the list for the 3D curve elements

## Abhängigkeiten

- `NemAll_Python_Geometry`

## Klassen

### `Curve3DList`

implementation of the list for the 3D curve elements
    

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
""" implementation of the list for the 3D curve elements
"""

import NemAll_Python_Geometry as AllplanGeo

class Curve3DList(list[(AllplanGeo.Arc3D | AllplanGeo.BSpline3D | AllplanGeo.Line3D | \
                        AllplanGeo.Path3D | AllplanGeo.Polyline3D | AllplanGeo.Polygon3D | AllplanGeo.Spline3D)]):
    """ implementation of the list for the 3D curve elements
    """

```

</details>