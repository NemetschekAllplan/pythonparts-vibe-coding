---
title: "PythonPartTransaction"
source: "PythonPartsFramework\GeneralScripts\PythonPartTransaction.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PythonPartTransaction

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPartTransaction.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the PythonPart transaction

## Abhängigkeiten

- `BuildingElementParameterListUtil`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `NemAll_Python_Precast`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`
- `TypeCollections.ElementConnectorParameterList`
- `TypeCollections.ModificationElementList`
- `Utilities.SystemAngleUtil`
- `Utils.Connections.ElementConnectorUtil`
- `ValueTypes.Connections.TimeStampConnectionImpl`
- `ValueTypes.Data.TimeStampConnection`
- `dataclasses`
- `enum`
- `typing`

## Klassen

### `ConnectToPythonPartState`

Enumeration of the possible types of relationships in a PythonPart connection.

The child modifies the parent!

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ConnectToPythonPart`

Data class for the PythonPart connection.

Attributes:
    pyp_uuid:                   UUID of the other PythonPart, to which the current one is connected to.
    pyp_uuid_parameter_name:    Name of the parameter of the other PythonPart, where the UUID of the current PythonPart will be stored
    pyp_connection_state:       Type of the connection

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ConnectToElements`

Data class for the PythonPart connection to element(s)

Attributes:
    connection_elements:        UUID(s) of the connected elements
    connect_pyp_as_child:       Connect the PythonPart as child to the first element in the list of connection elements
                                Allows to activate the PythonPart (e.g. for deleting) when the first element is selected.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ReinforcementRearrange`

implementation of the data class for the reinforcement rearrange

Attributes:
    rearrange:           Whether to rearrange the mark numbering
    from_bar_position:   Number at which to start the mark rearranging of rebars
    from_mesh_position:  Number at which to start the mark rearranging of meshes
    to_bar_position:     Number at which to end the mark rearranging of rebars
    to_mesh_position:    Number at which to end the mark rearranging of meshes
    after_bar_position:  New starting mark number, that rearranged rebars become after rearrangement
    after_mesh_position: New starting mark number, that rearranged meshes become after rearrangement
    tolerance:           Tolerance for comparing segment lengths
    rearranged_lock:     Whether to exclude reinforcement positions, that are already been rearranged
    identical_shapes:    Whether to combine identical shapes
    identical_prefix:    Whether to consider rebar prefix attribute during the rearrangement

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `PythonPartTransaction`

Implementation of the PythonPart transaction. The transaction creates the elements in the drawing
file and introduces additional steps, that would normally have to be introduced separately, **after**
the creation. This is to make the creation easier to implement in a PythonPart script. These additional
steps are:

-   correct creation of PrecastElements (precast elementation)
-   in modification mode: recreating reinforcement labels, created with native Allplan function
-   connecting existing elements (also other PythonParts) to the created PythonPart
-   creation of UVSs using the appropriate function
-   rearrangement of the reinforcement mark numbering
-   creation of one single undo step

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, doc: AllplanEleAdapter.DocumentAdapter, connect_to_pyp: ConnectToPythonPart | list[ConnectToPythonPart]=ConnectToPythonPart(), connect_to_ele: ConnectToElements=ConnectToElements(), ele_connector_params: ElementConnectorParameterList=ElementConnectorParameterList()` | `None` | Initialize  Args:     doc:                  document of the Allplan drawing files     connect_to_pyp:       connect to pyp data     connect_to_ele:       connect to element data     ele_connector_params: list with the element connector parameter |
| `execute` | `self, placement_matrix: AllplanGeo.Matrix3D, view_world_projection: AllplanIFW.ViewWorldProjection, model_ele_list: list[Any], modification_ele_list: ModificationElementList, rearrange_reinf_pos_nr: ReinforcementRearrange=ReinforcementRearrange(), append_reinf_pos_nr: bool=True, asso_ref_object: AllplanEleAdapter.BaseElementAdapter | None=None, uuid_parameter_name: str='', _elementation_delete_py: bool=True, use_system_angle: bool=True, elements_to_delete: AllplanEleAdapter.BaseElementAdapterList | None=None, elements_to_hide: AllplanEleAdapter.BaseElementAdapterList | None=None, elements_to_show: AllplanEleAdapter.BaseElementAdapterList | None=None` | `AllplanEleAdapter.BaseElementAdapterList` | Execute the transaction. Calling the method, makes the framework perform following operations:  1.  Creates the elements from the model_ele_list in the drawing file. 2.  If there are any PrecastElements in the model_ele_list, the framework sets the right reference     point and performs the precast elementation. 3.  In the modification mode: if there are any BarPlacement in the model_ele_list, the framework     recreates the labeling for them. This is particularly important, when some reinforcement was labeled     manually outside PythonPart with native Allplan functions after creating the PythonPart. 4.  If there were any ViewSectionElements in the model_ele_list, framework creates them using the right     creation function and considering other created elements. 5.  If the uuid_parameter_name was specified, the UUID of created PythonPart is written into this parameter. 6.  When a connection to another PythonPart was specified in the constructor, a connection is created. 7.  If the rearrange_reinf_pos_nr was provided, framework checks, if the rearrangement is needed     (any new reinforcement was created). If that's the case, the mark numbers are rearranged according     to the provided settings. 8.  At the end, **one** undo step is created for all the actions mentioned.  Args:     placement_matrix:        placement matrix     view_world_projection:   view world projection     model_ele_list:          list with the model elements     modification_ele_list:   list with the UUID's of the modified PythonPart elements     rearrange_reinf_pos_nr:  data for the reinforcement rearrange     append_reinf_pos_nr:     When set to True, the reinforcement position numbers are appended to the existing position numbers     asso_ref_object:         associative view reference object     uuid_parameter_name:     if set, the model object UUID of the created PythonPart is assigned to this name     _elementation_delete_py: delete the PythonPart after the precast elementation     use_system_angle:        use the default system angle state (False = no use of the system angle)     elements_to_delete:      elements which should be delete inside the created transaction     elements_to_hide:        elements to hide persting in the drawing file     elements_to_show:        elements to show persting in the drawing file  Returns:     list with the created elements |
| `__rearrange_reinforcement` | `self, bar_pos_start_current: int, mesh_pos_start_current: int, rearrange_reinf_pos_nr: ReinforcementRearrange, undo_service: AllplanIFW.UndoRedoService` | `None` | rearrange the reinforcement  Args:     bar_pos_start_current:  current start bar position before the transaction     mesh_pos_start_current: current start mesh position before the transaction     rearrange_reinf_pos_nr: data for the reinforcement rearrange     undo_service:           undo service |
| `__set_pythonpart_connection` | `self, pyp_ele: AllplanEleAdapter.BaseElementAdapter` | `None` | set the PythonPart connection  Args:     pyp_ele: created PythonPart |
| `__create_pyp_connection` | `self, connect_to_pyp: ConnectToPythonPart, connect_to_pyp_ele: AllplanEleAdapter.BaseElementAdapter, pyp_ele: AllplanEleAdapter.BaseElementAdapter` | `None` | Creates a connection between PythonParts  Args:     connect_to_pyp:     PythonPart connection     connect_to_pyp_ele: element to which the PythonPart will be connected to     pyp_ele:            created PythonPart |
| `__create_element_connection` | `self, pyp_uuid: AllplanEleAdapter.GUID` | `None` | create the element connection  Args:     pyp_uuid: UUID of the created PythonPart |
| `__assign_pythonpart_uuid` | `uuid_parameter_name: str, undo_service: AllplanIFW.UndoRedoService, elements: AllplanEleAdapter.BaseElementAdapterList` | `AllplanEleAdapter.BaseElementAdapterList` | assign the UUID of the PythonPart to the parameter  Args:     uuid_parameter_name: if set, the model object UUID of the created PythonPart is assigned to this name     undo_service:        description     elements:            description  Returns:     model elements |
| `__get_precast_element` | `placement_matrix: AllplanGeo.Matrix3D, model_ele_list: list[Any]` | `AllplanPrecast.PrecastElement | None` | get the precast element  Args:     placement_matrix: placement matrix     model_ele_list:   list with the model elements  Returns:     precast element |
| `__get_reinforcement_label_elements` | `model_ele_list: list[Any]` | `list[Any]` | get the elements for the reinforcement labeling  Args:     model_ele_list: list with the model elements  Returns:     elements for the reinforcement labeling |
| `__create_elements` | `self, placement_matrix: AllplanGeo.Matrix3D, model_ele_list: list[Any], modification_ele_list: ModificationElementList, asso_ref_object: AllplanEleAdapter.BaseElementAdapter | None=None, append_reinf_pos_nr: bool=True` | `AllplanEleAdapter.BaseElementAdapterList` | create the elements in the drawing file  Args:     placement_matrix:      placement matrix     model_ele_list:        list with the model elements     modification_ele_list: list with the UUID's of the modified PythonPart elements     asso_ref_object:       associative view reference object     append_reinf_pos_nr:   append reinforcement position numbers  Returns:     list with the created elements |
| `__is_parent_child_connection` | `pyp_ele: AllplanEleAdapter.BaseElementAdapter` | `bool` | Check if the connection is a parent-child connection  Args:     pyp_ele: created PythonPart  Returns:     True, when the connection is a parent-child connection |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the PythonPart transaction
"""

# pylint: disable=magic-value-comparison

from typing import Any, cast

from dataclasses import dataclass, field

import enum

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_Precast as AllplanPrecast
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_Utility as AllplanUtil

from BuildingElementParameterListUtil import BuildingElementParameterListUtil as ParameterListUtil

from Utilities.SystemAngleUtil import SystemAngleUtil

from ValueTypes.Data.TimeStampConnection import TimeStampConnection
from ValueTypes.Connections.TimeStampConnectionImpl import TimeStampConnectionImpl

from Utils.Connections.ElementConnectorUtil import ElementConnectorUtil

from TypeCollections.ModificationElementList import ModificationElementList
from TypeCollections.ElementConnectorParameterList import ElementConnectorParameterList


class ConnectToPythonPartState(enum.IntEnum):
    """Enumeration of the possible types of relationships in a PythonPart connection.

    The child modifies the parent!
    """

    IS_PARENT       = 1
    """Connected PythonPart is the **parent** of the other PythonPart."""

    IS_CHILD        = 2
    """Connected PythonPart is the **child** of the other PythonPart."""

    IS_PARENT_CHILD = 3
    """Creates a connection in **both directions**."""

@dataclass
class ConnectToPythonPart():
    """Data class for the PythonPart connection.

    Attributes:
        pyp_uuid:                   UUID of the other PythonPart, to which the current one is connected to.
        pyp_uuid_parameter_name:    Name of the parameter of the other PythonPart, where the UUID of the current PythonPart will be stored
        pyp_connection_state:       Type of the connection
    """

    pyp_uuid                : AllplanEleAdapter.GUID   = AllplanEleAdapter.GUID()
    pyp_uuid_parameter_name : str                      = ""
    pyp_connection_state    : ConnectToPythonPartState = ConnectToPythonPartState.IS_PARENT_CHILD


@dataclass
class ConnectToElements():
    """Data class for the PythonPart connection to element(s)

    Attributes:
        connection_elements:        UUID(s) of the connected elements
        connect_pyp_as_child:       Connect the PythonPart as child to the first element in the list of connection elements
                                    Allows to activate the PythonPart (e.g. for deleting) when the first element is selected.
    """

    connection_elements : list[str] = field(default_factory = list)

    connect_pyp_as_child: bool = False


@dataclass
class ReinforcementRearrange():
    """ implementation of the data class for the reinforcement rearrange

    Attributes:
        rearrange:           Whether to rearrange the mark numbering
        from_bar_position:   Number at which to start the mark rearranging of rebars
        from_mesh_position:  Number at which to start the mark rearranging of meshes
        to_bar_position:     Number at which to end the mark rearranging of rebars
        to_mesh_position:    Number at which to end the mark rearranging of meshes
        after_bar_position:  New starting mark number, that rearranged rebars become after rearrangement
        after_mesh_position: New starting mark number, that rearranged meshes become after rearrangement
        tolerance:           Tolerance for comparing segment lengths
        rearranged_lock:     Whether to exclude reinforcement positions, that are already been rearranged
        identical_shapes:    Whether to combine identical shapes
        identical_prefix:    Whether to consider rebar prefix attribute during the rearrangement
    """

    rearange            : bool  = True
    from_bar_position   : int   = 0
    from_mesh_position  : int   = 0
    to_bar_position     : int   = 99999
    to_mesh_position    : int   = 99999
    after_bar_position  : int   = 0
    after_mesh_position : int   = 0
    tolerance           : float = 1
    rearranged_lock     : bool  = True
    identical_shapes    : bool  = True
    identical_prefix    : bool  = False


class PythonPartTransaction():
    """ Implementation of the PythonPart transaction. The transaction creates the elements in the drawing
    file and introduces additional steps, that would normally have to be introduced separately, **after**
    the creation. This is to make the creation easier to implement in a PythonPart script. These additional
    steps are:

    -   correct creation of PrecastElements (precast elementation)
    -   in modification mode: recreating reinforcement labels, created with native Allplan function
    -   connecting existing elements (also other PythonParts) to the created PythonPart
    -   creation of UVSs using the appropriate function
    -   rearrangement of the reinforcement mark numbering
    -   creation of one single undo step
    """

    def __init__(self,
                 doc                 : AllplanEleAdapter.DocumentAdapter,
                 connect_to_pyp      : (ConnectToPythonPart | list[ConnectToPythonPart]) = ConnectToPythonPart(),
                 connect_to_ele      : ConnectToElements                                 = ConnectToElements(),
                 ele_connector_params: ElementConnectorParameterList                     = ElementConnectorParameterList()):
        """ Initialize

        Args:
            doc:                  document of the Allplan drawing files
            connect_to_pyp:       connect to pyp data
            connect_to_ele:       connect to element data
            ele_connector_params: list with the element connector parameter
        """

        self.doc                   = doc
        self.connect_to_pyp        = connect_to_pyp if isinstance(connect_to_pyp, list) else [connect_to_pyp]
        self.connect_to_ele        = connect_to_ele
        self.ele_connector_params  = ele_connector_params
        self.is_created_connection = False


    def execute(self,                                                                                           # pylint: disable=too-many-arguments
                placement_matrix       : AllplanGeo.Matrix3D,
                view_world_projection  : AllplanIFW.ViewWorldProjection,
                model_ele_list         : list[Any],
                modification_ele_list  : ModificationElementList,
                rearrange_reinf_pos_nr : ReinforcementRearrange                            = ReinforcementRearrange(),
                append_reinf_pos_nr    : bool                                              = True,
                asso_ref_object        : (AllplanEleAdapter.BaseElementAdapter | None)     = None,
                uuid_parameter_name    : str                                               = "",
                _elementation_delete_py: bool                                              = True,
                use_system_angle       : bool                                              = True,
                elements_to_delete     : (AllplanEleAdapter.BaseElementAdapterList | None) = None,
                elements_to_hide       : (AllplanEleAdapter.BaseElementAdapterList | None) = None,
                elements_to_show       : (AllplanEleAdapter.BaseElementAdapterList | None) = None) \
                                                                    -> AllplanEleAdapter.BaseElementAdapterList:
        """ Execute the transaction. Calling the method, makes the framework perform following operations:

        1.  Creates the elements from the model_ele_list in the drawing file.
        2.  If there are any PrecastElements in the model_ele_list, the framework sets the right reference
            point and performs the precast elementation.
        3.  In the modification mode: if there are any BarPlacement in the model_ele_list, the framework
            recreates the labeling for them. This is particularly important, when some reinforcement was labeled
            manually outside PythonPart with native Allplan functions after creating the PythonPart.
        4.  If there were any ViewSectionElements in the model_ele_list, framework creates them using the right
            creation function and considering other created elements.
        5.  If the uuid_parameter_name was specified, the UUID of created PythonPart is written into this parameter.
        6.  When a connection to another PythonPart was specified in the constructor, a connection is created.
        7.  If the rearrange_reinf_pos_nr was provided, framework checks, if the rearrangement is needed
            (any new reinforcement was created). If that's the case, the mark numbers are rearranged according
            to the provided settings.
        8.  At the end, **one** undo step is created for all the actions mentioned.

        Args:
            placement_matrix:        placement matrix
            view_world_projection:   view world projection
            model_ele_list:          list with the model elements
            modification_ele_list:   list with the UUID's of the modified PythonPart elements
            rearrange_reinf_pos_nr:  data for the reinforcement rearrange
            append_reinf_pos_nr:     When set to True, the reinforcement position numbers are appended to the existing position numbers
            asso_ref_object:         associative view reference object
            uuid_parameter_name:     if set, the model object UUID of the created PythonPart is assigned to this name
            _elementation_delete_py: delete the PythonPart after the precast elementation
            use_system_angle:        use the default system angle state (False = no use of the system angle)
            elements_to_delete:      elements which should be delete inside the created transaction
            elements_to_hide:        elements to hide persting in the drawing file
            elements_to_show:        elements to show persting in the drawing file

        Returns:
            list with the created elements
        """

        AllplanBaseEle.DrawingService.LockGraphicsEngineUpdate(self.doc, True)

        bar_pos_start_current  = AllplanReinf.ReinforcementUtil.GetNextBarPositionNumber(self.doc)
        mesh_pos_start_current = AllplanReinf.ReinforcementUtil.GetNextMeshPositionNumber(self.doc)


        #----------------- final transformation in case of rotated crosshair

        modification_ele_list = ModificationElementList(modification_ele_list)          # convert old list

        if not modification_ele_list.is_modification_element() and use_system_angle:
            placement_matrix = SystemAngleUtil.execute_rotation(placement_matrix)


        #----------------- get the starting reinforcement position numbers

        if isinstance(rearrange_reinf_pos_nr, bool):                   # old state conversion
            reinf_rearrange = ReinforcementRearrange()

            reinf_rearrange.rearange = rearrange_reinf_pos_nr

            rearrange_reinf_pos_nr = reinf_rearrange

        undo_service = AllplanIFW.UndoRedoService(self.doc, True, True, True)


        #----------------- delete elements

        if elements_to_delete is not None:
            AllplanBaseEle.DeleteElements(self.doc, elements_to_delete)

            undo_service.CollectElementsForMultipleTransactions()


        #----------------- hide/show elements

        if elements_to_hide is not None:
            AllplanIFW.VisibleService.ShowElements(elements_to_hide, True, False)

            AllplanBaseEle.ShowElements(self.doc, elements_to_hide, False)

            undo_service.CollectElementsForMultipleTransactions()

        if elements_to_show is not None:
            AllplanIFW.VisibleService.ShowElements(elements_to_show, True, False)

            AllplanBaseEle.ShowElements(self.doc, elements_to_show, True)

            undo_service.CollectElementsForMultipleTransactions()

        if not model_ele_list:
            AllplanBaseEle.DrawingService.LockGraphicsEngineUpdate(self.doc, False)

            undo_service.CreateUndoStep()

            return AllplanEleAdapter.BaseElementAdapterList()


        #----------------- set the parent connection state to the macro placement

        if self.connect_to_ele.connect_pyp_as_child:
            for model_ele in model_ele_list:
                if isinstance(model_ele, AllplanBasisEle.MacroPlacementElement):
                    props = model_ele.MacroPlacementProperties

                    props.HasParentModificationBehaviour = True

                    model_ele.MacroPlacementProperties = props


        #------------------- create the elements in the DB

        elements = self.__create_elements(placement_matrix, model_ele_list, modification_ele_list,
                                          asso_ref_object, append_reinf_pos_nr)


        #----------------- update the precast element only in case of created/updated elements

        precast_ele = self.__get_precast_element(placement_matrix, model_ele_list)

        if precast_ele is not None and elements:
            AllplanPrecast.CreatePrecastElements(self.doc, placement_matrix, elements,
                                                 model_ele_list, modification_ele_list,
                                                 view_world_projection, precast_ele.deletePython)

            undo_service.CollectElementsForMultipleTransactions()


        #----------------- create the reinforcement labeling and the sections and views

        reinf_label_ele_list = self.__get_reinforcement_label_elements(model_ele_list)

        AllplanReinf.CreateReinforcementLabeling(self.doc, placement_matrix, reinf_label_ele_list,
                                                 view_world_projection, undo_service)

        AllplanBaseEle.CreateSectionsAndViews(self.doc, placement_matrix, elements,
                                              model_ele_list, view_world_projection, undo_service)


        #----------------- set the UUID from the created PythonPart placement to the UUID parameter

        model_elements = self.__assign_pythonpart_uuid(uuid_parameter_name, undo_service, elements)


        #----------------- create the connections to the PythonPart

        if (pyp_ele := next((element for element in elements \
                             if AllplanBaseEle.PythonPartService.IsPythonPartGroupElement(element)), None)) is None:
            pyp_ele = next((element for element in elements if AllplanBaseEle.PythonPartService.IsPythonPartElement(element)), None)

        if pyp_ele is not None:
            pyp_uuid = pyp_ele.GetModelElementUUID()

            self.__set_pythonpart_connection(pyp_ele)

            self.__create_element_connection(pyp_uuid)

            if self.is_created_connection:
                AllplanBaseEle.AssociationService.ExecuteUpdate(self.doc)

            elif not self.__is_parent_child_connection(pyp_ele):
                AllplanBaseEle.AssociationService.DeletePythonPartAssociation(self.doc, pyp_uuid)



        #----------------- rearrange the reinforcement position numbers

        self.__rearrange_reinforcement(bar_pos_start_current, mesh_pos_start_current,
                                       rearrange_reinf_pos_nr, undo_service)


        #----------------- create the placement connection

        if self.ele_connector_params:
            ElementConnectorUtil.create_element_connector_pythonpart(self.ele_connector_params, elements[0], self.doc)


        #----------------- create the undo step

        AllplanBaseEle.DrawingService.LockGraphicsEngineUpdate(self.doc, False)

        undo_service.CreateUndoStep()

        return model_elements


    def __rearrange_reinforcement(self,
                                  bar_pos_start_current : int,
                                  mesh_pos_start_current: int,
                                  rearrange_reinf_pos_nr: ReinforcementRearrange,
                                  undo_service          : AllplanIFW.UndoRedoService):
        """ rearrange the reinforcement

        Args:
            bar_pos_start_current:  current start bar position before the transaction
            mesh_pos_start_current: current start mesh position before the transaction
            rearrange_reinf_pos_nr: data for the reinforcement rearrange
            undo_service:           undo service
        """

        if rearrange_reinf_pos_nr.rearange and \
           (bar_pos_start_current  < AllplanReinf.ReinforcementUtil.GetNextBarPositionNumber(self.doc) or \
            mesh_pos_start_current < AllplanReinf.ReinforcementUtil.GetNextMeshPositionNumber(self.doc)):
            undo_service.CollectElementsForMultipleTransactions()

            from_bar_position   = bar_pos_start_current  if rearrange_reinf_pos_nr.from_bar_position   == 0 else \
                                  rearrange_reinf_pos_nr.from_bar_position
            from_mesh_position  = mesh_pos_start_current if rearrange_reinf_pos_nr.from_mesh_position  == 0 else \
                                  rearrange_reinf_pos_nr.from_mesh_position
            after_bar_position  = bar_pos_start_current  if rearrange_reinf_pos_nr.after_bar_position  == 0 else \
                                  rearrange_reinf_pos_nr.after_bar_position
            after_mesh_position = mesh_pos_start_current if rearrange_reinf_pos_nr.after_mesh_position == 0 else \
                                  rearrange_reinf_pos_nr.after_mesh_position

            AllplanReinf.ReinforcementUtil.Rearrange(self.doc,
                                                     from_bar_position,                       from_mesh_position,
                                                     rearrange_reinf_pos_nr.to_bar_position,  rearrange_reinf_pos_nr.to_mesh_position,
                                                     after_bar_position,                      after_mesh_position,
                                                     rearrange_reinf_pos_nr.tolerance,        rearrange_reinf_pos_nr.rearranged_lock,
                                                     rearrange_reinf_pos_nr.identical_shapes, rearrange_reinf_pos_nr.identical_prefix,
                                                     False)


    def __set_pythonpart_connection(self,
                                    pyp_ele: AllplanEleAdapter.BaseElementAdapter):
        """ set the PythonPart connection

        Args:
            pyp_ele: created PythonPart
        """

        for connect_to_pyp in self.connect_to_pyp:
            if connect_to_pyp.pyp_uuid == AllplanEleAdapter.GUID():
                continue

            if not connect_to_pyp.pyp_uuid_parameter_name:
                AllplanUtil.ShowMessageBox("The parameter name in ConnectToPythonPart is empty!", AllplanUtil.MB_OK)

                continue


            #----------------- get the UUID of the created PythonPart

            connect_to_pyp_ele = AllplanEleAdapter.BaseElementAdapter.FromGUID(connect_to_pyp.pyp_uuid, self.doc)

            if not connect_to_pyp_ele.IsNull():
                self.__create_pyp_connection(connect_to_pyp, connect_to_pyp_ele, pyp_ele)


    def __create_pyp_connection(self,
                                connect_to_pyp    : ConnectToPythonPart,
                                connect_to_pyp_ele: AllplanEleAdapter.BaseElementAdapter,
                                pyp_ele           : AllplanEleAdapter.BaseElementAdapter):
        """ Creates a connection between PythonParts

        Args:
            connect_to_pyp:     PythonPart connection
            connect_to_pyp_ele: element to which the PythonPart will be connected to
            pyp_ele:            created PythonPart
        """

        _, pyp_name, pyp_parameters = AllplanBaseEle.PythonPartService.GetParameter(connect_to_pyp_ele)

        if (connected_pyps := ParameterListUtil.get_value(pyp_parameters, connect_to_pyp.pyp_uuid_parameter_name,
                                                          "TimeStampConnection")) is None:
            return

        if not isinstance(connected_pyps, list):
            connected_pyps = [connected_pyps]

        pyp_uuid = pyp_ele.GetModelElementUUID()

        str_pyp_uuid = str(pyp_uuid)


        #--------------------- create the association

        if (pyp_connection := next((item for item in connected_pyps if item.uuid == pyp_uuid), None)) is None:
            if connect_to_pyp.pyp_connection_state in {ConnectToPythonPartState.IS_PARENT,
                                                       ConnectToPythonPartState.IS_PARENT_CHILD}:
                AllplanBaseEle.AssociationService.AssociateElementsWithPythonPart(self.doc,
                                                                                 [str_pyp_uuid],
                                                                                 connect_to_pyp.pyp_uuid)

            if connect_to_pyp.pyp_connection_state in {ConnectToPythonPartState.IS_CHILD,
                                                       ConnectToPythonPartState.IS_PARENT_CHILD}:
                AllplanBaseEle.AssociationService.AssociateElementsWithPythonPart(self.doc,
                                                                                 [str(connect_to_pyp.pyp_uuid)],
                                                                                 pyp_uuid)

            connected_pyps.append(TimeStampConnection(pyp_ele))

        elif pyp_connection.time_stamp == pyp_ele.GetTimeStamp():
            self.is_created_connection = True

            return

        else:
            pyp_connection.time_stamp = pyp_ele.GetTimeStamp()

        self.is_created_connection = True


        #----------------- assign the connection data to the connected PythonPart

        ParameterListUtil.set_value(pyp_parameters, connect_to_pyp.pyp_uuid_parameter_name,
                                    TimeStampConnectionImpl.to_string(connected_pyps))

        AllplanBaseEle.PythonPartService.SetParameter(connect_to_pyp_ele, pyp_name, pyp_parameters)


    def __create_element_connection(self,
                                    pyp_uuid: AllplanEleAdapter.GUID):
        """ create the element connection

        Args:
            pyp_uuid: UUID of the created PythonPart
        """

        if not self.connect_to_ele.connection_elements:
            return

        AllplanBaseEle.AssociationService.AssociateElementsWithPythonPart(self.doc, self.connect_to_ele.connection_elements,
                                                                          pyp_uuid, self.connect_to_ele.connect_pyp_as_child)

        self.is_created_connection = True


    @staticmethod
    def __assign_pythonpart_uuid(uuid_parameter_name: str,
                                 undo_service       : AllplanIFW.UndoRedoService,
                                 elements           : AllplanEleAdapter.BaseElementAdapterList) -> AllplanEleAdapter.BaseElementAdapterList:
        """ assign the UUID of the PythonPart to the parameter

        Args:
            uuid_parameter_name: if set, the model object UUID of the created PythonPart is assigned to this name
            undo_service:        description
            elements:            description

        Returns:
            model elements
        """

        if not uuid_parameter_name:
            return elements


        #----------------- adapt the PythonPart parameter with the UUID

        model_elements = AllplanEleAdapter.BaseElementAdapterList()

        for element in elements:
            if AllplanBaseEle.PythonPartService.IsPythonPartElement(element) or \
                AllplanBaseEle.PythonPartService.IsPythonPartGroupElement(element):
                pyp_uuid = element.GetModelElementUUID()

                _, pyp_name, pyp_parameters = AllplanBaseEle.PythonPartService.GetParameter(element, True)

                undo_service.CollectElementsForMultipleTransactions()

                ParameterListUtil.set_value(pyp_parameters, uuid_parameter_name, str(pyp_uuid))

                model_elements.append(AllplanBaseEle.PythonPartService.SetParameter(element, pyp_name, pyp_parameters))
            else:
                model_elements.append(element)

        return model_elements


    @staticmethod
    def __get_precast_element(placement_matrix: AllplanGeo.Matrix3D,
                              model_ele_list  : list[Any]) -> (AllplanPrecast.PrecastElement | None):
        """ get the precast element

        Args:
            placement_matrix: placement matrix
            model_ele_list:   list with the model elements

        Returns:
            precast element
        """

        precast_ele = None

        for ele in enumerate(model_ele_list):
            if isinstance(ele[1], AllplanPrecast.PrecastElement):
                precast_ele       = cast(AllplanPrecast.PrecastElement, ele[1])
                precast_ele_props = precast_ele.Properties

                precast_ele_props.ReferencePoint = AllplanGeo.Transform(precast_ele_props.ReferencePoint,
                                                                        placement_matrix)

                ele[1].Properties = precast_ele_props

        return precast_ele


    @staticmethod
    def __get_reinforcement_label_elements(model_ele_list: list[Any]) -> list[Any]:
        """ get the elements for the reinforcement labeling

        Args:
            model_ele_list: list with the model elements

        Returns:
            elements for the reinforcement labeling
        """

        return [ele for ele in model_ele_list if isinstance(ele, (AllplanReinf.BarPlacement,
                                                                  AllplanReinf.BarsRepresentation,
                                                                  AllplanBasisEle.MacroPlacementElement,
                                                                  AllplanReinf.MeshPlacement))]

    def __create_elements(self,
                          placement_matrix     : AllplanGeo.Matrix3D,
                          model_ele_list       : list[Any],
                          modification_ele_list: ModificationElementList,
                          asso_ref_object      : (AllplanEleAdapter.BaseElementAdapter | None) = None,
                          append_reinf_pos_nr  : bool                                          = True) -> AllplanEleAdapter.BaseElementAdapterList:     # pylint: disable=line-too-long
        """ create the elements in the drawing file

        Args:
            placement_matrix:      placement matrix
            model_ele_list:        list with the model elements
            modification_ele_list: list with the UUID's of the modified PythonPart elements
            asso_ref_object:       associative view reference object
            append_reinf_pos_nr:   append reinforcement position numbers

        Returns:
            list with the created elements
        """

        #----------------- element creation or single PythonPart modification

        if len(modification_ele_list.get_base_element_adapter_list(self.doc)) <= 1:
            return AllplanBaseEle.CreateElements(self.doc, placement_matrix, model_ele_list, modification_ele_list,
                                                asso_ref_object, append_reinf_pos_nr, False)


        #----------------- split the list for a single PythonPart element modification

        index = 0

        pyp_model_ele_list = []

        created_elements = AllplanEleAdapter.BaseElementAdapterList()

        for model_ele in model_ele_list:
            if isinstance(model_ele, AllplanBasisEle.MacroElement):
                pyp_model_ele_list.append(model_ele)

            elif isinstance(model_ele, (AllplanBasisEle.MacroPlacementElement, AllplanBasisEle.MacroGroupElement)):
                pyp_model_ele_list.append(model_ele)

                created_elements += AllplanBaseEle.CreateElements(self.doc, placement_matrix, pyp_model_ele_list,
                                                                  [modification_ele_list[index]],
                                                                  asso_ref_object, append_reinf_pos_nr, False)

                index += 1

                pyp_model_ele_list.clear()

        return created_elements


    @staticmethod
    def __is_parent_child_connection(pyp_ele: AllplanEleAdapter.BaseElementAdapter) -> bool:
        """ Check if the connection is a parent-child connection

        Args:
            pyp_ele: created PythonPart

        Returns:
            True, when the connection is a parent-child connection
        """

        _, _, pyp_parameters = AllplanBaseEle.PythonPartService.GetParameter(pyp_ele)

        if any("TimeStampConnection(" in param for param in pyp_parameters):
            return True

        return False

```

</details>