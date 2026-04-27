---
title: "DocumentManager"
source: "PythonPartsFramework\GeneralScripts\DocumentManager.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# DocumentManager

> **Pfad:** `PythonPartsFramework\GeneralScripts\DocumentManager.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Script for DocumentManager functions

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_IFW_ElementAdapter`
- `TypeCollections.ModificationElementList`
- `__future__`
- `typing`

## Klassen

### `DocumentManager`

Singleton class for the document manager 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | Constructor  Raises:     PermissionError: if no instance exist |
| `get_instance` | `-` | `DocumentManager` | Get the one an only instance for the document manager  Returns:     DocumentManager object |
| `document` | `self` | `AllplanEleAdapter.DocumentAdapter` | get the document  Returns:     get the document |
| `document` | `self, document: AllplanEleAdapter.DocumentAdapter` | `None` | set the document  Args:     document: document |
| `pythonpart_element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | get the PythonPart element  Returns:     get the PythonPart element |
| `clear_pythonpart_element` | `self` | `None` | clear the PythonPart element          |
| `set_pythonpart_element` | `self, modification_ele_list: ModificationElementList` | `None` | set the PythonPart element from the model element UUID  Args:     modification_ele_list: list with the modification elements in modification mode |
| `asso_ref_element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | get the asso_ref element  Returns:     get the asso_ref element |
| `asso_ref_element` | `self, asso_ref_element: AllplanEleAdapter.BaseElementAdapter` | `None` | set the asso_ref element  Args:     asso_ref_element: asso_ref_element |
| `clear_asso_ref_element` | `self` | `None` | clear the asso_ref element          |
| `take_over_element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | get the take over element  Returns:     get the take over element |
| `take_over_element` | `self, take_over_element: AllplanEleAdapter.BaseElementAdapter` | `None` | set the take over element  Args:     take_over_element: take over element |
| `common_properties` | `self` | `AllplanBaseEle.CommonProperties` | get the common properties  Returns:     common properties of the modified PythonPart |
| `sub_pythonparts` | `self` | `dict[str, AllplanEleAdapter.BaseElementAdapter]` | get the sub PythonParts  Returns:     sub PythonParts |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for DocumentManager functions
"""

# pylint: disable=unused-private-member

from __future__ import annotations

from typing import cast

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from TypeCollections.ModificationElementList import ModificationElementList

DOC_MANAGER_INST = "DocumentManager__instance"

class DocumentManager():
    """ Singleton class for the document manager """

    if DOC_MANAGER_INST not in globals():
        globals()[DOC_MANAGER_INST] = None

    def __init__(self):
        """ Constructor

            Raises:
                PermissionError: if no instance exist
        """

        if globals()[DOC_MANAGER_INST] is not None:
            raise PermissionError("DocumentManager is a singleton")

        globals()[DOC_MANAGER_INST] = self

        self.__document           = AllplanEleAdapter.DocumentAdapter()
        self.__pythonpart_element = AllplanEleAdapter.BaseElementAdapter()
        self.__asso_ref_element   = AllplanEleAdapter.BaseElementAdapter()
        self.__take_over_element  = AllplanEleAdapter.BaseElementAdapter()
        self.__common_properties  = AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties()

        self.__sub_pythonparts = dict[str, AllplanEleAdapter.BaseElementAdapter]()


    @staticmethod
    def get_instance() -> DocumentManager:
        """ Get the one an only instance for the document manager

        Returns:
            DocumentManager object
        """

        if globals()[DOC_MANAGER_INST] is None:
            DocumentManager()

        return globals()[DOC_MANAGER_INST]


    @property
    def document(self) -> AllplanEleAdapter.DocumentAdapter:
        """ get the document

        Returns:
            get the document
        """

        return self.__document


    @document.setter
    def document(self,
                 document: AllplanEleAdapter.DocumentAdapter):
        """ set the document

        Args:
            document: document
        """

        self.__document = document


    @property
    def pythonpart_element(self) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the PythonPart element

        Returns:
            get the PythonPart element
        """

        return self.__pythonpart_element


    def clear_pythonpart_element(self):
        """ clear the PythonPart element
        """

        self.__pythonpart_element = AllplanEleAdapter.BaseElementAdapter()
        self.__sub_pythonparts    = dict[str, AllplanEleAdapter.BaseElementAdapter]()
        self.__take_over_element  = AllplanEleAdapter.BaseElementAdapter()


    def set_pythonpart_element(self,
                               modification_ele_list: ModificationElementList):
        """ set the PythonPart element from the model element UUID

        Args:
            modification_ele_list: list with the modification elements in modification mode
        """

        if self.document is None:
            return

        if not modification_ele_list.is_modification_element():
            self.__pythonpart_element = AllplanEleAdapter.BaseElementAdapter()

        elif isinstance(modification_ele_list[0], AllplanEleAdapter.BaseElementAdapter):
            self.__pythonpart_element = cast(AllplanEleAdapter.BaseElementAdapter, modification_ele_list[0])

        else:
            self.__pythonpart_element = modification_ele_list.get_base_element_adapter(self.document)

        if self.pythonpart_element.IsNull():
            self.__common_properties  = AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties()
            return


        #----------------- set the element data

        model_ele = cast(AllplanBasisEle.MacroPlacementElement, AllplanBaseEle.GetElement(self.pythonpart_element))

        self.__common_properties = model_ele.GetCommonProperties()

        if not AllplanBaseEle.PythonPartService.IsPythonPartGroupElement(self.pythonpart_element):
            return

        for sub_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(self.pythonpart_element, True):
            attributes = sub_ele.GetAttributes(AllplanBaseEle.eAttibuteReadState.ReadWithoutGeometry)

            if (sub_key := next((attribute[1] for attribute in attributes \
                                if attribute[0] == AllplanBaseEle.ATTRNR_SUB_PYTHONPART_KEY), None)) is not None:
                self.__sub_pythonparts[sub_key] = sub_ele


    @property
    def asso_ref_element(self) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the asso_ref element

        Returns:
            get the asso_ref element
        """

        return self.__asso_ref_element


    @asso_ref_element.setter
    def asso_ref_element(self,
                         asso_ref_element: AllplanEleAdapter.BaseElementAdapter):
        """ set the asso_ref element

        Args:
            asso_ref_element: asso_ref_element
        """

        self.__asso_ref_element = asso_ref_element


    def clear_asso_ref_element(self):
        """ clear the asso_ref element
        """

        self.__asso_ref_element = AllplanEleAdapter.BaseElementAdapter()


    @property
    def take_over_element(self) -> AllplanEleAdapter.BaseElementAdapter:
        """ get the take over element

        Returns:
            get the take over element
        """

        return self.__take_over_element

    @take_over_element.setter
    def take_over_element(self,
                          take_over_element: AllplanEleAdapter.BaseElementAdapter):
        """ set the take over element

        Args:
            take_over_element: take over element
        """

        self.__take_over_element = take_over_element


    @property
    def common_properties(self) -> AllplanBaseEle.CommonProperties:
        """ get the common properties

        Returns:
            common properties of the modified PythonPart
        """

        return self.__common_properties


    @property
    def sub_pythonparts(self) -> dict[str, AllplanEleAdapter.BaseElementAdapter]:
        """ get the sub PythonParts

        Returns:
            sub PythonParts
        """

        return self.__sub_pythonparts

```

</details>