---
title: "BaseValueToStringConverter"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\BaseValueToStringConverter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BaseValueToStringConverter

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\BaseValueToStringConverter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the base functions for the value to string conversion

## Abhängigkeiten

- `typing`

## Klassen

### `BaseValueToStringConverter`

implementation of the base functions for the value to string conversion
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `enum_to_string` | `value: Any` | `str` | convert an enum to a string  Args:     value: enum value  Returns:     string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the base functions for the value to string conversion
"""

from typing import Any

class BaseValueToStringConverter():
    """ implementation of the base functions for the value to string conversion
    """

    @staticmethod
    def enum_to_string(value: Any) -> str:
        """ convert an enum to a string

        Args:
            value: enum value

        Returns:
            string
        """

        value_str = repr(value)

        match value.__module__:
            case "NemAll_Python_ArchElements":
                return value_str.replace(value.__module__, "AllplanArchEle")

            case "NemAll_Python_BaseElements":
                return value_str.replace(value.__module__, "AllplanBaseEle")

            case "NemAll_Python_BasisElements":
                return value_str.replace(value.__module__, "AllplanBasisEle")

            case "NemAll_Python_Geometry":
                return value_str.replace(value.__module__, "AllplanGeo")

            case "NemAll_Python_IFW_Input":
                return value_str.replace(value.__module__, "AllplanIFW")

            case "NemAll_Python_Palette":
                return value_str.replace(value.__module__, "AllplanPalette")

            case "NemAll_Python_Reinforcement":
                return value_str.replace(value.__module__, "AllplanReinf")

            case "NemAll_Python_AllplanSettings":
                return value_str.replace(value.__module__, "AllplanSettings")

            case "NemAll_Python_Utility":
                return value_str.replace(value.__module__, "AllplanUtil")

        return ""

```

</details>