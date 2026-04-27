---
title: "ControlPropertiesValueListUtil"
source: "PythonPartsFramework\GeneralScripts\ControlPropertiesValueListUtil.py"
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


# ControlPropertiesValueListUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ControlPropertiesValueListUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

Implementation of the utilities for the control properties value list

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `ControlProperties`
- `ParameterProperty`
- `__future__`
- `typing`

## Klassen

### `ControlPropertiesValueListUtil`

Implementation of the utilities for the control properties value list 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `validate_values` | `build_ele: BuildingElement, ctrl_props: BuildingElementControlProperties, parameter_dict: dict[str, Any]` | `bool` | check and adapt the values accordingly to the values in the value list  Args:     build_ele:      building element with the parameter properties     ctrl_props:     control property list     parameter_dict: parameter dictionary for the range command  Returns:     True in case of adapted values, otherwise False |
| `validate_value` | `ctrl_prop: ControlProperties, prop: ParameterProperty, value: Any, parameter_dict: dict[str, Any]` | `tuple[bool, Any]` | check and adapt the value accordingly to the values in the value list  Args:     ctrl_prop     : control property     prop          : parameter property     value         : value to test     parameter_dict: parameter dictionary for the range command  Returns:    (value was updated, value if present in the list or nearest value from the list) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the utilities for the control properties value list
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from ControlProperties import ControlProperties

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from BuildingElementControlProperties import BuildingElementControlProperties
    from ParameterProperty import ParameterProperty

class ControlPropertiesValueListUtil():
    """ Implementation of the utilities for the control properties value list """

    @staticmethod
    def validate_values(build_ele     : BuildingElement,
                        ctrl_props    : BuildingElementControlProperties,
                        parameter_dict: dict[str, Any]) -> bool:
        """ check and adapt the values accordingly to the values in the value list

        Args:
            build_ele:      building element with the parameter properties
            ctrl_props:     control property list
            parameter_dict: parameter dictionary for the range command

        Returns:
            True in case of adapted values, otherwise False
        """

        is_adapted = False

        for ctrl_prop in ctrl_props:
            if (prop := build_ele.get_property(ctrl_prop.value_name)):
                has_new_value, value = ControlPropertiesValueListUtil.validate_value(ctrl_prop, prop, prop.value, parameter_dict)

                if has_new_value:
                    prop.value = value

                is_adapted = is_adapted or has_new_value

        return is_adapted


    @staticmethod
    def validate_value(ctrl_prop     : ControlProperties,
                       prop          : ParameterProperty,
                       value         : Any,
                       parameter_dict: dict[str, Any]) -> tuple[bool, Any]:
        """ check and adapt the value accordingly to the values in the value list

        Args:
            ctrl_prop     : control property
            prop          : parameter property
            value         : value to test
            parameter_dict: parameter dictionary for the range command

        Returns:
           (value was updated, value if present in the list or nearest value from the list)
        """

        if not ctrl_prop.value_list or ctrl_prop.value_dialog:
            return False, value

        if prop.value_list_util is not None:
            return False, value

        value_type = prop.value_type.replace("combobox", "")

        if value_type not in {"angle", "area", "double", "integer", "length", "string", "volume", "weight"}:
            return False, value

        return prop.value_type.validate_for_list_value(value, prop.value_type, ctrl_prop.value_list, parameter_dict)

```

</details>