---
title: "XmlReinforcementReader"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlReinforcementReader.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlReinforcementReader

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlReinforcementReader.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `xml`

## Übersicht

implementation of the reinforcement reader

## Abhängigkeiten

- `BuildingElement`
- `ReinforcementDefinition`
- `XmlElementTreeUtil`
- `xml.etree`

## Klassen

### `XmlReinforcementReader`

implementation of the reinforcement reader
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `execute` | `doc_ele: ElementTree.ElementTree, build_ele: BuildingElement` | `None` | Read the reinforcement data  Args:     doc_ele:   document element     build_ele: building element with the parameter properties |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the reinforcement reader
"""

from xml.etree import ElementTree

from BuildingElement import BuildingElement
from ReinforcementDefinition import ReinforcementDefinition

from .XmlElementTreeUtil import XmlElementTreeUtil

class XmlReinforcementReader():
    """ implementation of the reinforcement reader
    """

    @staticmethod
    def execute(doc_ele  : ElementTree.ElementTree,
                build_ele: BuildingElement):
        """ Read the reinforcement data

        Args:
            doc_ele:   document element
            build_ele: building element with the parameter properties
        """

        reinforcement_list = []

        for reinf in XmlElementTreeUtil.get_elements_by_tag_name(doc_ele, "Reinforcement"):
            reinf_def = ReinforcementDefinition()

            reinf_def.read_data(reinf)

            reinforcement_list.append(reinf_def)

        build_ele.set_reinforcement_definition_list(reinforcement_list)

```

</details>