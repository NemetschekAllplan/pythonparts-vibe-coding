---
title: "LengthPointDistance"
source: "PythonPartsFramework\GeneralScripts\Handles\LengthPointDistance.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# LengthPointDistance

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\LengthPointDistance.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the length modification

## Abhängigkeiten

- `BaseHandlePointUpdate`
- `NemAll_Python_Geometry`
- `TypeCollections.GeometryTyping`
- `ValueTypes.ValueTypeUtils.ParameterPropertyListUtil`
- `typing`

## Klassen

### `LengthPointDistance`

modify the length
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self` | `None` | execute the coordinate update          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the length modification
"""

from typing import cast

import NemAll_Python_Geometry as AllplanGeo

from ValueTypes.ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil

from TypeCollections.GeometryTyping import POLY_CURVES_2D, POLY_CURVES_3D

from .BaseHandlePointUpdate import BaseHandlePointUpdate

class LengthPointDistance(BaseHandlePointUpdate):
    """ modify the length
    """

    def __call__(self):
        """ execute the coordinate update
        """

        geo_ele = self._param_data.geo_element

        if isinstance(geo_ele, AllplanGeo.Line2D):
            geo_ele.Extend(self.value - AllplanGeo.CalcLength(geo_ele))

        elif isinstance(geo_ele, AllplanGeo.Line3D):
            geo_ele.TrimEnd(AllplanGeo.CalcLength(geo_ele) - self.value)

        elif isinstance(geo_ele, AllplanGeo.Arc2D):
            arc = cast(AllplanGeo.Arc2D, geo_ele)

            end_angle = arc.StartAngle + self.value / arc.MajorRadius

            arc.EndAngle = end_angle

        elif isinstance(geo_ele, POLY_CURVES_2D | POLY_CURVES_3D):
            if (index := ParameterPropertyListUtil.get_list_index(self._param_data.param_prop_name)) is None:
                return False

            start_pnt = geo_ele[index]
            end_pnt   = geo_ele[index + 1]

            if isinstance(geo_ele, POLY_CURVES_2D):
                line = AllplanGeo.Line2D(start_pnt, end_pnt)

                line.Extend(self.value - AllplanGeo.CalcLength(line))

                geo_ele[index + 1] = line.EndPoint

            else:
                line = AllplanGeo.Line3D(start_pnt, end_pnt)

                line.TrimEnd(AllplanGeo.CalcLength(line) - self.value)

                geo_ele[index + 1] = line.EndPoint

        return True

```

</details>