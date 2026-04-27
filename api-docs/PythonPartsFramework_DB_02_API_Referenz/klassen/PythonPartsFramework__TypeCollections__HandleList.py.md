---
title: "HandleList"
source: "PythonPartsFramework\TypeCollections\HandleList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
related:
  -
last_updated: "2026-02-20"
---


# HandleList

> **Pfad:** `PythonPartsFramework\TypeCollections\HandleList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`

## Übersicht

implementation of the handle list

## Abhängigkeiten

- `HandleProperties`
- `NemAll_Python_Geometry`
- `Utils.Geometry.TransformationStack`

## Klassen

### `HandleList`

implementation of the handle list
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, trans_stack: TransformationStack=TransformationStack(LengthUnit.MM, AngleUnit.RADIAN)` | `None` | initialize  Args:     trans_stack: transformation stack |
| `append` | `self, handle: HandleProperties` | `None` | add a handle to the list  Args:     handle: handle to add |
| `enable_transform` | `self` | `bool` | enable transformation  Returns:     True if transformation is enabled |
| `enable_transform` | `self, enable: bool` | `None` | set the transformation enabled  Args:     enable: True if transformation is enabled |
| `clear` | `self` | `None` | clear the handle list          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the handle list
"""

import NemAll_Python_Geometry as AllplanGeo

from HandleProperties import HandleProperties

from Utils.Geometry.TransformationStack import TransformationStack, LengthUnit, AngleUnit

class HandleList(list[HandleProperties]):
    """ implementation of the handle list
    """

    def __init__(self,
                 trans_stack: TransformationStack = TransformationStack(LengthUnit.MM, AngleUnit.RADIAN)):
        """ initialize

        Args:
            trans_stack: transformation stack
        """

        self.__trans_stack       = trans_stack
        self.__transform_enabled = True
        self.__unit_matrix       = AllplanGeo.Matrix3D()

        self.__unit_matrix.SetScaling(trans_stack.length_fac, trans_stack.length_fac, trans_stack.length_fac)


    def append(self,
               handle: HandleProperties):
        """ add a handle to the list

        Args:
            handle: handle to add
        """

        if self.__transform_enabled:
            handle.trans_matrix = self.__unit_matrix * AllplanGeo.Matrix3D(self.__trans_stack.trans_matrix)

        super().append(handle)


    @property
    def enable_transform(self) -> bool:
        """ enable transformation

        Returns:
            True if transformation is enabled
        """

        return self.__transform_enabled


    @enable_transform.setter
    def enable_transform(self,
                          enable: bool):
        """ set the transformation enabled

        Args:
            enable: True if transformation is enabled
        """

        self.__transform_enabled = enable


    def clear(self):
        """ clear the handle list
        """

        super().clear()

        self.__transform_enabled = True

```

</details>