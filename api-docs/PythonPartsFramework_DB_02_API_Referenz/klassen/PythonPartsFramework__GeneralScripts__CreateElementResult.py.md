---
title: "CreateElementResult"
source: "PythonPartsFramework\GeneralScripts\CreateElementResult.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# CreateElementResult

> **Pfad:** `PythonPartsFramework\GeneralScripts\CreateElementResult.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the data class for the result of the create_element function

## Abhängigkeiten

- `HandleProperties`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `PreviewSymbols`
- `PythonPartTransaction`
- `TypeCollections.ModelEleList`
- `dataclasses`
- `typing`

## Klassen

### `CreateElementResult`

Implementation of the data class for the result of the create_element function

Attributes:
    elements:                 list of elements to create
    handles:                  list of handles to create
    preview_elements:         list of element to draw only in the preview
    placement_point:          if set, the point is used as global placement point for the elements
    multi_placement:          if True, the elements can be placed multiple times
    preview_symbols:          preview symbols to show in the preview
    reinf_rearrange:          properties for rearranging the reinforcement mark numbering
    handle_placement_geo:     elements, which should be used during the handle modification
    as_static_preview:        if True, the preview is drawn as static preview
    connect_to_ele:           data for the PythonPart connection to element(s)
    uuid_parameter_name:      if set, the model object UUID of the created PythonPart is assigned to this name
    elements_to_delete:       elements which should be delete
    append_reinf_pos_nr:      when set to True, the reinforcement position numbers are appended to the existing position numbers
    elements_to_hide:         elements to hide persting in the drawing file
    elements_to_show:         elements to show persting in the drawing file
    hidden_preview_elements:  elements to hide in the preview
    visible_preview_elements: elements to show in the preview

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `is_empty` | `self` | `bool` | check for empty data  Returns:     True if no elements and handles exist, otherwise False |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the data class for the result of the create_element function
"""

from typing import Any

from dataclasses import dataclass, field

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from HandleProperties import HandleProperties
from PreviewSymbols import PreviewSymbols
from PythonPartTransaction import ConnectToElements, ReinforcementRearrange

from TypeCollections.ModelEleList import ModelEleList


@dataclass
class CreateElementResult():
    """ Implementation of the data class for the result of the create_element function

    Attributes:
        elements:                 list of elements to create
        handles:                  list of handles to create
        preview_elements:         list of element to draw only in the preview
        placement_point:          if set, the point is used as global placement point for the elements
        multi_placement:          if True, the elements can be placed multiple times
        preview_symbols:          preview symbols to show in the preview
        reinf_rearrange:          properties for rearranging the reinforcement mark numbering
        handle_placement_geo:     elements, which should be used during the handle modification
        as_static_preview:        if True, the preview is drawn as static preview
        connect_to_ele:           data for the PythonPart connection to element(s)
        uuid_parameter_name:      if set, the model object UUID of the created PythonPart is assigned to this name
        elements_to_delete:       elements which should be delete
        append_reinf_pos_nr:      when set to True, the reinforcement position numbers are appended to the existing position numbers
        elements_to_hide:         elements to hide persting in the drawing file
        elements_to_show:         elements to show persting in the drawing file
        hidden_preview_elements:  elements to hide in the preview
        visible_preview_elements: elements to show in the preview
    """

    elements                 : ModelEleList                                       = field(default_factory = ModelEleList)
    handles                  : list[HandleProperties]                             = field(default_factory = list)
    preview_elements         : ModelEleList                                       = field(default_factory = ModelEleList)
    placement_point          : ((AllplanGeo.Point2D | AllplanGeo.Point3D) | None) = None
    multi_placement          : bool                                               = False
    preview_symbols          : (PreviewSymbols | None)                            = None
    reinf_rearrange          : ReinforcementRearrange                             = field(default_factory = ReinforcementRearrange)
    handle_placement_geo     : list[Any]                                          = field(default_factory = list)
    as_static_preview        : bool                                               = False
    connect_to_ele           : ConnectToElements                                  = field(default_factory = ConnectToElements)
    uuid_parameter_name      : str                                                = ""
    elements_to_delete       : (AllplanEleAdapter.BaseElementAdapterList | None)  = None
    append_reinf_pos_nr      : bool                                               = True
    elements_to_hide         : (AllplanEleAdapter.BaseElementAdapterList | None)  = None
    elements_to_show         : (AllplanEleAdapter.BaseElementAdapterList | None)  = None
    hidden_preview_elements  : (AllplanEleAdapter.BaseElementAdapterList | None)  = None
    visible_preview_elements : (AllplanEleAdapter.BaseElementAdapterList | None)  = None


    def is_empty(self) -> bool:
        """ check for empty data

        Returns:
            True if no elements and handles exist, otherwise False
        """

        return not self.elements and not self.preview_elements and not self.handles

```

</details>