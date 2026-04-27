---
title: "BaseFilterObject"
source: "PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\BaseFilterObject.py"
type: "class"
category: "02_API_Referenz"
tags:
  - interactor
  - script
related:
  -
last_updated: "2026-02-20"
---


# BaseFilterObject

> **Pfad:** `PythonPartsFramework\GeneralScripts\ScriptObjectInteractors\BaseFilterObject.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `interactor`, `script`

## Übersicht

implementation of the base filter object

## Abhängigkeiten

- `NemAll_Python_IFW_ElementAdapter`
- `abc`

## Klassen

### `BaseFilterObject`

implementation of the base filter object
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self, _element: AllplanEleAdapter.BaseElementAdapter` | `bool` | execute the filtering  Args:     _element: element to filter  Returns:     element fulfills the filter: True/False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base filter object
"""

import abc

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter


class BaseFilterObject():
    """ implementation of the base filter object
    """

    @abc.abstractmethod
    def __call__(self,
                 _element: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ execute the filtering

        Args:
            _element: element to filter

        Returns:
            element fulfills the filter: True/False
        """

```

</details>