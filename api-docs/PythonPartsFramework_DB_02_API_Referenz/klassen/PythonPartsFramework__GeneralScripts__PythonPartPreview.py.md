---
title: "PythonPartPreview"
source: "PythonPartsFramework\GeneralScripts\PythonPartPreview.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PythonPartPreview

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPartPreview.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the PythonPart preview

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `TypeCollections.ModelEleList`
- `Utilities.SystemAngleUtil`

## Klassen

### `PythonPartPreview`

Implementation of the PythonPart transaction 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `execute` | `doc: AllplanEleAdapter.DocumentAdapter, placement_matrix: AllplanGeo.Matrix3D, model_ele_list: ModelEleList, direct_draw: bool=False, asso_ref_object: AllplanEleAdapter.BaseElementAdapter | None=None, use_system_angle: bool=True, as_static_preview: bool=False, elements_to_hide: AllplanEleAdapter.BaseElementAdapterList | None=None, elements_to_show: AllplanEleAdapter.BaseElementAdapterList | None=None, hidden_preview_elements: AllplanEleAdapter.BaseElementAdapterList | None=None, visible_preview_elements: AllplanEleAdapter.BaseElementAdapterList | None=None` | `None` | execute the preview draw  Args:     doc:                      document of the Allplan drawing files     placement_matrix:         placement matrix     model_ele_list:           list with the model elements     direct_draw:              direct draw of the preview     asso_ref_object:          associative view reference object     use_system_angle:         use the system angle state     as_static_preview:        draw as static preview state     elements_to_hide:         elements to hide persting in the drawing file     elements_to_show:         elements to show persting in the drawing file     hidden_preview_elements:  elements to hide in the preview     visible_preview_elements: elements to show in the preview |
| `close` | `-` | `None` | close the preview          |
| `set_preview_draw_lock` | `preview_draw_lock: bool` | `None` | set the preview draw lock state  Args:     preview_draw_lock: preview draw lock state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the PythonPart preview
"""


import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from Utilities.SystemAngleUtil import SystemAngleUtil

from TypeCollections.ModelEleList import ModelEleList


class PythonPartPreview():
    """ Implementation of the PythonPart transaction """

    __preview_draw_lock = False

    @staticmethod
    def execute(doc                     : AllplanEleAdapter.DocumentAdapter,
                placement_matrix        : AllplanGeo.Matrix3D,
                model_ele_list          : ModelEleList,
                direct_draw             : bool                                              = False,
                asso_ref_object         : (AllplanEleAdapter.BaseElementAdapter | None)     = None,
                use_system_angle        : bool                                              = True,
                as_static_preview       : bool                                              = False,
                elements_to_hide        : (AllplanEleAdapter.BaseElementAdapterList | None) = None,
                elements_to_show        : (AllplanEleAdapter.BaseElementAdapterList | None) = None,
                hidden_preview_elements : (AllplanEleAdapter.BaseElementAdapterList | None) = None,
                visible_preview_elements: (AllplanEleAdapter.BaseElementAdapterList | None) = None):
        """ execute the preview draw

        Args:
            doc:                      document of the Allplan drawing files
            placement_matrix:         placement matrix
            model_ele_list:           list with the model elements
            direct_draw:              direct draw of the preview
            asso_ref_object:          associative view reference object
            use_system_angle:         use the system angle state
            as_static_preview:        draw as static preview state
            elements_to_hide:         elements to hide persting in the drawing file
            elements_to_show:         elements to show persting in the drawing file
            hidden_preview_elements:  elements to hide in the preview
            visible_preview_elements: elements to show in the preview
        """

        if PythonPartPreview.__preview_draw_lock:
            return

        visible_service = AllplanIFW.VisibleService

        to_hide = [] if elements_to_hide is None else [ele for ele in elements_to_hide \
                                                       if visible_service.IsElementCurrentlyHidden(ele) is False]

        to_hide += [] if hidden_preview_elements is None else [ele for ele in hidden_preview_elements \
                                                               if visible_service.IsElementCurrentlyHidden(ele) is False]

        visible_service.ShowElements(AllplanEleAdapter.BaseElementAdapterList(to_hide), False, True)

        to_show = [] if elements_to_show is None else [ele for ele in elements_to_show \
                                                       if visible_service.IsElementCurrentlyHidden(ele)]

        to_show += [] if visible_preview_elements is None else [ele for ele in visible_preview_elements \
                                                                if visible_service.IsElementCurrentlyHidden(ele)]

        visible_service.ShowElements(AllplanEleAdapter.BaseElementAdapterList(to_show), True, True)


        #----------------- final transformation in case of rotated crosshair

        if not model_ele_list:
            return

        if use_system_angle:
            placement_matrix = SystemAngleUtil.execute_rotation(placement_matrix)


        #----------------- draw the preview

        AllplanBaseEle.DrawElementPreview(doc, placement_matrix, model_ele_list, direct_draw, asso_ref_object, as_static_preview)


    @staticmethod
    def close():
        """ close the preview
        """

        if PythonPartPreview.__preview_draw_lock:
            return

        AllplanBaseEle.CloseElementPreview()
        AllplanBaseEle.ClearElementPreview()


    @staticmethod
    def set_preview_draw_lock(preview_draw_lock: bool):
        """ set the preview draw lock state

        Args:
            preview_draw_lock: preview draw lock state
        """

        PythonPartPreview.__preview_draw_lock = preview_draw_lock

```

</details>