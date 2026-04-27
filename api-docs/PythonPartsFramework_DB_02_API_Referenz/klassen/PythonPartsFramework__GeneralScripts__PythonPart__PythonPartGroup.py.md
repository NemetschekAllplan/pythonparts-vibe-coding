---
title: "PythonPartGroup"
source: "PythonPartsFramework\GeneralScripts\PythonPart\PythonPartGroup.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PythonPartGroup

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPart\PythonPartGroup.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the PythonPart

## Abhängigkeiten

- `AttrBuilder`
- `BuildingElement`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `PythonPart`
- `PythonPartAttributeTakeoverService`
- `TypeCollections.ModelEleList`
- `__future__`

## Klassen

### `PythonPartGroup`

Definition of a PythonPart group
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, name: str, parameter_list: list[str], hash_value: str, python_file: str, pythonparts: list[PythonPart] | None=None, type_uuid: str='', type_display_name: str=''` | `None` | Initialize  Args:     name:              name     parameter_list:    parameter list     hash_value:        hash value of the parameter     python_file:       name of the pyp file     pythonparts:       list with the PythonParts to put into group     type_uuid:         define the selectable type defines the selectable type     type_display_name: display name for the tooltip and object palette  Raises:     TypeError:      When list of PythonParts to group contains a non-PythonPart object |
| `create` | `self` | `ModelEleList` | create the PythonPartGroup  Returns:     list with the created elements for the PythonPartGroup |
| `from_build_ele` | `cls, build_ele: BuildingElement, name: str='', pythonparts: list[PythonPart] | None=None, type_uuid: str='', type_display_name: str=''` | `PythonPartGroup` | Initialize the PythonPart group from a BuildingElement  Args:     cls:               description     build_ele:         building element with the parameter properties     name:              Name of the group. If not provided, the name of the .pyp file will be used     pythonparts:       List of PythonParts to put into group. You can initialize an empty group     type_uuid:         define the selectable type defines the selectable type     type_display_name: display name for the tooltip and object palette  Returns:     Constructed PythonPart group  Raises:     TypeError:      When list of PythonParts to group contains a non-PythonPart object |
| `append` | `self, pythonpart: PythonPart` | `None` | Add a new PythonPart to the group  Args:     pythonpart: PythonPart to add |
| `extend` | `self, pythonparts: list[PythonPart]` | `None` | Extend the group with new PythonParts  Args:     pythonparts: list of PythonParts to add to the group |
| `pythonparts` | `self` | `list[PythonPart]` | List of the PythonParts in the group  Returns:     PythonParts |
| `__str__` | `self` | `str` | create the element string  Returns:     element string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart
"""
from __future__ import annotations

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle

from BuildingElement import BuildingElement

from TypeCollections.ModelEleList import ModelEleList

from .AttrBuilder import AttrBuilder
from .PythonPart import PythonPart
from .PythonPartAttributeTakeoverService import PythonPartAttributeTakeoverService

class PythonPartGroup():
    """ Definition of a PythonPart group
    """
    def __init__(self,
                 name             : str,
                 parameter_list   : list[str],
                 hash_value       : str,
                 python_file      : str,
                 pythonparts      : (list[PythonPart] | None) = None,
                 type_uuid        : str                       = "",
                 type_display_name: str                       = ""):
        """ Initialize

        Args:
            name:              name
            parameter_list:    parameter list
            hash_value:        hash value of the parameter
            python_file:       name of the pyp file
            pythonparts:       list with the PythonParts to put into group
            type_uuid:         define the selectable type defines the selectable type
            type_display_name: display name for the tooltip and object palette

        Raises:
            TypeError:      When list of PythonParts to group contains a non-PythonPart object
        """

        self._name              = name
        self._hash_value        = hash_value
        self._python_file       = python_file
        self._parameter_list    = parameter_list
        self._type_uuid         = type_uuid
        self._type_display_name = type_display_name

        if pythonparts is None:
            pythonparts = list[PythonPart]()

        for elem in pythonparts:
            if not isinstance(elem, PythonPart):
                raise TypeError ('Provided list of the PythonParts contains an object, which is not a PythonPart')

        self._pythonparts = pythonparts


    def create(self) ->ModelEleList:
        """ create the PythonPartGroup

        Returns:
            list with the created elements for the PythonPartGroup
        """

        #------------------ Define macro placements / macro definitions for group

        macro_definitions = ModelEleList()
        macro_placements  = ModelEleList()

        for pythonpart in self._pythonparts:
            pythonpart.remove_parameter_attributes()
            
            macro_and_placement = pythonpart.create()

            macro_definitions.append(macro_and_placement[0])
            macro_placements.append(macro_and_placement[1])

        macrogroup_prop      = AllplanBasisEle.MacroGroupProperties()
        macrogroup_prop.Name = self._name
        macrogroup           = AllplanBasisEle.MacroGroupElement(macrogroup_prop, macro_placements)


        #----------------- add the attributes

        param_list_attr, geo_param_values = AttrBuilder.pyp_file_param_list_attr(self._python_file, self._parameter_list)

        attr_list = [param_list_attr,
                     AttrBuilder.python_part_attr()]

        if self._type_uuid:
            attr_list.append(AllplanBaseEle.AttributeString(AllplanBaseEle.ATTRNR_PYTHONPART_UUID, self._type_uuid))

        if self._type_display_name:
            attr_list.append(AllplanBaseEle.AttributeString(AllplanBaseEle.ATTRNR_PYTHONPART_DISPLAY_NAME, self._type_display_name))

        PythonPartAttributeTakeoverService.add_external_attributes(attr_list)

        attributes = AllplanBaseEle.Attributes([AllplanBaseEle.AttributeSet(attr_list)])

        macrogroup.SetAttributes(attributes)
        macrogroup.SetGeometryParameterValueList(geo_param_values)

        macro_definitions.append(macrogroup)

        return macro_definitions


    @classmethod
    def from_build_ele(cls,
                       build_ele        : BuildingElement,
                       name             : str                       = "",
                       pythonparts      : (list[PythonPart] | None) = None,
                       type_uuid        : str                       = "",
                       type_display_name: str                       = "") -> PythonPartGroup:
        """ Initialize the PythonPart group from a BuildingElement

        Args:
            cls:               description
            build_ele:         building element with the parameter properties
            name:              Name of the group. If not provided, the name of the .pyp file will be used
            pythonparts:       List of PythonParts to put into group. You can initialize an empty group
            type_uuid:         define the selectable type defines the selectable type
            type_display_name: display name for the tooltip and object palette

        Returns:
            Constructed PythonPart group

        Raises:
            TypeError:      When list of PythonParts to group contains a non-PythonPart object
        """

        if not name:
            name = build_ele.pyp_name

        if pythonparts is not None:
            for pyp in pythonparts:
                if not isinstance(pyp, PythonPart):
                    raise TypeError ('Provided list of the PythonParts contains an object, which is not a PythonPart')

        return cls(name,
                   build_ele.get_params_list(),
                   build_ele.get_hash(),
                   build_ele.pyp_file_name,
                   None,
                   type_uuid, type_display_name)


    def append(self,
               pythonpart: PythonPart):
        """ Add a new PythonPart to the group

        Args:
            pythonpart: PythonPart to add
        """

        self._pythonparts.append(pythonpart)


    def extend(self, pythonparts: list[PythonPart]):
        """Extend the group with new PythonParts

        Args:
            pythonparts: list of PythonParts to add to the group
        """
        self._pythonparts.extend(pythonparts)


    @property
    def pythonparts(self) -> list[PythonPart]:
        """ List of the PythonParts in the group

        Returns:
            PythonParts
        """

        return self._pythonparts


    def __str__(self) ->str:
        """ create the element string

        Returns:
            element string
        """

        return f"PythonPartGroup(name={self._name})\n" \
               f"======================================\n{self._pythonparts}\n"

```

</details>