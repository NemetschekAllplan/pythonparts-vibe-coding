---
title: "WpfPaletteChangeHandler"
source: "PythonPartsFramework\GeneralScripts\Palette\WpfPaletteChangeHandler.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# WpfPaletteChangeHandler

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\WpfPaletteChangeHandler.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the wpf palette change handler that handles change events from the palette

## Abhängigkeiten

- `__future__`
- `collections.abc`
- `typing`

## Klassen

### `WpfPaletteChangeHandler`

implementation of the palette change handler
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize  Args:      |
| `create_value_changed_handler` | `self, page: int, parameter_name: str, view_model_type: str` | `Callable[[Any], None]` | Creates a generic value changed handler for view models  Args:     page:            Page index     parameter_name:  Property name      view_model_type: Type (class name) of the view model  Returns:     Callable: Event handler function that is called when the value changes |
| `set_modify_property_callback` | `self, callback: Callable[[int, str, Any], None]` | `None` | Set callback for property value changes  Args:     callback: Function to be called when value of a property changes |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the wpf palette change handler that handles change events from the palette
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

class WpfPaletteChangeHandler:
    """ implementation of the palette change handler
    """

    # Maps the view model type (class name) to a property that holds the value of the control
    # This will be later extended to support all view models that have a value

    _VALUE_PROPERTY_MAP = {
        'ContructionPointSymbolViewModel': lambda vm: vm.SelectedValue.Value
    }

    def __init__(self):
        """ initialize

        Args:
            
        """

        self._modify_property_callback = None

    def create_value_changed_handler(self,
                                     page            : int,
                                     parameter_name  : str,
                                     view_model_type : str) -> Callable[[Any], None]:
        """Creates a generic value changed handler for view models
        
        Args:
            page:            Page index
            parameter_name:  Property name 
            view_model_type: Type (class name) of the view model
        
        Returns:
            Callable: Event handler function that is called when the value changes
        """
        def on_value_changed(changed_parameter):
            if self._modify_property_callback and (get_value := self._VALUE_PROPERTY_MAP.get(view_model_type)):
                value = get_value(changed_parameter)
                self._modify_property_callback(page, parameter_name, value)

        return on_value_changed

    def set_modify_property_callback(self,
                                     callback: Callable[[int, str, Any], None]):
        """Set callback for property value changes

        Args:
            callback: Function to be called when value of a property changes
        """
        self._modify_property_callback = callback

```

</details>