---
title: "BuildingElementParameterUtil"
source: "PythonPartsFramework\Utils\General\BuildingElementParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementParameterUtil

> **Pfad:** `PythonPartsFramework\Utils\General\BuildingElementParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the building element parameter utility

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementConverter`
- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`

## Klassen

### `BuildingElementParameterUtil`

implementation of the building element parameter utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `fill_parameter_from_python_part` | `build_ele: BuildingElement, python_part: AllplanEleAdapter.BaseElementAdapter, org_and_copy_ele_guids: dict[str, str]` | `None` | fill the parameter of the building element from the python part  Args:     build_ele:              building element with the parameter properties     python_part:            Python part element adapter     org_and_copy_ele_guids: original and copy element guids |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the building element parameter utility
"""

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from BuildingElement import BuildingElement
from BuildingElementConverter import BuildingElementConverter

class BuildingElementParameterUtil():
    """ implementation of the building element parameter utility
    """

    @staticmethod
    def fill_parameter_from_python_part(build_ele             : BuildingElement,
                                        python_part           : AllplanEleAdapter.BaseElementAdapter,
                                        org_and_copy_ele_guids: dict[str, str]):
        """ fill the parameter of the building element from the python part

        Args:
            build_ele:              building element with the parameter properties
            python_part:            Python part element adapter
            org_and_copy_ele_guids: original and copy element guids
        """

        _, _, parameters = AllplanBaseEle.PythonPartService.GetParameter(python_part)

        BuildingElementConverter.read_from_list(build_ele, parameters)

```

</details>