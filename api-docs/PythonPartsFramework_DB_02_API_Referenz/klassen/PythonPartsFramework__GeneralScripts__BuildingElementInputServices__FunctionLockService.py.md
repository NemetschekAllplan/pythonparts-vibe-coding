---
title: "FunctionLockService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\FunctionLockService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# FunctionLockService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\FunctionLockService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the function lock service

## Abhängigkeiten

- `BuildingElementPaletteService`
- `HandleModificationService`
- `NemAll_Python_AllplanSettings`
- `PythonPartPreview`

## Klassen

### `FunctionLockService`

implementation of the function lock service
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_is_only_update_locks` | `is_only_update: bool, execution_event: AllplanSettings.ExecutionEvent` | `None` | set the is only update locks  Args:     is_only_update:  only update the PythonPart, no user interaction     execution_event: execution event |
| `reset_is_only_update_locks` | `-` | `None` | reset the is only update locks          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the function lock service
"""

import NemAll_Python_AllplanSettings as AllplanSettings

from BuildingElementPaletteService import BuildingElementPaletteService
from HandleModificationService import HandleModificationService
from PythonPartPreview import PythonPartPreview


class FunctionLockService:
    """ implementation of the function lock service
    """

    @staticmethod
    def set_is_only_update_locks(is_only_update : bool,
                                 execution_event: AllplanSettings.ExecutionEvent):
        """ set the is only update locks

        Args:
            is_only_update:  only update the PythonPart, no user interaction
            execution_event: execution event
        """

        BuildingElementPaletteService.set_palette_lock(is_only_update or execution_event == AllplanSettings.ExecutionEvent.eHandles)

        HandleModificationService.set_handle_draw_lock(is_only_update)

        PythonPartPreview.set_preview_draw_lock(is_only_update or execution_event == AllplanSettings.ExecutionEvent.eHandles)


    @staticmethod
    def reset_is_only_update_locks():
        """ reset the is only update locks
        """

        BuildingElementPaletteService.set_palette_lock(False)

        HandleModificationService.set_handle_draw_lock(False)

        PythonPartPreview.set_preview_draw_lock(False)
```

</details>