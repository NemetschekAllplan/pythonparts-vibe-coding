---
title: "BuildingElementParamPropValues"
source: "PythonPartsFramework\GeneralScripts\BuildingElementParamPropValues.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementParamPropValues

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementParamPropValues.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of BuildingElementParamPropValues class

This class is used to hold parameter property values for the building element.
It allows adding properties and constants dynamically, and provides methods
to get and set property values.

## Abhängigkeiten

- `BuildingElement`
- `__future__`
- `typing`

## Klassen

### `BuildingElementParamPropValues`

Class to hold parameter property values for building elements.
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele: BuildingElement` | `None` | Initialize with a BuildingElement instance.  Args:     build_ele: building element with the parameter properties |
| `add_property` | `self, name: str` | `None` | Add a new property to class  Args:     name: the name of the property. |
| `add_constant` | `self, name: str` | `None` | Add a new constant to class  Args:     name: the name of the constant |
| `__get_value` | `self, name: str` | `Any` | Get the value of a property.  Args:     name: the name of the property.  Returns:     value of the property |
| `__set_value` | `self, name: str, value: Any` | `None` | Set the value of a property.  Args:     name:  the name of the property.     value: value to set for the property. |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of BuildingElementParamPropValues class

    This class is used to hold parameter property values for the building element.
    It allows adding properties and constants dynamically, and provides methods
    to get and set property values.
"""

# pylint: disable=unnecessary-lambda-assignment

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from BuildingElement import BuildingElement

class BuildingElementParamPropValues:
    """ Class to hold parameter property values for building elements.
    """

    def __init__(self,
                 build_ele: BuildingElement):
        """ Initialize with a BuildingElement instance.

        Args:
            build_ele: building element with the parameter properties
        """

        self.build_ele = build_ele


    def add_property(self,
                     name: str):
        """ Add a new property to class

        Args:
            name: the name of the property.
        """

        fget = lambda self: self.__get_value(name)
        fset = lambda self, value: self.__set_value(name, value)

        setattr(self.__class__, name, property(fget, fset))


    def add_constant(self,
                     name: str):
        """ Add a new constant to class

        Args:
            name: the name of the constant
        """

        fget = lambda self: getattr(self.build_ele, name, None)

        setattr(self.__class__, name, property(fget))


    def __get_value(self,
                    name: str) -> Any:
        """ Get the value of a property.

        Args:
            name: the name of the property.

        Returns:
            value of the property
        """

        return None if (prop := self.build_ele.get_property(name)) is None else prop.value


    def __set_value(self,
                    name : str,
                    value: Any):
        """ Set the value of a property.

        Args:
            name:  the name of the property.
            value: value to set for the property.
        """

        if (prop := self.build_ele.get_property(name)) is not None:
            prop.value = value

```

</details>