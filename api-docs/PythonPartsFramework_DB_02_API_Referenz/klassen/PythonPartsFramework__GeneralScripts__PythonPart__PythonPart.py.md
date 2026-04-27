---
title: "PythonPart"
source: "PythonPartsFramework\GeneralScripts\PythonPart\PythonPart.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PythonPart

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPart\PythonPart.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the PythonPart

## Abhängigkeiten

- `AttrBuilder`
- `BuildingElementAttributeList`
- `DocumentManager`
- `NemAll_Python_ArchElements`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_Precast`
- `NemAll_Python_Reinforcement`
- `PythonPartAttributeTakeoverService`
- `TypeCollections.ModelEleList`
- `View`
- `View2D`
- `View2D3D`
- `View3D`
- `ViewCode`
- `__future__`
- `typing`
- `uuid`

## Klassen

### `PythonPart`

Definition of class PythonPart
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, name: str, parameter_list: list[str], hash_value: str, python_file: str, views: list[View2D | View3D | View2D3D | View] | None=None, matrix: AllplanGeo.Matrix3D=AllplanGeo.Matrix3D(), common_props: AllplanBaseEle.CommonProperties | None=None, reinforcement: list[Any] | None=None, attribute_list: list[Any] | None=None, library_elements: list[Any] | None=None, architecture_elements: list[Any] | None=None, label_elements: list[Any] | None=None, fixture_elements: list[Any] | None=None, assembly_elements: list[Any] | None=None, mws_elements: list[Any] | None=None, placement_matrix: AllplanGeo.Matrix3D | None=None, type_uuid: str='', type_display_name: str='', structured_container_attributes: dict[uuid.UUID, BuildingElementAttributeList] | None=None` | `None` | Initialization of class PythonPart  Args:     name:                  name of the modified property     parameter_list:        list with the parameter     hash_value:            Hash value of the parameter     python_file:           File name of the pyp file     views:                 Views for PythonPart     matrix:                Local matrix of PythonPart, used for the local geometry transformation     common_props:          Common properties of PythonPart     reinforcement:         Reinforcement elements for PythonPart     attribute_list:        Attribute list     library_elements:      Library elements for PythonPart     architecture_elements: Architecture elements for PythonPart     label_elements:        Label elements     fixture_elements:      Fixture elements for PythonPart     assembly_elements:     assembly element     mws_elements:          mvs elements     placement_matrix:      Placement matrix of the PythonPart     type_uuid:             define the selectable type defines the selectable type     type_display_name:     display name for the tooltip and object palette     structured_container_attributes: attributes for StructuredContainer |
| `create` | `self` | `ModelEleList` | create the PythonPart  Returns:     created elements for the PythonPart |
| `remove_parameter_attributes` | `self` | `None` | remove the parameter attributes from the PythonPart          |
| `__repr__` | `self` | `str` | create the element string  Returns:     element string |
| `views` | `self` | `list[View]` | Get the views  Returns:     views |
| `add` | `self, view: View` | `None` | Add one view  Args:     view: view |
| `distortion_state` | `self, state: bool` | `None` | Set distortion state  Args:     state: distortion state |
| `leading_macro` | `self, macro_leading: bool` | `None` | Set leading macro  Args:     macro_leading: leading macro state |
| `reset` | `self, views: list[View]` | `None` | Reset views  Args:     views: views |
| `matrix` | `self` | `AllplanGeo.Matrix3D` | Transformation matrix used for local transformation of the PythonPart  Returns:     transformation matrix |
| `matrix` | `self, matrix: AllplanGeo.Matrix3D` | `None` | set the local placement matrix  Args:     matrix: placement matrix |
| `placement_matrix` | `self` | `AllplanGeo.Matrix3D | None` | Placement matrix  Returns:     placement matrix |
| `placement_matrix` | `self, matrix: AllplanGeo.Matrix3D` | `None` | set the placement matrix  Args:     matrix: placement matrix |
| `sub_pythonpart_key` | `self` | `str` | sub PythonPart key  Returns:     sub PythonPart key |
| `sub_pythonpart_key` | `self, sub_pythonpart_key: str` | `None` | set the sub PythonPart key  Args:     sub_pythonpart_key: sub PythonPart key |
| `__test_elements` | `elements: list[Any] | None, allowed_ele_type: Any` | `list[Any]` | test the elements  Args:     elements:         elements to test     allowed_ele_type: allowed element type  Returns:     adapted elements  Raises:     TypeError: raised in case of wrong element type |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart
"""
from __future__ import annotations

from typing import Any

import uuid

import NemAll_Python_ArchElements as AllplanArch
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Precast as AllplanPrecast
import NemAll_Python_Reinforcement as AllplanReinf

from BuildingElementAttributeList import BuildingElementAttributeList
from DocumentManager import DocumentManager

from TypeCollections.ModelEleList import ModelEleList

from .AttrBuilder import AttrBuilder
from .PythonPartAttributeTakeoverService import PythonPartAttributeTakeoverService
from .View import View
from .View2D import View2D
from .View3D import View3D
from .View2D3D import View2D3D
from .ViewCode import ViewCode

class PythonPart():                                             # pylint: disable=too-many-instance-attributes
    """ Definition of class PythonPart
    """

    def __init__(self,                                          # pylint: disable=too-many-arguments
                 name                           : str,
                 parameter_list                 : list[str],
                 hash_value                     : str,
                 python_file                    : str,
                 views                          : (list[(View2D | View3D | View2D3D | View)] | None)     = None,
                 matrix                         : AllplanGeo.Matrix3D                                    = AllplanGeo.Matrix3D(),
                 common_props                   : (AllplanBaseEle.CommonProperties | None)               = None,
                 reinforcement                  : (list[Any] | None)                                     = None,
                 attribute_list                 : (list[Any] | None)                                     = None,
                 library_elements               : (list[Any] | None)                                     = None,
                 architecture_elements          : (list[Any] | None)                                     = None,
                 label_elements                 : (list[Any] | None)                                     = None,
                 fixture_elements               : (list[Any] | None)                                     = None,
                 assembly_elements              : (list[Any] | None)                                     = None,
                 mws_elements                   : (list[Any] | None)                                     = None,
                 placement_matrix               : (AllplanGeo.Matrix3D | None)                           = None,
                 type_uuid                      : str                                                    = "",
                 type_display_name              : str                                                    = "",
                 structured_container_attributes: (dict[uuid.UUID, BuildingElementAttributeList] | None) = None):
        """ Initialization of class PythonPart

        Args:
            name:                  name of the modified property
            parameter_list:        list with the parameter
            hash_value:            Hash value of the parameter
            python_file:           File name of the pyp file
            views:                 Views for PythonPart
            matrix:                Local matrix of PythonPart, used for the local geometry transformation
            common_props:          Common properties of PythonPart
            reinforcement:         Reinforcement elements for PythonPart
            attribute_list:        Attribute list
            library_elements:      Library elements for PythonPart
            architecture_elements: Architecture elements for PythonPart
            label_elements:        Label elements
            fixture_elements:      Fixture elements for PythonPart
            assembly_elements:     assembly element
            mws_elements:          mvs elements
            placement_matrix:      Placement matrix of the PythonPart
            type_uuid:             define the selectable type defines the selectable type
            type_display_name:     display name for the tooltip and object palette
            structured_container_attributes: attributes for StructuredContainer
        """

        self._name                            = name
        self._parameter_list                  = parameter_list
        self._hash_value                      = hash_value
        self._python_file                     = python_file
        self._catalog_name                    = "STD\\Library" # set to some useful value
        self._sub_type                        = AllplanBasisEle.PYTHON_PART_SUB_TYPE       # 1780
        self._domain_type                     = AllplanBasisEle.PYTHON_PART_DOMAIN_TYPE # 21400
        self._matrix                          = matrix
        self._distortion_state                = False #block distortion for standard PythonParts
        self._label_elements                  = label_elements
        self._placement_matrix                = placement_matrix
        self._leading_macro                   = False
        self._type_uuid                       = type_uuid
        self._type_display_name               = type_display_name
        self._structured_container_attributes = structured_container_attributes if structured_container_attributes is not None else {}
        self._sub_pythonpart_key              = ""


        #----------------- use the default or current common properties

        if common_props is None:
            common_props = DocumentManager.get_instance().common_properties

        self._common_props = common_props

        self._views                 = views if views is not None else list[View]()
        self._reinforcement         = self.__test_elements(reinforcement, AllplanReinf.ReinfElement)
        self._library_elements      = self.__test_elements(library_elements, AllplanBasisEle.LibraryElement)
        self._architecture_elements = self.__test_elements(architecture_elements, (AllplanArch.ArchElement, AllplanBasisEle.BasisElement))
        self._attribute_list        = self.__test_elements(attribute_list, AllplanBaseEle.Attribute)
        self._fixture_elements      = self.__test_elements(fixture_elements,
                                                           (AllplanPrecast.FixturePlacementElement, AllplanPrecast.FixtureGroupElement))
        self._assembly_elements      = self.__test_elements(assembly_elements, AllplanPrecast.AssemblyGroupElement)
        self._mws_elements           = self.__test_elements(mws_elements, AllplanPrecast.PrecastMWSElement)



    def create(self) -> ModelEleList:
        """ create the PythonPart

        Returns:
            created elements for the PythonPart
        """

        model_element_list = ModelEleList()

        slide_list : list[AllplanBasisEle.MacroSlideElement] = [ViewCode(self._hash_value).create()]

        slide_list += [view.create() for view in self._views]

        macro_prop             = AllplanBasisEle.MacroProperties()
        macro_prop.Name        = self._name
        macro_prop.CatalogName = self._catalog_name
        macro_prop.SubType     = self._sub_type
        macro_prop.DomainType  = self._domain_type

        macro = AllplanBasisEle.MacroElement(macro_prop, slide_list)

        for sub_element_id, attribute_list in self._structured_container_attributes.items():
            attrib_set = AllplanBaseEle.AttributeSet(attribute_list.get_attribute_list())

            macro.SetAttributesForSubElementInStrucutredContainer(attrib_set, sub_element_id)

        macro.SetHash(self._hash_value)

        mp_prop = AllplanBasisEle.MacroPlacementProperties()

        mp_prop.Matrix          = self._matrix if self._placement_matrix is None else self._placement_matrix * self._matrix
        mp_prop.SubType         = self._sub_type
        mp_prop.DomainType      = self._domain_type
        mp_prop.DistortionState = self._distortion_state
        mp_prop.LeadingMacro    = self._leading_macro
        mp_prop.Name            = self._name

        macro_placement = AllplanBasisEle.MacroPlacementElement(self._common_props, mp_prop, macro,
                                                                self._reinforcement, self._library_elements,
                                                                self._architecture_elements, self._fixture_elements,
                                                                self._assembly_elements, self._mws_elements)

        # add all public attributes

        attr_list = self._attribute_list

        param_list_attr, geo_param_values = AttrBuilder.pyp_file_param_list_attr(self._python_file, self._parameter_list)

        attr_list.append(param_list_attr)
        attr_list.append(AttrBuilder.python_part_attr())

        if self._type_uuid:
            attr_list.append(AllplanBaseEle.AttributeString(AllplanBaseEle.ATTRNR_PYTHONPART_UUID, self._type_uuid))

        if self._type_display_name:
            attr_list.append(AllplanBaseEle.AttributeString(AllplanBaseEle.ATTRNR_PYTHONPART_DISPLAY_NAME, self._type_display_name))

        if self._sub_pythonpart_key:
            attr_list.append(AllplanBaseEle.AttributeString(AllplanBaseEle.ATTRNR_SUB_PYTHONPART_KEY, self._sub_pythonpart_key))

            if (ele_adapter := DocumentManager.get_instance().sub_pythonparts.get(self._sub_pythonpart_key)) is not None:
                macro_placement.BaseElementAdapter = ele_adapter

        attr_list.append(AttrBuilder.placement_matrix_attr(self._matrix))

        PythonPartAttributeTakeoverService.add_external_attributes(attr_list, self._sub_pythonpart_key)

        attributes = AllplanBaseEle.Attributes([AllplanBaseEle.AttributeSet(attr_list)])

        macro_placement.SetAttributes(attributes)
        macro_placement.SetGeometryParameterValueList(geo_param_values)

        if self._label_elements:
            macro_placement.SetLabelElements(self._label_elements)

        model_element_list.append(macro)
        model_element_list.append(macro_placement)

        return model_element_list


    def remove_parameter_attributes(self):
        """ remove the parameter attributes from the PythonPart
        """

        for index in range(len(self._attribute_list) - 1, -1, -1):
            if self._attribute_list[index].Id in {AllplanBaseEle.ATTRNR_PYTHONPART_PATH,
                                                  AllplanBaseEle.ATTRNR_PYTHONPART_CHECK,
                                                  AllplanBaseEle.ATTRNR_PYTHONPART_MATRIX}:
                del self._attribute_list[index]


    def __repr__(self) ->str:
        """ create the element string

        Returns:
            element string
        """

        return f"PythonPart(_name={self._name}, " \
               f"_hash_value     ={self._hash_value}, " \
               f"_python_file    ={self._python_file}, " \
               f"_catalog_name   ={self._catalog_name},"\
               f"_sub_type       ={self._sub_type}, " \
               f"_domain_type    ={self._domain_type}\n" \
               f"======================================\n{self.views}\n"


    @property
    def views(self) -> list[View]:
        """ Get the views

        Returns:
            views
        """
        return self._views

    def add(self, view: View):
        """ Add one view

        Args:
            view: view
        """

        self._views.append(view)

    def distortion_state(self, state: bool):
        """ Set distortion state

        Args:
            state: distortion state
        """
        self._distortion_state = state

    def leading_macro(self,
                      macro_leading: bool):
        """ Set leading macro

        Args:
            macro_leading: leading macro state
        """
        self._leading_macro = macro_leading

    def reset(self, views: list[View]):
        """ Reset views

        Args:
            views: views
        """
        self._views = views

    @property
    def matrix(self) -> AllplanGeo.Matrix3D:
        """ Transformation matrix used for local transformation of the PythonPart

        Returns:
            transformation matrix
        """

        return self._matrix

    @matrix.setter
    def matrix(self,
               matrix: AllplanGeo.Matrix3D):
        """ set the local placement matrix

        Args:
            matrix: placement matrix
        """
        self._matrix = AllplanGeo.Matrix3D(matrix)

    @property
    def placement_matrix(self) -> (AllplanGeo.Matrix3D | None):
        """ Placement matrix

        Returns:
            placement matrix
        """

        return self._placement_matrix

    @placement_matrix.setter
    def placement_matrix(self,
                         matrix: AllplanGeo.Matrix3D):
        """ set the placement matrix

        Args:
            matrix: placement matrix
        """
        self._placement_matrix = AllplanGeo.Matrix3D(matrix)

    @property
    def sub_pythonpart_key(self) -> str:
        """ sub PythonPart key

        Returns:
            sub PythonPart key
        """

        return self._sub_pythonpart_key

    @sub_pythonpart_key.setter
    def sub_pythonpart_key(self,
                           sub_pythonpart_key: str):
        """ set the sub PythonPart key

        Args:
            sub_pythonpart_key: sub PythonPart key
        """
        self._sub_pythonpart_key = sub_pythonpart_key


    @staticmethod
    def __test_elements(elements        : (list[Any] | None),
                        allowed_ele_type: Any) -> list[Any]:
        """ test the elements

        Args:
            elements:         elements to test
            allowed_ele_type: allowed element type

        Returns:
            adapted elements

        Raises:
            TypeError: raised in case of wrong element type
        """

        if elements is None:
            return []

        for ele in elements:
            if not isinstance(ele, allowed_ele_type):
                parts = str(type(allowed_ele_type)).split(".")

                allowed_ele_type_str = parts[1].rstrip("'>").lower() if len(parts) < 1 else str(type(allowed_ele_type()))

                parts = str(type(ele)).split(".")

                ele_type_str = parts[1].rstrip("'>").lower() if len(parts) < 1 else str(type(ele))

                print(f"===== Wrong element for type {allowed_ele_type_str} element =====")
                print(ele)

                raise TypeError (f"PythonPart.__init__: Element{ele_type_str} is not of type {ele_type_str}")

        return elements

```

</details>