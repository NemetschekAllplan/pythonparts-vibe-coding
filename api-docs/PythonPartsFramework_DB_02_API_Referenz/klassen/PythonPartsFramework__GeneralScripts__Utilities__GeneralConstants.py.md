---
title: "GeneralConstants"
source: "PythonPartsFramework\GeneralScripts\Utilities\GeneralConstants.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GeneralConstants

> **Pfad:** `PythonPartsFramework\GeneralScripts\Utilities\GeneralConstants.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the general constants

## Abhängigkeiten

- Keine

## Klassen

### `GeneralConstants`

implementation of the general constants
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the general constants
"""

# pylint: disable=too-few-public-methods

class GeneralConstants():
    """ implementation of the general constants
    """

    TEXT_SEPARATOR = "|"
    EMPTY_TEXT_ID  = "0"
    EMPTY_LIST     = "[]"
    EMPTY_TUPLE    = "(_)"
    EMPTY_SET      = "{}"

    BRACKET_OPEN  = "("
    BRACKET_CLOSE = ")"

    SUB_NAME_SEPARATOR = "."
    SUB_TEXT_SEPARATOR = ","
    TEXT_KEY           = "\""
    FLOAT_KEY          = "."
    COMBOBOX_KEY       = "combobox"

    LIST_SEPARATOR_START = "["
    LIST_SEPARATOR_END   = "]"
    LIST_SEPARATOR_2_DIM = "]["
    LIST_ITEM_SEPARATOR  = ";"

    TUPLE_SEPARATOR_START = "("
    TUPLE_SEPARATOR_END   = ")"
    TUPLE_LIST_SEPARATOR  = "]("

    FALSE      = "False"
    LOWER_TRUE = "true"

    LIST_ROW_KEYWORD = "$list_row"
    LIST_COL_KEYWORD = "$list_col"

    DIALOG_BUTTON_KEY                 = "___DialogButton___"
    DIALOG_BUTTON_COMBO_DEL_ENTRY     = "___DialogButton___Combo_Del"
    DATE_DIALOG_BUTTON_KEY            = "___DialogButton___DateDialog"
    BITMAP_RESOURCE_DIALOG_BUTTON_KEY = "___DialogButton___BitmapResourceDialog"

    PALETTE_BUTTON_KEY                 = "___PaletteButton___"
    PALETTE_BUTTON_DELETE_KEY          = "___PaletteButton___delete"
    PALETTE_BUTTON_SHOW_POINT_KEY      = "___PaletteButton___ShowPoints"
    PALETTE_BUTTON_SHOW_KNOTS_KEY      = "___PaletteButton___ShowKnots"
    PALETTE_BUTTON_SHOW_WEIGHTS_KEY    = "___PaletteButton___ShowWeights"
    PALETTE_BUTTON_PARAM_TAKE_OVER_KEY = "___PaletteButton___ParameterTakeOver"
    PALETTE_BUTTON_POINT_TAKE_OVER_KEY = "___PaletteButton___PointTakeOver"

    XYZ_IN_ROW_KEY     = "__Row__"
    EMPTY_ROW_NAME_KEY = "_"

    ROW_STATE_KEY_SEPARATOR = ":"

    MULTI_INDEX_SINGLE_SEPARATOR = ","
    MULTI_INDEX_RANGE_SEPARATOR  = "-"

    USE_CURRENT_RESOURCE_VALUE = "-1"

    HIDDEN_PAGE_KEY       = "__HiddenPage__"
    IN_MANDATORY_PAGE_KEY = "__IN_MANDATORY__"
    IN_PAGE_KEY           = "__IN__"
    OUT_PAGE_KEY          = "__OUT__"
    IN_OUT_PAGE_KEY       = "__IN_OUT__"
    IN_OPTIONAL_PAGE_KEY  = "__IN_OPTIONAL__"

    ELEMENT_INDEX_KEY    = "__ElementIndex__"
    PLACEMENT_MATRIX_KEY = "__PlacementMatrix__"
    PYPSUB_KEY           = ".pypsub"

    VISUAL_SCRIPTS_FOLDER_KEY = "\\visualscripts\\"

```

</details>