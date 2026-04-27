---
title: "BaseConnection"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Data\BaseConnection.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BaseConnection

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Data\BaseConnection.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the base data class for the connection data

## Abhängigkeiten

- `abc`
- `dataclasses`

## Klassen

### `BaseConnection`

implementation of the base data class for the connection data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `deep_copy` | `self` | `None` | deep copy  Returns:     deep copy |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base data class for the connection data
"""

from dataclasses import dataclass

import abc

@dataclass
class BaseConnection(abc.ABC):
    """ implementation of the base data class for the connection data
    """

    @abc.abstractmethod
    def deep_copy(self):
        """ deep copy

        Returns:
            deep copy
        """

```

</details>