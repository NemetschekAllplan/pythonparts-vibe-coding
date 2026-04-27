---
title: "Point"
source: "PythonPartsFramework\GeneralScripts\Handles\Point.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# Point

> **Pfad:** `PythonPartsFramework\GeneralScripts\Handles\Point.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

implementation of the point distance modification

## Abhängigkeiten

- `BaseHandlePropUpdate`
- `BuildingElementParameterPropertyUtil`
- `NemAll_Python_Geometry`
- `NemAll_Python_Utility`
- `ValueTypes.ParameterPropertyValueTypes`
- `typing`

## Klassen

### `Point`

modify the point
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__call__` | `self` | `None` | execute the value update          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the point distance modification
"""

from typing import cast

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Utility as AllplanUtil

import BuildingElementParameterPropertyUtil as PropertyUtil

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from .BaseHandlePropUpdate import BaseHandlePropUpdate

class Point(BaseHandlePropUpdate):
    """ modify the point
    """

    def __call__(self):
        """ execute the value update
        """

        prop, item_name, name = self.get_property_data()

        if prop is None:
            return

        _, _, _, interval_value = self._handle_prop.get_min_max_values(name)


        #----------------- delete the point

        param_data = self._handle_prop.parameter_data[0]

        if AllplanUtil.KeyboardState.IsShiftKeyPressed() and param_data.list_index is not None and param_data.delete_list_item:
            del prop.value[cast(int, param_data.list_index)]

            return


        #----------------- adapt the point coordinate to an interval

        if interval_value:
            dist_vec = AllplanGeo.Vector3D(self._dist_pnt)

            if (dist := dist_vec.GetLength()):
                interval_value = eval(interval_value, self._build_ele.get_parameter_dict())     # pylint: disable=eval-used

                count = round(dist / interval_value)

                if (dist := count * interval_value):
                    dist_vec.Normalize(dist)

                    self._local_input_pnt = self._handle_prop.ref_point + dist_vec        # pylint: disable=attribute-defined-outside-init

        input_pnt = self._local_input_pnt.To2D if prop.value_type == ParameterPropertyValueTypes.POINT2D else self._local_input_pnt

        self._update_palette = PropertyUtil.set_property_value(prop, item_name, input_pnt)    # pylint: disable=attribute-defined-outside-init

```

</details>