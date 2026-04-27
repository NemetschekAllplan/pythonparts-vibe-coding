---
title: "ElementConnectorParameterList"
source: "PythonPartsFramework\TypeCollections\ElementConnectorParameterList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - connector
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# ElementConnectorParameterList

> **Pfad:** `PythonPartsFramework\TypeCollections\ElementConnectorParameterList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `connector`, `parameter`

## Übersicht

Implementation of the list for the element connector parameter

The ParameterProperty is the parameter property of the connection like PointConnection, ...

## Abhängigkeiten

- `ParameterProperty`

## Klassen

### `ElementConnectorParameterList`

Implementation of the list for the element connector parameter

The ParameterProperty is the parameter property of the connection like PointConnection, ...

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
""" Implementation of the list for the element connector parameter

    The ParameterProperty is the parameter property of the connection like PointConnection, ...
"""

from ParameterProperty import ParameterProperty

class ElementConnectorParameterList(list[ParameterProperty]):
    """ Implementation of the list for the element connector parameter

        The ParameterProperty is the parameter property of the connection like PointConnection, ...
    """

```

</details>