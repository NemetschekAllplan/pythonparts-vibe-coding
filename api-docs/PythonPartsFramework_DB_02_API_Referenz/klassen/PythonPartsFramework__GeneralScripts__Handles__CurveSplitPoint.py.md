---
title: "CurveSplitPoint"
source: "PythonPartsFramework\GeneralScripts\Handles\CurveSplitPoint.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# CurveSplitPoint

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\CurveSplitPoint.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the curve split point modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `TypeCollections.GeometryTyping`
- `typing`

## Klassen

### `CurveSplitPoint`

modify the curve point
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self` | `None` | execute the value update          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the curve split point modification
"""

from typing import cast

from TypeCollections.GeometryTyping import CURVES_3D

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class CurveSplitPoint(BaseHandlePropUpdate):
    """ modify the curve point
    """

    def __call__(self):
        """ execute the value update
        """

        param_data = self._handle_prop.parameter_data[0]

        if (geo_element := param_data.geo_element) is None or param_data.list_index is None:
            return

        input_pnt = self._local_input_pnt if isinstance(geo_element, CURVES_3D) else self._local_input_pnt.To2D


        #----------------- insert the point into the list

        if not self._handle_prop.in_modification:
            geo_element.Insert(input_pnt, cast(int, param_data.list_index))     # type: ignore

            self._handle_prop.in_modification = True

            return


        #----------------- update the point in the list

        geo_element.SetPoint(input_pnt, cast(int, param_data.list_index))     # type: ignore

```

</details>