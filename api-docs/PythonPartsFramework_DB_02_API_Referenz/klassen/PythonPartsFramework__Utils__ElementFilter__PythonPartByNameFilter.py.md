---
title: "PythonPartByNameFilter"
source: "PythonPartsFramework\Utils\ElementFilter\PythonPartByNameFilter.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PythonPartByNameFilter

> **Pfad:** `PythonPartsFramework\Utils\ElementFilter\PythonPartByNameFilter.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the PythonPart by name filter

## Abhängigkeiten

- `BuildingElementSubElementUtil`
- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`
- `ScriptObjectInteractors.BaseFilterObject`

## Klassen

### `PythonPartByNameFilter`

implementation of the PythonPart by name filter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, ref_pyp_ele: AllplanEleAdapter.BaseElementAdapter` | `None` | initialize  Args:     ref_pyp_ele: reference PythonPart |
| `__call__` | `self, element: AllplanEleAdapter.BaseElementAdapter` | `bool` | execute the filtering  Args:     element: element to filter  Returns:     element fulfills the filter: True/False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart by name filter
"""

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from ScriptObjectInteractors.BaseFilterObject import BaseFilterObject

from BuildingElementSubElementUtil import BuildingElementSubElementUtil

class PythonPartByNameFilter(BaseFilterObject):
    """ implementation of the PythonPart by name filter
    """

    def __init__(self,
                 ref_pyp_ele: AllplanEleAdapter.BaseElementAdapter):
        """ initialize

        Args:
            ref_pyp_ele: reference PythonPart
        """

        self.ref_pyp_ele = ref_pyp_ele

        _, ref_pyp_name, _ = AllplanBaseEle.PythonPartService.GetParameter(ref_pyp_ele)

        self.ref_pyp_name = ref_pyp_name.lower()

        _, _, parameter = AllplanBaseEle.PythonPartService.GetParameter(ref_pyp_ele)

        self.sub_file_name     = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter, "SubElementsName")
        self.add_sub_file_name = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter, "__AddPypSubFile__")


    def __call__(self, element: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ execute the filtering

        Args:
            element: element to filter

        Returns:
            element fulfills the filter: True/False
        """

        if not AllplanBaseEle.PythonPartService.IsPythonPartElement(element) and \
           not AllplanBaseEle.PythonPartService.IsPythonPartGroupElement(element):
            return False

        _, name, _ = AllplanBaseEle.PythonPartService.GetParameter(element)

        name = name.lower()

        if not name.endswith(self.ref_pyp_name) and not self.ref_pyp_name.endswith(name):
            return False

        #----------------- check the sub elements name

        _, _, parameter = AllplanBaseEle.PythonPartService.GetParameter(element)

        if self.sub_file_name != BuildingElementSubElementUtil.get_file_name_from_parameter(parameter, "SubElementsName"):
            return False

        if self.add_sub_file_name != BuildingElementSubElementUtil.get_file_name_from_parameter(parameter, "__AddPypSubFile__"):
            return False

        return True

```

</details>