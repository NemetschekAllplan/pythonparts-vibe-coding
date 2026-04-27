---
title: "PointListHandlesCreator"
source: "PythonPartsFramework\Utils\HandleCreator\PointListHandlesCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PointListHandlesCreator

> **Pfad:** `PythonPartsFramework\Utils\HandleCreator\PointListHandlesCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `utility`

## Übersicht

implementation of the handle creator

## Abhängigkeiten

- `HandleCreator`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `TypeCollections.HandleList`
- `math`
- `string`

## Klassen

### `PointListHandlesCreator`

implementation of the handle creator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `point_list` | `handle_list: HandleList, name: str, handle_points: list[AllplanGeo.Point2D] | list[AllplanGeo.Point3D], info_text: str='', info_text_template: Template=Template(''), index_offset: int=0, delete_point: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), plane: AllplanGeo.Plane3D | None=None` | `None` | create point move handles  Args:     handle_list:        handle list     name:               handle parameter name     handle_points:      handle points     info_text:          info text     info_text_template: info text template     index_offset:       index offset for the info text     delete_point:       enable delete point state     owner_element:      owner element of the handle (in element modification mode)     plane:              input plane for the handle_point movement |
| `point_list_segment_center` | `handle_list: HandleList, name: str, handle_points: list[AllplanGeo.Point2D] | list[AllplanGeo.Point3D], info_text: str='', info_text_template: Template=Template(''), index_offset: int=0, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), plane: AllplanGeo.Plane3D | None=None` | `None` | create point handles from a segment center to insert and move  Args:     handle_list:        handle list     name:               handle parameter name     handle_points:      handle points     info_text:          info text     info_text_template: info text template     index_offset:       index offset for the info text     owner_element:      owner element of the handle (in element modification mode)     plane:              input plane for the handle_point movement |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the handle creator
"""

# pylint: disable=too-many-arguments

from string import Template

import math

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from TypeCollections.HandleList import HandleList

from .HandleCreator import HandleCreator

class PointListHandlesCreator():
    """ implementation of the handle creator
    """

    @staticmethod
    def point_list(handle_list       : HandleList,
                   name              : str,
                   handle_points     : (list[AllplanGeo.Point2D] | list[AllplanGeo.Point3D]),
                   info_text         : str                                  = "",
                   info_text_template: Template                             = Template(""),
                   index_offset      : int                                  = 0,
                   delete_point      : bool                                 = False,
                   owner_element     : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                   plane             : (AllplanGeo.Plane3D | None)          = None):
        """ create point move handles

        Args:
            handle_list:        handle list
            name:               handle parameter name
            handle_points:      handle points
            info_text:          info text
            info_text_template: info text template
            index_offset:       index offset for the info text
            delete_point:       enable delete point state
            owner_element:      owner element of the handle (in element modification mode)
            plane:              input plane for the handle_point movement
        """

        for index, pnt in enumerate(handle_points):
            if info_text_template:
                info_text = info_text_template.substitute(index = index + index_offset)

            HandleCreator.point(handle_list, name, AllplanGeo.Point3D(pnt), index, info_text, delete_point, owner_element,
                                plane = plane)


    @staticmethod
    def point_list_segment_center(handle_list       : HandleList,
                                  name              : str,
                                  handle_points     : (list[AllplanGeo.Point2D] | list[AllplanGeo.Point3D]),
                                  info_text         : str                                  = "",
                                  info_text_template: Template                             = Template(""),
                                  index_offset      : int                                  = 0,
                                  owner_element     : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                                  plane             : (AllplanGeo.Plane3D | None)          = None):
        """ create point handles from a segment center to insert and move

        Args:
            handle_list:        handle list
            name:               handle parameter name
            handle_points:      handle points
            info_text:          info text
            info_text_template: info text template
            index_offset:       index offset for the info text
            owner_element:      owner element of the handle (in element modification mode)
            plane:              input plane for the handle_point movement
        """

        for index in range(len(handle_points) - 1):
            if info_text_template:
                info_text = info_text_template.substitute(index = index + index_offset)

            start_pnt = AllplanGeo.Point3D(handle_points[index])
            end_pnt   = AllplanGeo.Point3D(handle_points[index + 1])

            pnt = (start_pnt + end_pnt) / 2

            HandleCreator.split_point(handle_list, name, pnt,
                                      AllplanGeo.Vector2D(start_pnt.To2D, end_pnt.To2D).GetAngle() + AllplanGeo.Angle(math.pi / 4),
                                      index, info_text, owner_element, plane = plane)

```

</details>