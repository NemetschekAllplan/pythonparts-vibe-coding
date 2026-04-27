---
title: "CheckBox"
source: "PythonPartsFramework\GeneralScripts\Handles\CheckBox.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# CheckBox

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\CheckBox.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the x distance modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `BuildingElementParameterPropertyUtil`

## Klassen

### `CheckBox`

modify the value by checkbox toggle
    

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
""" implementation of the x distance modification
"""

import BuildingElementParameterPropertyUtil as PropertyUtil

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class CheckBox(BaseHandlePropUpdate):
    """ modify the value by checkbox toggle
    """

    def __call__(self):
        """ execute the value update
        """

        prop, item_name, _ = self.get_property_data()

        if prop is None:
            return

        self._update_palette = PropertyUtil.set_property_value(prop, item_name,
                                                               not PropertyUtil.get_property_value(prop, item_name))

```

</details>