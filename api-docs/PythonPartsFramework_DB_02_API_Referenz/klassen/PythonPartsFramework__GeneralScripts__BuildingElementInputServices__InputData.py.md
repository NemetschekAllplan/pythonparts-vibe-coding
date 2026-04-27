---
title: "InputData"
source: "PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InputData.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# InputData

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementInputServices\InputData.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Definition of the input data

## Abhängigkeiten

- `BaseInteractor`
- `BaseScriptObject`
- `BuildingElement`
- `BuildingElementComposite`
- `BuildingElementControlProperties`
- `BuildingElementListService`
- `BuildingElementPaletteService`
- `BuildingElementService`
- `BuildingElementValueConstraint`
- `CreateElementResult`
- `DocumentManager`
- `GeometryExpandService`
- `HandleModificationService`
- `InputMode`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Reinforcement`
- `PythonPart.PythonPartAttributeTakeoverService`
- `PythonScriptType`
- `StringTableService`
- `TestHelper.Mock.CoordinateInputMock`
- `TypeCollections.ModificationElementList`
- `collections.abc`
- `typing`

## Klassen

### `InputData`

Definition of the input data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, coord_input: AllplanIFW.CoordinateInput, path: str` | `None` | Initialization of class BuildingElementInputData  Args:     coord_input:    Coordinate input class     path:           Python script path |
| `init_input_data` | `self` | `None` | initialize the data          |
| `init_general_data` | `self, modify_uuid_list: ModificationElementList, asso_ref_ele: AllplanEleAdapter.BaseElementAdapter, is_only_update: bool, execution_event: AllplanSettings.ExecutionEvent, modification_matrix: AllplanGeo.Matrix3D, org_and_copy_ele_guids: dict[str, str]` | `None` | initialize the general data  Args:     modify_uuid_list:       list with the UUIDs of the modified elements     asso_ref_ele:           reference element of the associative view     is_only_update:         only update the PythonPart, no user interaction     execution_event:        execution event     modification_matrix:    modification matrix     org_and_copy_ele_guids: Map of GUIDs for original and copy elements, for the case when python part was called by copy function. |
| `prepare_script_data` | `self, parameter_data: list[str], msg_info: AllplanIFW.AddMsgInfo | None, is_modification_mode: bool, geo_matrix: AllplanGeo.Matrix3D, local_placement_matrix: AllplanGeo.Matrix3D` | `None` | prepare the script data  Args:     parameter_data:         parameter data of the selected PythonPart     msg_info:               additional mouse message info     is_modification_mode:   is started in modification mode     geo_matrix:             placement matrix     local_placement_matrix: local placement matrix |
| `set_insert_matrix_from_point` | `self, pnt: AllplanGeo.Point3D` | `None` | Set the translation into the insert matrix  Args:     pnt: input point |
| `calculate_update_matrix` | `geo_matrix: AllplanGeo.Matrix3D, local_placement_matrix: AllplanGeo.Matrix3D` | `AllplanGeo.Matrix3D` | Calculate matrix for update  Args:     geo_matrix:             geometry matrix     local_placement_matrix: local placement matrix  Returns:     original insert matrix of the PythonPart |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Definition of the input data
"""

# pylint: disable=too-many-instance-attributes

from typing import Any, cast, TYPE_CHECKING

from collections.abc import Callable

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Reinforcement as AllplanReinf

from BaseInteractor import BaseInteractor
from BaseScriptObject import BaseScriptObject
from BuildingElement import BuildingElement
from BuildingElementComposite import BuildingElementComposite
from BuildingElementListService import BuildingElementListService
from BuildingElementService import BuildingElementService

from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementValueConstraint import BuildingElementValueConstraint
from CreateElementResult import CreateElementResult
from DocumentManager import DocumentManager
from HandleModificationService import HandleModificationService
from InputMode import InputMode
from StringTableService import StringTableService

from PythonPart.PythonPartAttributeTakeoverService import PythonPartAttributeTakeoverService

from TypeCollections.ModificationElementList import ModificationElementList

from TestHelper.Mock.CoordinateInputMock import CoordinateInputMock

from .GeometryExpandService import GeometryExpandService
from .PythonScriptType import PythonScriptType

if TYPE_CHECKING:
    from BuildingElementPaletteService import BuildingElementPaletteService

class InputData:
    """ Definition of the input data
    """

    def __init__(self,
                 coord_input: AllplanIFW.CoordinateInput,
                 path       : str)                      :
        """ Initialization of class BuildingElementInputData

        Args:
            coord_input:    Coordinate input class
            path:           Python script path
        """

        if isinstance(coord_input, AllplanEleAdapter.DocumentAdapter):
            coord_input = cast(AllplanIFW.CoordinateInput, CoordinateInputMock(coord_input))

        self.coord_input = coord_input

        self.build_ele_list           : list[BuildingElement]                         = []
        self.build_ele_script         : Any                                           = Any
        self.build_ele_ctrl_props_list: list[BuildingElementControlProperties]        = []
        self.interactor               : BaseInteractor                                = cast(BaseInteractor, None)
        self.script_object            : BaseScriptObject                              = cast(BaseScriptObject, None)
        self.expand_util              : (AllplanReinf.GeometryExpansionUtil | None)   = None
        self.palette_service          : (BuildingElementPaletteService | None)        = None
        self.last_input_doc           : AllplanEleAdapter.DocumentAdapter
        self.last_view_proj           : AllplanIFW.ViewWorldProjection
        self.build_ele_composite      : BuildingElementComposite
        self.asso_ref_ele             : (AllplanEleAdapter.BaseElementAdapter | None) = None
        self.exec_switch_pythonpart   : (Callable[[str, bool], None] | None)          = None
        self.is_switch_pythonpart     : bool                                          = False

        self.str_table_service = StringTableService(path)

        self.input_mode                     : InputMode
        self.build_ele_service              : BuildingElementService
        self.file_name                      : str
        self.part_name                      : str
        self.insert_matrix                  : AllplanGeo.Matrix3D
        self.modification_ele_list          : ModificationElementList
        self.active_page                    : int
        self.create_ele_result              : CreateElementResult
        self.old_build_ele_list             : list[BuildingElement]
        self.last_expanded                  : bool
        self.b_insert_point                 : bool
        self.is_only_update                 : bool
        self.execution_event                : AllplanSettings.ExecutionEvent
        self.modification_matrix            : AllplanGeo.Matrix3D
        self.org_and_copy_ele_guids : dict[str, str]
        self.is_modify_elements             : bool
        self.is_modified_parameter          : bool
        self.python_script_type             : PythonScriptType
        self.handle_modi_service            : HandleModificationService

        self.init_input_data()


    def init_input_data(self):
        """ initialize the data
        """

        self.input_mode             = InputMode.RefPoint
        self.build_ele_service      = BuildingElementService()
        self.file_name              = ""
        self.part_name              = ""
        self.insert_matrix          = AllplanGeo.Matrix3D()
        self.modification_ele_list  = ModificationElementList()
        self.active_page            = 0
        self.create_ele_result      = CreateElementResult()
        self.old_build_ele_list     = []
        self.last_expanded          = False
        self.b_insert_point         = False
        self.is_only_update         = False
        self.execution_event        = AllplanSettings.ExecutionEvent.eCreation
        self.modification_matrix    = AllplanGeo.Matrix3D()
        self.org_and_copy_ele_guids = {}
        self.is_modify_elements     = False
        self.is_modified_parameter  = False
        self.python_script_type     = PythonScriptType.STANDARD
        self.handle_modi_service    = HandleModificationService(self.coord_input, self.build_ele_list, self.build_ele_ctrl_props_list,
                                                                None, not self.modification_ele_list.is_modification_element())


    def init_general_data(self,
                          modify_uuid_list      : ModificationElementList,
                          asso_ref_ele          : AllplanEleAdapter.BaseElementAdapter,
                          is_only_update        : bool,
                          execution_event       : AllplanSettings.ExecutionEvent,
                          modification_matrix   : AllplanGeo.Matrix3D,
                          org_and_copy_ele_guids: dict[str, str]):
        """ initialize the general data

        Args:
            modify_uuid_list:       list with the UUIDs of the modified elements
            asso_ref_ele:           reference element of the associative view
            is_only_update:         only update the PythonPart, no user interaction
            execution_event:        execution event
            modification_matrix:    modification matrix
            org_and_copy_ele_guids: Map of GUIDs for original and copy elements, for the case when python part was called by copy function.
        """

        modification_ele_list = ModificationElementList(modify_uuid_list)

        DocumentManager.get_instance().set_pythonpart_element(modification_ele_list)
        DocumentManager.get_instance().asso_ref_element = asso_ref_ele

        self.last_input_doc         = self.coord_input.GetInputViewDocument()
        self.last_view_proj         = self.coord_input.GetViewWorldProjection()
        self.asso_ref_ele           = asso_ref_ele
        self.is_only_update         = is_only_update
        self.execution_event        = execution_event
        self.modification_matrix    = modification_matrix
        self.org_and_copy_ele_guids = org_and_copy_ele_guids

        if execution_event == AllplanSettings.ExecutionEvent.eCreation:
            DocumentManager.get_instance().take_over_element = modification_ele_list.get_base_element_adapter(self.last_input_doc)

            self.modification_ele_list.append(ModificationElementList.EMPTY_GUID)
        else:
            DocumentManager.get_instance().take_over_element = AllplanEleAdapter.BaseElementAdapter()

            self.modification_ele_list.extend(modification_ele_list)


    def prepare_script_data(self,
                            parameter_data        : list[str],
                            msg_info              : (AllplanIFW.AddMsgInfo | None),
                            is_modification_mode  : bool,
                            geo_matrix            : AllplanGeo.Matrix3D,
                            local_placement_matrix: AllplanGeo.Matrix3D):
        """ prepare the script data

        Args:
            parameter_data:         parameter data of the selected PythonPart
            msg_info:               additional mouse message info
            is_modification_mode:   is started in modification mode
            geo_matrix:             placement matrix
            local_placement_matrix: local placement matrix
        """

        #----------------- get the values from the parameters

        if parameter_data:
            BuildingElementListService.read_fav_data(parameter_data, self.build_ele_list,
                                                     is_modification_mode = is_modification_mode,
                                                     script               = self.build_ele_script)

            for build_ele, ctrl_prop_list in zip(self.build_ele_list, self.build_ele_ctrl_props_list):
                BuildingElementValueConstraint.update_enable_by_constraint(build_ele, ctrl_prop_list)
                BuildingElementValueConstraint.check_property_constraint_init(build_ele, ctrl_prop_list)

            PythonPartAttributeTakeoverService.check_external_attribute_modification(self.build_ele_list)


        #----------------- set the data for the modification mode

        if is_modification_mode:
            update_matrix = self.calculate_update_matrix(geo_matrix, local_placement_matrix)

            self.build_ele_list[0].set_insert_matrix(AllplanGeo.Matrix3D(update_matrix))

            self.b_insert_point = True
            self.insert_matrix  = self.build_ele_list[0].get_insert_matrix()
            self.input_mode     = InputMode.HandleSelect


        #------------------ Initialize the geometry expansion utility

        elif self.build_ele_list[0].geometry_expand and msg_info is not None:
            GeometryExpandService.init(self, msg_info)


    def set_insert_matrix_from_point(self,
                                     pnt: AllplanGeo.Point3D):
        """ Set the translation into the insert matrix

        Args:
            pnt: input point
        """

        angle = AllplanGeo.Angle()

        if not self.is_modify_elements and self.coord_input.IsValueInputControl():
            angle.Rad = self.coord_input.GetInputControlValue()

        self.insert_matrix.SetRotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(0, 0, 1000)), angle)

        trans_vec = AllplanGeo.Vector3D(pnt)

        self.insert_matrix.SetTranslation(trans_vec)

        self.build_ele_list[0].set_insert_matrix(AllplanGeo.Matrix3D(self.insert_matrix))


    @staticmethod
    def calculate_update_matrix(geo_matrix            : AllplanGeo.Matrix3D,
                                local_placement_matrix: AllplanGeo.Matrix3D) -> AllplanGeo.Matrix3D:
        """ Calculate matrix for update

        Args:
            geo_matrix:             geometry matrix
            local_placement_matrix: local placement matrix

        Returns:
            original insert matrix of the PythonPart
        """

        local_pl__tmp_inv = AllplanGeo.Matrix3D(local_placement_matrix)
        local_pl__tmp_inv.GaussInvert()

        return local_pl__tmp_inv * geo_matrix

```

</details>