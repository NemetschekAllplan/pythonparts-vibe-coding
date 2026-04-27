---
title: "XmlParameterInclude"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterInclude.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlParameterInclude

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterInclude.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `xml`

## Übersicht

implementation of the XML parameter include

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementMaterialStringTable`
- `BuildingElementStringTable`
- `FileNameService`
- `IncludeData`
- `NemAll_Python_AllplanSettings`
- `XmlElementTreeUtil`
- `XmlParentParameterData`
- `collections.abc`
- `itertools`
- `xml.etree`

## Klassen

### `XmlParameterInclude`

implementation of the XML parameter include
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele: BuildingElement, local_str_table: BuildingElementStringTable` | `None` | initialize  Args:     build_ele:       building element with the parameter properties     local_str_table: local string table |
| `execute` | `self, page_index: int, param: ElementTree.Element, parent_param_data: XmlParentParameterData, material_str_table: BuildingElementMaterialStringTable, get_parameter_data: Callable[[int, ElementTree.Element, XmlParentParameterData, BuildingElementMaterialStringTable, BuildingElementStringTable, IncludeData], None]` | `None` | Get the data from one expander parameter node  Args:     page_index:         page index / number     param:              this parameter node     parent_param_data:  data of the parent parameter     material_str_table: material string table     get_parameter_data: function for getting the parameter |
| `__get_include_visible_dict` | `self, param: ElementTree.Element` | `None` | get the visible dict for include  Args:     param: this parameter node |
| `__get_include_text_postfix` | `self, param: ElementTree.Element` | `list[str]` | get the text postfix for the include  Args:     param: this parameter node  Returns:     text postfix |
| `get_include_language_file` | `self, param: ElementTree.Element, pyp_path: str` | `None` | get the language file for the include  Args:     param:    this parameter node     pyp_path: path of the pyp file |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the XML parameter include
"""

from itertools import zip_longest
from xml.etree import ElementTree
from collections.abc import Callable

import NemAll_Python_AllplanSettings as AllplanSettings

from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from FileNameService import FileNameService

from .IncludeData import IncludeData
from .XmlElementTreeUtil import XmlElementTreeUtil
from .XmlParentParameterData import XmlParentParameterData

class XmlParameterInclude():
    """ implementation of the XML parameter include
    """

    def __init__(self,
                 build_ele      : BuildingElement,
                 local_str_table: BuildingElementStringTable):
        """ initialize

        Args:
            build_ele:       building element with the parameter properties
            local_str_table: local string table
        """

        self.local_str_table = local_str_table
        self.build_ele       = build_ele

        self.incl_visible : dict[str, str] = {}


    def execute(self,
                page_index        : int,
                param             : ElementTree.Element,
                parent_param_data : XmlParentParameterData,
                material_str_table: BuildingElementMaterialStringTable,
                get_parameter_data: Callable[[int, ElementTree.Element, XmlParentParameterData,
                                              BuildingElementMaterialStringTable, BuildingElementStringTable, IncludeData], None]):
        """ Get the data from one expander parameter node

        Args:
            page_index:         page index / number
            param:              this parameter node
            parent_param_data:  data of the parent parameter
            material_str_table: material string table
            get_parameter_data: function for getting the parameter
        """

        path = XmlElementTreeUtil.get_tag_data(param, 'Value')

        pyp_path = self.build_ele.pyp_file_path

        if not (global_incl_path := FileNameService.get_global_standard_path(path)):
            global_incl_path = f"{pyp_path}\\{path}"

        incl_ele = XmlElementTreeUtil.parse(global_incl_path)

        if not (names := XmlElementTreeUtil.get_tag_data(param, 'Name').split(";")):
            names = [""]


        #----------------- get the visible dict

        self.__get_include_visible_dict(param)


        #----------------- get the text postfix from the text IDs

        texts = self.__get_include_text_postfix(param)


        #----------------- set the language file for the include file

        self.get_include_language_file(param, pyp_path)


        #----------------- create the parameter for the defines postfixes

        for name_item, text_item in zip_longest(names, texts, fillvalue = ""):
            start, _, end = name_item.partition("-")

            if end:
                name_list = [str(index) for index in range(int(start), int(end) + 1)]
                text_list = name_list
            else:
                name_list = [name_item]
                text_list = [text_item]


            #------------- get the parameter

            for sub_name_postfix, sub_text_postfix in zip(name_list, text_list):
                for incl_param in XmlElementTreeUtil.get_children_by_title(incl_ele, 'Parameter'):
                    get_parameter_data(page_index, incl_param, parent_param_data, material_str_table, self.local_str_table,
                                       IncludeData(True, self.incl_visible, sub_name_postfix, sub_text_postfix))


    def __get_include_visible_dict(self,
                                   param: ElementTree.Element):
        """ get the visible dict for include

        Args:
            param: this parameter node
        """

        if (visible := XmlElementTreeUtil.get_tag_data(param, 'Visible', "Include")):
            for item in visible.split(";"):
                incl_name, _, incl_visible = item.partition(":")

                if not incl_visible:
                    incl_visible = incl_name
                    incl_name    = "__ALL__"

                self.incl_visible[incl_name] = incl_visible


    def __get_include_text_postfix(self,
                                   param: ElementTree.Element) -> list[str]:
        """ get the text postfix for the include

        Args:
            param: this parameter node

        Returns:
            text postfix
        """

        texts = XmlElementTreeUtil.get_tag_data(param, 'Text').split(";")

        if (text_ids := XmlElementTreeUtil.get_tag_data(param, 'TextId').split(";")):
            texts += [""] * (len(text_ids) - len(texts))

            for index, text_id in enumerate(text_ids):
                if text_id:
                    texts[index] = self.local_str_table.get_entry(text_id)[0]

        return texts


    def get_include_language_file(self,
                                  param   : ElementTree.Element,
                                  pyp_path: str):
        """ get the language file for the include

        Args:
            param:    this parameter node
            pyp_path: path of the pyp file
        """

        if (language_file := XmlElementTreeUtil.get_tag_data(param, 'LanguageFile')):
            if not (global_lang_path := FileNameService.get_global_standard_path(language_file)):
                global_lang_path = f"{pyp_path}\\{language_file}"

            self.local_str_table = BuildingElementStringTable(f"{global_lang_path}.pyp",  True,
                                                              AllplanSettings.AllplanLocalisationService.AllplanLanguage())

```

</details>