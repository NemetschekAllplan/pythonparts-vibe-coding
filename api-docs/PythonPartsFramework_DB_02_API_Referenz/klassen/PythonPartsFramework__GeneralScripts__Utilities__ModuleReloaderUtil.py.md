---
title: "ModuleReloaderUtil"
source: "PythonPartsFramework\GeneralScripts\Utilities\ModuleReloaderUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ModuleReloaderUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\Utilities\ModuleReloaderUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the module reloader utility

## Abhängigkeiten

- Keine

## Klassen

### `ModuleReloaderUtil`

Module reloader utility class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_reload` | `cls` | `None` | set the reload state          |
| `reset_reload` | `cls` | `None` | reset the reload state          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the module reloader utility
"""

class ModuleReloaderUtil:
    """ Module reloader utility class
    """

    RELOAD_MODULE = False

    @classmethod
    def set_reload(cls):
        """ set the reload state
        """

        cls.RELOAD_MODULE = True

    @classmethod
    def reset_reload(cls):
        """ reset the reload state
        """

        cls.RELOAD_MODULE = False

```

</details>