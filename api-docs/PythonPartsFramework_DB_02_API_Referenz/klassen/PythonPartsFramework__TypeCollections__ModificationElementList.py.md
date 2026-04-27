---
title: "ModificationElementList"
source: "PythonPartsFramework\TypeCollections\ModificationElementList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# ModificationElementList

> **Pfad:** `PythonPartsFramework\TypeCollections\ModificationElementList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dokumentation`

## Übersicht

implementation of the list with the data of the modification elements

## Abhängigkeiten

- `NemAll_Python_IFW_ElementAdapter`
- `typing`

## Klassen

### `ModificationElementList`

implementation of the list with the data of the modification elements
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, elements: list[str | AllplanEleAdapter.BaseElementAdapter] | None=None` | `None` | initialize  Args:     elements: elements to modify |
| `is_modification_element` | `self` | `bool` | check for an existing modification element  Returns:     modification element state |
| `get_base_element_adapter` | `self, doc: AllplanEleAdapter.DocumentAdapter` | `AllplanEleAdapter.BaseElementAdapter` | get the BaseElementAdapter of the first element  Args:     doc: document of the Allplan drawing files  Returns:     BaseElementAdapter |
| `get_base_element_adapter_list` | `self, doc: AllplanEleAdapter.DocumentAdapter` | `list[AllplanEleAdapter.BaseElementAdapter]` | get the BaseElementAdapter of the elements  Args:     doc: document of the Allplan drawing files  Returns:     BaseElementAdapter of the elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the list with the data of the modification elements
"""

from typing import cast

import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

class ModificationElementList(list[(str | AllplanEleAdapter.BaseElementAdapter)]):
    """ implementation of the list with the data of the modification elements
    """

    EMPTY_GUID         = "00000000-0000-0000-0000-000000000000--0"
    EMPTY_ADAPTER_GUID = "00000000-0000-0000-0000-000000000000"

    def __init__(self,
                 elements: (list[(str | AllplanEleAdapter.BaseElementAdapter)] | None) = None):
        """ initialize

        Args:
            elements: elements to modify
        """

        if elements is None:
            return

        for ele in elements:
            if isinstance(ele, AllplanEleAdapter.BaseElementAdapter):
                self.append(f"{ele.GetModelElementUUID()}--0")

            elif isinstance(ele, str):
                if not ele.endswith("--0"):
                    self.append(f"{ele}--0")
                else:
                    self.append(ele)

            else:
                self.append(ele)


    def is_modification_element(self) -> bool:
        """ check for an existing modification element

        Returns:
            modification element state
        """

        if not self:
            return False

        return isinstance(self[0], AllplanEleAdapter.BaseElementAdapter) and not self[0].IsNull() or \
               self[0] != self.EMPTY_GUID


    def get_base_element_adapter(self,
                                 doc: AllplanEleAdapter.DocumentAdapter) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the BaseElementAdapter of the first element

        Args:
            doc: document of the Allplan drawing files

        Returns:
            BaseElementAdapter
        """

        if not self:
            return AllplanEleAdapter.BaseElementAdapter()

        return AllplanEleAdapter.BaseElementAdapter.FromGUID(AllplanEleAdapter.GUID.FromString(cast(str, self[0])[:-3]), doc)


    def get_base_element_adapter_list(self,
                                      doc: AllplanEleAdapter.DocumentAdapter) -> list[AllplanEleAdapter.BaseElementAdapter]:
        """ get the BaseElementAdapter of the elements

        Args:
            doc: document of the Allplan drawing files

        Returns:
            BaseElementAdapter of the elements
        """

        return [AllplanEleAdapter.BaseElementAdapter.FromGUID(AllplanEleAdapter.GUID.FromString(cast(str, ele)[:-3]), doc)
                for ele in self if isinstance(ele, str)]

```

</details>