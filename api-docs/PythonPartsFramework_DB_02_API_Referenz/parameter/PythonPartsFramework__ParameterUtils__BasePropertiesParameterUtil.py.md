---
title: "BasePropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\BasePropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BasePropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\BasePropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implements the BasePropertiesParameterUtil class

## Abhängigkeiten

- `BuildingElement`
- `typing`

## Klassen

### `BasePropertiesParameterUtil`

implements the BasePropertiesParameterUtil class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele: BuildingElement, name_postfix: str` | `None` | initialize  Args:     build_ele:    building element with the parameter properties     name_postfix: postfix of the parameter names |
| `get_parameter_value` | `self, name: str` | `Any` | get the parameter value  Args:     name: parameter name  Returns:     parameter value |
| `get_modified_parameter_value` | `self, name: str, current_value: Any` | `Any` | get the modified parameter value or the current value if not modified  Args:     name:          parameter name     current_value: current parameter value  Returns:     parameter value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implements the BasePropertiesParameterUtil class
"""

from typing import Any

from BuildingElement import BuildingElement

class BasePropertiesParameterUtil():
    """ implements the BasePropertiesParameterUtil class
    """

    def __init__(self,
                 build_ele   : BuildingElement,
                 name_postfix: str):
        """ initialize

        Args:
            build_ele:    building element with the parameter properties
            name_postfix: postfix of the parameter names
        """

        self.build_ele    = build_ele
        self.name_postfix = name_postfix


    def get_parameter_value(self,
                            name: str) -> Any:
        """ get the parameter value

        Args:
            name: parameter name

        Returns:
            parameter value
        """

        return self.build_ele.get_existing_property(f"{name}{self.name_postfix}").value


    def get_modified_parameter_value(self,
                                     name         : str,
                                     current_value: Any) -> Any:
        """ get the modified parameter value or the current value if not modified

        Args:
            name:          parameter name
            current_value: current parameter value

        Returns:
            parameter value
        """

        prop = self.build_ele.get_existing_property(f"{name}{self.name_postfix}")

        return prop.get_unique_value(current_value)

```

</details>