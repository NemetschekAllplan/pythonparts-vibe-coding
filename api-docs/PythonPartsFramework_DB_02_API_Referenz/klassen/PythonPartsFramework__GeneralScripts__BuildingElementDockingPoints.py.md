---
title: "BuildingElementDockingPoints"
source: "PythonPartsFramework\GeneralScripts\BuildingElementDockingPoints.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementDockingPoints

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementDockingPoints.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Script for BuildingElementInput

## Abhängigkeiten

- `BuildingElementListService`
- `BuildingElementService`
- `BuildingElementStringTableManager`
- `BuildingElementSubElementUtil`
- `DocumentManager`
- `FileNameService`
- `ImportHook`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `StringTableService`
- `Utils`
- `os`
- `os.path`
- `sys`
- `typing`

## Klassen

### `BuildingElementDockingPoints`

Definition of class BuildingElementDockingPoints
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, element: AllplanEleAdapter.BaseElementAdapter, path: str` | `None` | Initialization of class BuildingElementInput  Args:     element: element for the docking points     path:    Python script path |
| `get_docking_points` | `self, file_name: str, parameter_data: List[str]` | `Tuple[List[Tuple[str, AllplanGeo.Point3D]], List[Tuple[str, AllplanGeo.Point3D]], List[Tuple[str, AllplanGeo.Point3D]]]` | get the docking points  Args:     file_name:      file name of the pyp file     parameter_data: parameter data of the selected PythonPart  Returns:     docking points |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for BuildingElementInput
"""

# pylint: disable=too-many-instance-attributes
# pylint: disable=not-callable
# pylint: disable=bare-except
# pylint: disable=too-many-nested-blocks

import os
import os.path
import sys

from typing import List, Tuple

import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from BuildingElementService import BuildingElementService
from BuildingElementListService import BuildingElementListService
from BuildingElementStringTableManager import BuildingElementStringTableManager
from BuildingElementSubElementUtil import BuildingElementSubElementUtil
from DocumentManager import DocumentManager
from FileNameService import FileNameService
from ImportHook import ImportHookFinder
from StringTableService import StringTableService

from Utils import DockingPointUtil

sys.meta_path.append(ImportHookFinder)


class BuildingElementDockingPoints():
    """ Definition of class BuildingElementDockingPoints
    """
    def __init__(self,
                 element: AllplanEleAdapter.BaseElementAdapter,
                 path   : str):
        """ Initialization of class BuildingElementInput

        Args:
            element: element for the docking points
            path:    Python script path
        """

        if (str_table := BuildingElementStringTableManager.get_instance()) is not None:
            str_table.clear_global_string_table()

        FileNameService.set_node_script_default_path(os.path.dirname(os.path.abspath(path)))

        self.doc     = element.GetDocument()
        self.element = element

        DocumentManager.get_instance().document = self.doc

        self.str_table_service = StringTableService(path)


    def get_docking_points(self,
                           file_name     : str,
                           parameter_data: List[str]) -> Tuple[List[Tuple[str, AllplanGeo.Point3D]],
                                                               List[Tuple[str, AllplanGeo.Point3D]],
                                                               List[Tuple[str, AllplanGeo.Point3D]]]:
        """ get the docking points

        Args:
            file_name:      file name of the pyp file
            parameter_data: parameter data of the selected PythonPart

        Returns:
            docking points
        """


        #----------------- start from Allplan command line

        params = file_name.split("|")

        file_name = params[-1]


        #----------------- get the sub file name from the input by ?

        sub_file_name     = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter_data, "SubElementsName")
        add_sub_file_name = BuildingElementSubElementUtil.get_file_name_from_parameter(parameter_data, "__AddPypSubFile__")


        #------------------ Load the building element

        result, build_ele_script, build_ele_list, _,    \
            _, _, _ = \
            BuildingElementService.read_data_from_pyp(file_name,
                                                      self.str_table_service.str_table, False, \
                                                      self.str_table_service.material_str_table, sub_file_name, False, add_sub_file_name)

        if not result or build_ele_script is None:
            return [], [], []

        if parameter_data:
            BuildingElementListService.read_fav_data(parameter_data, build_ele_list, is_modification_mode = True,
                                                     script = build_ele_script)


        #----------------- get the dynamic docking points

        points_2d   = []
        points_3d   = []
        points_2d3d = []

        if getattr(build_ele_script, "create_docking_points", None) is not None:
            points_2d, points_3d, points_2d3d = build_ele_script.create_docking_points(build_ele_list[0], self.doc)

        has_dynamic_points = points_2d != [] or points_3d != [] or points_2d3d != []


        #----------------- get the existing PythonPart

        element_list = AllplanEleAdapter.BaseElementAdapterList()
        element_list.append(self.element)

        model_elements = AllplanBaseEle.GetElements(element_list)

        python_part : AllplanBasisEle.MacroPlacementElement = model_elements[0]


        #----------------- get the docking points from all elements or only dynamic group elements

        key_index = 1

        for slide in python_part.GetMacro().GetSlideList():
            slide_prop = slide.GetMacroSlideProperties()

            for slide_obj in slide.GetObjectList():
                attributes = slide_obj.GetAttributes()

                key = ""


                #--------------- check for a docking point key

                if attributes:
                    for attr_set in attributes.GetAttributeSets():
                        for attribute in attr_set.GetAttributes():
                            if isinstance(attribute, AllplanBaseEle.AttributeStringVec):
                                if attribute.Id == AllplanBaseEle.ATTRNR_PYTHONPART_PATH:
                                    key = str(attribute.Value[0])

                                    break

                        if key:
                            break


                #--------------- get the docking points

                if key or not has_dynamic_points:
                    if not key:
                        key = "__dyn_key_" + str(key_index) + "_"

                        key_index += 1

                    if slide_prop.VisibilityGeo2D and slide_prop.VisibilityGeo3D:
                        points_2d3d += DockingPointUtil.get_docking_points(key, slide_obj.GetGeometryObject())

                    elif slide_prop.VisibilityGeo3D:
                        points_3d += DockingPointUtil.get_docking_points(key, slide_obj.GetGeometryObject())

                    else:
                        points_2d += DockingPointUtil.get_docking_points(key, slide_obj.GetGeometryObject())

        return points_2d, points_3d, points_2d3d

```

</details>