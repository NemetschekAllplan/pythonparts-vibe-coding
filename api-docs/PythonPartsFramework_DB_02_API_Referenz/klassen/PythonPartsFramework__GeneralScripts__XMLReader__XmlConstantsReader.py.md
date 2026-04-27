---
title: "XmlConstantsReader"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlConstantsReader.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlConstantsReader

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlConstantsReader.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `xml`

## Übersicht

implementation of the constants reader

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementStringTable`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `XmlElementTreeUtil`
- `XmlStringToValueConverter`
- `xml.etree`

## Klassen

### `XmlConstantsReader`

implementation of the constants reader
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `exeute` | `doc_ele: ElementTree.ElementTree, build_ele: BuildingElement, local_str_table: BuildingElementStringTable` | `None` | Read the constants  Args:     doc_ele:         document element     build_ele:       building element with the parameter properties     local_str_table: local string table |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the constants reader
"""

from xml.etree import ElementTree

from BuildingElement import BuildingElement
from BuildingElementStringTable import BuildingElementStringTable
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

from .XmlElementTreeUtil import XmlElementTreeUtil
from .XmlStringToValueConverter import XmlStringToValueConverter

class XmlConstantsReader():
    """ implementation of the constants reader
    """

    @staticmethod
    def exeute(doc_ele        : ElementTree.ElementTree,
               build_ele      : BuildingElement,
               local_str_table: BuildingElementStringTable):
        """ Read the constants

        Args:
            doc_ele:         document element
            build_ele:       building element with the parameter properties
            local_str_table: local string table
        """

        if not (constants := XmlElementTreeUtil.get_elements_by_tag_name(doc_ele, "Constants")):
            return

        if (constants := next(constants, None)) is None:
            return

        for constant in XmlElementTreeUtil.get_children_by_title(constants, 'Constant'):
            name           = XmlElementTreeUtil.get_str_value(constant, "Name", "")
            value_str      = XmlElementTreeUtil.get_str_value(constant, "Value", "")
            value_type_str = XmlElementTreeUtil.get_str_value(constant, "ValueType", "").lower()

            value = XmlStringToValueConverter.get_value(build_ele,
                                                        ParameterPropertyValueTypesImpl.get_value_type_impl(value_type_str),
                                                        value_str, None, 0, local_str_table, None)

            build_ele.add_constant(name, value)

```

</details>