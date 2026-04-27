---
title: "NemAll_Python_IFW_Input"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_IFW_Input.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_IFW_Input

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_IFW_Input.pyi`  
> **Typ:** `stub`  
> **Tags:** `dokumentation`

## Inhalt

```text
# pylint: disable=invalid-name
# pylint: disable=used-before-assignment
# pylint: disable=too-many-public-methods
# pylint: disable=c-extension-no-member
# pylint: disable=import-self
# pylint: disable=empty-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=line-too-long
# pylint: disable=unused-argument
# pylint: disable=redefined-builtin
# pylint: disable=anomalous-backslash-in-string
# pylint: disable=too-few-public-methods
# pylint: disable=function-redefined
# pylint: disable=eq-without-hash
# pylint: disable=too-many-lines
# pylint: disable=too-many-arguments

"""Exposed classes and functions from NemAll_Python_IFW_Input"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_BasisElements
import NemAll_Python_IFW_ElementAdapter
import NemAll_Python_Utility
import NemAll_Python_Geometry


__all__ = [
    "AddMsgInfo",
    "BuildingElementInputControls",
    "CNOI_DocumentWrapper",
    "CoordinateInput",
    "CoordinateInputMode",
    "CoordinateInputResult",
    "DockingPoint",
    "EAST_VIEW",
    "ELEMENT3D_EDGES",
    "ELEMENT3D_FACES",
    "ELEMENT3D_NO_SPLIT",
    "ElementHandleType",
    "ElementSelect",
    "ElementSelectFilterSetting",
    "FREE_ONLY_3D",
    "FREE_VIEW",
    "GROUND_PLAN",
    "HandleService",
    "HighlightService",
    "InputFunctionStarter",
    "InputStringConvert",
    "InputViewData",
    "InputViewDocumentData",
    "LocalCoordinateSystemFlags",
    "NORTH_EAST_VIEW",
    "NORTH_VIEW",
    "NORTH_WEST_VIEW",
    "PolygonInput",
    "PolylineInput",
    "PostElementSelection",
    "PreviewSymbolBuilder",
    "QueryTypeID",
    "SOUTH_EAST_VIEW",
    "SOUTH_VIEW",
    "SOUTH_WEST_VIEW",
    "SelectElementsService",
    "SelectionMode",
    "SelectionQuery",
    "SnoopElementGeometryFilter",
    "UndoRedoService",
    "ValueInputControlData",
    "ViewWorldProjection",
    "VisibleService",
    "WEST_VIEW",
    "WORKING_PLANE_VIEW",
    "eDocumentSnoopType",
    "eDrawElementIdentPointSymbols",
    "eIdentificationMode",
    "eLayerSnoopType",
    "eProjectionType",
    "eSelectGeometry",
    "eSelectObject",
    "eSelectSubObject",
    "eSplitElement3D",
    "eTrackLineType",
    "eValueInputControlType"
]


class AddMsgInfo():

    def __init__(self):
        """Initialize
        """

class BuildingElementInputControls():
    """Implementation of the building element input controls
    """
    def CloseControls(self):
        """Close the input controls
        """
    def CreateControls(self, handlePropList: object, insertionMat: NemAll_Python_Geometry.Matrix3D, viewProj: ViewWorldProjection,
                       bUpdateControls: bool, assoRefObj: object):
        """Create the controls

        Args:
            handlePropList:  List with the handle properties
            insertionMat:    Transformation matrix
            viewProj:        View world projection
            bUpdateControls: Update the controls: true/false
            assoRefObj:      Reference element for the drawing inside the associative views
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: BuildingElementInputControls):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class CNOI_DocumentWrapper():

    def __init__(self):
        """Initialize
        """

class InputViewDocumentData():
    """Implementation of the functions for the input view and document data
    """
    def EnableAssistWndClick(self, bEnable: bool):
        """Enable/disable a click inside the assist window

        Args:
            bEnable: Enable a click inside the assist window: 1/0
        """
    def GetActiveViewDocument(self) -> NemAll_Python_IFW_ElementAdapter.DocumentAdapter:
        """Get the active view document

        Returns:
            Active view document
        """
    def GetInputViewDocument(self) -> NemAll_Python_IFW_ElementAdapter.DocumentAdapter:
        """Get the input view document

        Returns:
            Input view document
        """
    def GetInputViewDocumentID(self) -> int:
        """Get the document ID of the current input view.

        Returns:
            Document ID of the current input view
        """
    def GetViewWorldProjection(self) -> ViewWorldProjection:
        """Get the view-world projection object

        Returns:
            View-world projection object
        """

class CoordinateInputMode():
    """Settings regarding mode, in which elements and/or points should be identified during point input
    """
    def GetIdentMode(self) -> eIdentificationMode:
        """Get the identification mode

        Returns:
            Identification mode
        """
    def IsLocalCoordInput(self) -> bool:
        """Get the local coordinate input state

        Returns:
            Local coordinate input state
        """
    def SetLocalCoordInput(self, bLocalCoordInput: bool):
        """Set the local coordinate input state

        Args:
            bLocalCoordInput: Only local coordinate input: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, identMode: eIdentificationMode,
                 drawPointSymbol: eDrawElementIdentPointSymbols = eDrawElementIdentPointSymbols.eDRAW_IDENT_ELEMENT_POINT_SYMBOL_YES):
        """Constructor, sets the local coordinate input to false

        Args:
            identMode:       Identification mode
            drawPointSymbol: Draw the identification point symbol at the element (if an element is selected): true/false
        """
    @typing.overload
    def __init__(self, identMode: eIdentificationMode, bLocalCoordInput: bool):
        """Constructor, sets the local coordinate input

        Args:
            identMode:        Identification mode
            bLocalCoordInput: Only local coordinate input: true/false
        """
    @typing.overload
    def __init__(self, element: CoordinateInputMode):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class CoordinateInputResult():
    """Data class containing result of a successful point input
    """
    def GetIdentPntType(self) -> object:
        """Get the type of the identification point

        Returns:
            Type of the identification point
        """
    def GetPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the 3D point identified during a point input in world coordinates

        Returns:
            Identified point
        """
    def IsIdentElement(self) -> bool:
        """Check for element identification

        Returns:
            Identification of an element
        """
    def IsIdentPntType(self) -> bool:
        """Check for existing identification point

        Returns:
            Identification exists: true/false
        """
    def IsIdentPoinIntersectionPoint(self) -> bool:
        """Check for intersection identification point

        Returns:
            Identification point is an intersection point
        """
    def IsIdentPointArcIntersection(self) -> bool:
        """Check for a arc intersection identification point

        Returns:
            Identification point is an arc intersection point
        """
    def IsIdentPointCenter(self) -> bool:
        """Check for center identification point

        Returns:
            Identification point is center point
        """
    def IsIdentPointCenterElement(self) -> bool:
        """Check for center element identification point

        Returns:
            Identification point is center element point
        """
    def IsIdentPointDivision(self) -> bool:
        """Check for a division identification point

        Returns:
            Identification point is a division point
        """
    def IsIdentPointDockingPoint(self) -> bool:
        """Check for docking point

        Returns:
            Identification point is docking point: true/false
        """
    def IsIdentPointElement(self) -> bool:
        """Check for element identification point

        Returns:
            Identification point is element point
        """
    def IsIdentPointEndpoint(self) -> bool:
        """Check for end point

        Returns:
            Identification point is end point: true/false
        """
    def IsIdentPointOffset(self) -> bool:
        """Check for offset identification point

        Returns:
            Identification point is offset point: true/false
        """
    def IsIdentPointOrthogonal(self) -> bool:
        """Check for orthogonal identification point

        Returns:
            Identification point is an orthogonal point
        """
    def IsIdentPointPerpendicular(self) -> bool:
        """Check for perpendicular identification point

        Returns:
            Identification point is an perpendicular point
        """
    def IsIdentPointQuadrantPoint(self) -> bool:
        """Check for quadrant identification point

        Returns:
            Identification point is quadrant point of a circle: true/false
        """
    def IsIdentPointTrackElement(self) -> bool:
        """Check, whether the identification point is a track element point

        Returns:
            Identification point is a track element point: true/false
        """
    def IsIdentPointTrackElementFree(self) -> bool:
        """Check, whether the identification point is a free track element point

        Returns:
            Identification point is a track element point: true/false
        """
    def IsIdentPointTrackHelpElement(self) -> bool:
        """Check, whether the identification point is a track element or help element point

        Returns:
            Identification point is a track element or help element point: true/false
        """
    def IsIdentPointTrackIntersection(self) -> bool:
        """Check, whether the identification point is a track intersection point

        Returns:
            Identification point is a track intersection point: true/false
        """
    def IsIdentPointTrackParallel(self) -> bool:
        """Check, whether the identification point is a track parallel point

        Returns:
            Identification point is a track parallel point: true/false
        """
    def IsInputPointError(self) -> bool:
        """Get the error state of the input point

        In some cases the input point must fulfill a rule, e.g. must be
        a point at a wall in case of mode IDENT_ARCH_ELEMENTPOINT mode.
        To check this and continue the input in this case, this member can be used.

        Returns:
            The input point is not correct: true/false
        """
    def __eq__(self, pntType: CoordinateInputResult) -> bool:
        """Assign operator

        Args:
            pntType: Point type to compare

        Returns:
            New value
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, inputPnt: NemAll_Python_Geometry.Point3D, pntType: object):
        """Constructor

        Args:
            inputPnt: Input point
            pntType:  Identification point type
        """
    @typing.overload
    def __init__(self, inputPnt: NemAll_Python_Geometry.Point3D, pntType: object, bError: bool):
        """Constructor

        Args:
            inputPnt: Input point
            pntType:  Type of the identification point
            bError:   The input point is not correct: true/false
        """
    @typing.overload
    def __init__(self, element: CoordinateInputResult):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, pntType: CoordinateInputResult) -> bool:
        """Assign operator

        Args:
            pntType: Point type to assign

        Returns:
            New value
        """

class DockingPoint():
    """Implementation of the docking point wrapper
    """
    def FromString(self, dockingPointStr: str):
        """Create the docking point from a string

        Args:
            dockingPointStr: Docking point string
        """
    def GetDockedElements(self) -> NemAll_Python_Utility.VecGUIDList:
        """Get the docked elements

        Returns:
            Docked elements
        """
    def GetPoint(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> NemAll_Python_Geometry.Point3D:
        """Get the docking point

        Args:
            doc: Document

        Returns:
            Docking point
        """
    def IsValid(self) -> bool:
        """Test for valid docking point

        Returns:
            Valid state
        """
    def ToString(self) -> str:
        """Convert the docking point to a string

        Returns:
            Docking point string
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: DockingPoint):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class ElementHandleType():
    """Element handle type
    """
    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """
    HANDLE_ARROW: ElementHandleType
    """
    Arrow handle

    """
    HANDLE_CIRCLE: ElementHandleType
    """
    Circle handle

    """
    HANDLE_SQUARE_BLUE: ElementHandleType
    """
    Filled square handle with blue color

    """
    HANDLE_SQUARE_EMPTY: ElementHandleType
    """
    Empty square handle

    """
    HANDLE_SQUARE_RED: ElementHandleType
    """
    Filled square handle with red color

    """
    HANDLE_SQUARE_RIGHT: ElementHandleType
    """
    Halve-filled square handle

    """

class ElementSelect():
    """Implementation of the ElementSelect wrapper
    """
    def InitSelection(self, text: InputStringConvert):
        """Initialize the selection

        Args:
            text: Input text
        """
    def IsMouseMove(self, mouseMsg: int) -> bool:
        """Check for mouse move

        Args:
            mouseMsg: Mouse message

        Returns:
            Message is a mouse move: true/false
        """
    def __init__(self):
        """Initialize
        """

class ElementSelectFilterSetting():
    """Class containing settings for filtering elements during element selection, such as:

    -   which layer to consider (active, passive, both)
    -   which document to consider (active, passive, both)
    -   query for specific element types

    """
    def Clear(self):
        """Reset the settings
        """
    def GetLayerSelectType(self) -> eLayerSnoopType:
        """Get the layer selection type

        Returns:
            Return the layer selection type
        """
    @staticmethod
    def IsBaseClassType(typeID: NemAll_Python_IFW_ElementAdapter.GUID) -> bool:
        """Check, whether the element type is a base class type

        Args:
            typeID: Element type ID

        Returns:
            Element type is a base class type: true/false
        """
    def IsClear(self) -> bool:
        """Get the clear state

        Returns:
            true, if the members contain default values
        """
    def IsPointSelect(self) -> bool:
        """Get the point select state

        Returns:
            Point selection is active: true/false
        """
    def IsSelectPassiveInfoElement(self) -> bool:
        """Get the selection state of a passive info element

        Returns:
            Allow to select passive info element if no active element was found: true/false
        """
    def SelectPassiveInfoElement(self):
        """Allow to select passive info element if no active element was found
        """
    def SetArchitectureFilterQuery(self, positive: bool = True):
        """Set a prefabricated filter for all architecture elements

        Args:
            positive: if the filter will true for architecture elements otherwise the filter will be false for architecture elements
        """
    def SetAssoFilterQuery(self, positive: bool = True):
        """Set a prefabricated filter for all associative view elements

        Args:
            positive: if the filter will true for associative view elements otherwise the filter will be false for associative view elements
        """
    def SetDocumentLayerFilter(self, bSnoopAllElements: bool):
        """Set the document and layer filter

        Args:
            bSnoopAllElements: Snoop all elements: true/false
        """
    def SetDocumentSelectType(self, documentSnoopType: eDocumentSnoopType):
        """Set the selection mode for the document (active, passive or all documents)

        Args:
            documentSnoopType: Selection mode for the document (active, passive or all documents)
        """
    def SetLayerSelectType(self, layerSnoopType: eLayerSnoopType):
        """Set the layer selection type

        Args:
            layerSnoopType: Type of the allowed layers for the selection
        """
    def SetPointSelect(self):
        """Set the point select state
        """
    @typing.overload
    def __init__(self):
        """Construct the filter with default settings:

        -   filter only active layers (eSnoopActiveLayers)
        -   filter only active documents (eSnoopActiveDocuments)
        -   query is empty (all elements can be selected)
        """
    @typing.overload
    def __init__(self, bSnoopAllElements: bool):
        """Construct the filter with an empty element type query (all type of elements can be selected)

        Args:
            bSnoopAllElements:  True will consider elements on both active and passive layers and 
                                documents. False will consider elements on active layers and documents only
        """
    @typing.overload
    def __init__(self, filter: SelectionQuery, bSnoopAllElements: bool):
        """Construct the filter with a custom element type query

        Args:
            filter:             Query for specific elements to search for
            bSnoopAllElements:  True will consider elements on both active and passive layers and 
                                documents. False will consider elements on active layers and documents only
        """
    @typing.overload
    def __init__(self, filter: SelectionQuery, documentSnoopType: eDocumentSnoopType = eDocumentSnoopType.eSnoopActiveDocuments,
                 layerSnoopType: eLayerSnoopType = eLayerSnoopType.eSnoopActiveLayers):
        """Constructor

        default value for eObjectSelectType == SEL_ALL

        Args:
            filter:            Filter for the type of the object to search for
            documentSnoopType: Selection mode for the document (active, passive or all documents)
            layerSnoopType:    Selection mode for the layer (active, passive or all layers)
        """
    @typing.overload
    def __init__(self, selectSetting: ElementSelectFilterSetting):
        """Copy Constructor

        Args:
            selectSetting:  Filter settings to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def LayerSelectType(self) -> eLayerSnoopType:
        """Get the layer selection type
        """
    @LayerSelectType.setter
    def LayerSelectType(self, layerSnoopType: eLayerSnoopType) -> None:
        """Set the layer selection type

        Args:
            layerSnoopType: Type of the allowed layers for the selection
        """

class HandleService():
    """Implementation of the handle service
    """
    def AddHandles(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, handlePropList: object,
                   insertionMat: NemAll_Python_Geometry.Matrix3D, assoRefObj: object):
        """Add the handles

        Args:
            doc:            Document
            handlePropList: Handle properties list
            insertionMat:   Transformation matrix
            assoRefObj:     Reference element for the drawing inside the associative views
        """
    def DeleteToolTipText(self):
        """Delete the tool tip text
        """
    def DrawHandles(self):
        """Draw the handles
        """
    def RemoveHandles(self):
        """Remove the handles
        """
    def SelectHandle(self, pnt: NemAll_Python_Geometry.Point2D, viewProj: ViewWorldProjection,
                     eleAdapterTypeUUID: NemAll_Python_IFW_ElementAdapter.GUID = 00000000-0000-0000-0000-000000000000) -> tuple[int, NemAll_Python_Geometry.Matrix3D]:
        """Select a handle

        Args:
            pnt:                Cursor point
            viewProj:           View world projection
            eleAdapterTypeUUID: UUID of the handle elements

        Returns:
            Handle index (-1 = no selection) , associative view to world matrix
        """
    def ShowToolTipText(self, text: str):
        """Show the tool tip text

        Args:
            text: Text
        """
    def __init__(self):
        """Initialize
        """

class HighlightService():

    @staticmethod
    def CancelAllHighlightedElements(documentID: int):
        """Cancel the highlight of all elements

        Args:
            documentID: document ID
        """
    @staticmethod
    def HighlightElements(eleList: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList):
        """Highlight the elements

        Args:
            eleList: Element list as BaseElementAdapterList
        """

class InputFunctionStarter():

    """Utility with methods to start and terminate **multiple element selection** (selection with a rectangle)
    """
    @staticmethod
    def RemoveFunction():
        """Remove the current input function from the input function stack. This method can be called only, if there is a selection function in the input function stack (started by calling e.g. StartElementSelect)"""
    @staticmethod
    def StartElementSelect(text: str, selectSetting: ElementSelectFilterSetting, postSel: PostElementSelection, markSelectedElements: bool,
                           selectionMode: SelectionMode = SelectionMode.eSelectGeometry):
        """Start the multiple element selection. In this mode elements can be selected in the viewport by
        a selection rectangle or polygonal fence. The user can also point out individual elements
        by activating a _bracket_ (right-click before and after selection)

        The element selection overloads the process_mouse_msg, which means that this event is not called
        until the selection is completed. This is the case, when at least one of the following applies:

        -   one or more elements were selected
        -   selection rectangle was drawn in the viewport (regardless if any elements were selected)

        After that, the result is saved in the PostElementSelection object and the function is removed
        from the function stack.

        **IMPORTANT**: There can only be one selection function in the input function stack! If the running
        element selection must be restarted, call RemoveFunction first!

        Args:
            text:                 Prompt message shown to the user in the Allplan dialog line
            selectSetting:        Filter setting
            postSel:              Object to store the result of the selection. The result will be saved
                                  after a successful selection (see cases above)
            markSelectedElements: Whether to mark the selected elements
            selectionMode:        Selection mode
        """

class InputStringConvert():

    """Representation of the **prompt** shown in Allplan UI in the so called _dialog line_ during an input (selection or point input)
    """
    def GetString(self) -> str:
        """Get the input string

        Returns:
             Input string
        """
    @typing.overload
    def __init__(self, id: int):
        """Construct the prompt from an ID pointing out to a built-in string

        Args:
            arg2:   ID of the build-in prompt
        """
    @typing.overload
    def __init__(self, text: str):
        """Construct the prompt from any string

        Args:
            arg2:   Prompt to show in the dialog line
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class InputViewData():

    def __init__(self):
        """Initialize
        """

class CoordinateInput(InputViewDocumentData):
    """Base class implementation of the coordinate input

    The CoordinateInput class is the base class for input classes
    which need access to coordinate input.

    Each coordinate input has to be start with a call to a InitxxxInput(...) member
    function. This call initializes the coordinate input mode and shows the
    coordinate input dialog.

    To get the current input point of a mouse position, the GetInputPoint(...)
    member has to be called. This call returns the resulting world point of
    the mouse position (free point, identification point, distance point to
    the start or identification point, ...)

    Inside a member, where no mouse message is available, the current input
    point can be get by a call to GetCurrentPoint(...).
    """
    def AddGeometryFromPreviewElements(self, elements: list):
        """Add the geometry elements from the preview elements for the point and element search

        Args:
            elements:  Geometry elements
        """
    def AllowSelectGeometryElement(self, bSelectGeoElement: bool):
        """Allow to select an element

        Args:
            bSelectGeoElement: Select geometry element allowed: true/false
        """
    def CancelHighlightGeoElement(self):
        """Cancel geometry element highlight
        """
    def CancelInput(self):
        """Explicit cancel of the input function
        """
    def EnableChangeXYFocus(self, bChangeXYFocus: bool):
        """Enable the change of the x/y-focus after each input

        Args:
            bChangeXYFocus: if true, the xy focus will be changed
        """
    def EnableCoordinateInput(self, bEnable: bool):
        """Enable / disable the coordinate input

        This function can be used to enable or disable the coordinate input.

         - disable: the coordinate input dialog is removed from the input toolbar
         - enable:  the coordinate input dialog is shown in the input toolbar

        Args:
            bEnable: Enable the coordinate input: true/false
        """
    def EnableUndoStep(self, bEnableUndoStep: bool):
        """Enable disable the undo step

        Args:
            bEnableUndoStep: Enable the undo step: true/false
        """
    def EnableZCoord(self, bEnable: bool):
        """Enable the z-coordinate inside the coordinate dialog

        Args:
            bEnable: Z coordinate inside the coordinate dialog is enabled: true/false
        """
    def GetAssocViewFromPoint(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D,
                              pMsgInfo: AddMsgInfo) -> NemAll_Python_IFW_ElementAdapter.AssocViewElementAdapter:
        """Get the associative view from the point

        Args:
            mouseMsg: Mouse message WM_xxx
            pnt:      Cursor point (view coordinate)
            pMsgInfo: Additional message info

        Returns:
            Standard return
        """
    @typing.overload
    def GetCurrentPoint(self) -> CoordinateInputResult:
        """Get and mark the current input point

        Returns:
            Current input point
        """
    @typing.overload
    def GetCurrentPoint(self, startPnt: NemAll_Python_Geometry.Point3D) -> CoordinateInputResult:
        """Get and mark the current input point

        Args:
            startPnt: Starting point End point input is possible by a distance input to the start point

        Returns:
            Current input point
        """
    @typing.overload
    def GetCurrentPoint(self, startPnt: NemAll_Python_Geometry.Point3D, bStartPnt: bool) -> CoordinateInputResult:
        """Get and mark the current input point

        Args:
            startPnt:  Starting point
            bStartPnt: Starting point is active End point input is possible by a distance input to the start point

        Returns:
            Current input point
        """
    @typing.overload
    def GetCurrentPoint(self, bStartPnt: bool) -> CoordinateInputResult:
        """Get and mark the current input point

        Args:
            bStartPnt: Starting point is active true/false.
                       End point input is possible by a distance input to the input point
                       of the last input step

        Returns:
            Current input point
        """
    def GetCurrentPoint(self) -> CoordinateInputResult:
        """ Overloaded function. See individual overloads.
        """
    def GetInputAssocView(self) -> NemAll_Python_IFW_ElementAdapter.AssocViewElementAdapter:
        """Get the associative view of the input point / element

        The function can be used after a call to GetInputPoint,
        SelectGeometryElement, SelectElement, ...

        Returns:
            Associative view of the input point / element, NULL if point is outside
        """
    def GetInputControlIntValue(self) -> int:
        """Get the integer value from the value input control

        Returns:
            Integer value from the value input control
        """
    def GetInputControlText(self) -> object:
        """Get the text from the text input control

        Returns:
            Text from the text input control
        """
    def GetInputControlValue(self) -> float:
        """Get the double value from the value input control

        Returns:
            Double value from the value input control
        """
    def GetInputDockingPoint(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo) -> DockingPoint:
        """Get the current input point

        Args:
            mouseMsg:  Mouse message WM_xxx
            pnt:       Cursor point (view coordinate)
            pMsgInfo:  Additional message info
            startPnt:  Starting point
            bStartPnt: Starting point is active
                       End point input is possible by a distance input to the start point

        Returns:
            Current input point result
        """
    @typing.overload
    def GetInputPoint(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo) -> CoordinateInputResult:
        """Perform a point identification inside the viewport

        Args:
            mouseMsg:  Mouse message
            pnt:       Cursor point (view coordinate)
            pMsgInfo:  Additional message info

        Returns:
            Result of the point identification
        """
    @typing.overload
    def GetInputPoint(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo,
                      bStartPnt: bool) -> CoordinateInputResult:
        """Get the current input point

        Args:
            mouseMsg:  Mouse message WM_xxx
            pnt:       Cursor point (view coordinate)
            pMsgInfo:  Additional message info
            bStartPnt: Starting point is active
                       End point input is possible by a distance input to the input point
                       of the last input step

        Returns:
            Current input point result
        """
    @typing.overload
    def GetInputPoint(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo,
                      startPnt: NemAll_Python_Geometry.Point3D, bStartPnt: bool) -> CoordinateInputResult:
        """Get the current input point

        Args:
            mouseMsg:  Mouse message WM_xxx
            pnt:       Cursor point (view coordinate)
            pMsgInfo:  Additional message info
            startPnt:  Starting point
            bStartPnt: Starting point is active
                       End point input is possible by a distance input to the start point

        Returns:
            Current input point result
        """
    def GetInputPoint(self) -> CoordinateInputResult:
        """ Overloaded function. See individual overloads.
        """
    def GetReferenceLine(self) -> NemAll_Python_Geometry.Line2D:
        """Get the reference line, on which the identified point is located.

        This method works when eIdentificationMode is set to eIDENT_ARCH...
        and only with on architectural elements

        Returns:
            Reference line
        """
    def GetSelectedElement(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Get the selected element

        The function can be used in case of eIdentMode = MODE_TEXTPOINT,
        SelectGeometryElement, SelectElement, ...

        Returns:
            Selected element
        """
    def GetSelectedElementAssocView(self) -> NemAll_Python_IFW_ElementAdapter.AssocViewElementAdapter:
        """Get the related associative view of the selected element

        Returns:
            Related associative view of the selected element
        """
    def GetSelectedElements(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Get the selected elements

        The function can be used in case of eIdentMode = MODE_TEXTPOINT,
        SelectGeometryElement, SelectElement, ...

        Returns:
            Vector of elements with the same distance to the cursor
        """
    def GetSelectedGeometryElement(self) -> typing.Any:
        """Get the selected geometry element

        Returns:
            IGeometry element of the selected geometry element (0 = no selection)
        """
    def GetSelectedGeometryElements(self) -> list[typing.Any]:
        """Get the selected geometry element

        Returns:
            IGeometry elements of the selected geometry elements (with the same distance)
        """
    def InitFirstElementInput(self, text: InputStringConvert, identMode: CoordinateInputMode = CoordinateInputMode()):
        """Initialize the input for an **element selection** (point, line, ...) as free point input:

        -   only a short prompt is shown in the dialog line
        -   the input is allowed in each of the currently opened documents

        Args:
            text:       Prompt shown in the dialog line
            identMode:  Identification mode
      
        """
    def InitFirstElementValueInput(self, text: InputStringConvert, ctrlData: ValueInputControlData,
                                   identMode: CoordinateInputMode = CoordinateInputMode()):
        """Initialize the input for an **element selection** (point, line, ...) as free point input:

        -   beside the prompt, also an input control is shown in the dialog line
        -   the input is allowed in each of the currently opened documents

        Args:
            text:       Prompt shown in the dialog line
            ctrlData:   Settings of the input control
            identMode:  Identification mode
      
        """
    def InitFirstPointInput(self, text: InputStringConvert, identMode: CoordinateInputMode = CoordinateInputMode(),
                            inputViewData: InputViewData = InputViewData()):
        """Initialize the input of a **point**:

        -   the prompt and standard coordinate input controls are shown in the dialog line
        -   the input is allowed in each of the currently opened documents

        Args:
            text:           Prompt shown in the dialog line
            identMode:      Identification mode
            inputViewData:  Input view data
      
        """
    def InitFirstPointValueInput(self, text: InputStringConvert, ctrlData: ValueInputControlData,
                                 identMode: CoordinateInputMode = CoordinateInputMode(), inputViewData: InputViewData = InputViewData()):
        """Initialize the input of a **point**:

        -   additionally to the prompt and standard coordinate input controls, also
            an extra input control is shown in the dialog line
        -   the input is allowed in each of the currently opened documents

        Args:
            text:       Prompt shown in the dialog line
            ctrlData:   Settings of the additional input control
            identMode:  Identification mode
      
        """
    def InitNextElementInput(self, text: InputStringConvert, identMode: CoordinateInputMode = CoordinateInputMode()):
        """Initialize the input for an **element selection** (point, line, ...) as free point input.

        -   only a short prompt is shown in the dialog line
        -   the input is allowed only in the document, where the first input was done

        Remarks:
            Initialize this input after the input started with InitFirst...Input is completed

        Args:
            text:       Prompt shown in the dialog line
            identMode:  Identification mode
      
        """
    def InitNextElementValueInput(self, text: InputStringConvert, ctrlData: ValueInputControlData,
                                  identMode: CoordinateInputMode = CoordinateInputMode()):
        """Initialize the input for an **element selection** (point, line, ...) as free point input:

        -   beside the prompt, also an input control is shown in the dialog line
        -   the input is allowed only in the document, where the first input was done

        Remarks:
            Initialize this input after the input started with InitFirst...Input is completed

        Args:
            text:       Prompt shown in the dialog line
            ctrlData:   Settings of the input control
            identMode:  Identification mode
      
        """
    def InitNextPointInput(self, text: InputStringConvert, identMode: CoordinateInputMode = CoordinateInputMode()):
        """Initialize the input of a **point**:

        -   the prompt and standard coordinate input controls are shown in the dialog line
        -   the input is allowed only in the document, where the first input was done

        Remarks:
            Initialize this input after the input started with InitFirst...Input is completed

        Args:
            text:           Prompt shown in the dialog line
            identMode:      Identification mode
      
        """
    def InitNextPointValueInput(self, text: InputStringConvert, ctrlData: ValueInputControlData,
                                identMode: CoordinateInputMode = CoordinateInputMode()):
        """Initialize the input of a **point**:

        -   additionally to the prompt and standard coordinate input controls, also
            an extra input control is shown in the dialog line
        -   the input is allowed only in the document, where the first input was done

        Remarks:
            Initialize this input after the input started with InitFirst...Input is completed

        Args:
            text:       Prompt shown in the dialog line
            ctrlData:   Settings of the additional input control
            identMode:  Identification mode
      
        """
    def InitValueInput(self, text: InputStringConvert, ctrlData: ValueInputControlData):
        """Initialize the value input

        -   the prompt and an input control is shown in the dialog line
        -   no point input or element selection is allowed in any of the currently opened documents

        Remarks:
          Initialize this input after the input started with InitFirst...Input is completed


        Args:
            text:       Prompt shown in the dialog line
            ctrlData:   Settings of the additional input control
        """
    def IsCoordinateInputEnabled(self) -> bool:
        """Check, whether the input controls are active (enabled)

        Returns:
            Coordinate input is active: true/false
        """
    def IsEmptyValueInputControl(self) -> bool:
        """Check, whether there is no input inside the input control

        Returns:
            Input control is empty: true/false
        """
    def IsIdentElementAllowed(self, bAllowCenter: bool) -> bool:
        """Check, whether the result of the point identification allows an element identification

        Args:
            bAllowCenter: Allow element identification by center point

        Returns:
            Element identification allowed: true false
        """
    def IsIdentModeOriginal(self) -> bool:
        """Check, whether the current identification mode is the original mode

        Returns:
            Current identification mode is the original mode
        """
    def IsIdentModePointWallPoint(self) -> bool:
        """Check, whether the identification mode is point and wall point

        Returns:
            Identification mode is point and wall point: true false
        """
    def IsIdentModeWallPoint(self) -> bool:
        """Check, whether the identification mode is wall point

        Returns:
            Identification mode is wall point: true false
        """
    def IsIdentPoint(self) -> bool:
        """Get the identification state of the current point

        Returns:
            Identification point: true false
        """
    def IsMouseLeave(self) -> bool:
        """Check, whether the mouse is outside the view

        Returns:
            Mouse is outside the view: true/false
        """
    def IsMouseMove(self, mouseMsg: int) -> bool:
        """Check on mouse move

        Args:
            mouseMsg: Mouse message WM_xxx

        Returns:
            Mouse move: true false
        """
    def IsSelectedGeometryElement(self) -> bool:
        """Get the state of the selected geometry element

        Returns:
            Geometry element is selected: true/false
        """
    @typing.overload
    def IsValueInputControl(self, id: int) -> bool:
        """Check, whether the ID belongs to the value input control (from the coordinate input dialog)

        Args:
            id: ID to check

        Returns:
            ID belongs to the value input control (from the coordinate input dialog): true/false
        """
    @typing.overload
    def IsValueInputControl(self) -> bool:
        """Check, whether a value input control exists

        Returns:
            A value input control exists: true/false
        """
    def IsValueInputControl(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    def IsValueInputControlInput(self, bIdentPoint: bool) -> bool:
        """Check, whether an input inside the value input control is done
        and the value should be used

        Args:
            bIdentPoint: Identification point has higher priority: true/false

        Returns:
            Check, whether the input value inside the added control
        """
    def ProcessMouseMsg(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo) -> object:
        """Process a mouse message

        Args:
            mouseMsg: Mouse message WM_xxx
            pnt:      Cursor point (view coordinate)
            pMsgInfo: Additional message info

        Returns:
            Standard return
        """
    @typing.overload
    def SelectElement(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo, bHighlight: bool, bSelAlways: bool,
                      bAllowCenter: bool) -> bool:
        """Select an element if no identification point exists. Use the filter set by

        SetElementFilter

        Args:
            mouseMsg:     Mouse message WM_xxx
            pnt:          Cursor point (view coordinate)
            pMsgInfo:     Additional message info
            bHighlight:   Highlight the selected element
            bSelAlways:   true:  Select always
            bAllowCenter: Allow element identification by center point

        Returns:
            Element is selected: true false
        """
    @typing.overload
    def SelectElement(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo, bHighlight: bool, bSelAlways: bool,
                      bAllowCenter: bool, selectSetting: ElementSelectFilterSetting) -> bool:
        """Select an element if no identification point exists. Use the filter set by

        SetElementFilter

        Args:
            mouseMsg:      Mouse message WM_xxx
            pnt:           Cursor point (view coordinate)
            pMsgInfo:      Additional message info
            bHighlight:    Highlight the selected element
            bSelAlways:    true:  Select always
            bAllowCenter:  Allow element identification by center point
            selectSetting: Element selection filter

        Returns:
            Element is selected: true false
        """
    def SelectElement(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
        """Perform element search 

        Uses the filter set by the _SetElementFilter_

        Args:
            mouseMsg:       Mouse message
            pnt:            Cursor point (view coordinate)
            pMsgInfo:       Additional message info
            bHighlight:     Highlight the selected element
            bSelAlways:     Relevant when used in combination with _GetInputPoint_ method. When set to False, the element search is
                            terminated after the method _GetInputPoint_ found a start/end/mid point of an element. When set to True,
                            the element search will be performed anyway.
            bAllowCenter:   Relevant when used in combination with _GetInputPoint_ method. When bSelAlways is set to False and this
                            option to True, the element search is performed after the method _GetInputPoint_ found a mid point.
                            When bSelAlways is set to True, this option becomes irrelevant.

        Returns:
            True, when element is selected. False otherwise
        """
    def SelectGeometryElement(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo,
                              bHighlightCompleteElement: bool = False) -> bool:
        """Select a base geometry element.  Use the filter set by
        SetGeometryElementFilter and SetGeometryFilter

        Args:
            mouseMsg:                  Mouse message WM_xxx
            pnt:                       Cursor point (view coordinate)
            pMsgInfo:                  Additional message info
            bHighlightCompleteElement: true = highlight the complete element, false = highlight only the selected geometry part

        Returns:
            Element was found: true false
        """
    def SelectPolyhedronFace(self, arg2: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, arg3: NemAll_Python_Geometry.Point2D,
                             arg4: bool) -> tuple:
        """.. deprecated:: since Allplan 2023-1-0
           use FaceSelectService::SelectPolyhedronFace
        """
    def SelectWallFace(self, arg2: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, arg3: NemAll_Python_Geometry.Point2D,
                       arg4: bool) -> tuple:
        """.. deprecated:: since Allplan 2023-1-0
           use FaceSelectService::SelectWallFace
        """
    def SelectWallFaceInUVS(self, arg2: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, arg3: NemAll_Python_Geometry.Point2D,
                            arg4: bool) -> tuple:
        """.. deprecated:: since Allplan 2023-1-0
           use FaceSelectService::SelectWallFaceInUVS
        """
    def SetAbscissaElement(self, abscissa: object, abscissaAssoMat: NemAll_Python_Geometry.Matrix3D):
        """Set the abscissa element

        Args:
            abscissa:        Abscissa
            abscissaAssoMat: Abscissa matrix of the associative view
        """
    def SetElementFilter(self, selectSetting: ElementSelectFilterSetting):
        """Set the element selection filter

        Args:
            selectSetting: Element selection filter
        """
    def SetGeometryElementFilter(self, selectSetting: ElementSelectFilterSetting):
        """Set the geometry element selection filter

        Args:
            selectSetting: Geometry element selection filter
        """
    def SetGeometryFilter(self, geoFilter: SnoopElementGeometryFilter):
        """Set the geometry filter used for geometry search during **point input**
        (initialized with InitFirstPointInput or InitNextPointInput).

        This filter is used, when the identification mode (eIdentificationMode) is set to
        identify points **and** geometry elements, i.e. to eIDENT_POINT_ELEMENT...

        Args:
            selectSetting:  Geometry element selection filter
        """
    def SetInputPlane(self, plane: NemAll_Python_Geometry.Plane3D):
        """Set the input plane.

        The input point will be projected onto this plane along the plane's normal vector.

        Args:
            plane:  Input plane
        """
    def SetInputText(self, text: InputStringConvert):
        """Set the input text

        Args:
            text: Request string as resource ID, str
        """
    def SetInputTextPrefix(self, iDPrefix: int):
        """Set the input text prefix

        Args:
            iDPrefix: ID of the prefix text
        """
    def SetProjectionBase0(self, setProjectionBase0: bool):
        """Set the projection base to 0 during **point input** in floor plan view or side view

        When this option is set to True, then if a point is found and snapped during the input
        inside a **floor plan view** or a **side view** (front, rear, left or right),
        the resulting point will be projected on:

        -   the XY plane in case of floor plan view
        -   the XZ plane in case of front or rear view
        -   the YZ plane in case of left ir right view

        When this option is set to False, then the resulting point is not projected onto
        those planes. Instead it is being snapped to the first visible point from the observer's
        perspective.

        Default value is: False

        Args:
            setProjectionBase0: True, to set the projection base to 0
        """
    def StartHandleModification(self):
        """Start the handle modification
        """
    def StartScriptObjectInteractor(self):
        """Start the script object interactor
        """
    def StopHandleModification(self):
        """Stop the handle modification
        """
    def StopScriptObjectInteractor(self):
        """Stop the script object interactor
        """
    def __init__(self, bZCoord: bool = True):
        """Constructor

        Args:
            bZCoord: Z coordinate input is active: true/false
        """

class LocalCoordinateSystemFlags(enum.Enum):
    """eStandard: standard coordinate system symbol
    eSmall   : small coordinate system symbol
    eHoverX  : the x arrow will be black
    eHoverY  : the y arrow will be black
    eHoverZ  : the z arrow will be black
    """
    eHoverX = 2
    eHoverY = 4
    eHoverZ = 8
    eSmall = 1
    eStandard = 0

    names = {eStandard: eStandard,
             eSmall: eSmall,
             eHoverX: eHoverX,
             eHoverY: eHoverY,
             eHoverZ: eHoverZ}

    values = {0: eStandard,
              1: eSmall,
              2: eHoverX,
              4: eHoverY,
              8: eHoverZ}

    def __getitem__(self, key: (str | int | float)) -> LocalCoordinateSystemFlags:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PolygonInput(CoordinateInput, InputViewDocumentData):
    """Implementation of the polygon input
    """
    def ExecuteInput(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo) -> int:
        """Execute the input

        Args:
            mouseMsg: Mouse message
            pnt:      View input point
            pMsgInfo: Additional message info

        Returns:
            execution state
        """
    def GetPolygon(self) -> NemAll_Python_Geometry.Polygon3D:
        """get the final polygon

        Returns:
            final polygon
        """
    def GetPreviewPolygon(self) -> NemAll_Python_Geometry.Polygon3D:
        """get the preview polygon

        Returns:
            preview polygon
        """
    def StartNewInput(self):
        """Start new input
        """
    def __init__(self, coordInput: CoordinateInput, bZCoord: bool, multiPolygon: bool):
        """Default constructor

        After constructing the object, the polygon input toolbar is shown in the Allplan UI

        Args:
            coordInput:     Coordinate input object
            bZCoord:        True will show the Z-coordinate input control, False will hide it.
            multiPolygon:   True allows the user to input a polygon consisting of multiple components.
                            Also negative components (openings) are be allowed. False allows to enter
                            only one polygon component.
        """

class PolylineInput(CoordinateInput, InputViewDocumentData):
    """Implementation of the polyline input
    """
    def ExecuteInput(self, mouseMsg: int, pnt: NemAll_Python_Geometry.Point2D, pMsgInfo: AddMsgInfo) -> int:
        """Execute the input

        Args:
            mouseMsg: Mouse message
            pnt:      View input point
            pMsgInfo: Additional message info

        Returns:
            execution state
        """
    def GetPolyline(self) -> NemAll_Python_Geometry.Polyline3D:
        """get the final polyline

        Returns:
            final polyline
        """
    def GetPreviewPolyline(self) -> NemAll_Python_Geometry.Polyline3D:
        """get the preview polyline

        Returns:
            preview polyline
        """
    def StartNewInput(self):
        """Start new input
        """
    def __init__(self, coordInput: CoordinateInput, bZCoord: bool):
        """Default constructor

        After constructing the object, the line input toolbar is shown in the Allplan UI

        Args:
            coordInput:     Coordinate input object
            bZCoord:        True will show the Z-coordinate input control, False will hide it.
                            False will not prevent from input of a 3D polyline!
        """

class PostElementSelection():

    """Data class containing the result of an element selection started with the InputFunctionStarter
    """
    def GetSelectedElements(self,
                            doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Pop the elements out of the object and return them as a list with element adapters

        Args:
            doc:  Document

        Returns:
            Selected elements as element adapters
        """
    def __init__(self):
        """Initialize
        """

class PreviewSymbolBuilder():
    """Implementation of the preview symbol builder
    """
    @staticmethod
    @typing.overload
    def ArrowSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                    colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int, rotationAngle: float, allWindows: bool = True):
        """Create an arrow symbol

        Args:
            pnt:           Arrowhead point
            bDrawIso:      Draw the arrow symbol inside the isometric view: true/false
            viewProj:      View world projection data
            colorVariant:  Color of the preview
            widthVariant:  Width of the symbol
            rotationAngle: Rotation angle of the rectangle
            allWindows:    Show symbol in all windows
        """
    @staticmethod
    @typing.overload
    def ArrowSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                    colorVariant: NemAll_Python_BasisElements.ARGB, rotationAngle: float, allWindows: bool = True):
        """Create a small arrow symbol

        Args:
            pnt:           Arrowhead point
            bDrawIso:      Draw the arrow symbol inside the isometric view: true/false
            viewProj:      View world projection data
            colorVariant:  Color of the preview
            rotationAngle: Rotation angle of the rectangle
            allWindows:    Show symbol in all windows
        """
    @staticmethod
    def ArrowSymbol():
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def Circle3DSymbol(refPnt: NemAll_Python_Geometry.Point3D, circle: NemAll_Python_Geometry.Arc3D, viewProj: ViewWorldProjection,
                       colorVariant: NemAll_Python_BasisElements.ARGB, linePattern: int, lineWidth: float):
        """Create a 3D circle symbol preview

        Args:
            refPnt:       Reference point
            circle:       3D circle
            viewProj:     View world projection data
            colorVariant: Color of the preview
            linePattern:  Line pattern
            lineWidth:    Width of the line
        """
    @staticmethod
    def CircleSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                     colorVariant: NemAll_Python_BasisElements.ARGB, radius: int):
        """Create a circle symbol

        Args:
            pnt:          Center point
            bDrawIso:     Draw the circle symbol inside the isometric view: true/false
            viewProj:     View world projection data
            colorVariant: Color of the preview
            radius:       Radius of the circle in pixel
        """
    @staticmethod
    @typing.overload
    def CoordCrossSymbol(plane: NemAll_Python_Geometry.Plane3D, armLength: int, viewProj: ViewWorldProjection):
        """Draw the coordinate cross symbol

        Args:
            plane:     Plane
            armLength: Length of the symbol arms
            viewProj:  View world projection
        """
    @staticmethod
    @typing.overload
    def CoordCrossSymbol(axisPlacement: NemAll_Python_Geometry.AxisPlacement3D, armLength: int, viewProj: ViewWorldProjection):
        """Draw the coordinate cross symbol

        Args:
            axisPlacement: Axis placement
            armLength:     Length of the symbol arms
            viewProj:      View world projection
        """
    @staticmethod
    def CoordCrossSymbol():
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def CrossSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                    colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int):
        """Create a cross symbol

        Args:
            pnt:          Cross center point
            bDrawIso:     Draw the cross symbol inside the isometric view: true/false
            viewProj:     View world projection data
            colorVariant: Color of the preview
            widthVariant: Width of the symbol
        """
    @staticmethod
    def FilledRectangleSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                              colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int, rotationAngle: float):
        """Create a filled rectangle symbol

        Args:
            pnt:           Rectangle center point
            bDrawIso:      Draw the rectangle symbol inside the isometric view: true/false
            viewProj:      View world projection data
            colorVariant:  Color of the preview
            widthVariant:  Width of the symbol
            rotationAngle: Rotation angle of the rectangle
        """
    @staticmethod
    def Line3DSymbol(refPnt: NemAll_Python_Geometry.Point3D, line: NemAll_Python_Geometry.Line3D, viewProj: ViewWorldProjection,
                     colorVariant: NemAll_Python_BasisElements.ARGB, linePattern: int, lineWidth: int):
        """Create a 3D line symbol preview

        Args:
            refPnt:       Reference point
            line:         3D line
            viewProj:     View world projection data
            colorVariant: Color of the preview
            linePattern:  Line pattern
            lineWidth:    Line width
        """
    @staticmethod
    def LocalCoordinateSystem(coordSystemMatrix: NemAll_Python_Geometry.Matrix3D, flags: LocalCoordinateSystemFlags, maxSize: float):
        """Create a symbol for a local coordinate system

        Args:
            coordSystemMatrix: Matrix of the coordinate system
            flags:             Coordinate system flags
            maxSize:           Max size of the coordinate system
        """
    @staticmethod
    def MarkSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                   colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int):
        """Create a mark symbol (drawn an x)

        Args:
            pnt:          Mark center point
            bDrawIso:     Draw the mark symbol inside the isometric view: true/false
            viewProj:     View world projection data
            colorVariant: Color of the preview
            widthVariant: Width of the symbol
        """
    @staticmethod
    def OffsetPointSymbols(refPnt: NemAll_Python_Geometry.Point3D, offPnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool,
                           viewProj: ViewWorldProjection, colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int, refPntAngle: float, offPntAngle: float):
        """Create the symbols for an offset point

        Args:
            refPnt:       Reference point
            offPnt:       Offset point
            bDrawIso:     Draw the arrow symbol inside the isometric view: true/false
            viewProj:     View world projection data
            colorVariant: Color of the preview
            widthVariant: Width of the symbol
            refPntAngle:  Angle at the reference point
            offPntAngle:  Angle at the offset point
        """
    @staticmethod
    def OrthogonalSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                         colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int):
        """Create an orthogonal symbol

        Args:
            pnt:          Center point
            bDrawIso:     Draw the circle symbol inside the isometric view: true/false
            viewProj:     View world projection data
            colorVariant: Color of the preview
            widthVariant: Width of the symbol
        """
    @staticmethod
    def ParallelSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                       colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int):
        """Create a parallel symbol

        Args:
            pnt:          Center point
            bDrawIso:     Draw the circle symbol inside the isometric view: true/false
            viewProj:     View world projection data
            colorVariant: Color of the preview
            widthVariant: Width of the symbol
        """
    @staticmethod
    def Polyline2DSymbol(refPnt: NemAll_Python_Geometry.Point3D, polyline: NemAll_Python_Geometry.Polyline2D, viewProj: ViewWorldProjection,
                         colorVariant: NemAll_Python_BasisElements.ARGB, linePattern: int):
        """Create a 2D polyline symbol preview

        Args:
            refPnt:       Reference point
            polyline:     Polyline
            viewProj:     View world projection
            colorVariant: Color of the preview
            linePattern:  Line pattern
        """
    @staticmethod
    @typing.overload
    def Polyline3DSymbol(polyline: NemAll_Python_Geometry.Polyline3D, viewProj: ViewWorldProjection,
                         colorVariant: NemAll_Python_BasisElements.ARGB, linePattern: int):
        """Create a 3D polyline symbol preview

        Args:
            polyline:     3D Polyline
            viewProj:     View world projection data
            colorVariant: Color of the preview
            linePattern:  Line pattern
        """
    @staticmethod
    @typing.overload
    def Polyline3DSymbol(refPnt: NemAll_Python_Geometry.Point3D, polyline: NemAll_Python_Geometry.Polyline3D, viewProj: ViewWorldProjection,
                         colorVariant: NemAll_Python_BasisElements.ARGB, linePattern: int):
        """Create a 3D polyline symbol preview

        Args:
            refPnt:       Reference point
            polyline:     Polyline
            viewProj:     View world projection
            colorVariant: Color of the preview
            linePattern:  Line pattern
        """
    @staticmethod
    def Polyline3DSymbol():
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def TrackLine(line: NemAll_Python_Geometry.Line3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                  colorVariant: NemAll_Python_BasisElements.ARGB, trackLineType: eTrackLineType):
        """Create a track line

        Args:
            line:          Track line
            bDrawIso:      Draw the circle symbol inside the isometric view: true/false
            viewProj:      View world projection data
            colorVariant:  Color of the preview
            trackLineType: Type of the track line
        """
    @staticmethod
    def TrackMarkSymbol(pnt: NemAll_Python_Geometry.Point3D, bDrawIso: bool, viewProj: ViewWorldProjection,
                        colorVariant: NemAll_Python_BasisElements.ARGB, widthVariant: int):
        """Create a track mark symbol

        Args:
            pnt:          Center point
            bDrawIso:     Draw the circle symbol inside the isometric view: true/false
            viewProj:     View world projection data
            colorVariant: Color of the preview
            widthVariant: Width of the symbol
        """

class QueryTypeID():
    """Implementation of the element type ID query
    """
    def GetQueryText(self) -> str:
        """Get the query text

        Returns:
            Query text
        """
    def GetQueryTypeID(self) -> NemAll_Python_IFW_ElementAdapter.GUID:
        """Get the ID of the type query

        Returns:
            ID of the type query
        """
    def __call__(self, ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> bool:
        """Overloaded operator ()

        Args:
            ele: Element to check

        Returns:
            Type of the element is same as the filter type: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, typeID: NemAll_Python_IFW_ElementAdapter.GUID):
        """Constructor

        Args:
            typeID: Element type ID of the filter
        """
    @typing.overload
    def __init__(self, element: QueryTypeID):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """

class SelectElementsService():

    class eSelectCondition(enum.Enum):
        """Element selection condition
        """
        SELECT_ALL = 1
        SELECT_INSIDE = 0
        SELECT_INTERSECTED = 2

        names = {SELECT_INSIDE: SELECT_INSIDE,
                 SELECT_ALL: SELECT_ALL,
                 SELECT_INTERSECTED: SELECT_INTERSECTED}

        values = {0: SELECT_INSIDE,
                  1: SELECT_ALL,
                  2: SELECT_INTERSECTED}

        def __getitem__(self, key: (str | int | float)) -> SelectElementsService.eSelectCondition:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    @staticmethod
    def GetPreSelectedElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                               filter: SelectionQuery) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Get the pre selected elements
        Args:
            doc:            Document
            filter:         Selection filter

        Returns:
            Pre selected elements
        """
    @staticmethod
    def SelectByPolygon(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, polygon: NemAll_Python_Geometry.Polygon2D,
                        viewProjection: ViewWorldProjection, selCond: eSelectCondition, filter: SelectionQuery, isWorldPolygon: bool = False) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Select an element by a point

        Args:
            doc:            Document
            polygon:        surrounding search polygon (view coordinates)
            viewProjection: Identification of view projection (window)
            selCond:        True when elements inside rectangle must be selected only
            filter:         Selection filter
            isWorldPolygon: true=world polygon, false=view polygon

        Returns:
            Data of the selected elements
        """
    @staticmethod
    def SelectByRect(cursorLeftBottomPoint: NemAll_Python_Geometry.Point2D, cursorRightTopPoint: NemAll_Python_Geometry.Point2D,
                     viewProjection: ViewWorldProjection, selCond: eSelectCondition, filter: SelectionQuery) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Select an element by a point

        Args:
            cursorLeftBottomPoint: Coordinate of left bottom point where elements will be searching
            cursorRightTopPoint:   Coordinate of right top point where elements will be searching
            viewProjection:        Identification of view projection (window)
            selCond:               True when elements inside rectangle must be selected only
            filter:                Selection filter

        Returns:
            Data of the selected elements
        """
    SELECT_ALL = eSelectCondition.SELECT_ALL
    SELECT_INSIDE = eSelectCondition.SELECT_INSIDE
    SELECT_INTERSECTED = eSelectCondition.SELECT_INTERSECTED

class SelectionMode(enum.Enum):
    """Possible selection modes for multiple selection using InputFunctionStarter
    """
    eSelectGeometry = 0
    """Result of the selection is only the selected element"""
    eSelectObject = 1
    """Result of the selection is the selected element with all its related elements (e.g. wall tier together with axis, labels, attribute container, etc...) and all child elements (if existing)"""
    eSelectSubObject = 3
    """Result of the selection is the selected element with some related elements (e.g. wall tier with labels and attribute container)"""

    names = {eSelectGeometry: eSelectGeometry,
             eSelectObject: eSelectObject,
             eSelectSubObject: eSelectSubObject}

    values = {0: eSelectGeometry,
              1: eSelectObject,
              3: eSelectSubObject}

    def __getitem__(self, key: (str | int | float)) -> SelectionMode:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SelectionQuery():
    """Class containing checking procedures to obtain, whether an element is valid for being selected during element selection.
    """
    def Clear(self):
        """Clear the query
        """
    def IsEmpty(self) -> bool:
        """Check for an empty query

        Returns:
            Filter is empty: true/false
        """
    def __call__(self, arg2: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> bool:
        """
        """
    @typing.overload
    def __init__(self):
        """Construct empty query. All elements are considered valid for selection"""
    @typing.overload
    def __init__(self, query: SelectionQuery):
        """Copy constructor

        Args:
            query:  Query to copy
        """
    @typing.overload
    def __init__(self, query: (list[(NemAll_Python_IFW_Input.QueryTypeID | object)]  |  (NemAll_Python_IFW_Input.QueryTypeID | object))):
        """Default constructor

        Args:
            query:  Selection query as list with queries or single query.

        Examples:
            The query can be a list of QueryTypeID like this:
        
            >>> type_uuids = [AllplanIFW.QueryTypeID(AllplanElementAdapter.Beam_TypeUUID),
            ...               AllplanIFW.QueryTypeID(AllplanElementAdapter.Column_TypeUUID)]
            ... selection_query = AllplanIFW.SelectionQuery(type_uuids)

            or a class with a __call__ member, like this:

            >>> class CustomFilter():
            ...     def __call__(self, element: AllplanElementAdapter.BaseElementAdapter) -> bool:
            ...         return isinstance(element.GetModelGeometry(), AllplanGeometry.Polyhedron3D):
            ... selection_query = AllplanIFW.SelectionQuery([CustomFilter()])
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class SnoopElementGeometryFilter():

    def AddElements(self, elementNames: str):
        """Add elements to the filter

        Args:
            elementNames:   Element names, separated by ,
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, bFindBaseGeometry: bool, bFindAreaGeometry: bool, bPerpendicularOnElement: bool, bFindNonPassiveOnly: bool,
                 bSplitAreaGeometries: bool, bIdentifyEmbeddedElement: bool, bFindCompleteFootprint: bool, splitElement3D: eSplitElement3D):
        """Constructor

        Passive geometry is virtual geometry which is using for element snooping. Typical passive geometry is
        boundary area around text. This area has no edges like a Hatching, but if cursor is inside this area,
        then element must be snooped. Passive geometry has no points, perpendicular points, edges, etc. .

        Args:
            bFindBaseGeometry:        If true, find the base geometry element (e.g. line from polyline)
            bFindAreaGeometry:        If true, the service adds the nearest area geometry if nothing else is found
            bPerpendicularOnElement:  If true, the service adds perpendicular geometry
            bFindNonPassiveOnly:      If true, then only non passive geometry will be searching
            bSplitAreaGeometries:     If true, find the line geometry element for area geometries (e.g line from polygon)
            bIdentifyEmbeddedElement: If true, find elements from embedded documents
            bFindCompleteFootprint:   If true, find the complete footprint of a wall instead of the footprint of the wall tier
            splitElement3D:           Split the 3D element geometry ---> in case of bFindBaseGeometry the split is always done to edges !!!
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class UndoRedoService():
    """Implementation of the undo/redo service
    """
    def ActivateCollectedElementsForFinishUpdate(self):
        """activate collected elements from undo step, important for next
        finish update
        """
    def CollectElementsForMultipleTransactions(self):
        """Collect the elements for adding multiple transactions to one undo step
        """
    @typing.overload
    def CreateUndoStep(self, eventID: int):
        """Create an undo step

        Args:
            eventID: Event ID of the undo step
        """
    @typing.overload
    def CreateUndoStep(self):
        """Create an undo step
        """
    def CreateUndoStep(self):
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def IsInUndoService() -> bool:
        """Check if an active undo service is present

        Returns:
            Active undo service is present
        """
    def ResetTransactionError(self):
        """Reset the transaction error
        """
    def SetUndoDescription(self, textID: int):
        """Set the undo step description independent from menu event text

        Args:
            textID: Text ID of the undo step
        """
    def SetUndoStepEvent(self, eventID: int):
        """Set the undo step event

        Args:
            eventID: Event ID of the undo step
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, isPassivateAll: bool = False, isLockPreviewDraw: bool = False,
                 collectEleForMultipleTransactions: bool = False):
        """Constructor

        Args:
            doc:                               Current document
            isPassivateAll:                    if true passivate all, default is false
            isLockPreviewDraw:                 Lock the preview drawing during the undo step creation
            collectEleForMultipleTransactions: Collect the elements, if the UndoRedoService is included in multiple transactions
        """
    @typing.overload
    def __init__(self, element: UndoRedoService):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class ValueInputControlData():
    """Data class with settings of the input control, that can be optionally displayed in the dialog line e.g. along with the XYZ coordinate input fields.
    """
    def AddShortcutControl(self, ctrlType: eValueInputControlType):
        """Add a shortcut control to the coordinate input dialog

        Args:
            ctrlType: Type of the shortcut control
        """
    def GetControlType(self) -> eValueInputControlType:
        """Get the type of the input control

        Returns:
            Type of the input control
        """
    def GetInitText(self) -> object:
        """Get the init input text

        Returns:
            Init input text
        """
    def GetInitValue(self) -> float:
        """Get the init input value

        Returns:
            Init input value
        """
    def GetMaxTextLen(self) -> int:
        """Get the maximal length of the input text

        Returns:
            Maximal length of the input text
        """
    def GetMaxValue(self) -> float:
        """Get the maximal input value

        Returns:
            Maximal input value
        """
    def GetMinTextLen(self) -> int:
        """Get the minimal length of the input text

        Returns:
            Minimal length of the input text
        """
    def GetMinValue(self) -> float:
        """Get the minimal input value

        Returns:
            Minimal input value
        """
    def GetShortcutControlType(self) -> eValueInputControlType:
        """Get the type of the shortcut input control

        Returns:
            Type of the shortcut input control
        """
    def IsDisableCoord(self) -> bool:
        """Get the disable coordinate input state

        Returns:
            Disable the coordinate input in case of value input: true/false
        """
    def IsEmptyControl(self) -> bool:
        """Get the empty input control state

        Returns:
            Set an empty value to the input control: true/false
        """
    def IsSetFocus(self) -> bool:
        """Get the input focus state

        Returns:
            Set the input focus to the control: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ctrlType: eValueInputControlType, bSetFocus: bool = True, bDisableCoord: bool = True):
        """Constructor to create a control with standard behavior defined by the control type

        Args:
            ctrlType:      Control type
            bSetFocus:     Set the input focus to the control: true/false
            bDisableCoord: Input inside the external control disables the coordinate controls: true/false
        """
    @typing.overload
    def __init__(self, ctrlType: eValueInputControlType, minValue: float, maxValue: float, bSetFocus: bool, bDisableCoord: bool):
        """Constructor to create an empty control

        Args:
            ctrlType:      Control type
            minValue:      Minimal input value
            maxValue:      Maximal input value
            bSetFocus:     Set the input focus to the control: true/false
            bDisableCoord: Input inside the external control disables the coordinate controls: true/false
        """
    @typing.overload
    def __init__(self, ctrlType: eValueInputControlType, minValue: int, maxValue: int, bSetFocus: bool, bDisableCoord: bool):
        """Constructor to create an empty control

        Args:
            ctrlType:      Control type
            minValue:      Minimal input value
            maxValue:      Maximal input value
            bSetFocus:     Set the input focus to the control: true/false
            bDisableCoord: Input inside the external control disables the coordinate controls: true/false
        """
    @typing.overload
    def __init__(self, ctrlType: eValueInputControlType, initValue: float, minValue: float, maxValue: float, bSetFocus: bool,
                 bDisableCoord: bool):
        """Constructor to create a control with an init value

        Args:
            ctrlType:      Control type
            initValue:     Initialize input value
            minValue:      Minimal input value
            maxValue:      Maximal input value
            bSetFocus:     Set the input focus to the control: true/false
            bDisableCoord: Input inside the external control disables the coordinate controls: true/false
        """
    @typing.overload
    def __init__(self, ctrlType: eValueInputControlType, initValue: int, minValue: int, maxValue: int, bSetFocus: bool,
                 bDisableCoord: bool):
        """Constructor to create a control with an init value

        Args:
            ctrlType:      Control type
            initValue:     Initialize input value
            minValue:      Minimal input value
            maxValue:      Maximal input value
            bSetFocus:     Set the input focus to the control: true/false
            bDisableCoord: Input inside the external control disables the coordinate controls: true/false
        """
    @typing.overload
    def __init__(self, ctrlType: eValueInputControlType, initValue: float, bSetFocus: bool, bDisableCoord: bool):
        """Constructor to create a control with an init value.
        The value range is defined by the control type

        Args:
            ctrlType:      Control type
            initValue:     Initialize input value
            bSetFocus:     Set the input focus to the control: true/false
            bDisableCoord: Input inside the external control disables the coordinate controls: true/false
        """
    @typing.overload
    def __init__(self, ctrlType: eValueInputControlType, initText: object, minTextLen: int, maxTextLen: int, bSetFocus: bool = True,
                 bDisableCoord: bool = False):
        """Constructor to create a control with an init text

        Args:
            ctrlType:      Control type
            initText:      Initialize input text
            minTextLen:    Minimal text length
            maxTextLen:    Maximal text length
            bSetFocus:     Set the input focus to the control: true/false
            bDisableCoord: Input inside the external control disables the coordinate controls: true/false
        """
    @typing.overload
    def __init__(self, element: ValueInputControlData):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class ViewWorldProjection():
    """Implementation of the view - world projection
    """
    @staticmethod
    def CreateForUnitTest(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> ViewWorldProjection:
        """Create the object for a unit test

        Args:
            doc: Document

        Returns:
            created object
        """
    def GetDocumentID(self) -> int:
        """Get the document ID

        Returns:
            Document ID
        """
    def GetEyePoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get eye point of current projection

        Eye point is point where camera is.

        Returns:
            Eye point
        """
    def GetIsoProjection(self) -> eProjectionType:
        """Get the isometric projection of the view

        Returns:
            Isometric projection of the view
        """
    def GetMatrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """Get the view matrix
        """
    def GetPixelFactor(self) -> tuple[float, float]:
        """Get factor of pixel to world coordinates

        Used when you need calculate how much millimeters are one pixel

        Returns:
            tuple(Pixel factor in x direction,
                  Pixel factor in y direction)
        """
    def GetScreenScale(self) -> float:
        """Get the screen scale

        Returns:
            Screen scale
        """
    def GetSearchRadiusByPixel(self, pixel: int) -> float:
        """Get the search radius by pixel

        Args:
            pixel: Pixel of the search radius

        Returns:
            Search radius in view size
        """
    def GetViewAngle(self) -> float:
        """Get the rotation angle of the view

        Returns:
            Rotation angle of the view
        """
    def GetViewPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get view point of current projection

        View point is point where you are looking (focused). View point lie in plain of drawn data.

        Returns:
            Eye point
        """
    def GetViewSize(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the size of the view

        Returns:
            Size of the view
        """
    def GetViewZAngle(self) -> float:
        """Get the rotation angle of the view in z-direction

        Returns:
            Rotation angle of the view in z-direction
        """
    def GetWindowNumber(self) -> int:
        """Get the window number

        Returns:
            Window number
        """
    def GetZoomWindowNumber(self) -> int:
        """Get the zoom window number. Numbers 1 and more for active zoom window.

        Returns:
            Window number
        """
    def GetZoomWndTextFac(self) -> float:
        """Get the text-factor of the zoom window

        Returns:
            Text-factor of the zoom window
        """
    def GetZoomWndXFac(self) -> float:
        """Get the x-factor of the zoom window

        Returns:
            X-factor of the zoom window
        """
    def GetZoomWndYFac(self) -> float:
        """Get the y-factor of the zoom window

        Returns:
            Y-factor of the zoom window
        """
    def IsAssistWindow(self) -> bool:
        """Check for assist window

        Returns:
            The document is an assist window: true/false
        """
    def IsCentralProjection(self) -> bool:
        """Check, whether the projection is a central projection

        Returns:
            Central projection: true/false
        """
    def IsFreeProjection(self) -> bool:
        """Check, whether the projection is a free projection

        Returns:
            Projection is a free view: true/false
        """
    def IsGroundplanView(self) -> bool:
        """Check, whether the projection is ground plan view

        Returns:
            Projection is ground plan view: true/false
        """
    def IsInView(self, pnt: NemAll_Python_Geometry.Point2D) -> bool:
        """Check, whether the point is inside the view

        Args:
            pnt: View point

        Returns:
            Point is inside the view: true/false
        """
    def IsIsometricProjection(self) -> bool:
        """Check, whether the projection is a isometric projection

        Returns:
            Projection is a isometric projection: true/false
        """
    def IsSideView(self) -> bool:
        """Check, whether the projection is a side view

        Returns:
            Projection is a side view: true/false
        """
    def IsZoomWindow(self) -> bool:
        """Check if the input is inside the zoom window

        Returns:
            Window number
        """
    def ProjectionToWorld(self, pnt: NemAll_Python_Geometry.Point2D,
                          refPnt: NemAll_Python_Geometry.Point3D) -> NemAll_Python_Geometry.Point3D:
        """Get the world 3D point from a projection 2D point and a reference point

        Args:
            pnt:    View Point
            refPnt: Reference point with the additional coordinate

        Returns:
            World 3D point
        """
    def SetPointDepth(self, pointWithDepth: NemAll_Python_Geometry.Point3D) -> NemAll_Python_Geometry.Point3D:
        """Set point depth by current view projection type and pointWithDepth

        Args:
            pointWithDepth: Point with depth

        Returns:
            Point to set
        """
    def ViewPerpendicularToWorld(self, line3D: NemAll_Python_Geometry.Line3D,
                                 pnt: NemAll_Python_Geometry.Point3D) -> NemAll_Python_Geometry.Point3D:
        """Transform a view perpendicular point to a world perpendicular point

        Args:
            line3D: 3D perpendicular line
            pnt:    Reference point for the perpendicular

        Returns:
            World perpendicular point
        """
    def ViewToPixel(self, pnt: NemAll_Python_Geometry.Point2D, bBottomTop: bool,
                    considerZoomwindow: bool = True) -> NemAll_Python_Geometry.Point2D:
        """Transform a view point to a pixel coordinate

        Args:
            pnt:                View point
            bBottomTop:         The y zero point is on the bottom of the screen: true/false
            considerZoomwindow: if true and the position is in a zoom window, then the zoom window will be used for the calculation

        Returns:
            Pixel view point
        """
    def ViewToWorld(self, pnt: NemAll_Python_Geometry.Point2D, z: float = 0) -> NemAll_Python_Geometry.Point3D:
        """Transform a view point to a world point

        Args:
            pnt: View point
            z:   z-coordinate

        Returns:
            World point
        """
    def ViewToWorldBaseZ(self, pnt: NemAll_Python_Geometry.Point2D, zWorld: float) -> NemAll_Python_Geometry.Point3D:
        """Transform a view point to a world point with resulting z-coordinate

        Args:
            pnt:    View point
            zWorld: Z-coordinate

        Returns:
            World point with resulting z-coordinate
        """
    def ViewToWorldBaseZ0(self, pnt: NemAll_Python_Geometry.Point2D) -> NemAll_Python_Geometry.Point3D:
        """Transform a view point to a world point with resulting z-world = 0

        Args:
            pnt: View point

        Returns:
            World point with z=0
        """
    def ViewToWorldPlane(self, pnt: NemAll_Python_Geometry.Point2D,
                         plane: NemAll_Python_Geometry.Plane3D) -> NemAll_Python_Geometry.Point3D:
        """Transform the view point to a world plane

        Args:
            pnt:   View point
            plane: Plane

        Returns:
            World point at the plane
        """
    def ViewToWorldRay(self, pnt: NemAll_Python_Geometry.Point2D) -> tuple[NemAll_Python_Geometry.Point3D, NemAll_Python_Geometry.Vector3D]:
        """Calculates a ray

        Calculates a ray (for non-vanishing-point-projections,
        rather a line) from the given view 2D point.
        Can be used for pick-point calculations.

        Note that we have a right-hand view coordinate system, so
        its Z axis points towards the eye.

        Args:
            pnt: View point

        Returns:
            tuple(World point of ray,
                  Vector of calculated ray point)
        """
    def ViewToWorldViewZ(self, pnt: NemAll_Python_Geometry.Point2D, viewZ: float) -> NemAll_Python_Geometry.Point3D:
        """Transform a view 2D point with view Z coordinate to a world point

        Args:
            pnt:   View point
            viewZ: z-coordinate in view transformation

        Returns:
            World point
        """
    def WorldToPixel(self, pnt: NemAll_Python_Geometry.Point3D, bBottomTop: bool) -> NemAll_Python_Geometry.Point2D:
        """Transform the world point to a pixel point

        Args:
            pnt:        World point
            bBottomTop: The y zero point is on the bottom of the screen: true/false

        Returns:
            Pixel point
        """
    @typing.overload
    def WorldToProjection(self, pnt: NemAll_Python_Geometry.Point3D) -> NemAll_Python_Geometry.Point2D:
        """Get the projection 2D point from a world 3D point

        Args:
            pnt: World point

        Returns:
            2D projection point
        """
    @typing.overload
    def WorldToProjection(self, line: NemAll_Python_Geometry.Line3D) -> NemAll_Python_Geometry.Line2D:
        """Get the projection 2D line from a world 3D line

        Args:
            line: World line

        Returns:
            2D projection line
        """
    def WorldToProjection(self) -> NemAll_Python_Geometry.Line2D:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def WorldToProjectionBase0(self, pnt: NemAll_Python_Geometry.Point3D) -> NemAll_Python_Geometry.Point3D:
        """Get the world projection point with the base 0

        Args:
            pnt: World point

        Returns:
            World projection point with the base 0
        """
    @typing.overload
    def WorldToProjectionBase0(self, line: NemAll_Python_Geometry.Line3D) -> NemAll_Python_Geometry.Line3D:
        """Get the world projection line with the base 0

        Args:
            line: World coordinate line

        Returns:
            World projection point with the base 0
        """
    def WorldToProjectionBase0(self) -> NemAll_Python_Geometry.Line3D:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def WorldToView(self, pnt: NemAll_Python_Geometry.Point3D) -> NemAll_Python_Geometry.Point2D:
        """Transform a world point to a view point

        Args:
            pnt: World point

        Returns:
            View point
        """
    @typing.overload
    def WorldToView(self, pnt: NemAll_Python_Geometry.Point2D) -> NemAll_Python_Geometry.Point2D:
        """Transform a world point to a view point

        Args:
            pnt: World point

        Returns:
            View point
        """
    @typing.overload
    def WorldToView(self, x: float, y: float, z: float) -> NemAll_Python_Geometry.Point2D:
        """Transform a world point to a view point

        Args:
            x: X-coordinate world
            y: Y-coordinate world
            z: Z-coordinate world

        Returns:
            View point
        """
    @typing.overload
    def WorldToView(self, line: NemAll_Python_Geometry.Line3D) -> NemAll_Python_Geometry.Line2D:
        """Transform a 3D world line to a 2D view line

        Args:
            line: World line

        Returns:
            View line
        """
    @typing.overload
    def WorldToView(self, line: NemAll_Python_Geometry.Line2D) -> NemAll_Python_Geometry.Line2D:
        """Transform a 2D world line to a 2D view line

        Args:
            line: World line

        Returns:
            View line
        """
    @typing.overload
    def WorldToView(self, polyline3D: NemAll_Python_Geometry.Polyline3D) -> NemAll_Python_Geometry.Polyline2D:
        """Transform a 3D world polyline to a 2D view polyline

        Args:
            polyline3D: World polyline

        Returns:
            View polyline
        """
    def WorldToView(self) -> NemAll_Python_Geometry.Polyline2D:
        """ Overloaded function. See individual overloads.
        """
    def WorldToView3D(self, pnt: NemAll_Python_Geometry.Point3D) -> NemAll_Python_Geometry.Point3D:
        """Transform a world point to a view 3D point

        If Z coordinate of returned view point is positive, then world point is before eye (i.e. is visible).

        Args:
            pnt: World point

        Returns:
            View point
        """
    @typing.overload
    def WorldToWorldPlane(self, pnt: NemAll_Python_Geometry.Point3D,
                          plane: NemAll_Python_Geometry.Plane3D) -> NemAll_Python_Geometry.Point3D:
        """Transform a world point to a plane point

        Args:
            pnt:   World point
            plane: Plane

        Returns:
            Plane point in world coordinates
        """
    @typing.overload
    def WorldToWorldPlane(self, line: NemAll_Python_Geometry.Line3D,
                          plane: NemAll_Python_Geometry.Plane3D) -> NemAll_Python_Geometry.Line3D:
        """Transform a world line to a plane line

        Args:
            line:  World line
            plane: Plane

        Returns:
            Plane line in world coordinates
        """
    def WorldToWorldPlane(self) -> NemAll_Python_Geometry.Line3D:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: ViewWorldProjection):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class VisibleService():

    @staticmethod
    def IsElementCurrentlyHidden(element: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> bool:
        """Get the hidden state of the element

        Args:
            element
        """
    @staticmethod
    def ShowAllElements():
        """Show all elements
        """
    @staticmethod
    def ShowElement(eleList: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, bShow: bool, bForceDraw: bool):
        """Show/hide the element

        Args:
            eleList:       Element list as BaseElementAdapterList
            bShow:         Show / Hide = true/false
            bForceDraw:    Force the draw state
        """
    @staticmethod
    def ShowElements(eleList: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, bShow: bool, bForceDraw: bool = True):
        """Show/hide the elements

        Args:
            eleList:   Element list as BaseElementAdapterList
            bShow:     Show / Hide = true/false
            bForceDraw:Force the draw state
        """

class eDocumentSnoopType(enum.Enum):
    """Definition of the document snoop types

    eSnoopActiveDocuments    : Snoop only in active documents
    eSnoopPassiveDocuments   : Snoop only in passive documents
    eSnoopAllDocuments       : Snoop in all documents
    eSnoopPassiveDocsOrLayers: Snoop in passive documents or passive layers
    """
    eSnoopActiveDocuments = 0
    eSnoopAllDocuments = 2
    eSnoopPassiveDocsOrLayers = 3
    eSnoopPassiveDocuments = 1

    names = {eSnoopActiveDocuments: eSnoopActiveDocuments,
             eSnoopPassiveDocuments: eSnoopPassiveDocuments,
             eSnoopAllDocuments: eSnoopAllDocuments,
             eSnoopPassiveDocsOrLayers: eSnoopPassiveDocsOrLayers}

    values = {0: eSnoopActiveDocuments,
              1: eSnoopPassiveDocuments,
              2: eSnoopAllDocuments,
              3: eSnoopPassiveDocsOrLayers}

    def __getitem__(self, key: (str | int | float)) -> eDocumentSnoopType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eDrawElementIdentPointSymbols(enum.Enum):
    """If the identification mode allows to select an element (IDENT_..._ELEMENT_...), it's possible
    to draw also the identification point symbol of the identification point
    (element point, center point, ...) at the element

    eDRAW_IDENT_ELEMENT_POINT_SYMBOL_NO : Don't draw an identification point symbol on a selected element
    eDRAW_IDENT_ELEMENT_POINT_SYMBOL_YES: Draw an identification point symbol on a selected element
    """
    eDRAW_IDENT_ELEMENT_POINT_SYMBOL_NO = 0
    eDRAW_IDENT_ELEMENT_POINT_SYMBOL_YES = 1

    names = {eDRAW_IDENT_ELEMENT_POINT_SYMBOL_NO: eDRAW_IDENT_ELEMENT_POINT_SYMBOL_NO,
             eDRAW_IDENT_ELEMENT_POINT_SYMBOL_YES: eDRAW_IDENT_ELEMENT_POINT_SYMBOL_YES}

    values = {0: eDRAW_IDENT_ELEMENT_POINT_SYMBOL_NO,
              1: eDRAW_IDENT_ELEMENT_POINT_SYMBOL_YES}

    def __getitem__(self, key: (str | int | float)) -> eDrawElementIdentPointSymbols:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eIdentificationMode(enum.Enum):
    """Type of the identification mode during **point input**.

    This class defines possible options for point or/and element identification.
    In other words, for what kind of points or geometry elements should the IFW search
    for during a **point input**.

    """
    eIDENT_ARCHPOINT = 10
    """Identify the nearest **point** at the cursor position.

        Similar to eIDENT_POINT, but additionally when point was found on an **architectural element**,
        a reference 2D line, on which this point is located, is identified. The line can be get with
        GetReferenceLine.
        """
    eIDENT_ARCHPOINT_OFFSET = 11
    """Identify the nearest **point** at the cursor position.

        As eIDENT_ARCHPOINT, but in case a line is identified,
        a second input step is activated similar to the in eIDENT_POINT_OFFSET

        When the point was found in an UVS, the point is returned in the world coordinate system
        """
    eIDENT_ARCH_ELEMENTPOINT = 12
    """Identify the nearest **element point** at an architecture element.

        Similar to eIDENT_ELEMENTPOINT, but additionally a reference line of an architectural element
        is identified and can be get with GetReferenceLine
        """
    eIDENT_DOCKINGPOINT = 13
    """Identify the nearest docking point at the cursor position"""
    eIDENT_ELEMENTPOINT = 1
    """Identify the nearest **element point** at the cursor position.

        Similar to eIDENT_POINT, but input controls for XYZ coordinates are disabled
        and track tracing is not performed. This implies, that the input point lies on
        an existing element.
        """
    eIDENT_POINT = 0
    """Identify the nearest **point** at the cursor position.

        Identified are start, end, center or intersection points of **all** kind of elements.
        Snapping options set by the user in Allplan settings are considered.
        This is the default way of point identification.
        """
    eIDENT_POINT_ASSOC_VIEW_WORLD = 2
    """Identify the nearest **point** at the cursor position.

        Similar to eIDENT_POINT, but when the point was found in an UVS, the point is returned
        in the world coordinate system
        """
    eIDENT_POINT_ELEMENT = 3
    """Identify the nearest **point or element** at the cursor position

        As eIDENT_POINT, but additionally a geometry element (like edge/face of a polyhedron,
        polygon segment, etc...) is searched during the point input. The found geometry element
        can be get with GetSelectedGeometryElement. Element is **not identified**, when a point
        (start, end, center, intersection, etc...) is found.

        Filter for the element identification can be set with SetGeometryFilter and SetGeometryElementFilter
        """
    eIDENT_POINT_ELEMENT_ALWAYS = 5
    """Similar to eIDENT_POINT_ELEMENT, but the element is **always** identified, even when a point was found"""
    eIDENT_POINT_ELEMENT_ALWAYS_CENTER = 6
    """As eIDENT_POINT_ELEMENT_ALWAYS"""
    eIDENT_POINT_ELEMENT_CENTER = 4
    """Similar to eIDENT_POINT_ELEMENT, but the element is identified also, when a center point (but not start/end point) is found."""
    eIDENT_POINT_OFFSET = 8
    """Identify the nearest **point or element** at the cursor position
        Similar to POINT_ELEMENT, but in case a line is identified (2D or 3D), a second input step is introduced, where the user can provide the offset distance. The resulting point will be located on the line at the given distance from the start or end point (depending, where the line was clicked)"""
    eIDENT_POINT_PERPENDICULAR = 7
    """Identify the nearest **point** or point perpendicular to a line

        Similar to eIDENT_POINT, but additionally if a 2D line is identified, the result will be
        a point calculated by projecting the previously input point onto this line.

        Works only in ground view!
        """
    eIDENT_TEXTPOINT = 9
    """Snapping only to the anchor points of text or label elements"""
    eIDENT_TEXTPOINTER_POINT = 14

    names = {eIDENT_POINT: eIDENT_POINT,
             eIDENT_ELEMENTPOINT: eIDENT_ELEMENTPOINT,
             eIDENT_POINT_ASSOC_VIEW_WORLD: eIDENT_POINT_ASSOC_VIEW_WORLD,
             eIDENT_POINT_ELEMENT: eIDENT_POINT_ELEMENT,
             eIDENT_POINT_ELEMENT_CENTER: eIDENT_POINT_ELEMENT_CENTER,
             eIDENT_POINT_ELEMENT_ALWAYS: eIDENT_POINT_ELEMENT_ALWAYS,
             eIDENT_POINT_ELEMENT_ALWAYS_CENTER: eIDENT_POINT_ELEMENT_ALWAYS_CENTER,
             eIDENT_POINT_PERPENDICULAR: eIDENT_POINT_PERPENDICULAR,
             eIDENT_POINT_OFFSET: eIDENT_POINT_OFFSET,
             eIDENT_TEXTPOINT: eIDENT_TEXTPOINT,
             eIDENT_ARCHPOINT: eIDENT_ARCHPOINT,
             eIDENT_ARCHPOINT_OFFSET: eIDENT_ARCHPOINT_OFFSET,
             eIDENT_ARCH_ELEMENTPOINT: eIDENT_ARCH_ELEMENTPOINT,
             eIDENT_DOCKINGPOINT: eIDENT_DOCKINGPOINT,
             eIDENT_TEXTPOINTER_POINT: eIDENT_TEXTPOINTER_POINT}

    values = {0: eIDENT_POINT,
              1: eIDENT_ELEMENTPOINT,
              2: eIDENT_POINT_ASSOC_VIEW_WORLD,
              3: eIDENT_POINT_ELEMENT,
              4: eIDENT_POINT_ELEMENT_CENTER,
              5: eIDENT_POINT_ELEMENT_ALWAYS,
              6: eIDENT_POINT_ELEMENT_ALWAYS_CENTER,
              7: eIDENT_POINT_PERPENDICULAR,
              8: eIDENT_POINT_OFFSET,
              9: eIDENT_TEXTPOINT,
              10: eIDENT_ARCHPOINT,
              11: eIDENT_ARCHPOINT_OFFSET,
              12: eIDENT_ARCH_ELEMENTPOINT,
              13: eIDENT_DOCKINGPOINT,
              14: eIDENT_TEXTPOINTER_POINT}

    def __getitem__(self, key: (str | int | float)) -> eIdentificationMode:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eLayerSnoopType(enum.Enum):
    """Definition of the layer snoop types

    eSnoopActiveLayers : Snoop only in active layers
    eSnoopPassiveLayers: Snoop only in passive layers
    eSnoopAllLayers    : Snoop in all layers
    """
    eSnoopActiveLayers = 0
    eSnoopAllLayers = 2
    eSnoopPassiveLayers = 1

    names = {eSnoopActiveLayers: eSnoopActiveLayers,
             eSnoopPassiveLayers: eSnoopPassiveLayers,
             eSnoopAllLayers: eSnoopAllLayers}

    values = {0: eSnoopActiveLayers,
              1: eSnoopPassiveLayers,
              2: eSnoopAllLayers}

    def __getitem__(self, key: (str | int | float)) -> eLayerSnoopType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eProjectionType(enum.Enum):
    """Projection type of the view
    """
    EAST_VIEW = 3
    FREE_ONLY_3D = 9
    FREE_VIEW = 0
    GROUND_PLAN = 1
    NORTH_EAST_VIEW = 5
    NORTH_VIEW = 2
    NORTH_WEST_VIEW = 6
    SOUTH_EAST_VIEW = 8
    SOUTH_VIEW = -2
    SOUTH_WEST_VIEW = 7
    WEST_VIEW = -3
    WORKING_PLANE_VIEW = 4

    names = {FREE_VIEW: FREE_VIEW,
             GROUND_PLAN: GROUND_PLAN,
             NORTH_VIEW: NORTH_VIEW,
             SOUTH_VIEW: SOUTH_VIEW,
             EAST_VIEW: EAST_VIEW,
             WEST_VIEW: WEST_VIEW,
             WORKING_PLANE_VIEW: WORKING_PLANE_VIEW,
             NORTH_EAST_VIEW: NORTH_EAST_VIEW,
             NORTH_WEST_VIEW: NORTH_WEST_VIEW,
             SOUTH_WEST_VIEW: SOUTH_WEST_VIEW,
             SOUTH_EAST_VIEW: SOUTH_EAST_VIEW,
             FREE_ONLY_3D: FREE_ONLY_3D}

    values = {0: FREE_VIEW,
              1: GROUND_PLAN,
              2: NORTH_VIEW,
              -2: SOUTH_VIEW,
              3: EAST_VIEW,
              -3: WEST_VIEW,
              4: WORKING_PLANE_VIEW,
              5: NORTH_EAST_VIEW,
              6: NORTH_WEST_VIEW,
              7: SOUTH_WEST_VIEW,
              8: SOUTH_EAST_VIEW,
              9: FREE_ONLY_3D}

    def __getitem__(self, key: (str | int | float)) -> eProjectionType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eSplitElement3D(enum.Enum):
    """Split type for 3D elements
    """
    ELEMENT3D_EDGES = 2
    ELEMENT3D_FACES = 1
    ELEMENT3D_NO_SPLIT = 0

    names = {ELEMENT3D_NO_SPLIT: ELEMENT3D_NO_SPLIT,
             ELEMENT3D_FACES: ELEMENT3D_FACES,
             ELEMENT3D_EDGES: ELEMENT3D_EDGES}

    values = {0: ELEMENT3D_NO_SPLIT,
              1: ELEMENT3D_FACES,
              2: ELEMENT3D_EDGES}

    def __getitem__(self, key: (str | int | float)) -> eSplitElement3D:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eTrackLineType(enum.Enum):
    """Definition of the track line types

    TRACKLINE_NO           : No track line
    TRACKLINE_ENDLESS      : Endless track line
    TRACKLINE_EXTENSION    : Extension track line from the start point
    TRACKLINE_EXTENSION_END: Extension track line from the end point
    """
    TRACKLINE_ENDLESS = 1
    TRACKLINE_EXTENSION = 2
    TRACKLINE_EXTENSION_END = 3
    TRACKLINE_NO = 0

    names = {TRACKLINE_NO: TRACKLINE_NO,
             TRACKLINE_ENDLESS: TRACKLINE_ENDLESS,
             TRACKLINE_EXTENSION: TRACKLINE_EXTENSION,
             TRACKLINE_EXTENSION_END: TRACKLINE_EXTENSION_END}

    values = {0: TRACKLINE_NO,
              1: TRACKLINE_ENDLESS,
              2: TRACKLINE_EXTENSION,
              3: TRACKLINE_EXTENSION_END}

    def __getitem__(self, key: (str | int | float)) -> eTrackLineType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eValueInputControlType(enum.Enum):
    """Types of the input controls, that can be displayed in the _dialog line_ in Allplan
    """
    eANGLE_COMBOBOX = 6
    """Angle input as a combo box with suggested angle values. Free input is possible."""
    eANGLE_EDIT = 11
    """Angle input as a regular edit field. Value is entered in the current Allplan angle units, but returned in radians."""
    eCONTROL_EXTERNAL = 1
    eCONTROL_NONE = 0
    """No input control"""
    eCOORDINATE_EDIT = 101
    """Input control for a single coordinate. Value is entered in the current Allplan length units, but returned in millimeters. Allowed values between -1e10 and 1-e10"""
    eCOORDINATE_EDIT_FIX = 102
    """Similar to eCOORDINATE_EDIT"""
    eCOORDINATE_EDIT_GE0 = 103
    """Similar to eCOORDINATE_EDIT, but only values >= 0 allowed"""
    eCOORDINATE_EDIT_GT0 = 104
    """Similar to eCOORDINATE_EDIT, but only values > 0 allowed"""
    eDIMENSION_EDIT = 5
    """Length input with current length units. Returned value is in millimeters. Values between 0.0 and 1e10 allowed"""
    eDIMENSION_EDIT_MM = 10
    """Length input in millimeters. Values between 0.0 and 1e10 allowed"""
    eDOUBLE_EDIT = 2
    """Input control for a double value. Values between 0.0 and 1e10 allowed"""
    eINT_COMBOBOX = 4
    """Similar to eINT_EDIT, but with a combo box with suggested values."""
    eINT_EDIT = 3
    """Input control for a 32-bit signed integer, with allowed value between 0 and -2147483684"""
    eNUMBER_EDIT_1 = 201
    """Edit control for an integer value between 1 and 1e6"""
    eNUMBER_EDIT_1_GE0 = 202
    """Edit control for an integer value between 0 and 1e6"""
    eROTATION_ANGLE_STEP = 8
    """Input control for a shortcut input (+ or -). Input triggers the on_shortcut_control_input event."""
    eTEXT_EDIT = 9
    """String input control"""
    eWALL_PLACEMENT = 7
    """Input control for a shortcut input (+ or -). Input triggers the on_shortcut_control_input event."""

    names = {eCONTROL_NONE: eCONTROL_NONE,
             eCONTROL_EXTERNAL: eCONTROL_EXTERNAL,
             eDOUBLE_EDIT: eDOUBLE_EDIT,
             eINT_EDIT: eINT_EDIT,
             eINT_COMBOBOX: eINT_COMBOBOX,
             eDIMENSION_EDIT: eDIMENSION_EDIT,
             eANGLE_COMBOBOX: eANGLE_COMBOBOX,
             eWALL_PLACEMENT: eWALL_PLACEMENT,
             eROTATION_ANGLE_STEP: eROTATION_ANGLE_STEP,
             eTEXT_EDIT: eTEXT_EDIT,
             eDIMENSION_EDIT_MM: eDIMENSION_EDIT_MM,
             eANGLE_EDIT: eANGLE_EDIT,
             eCOORDINATE_EDIT: eCOORDINATE_EDIT,
             eCOORDINATE_EDIT_FIX: eCOORDINATE_EDIT_FIX,
             eCOORDINATE_EDIT_GE0: eCOORDINATE_EDIT_GE0,
             eCOORDINATE_EDIT_GT0: eCOORDINATE_EDIT_GT0,
             eNUMBER_EDIT_1: eNUMBER_EDIT_1,
             eNUMBER_EDIT_1_GE0: eNUMBER_EDIT_1_GE0}

    values = {0: eCONTROL_NONE,
              1: eCONTROL_EXTERNAL,
              2: eDOUBLE_EDIT,
              3: eINT_EDIT,
              4: eINT_COMBOBOX,
              5: eDIMENSION_EDIT,
              6: eANGLE_COMBOBOX,
              7: eWALL_PLACEMENT,
              8: eROTATION_ANGLE_STEP,
              9: eTEXT_EDIT,
              10: eDIMENSION_EDIT_MM,
              11: eANGLE_EDIT,
              101: eCOORDINATE_EDIT,
              102: eCOORDINATE_EDIT_FIX,
              103: eCOORDINATE_EDIT_GE0,
              104: eCOORDINATE_EDIT_GT0,
              201: eNUMBER_EDIT_1,
              202: eNUMBER_EDIT_1_GE0}

    def __getitem__(self, key: (str | int | float)) -> eValueInputControlType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]



```