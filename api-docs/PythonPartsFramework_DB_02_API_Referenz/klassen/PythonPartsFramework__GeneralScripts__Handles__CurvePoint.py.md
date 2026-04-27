---
title: "CurvePoint"
source: "PythonPartsFramework\GeneralScripts\Handles\CurvePoint.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# CurvePoint

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\CurvePoint.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the curve point modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `NemAll_Python_Geometry`
- `NemAll_Python_Utility`
- `TypeCollections.GeometryTyping`
- `typing`

## Klassen

### `CurvePoint`

modify the curve point
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self` | `None` | execute the value update          |
| `__modify_line` | `self, line: AllplanGeo.Line2D | AllplanGeo.Line3D, list_index: int` | `None` | modify the line  Args:     line:       line to modify     list_index: index of the point to modify |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the curve point modification
"""

from typing import cast

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Utility as AllplanUtil

from TypeCollections.GeometryTyping import CURVES_3D

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class CurvePoint(BaseHandlePropUpdate):
    """ modify the curve point
    """

    def __call__(self):
        """ execute the value update
        """

        param_data = self._handle_prop.parameter_data[0]

        if (geo_element := param_data.geo_element) is None or param_data.list_index is None:
            return

        list_index = cast(int, param_data.list_index)


        #----------------- lines

        if isinstance(geo_element, (AllplanGeo.Line2D, AllplanGeo.Line3D)):
            self.__modify_line(geo_element, list_index)

            return


        #----------------- delete the point

        if AllplanUtil.KeyboardState.IsShiftKeyPressed() and param_data.delete_list_item:
            if (geo_element := param_data.geo_element) is None:
                return

            if geo_element.StartPoint != geo_element.EndPoint:      # type: ignore
                geo_element.Remove(list_index)                      # type: ignore
                return

            if list_index in (0, geo_element.Count() - 1):          # type: ignore
                geo_element.Remove(0)                               # type: ignore
                geo_element.RemoveLastPoint()                       # type: ignore
                geo_element += geo_element.StartPoint               # type: ignore
                return

            geo_element.Remove(list_index)                          # type: ignore

            return

        input_pnt = self._local_input_pnt if isinstance(geo_element, CURVES_3D) else self._local_input_pnt.To2D

        index = cast(int, param_data.list_index)

        geo_element.SetPoint(input_pnt, index)     # type: ignore

        if not isinstance(geo_element, (AllplanGeo.Polygon2D, AllplanGeo.Polygon3D)):
            return

        if index == 0:
            geo_element.EndPoint = geo_element.StartPoint   # type: ignore

        elif index == geo_element.Count() - 1:
            geo_element.StartPoint = geo_element.EndPoint   # type: ignore


    def __modify_line(self,
                      line      : (AllplanGeo.Line2D | AllplanGeo.Line3D),
                      list_index: int):
        """ modify the line

        Args:
            line:       line to modify
            list_index: index of the point to modify
        """

        if list_index == 0:
            line.StartPoint = self._local_input_pnt if isinstance(line, AllplanGeo.Line3D) else \
                              self._local_input_pnt.To2D                                                # type: ignore
        else:
            line.EndPoint = self._local_input_pnt if isinstance(line, AllplanGeo.Line3D) else \
                            self._local_input_pnt.To2D                                                  # type: ignore

```

</details>