---
title: "XmlParentParameterData"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlParentParameterData.py"
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


# XmlParentParameterData

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlParentParameterData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `xml`

## Übersicht

implementation of the data for a xml parent parameter

## Abhängigkeiten

- `dataclasses`
- `typing`

## Klassen

### `XmlParentParameterData`

implementation of the data for a xml parent parameter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `reset_expander` | `self` | `None` | reset the expander data          |
| `reset_row` | `self` | `None` | reset the row data          |
| `reset_radio_group` | `self` | `None` | reset the radio group data          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the data for a xml parent parameter
"""

from typing import Any

from dataclasses import dataclass, field

EXPANDER_LEVEL_SEPARATOR = "|"

@dataclass
class XmlParentParameterData():
    """ implementation of the data for a xml parent parameter
    """

    expander_name         : str               = ""
    row_name              : str               = ""
    row_state_key         : str               = ""
    expander_state_key    : str               = ""
    radio_group_name      : str               = ""
    radio_group_text      : str               = ""
    radio_group_selection : (list[Any] | Any) = field(default_factory = list)


    def reset_expander(self):
        """ reset the expander data
        """
        # reset the expander name and state key to the parent expander
        # by removing the last level of the composed name

        if EXPANDER_LEVEL_SEPARATOR in self.expander_name:
            self.expander_name = self.expander_name.rsplit(EXPANDER_LEVEL_SEPARATOR, 1)[0]
        else:
            self.expander_name = ""

        if EXPANDER_LEVEL_SEPARATOR in self.expander_state_key:
            self.expander_state_key = self.expander_state_key.rsplit(EXPANDER_LEVEL_SEPARATOR, 1)[0]
        else:
            self.expander_state_key = ""


    def reset_row(self):
        """ reset the row data
        """

        self.row_name      = ""
        self.row_state_key = ""


    def reset_radio_group(self):
        """ reset the radio group data
        """

        self.radio_group_text      = ""
        self.radio_group_name      = ""
        self.radio_group_selection = []

```

</details>