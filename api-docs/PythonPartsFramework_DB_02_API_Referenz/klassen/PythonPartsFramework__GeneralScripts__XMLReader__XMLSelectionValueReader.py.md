---
title: "XMLSelectionValueReader"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XMLSelectionValueReader.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XMLSelectionValueReader

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XMLSelectionValueReader.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`, `xml`

## Übersicht

implementation of the selection value reader

## Abhängigkeiten

- `NemAll_Python_Palette`
- `ParameterProperty`
- `XmlElementTreeUtil`
- `xml.etree`

## Klassen

### `XMLSelectionValueReader`

implementation of the selection value reader
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_selected_value` | `param: ElementTree.Element, param_prop: ParameterProperty` | `None` | set the selected value  Args:     param:      parameter node     param_prop: parameter property |
| `__set_sel_value_tuple` | `param: ElementTree.Element` | `AllplanPalette.Orientation` | set the selection value for the tuple  Args:     param: parameter node  Returns:     Picture orientation |
| `__set_sel_value_picture` | `param: ElementTree.Element` | `AllplanPalette.Orientation` | set the picture orientation as selected value  Args:     param: parameter node  Returns:     picture orientation |
| `__set_sel_value_text` | `param: ElementTree.Element` | `AllplanPalette.Orientation` | set the picture orientation as selected value  Args:     param: parameter node  Returns:     picture orientation |
| `__set_sel_value_materialbutton` | `param: ElementTree.Element` | `int` | disable button state  Args:     param: parameter node  Returns:     disable button state |
| `__get_orientation` | `param: ElementTree.Element, value_type: str` | `AllplanPalette.Orientation` | set the picture orientation as selected value  Args:     param:      parameter node     value_type: value type of the orientation  Returns:     picture orientation |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the selection value reader
"""

# pylint: disable=unused-private-member

from xml.etree import ElementTree

import NemAll_Python_Palette as AllplanPalette

from ParameterProperty import ParameterProperty

from .XmlElementTreeUtil import XmlElementTreeUtil


class XMLSelectionValueReader():
    """ implementation of the selection value reader
    """

    @staticmethod
    def set_selected_value(param     : ElementTree.Element,
                           param_prop: ParameterProperty):
        """ set the selected value

        Args:
            param:      parameter node
            param_prop: parameter property
        """


        function_set_selection =  "_XMLSelectionValueReader__set_sel_value_tuple" if param_prop.value_type.is_tuple_type() else \
                                 f"_XMLSelectionValueReader__set_sel_value_{param_prop.value_type}"

        if (function_sel := getattr(XMLSelectionValueReader, function_set_selection, None)) is not None:
            param_prop.selected_value = function_sel(param)                                                 # pylint: disable=not-callable


    @staticmethod
    def __set_sel_value_tuple(param: ElementTree.Element) -> AllplanPalette.Orientation:    # NOSONAR
        """ set the selection value for the tuple

        Args:
            param: parameter node

        Returns:
            Picture orientation
        """

        return XMLSelectionValueReader.__get_orientation(param, "Tuple")


    @staticmethod
    def __set_sel_value_picture(param: ElementTree.Element) -> AllplanPalette.Orientation:    # NOSONAR
        """ set the picture orientation as selected value

        Args:
            param: parameter node

        Returns:
            picture orientation
        """

        return XMLSelectionValueReader.__get_orientation(param, "Picture")


    @staticmethod
    def __set_sel_value_text(param: ElementTree.Element) -> AllplanPalette.Orientation:    # NOSONAR
        """ set the picture orientation as selected value

        Args:
            param: parameter node

        Returns:
            picture orientation
        """

        return XMLSelectionValueReader.__get_orientation(param, "Text")


    @staticmethod
    def __set_sel_value_materialbutton(param: ElementTree.Element) -> int:    # NOSONAR
        """ disable button state

        Args:
            param: parameter node

        Returns:
            disable button state
        """

        return 1 if XmlElementTreeUtil.get_bool_value(param, 'DisableButtonIsShown') else 0
                                                # pylint: disable=not-callable


    @staticmethod
    def __get_orientation(param     : ElementTree.Element,
                          value_type: str) -> AllplanPalette.Orientation:
        """ set the picture orientation as selected value

        Args:
            param:      parameter node
            value_type: value type of the orientation

        Returns:
            picture orientation
        """

        if not (orientation := XmlElementTreeUtil.get_tag_data(param, 'Orientation', value_type)):
            return AllplanPalette.Orientation.eLeft

        match orientation.upper():
            case "LEFT":
                return AllplanPalette.Orientation.eLeft

            case "MIDDLE":
                return AllplanPalette.Orientation.eCenter

            case _:
                return AllplanPalette.Orientation.eRight

```

</details>