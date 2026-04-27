---
title: "BuildingElementMigrationUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementMigrationUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementMigrationUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementMigrationUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

Implementation of the migration utilities for the building element 

## Abhängigkeiten

- `typing`

## Klassen

### `BuildingElementMigrationUtil`

Implementation of the migration utilities for the building element 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `transfer_parameter_value` | `parameter_list: List[str], old_element_id: str, old_value_name: str, new_element_id: str, new_value_name: str, converter_function: Optional[Callable]=None, append_parameter: bool=False` | `None` | transfer a parameter value for an old ID and name to a new ID and name  Args:  parameter_list    : list with the parameter names and values old_element_id    : old element ID of the PythonPart old_value_name    : old value name new_element_id    : new element ID of the PythonPart new_value_name    : new value name converter_function: convert function for the value as converter_function(value: str) -> str append_parameter  : append the parameter (False replaces the old parameter) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the migration utilities for the building element """

from typing import Callable, List, Optional

class BuildingElementMigrationUtil():
    """ Implementation of the migration utilities for the building element """

    @staticmethod
    def transfer_parameter_value(parameter_list    : List[str],
                                 old_element_id    : str,
                                 old_value_name    : str,
                                 new_element_id    : str,
                                 new_value_name    : str,
                                 converter_function: Optional[Callable] = None,
                                 append_parameter  : bool = False)            :
        """ transfer a parameter value for an old ID and name to a new ID and name

            Args:

            parameter_list    : list with the parameter names and values
            old_element_id    : old element ID of the PythonPart
            old_value_name    : old value name
            new_element_id    : new element ID of the PythonPart
            new_value_name    : new value name
            converter_function: convert function for the value as converter_function(value: str) -> str
            append_parameter  : append the parameter (False replaces the old parameter)
        """

        old_value_name += "="
        new_value_name += "="

        start_index = next((index for index, old_parameter in enumerate(parameter_list) if old_parameter.find(old_element_id) != -1), -1)

        if start_index == -1:
            print("------------------------------")
            print("no migration (node doesn't exist anymore)")
            print("------------------------------")
            return

        for index in range(start_index, len(parameter_list)):
            old_parameter = parameter_list[index]

            if old_parameter.find("-------------------") != -1:
                break

            if not old_parameter.startswith(old_value_name):
                continue

            org_old_parameter = old_parameter.replace("\n", "")

            old_parameter = old_parameter[old_parameter.find("=") + 1:]

            if converter_function:
                old_parameter = converter_function(old_parameter)

            parameter = new_value_name + old_parameter

            if old_element_id == new_element_id:
                if append_parameter:
                    parameter_list.insert(index, parameter)
                else:
                    parameter_list[index] = parameter

                print("------------------------------")
                print("Migrate " + org_old_parameter + " to " + parameter)
                print("------------------------------")

                return

            del parameter_list[index]

            print("------------------------------")
            print("Migrate " + org_old_parameter + " to " + parameter)
            print("------------------------------")


            #---------------- delete the old id if empty

            if parameter_list[index - 1].find(old_element_id) != -1 and parameter_list[index].find("-------------------") != -1:
                del parameter_list[index - 1: index + 1]


            #---------------- append the new value

            index = next((index for index, new_id_entry in enumerate(parameter_list) if new_id_entry.find(new_element_id) != -1), -1)

            if index == -1:
                parameter_list.append("__ElementID=" + new_element_id + "___\n")
                parameter_list.append(parameter)
                parameter_list.append("-------------------\n")

                return

            parameter_list.insert(index + 1, parameter)

            return

        print("------------------------------")
        print("no migration (old parameter doesn't exist anymore)")
        print("------------------------------")

```

</details>