---
title: "ConditionUtil"
source: "PythonPartsFramework\GeneralScripts\Utilities\ConditionUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ConditionUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\Utilities\ConditionUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the condition utilities

## Abhängigkeiten

- `GeneralConstants`
- `typing`

## Klassen

### `ConditionUtil`

implementation of the condition utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `modify_condition` | `value_name: str, condition: str, value: str` | `str` | Modify the condition  Args:     value_name: name of the value     condition:  visible condition     value:      condition value  Returns:     modified condition |
| `get_condition_dict` | `condition_str: str, value_name: str, param_dict: dict[str, Any]` | `dict[str, bool]` | Get the condition dictionary  Args:     condition_str: condition     value_name:    value name     param_dict:    parameter dictionary  Returns:     condition dictionary |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the condition utilities
"""

from typing import Any

from .GeneralConstants import GeneralConstants

class ConditionUtil():
    """ implementation of the condition utilities
    """

    @staticmethod
    def modify_condition(value_name: str,
                         condition : str,
                         value     : str) -> str:
        """ Modify the condition

        Args:
            value_name: name of the value
            condition:  visible condition
            value:      condition value

        Returns:
            modified condition
        """

        if GeneralConstants.SUB_NAME_SEPARATOR not in value_name:
            if GeneralConstants.TEXT_SEPARATOR not in condition:
                return value

            return value + GeneralConstants.TEXT_SEPARATOR + condition.split(GeneralConstants.TEXT_SEPARATOR, 1)[-1]

        sub_conds = condition.split(GeneralConstants.TEXT_SEPARATOR)

        value_name += ":"

        for index, sub_cond in enumerate(sub_conds):
            if sub_cond.startswith(value_name):
                sub_conds[index] = value_name + value

                return GeneralConstants.TEXT_SEPARATOR.join(sub_conds)

        return condition + GeneralConstants.TEXT_SEPARATOR + value_name + value


    @staticmethod
    def get_condition_dict(condition_str: str,
                           value_name   : str,
                           param_dict   : dict[str, Any]) -> dict[str, bool]:
        """ Get the condition dictionary

        Args:
            condition_str: condition
            value_name:    value name
            param_dict:    parameter dictionary

        Returns:
            condition dictionary
        """

        if not condition_str:
            return {}

        condition_list = condition_str.split(GeneralConstants.TEXT_SEPARATOR)

        condition_dict = {}

        for condition in condition_list:
            if (ip_colon := condition.find(":")) == -1:
                continue

            name = condition[:ip_colon]

            if GeneralConstants.LIST_SEPARATOR_START in value_name:
                if (pure_name := value_name.split(GeneralConstants.LIST_SEPARATOR_START, 1)[0]) == name:
                    name = value_name

                elif name.startswith(pure_name + GeneralConstants.SUB_NAME_SEPARATOR):
                    name = name.replace(pure_name + GeneralConstants.SUB_NAME_SEPARATOR, value_name + GeneralConstants.SUB_NAME_SEPARATOR)

                else:
                    name = value_name + GeneralConstants.SUB_NAME_SEPARATOR + name

            condition_dict[name] = eval(condition[ip_colon + 1:], param_dict)       # pylint: disable=eval-used

        return condition_dict

```

</details>