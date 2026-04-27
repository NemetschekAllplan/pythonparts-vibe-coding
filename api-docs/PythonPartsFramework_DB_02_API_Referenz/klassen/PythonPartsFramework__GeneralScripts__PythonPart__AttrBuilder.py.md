---
title: "AttrBuilder"
source: "PythonPartsFramework\GeneralScripts\PythonPart\AttrBuilder.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# AttrBuilder

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPart\AttrBuilder.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the AttrBuilder

## Abhängigkeiten

- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_Utility`
- `__future__`
- `uuid`

## Klassen

### `AttrBuilder`

Define specific PythonPart attributes
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `pyp_file_param_list_attr` | `python_file: str, parameter_list: list[str]` | `tuple[AllplanBaseEle.AttributeStringVec, list[str]]` | Define attribute holding python file name and all parameter - values pairs of pyp file  Args:     python_file   : Filename of PYP file     parameter_list: list of parameters of PYP file  Returns:     Attribute holding values as string vector, geometry parameter values |
| `python_part_attr` | `-` | `AllplanBaseEle.AttributeString` | Define attribute holding "PythonPart" identification string  Returns:     Attribute holding PythonPart identifier |
| `placement_matrix_attr` | `matrix: AllplanGeo.Matrix3D` | `AllplanBaseEle.AttributeDoubleVec` | Define attribute holding PythonPart matrix for update  Args:     matrix: placement matrix  Returns:     Attribute holding PythonPart matrix for update |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the AttrBuilder
"""
from __future__ import annotations

import uuid

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Utility as AllplanUtil

class AttrBuilder():
    """ Define specific PythonPart attributes
    """

    @staticmethod
    def pyp_file_param_list_attr(python_file   : str,
                                 parameter_list: list[str]) -> tuple[AllplanBaseEle.AttributeStringVec, list[str]]:
        """ Define attribute holding python file name and all parameter - values pairs of pyp file

        Args:
            python_file   : Filename of PYP file
            parameter_list: list of parameters of PYP file

        Returns:
            Attribute holding values as string vector, geometry parameter values
        """

        values = AllplanUtil.VecStringList()

        geom_param_values : list[str] = []

        values.append(python_file)

        for item in parameter_list:
            
            # if string length is bigger than 500 the string is stored in proxy object because when the
            # parameter list gets to long it can't be stored in an Allplan attribute
            
            if len(item) > 500:                                                         # pylint: disable=R2004:magic-value-comparison
                name, _, geo_param_value = item.partition("=")

                geo_uuid = str(uuid.uuid4())

                values.append(f"{name}=GeometryProxyElement:{geo_uuid}{chr(10)}")

                geom_param_values.append(f"{geo_uuid}={geo_param_value}")

            else:
                values.append(item)

        return AllplanBaseEle.AttributeStringVec(AllplanBaseEle.ATTRNR_PYTHONPART_PATH, values), geom_param_values


    @staticmethod
    def python_part_attr() -> AllplanBaseEle.AttributeString:
        """ Define attribute holding "PythonPart" identification string

        Returns:
            Attribute holding PythonPart identifier
        """

        return AllplanBaseEle.AttributeString(AllplanBaseEle.ATTRNR_PYTHONPART_CHECK, 'PythonPart')


    @staticmethod
    def placement_matrix_attr(matrix: AllplanGeo.Matrix3D) -> AllplanBaseEle.AttributeDoubleVec:
        """ Define attribute holding PythonPart matrix for update

        Args:
            matrix: placement matrix

        Returns:
            Attribute holding PythonPart matrix for update
        """

        return AllplanBaseEle.AttributeDoubleVec(AllplanBaseEle.ATTRNR_PYTHONPART_MATRIX,
                                                 AllplanUtil.VecDoubleList([matrix[i] for i in range(0, 16)]))

```

</details>