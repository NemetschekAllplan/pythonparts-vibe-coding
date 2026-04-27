---
title: "DecrementButton"
source: "PythonPartsFramework\GeneralScripts\Handles\DecrementButton.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# DecrementButton

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\DecrementButton.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the decrement button modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `BuildingElementParameterPropertyUtil`

## Klassen

### `DecrementButton`

modify the value by decrement
    

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
""" implementation of the decrement button modification
"""

import BuildingElementParameterPropertyUtil as PropertyUtil

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class DecrementButton(BaseHandlePropUpdate):
    """ modify the value by decrement
    """

    def __call__(self):
        """ execute the value update
        """

        prop, item_name, _ = self.get_property_data()

        if prop is None:
            return

        self._update_palette = PropertyUtil.set_property_value(prop, item_name,
                                                               PropertyUtil.get_property_value(prop, item_name) - \
                                                               self._param_data.in_decrement_value)
```

</details>