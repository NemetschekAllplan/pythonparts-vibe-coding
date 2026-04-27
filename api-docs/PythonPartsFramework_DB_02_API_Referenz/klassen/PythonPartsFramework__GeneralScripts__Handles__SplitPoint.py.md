---
title: "SplitPoint"
source: "PythonPartsFramework\GeneralScripts\Handles\SplitPoint.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# SplitPoint

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\SplitPoint.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the split point modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `Point`
- `ValueTypes.ParameterPropertyValueTypes`

## Klassen

### `SplitPoint`

modify the split point
    

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
""" implementation of the split point modification
"""

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from .BaseHandlePropUpdate import BaseHandlePropUpdate
from .Point import Point

class SplitPoint(BaseHandlePropUpdate):
    """ modify the split point
    """

    def __call__(self):
        """ execute the value update
        """

        prop, _, _ = self.get_property_data()

        if prop is None:
            return


        #----------------- insert the point into the list

        if not self._handle_prop.in_modification:
            input_pnt = self._local_input_pnt.To2D if prop.value_type == ParameterPropertyValueTypes.POINT2D else self._local_input_pnt

            prop.value.insert(self._param_data.list_index, input_pnt)

            self._handle_prop.in_modification = True

            return


        #----------------- update the point in the list

        point = Point(self._build_ele, self._handle_prop, self._input_pnt, self._param_data)

        point()

```

</details>