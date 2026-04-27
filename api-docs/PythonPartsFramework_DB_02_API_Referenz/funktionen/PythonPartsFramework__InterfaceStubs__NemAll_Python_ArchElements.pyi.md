---
title: "NemAll_Python_ArchElements"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_ArchElements.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_ArchElements

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_ArchElements.pyi`  
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

"""Exposed classes and functions from NemAll_Python_ArchElements"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_IFW_ElementAdapter
import NemAll_Python_BaseElements
import NemAll_Python_BasisElements
import NemAll_Python_Geometry


__all__ = [
    "ArchBaseProperties",
    "ArchElement",
    "ArchitectureElementsGeometryService",
    "AxisProperties",
    "BasePlaneReferences",
    "BeamElement",
    "BeamProperties",
    "BlockFoundationElement",
    "BlockFoundationProperties",
    "BottomTopPlaneService",
    "Center",
    "CenterOfGravity",
    "CircularShape",
    "ColumnElement",
    "ColumnProperties",
    "CustomBoxPoint",
    "DoorOpeningElement",
    "DoorOpeningProperties",
    "DoorSwingProperties",
    "DoorSwingType",
    "ElementConverter",
    "FlushPierElement",
    "FlushPierProperties",
    "FreePlane",
    "GeneralOpeningElement",
    "GeneralOpeningProperties",
    "Horizontal",
    "JointElement",
    "JointProperties",
    "LeftBottom",
    "LeftTop",
    "MiddleBottom",
    "MiddleLeft",
    "MiddleRight",
    "MiddleTop",
    "NormalToBodyAxis",
    "OpeningSide",
    "OpeningSymbolsProperties",
    "OpeningType",
    "PlaneReferences",
    "ProfileCatalogService",
    "ProfileShape",
    "PropertyDialogs",
    "RectangularShape",
    "ReferencePlaneID",
    "RightBottom",
    "RightTop",
    "RoomElement",
    "RoomProperties",
    "ShapeType",
    "SlabElement",
    "SlabFoundationElement",
    "SlabFoundationProperties",
    "SlabOpeningElement",
    "SlabOpeningProperties",
    "SlabOpeningType",
    "SlabProperties",
    "SlabTierProperties",
    "SolidElementTruncationType",
    "StripFoundationElement",
    "StripFoundationProperties",
    "StructuralBeamElement",
    "StructuralBeamProperties",
    "StructuralBraceElement",
    "StructuralBraceProperties",
    "StructuralColumnElement",
    "StructuralColumnProperties",
    "StructuralElementProperties",
    "StructuralPurlinElement",
    "StructuralPurlinProperties",
    "SurfaceElementProperties",
    "Vertical",
    "VerticalElementProperties",
    "VerticalOpeningFacingProperties",
    "VerticalOpeningGeometryProperties",
    "VerticalOpeningRevealProperties",
    "VerticalOpeningRevealType",
    "VerticalOpeningShapeType",
    "VerticalOpeningSillProperties",
    "VerticalOpeningSillType",
    "VerticalOpeningTierOffsetProperties",
    "VerticalOpeningTierOffsetType",
    "WallAxisPosition",
    "WallElement",
    "WallProperties",
    "WallTierProperties",
    "WindowOpeningElement",
    "WindowOpeningProperties",
    "eArbitrary",
    "eCenter",
    "eChamfer",
    "eCircular",
    "eConical",
    "eFree",
    "eLeft",
    "ePolygonal",
    "eProfile",
    "eRectangular",
    "eRegularPolygonCircumscribed",
    "eRegularPolygonInscribed",
    "eRight",
    "eRiseBottomTop",
    "eStep",
    "eUnknown"
]


class ArchBaseProperties():
    """Base class representing properties of all kinds of architectural components
    """
    def GetAreaPresentationID(self) -> int:
        """Get the ID of the area representation

        Returns:
            ID of the area representation
        """
    def GetAreaPresentationType(self) -> int:
        """Get the type of the area representation

        Returns:
            Type of the area representation
        """
    def GetBackgroundColor(self) -> int:
        """Get the background color

        Returns:
            Background color
        """
    def GetBitmapName(self) -> str:
        """Get the name of the bitmap

        Returns:
            Name of the bitmap
        """
    def GetCalculationMode(self) -> int:
        """Get the calculation mode

        Returns:
            Integer representing the calculation mode as follows:

                -   0:  m3
                -   1:  m2
                -   2:  m
                -   3:  Pcs
                -   4:  kg
        """
    def GetCircleDivision(self) -> int:
        """Get the circle division (relevant only for circular profiles))

        Returns:
            Number of circle segments
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetFaceStyle(self) -> int:
        """Get the face style ID

        Returns:
            Face style ID
        """
    def GetFactor(self) -> float:
        """Get the factor

        Returns:
            Factor
        """
    def GetFilling(self) -> int:
        """Get the filling ID

        Returns:
            Filling ID
        """
    def GetHatch(self) -> int:
        """Get the hatch ID

        Returns:
            Hatch ID
        """
    def GetMaterial(self) -> str:
        """Get the material

        Returns:
            Material
        """
    def GetName(self) -> str:
        """Get the name

        Returns:
            Name
        """
    def GetPattern(self) -> int:
        """Get the pattern ID

        Returns:
            Pattern ID
        """
    def GetPlaneReferences(self) -> PlaneReferences:
        """Get the plane references

        Returns:
            Plane references
        """
    def GetPriority(self) -> int:
        """Get the priority

        Returns:
            Priority
        """
    def GetStatus(self) -> int:
        """Get the Status ID

        Returns:
            Status ID
        """
    def GetSurface(self) -> str:
        """Get the surface name and path

        Returns:
            Surface name and path
        """
    def GetTrade(self) -> int:
        """Get the trade index

        Returns:
            Trade index according to the definition of the enumeration attribute _trade_ (@209@)
        """
    def IsShowAreaElementInGroundView(self) -> bool:
        """Get the 'Show the area element in the ground view' state

        Returns:
            Show the area element in the ground view: true/false
        """
    def LoadFromFavoriteFile(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Load the properties from the favorite file

        Args:
            doc: Document
        """
    def RemoveCommonProperties(self):
        """Remove the common properties
        """
    def ResetAreaElement(self):
        """Reset the area element
        """
    def ResetBackgroundColor(self):
        """Reset the background color
        """
    def SetBackgroundColor(self, colorID: int):
        """Set the background color

        Args:
            colorID: Background color ID
        """
    def SetBitmapName(self, bitmapName: str):
        """Set the name of the bitmap

        Args:
            bitmapName: Bitmap name
        """
    def SetCalculationMode(self, calculationMode: int):
        """Set the calculation mode

        Args:
            calculationMode: Calculation mode
        """
    def SetCircleDivision(self, circleDivision: int):
        """Set the circle division

        Args:
            circleDivision: Circle division
        """
    def SetCommonProperties(self, comProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            comProp: Common properties
        """
    def SetFaceStyle(self, faceStyleID: int):
        """Set the face style

        Args:
            faceStyleID: Face style ID
        """
    def SetFactor(self, factor: float):
        """Set the factor

        Args:
            factor: Factor
        """
    def SetFilling(self, fillingID: int):
        """Set the filling

        Args:
            fillingID: Filling ID
        """
    def SetHatch(self, hatchID: int):
        """Set the hatch

        Args:
            hatchID: Hatch ID
        """
    def SetMaterial(self, material: str):
        """Set the material

        Args:
            material: Material
        """
    def SetName(self, name: str):
        """Set the name

        Args:
            name: Name
        """
    def SetPattern(self, patternID: int):
        """Set the pattern

        Args:
            patternID: Pattern ID
        """
    def SetPlaneReferences(self, planeRef: PlaneReferences):
        """Set the plane references

        Args:
            planeRef: Plane references
        """
    def SetPriority(self, priority: int):
        """Set the priority

        Args:
            priority: Priority
        """
    def SetShowAreaElementInGroundView(self, showInGroundView: bool):
        """Set the show area element in ground view state

        Args:
            showInGroundView: Show the area element in the ground view
        """
    def SetStatus(self, statusID: int):
        """Set the Status ID

        Args:
            statusID: Status ID
        """
    def SetSurface(self, surface: str):
        """Set the surface

        Args:
            surface: Surface
        """
    def SetTrade(self, value: int):
        """Set the trade index

        Args:
            value:  Trade index according to the definition of the enumeration attribute _trade_ (@209@)
        """
    def __init__(self, element: ArchBaseProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def BackgroundColor(self) -> int:
        """Get the background color
        """
    @BackgroundColor.setter
    def BackgroundColor(self, colorID: int) -> None:
        """Set the background color

        Args:
            colorID: Background color ID
        """
    @property
    def BitmapName(self) -> str:
        """Get the name of the bitmap
        """
    @BitmapName.setter
    def BitmapName(self, bitmapName: str) -> None:
        """Set the name of the bitmap

        Args:
            bitmapName: Bitmap name
        """
    @property
    def CalculationMode(self) -> int:
        """Calculation mode, represented by an integer as follows:

        -   0:  m3
        -   1:  m2
        -   2:  m
        -   3:  Pcs
        -   4:  kg
        """
    @CalculationMode.setter
    def CalculationMode(self, calculationMode: int) -> None:
        """Set the calculation mode

        Args:
            calculationMode: Calculation mode
        """
    @property
    def CircleDivision(self) -> int:
        """Number the circle segments in case of a circular cross section"""
    @CircleDivision.setter
    def CircleDivision(self, circleDivision: int) -> None:
        """Set the circle division

        Args:
            circleDivision: Circle division
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, comProp: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties

        Args:
            comProp: Common properties
        """
    @property
    def FaceStyle(self) -> int:
        """Get the face style ID
        """
    @FaceStyle.setter
    def FaceStyle(self, faceStyleID: int) -> None:
        """Set the face style

        Args:
            faceStyleID: Face style ID
        """
    @property
    def Factor(self) -> float:
        """Get the factor
        """
    @Factor.setter
    def Factor(self, factor: float) -> None:
        """Set the factor

        Args:
            factor: Factor
        """
    @property
    def Filling(self) -> int:
        """Get the filling ID
        """
    @Filling.setter
    def Filling(self, fillingID: int) -> None:
        """Set the filling

        Args:
            fillingID: Filling ID
        """
    @property
    def Hatch(self) -> int:
        """Get the hatch ID
        """
    @Hatch.setter
    def Hatch(self, hatchID: int) -> None:
        """Set the hatch

        Args:
            hatchID: Hatch ID
        """
    @property
    def Material(self) -> str:
        """Get the material
        """
    @Material.setter
    def Material(self, material: str) -> None:
        """Set the material

        Args:
            material: Material
        """
    @property
    def Name(self) -> str:
        """Get the name
        """
    @Name.setter
    def Name(self, name: str) -> None:
        """Set the name

        Args:
            name: Name
        """
    @property
    def Pattern(self) -> int:
        """Get the pattern ID
        """
    @Pattern.setter
    def Pattern(self, patternID: int) -> None:
        """Set the pattern

        Args:
            patternID: Pattern ID
        """
    @property
    def PlaneReferences(self) -> PlaneReferences:
        """Get the plane references
        """
    @PlaneReferences.setter
    def PlaneReferences(self, planeRef: PlaneReferences) -> None:
        """Set the plane references

        Args:
            planeRef: Plane references
        """
    @property
    def Priority(self) -> int:
        """Get the priority
        """
    @Priority.setter
    def Priority(self, priority: int) -> None:
        """Set the priority

        Args:
            priority: Priority
        """
    @property
    def Status(self) -> int:
        """Get the Status ID
        """
    @Status.setter
    def Status(self, statusID: int) -> None:
        """Set the Status ID

        Args:
            statusID: Status ID
        """
    @property
    def Surface(self) -> str:
        """Get the surface name and path
        """
    @Surface.setter
    def Surface(self, surface: str) -> None:
        """Set the surface

        Args:
            surface: Surface
        """
    @property
    def SurfaceElementProperties(self) -> SurfaceElementProperties:
        """Get the surface element properties
        """
    @SurfaceElementProperties.setter
    def SurfaceElementProperties(self, surfaceElementProp: SurfaceElementProperties) -> None:
        """Set the surface element properties

        Args:
            surfaceElementProp: surface element properties
        """
    @property
    def Trade(self) -> int:
        """Trade index according to the definition of the enumeration attribute _trade_ (@209@)"""
    @Trade.setter
    def Trade(self, value: int) -> None:
        """Set the trade

        Args:
            value: Trade index
        """

class ArchElement(NemAll_Python_BasisElements.AllplanElement):
    """Abstract base class representing all architectural components"""
    def GetConnectionUUID(self) -> NemAll_Python_IFW_ElementAdapter.GUID:
        """Get the connection UUID

        Returns:
            Connection UUID
        """
    def SetConnectionUUID(self, connectionGuid: NemAll_Python_IFW_ElementAdapter.GUID):
        """Set the connection UUID

        Args:
            connectionGuid: Connection UUID
        """
    @property
    def ConnectionUUID(self) -> NemAll_Python_IFW_ElementAdapter.GUID:
        """Get the connection UUID
        """
    @ConnectionUUID.setter
    def ConnectionUUID(self, connectionGuid: NemAll_Python_IFW_ElementAdapter.GUID) -> None:
        """Set the connection UUID

        Args:
            connectionGuid: Connection UUID
        """

class ArchitectureElementsGeometryService():
    """Implementation of the architecture elements geometry service
    """
    @staticmethod
    def CreatePlacementArc(element: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, elementAxis: NemAll_Python_Geometry.Arc2D,
                           placementPnt: NemAll_Python_Geometry.Point2D, directionPnt: NemAll_Python_Geometry.Point2D) -> tuple[NemAll_Python_Geometry.Arc2D, bool]:
        """Create a placement arc at the placement point

        Args:
            element:      Element
            elementAxis:  Element axis
            placementPnt: Placement point
            directionPnt: Direction point

        Returns:
            Placement arc, placement a bottom/top (true/false)
        """
    @staticmethod
    def GetOpeningOffsetPoints(parentEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                               openingStartPnt: NemAll_Python_Geometry.Point2D, openingEndPnt: NemAll_Python_Geometry.Point2D) -> tuple[bool, NemAll_Python_Geometry.Point2D, NemAll_Python_Geometry.Point2D]:
        """Get the offset points for the opening

        Args:
            parentEle:       Parent element of the opening
            openingStartPnt: Start point of the opening
            openingEndPnt:   End point of the opening

        Returns:
            Offset point for the opening
        """
    @staticmethod
    def GetOuterPolyline(elementPolygon: NemAll_Python_Geometry.Polygon2D, refLine: NemAll_Python_Geometry.Line2D,
                         elementAxis: object) -> NemAll_Python_Geometry.Polyline2D:
        """Get the outer polyline from a curved element located at the reference line

        Args:
            elementPolygon: Polygon of the curved element
            refLine:        Reference line of the polyline
            elementAxis:    Axis of the element

        Returns:
            Outer polyline
        """
    @staticmethod
    def GetOutlineSegmentAndPoint(element: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                  refPoint: NemAll_Python_Geometry.Point2D) -> tuple[NemAll_Python_Geometry.Line2D, NemAll_Python_Geometry.Point2D, NemAll_Python_IFW_ElementAdapter.BaseElementAdapter]:
        """Get the outline segment and point related to the reference point

        Args:
            element:  Element
            refPoint: Reference point

        Returns:
            Outline segment, point and element
        """
    @staticmethod
    def IsOpeningPlacementAtFirstTier(openingPlacementEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                      openingStartPnt: NemAll_Python_Geometry.Point2D, openingEndPnt: NemAll_Python_Geometry.Point2D) -> bool:
        """Get the placement state of the opening

        Args:
            openingPlacementEle: GUID of the placement element
            openingStartPnt:     Start point of the opening
            openingEndPnt:       End point of the opening

        Returns:
            Opening placement is located at first tier state
        """
    @staticmethod
    def SelectTier(parentEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                   selectionPoint: NemAll_Python_Geometry.Point2D) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Selecte a tier

        Args:
            parentEle:      Parent element
            selectionPoint: Selection point

        Returns:
            Selected tier
        """

class AxisProperties():
    """Properties of the axis of a linear architectural component (beam, wall, etc.).

    These properties describe the **position** of the axis in relation to the architectural
    component.

    """
    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """
    @property
    def Distance(self) -> float:
        """Offset distance between the axis and the **outer** side of the architectural component.

        **IMPORTANT**: The value must be set in the range between <0.0 , component_width>
        """
    @Distance.setter
    def Distance(self, value: float) -> None:
        """Set the distance

        Args:
            value: Distance
        """
    @property
    def Extension(self) -> int:
        """Defines, on which side of the axis to generate the architectural component (or its tiers).

        Assuming the axis origins in (0,0) and points in **X+ direction**, setting the value to:

        -   **1** will result in the architectural component being **above** the axis (on +Y side)
        -   **-1** will result in the architectural component being **below** the axis (on -Y side)

        **IMPORTANT**: Default value is 0 and must be changed to either 1 or -1!
        """
    @Extension.setter
    def Extension(self, value: int) -> None:
        """Set the extension

        Args:
            value:   Extension
        """
    @property
    def Modus(self) -> int:
        """Get the modus
        """
    @Modus.setter
    def Modus(self, value: int) -> None:
        """Set the modus

        Args:
            value:   Modus
        """
    @property
    def OnTier(self) -> int:
        """Get the axis tier
        """
    @OnTier.setter
    def OnTier(self, onTier: int) -> None:
        """Set the axis tier

        Args:
            onTier:  Axis tier
        """
    @property
    def Position(self) -> int:
        """Position of the axis relative to the architectural component.

        **IMPORTANT**: When setting this property, remember to set the _Distance_ accordingly!
        Otherwise, the architectural component may behave unexpectedly when being modified.
        """
    @Position.setter
    def Position(self, position: int) -> None:
        """Set the axis position

        Args:
            position:    Axis position
        """

class BasePlaneReferences():

    """Base class for the plane references"""
    def __init__(self):
        """Initialize
        """

class BeamElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of the upstand/downstand beam
    """
    def GetProperties(self) -> BeamProperties:
        """Get the beam properties

        Returns:
            Beam properties
        """
    def SetProperties(self, beamProp: BeamProperties):
        """Set the beam properties

        Args:
            beamProp: Beam properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, beamProp: BeamProperties, axis: object):
        """Constructor

        Args:
            beamProp: Beam properties
            axis:     Axis
        """
    @typing.overload
    def __init__(self, element: BeamElement):
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
    @property
    def Properties(self) -> BeamProperties:
        """Properties of the beam"""
    @Properties.setter
    def Properties(self, beamProp: BeamProperties) -> None:
        """Set the beam properties

        Args:
            beamProp: Beam properties
        """

class BeamProperties(ArchBaseProperties):
    """Representation of the properties of an upstand/downstand beam
    """
    def GetAxis(self) -> AxisProperties:
        """Get the axis

        Returns:
            axis  Axis data
        """
    def GetProfileFullName(self) -> str:
        """Get the Profile Full Name

        Returns:
            str ProfileFullName
        """
    def GetShapeType(self) -> ShapeType:
        """Get the type of the cross-section shape

        Returns:
            Shape type
        """
    def GetWidth(self) -> float:
        """Get the width of the rectangular cross-section shape

        Returns:
            Width
        """
    def SetAttribute(self, attrib: object):
        """Set the attribute

        Args:
            attrib: Attribute
        """
    def SetAxis(self, axis: AxisProperties):
        """Set the axis

        Args:
            axis: Axis data
        """
    def SetProfileFullName(self, str: str):
        """Set the Profile Full Name

        Args:
            str:ProfileFullName
        """
    def SetShapeType(self, shapeType: ShapeType):
        """Set the type of the cross-section shape

        Args:
            shapeType: Shape type 
        """
    def SetWidth(self, width: float):
        """Set the width of the rectangular cross-section shape

        Args:
            width: Width 
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, beamProp: BeamProperties):
        """Copy constructor

        Args:
            beamProp: Beam properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def IsStartNewJoinedBeamGroup(self) -> bool:
        """Should this beam be the first of a new group of beams joined together

        Set this property to **False** in the second or subsequent beams in order
        to join all of them with each other at their ends to create a continous chain of beams.
        """
    @IsStartNewJoinedBeamGroup.setter
    def IsStartNewJoinedBeamGroup(self, startNewJoinedBeamGroup: bool) -> None:
        """Set the state for starting a new joined beam group.
        All beams in a group are used for to create a continues join
        between the beams.

        Args:
            startNewJoinedBeamGroup: Start new beam group
        """
    @property
    def ProfileFullName(self) -> str:
        """Get Profile Full Name
        """
    @ProfileFullName.setter
    def ProfileFullName(self, str: str) -> None:
        """Set Profile Full Name

        Args:
            str: ProfileFullName
        """
    @property
    def ShapeType(self) -> ShapeType:
        """Type of the cross-section shape"""
    @ShapeType.setter
    def ShapeType(self, shapeType: ShapeType) -> None:
        """Set the type of the shape

        Args:
            shapeType: Shape type
        """
    @property
    def Width(self) -> float:
        """Width of the rectangular cross-section shape"""
    @Width.setter
    def Width(self, width: float) -> None:
        """Set the width

        Args:
            width: Width
        """

class BlockFoundationElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the Block Foundation element
    """
    def GetPlacementPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the Block Foundation placement point

        Returns:
            Block Foundation placement point
        """
    def GetProperties(self) -> BlockFoundationProperties:
        """Get the Block Foundation properties

        Returns:
            Block Foundation properties
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetPlacementPoint(self, placementPoint: NemAll_Python_Geometry.Point2D):
        """Args:
            placementPoint
        """
    def SetProperties(self, BlockFoundationProp: BlockFoundationProperties):
        """Set the Block Foundation properties

        Args:
            BlockFoundationProp: Block Foundation properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, BlockFoundationProp: BlockFoundationProperties, placementPoint: object):
        """Constructor

        Args:
            BlockFoundationProp: Block Foundation properties
            placementPoint:      Placement point
        """
    @typing.overload
    def __init__(self, element: BlockFoundationElement):
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
    @property
    def PlacementPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the Block Foundation placement point
        """
    @property
    def Properties(self) -> BlockFoundationProperties:
        """Get the Block Foundation properties
        """
    @Properties.setter
    def Properties(self, BlockFoundationProp: BlockFoundationProperties) -> None:
        """Set the Block Foundation properties

        Args:
            BlockFoundationProp: Block Foundation properties
        """

class VerticalElementProperties(ArchBaseProperties):
    """Base class representing properties of vertical architectural components, such as columns.
    """
    def GetAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get the angle

        Returns:
            Get angle
        """
    def GetDepth(self) -> float:
        """Get the depth

        Returns:
            Depth
        """
    def GetProfileFullName(self) -> str:
        """Get the full name of the profile

        Returns:
            Path and name of the profile
        """
    def GetRadius(self) -> float:
        """Get the radius

        Returns:
            Radius
        """
    def GetShapePolygon(self) -> NemAll_Python_Geometry.Polygon2D:
        """Get the shape polygon

        Returns:
            Shape polygon
        """
    def GetShapeType(self) -> ShapeType:
        """Get the shape type

        Returns:
            Shape type
        """
    def GetWidth(self) -> float:
        """Get the width

        Returns:
            Width
        """
    def SetAngle(self, angle: NemAll_Python_Geometry.Angle):
        """Set the angle

        Args:
            angle: Angle
        """
    def SetAttribute(self, attrib: object):
        """Set the attribute

        Args:
            attrib: Attribute
        """
    def SetCornerRadius(self, radius: float):
        """Set the corner radius

        Args:
            radius: Corner radius
        """
    def SetDepth(self, depth: float):
        """Set the depth

        Args:
          depth:  Depth
        """
    def SetProfileFullName(self, fullName: str):
        """Set the full name of the profile

        Args:
            fullName: Path and name of the profile
        """
    def SetRadius(self, radius: float):
        """Set the radius

        Args:
            radius: Radius
        """
    def SetShapePolygon(self, shapePol: NemAll_Python_Geometry.Polygon2D):
        """Set the shape polygon

        Args:
            shapePol: Shape polygon
        """
    def SetShapeType(self, shapeType: ShapeType):
        """Set the type of the shape

        Args:
            shapeType: Shape type
        """
    def SetSize(self, width: float, depth: float):
        """Set the size of the element

        Args:
            width: Width
            depth: Depth
        """
    def SetWidth(self, width: float):
        """Set the width

        Args:
            width:  Width
        """
    def __init__(self, element: VerticalElementProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def Angle(self) -> NemAll_Python_Geometry.Angle:
        """Get the angle
        """
    @Angle.setter
    def Angle(self, angle: NemAll_Python_Geometry.Angle) -> None:
        """Set the angle

        Args:
            angle: Angle
        """
    @property
    def Depth(self) -> float:
        """Get the depth
        """
    @Depth.setter
    def Depth(self, depth: float) -> None:
        """Set the depth

        Args:
            depth: Set the depth
        """
    @property
    def ProfileFullName(self) -> str:
        """Get the full name of the profile
        """
    @ProfileFullName.setter
    def ProfileFullName(self, fullName: str) -> None:
        """Set the full name of the profile

        Args:
            fullName: Path and name of the profile
        """
    @property
    def Radius(self) -> float:
        """Get the radius
        """
    @Radius.setter
    def Radius(self, radius: float) -> None:
        """Set the radius

        Args:
            radius: Radius
        """
    @property
    def ShapePolygon(self) -> NemAll_Python_Geometry.Polygon2D:
        """Get the shape polygon
        """
    @ShapePolygon.setter
    def ShapePolygon(self, shapePol: NemAll_Python_Geometry.Polygon2D) -> None:
        """Set the shape polygon

        Args:
            shapePol: Shape polygon
        """
    @property
    def ShapeType(self) -> ShapeType:
        """Get the shape type
        """
    @ShapeType.setter
    def ShapeType(self, shapeType: ShapeType) -> None:
        """Set the type of the shape

        Args:
            shapeType: Shape type
        """
    @property
    def Width(self) -> float:
        """Get the width
        """
    @Width.setter
    def Width(self, width: float) -> None:
        """Set the width

        Args:
            width: Width
        """

class BottomTopPlaneService():
    """Service providing methods for reading various properties of the reference planes set in the current document.
    """
    @staticmethod
    def GetAbsoluteBottomElevation(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                   doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeProp: BasePlaneReferences) -> float:
        """Get the absolute elevation of the bottom plane

        Args:
            refElement: Reference element (empty element if not exist)
            doc:        Document
            planeProp:  Plane properties

        Returns:
            Absolute elevation of the bottom plane
        """
    @staticmethod
    def GetAbsoluteTopElevation(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeProp: BasePlaneReferences) -> float:
        """Get the absolute elevation of the top plane

        Args:
            refElement: Reference element (empty element if not exist)
            doc:        Document
            planeProp:  Plane properties

        Returns:
            Absolute elevation of the top plane
        """
    @staticmethod
    def GetBottomReferencePlane(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeProp: BasePlaneReferences) -> (NemAll_Python_Geometry.BRep3D | NemAll_Python_Geometry.Polyhedron3D | NemAll_Python_Geometry.Plane3D):
        """Get the bottom reference plane

        Args:
            refElement: Reference element (empty element if not exist)
            doc:        Document
            planeProp:  Plane properties

        Returns:
            Bottom reference plane as Plan3D, BRep3D or Polyhedron3D
        """
    @staticmethod
    def GetDocumentBottomElevation(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                   doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeProp: BasePlaneReferences) -> float:
        """Get the document elevation of the bottom plane

        Args:
            refElement: Reference element (empty element if not exist)
            doc:        Document
            planeProp:  Plane properties

        Returns:
            Absolute elevation of the bottom plane
        """
    @staticmethod
    def GetDocumentDefaultPlanes(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> tuple[NemAll_Python_Geometry.Plane3D,
                                 NemAll_Python_Geometry.Plane3D]:
        """Get the default bottom and top plane of the document

        Args:
            doc:    Document

        Returns:
            Default bottom plane
            Default top plane
        """
    @staticmethod
    def GetDocumentTopElevation(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeProp: BasePlaneReferences) -> float:
        """Get the document elevation of the top plane

        Args:
            refElement: Reference element (empty element if not exist)
            doc:        Document
            planeProp:  Plane properties

        Returns:
            Absolute elevation of the top plane
        """
    @staticmethod
    def GetTopReferencePlane(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                             doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeProp: BasePlaneReferences) -> (NemAll_Python_Geometry.BRep3D | NemAll_Python_Geometry.Polyhedron3D | NemAll_Python_Geometry.Plane3D):
        """Get the top reference plane

        Args:
            refElement: Reference element (empty element if not exist)
            doc:        Document
            planeProp:  Plane properties

        Returns:
            Bottom reference plane as Plan3D, BRep3D or Polyhedron3D
        """

class CircularShape():
    """Representation of a circular cross section  of a structural framing element
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: CircularShape):
        """Constructor

        Args:
            value: Circular shape
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Radius(self) -> None:
        """Radius of the cross section"""

class ColumnElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of the architectural column
    """
    def GetPlacementPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the placement point

        Returns:
            Placement point
        """
    def GetProperties(self) -> ColumnProperties:
        """Get the Column properties

        Returns:
            Column properties
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetPlacementPoint(self, placementPoint: NemAll_Python_Geometry.Point2D):
        """Set the placement point

        Args:
            placementPoint: Placement point
        """
    def SetProperties(self, ColumnProp: ColumnProperties):
        """Set the Column properties

        Args:
            ColumnProp: Column properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, columnProp: ColumnProperties, placementPoint: object):
        """Constructor

        Args:
            columnProp:     Column properties
            placementPoint: Placement point
        """
    @typing.overload
    def __init__(self, element: ColumnElement):
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
    @property
    def PlacementPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the placement point
        """
    @PlacementPoint.setter
    def PlacementPoint(self, placementPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the placement point

        Args:
            placementPoint: Placement point
        """
    @property
    def Properties(self) -> ColumnProperties:
        """Get the Column properties
        """
    @Properties.setter
    def Properties(self, ColumnProp: ColumnProperties) -> None:
        """Set the Column properties

        Args:
            ColumnProp: Column properties
        """

class ColumnProperties(VerticalElementProperties, ArchBaseProperties):
    """Implementation of the Column properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, columnProp: ColumnProperties):
        """Copy constructor

        Args:
            columnProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class CustomBoxPoint(enum.Enum):
    """Enumeration of possible anchor points of structural framing elements
    """
    Center = 5
    CenterOfGravity = 10
    LeftBottom = 1
    LeftTop = 4
    MiddleBottom = 6
    MiddleLeft = 9
    MiddleRight = 7
    MiddleTop = 8
    RightBottom = 2
    RightTop = 3

    names = {LeftBottom: LeftBottom,
             RightBottom: RightBottom,
             RightTop: RightTop,
             LeftTop: LeftTop,
             Center: Center,
             MiddleBottom: MiddleBottom,
             MiddleRight: MiddleRight,
             MiddleTop: MiddleTop,
             MiddleLeft: MiddleLeft,
             CenterOfGravity: CenterOfGravity}

    values = {1: LeftBottom,
              2: RightBottom,
              3: RightTop,
              4: LeftTop,
              5: Center,
              6: MiddleBottom,
              7: MiddleRight,
              8: MiddleTop,
              9: MiddleLeft,
              10: CenterOfGravity}

    def __getitem__(self, key: (str | int | float)) -> CustomBoxPoint:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class DoorOpeningElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of door opening
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, openingProp: DoorOpeningProperties, generalEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                 startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D, drawPlacementPreview: bool):
        """Constructor

        Args:
            openingProp:          Opening properties
            generalEle:           General element which includes the opening
            startPnt:             Start point of the opening
            endPnt:               End point
            drawPlacementPreview: Draw as placement preview (no wall adaptions) state
        """
    @typing.overload
    def __init__(self, element: DoorOpeningElement):
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
    @property
    def EndPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the end point
        """
    @EndPoint.setter
    def EndPoint(self, endPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the end point

        Args:
            endPoint: End point
        """
    @property
    def Properties(self) -> DoorOpeningProperties:
        """Door opening properties"""
    @Properties.setter
    def Properties(self, DoorOpeningProp: DoorOpeningProperties) -> None:
        """Set the DoorOpening properties

        Args:
            DoorOpeningProp: General opening properties
        """
    @property
    def StartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the start point
        """
    @StartPoint.setter
    def StartPoint(self, startPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the start point

        Args:
            startPoint: Start point
        """

class DoorOpeningProperties():
    """Properties of door opening
    """
    def GetDoorSwingProperties(self) -> DoorSwingProperties:
        """Get a reference of the door swing properties

        Returns:
            Door swing properties reference
        """
    def GetGeometryProperties(self) -> VerticalOpeningGeometryProperties:
        """Get a reference of the geometry properties

        Returns:
            Geometry properties reference
        """
    def GetOpeningSymbolsProperties(self) -> OpeningSymbolsProperties:
        """Get a reference of the opening symbols properties

        Returns:
            Opening symbols properties reference
        """
    def GetRevealProperties(self) -> VerticalOpeningRevealProperties:
        """Get a reference of the reveal properties

        Returns:
            Reveal properties reference
        """
    def GetSillProperties(self) -> VerticalOpeningSillProperties:
        """Get a reference of the sill properties

        Returns:
            Sill properties reference
        """
    def GetTierOffsetProperties(self) -> VerticalOpeningTierOffsetProperties:
        """Get a reference of the tier offset properties

        Returns:
            Tier offset properties reference
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, doorProp: DoorOpeningProperties):
        """Copy constructor

        Args:
            doorProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def FrenchDoor(self) -> bool:
        """Get the french door attribute state
        """
    @FrenchDoor.setter
    def FrenchDoor(self, isFrenchDoor: bool) -> None:
        """Set the french door state

        Args:
            isFrenchDoor: French door state
        """
    @property
    def Independent2DInteraction(self) -> bool:
        """Set to True, when the opening is above/below the section plane and should therefor NOT interact with the hatching/filling of the parent architectural element in ground view. Defaults to False."""
    @Independent2DInteraction.setter
    def Independent2DInteraction(self, isIndependent2DInteraction: bool) -> None:
        """Set the independent 2D interaction state

        Args:
            isIndependent2DInteraction: Independent 2D interaction state
        """
    @property
    def PlaneReferences(self) -> PlaneReferences:
        """Get the plane references
        """
    @PlaneReferences.setter
    def PlaneReferences(self, planeRef: PlaneReferences) -> None:
        """Set the plane references

        Args:
            planeRef: Plane references
        """

class DoorSwingProperties():
    """Implementation of the door swing properties
    """
    def __init__(self, element: DoorSwingProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def Angle(self) -> float:
        """Get the Angle
        """
    @Angle.setter
    def Angle(self, angle: float) -> None:
        """Set the angle

        Args:
            angle: Angle
        """
    @property
    def BasePointIndex(self) -> int:
        """Get the base point index
        """
    @BasePointIndex.setter
    def BasePointIndex(self, basePointIndex: int) -> None:
        """Set the base point index

        Args:
            basePointIndex: Base point index
        """
    @property
    def LeafThickness(self) -> float:
        """Get the leaf thickness
        """
    @LeafThickness.setter
    def LeafThickness(self, leafThickness: float) -> None:
        """Set the leaf thickness

        Args:
            leafThickness: Leaf thickness
        """
    @property
    def Type(self) -> DoorSwingType:
        """Get the swing type
        """
    @Type.setter
    def Type(self, type: DoorSwingType) -> None:
        """Set the swing type

        Args:
            type: Swing type
        """

class DoorSwingType(enum.Enum):
    """Type of the door swing
    """
    eBiFold = 19
    eDoubleOppositeSwingCircular = 5
    """Revolving door, two leaves, opposite (arc)"""
    eDoubleOppositeSwingLinear = 6
    """Revolving door, two leaves, opposite (diagonal)"""
    eDoubleSwingCircular = 3
    """Revolving door, two leaves (arc)"""
    eDoubleSwingLinear = 4
    """Revolving door, two leaves (diagonal)"""
    eFolding = 18
    """Folding door"""
    eLifting = 27
    """Lifting door"""
    eLiftingSingleSwingCircular = 11
    """Lifting revolving door (arc)"""
    eLiftingSingleSwingLinear = 12
    """Lifting revolving door (diagonal)"""
    eLiftingSliding = 16
    """Lift and slide door"""
    eNone = 0
    """None"""
    eOneSidedDoubleRevolving = 23
    """Double revolving door, single-sided"""
    eOneSidedRevolving = 21
    """Revolving door, single-sided"""
    eOneSidedSwingOptional = 25
    """Up and over door, single-sided (optional)"""
    ePendulumDoubleSwingCircular = 9
    """Swing door, two leaves (arc)"""
    ePendulumDoubleSwingLinear = 10
    """Swing door, two leaves (diagonal)"""
    ePendulumSingleSwingCircular = 7
    """Swing door, one leaf (arc)"""
    ePendulumSingleSwingLinear = 8
    """Swing door, one leaf (diagonal)"""
    eRevolving = 17
    """Turnstile door"""
    eSingleSwingCircular = 1
    """Revolving door, one leaf (arc)"""
    eSingleSwingLinear = 2
    """Revolving door, one leaf (diagonal)"""
    eSliding = 15
    eSlidingDoubleSwing = 14
    """Sliding door, two leaves"""
    eSlidingSingleSwing = 13
    """Sliding door, one leaf"""
    eSwing = 20
    """Up and over door"""
    eTwoSidedDoubleRevolving = 24
    """Double revolving door, double-sided"""
    eTwoSidedFolding = 28
    """Folding door double-sided"""
    eTwoSidedRevolving = 22
    """Revolving door, double-sided"""
    eTwoSidedSwingOptional = 26
    """Up and over door, double-sided (optional)"""

    names = {eNone: eNone,
             eSingleSwingCircular: eSingleSwingCircular,
             eSingleSwingLinear: eSingleSwingLinear,
             eDoubleSwingCircular: eDoubleSwingCircular,
             eDoubleSwingLinear: eDoubleSwingLinear,
             eDoubleOppositeSwingCircular: eDoubleOppositeSwingCircular,
             eDoubleOppositeSwingLinear: eDoubleOppositeSwingLinear,
             ePendulumSingleSwingCircular: ePendulumSingleSwingCircular,
             ePendulumSingleSwingLinear: ePendulumSingleSwingLinear,
             ePendulumDoubleSwingCircular: ePendulumDoubleSwingCircular,
             ePendulumDoubleSwingLinear: ePendulumDoubleSwingLinear,
             eLiftingSingleSwingCircular: eLiftingSingleSwingCircular,
             eLiftingSingleSwingLinear: eLiftingSingleSwingLinear,
             eSlidingSingleSwing: eSlidingSingleSwing,
             eSlidingDoubleSwing: eSlidingDoubleSwing,
             eSliding: eSliding,
             eLiftingSliding: eLiftingSliding,
             eRevolving: eRevolving,
             eFolding: eFolding,
             eBiFold: eBiFold,
             eSwing: eSwing,
             eOneSidedRevolving: eOneSidedRevolving,
             eTwoSidedRevolving: eTwoSidedRevolving,
             eOneSidedDoubleRevolving: eOneSidedDoubleRevolving,
             eTwoSidedDoubleRevolving: eTwoSidedDoubleRevolving,
             eOneSidedSwingOptional: eOneSidedSwingOptional,
             eTwoSidedSwingOptional: eTwoSidedSwingOptional,
             eLifting: eLifting,
             eTwoSidedFolding: eTwoSidedFolding}

    values = {0: eNone,
              1: eSingleSwingCircular,
              2: eSingleSwingLinear,
              3: eDoubleSwingCircular,
              4: eDoubleSwingLinear,
              5: eDoubleOppositeSwingCircular,
              6: eDoubleOppositeSwingLinear,
              7: ePendulumSingleSwingCircular,
              8: ePendulumSingleSwingLinear,
              9: ePendulumDoubleSwingCircular,
              10: ePendulumDoubleSwingLinear,
              11: eLiftingSingleSwingCircular,
              12: eLiftingSingleSwingLinear,
              13: eSlidingSingleSwing,
              14: eSlidingDoubleSwing,
              15: eSliding,
              16: eLiftingSliding,
              17: eRevolving,
              18: eFolding,
              19: eBiFold,
              20: eSwing,
              21: eOneSidedRevolving,
              22: eTwoSidedRevolving,
              23: eOneSidedDoubleRevolving,
              24: eTwoSidedDoubleRevolving,
              25: eOneSidedSwingOptional,
              26: eTwoSidedSwingOptional,
              27: eLifting,
              28: eTwoSidedFolding}

    def __getitem__(self, key: (str | int | float)) -> DoorSwingType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ElementConverter():
    """Utility providing methods for conversion of architectural components
    """
    @staticmethod
    def ConvertToUDElement(elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Create user defined elements (U-D element) from 3D objects

        Args:
            elements:    Element adapters pointing to the 3D objects to convert

        Returns:
            Element adapters pointing to the converted 3D objects
        """
    def __init__(self):
        """Initialize
        """

class FlushPierElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the FlushPier element
    """
    def GetEndPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the End Point

        Returns:
            End Point
        """
    def GetProperties(self) -> FlushPierProperties:
        """Get the FlushPier properties

        Returns:
            FlushPier properties
        """
    def GetStartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the Start Point

        Returns:
            Start Point
        """
    def SetProperties(self, FlushPierProp: FlushPierProperties):
        """Set the FlushPier properties

        Args:
            FlushPierProp: FlushPier properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, flushPierProp: FlushPierProperties, generalEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                 startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D, drawPlacementPreview: bool):
        """Constructor

        Args:
            flushPierProp:        FlushPier properties
            generalEle:           General element which includes the FlushPier
            startPnt:             Start point of the FlushPier
            endPnt:               End point of the FlushPier
            drawPlacementPreview: Draw a placement preview (no general element adaption) state
        """
    @typing.overload
    def __init__(self, element: FlushPierElement):
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
    @property
    def Properties(self) -> FlushPierProperties:
        """Get the FlushPier properties
        """
    @Properties.setter
    def Properties(self, FlushPierProp: FlushPierProperties) -> None:
        """Set the FlushPier properties

        Args:
            FlushPierProp: FlushPier properties
        """

class FlushPierProperties(ArchBaseProperties):
    """Implementation of the FlushPier properties
    """
    def GetWidth(self) -> float:
        """Get the width of the Flush Pier

        Returns:
            Width of the Flush Pier
        """
    def SetWidth(self, width: float):
        """Set the width of the Flush Pier

        Args:
            width: Width of the Flush Pier
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, flushPierProp: FlushPierProperties):
        """Copy constructor

        Args:
            flushPierProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Width(self) -> float:
        """Get the width of the Flush Pier
        """
    @Width.setter
    def Width(self, width: float) -> None:
        """Set the width of the Flush Pier

        Args:
            width: Width of the Flush Pier
        """

class GeneralOpeningElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of (polygonal) niche, recess, slit or opening.
    """
    @typing.overload
    def __init__(self):
        """Initialize with default values
        """
    @typing.overload
    def __init__(self, wallOpeningProp: GeneralOpeningProperties, generalEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                 startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D, drawPlacementPreview: bool):
        """Constructor

        Args:
            wallOpeningProp:      Opening properties
            generalEle:           General element which includes the opening
            startPnt:             Start point of the opening
            endPnt:               End point
            drawPlacementPreview: Draw a placement preview (no general element adaption) state
        """
    @typing.overload
    def __init__(self, wallOpeningProp: GeneralOpeningProperties, generalEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                 groundPlanePolygon: NemAll_Python_Geometry.Polygon2D, drawPlacementPreview: bool):
        """Constructor

        Args:
            wallOpeningProp:      Opening properties
            generalEle:           General element which includes the opening
            groundPlanePolygon:   Ground plan polygon
            drawPlacementPreview: Draw a placement preview (no general element adaption) state
        """
    @typing.overload
    def __init__(self, element: GeneralOpeningElement):
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
    @property
    def EndPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the end point
        """
    @EndPoint.setter
    def EndPoint(self, endPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the end point

        Args:
            endPoint: End point
        """
    @property
    def GroundPlanePolygon(self) -> NemAll_Python_Geometry.Polygon2D:
        """Get the ground plane polygon
        """
    @GroundPlanePolygon.setter
    def GroundPlanePolygon(self, groundPlanePolygon: NemAll_Python_Geometry.Polygon2D) -> None:
        """Set the ground plane polygon

        Args:
            groundPlanePolygon: Ground plane polygon
        """
    @property
    def Properties(self) -> GeneralOpeningProperties:
        """Opening properties"""
    @Properties.setter
    def Properties(self, GeneralOpeningProp: GeneralOpeningProperties) -> None:
        """Set the GeneralOpening properties

        Args:
            GeneralOpeningProp: General opening properties
        """
    @property
    def StartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the start point
        """
    @StartPoint.setter
    def StartPoint(self, startPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the start point

        Args:
            startPoint: Start point
        """

class GeneralOpeningProperties():
    """Properties of a regular or polygonal niche, recess, slit or opening
    """
    def GetGeometryProperties(self) -> VerticalOpeningGeometryProperties:
        """Get a reference of the geometry properties

        Returns:
            Geometry properties reference
        """
    def GetOpeningSymbolsProperties(self) -> OpeningSymbolsProperties:
        """Get a reference of the opening symbols properties

        Returns:
            Opening symbols properties reference
        """
    def GetSillProperties(self) -> VerticalOpeningSillProperties:
        """Get a reference of the sill properties

        Returns:
            Sill properties reference
        """
    @typing.overload
    def __init__(self, openingType: OpeningType):
        """Constructor

        Args:
            openingType: Opening type
        """
    @typing.overload
    def __init__(self, openingProp: GeneralOpeningProperties):
        """Copy constructor

        Args:
            openingProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Independent2DInteraction(self) -> bool:
        """Set to True, when the opening is above/below the section plane and should therefor NOT interact with the hatching/filling of the parent architectural element in ground view. Defaults to False."""
    @Independent2DInteraction.setter
    def Independent2DInteraction(self, isIndependent2DInteraction: bool) -> None:
        """Set the independent 2D interaction state

        Args:
            isIndependent2DInteraction: Independent 2D interaction state
        """
    @property
    def OpeningType(self) -> OpeningType:
        """Get the type of the opening
        """
    @OpeningType.setter
    def OpeningType(self, openingType: OpeningType) -> None:
        """Set the type of the opening

        Args:
            openingType: Type of the niche
        """
    @property
    def PlaneReferences(self) -> PlaneReferences:
        """Get the plane references
        """
    @PlaneReferences.setter
    def PlaneReferences(self, planeRef: PlaneReferences) -> None:
        """Set the plane references

        Args:
            planeRef: Plane references
        """
    @property
    def VisibleInViewSection3D(self) -> bool:
        """When set to False, the opening does NOT cut out the 3D model element of the parent architectural component (hence opening is invisible in UVSs). Relevant for recess only! Defaults to True."""
    @VisibleInViewSection3D.setter
    def VisibleInViewSection3D(self, isVisibleInViewSection3D: bool) -> None:
        """Set the visible in view/section/3D model state

        Args:
            isVisibleInViewSection3D: Visible in view/section/3D model state
        """

class JointElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the Joint element
    """
    def GetEndPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Set the End Point
        """
    def GetProperties(self) -> JointProperties:
        """Get the Joint properties

        Returns:
            Joint properties
        """
    def GetStartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the Start Point

        Returns:
            Start Point
        """
    def SetProperties(self, JointProp: JointProperties):
        """Set the Joint properties

        Args:
            JointProp: Joint properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, jointProp: JointProperties, generalEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                 startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D, drawPlacementPreview: bool):
        """Constructor

        Args:
            jointProp:            Joint properties
            generalEle:           General element which includes the Joint
            startPnt:             Start point of the Joint
            endPnt:               End point of the Joint
            drawPlacementPreview: Draw a placement preview (no general element adaption) state
        """
    @typing.overload
    def __init__(self, element: JointElement):
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
    @property
    def Properties(self) -> JointProperties:
        """Get the Joint properties
        """
    @Properties.setter
    def Properties(self, JointProp: JointProperties) -> None:
        """Set the Joint properties

        Args:
            JointProp: Joint properties
        """

class JointProperties():
    """Implementation of the Joint properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, jointProp: JointProperties):
        """Copy constructor

        Args:
            jointProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Depth(self) -> float:
        """Get the depth of the joint
        """
    @Depth.setter
    def Depth(self, depth: float) -> None:
        """Set the depth of the joint

        Args:
            depth: Depth of the joint
        """
    @property
    def PlaneReferences(self) -> PlaneReferences:
        """Get the plane references
        """
    @PlaneReferences.setter
    def PlaneReferences(self, planeRef: PlaneReferences) -> None:
        """Set the plane references

        Args:
            planeRef: Plane references
        """
    @property
    def Width(self) -> float:
        """Get the width of the joint
        """
    @Width.setter
    def Width(self, width: float) -> None:
        """Set the width of the joint

        Args:
            width: Width of the joint
        """

class OpeningSide(enum.Enum):
    """Type of the opening side

    eInnerSide: Opening width at the inner side
    eOuterSide: Opening width at the outer side
    """
    eInnerSide = 0
    eOuterSide = 1

    names = {eInnerSide: eInnerSide,
             eOuterSide: eOuterSide}

    values = {0: eInnerSide,
              1: eOuterSide}

    def __getitem__(self, key: (str | int | float)) -> OpeningSide:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class OpeningSymbolsProperties():
    """Implementation of the opening symbols properties
    """
    def __init__(self, element: OpeningSymbolsProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def OpeningRefPntIndex(self) -> int:
        """Get the opening reference point index
        """
    @OpeningRefPntIndex.setter
    def OpeningRefPntIndex(self, openingRefPntIndex: int) -> None:
        """Set the opening reference point index

        Args:
            openingRefPntIndex: Opening reference point index
        """
    @property
    def OpeningTierIndex(self) -> int:
        """Get the opening tier index
        """
    @OpeningTierIndex.setter
    def OpeningTierIndex(self, openingTierIndex: int) -> None:
        """Set the opening tier index

        Args:
            openingTierIndex: Opening tier index
        """
    @property
    def SymbolNames(self) -> list[str]:
        """Get the symbol names
        """
    @SymbolNames.setter
    def SymbolNames(self, symbolNames: list[str]) -> None:
        """Set the symbol names

        Args:
            symbolNames: Symbol names
        """

class OpeningType(enum.Enum):
    """Type of the opening

    eNiche : Niche
    eRecess: Recess
    """
    eNiche = 0
    eRecess = 1

    names = {eNiche: eNiche,
             eRecess: eRecess}

    values = {0: eNiche,
              1: eRecess}

    def __getitem__(self, key: (str | int | float)) -> OpeningType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PlaneReferences(BasePlaneReferences):
    """Implementation of the plane references
    """
    class Direction(enum.Enum):
        """Definition of the plane directions

        eParallel  :
        eOrthogonal:
        """
        eOrthogonal = 1
        eParallel = 0

        names = {eParallel: eParallel,
                 eOrthogonal: eOrthogonal}

        values = {0: eParallel,
                  1: eOrthogonal}

        def __getitem__(self, key: (str | int | float)) -> PlaneReferences.Direction:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class ElementToPlaneModeling(enum.Enum):
        """Definition of the element to plane modelling

        eFitToPlane     :
        eLowerCutToPlane:
        eUpperCutToPlane:
        """
        eFitToPlane = 0
        eLowerCutToPlane = 1
        eUpperCutToPlane = 2

        names = {eFitToPlane: eFitToPlane,
                 eLowerCutToPlane: eLowerCutToPlane,
                 eUpperCutToPlane: eUpperCutToPlane}

        values = {0: eFitToPlane,
                  1: eLowerCutToPlane,
                  2: eUpperCutToPlane}

        def __getitem__(self, key: (str | int | float)) -> PlaneReferences.ElementToPlaneModeling:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class PlaneReferenceDependency(enum.Enum):
        """Definition of the plane dependencies

        eAbsElevation         :
        eBottomPlane          :
        eTopPlane             :
        eComponentsBottomPlane:
        eComponentsTopPlane   :
        eTopFixed             :
        eBottomFixed          :
        """
        eAbsElevation = 0
        eBottomFixed = 6
        eBottomPlane = 1
        eComponentsBottomPlane = 3
        eComponentsTopPlane = 4
        eTopFixed = 5
        eTopPlane = 2

        names = {eAbsElevation: eAbsElevation,
                 eBottomPlane: eBottomPlane,
                 eTopPlane: eTopPlane,
                 eComponentsBottomPlane: eComponentsBottomPlane,
                 eComponentsTopPlane: eComponentsTopPlane,
                 eTopFixed: eTopFixed,
                 eBottomFixed: eBottomFixed}

        values = {0: eAbsElevation,
                  1: eBottomPlane,
                  2: eTopPlane,
                  3: eComponentsBottomPlane,
                  4: eComponentsTopPlane,
                  5: eTopFixed,
                  6: eBottomFixed}

        def __getitem__(self, key: (str | int | float)) -> PlaneReferences.PlaneReferenceDependency:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def GetAbsBottomElevation(self) -> float:
        """Get the absolute bottom elevation

        Returns:
            Absolute bottom elevation
        """
    def GetAbsTopElevation(self) -> float:
        """Get the absolute top elevation

        Returns:
            Absolute top elevation
        """
    def GetBottomDirection(self) -> Direction:
        """Get the bottom direction

        Returns:
            Bottom direction
        """
    def GetBottomElevation(self) -> float:
        """Get the bottom plane elevation relative to the bottom plane of the document

        Returns:
            Bottom plane elevation
        """
    def GetBottomOffset(self) -> float:
        """Get the offset relative to the defined plane for the bottom

        Returns:
            Offset relative to the defined plane for the bottom
        """
    def GetBottomPlaneDependency(self) -> PlaneReferenceDependency:
        """Get the bottom plane dependency

        Returns:
            Bottom plane dependency
        """
    def GetBottomPlaneSurface(self) -> typing.Any:
        """Get the bottom plane surface

        Returns:
            Bottom plane surface
        """
    def GetBottomReferencePlane(self) -> ReferencePlaneID:
        """Get the bottom reference plane

        Returns:
            Bottom reference plane
        """
    def GetDocument(self) -> NemAll_Python_IFW_ElementAdapter.DocumentAdapter:
        """Get the document

        Returns:
            Document
        """
    def GetHeight(self) -> float:
        """Get the height

        Returns:
            Height
        """
    def GetMaximumHeight(self) -> float:
        """Get the maximum height

        Returns:
            Maximum height
        """
    def GetReferenceElement(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Get the reference element for the plane
        """
    def GetTopDirection(self) -> Direction:
        """Get the top direction

        Returns:
            Top direction
        """
    def GetTopElevation(self) -> float:
        """Get the top plane elevation relative to the top plane of the document

        Returns:
            Top plane elevation
        """
    def GetTopOffset(self) -> float:
        """Get the offset relative to the defined plane for the top

        Returns:
            Offset relative to the defined plane for the top
        """
    def GetTopPlaneDependency(self) -> PlaneReferenceDependency:
        """Get the top plane dependency

        Returns:
            Top plane dependency
        """
    def GetTopPlaneSurface(self) -> typing.Any:
        """Get the top plane surface

        Returns:
            Top plane surface
        """
    def GetTopReferencePlane(self) -> ReferencePlaneID:
        """Get the top reference plane

        Returns:
            Top reference plane
        """
    def SetAbsBottomElevation(self, absElevation: float):
        """Set the absolute bottom elevation

        Args:
            absElevation: Absolute bottom elevation
        """
    def SetAbsTopElevation(self, absElevation: float):
        """Set the absolute top elevation

        Args:
            absElevation: Absolute top elevation
        """
    def SetBottomDirection(self, direction: Direction):
        """Set the bottom plane Direction

        Args:
            direction: Direction
        """
    def SetBottomElevation(self, elevation: float):
        """Set the bottom plane elevation relative to the bottom plane of the document

        Args:
            elevation: Elevation
        """
    def SetBottomOffset(self, offset: float):
        """Set the offset relative to the defined plane for the bottom

        Args:
            offset: Offset relative to the defined plane for the bottom
        """
    def SetBottomPlaneDependency(self, dependency: PlaneReferenceDependency):
        """Set the bottom plane dependency

        Args:
            dependency: Dependency
        """
    def SetBottomPlaneSurface(self, bottomSurface: object):
        """Set the bottom plane surface

        Args:
            bottomSurface: Bottom plane surface
        """
    def SetBottomReferencePlane(self, bottomReferencePlane: ReferencePlaneID):
        """Set the bottom reference plane

        Args:
            bottomReferencePlane: Bottom reference plane
        """
    def SetBottomSurfacePlaneElement(self, surfacePlane: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Set the bottom surface plane

        Args:
            surfacePlane: Bottom surface plane
        """
    def SetBottomToBottom(self, planeRef: PlaneReferences):
        """Set the bottom level to the bottom level of the source plane reference

        Args:
            planeRef: Source plane reference
        """
    def SetBottomToTop(self, planeRef: PlaneReferences):
        """Set the bottom level to the top level of the source plane reference

        Args:
            planeRef: Source plane reference
        """
    def SetDocument(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Set the document

        Args:
            doc: Document
        """
    def SetElementToPlaneModeling(self, elementToPlaneModeling: ElementToPlaneModeling):
        """Set element to plane modeling

        Args:
            elementToPlaneModeling: ElementToPlaneModeling
        """
    def SetHeight(self, height: float):
        """Set the height

        Args:
            height: Height
        """
    def SetMaximumHeight(self, maximumHeight: float):
        """Set maximum height

        Args:
            maximumHeight: double
        """
    def SetReferenceElement(self, refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Set the reference element for the plane

        Args:
            refElement: Reference element
        """
    def SetTopDirection(self, direction: Direction):
        """Set the top plane Direction

        Args:
            direction: Direction
        """
    def SetTopElevation(self, elevation: float):
        """Set the top plane elevation relative to the top plane of the document

        Args:
            elevation: Elevation
        """
    def SetTopOffset(self, offset: float):
        """Set the offset relative to the defined plane for the top

        Args:
            offset: Offset relative to the defined plane for the top
        """
    def SetTopPlaneDependency(self, dependency: PlaneReferenceDependency):
        """Set the top plane dependency

        Args:
            dependency: Dependency
        """
    def SetTopPlaneSurface(self, topPlaneSurface: object):
        """Set the top plane surface

        Args:
            topPlaneSurface: Top plane surface
        """
    def SetTopReferencePlane(self, topReferencePlane: ReferencePlaneID):
        """Set the top reference plane

        Args:
            topReferencePlane: Top reference plane
        """
    def SetTopSurfacePlaneElement(self, surfacePlane: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Set the top surface plane

        Args:
            surfacePlane: Top surface plane
        """
    def SetTopToBottom(self, planeRef: PlaneReferences):
        """Set the top level to the bottom level of the source plane reference

        Args:
            planeRef: Source plane reference
        """
    def SetTopToTop(self, planeRef: PlaneReferences):
        """Set the top level to the top level of the source plane reference

        Args:
            planeRef: Source plane reference
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                 refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Constructor

        Args:
            doc:        Document
            refElement: Reference element for the plane (if current exist)
        """
    @typing.overload
    def __init__(self, element: PlaneReferences):
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
    @property
    def AbsBottomElevation(self) -> float:
        """Get the absolute bottom elevation
        """
    @AbsBottomElevation.setter
    def AbsBottomElevation(self, absElevation: float) -> None:
        """Set the absolute bottom elevation

        Args:
            absElevation: Absolute bottom elevation
        """
    @property
    def AbsTopElevation(self) -> float:
        """Get the absolute top elevation
        """
    @AbsTopElevation.setter
    def AbsTopElevation(self, absElevation: float) -> None:
        """Set the absolute top elevation

        Args:
            absElevation: Absolute top elevation
        """
    @property
    def BottomDirection(self) -> Direction:
        """Get the bottom direction
        """
    @BottomDirection.setter
    def BottomDirection(self, direction: Direction) -> None:
        """Set the bottom plane Direction

        Args:
            direction: Direction
        """
    @property
    def BottomElevation(self) -> float:
        """Get the bottom plane elevation relative to the bottom plane of the document
        """
    @BottomElevation.setter
    def BottomElevation(self, elevation: float) -> None:
        """Set the bottom plane elevation relative to the bottom plane of the document

        Args:
            elevation: Elevation
        """
    @property
    def BottomOffset(self) -> float:
        """Offset between the reference plane and the bottom edge of an architectural component.

        If the property _BottomPlaneDependency_ is set to _eAbsElevation_, this is the **absolute elevation**
        of the bottom edge.
        """
    @BottomOffset.setter
    def BottomOffset(self, offset: float) -> None:
        """Set the offset relative to the defined plane for the bottom

        Args:
            offset: Offset relative to the defined plane for the bottom
        """
    @property
    def BottomPlaneDependency(self) -> PlaneReferenceDependency:
        """Type of dependency of the bottom edge of the architectural component"""
    @BottomPlaneDependency.setter
    def BottomPlaneDependency(self, dependency: PlaneReferenceDependency) -> None:
        """Set the bottom plane dependency

        Args:
            dependency: Dependency
        """
    @property
    def BottomPlaneSurface(self) -> typing.Any:
        """Get the bottom plane surface
        """
    @BottomPlaneSurface.setter
    def BottomPlaneSurface(self, bottomSurface: typing.Any) -> None:
        """Set the bottom plane surface

        Args:
            bottomSurface: Bottom plane surface
        """
    @property
    def BottomReferencePlane(self) -> ReferencePlaneID:
        """Get the bottom reference plane
        """
    @BottomReferencePlane.setter
    def BottomReferencePlane(self, bottomReferencePlane: ReferencePlaneID) -> None:
        """Set the bottom reference plane

        Args:
            bottomReferencePlane: Bottom reference plane
        """
    @property
    def Document(self) -> NemAll_Python_IFW_ElementAdapter.DocumentAdapter:
        """Get the document
        """
    @Document.setter
    def Document(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> None:
        """Set the document

        Args:
            doc: Document
        """
    @property
    def Height(self) -> float:
        """Get the height
        """
    @Height.setter
    def Height(self, height: float) -> None:
        """Set the height

        Args:
            height: Height
        """
    @property
    def MaximumHeight(self) -> float:
        """Get the maximum height
        """
    @MaximumHeight.setter
    def MaximumHeight(self, maximumHeight: float) -> None:
        """Set maximum height

        Args:
            maximumHeight: double
        """
    @property
    def ReferenceElement(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Get the reference element for the plane
        """
    @ReferenceElement.setter
    def ReferenceElement(self, refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> None:
        """Set the reference element for the plane

        Args:
            refElement: Reference element
        """
    @property
    def TopDirection(self) -> Direction:
        """Get the top direction
        """
    @TopDirection.setter
    def TopDirection(self, direction: Direction) -> None:
        """Set the top plane Direction

        Args:
            direction: Direction
        """
    @property
    def TopElevation(self) -> float:
        """Get the top plane elevation relative to the top plane of the document
        """
    @TopElevation.setter
    def TopElevation(self, elevation: float) -> None:
        """Set the top plane elevation relative to the top plane of the document

        Args:
            elevation: Elevation
        """
    @property
    def TopOffset(self) -> float:
        """Offset between the reference plane and the top edge of an architectural component.
        If the property _TopPlaneDependency_ is set to _eAbsElevation_, this is the **absolute elevation** of the top edge."""
    @TopOffset.setter
    def TopOffset(self, offset: float) -> None:
        """Set the offset relative to the defined plane for the top

        Args:
            offset: Offset relative to the defined plane for the top
        """
    @property
    def TopPlaneDependency(self) -> PlaneReferenceDependency:
        """Type of dependency of the top edge of the architectural component"""
    @TopPlaneDependency.setter
    def TopPlaneDependency(self, dependency: PlaneReferenceDependency) -> None:
        """Set the top plane dependency

        Args:
            dependency: Dependency
        """
    @property
    def TopPlaneSurface(self) -> typing.Any:
        """Get the top plane surface
        """
    @TopPlaneSurface.setter
    def TopPlaneSurface(self, topPlaneSurface: typing.Any) -> None:
        """Set the top plane surface

        Args:
            topPlaneSurface: Top plane surface
        """
    @property
    def TopReferencePlane(self) -> ReferencePlaneID:
        """Get the top reference plane
        """
    @TopReferencePlane.setter
    def TopReferencePlane(self, topReferencePlane: ReferencePlaneID) -> None:
        """Set the top reference plane

        Args:
            topReferencePlane: Top reference plane
        """
    eAbsElevation = PlaneReferenceDependency.eAbsElevation
    eBottomFixed = PlaneReferenceDependency.eBottomFixed
    eBottomPlane = PlaneReferenceDependency.eBottomPlane
    eComponentsBottomPlane = PlaneReferenceDependency.eComponentsBottomPlane
    eComponentsTopPlane = PlaneReferenceDependency.eComponentsTopPlane
    eFitToPlane = ElementToPlaneModeling.eFitToPlane
    eLowerCutToPlane = ElementToPlaneModeling.eLowerCutToPlane
    eOrthogonal = Direction.eOrthogonal
    eParallel = Direction.eParallel
    eTopFixed = PlaneReferenceDependency.eTopFixed
    eTopPlane = PlaneReferenceDependency.eTopPlane
    eUpperCutToPlane = ElementToPlaneModeling.eUpperCutToPlane

class ProfileCatalogService():

    """Service providing methods returning profiles as geometrical objects (Path2D, Polyline2D) based on path pointing to a symbol (.sym file) containing a closed profile.
    """
    @staticmethod
    def GetDoubleProfileGap(fullProfileName: str) -> float:
        """Gets double profile gap

        Args:
            fullProfileName:Profile name with path

        Returns:
            Double profile gap
        """
    @staticmethod
    def GetFullProfileBoundaryPaths(fullProfileName: str, overrideDefaultGap: bool = False,
                                    overrideGap: float = 0.0) -> NemAll_Python_Geometry.Path2DList:
        """Get the boundary path of the full profile (e.g. in case of double profile).

        Args:
            fullProfileName:    Profile name with path
            overrideDefaultGap: Override default gap for double profiles
            overrideGap:        Override gap for double profiles

        Returns:
            Profile boundary paths
        """
    @staticmethod
    def GetFullProfileBoundaryPolylines(fullProfileName: str, overrideDefaultGap: bool = False,
                                        overrideGap: float = 0.0) -> NemAll_Python_Geometry.Polyline2DList:
        """Get the boundary polylines of the full profile (e.g. in case of double profile).

        Args:
            fullProfileName:    Profile name with path
            overrideDefaultGap: Override default gap for double profiles
            overrideGap:        Override gap for double profiles

        Returns:
            Profile boundary polylines
        """
    @staticmethod
    def GetProfileAttributes(fullProfileName: str, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> list:
        """Get the profile attributes

        Args:
            fullProfileName:Profile name with path
            doc:            Document

        Returns:
             Attributes
        """
    @staticmethod
    def GetProfileBoundaryPath(fullProfileName: str, overrideDefaultGap: bool = False,
                               overrideGap: float = 0.0) -> NemAll_Python_Geometry.Path2D:
        """Get the boundary path of the single profile

        Args:
            fullProfileName:    Profile name with path
            overrideDefaultGap: Override default gap for double profiles
            overrideGap:        Override gap for double profiles

        Returns:
            Profile boundary path
        """
    @staticmethod
    def GetProfileBoundaryPolyline(fullProfileName: str, overrideDefaultGap: bool = False,
                                   overrideGap: float = 0.0) -> NemAll_Python_Geometry.Polyline2D:
        """Get the boundary polyline of the single profile

        Args:
            fullProfileName:    Profile name with path
            overrideDefaultGap: Override default gap for double profiles
            overrideGap:        Override gap for double profiles

        Returns:
            Profile boundary polyline
        """
    @staticmethod
    def GetProfileGeometry(fullProfileName: str, overrideDefaultGap: bool = False,
                           overrideGap: float = 0.0) -> NemAll_Python_Geometry.BRep3D:
        """Get the profile geometry

        Args:
            fullProfileName:    Profile name with path
            overrideDefaultGap: Override default gap for double profiles
            overrideGap:        Override gap for double profiles

        Returns:
            Profile geometry as BRep3D
        """
    @staticmethod
    def GetProfilePlacementPoint(fullProfileName: str, overrideDefaultGap: bool = False,
                                 overrideGap: float = 0.0) -> NemAll_Python_Geometry.Point3D:
        """Get the profile placement point

        Args:
            fullProfileName:    Profile name with path
            overrideDefaultGap: Override default gap for double profiles
            overrideGap:        Override gap for double profiles

        Returns:
            Profile placement point as Point3D
        """

class ProfileShape():
    """Representation of profile cross section of a structural framing element
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: ProfileShape):
        """Constructor

        Args:
            value: ProfileShape shape
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def ProfilePath(self) -> None:
        """Full path to the cross section profile"""

class PropertyDialogs():

    """Utility class providing methods related to architectural properties such as plane references or trade.
    """
    @staticmethod
    def GetLastSymbolPath() -> str:
        """Get the last symbol path

        Returns:
             Last symbol path
        """
    @staticmethod
    def GetSymbolName(symbolPath: str) -> str:
        """Get the symbol name

        Args:
            symbolPath: Symbol path

        Returns:
             Symbol name
        """
    @staticmethod
    def GetTradeDescription(tradeID: int) -> str:
        """Get the trade description

        Args:
            tradeID: Trade ID

        Returns:
             Trade description
        """
    @staticmethod
    def OpenBottomPlaneReferenceDialog(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                       doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeRefs: PlaneReferences) -> float:
        """Open the plane references dialog

        Returns:
               bottom height

        Args:
            refElement:Reference element (empty element if not exist)
            doc:       Document
            planeRefs: Plane references
        """
    @staticmethod
    def OpenPlaneReferencesDialog(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                  doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeRefs: PlaneReferences):
        """Open the plane references dialog

        Args:
            refElement:Reference element (empty element if not exist)
            doc:       Document
            planeRefs: Plane references
        """
    @staticmethod
    def OpenSmartSymbolPartDialog(smartSymbolPath: str, showSmartSymbols: bool, showSmartParts: bool) -> str:
        """Open the library dialog for SmartSymbols and SmartParts

        Returns:
               result path

        Args:
            smartSymbolPath:  Path to file
            showSmartSymbols: Show smart symbols state
            showSmartParts:   Show SmartParts state
        """
    @staticmethod
    def OpenSymbolDialog(symbolPath: str) -> str:
        """Open the symbol library dialog

        Returns:
               result path

        Args:
            symbolPath:Path to .sym file
        """
    @staticmethod
    def OpenTopPlaneReferenceDialog(refElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                    doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeRefs: PlaneReferences) -> float:
        """Open the plane references dialog

        Returns:
               top height

        Args:
            refElement:Reference element (empty element if not exist)
            doc:       Document
            planeRefs: Plane references
        """
    @staticmethod
    def OpenTradeDialog(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, tradeID: int) -> int:
        """Open the trade dialog

        Args:
            doc:     Document
            tradeID: Current trade ID

        Returns:
             Trade ID
        """

class RectangularShape():
    """Representation of rectangular cross section of a structural framing element
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: RectangularShape):
        """Constructor

        Args:
            value: Rectangular shape
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Thickness(self) -> None:
        """Thickness of rectangular cross section"""
    @property
    def Width(self) -> None:
        """Width of rectangular cross section"""

class ReferencePlaneID():
    """struct for handling reference plane IDs
    """
    def Invalidate(self):
        """Set values to undefined state
        """
    def IsDefaultLowerPlane(self) -> bool:
        """Find out if reference plane is default lower reference plane

        Returns:
            true if ref plane is default lower ref plane
        """
    def IsDefaultUpperPlane(self) -> bool:
        """Find out if reference plane is default upper reference plane

        Returns:
            true if ref plane is default upper ref plane
        """
    def IsDocumentRefSurface(self) -> bool:
        """Find out if reference surface is from document

        Returns:
            true is reference surface from document (not in model)
        """
    def IsInModel(self) -> bool:
        """Find out if reference plane is in model

        Returns:
            true if ref plane is in model
        """
    def IsValid(self) -> bool:
        """Get validity of ref plane

        Returns:
            true if ref plane is valid
        """
    def SetCustomLowerPlane(self):
        """Set values to custom lower state
        """
    def SetCustomUpperPlane(self):
        """Set values to custom upper state
        """
    def __eq__(self, other: ReferencePlaneID) -> bool:
        """Equal operator

        Args:
            other: Reference plane ID to compare

        Returns:
            Reference plane IDs are equal
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, modelGuid: NemAll_Python_IFW_ElementAdapter.GUID, planeId: int):
        """Constructor

        Args:
            modelGuid: Model guid
            planeId:   Plane ID
        """
    @typing.overload
    def __init__(self, element: ReferencePlaneID):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __lt__(self, other: ReferencePlaneID) -> bool:
        """Less operator

        Args:
            other: Reference plane ID to compare

        Returns:
            Reference plane is lees then other
        """
    def __ne__(self, other: ReferencePlaneID) -> bool:
        """Unequal operator

        Args:
            other: Reference plane ID to compare

        Returns:
            Reference plane IDs are not equal
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def ModelGuid(self) -> NemAll_Python_IFW_ElementAdapter.GUID:
        """Get model

        change model id to another
        """
    @ModelGuid.setter
    def ModelGuid(self, inputModelGuid: NemAll_Python_IFW_ElementAdapter.GUID) -> None:
        """change model id to another

        Args:
            inputModelGuid: Model guid
        """
    @property
    def PlaneId(self) -> int:
        """Get plane ID
        """

class RoomElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the Room element
    """
    def GetProperties(self) -> RoomProperties:
        """Get the Room properties

        Returns:
            Room properties
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetProperties(self, RoomProp: RoomProperties):
        """Set the Room properties

        Args:
            RoomProp: Room properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, RoomProp: RoomProperties, RoomPolygon: NemAll_Python_Geometry.Polygon2D):
        """Constructor

        Args:
            RoomProp:    Room properties
            RoomPolygon: Room polygon
        """
    @typing.overload
    def __init__(self, element: RoomElement):
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
    @property
    def Properties(self) -> RoomProperties:
        """Get the Room properties
        """
    @Properties.setter
    def Properties(self, RoomProp: RoomProperties) -> None:
        """Set the Room properties

        Args:
            RoomProp: Room properties
        """

class RoomProperties(ArchBaseProperties):
    """Implementation of the Room properties
    """
    def GetAttributes(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, onlyModifiable: bool) -> list[tuple[int,
                      (int | float | str)]]:
        """Get the room attributes

        Args:
            doc:             Document
            onlyModifiable:  when true, gets only modifiable attributes, otherwise gets all attributes

        Returns:
            List with the attributes represented with tuples like (attributeID, attributeValue)
        """
    def GetFunction(self) -> str:
        """Get the function

        Returns:
            Function
        """
    def GetStoreyCode(self) -> str:
        """Get the storey code

        Returns:
            Storey code
        """
    def GetText(self, number: int) -> str:
        """Get the value of the attributes Text1 to Text5

        Args:
            number:  Number (1-5 allowed)
        Returns:
            Value of the attribute
        """
    def SetAttribute(self,
                     attrib: (NemAll_Python_BaseElements.AttributeInteger | NemAll_Python_BaseElements.AttributeDouble | NemAll_Python_BaseElements.AttributeString | NemAll_Python_BaseElements.AttributeEnum)):
        """Set the attribute

        Args:
            attrib: Attribute
        """
    def SetFunction(self, name: str):
        """Set the function

        Args:
            name: Function
        """
    def SetStoreyCode(self, storeyCode: str):
        """Set the storey code

        Args:
            storeyCode: Storey code
        """
    def SetText(self, text: str, number: int):
        """Set a value to the attributes Text1 to Text5

        Args:
            text:    Desired value of the attribute
            number:  Number (1-5 allowed)
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, RoomProp: RoomProperties):
        """Copy constructor

        Args:
            RoomProp: Room properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Function(self) -> str:
        """Get the function
        """
    @Function.setter
    def Function(self, name: str) -> None:
        """Set the function

        Args:
            name: Function
        """
    @property
    def StoreyCode(self) -> str:
        """Get the storey code
        """
    @StoreyCode.setter
    def StoreyCode(self, storeyCode: str) -> None:
        """Set the storey code

        Args:
            storeyCode: Storey code
        """

class ShapeType(enum.Enum):
    """Types of cross sections of linear architectural objects, like beams or columns.
    """
    eArbitrary = 6
    eChamfer = 9
    eCircular = 1
    """Round cross section"""
    eConical = 4
    ePolygonal = 5
    """Cross section bounded with a free, closed polygon"""
    eProfile = 6
    """Cross section defined with a symbol from the library containing a closed profile"""
    eRectangular = 0
    """Rectangular cross section"""
    eRegularPolygonCircumscribed = 3
    """Cross section in a shape of a regular polygon circumscribed on a circle"""
    eRegularPolygonInscribed = 2
    """Cross section in a shape of a regular polygon inscribed in a circle"""
    eRiseBottomTop = 7
    eStep = 8
    eUnknown = 10

    names = {eRectangular: eRectangular,
             eCircular: eCircular,
             eRegularPolygonInscribed: eRegularPolygonInscribed,
             eRegularPolygonCircumscribed: eRegularPolygonCircumscribed,
             eConical: eConical,
             ePolygonal: ePolygonal,
             eProfile: eProfile,
             eArbitrary: eArbitrary,
             eRiseBottomTop: eRiseBottomTop,
             eStep: eStep,
             eChamfer: eChamfer,
             eUnknown: eUnknown}

    values = {0: eRectangular,
              1: eCircular,
              2: eRegularPolygonInscribed,
              3: eRegularPolygonCircumscribed,
              4: eConical,
              5: ePolygonal,
              6: eArbitrary,
              7: eRiseBottomTop,
              8: eStep,
              9: eChamfer,
              10: eUnknown}

    def __getitem__(self, key: (str | int | float)) -> ShapeType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SlabElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the Slab element
    """
    def GetProperties(self) -> SlabProperties:
        """Get the Slab properties

        Returns:
            Slab properties
        """
    def SetProperties(self, SlabProp: SlabProperties):
        """Set the Slab properties

        Args:
            SlabProp: Slab properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, slabProp: SlabProperties, slabPolygon: NemAll_Python_Geometry.Polygon2D):
        """Constructor

        Args:
            slabProp:    Slab properties
            slabPolygon: Slab polygon
        """
    @typing.overload
    def __init__(self, element: SlabElement):
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
    @property
    def Properties(self) -> SlabProperties:
        """Get the Slab properties
        """
    @Properties.setter
    def Properties(self, SlabProp: SlabProperties) -> None:
        """Set the Slab properties

        Args:
            SlabProp: Slab properties
        """

class SlabFoundationElement(SlabElement, ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the Slab foundation element
    """
    def GetProperties(self) -> SlabFoundationProperties:
        """Get the Slab found properties

        Returns:
            Slab foundation properties
        """
    def SetProperties(self, SlabFoundProp: SlabFoundationProperties):
        """Set the Slab found properties

        Args:
            SlabFoundProp: Slab foundation properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, slabFoundProp: SlabFoundationProperties, slabPolygon: NemAll_Python_Geometry.Polygon2D):
        """Constructor

        Args:
            slabFoundProp: Slab foundation properties
            slabPolygon:   Slab polygon
        """
    @typing.overload
    def __init__(self, element: SlabFoundationElement):
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
    @property
    def Properties(self) -> SlabFoundationProperties:
        """Get the Slab found properties
        """
    @Properties.setter
    def Properties(self, SlabFoundProp: SlabFoundationProperties) -> None:
        """Set the Slab found properties

        Args:
            SlabFoundProp: Slab foundation properties
        """

class SlabProperties(ArchBaseProperties):
    """Implementation of the Slab properties
    """
    def GetAreaPresentationID(self) -> int:
        """Get the ID of the area representation

        Returns:
            ID of the area representation
        """
    def GetAreaPresentationType(self) -> int:
        """Get the type of the area representation

        Returns:
            Type of the area representation
        """
    def GetBackgroundColor(self) -> int:
        """Get the background color

        Returns:
            Background color
        """
    def GetBitmapName(self) -> str:
        """Get the name of the bitmap

        Returns:
            Name of the bitmap
        """
    def GetCalculationMode(self) -> int:
        """Get the calculation model

        Returns:
            Calculation model
        """
    def GetCircleDivision(self) -> int:
        """Get the circle division

        Returns:
            Circle division
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetFaceStyle(self) -> int:
        """Get the face style ID

        Returns:
            Face style ID
        """
    def GetFactor(self) -> float:
        """Get the factor

        Returns:
            Factor
        """
    def GetFilling(self) -> int:
        """Get the filling ID

        Returns:
            Filling ID
        """
    def GetHatch(self) -> int:
        """Get the hatch ID

        Returns:
            Hatch ID
        """
    def GetMaterial(self) -> str:
        """Get the material

        Returns:
            Material
        """
    def GetName(self) -> str:
        """Get the name

        Returns:
            Name
        """
    def GetPattern(self) -> int:
        """Get the pattern ID

        Returns:
            Pattern ID
        """
    def GetPresentationProperties(self) -> object:
        """Get the presentation properties

        Returns:
            Presentation properties
        """
    def GetPriority(self) -> int:
        """Get the priority

        Returns:
            Priority
        """
    def GetSlabTierProperties(self, tierIndex: int) -> SlabTierProperties:
        """Get the wall tier properties

        Args:
            tierIndex: Tier index

        Returns:
            Wall tier properties
        """
    def GetStatus(self) -> int:
        """Get the Status ID

        Returns:
            Status ID
        """
    def GetSurface(self) -> str:
        """Get the surface name and path

        Returns:
            Surface name and path
        """
    def GetSurfaceElementProperties(self) -> SurfaceElementProperties:
        """Get the surface element properties

        Returns:
            Surface element properties
        """
    def GetTierCount(self) -> int:
        """Get the tier count

        Returns:
            Tier count
        """
    def GetTrade(self) -> int:
        """Get the trade index

        Returns:
            Trade index
        """
    def GetVariableTier(self) -> int:
        """Get the variable tier

        Returns:
            Attribute data set
            Attribute data set
        """
    def IsShowAreaElementInGroundView(self) -> bool:
        """Get the 'Show the area element in the ground view' state

        Returns:
            Show the area element in the ground view: true/false
        """
    def RemoveCommonProperties(self):
        """Remove the common properties
        """
    def ResetAreaElement(self):
        """Reset the area element
        """
    def ResetBackgroundColor(self):
        """Reset the background color
        """
    def SetBackgroundColor(self, colorID: int):
        """Set the background color

        Args:
            colorID: Background color ID
        """
    def SetBitmapName(self, bitmapName: str):
        """Set the name of the bitmap

        Args:
            bitmapName: Bitmap name
        """
    def SetCalculationMode(self, calculationMode: int):
        """Set the calculation mode

        Args:
            calculationMode: Calculation mode
        """
    def SetCircleDivision(self, circleDivision: int):
        """Set the circle division

        Args:
            circleDivision: Circle division
        """
    def SetCommonProperties(self, comProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            comProp: Common properties
        """
    def SetFaceStyle(self, faceStyleID: int):
        """Set the face style

        Args:
            faceStyleID: Face style ID
        """
    def SetFactor(self, factor: float):
        """Set the factor

        Args:
            factor: Factor
        """
    def SetFilling(self, fillingID: int):
        """Set the filling

        Args:
            fillingID: Filling ID
        """
    def SetHatch(self, hatchID: int):
        """Set the hatch

        Args:
            hatchID: Hatch ID
        """
    def SetMaterial(self, material: str):
        """Set the material

        Args:
            material: Material
        """
    def SetName(self, name: str):
        """Set the name

        Args:
            name: Name
        """
    def SetPattern(self, patternID: int):
        """Set the pattern

        Args:
            patternID: Pattern ID
        """
    def SetPriority(self, priority: int):
        """Set the priority

        Args:
            priority: Priority
        """
    def SetShowAreaElementInGroundView(self, showInGroundView: bool):
        """Set the show area element in ground view state

        Args:
            showInGroundView: Show the area element in the ground view
        """
    def SetStatus(self, statusID: int):
        """Set the Status ID

        Args:
            statusID: Status ID
        """
    def SetSurface(self, surface: str):
        """Set the surface

        Args:
            surface: Surface
        """
    def SetSurfaceElementProperties(self, surfaceElementProp: SurfaceElementProperties):
        """Set the surface element properties

        Args:
            surfaceElementProp: surface element properties
        """
    def SetTierCount(self, tierCount: int):
        """Set the tier count

        Args:
            tierCount: Tier count
        """
    def SetTrade(self, value: int):
        """Set the trade

        Args:
            value: Trade index
        """
    def SetVariableTier(self, tierIndex: int):
        """Set the variable tier

        Args:
            tierIndex: Tier index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, slabProp: SlabProperties):
        """Copy constructor

        Args:
            slabProp: Slab properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def BackgroundColor(self) -> int:
        """Get the background color
        """
    @BackgroundColor.setter
    def BackgroundColor(self, colorID: int) -> None:
        """Set the background color

        Args:
            colorID: Background color ID
        """
    @property
    def BitmapName(self) -> str:
        """Get the name of the bitmap
        """
    @BitmapName.setter
    def BitmapName(self, bitmapName: str) -> None:
        """Set the name of the bitmap

        Args:
            bitmapName: Bitmap name
        """
    @property
    def CalculationMode(self) -> int:
        """Get the calculation model
        """
    @CalculationMode.setter
    def CalculationMode(self, calculationMode: int) -> None:
        """Set the calculation mode

        Args:
            calculationMode: Calculation mode
        """
    @property
    def CircleDivision(self) -> int:
        """Get the circle division
        """
    @CircleDivision.setter
    def CircleDivision(self, circleDivision: int) -> None:
        """Set the circle division

        Args:
            circleDivision: Circle division
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, comProp: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties

        Args:
            comProp: Common properties
        """
    @property
    def FaceStyle(self) -> int:
        """Get the face style ID
        """
    @FaceStyle.setter
    def FaceStyle(self, faceStyleID: int) -> None:
        """Set the face style

        Args:
            faceStyleID: Face style ID
        """
    @property
    def Factor(self) -> float:
        """Get the factor
        """
    @Factor.setter
    def Factor(self, factor: float) -> None:
        """Set the factor

        Args:
            factor: Factor
        """
    @property
    def Filling(self) -> int:
        """Get the filling ID
        """
    @Filling.setter
    def Filling(self, fillingID: int) -> None:
        """Set the filling

        Args:
            fillingID: Filling ID
        """
    @property
    def Hatch(self) -> int:
        """Get the hatch ID
        """
    @Hatch.setter
    def Hatch(self, hatchID: int) -> None:
        """Set the hatch

        Args:
            hatchID: Hatch ID
        """
    @property
    def Material(self) -> str:
        """Get the material
        """
    @Material.setter
    def Material(self, material: str) -> None:
        """Set the material

        Args:
            material: Material
        """
    @property
    def Name(self) -> str:
        """Get the name
        """
    @Name.setter
    def Name(self, name: str) -> None:
        """Set the name

        Args:
            name: Name
        """
    @property
    def Pattern(self) -> int:
        """Get the pattern ID
        """
    @Pattern.setter
    def Pattern(self, patternID: int) -> None:
        """Set the pattern

        Args:
            patternID: Pattern ID
        """
    @property
    def Priority(self) -> int:
        """Get the priority
        """
    @Priority.setter
    def Priority(self, priority: int) -> None:
        """Set the priority

        Args:
            priority: Priority
        """
    @property
    def Status(self) -> int:
        """Get the Status ID
        """
    @Status.setter
    def Status(self, statusID: int) -> None:
        """Set the Status ID

        Args:
            statusID: Status ID
        """
    @property
    def Surface(self) -> str:
        """Get the surface name and path
        """
    @Surface.setter
    def Surface(self, surface: str) -> None:
        """Set the surface

        Args:
            surface: Surface
        """
    @property
    def SurfaceElementProperties(self) -> SurfaceElementProperties:
        """Get the surface element properties
        """
    @SurfaceElementProperties.setter
    def SurfaceElementProperties(self, surfaceElementProp: SurfaceElementProperties) -> None:
        """Set the surface element properties

        Args:
            surfaceElementProp: surface element properties
        """
    @property
    def TierCount(self) -> int:
        """Get the tier count
        """
    @TierCount.setter
    def TierCount(self, tierCount: int) -> None:
        """Set the tier count

        Args:
            tierCount: Tier count
        """
    @property
    def Trade(self) -> int:
        """Get the trade index
        """
    @Trade.setter
    def Trade(self, value: int) -> None:
        """Set the trade

        Args:
            value: Trade index
        """
    @property
    def VariableTier(self) -> int:
        """Get the variable tier
        """
    @VariableTier.setter
    def VariableTier(self, tierIndex: int) -> None:
        """Set the variable tier

        Args:
            tierIndex: Tier index
        """

class SlabOpeningElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of recess or opening in slab
    """
    def GetPlacementPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the placement point

        Returns:
            Placement point
        """
    def GetProperties(self) -> SlabOpeningProperties:
        """Get the slab opening properties

        Returns:
            Slab opening properties
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetPlacementPoint(self, placementPoint: NemAll_Python_Geometry.Point2D):
        """Set the placement point

        Args:
            placementPoint: Placement point
        """
    def SetProperties(self, slabOpeningProp: SlabOpeningProperties):
        """Set the SlabOpening properties

        Args:
            slabOpeningProp: Slab opening properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, slabOpeningProp: SlabOpeningProperties, placementPoint: NemAll_Python_Geometry.Point3D,
                 slabConnectionUUID: NemAll_Python_IFW_ElementAdapter.GUID):
        """Constructor

        Args:
            slabOpeningProp:    SlabOpening properties
            placementPoint:     Placement point
            slabConnectionUUID: Connection UUID of the slab
        """
    @typing.overload
    def __init__(self, slabOpeningProp: SlabOpeningProperties, placementPoint: NemAll_Python_Geometry.Point2D,
                 slabConnectionUUID: NemAll_Python_IFW_ElementAdapter.GUID):
        """Constructor

        Args:
            slabOpeningProp:    SlabOpening properties
            placementPoint:     Placement point
            slabConnectionUUID: Connection UUID of the slab
        """
    @typing.overload
    def __init__(self, element: SlabOpeningElement):
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
    @property
    def PlacementPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the placement point
        """
    @PlacementPoint.setter
    def PlacementPoint(self, placementPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the placement point

        Args:
            placementPoint: Placement point
        """
    @property
    def Properties(self) -> SlabOpeningProperties:
        """Get the slab opening properties
        """
    @Properties.setter
    def Properties(self, slabOpeningProp: SlabOpeningProperties) -> None:
        """Set the SlabOpening properties

        Args:
            slabOpeningProp: Slab opening properties
        """

class SlabOpeningProperties(VerticalElementProperties, ArchBaseProperties):
    """Implementation of the slab opening properties
    """
    def GetOpeningSymbolsProperties(self) -> OpeningSymbolsProperties:
        """Get a reference of the opening symbols properties

        Returns:
            Opening symbols properties reference
        """
    def GetOpeningType(self) -> SlabOpeningType:
        """Get the opening type

        Returns:
            Opening type
        """
    @typing.overload
    def __init__(self, openingType: SlabOpeningType = SlabOpeningType.eOpening):
        """Constructor

        Args:
            openingType
        """
    @typing.overload
    def __init__(self, openingProps: SlabOpeningProperties):
        """Copy constructor

        Args:
            openingProps: Opening properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Independent2DInteraction(self) -> bool:
        """Get the independent 2D interaction state
        """
    @Independent2DInteraction.setter
    def Independent2DInteraction(self, isIndependent2DInteraction: bool) -> None:
        """Set the independent 2D interaction state

        Args:
            isIndependent2DInteraction: Independent 2D interaction state
        """

class SlabOpeningType(enum.Enum):
    """eOpening:
    eRecess :
    """
    eOpening = 0
    eRecess = 1

    names = {eOpening: eOpening,
             eRecess: eRecess}

    values = {0: eOpening,
              1: eRecess}

    def __getitem__(self, key: (str | int | float)) -> SlabOpeningType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SlabFoundationProperties(SlabProperties, ArchBaseProperties):
    """Implementation of the Slab foundation properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: SlabFoundationProperties):
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

class SlabTierProperties(ArchBaseProperties):
    """Implementation of the slab tier properties
    """
    def GetThickness(self) -> float:
        """
        """
    def SetThickness(self, thickness: float):
        """Args:
            thickness
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, tierProp: SlabTierProperties):
        """Copy constructor

        Args:
            tierProp: Tier properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Thickness(self) -> float:
        """
        """
    @Thickness.setter
    def Thickness(self, value: float) -> None:
        """Set the float
        """

class SolidElementTruncationType(enum.Enum):
    """Type of cutting/stretching method of a structural framing element at its start or end
    """
    FreePlane = 3
    """Cutting with any plane"""
    Horizontal = 1
    """Horizontal cutting"""
    NormalToBodyAxis = 0
    """Perpendicular to the element axis"""
    Vertical = 2
    """Vertical cutting"""

    names = {NormalToBodyAxis: NormalToBodyAxis,
             Horizontal: Horizontal,
             Vertical: Vertical,
             FreePlane: FreePlane}

    values = {0: NormalToBodyAxis,
              1: Horizontal,
              2: Vertical,
              3: FreePlane}

    def __getitem__(self, key: (str | int | float)) -> SolidElementTruncationType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class StripFoundationElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the strip foundation element
    """
    def GetProperties(self) -> StripFoundationProperties:
        """Get the strip foundation properties

        Returns:
            strip foundation properties
        """
    def SetProperties(self, stripfoundationProp: StripFoundationProperties):
        """Set the strip foundation properties

        Args:
            stripfoundationProp: Strip foundation properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, stripFoundationProp: StripFoundationProperties, axis: object):
        """Constructor

        Args:
            stripFoundationProp:  Strip Foundation properties
            axis:                 Axis
        """
    @typing.overload
    def __init__(self, element: StripFoundationElement):
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
    @property
    def Properties(self) -> StripFoundationProperties:
        """Get the strip foundation properties
        """
    @Properties.setter
    def Properties(self, stripfoundationProp: StripFoundationProperties) -> None:
        """Set the strip foundation properties

        Args:
            stripfoundationProp: Strip foundation properties
        """

class StripFoundationProperties(ArchBaseProperties):
    """Implementation of the strip foundation properties
    """
    def GetAxis(self) -> AxisProperties:
        """Get the axis
        """
    def GetLeftHaunch(self) -> float:
        """Get the Left haunch

        Returns:
            width  Left haunch
        """
    def GetProfileFullName(self) -> str:
        """Get the full name of the profile

        Returns:
            fullName  Path and name of the profile
        """
    def GetRightHaunch(self) -> float:
        """Get the Right haunch

        Returns:
            width  Right haunch
        """
    def GetShapeType(self) -> ShapeType:
        """Get the shape type

        Returns:
            Shape type
        """
    def GetStepBounce(self) -> float:
        """Get the Step bounce

        Returns:
            width  Step bounce
        """
    def GetStepChamferEccentricity(self) -> float:
        """Get the Step chamfer eccentricity

        Returns:
            width  Step chamfer eccentricity
        """
    def GetStepChamferHeight(self) -> float:
        """Get the Step chamfer height

        Returns:
            width  Step chamfer height
        """
    def GetStepChamferWidth(self) -> float:
        """Get the Step chamfer width

        Returns:
            width  Step chamfer width
        """
    def GetWidth(self) -> float:
        """Get the width

        Returns:
            Width
        """
    def SetAttribute(self, attrib: object):
        """Set the attribute

        Args:
            attrib: Attribute
        """
    def SetAxis(self, axis: AxisProperties):
        """Set the axis

        Args:
            axis: Axis data
        """
    def SetLeftHaunch(self, width: float):
        """Set the Left haunch

        Args:
            width: Left haunch
        """
    def SetProfileFullName(self, fullName: str):
        """Set the full name of the profile

        Args:
            fullName: Path and name of the profile
        """
    def SetRightHaunch(self, width: float):
        """Set the Right haunch

        Args:
            width: Right haunch
        """
    def SetShapeType(self, shapeType: ShapeType):
        """Set the type of the shape

        Args:
            shapeType: Shape type
        """
    def SetStepBounce(self, width: float):
        """Set the Step bounce

        Args:
            width: Step bounce
        """
    def SetStepChamferEccentricity(self, height: float):
        """Set the Step chamfer eccentricity

        Args:
            height: Step chamfer eccentricity
        """
    def SetStepChamferHeight(self, height: float):
        """Set the Step chamfer height

        Args:
            height: Step chamfer height
        """
    def SetStepChamferWidth(self, width: float):
        """Set the Step chamfer width

        Args:
            width: Step chamfer width
        """
    def SetWidth(self, width: float):
        """Set the width

        Args:
            width: Width
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, stripfoundationProp: StripFoundationProperties):
        """Copy constructor

        Args:
            stripfoundationProp: Strip foundation properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Axis(self) -> AchseDataT:
        """Get the axis
        """
    @Axis.setter
    def Axis(self, axis: AchseDataT) -> None:
        """Set the axis

        Args:
            axis: Axis data
        """
    @property
    def IsStartNewJoinedStripFoundationGroup(self) -> bool:
        """Get the state for starting a new joined strip foundation group

        All strip foundations in a group are used for to create a continues join
        between the strip foundations.
        """
    @IsStartNewJoinedStripFoundationGroup.setter
    def IsStartNewJoinedStripFoundationGroup(self, startNewJoinedStripFoundationGroup: bool) -> None:
        """Set the state for starting a new joined strip foundation group.
        All strip foundations in a group are used for to create a continues join
        between the strip foundations.

        Args:
            startNewJoinedStripFoundationGroup: Start new strip foundation group
        """
    @property
    def LeftHaunch(self) -> float:
        """Get the Left haunch
        """
    @LeftHaunch.setter
    def LeftHaunch(self, width: float) -> None:
        """Set the Left haunch

        Args:
            width: Left haunch
        """
    @property
    def ProfileFullName(self) -> str:
        """Get the full name of the profile
        """
    @ProfileFullName.setter
    def ProfileFullName(self, fullName: str) -> None:
        """Set the full name of the profile

        Args:
            fullName: Path and name of the profile
        """
    @property
    def RightHaunch(self) -> float:
        """Get the Right haunch
        """
    @RightHaunch.setter
    def RightHaunch(self, width: float) -> None:
        """Set the Right haunch

        Args:
            width: Right haunch
        """
    @property
    def ShapeType(self) -> ShapeType:
        """Get the shape type
        """
    @ShapeType.setter
    def ShapeType(self, shapeType: ShapeType) -> None:
        """Set the type of the shape

        Args:
            shapeType: Shape type
        """
    @property
    def StepBounce(self) -> float:
        """Get the Step bounce
        """
    @StepBounce.setter
    def StepBounce(self, width: float) -> None:
        """Set the Step bounce

        Args:
            width: Step bounce
        """
    @property
    def StepChamferEccentricity(self) -> float:
        """Get the Step chamfer eccentricity
        """
    @StepChamferEccentricity.setter
    def StepChamferEccentricity(self, height: float) -> None:
        """Set the Step chamfer eccentricity

        Args:
            height: Step chamfer eccentricity
        """
    @property
    def StepChamferHeight(self) -> float:
        """Get the Step chamfer height
        """
    @StepChamferHeight.setter
    def StepChamferHeight(self, height: float) -> None:
        """Set the Step chamfer height

        Args:
            height: Step chamfer height
        """
    @property
    def StepChamferWidth(self) -> float:
        """Get the Step chamfer width
        """
    @StepChamferWidth.setter
    def StepChamferWidth(self, width: float) -> None:
        """Set the Step chamfer width

        Args:
            width: Step chamfer width
        """
    @property
    def Width(self) -> float:
        """Get the width
        """
    @Width.setter
    def Width(self, width: float) -> None:
        """Set the width

        Args:
            width: Width
        """

class StructuralBeamElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of the structural framing beam
    """
    def GetStructuralBeamProperties(self) -> StructuralBeamProperties:
        """Get the Structural Beam properties

        Returns:
            Beam properties
        """
    def SetAxisVisibility(self, visibility: bool):
        """Set the Visibility of element axis

        Args:
            visibility: Bool if axis of element should be visible
        """
    def SetStructuralBeamProperties(self, properties: StructuralBeamProperties):
        """Set the Structural Beam properties

        Args:
            properties: Beam properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, properties: StructuralBeamProperties):
        """Constructor

        Args:
            properties: StructuralBeam properties
        """
    @typing.overload
    def __init__(self, element: StructuralBeamElement):
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
    @property
    def StructuralBeamProperties(self) -> StructuralBeamProperties:
        """Get the Structural Beam properties
        """
    @StructuralBeamProperties.setter
    def StructuralBeamProperties(self, properties: StructuralBeamProperties) -> None:
        """Set the Structural Beam properties

        Args:
            properties: Beam properties
        """

class StructuralElementProperties(ArchBaseProperties):
    """Representation of the properties of **structural framing element**
    """
    def AddHole(self, holeGeometry: NemAll_Python_Geometry.BRep3D) -> int:
        """Adds a hole to the list of holes for the Structural Element

        Args:
            holeGeometry: 3D BRep Geometry of the hole

        Returns:
            Unique ID for the created hole
        """
    def GetAnglesAtEnd(self) -> tuple:
        """Get angles between the cross-sectional area and the plane perpendicular to the axis
        of the structural framing element at its end

        Returns:
            angle in local X direction
            angle in local Y direction
        """
    def GetAnglesAtStart(self) -> tuple:
        """Get angles between the cross-sectional area and the plane perpendicular to the axis
        of the structural framing element at its start

        Returns:
            angle in local X direction
            angle in local Y direction
        """
    def GetBodyAxis(self) -> NemAll_Python_Geometry.Line3D:
        """Get the Axis of the structural framing element calculated in the cross section's **center of gravity**

        Returns:
            Axis
        """
    def GetCenterAxis(self) -> NemAll_Python_Geometry.Line3D:
        """Get the axis of the structural framing element calculated in the **center of the cross section outline**

        Returns:
            Axis
        """
    def GetConnectionAxis(self) -> NemAll_Python_Geometry.Line3D:
        """Get Connection Axis as a Line3D

        Returns:
            Line3D which contains information about start and end point coordinates
        """
    def GetDoubleProfileGap(self) -> float:
        """Gets double profile gap

        Returns:
            Double profile gap
        """
    def GetEndPointAdditionalOffset(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the end point distance dx/dy

        Returns:
            Vector3D with offsets in x and y like Vector3D(distance_dx, distance dy, 0)
        """
    def GetEndPointZOffset(self) -> float:
        """Get the the offset between the _anchor end point_ and the _element end point_ of a structural framing element

        Returns:
            Offset value
        """
    def GetEndReferencePointType(self) -> CustomBoxPoint:
        """Get type the reference point at end

        Returns:
            Type the reference point at end
        """
    def GetHeightProperties(self) -> PlaneReferences:
        """Get HeightProperties

        Returns:
            HeightProperties
        """
    def GetHoles(self) -> dict:
        """Returns existing holes as python dictionary, where key is hole ID, value is its geometry

        Returns:
            Existing holes as python dictionary, where key is hole ID, value is its geometry
        """
    def GetProfileAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get rotation angle of cross section profile around the axis of a structural framing element

        Returns:
            Rotation angle
        """
    def GetProfileShapeProperties(self) -> object:
        """Get the shape properties of the cross section

        Returns:
            Cross section properties
        """
    def GetShapeTypeAtEnd(self) -> SolidElementTruncationType:
        """Get truncation type at the element's end point

        Returns:
            truncation type
        """
    def GetShapeTypeAtStart(self) -> SolidElementTruncationType:
        """Get truncation type at the element's start point

        Returns:
            truncation type
        """
    def GetSkeletonSolidElementProperties(self) -> object:
        """Get SkeletonSolidElementProperties

        Returns:
            SkeletonSolidElementProperties
        """
    def GetStartPointAdditionalOffset(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the start point distance dx/dy

        Returns:
            Vector3D with offsets in x and y like Vector3D(distance_dx, distance dy, 0)
        """
    def GetStartPointZOffset(self) -> float:
        """Get the the offset between the _anchor start point_ and the _element start point_ of a structural framing element

        Returns:
            Offset value
        """
    def GetStartReferencePointType(self) -> CustomBoxPoint:
        """Get type of the reference point at start

        Returns:
            Type of the reference point at start
        """
    def GetZCoordsVisibility(self) -> bool:
        """Get visibility of Z coordinates of insertion point

        Returns:
            True if Z coordinates visible, False otherwise
        """
    def HasTwoAnchorPoints(self) -> bool:
        """Get the two anchor point state

        Returns:
            Two anchor point state
        """
    def RemoveHole(self, holeID: int):
        """Removes a hole to the list of holes for the Structural Element

        Args:
            holeID: ID of the hole to remove. This ID is obtained by AddHole operation
        """
    def SetAnglesAtEnd(self, angleX: NemAll_Python_Geometry.Angle, angleY: NemAll_Python_Geometry.Angle):
        """Set angles between the cross-sectional area and the plane perpendicular to the axis
        of the structural framing element at its end

        Args:
            angleX: angle in local X direction
            angleY: angle in local Y direction
        """
    def SetAnglesAtStart(self, angleX: NemAll_Python_Geometry.Angle, angleY: NemAll_Python_Geometry.Angle):
        """Set angles between the cross-sectional area and the plane perpendicular to the axis
        of the structural framing element at its start

        Args:
            angleX: angle in local X direction
            angleY: angle in local Y direction
        """
    def SetAttribute(self, attrib: object):
        """Set the attribute

        Args:
            attrib: Attribute
        """
    def SetCommonProperties(self, comProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the Common properties

        Args:
            comProp: Common properties
        """
    def SetDoubleProfileGap(self, desiredGap: float) -> bool:
        """Set the gap of double profile

        Args:
            desiredGap: Desired gap

        Returns:
            true if attribute Gap was correctly set and exists / false if given profile doesn't have attribute Gap
        """
    def SetEndPointZOffset(self, desiredOffset: float):
        """Set the offset between the _anchor end point_ and the _element end point_ of a structural framing element

        Args:
            desiredOffset:  offset value
        """
    def SetProfileAngle(self, value: NemAll_Python_Geometry.Angle):
        """Set rotation angle of cross section profile around the axis of a structural framing element

        Args:
            value:  Rotation angle
        """
    def SetProfileShapeProperties(self, value: object):
        """Set cross-section shape properties

        Args:
            value:  Profile Shape Properties\n
        """
    def SetShapeTypeAtEnd(self, endTruncationType: SolidElementTruncationType):
        """Set truncation type at the element's end point

        Args:
            endTruncationType:  truncation type
        """
    def SetShapeTypeAtStart(self, startTruncationType: SolidElementTruncationType):
        """Set truncation type at the element's start point

        Args:
            startTruncationType:  truncation type
        """
    def SetStartPointZOffset(self, desiredOffset: float):
        """Set the offset between the _anchor start point_ and the _element start point_ of a structural framing element

        Args:
            desiredOffset:  offset value
        """
    def SetTwoAnchorPoints(self, areTwoAnchorPoint: bool):
        """Whether the structural framing element should have two different anchor points at beginning and at end

        Args:
            areTwoAnchorPoint:  True to make the element have two different anchor points, False otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: StructuralElementProperties):
        """Constructor

        Args:
            value: Structural Element properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def DoubleProfileGap(self) -> float:
        """Gets double profile gap
        """
    @DoubleProfileGap.setter
    def DoubleProfileGap(self, desiredGap: float) -> None:
        """Gets double profile gap

        Set the gap of double profile

        Args:
            desiredGap: Desired gap
        """
    @property
    def EndPointZOffset(self) -> float:
        """Get the value of Z offset of the anchor point at end the point of SF element
        """
    @EndPointZOffset.setter
    def EndPointZOffset(self, desiredOffset: float) -> None:
        """Set the value of the Z offset of the anchor point at the end point of SF element to desired value

        Args:
            desiredOffset: Desired offset
        """
    @property
    def ProfileAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get the rotation angle of element profile
        """
    @ProfileAngle.setter
    def ProfileAngle(self, value: NemAll_Python_Geometry.Angle) -> None:
        """Set the rotation angle of element profile

        Args:
            value: Rotation angle of element profile
        """
    @property
    def ProfileShapeProperties(self) -> object:
        """Get ProfileShapeProperties
        """
    @ProfileShapeProperties.setter
    def ProfileShapeProperties(self, value: object) -> None:
        """Set the Column ProfileShape Properties

        Args:
            value: ProfileShape Properties of Column
        """
    @property
    def ShapeTypeAtEnd(self) -> SolidElementTruncationType:
        """Get truncation type at the start of the Structural Element
        """
    @ShapeTypeAtEnd.setter
    def ShapeTypeAtEnd(self, endTruncationType: SolidElementTruncationType) -> None:
        """Set truncation type at the end of the Structural Element

        Args:
            endTruncationType: Truncation type
        """
    @property
    def ShapeTypeAtStart(self) -> SolidElementTruncationType:
        """Get truncation type at the end of the Structural Element
        """
    @ShapeTypeAtStart.setter
    def ShapeTypeAtStart(self, startTruncationType: SolidElementTruncationType) -> None:
        """Set truncation type at the start of the Structural Element

        Args:
            startTruncationType: Truncation type
        """
    @property
    def StartPointZOffset(self) -> float:
        """Get the value of Z offset of the anchor point at start the point of SF element
        """
    @StartPointZOffset.setter
    def StartPointZOffset(self, desiredOffset: float) -> None:
        """Set the value of the Z offset of the anchor point at the start point of SF element to desired value.

        Args:
            desiredOffset: Desired offset
        """

class StructuralBraceElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of the structural framing bracing
    """
    def GetStructuralBraceProperties(self) -> StructuralBraceProperties:
        """Get the Structural Brace properties

        Returns:
            Brace properties
        """
    def SetAxisVisibility(self, visibility: bool):
        """Set the Visibility of element axis

        Args:
            visibility: Bool if axis of element should be visible
        """
    def SetStructuralBraceProperties(self, properties: StructuralBraceProperties):
        """Set the Structural Brace properties

        Args:
            properties: Brace properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, properties: StructuralBraceProperties):
        """Constructor

        Args:
            properties: StructuralBrace properties
        """
    @typing.overload
    def __init__(self, element: StructuralBraceElement):
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
    @property
    def StructuralBraceProperties(self) -> StructuralBraceProperties:
        """Get the Structural Brace properties
        """
    @StructuralBraceProperties.setter
    def StructuralBraceProperties(self, properties: StructuralBraceProperties) -> None:
        """Set the Structural Brace properties

        Args:
            properties: Brace properties
        """

class StructuralBraceProperties(StructuralElementProperties, ArchBaseProperties):
    """Representation of the properties of the structural framing bracing
    """
    def GetEndPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the end point of the element in world coordinate system

        Returns:
            End point
        """
    def GetStartPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the start point of the element in world coordinate system

        Returns:
            Start point
        """
    def SetAnchorPointProperties(self, anchorPointStart: int, offsetStart: NemAll_Python_Geometry.Point2D, anchorPointEnd: int,
                                 offsetEnd: NemAll_Python_Geometry.Point2D, twoAnchorPoints: bool):
        """Set the Column Anchor Point Properties

        Values for anchor point:
            1 - LeftBottom
            2 - RightBottom
            3 - RightTop
            4 - LeftTop
            5 - Center
            6 - MiddleBottom
            7 - MiddleRight
            8 - MiddleTop
            9 - MiddleLeft
           10 - CenterOfGravity

        Args:
            anchorPointStart: Anchor point position
            offsetStart:      Offset from start anchor point
            anchorPointEnd:   Anchor point position
            offsetEnd:        Offset from end anchor point
            twoAnchorPoints:  true when both anchor points are used
        """
    def SetEndPoint(self, x: float, y: float, z: float):
        """Set the end point of the element in world coordinate system

        Args:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        """
    def SetHeightProperties(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeReferences: BasePlaneReferences):
        """Set height properties

        Args:
            doc:              Document
            planeReferences:  Height properties as PlaneReferences object
        """
    def SetHeightPropsByPlacementPoints(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, value: BasePlaneReferences,
                                        startPointZcoord: float, endPointZcoord: float):
        """Set HeightProperties by the placement points

        Args:
            doc:              Document
            value:            Height properties
            startPointZcoord: Z coordinate of the start point
            endPointZcoord:   Z coordinate of the end point
        """
    def SetStartPoint(self, x: float, y: float, z: float):
        """Set the start point of the element in world coordinate system

        Args:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: StructuralBraceProperties):
        """Constructor

        Args:
            value: Structural Beam properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class StructuralColumnElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of the structural framing column
    """
    def GetStructuralColumnProperties(self) -> StructuralColumnProperties:
        """Get the Structural Column properties

        Returns:
            Column properties
        """
    def SetAxisVisibility(self, visibility: bool):
        """Set the Visibility of element axis

        Args:
            visibility: Bool if axis of element should be visible
        """
    def SetStructuralColumnProperties(self, structuralColumnProp: StructuralColumnProperties):
        """Set the Structural Column properties

        Args:
            structuralColumnProp: Column properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, structuralColumnProp: StructuralColumnProperties):
        """Constructor

        Args:
            structuralColumnProp: StructuralColumn properties
        """
    @typing.overload
    def __init__(self, element: StructuralColumnElement):
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
    @property
    def StructuralColumnProperties(self) -> StructuralColumnProperties:
        """Get the Structural Column properties
        """
    @StructuralColumnProperties.setter
    def StructuralColumnProperties(self, structuralColumnProp: StructuralColumnProperties) -> None:
        """Set the Structural Column properties

        Args:
            structuralColumnProp: Column properties
        """

class StructuralColumnProperties(StructuralElementProperties, ArchBaseProperties):
    """Representation of the properties of the structural framing column
    """
    def GetHeight(self) -> float:
        """Get the Column Height

        Returns:
            Column Height
        """
    def GetPosition(self) -> NemAll_Python_Geometry.Point3D:
        """Get the Column position in world coordinate system

        Returns:
            Column position in world coordinate system
        """
    def SetAnchorPointProperties(self, anchorPoint: int, offset: NemAll_Python_Geometry.Point2D):
        """Set the Column Anchor Point Properties

        Values for anchor point:
            1 - LeftBottom
            2 - RightBottom
            3 - RightTop
            4 - LeftTop
            5 - Center
            6 - MiddleBottom
            7 - MiddleRight
            8 - MiddleTop
            9 - MiddleLeft
           10 - CenterOfGravity

        Args:
            anchorPoint: Anchor point position
            offset:      Offset from start anchor point
        """
    def SetHeight(self, height: float, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, heightRefereces: PlaneReferences):
        """Set Column Height

        Args:
            height:          Height
            doc:             Document
            heightRefereces: Height Properties of Column, as PlaneReferences type
        """
    def SetHeightProperties(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, value: PlaneReferences):
        """Set height properties

        Args:
            doc:              Document
            planeReferences:  Height properties as PlaneReferences object
        """
    def SetHeightPropsByPlacementPoint(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, value: PlaneReferences,
                                       startPointZcoord: float):
        """Set HeightProperties by a placement point

        Args:
            doc:              Document
            value:            Height Properties of Column, as PlaneReferences type
            startPointZcoord: Z coordinate start point
        """
    def SetPosition(self, x: float, y: float, z: float):
        """Set the position of the column in world coordinate system

        Args:
            x:  x coordinate
            y:  y coordinate
            z:  z coordinate
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: StructuralColumnProperties):
        """Constructor

        Args:
            value: Structural Beam properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class StructuralBeamProperties(StructuralElementProperties, ArchBaseProperties):
    """Representation of the properties of the structural framing beam
    """
    def GetEndPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the end point of the element in world coordinate system

        Returns:
            End point
        """
    def GetStartPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the start point of the element in world coordinate system

        Returns:
            Start point
        """
    def SetAnchorPointProperties(self, anchorPointStart: int, offsetStart: NemAll_Python_Geometry.Point2D, anchorPointEnd: int,
                                 offsetEnd: NemAll_Python_Geometry.Point2D, twoAnchorPoints: bool):
        """Set the properties of the beam anchor points

        Args:
            anchorPointStart:   anchor point position
            offsetStart:        offset from start anchor point
            anchorPointEnd:     anchor point position
            offsetEnd:          offset from end anchor point
            twoAnchorPoints:    true when both anchor points are used
        """
    def SetEndPoint(self, x: float, y: float, z: float):
        """Set the end point of the element in world coordinate system

        Args:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        """
    def SetHeightProperties(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeReferences: PlaneReferences):
        """Set height properties

        Args:
            doc:              Document
            planeReferences:  Height properties as PlaneReferences object
        """
    def SetHeightPropsByPlacementPoints(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, value: PlaneReferences,
                                        startPointZcoord: float, endPointZcoord: float):
        """Set HeightProperties by the placement points

        Args:
            doc:              Document
            value:            Height properties
            startPointZcoord: Z coordinate of the start point
            endPointZcoord:   Z coordinate of the end point
        """
    def SetStartPoint(self, x: float, y: float, z: float):
        """Set the start point of the element in world coordinate system

        Args:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: StructuralBeamProperties):
        """Constructor

        Args:
            value: Structural Beam properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class StructuralPurlinElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the Structural Purlin Element
    """
    def GetStructuralPurlinProperties(self) -> StructuralPurlinProperties:
        """Get the Structural Purlin properties

        Returns:
            Purlin properties
        """
    def SetAxisVisibility(self, visibility: bool):
        """Set the Visibility of element axis

        Args:
            visibility: Bool if axis of element should be visible
        """
    def SetStructuralPurlinProperties(self, properties: StructuralPurlinProperties):
        """Set the Structural Purlin properties

        Args:
            properties: Purlin properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, properties: StructuralPurlinProperties):
        """Constructor

        Args:
            properties: StructuralPurlin properties
        """
    @typing.overload
    def __init__(self, element: StructuralPurlinElement):
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
    @property
    def StructuralPurlinProperties(self) -> StructuralPurlinProperties:
        """Get the Structural Purlin properties
        """
    @StructuralPurlinProperties.setter
    def StructuralPurlinProperties(self, properties: StructuralPurlinProperties) -> None:
        """Set the Structural Purlin properties

        Args:
            properties: Purlin properties
        """

class StructuralPurlinProperties(StructuralElementProperties, ArchBaseProperties):
    """Implementation of the Structural Purlin properties
    """
    def GetEndPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the end point of the element in world coordinate system

        Returns:
            End point
        """
    def GetStartPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the start point of the element in world coordinate system

        Returns:
            Start point
        """
    def SetAnchorPointProperties(self, anchorPointStart: int, offsetStart: NemAll_Python_Geometry.Point2D, anchorPointEnd: int,
                                 offsetEnd: NemAll_Python_Geometry.Point2D, twoAnchorPoints: bool):
        """Set the Column Anchor Point Properties

        Values for anchor point:"
            1 - LeftBottom"
            2 - RightBottom"
            3 - RightTop"
            4 - LeftTop"
            5 - Center"
            6 - MiddleBottom"
            7 - MiddleRight"
            8 - MiddleTop"
            9 - MiddleLeft"
           10 - CenterOfGravity"

        Args:
            anchorPointStart: Anchor point position
            offsetStart:      Offset from start anchor point
            anchorPointEnd:   Anchor point position
            offsetEnd:        Offset from end anchor point
            twoAnchorPoints:  true when both anchor points are used
        """
    def SetEndPoint(self, x: float, y: float, z: float):
        """Set the end point of the element in world coordinate system

        Args:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        """
    def SetHeightProperties(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeReferences: PlaneReferences):
        """Set HeightProperties

        Args:
            doc:             Document
            planeReferences: Height Properties of Column, as PlaneReferences type
        """
    def SetHeightPropsByPlacementPoints(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, value: PlaneReferences,
                                        startPointZcoord: float, endPointZcoord: float):
        """Set HeightProperties by the placement points

        Args:
            doc:              Document
            value:            Height properties
            startPointZcoord: Z coordinate of the start point
            endPointZcoord:   Z coordinate of the end point
        """
    def SetStartPoint(self, x: float, y: float, z: float):
        """Set the start point of the element in world coordinate system

        Args:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, value: StructuralPurlinProperties):
        """Constructor

        Args:
            value: Structural Purlin properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class SurfaceElementProperties():
    """Implementation of the surface element properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, baseProp: SurfaceElementProperties):
        """Copy constructor

        Args:
            baseProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def BitmapID(self) -> str:
        """Get bitmap id
        """
    @BitmapID.setter
    def BitmapID(self, bitmapID: str) -> None:
        """Set bitmap id

        Args:
            bitmapID: ID of bitmap
        """
    @property
    def BitmapSelected(self) -> bool:
        """Get the bitmap selected state
        """
    @BitmapSelected.setter
    def BitmapSelected(self, isBitmapSelected: bool) -> None:
        """Set the bitmap selected state. If bitmap is selected - hatch, pattern, filling and faceStyle will be deselected

        Args:
            isBitmapSelected: True if bitmap is selected, false otherwise
        """
    @property
    def FaceStyleID(self) -> int:
        """Get face style id
        """
    @FaceStyleID.setter
    def FaceStyleID(self, facestyleID: int) -> None:
        """Set face style id

        Args:
            facestyleID: ID of face style
        """
    @property
    def FaceStyleSelected(self) -> bool:
        """Get the faceStyle selected state
        """
    @FaceStyleSelected.setter
    def FaceStyleSelected(self, isFaceStyleSelected: bool) -> None:
        """Set the faceStyle selected state. If faceStyle is selected - hatch, pattern, filling and bitmap will be deselected

        Args:
            isFaceStyleSelected: True if faceStyle is selected, false otherwise
        """
    @property
    def FillingID(self) -> int:
        """Get filling id
        """
    @FillingID.setter
    def FillingID(self, fillingID: int) -> None:
        """Set filling id

        Args:
            fillingID: ID of filling
        """
    @property
    def FillingSelected(self) -> bool:
        """Get the filling selected state

        Hatch and pattern can be used in combination with filling.
        """
    @FillingSelected.setter
    def FillingSelected(self, isFillingSelected: bool) -> None:
        """Set the filling selected state. If filling is selected - faceStyle and bitmap will be deselected.
        Hatch and pattern can be used in combination with filling.

        Args:
            isFillingSelected: True if filling is selected, false otherwise
        """
    @property
    def HatchID(self) -> int:
        """Get hatch id
        """
    @HatchID.setter
    def HatchID(self, hatchID: int) -> None:
        """Set hatch id

        Args:
            hatchID: ID of hatch
        """
    @property
    def HatchSelected(self) -> bool:
        """Get the hatch selected state
        """
    @HatchSelected.setter
    def HatchSelected(self, isHatchSelected: bool) -> None:
        """Set the hatch selected state. If hatch is selected - pattern, faceStyle and bitmap will be deselected

        Args:
            isHatchSelected: True if hatch is selected, false otherwise
        """
    @property
    def PatternID(self) -> int:
        """Get pattern id
        """
    @PatternID.setter
    def PatternID(self, patternID: int) -> None:
        """Set the pattern id

        Args:
            patternID: ID of pattern
        """
    @property
    def PatternSelected(self) -> bool:
        """Get the pattern selected state
        """
    @PatternSelected.setter
    def PatternSelected(self, isPatternSelected: bool) -> None:
        """Set the pattern selected state. If pattern is selected - hatch, faceStyle and bitmap will be deselected

        Args:
            isPatternSelected: True if pattern is selected, false otherwise
        """
    @property
    def UseAreaInGroundplan(self) -> bool:
        """Get if the area should be used in ground plan
        """
    @UseAreaInGroundplan.setter
    def UseAreaInGroundplan(self, useArea: bool) -> None:
        """Set if the area should be used in ground plan

        Args:
            useArea: true if to use area
        """

class BlockFoundationProperties(VerticalElementProperties, ArchBaseProperties):
    """Implementation of the BlockFoundation properties
    """
    def GetShapeType(self) -> ShapeType:
        """Get Shape Type

        Returns:
            Shape Type
        """
    def GetVouteBack(self) -> float:
        """Get Voute Back

        Returns:
            Voute Back
        """
    def GetVouteFront(self) -> float:
        """Get Voute Front

        Returns:
            Voute Front
        """
    def GetVouteLeft(self) -> float:
        """Get Voute Left

        Returns:
            Voute Left
        """
    def GetVouteRight(self) -> float:
        """Get Voute Right

        Returns:
            Voute Right
        """
    def SetShapeType(self, ShapeType: ShapeType):
        """Set the ShapeType

        Args:
            ShapeType:Shape Type
        """
    def SetVouteBack(self, VouteBack: float):
        """Set the VouteBack

        Args:
            VouteBack:Voute Back
        """
    def SetVouteFront(self, VouteFront: float):
        """Set the VouteFront

        Args:
            VouteFront:Voute Front
        """
    def SetVouteLeft(self, VouteLeft: float):
        """Set the VouteLeft

        Args:
            VouteLeft:Voute Left
        """
    def SetVouteRight(self, VouteRight: float):
        """Set the VouteRight

        Args:
            Voutefront:Voute Right
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, BlockFoundationProp: BlockFoundationProperties):
        """Copy constructor

        Args:
            BlockFoundationnProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def ShapeType(self) -> ShapeType:
        """Get the Shape Type
        """
    @ShapeType.setter
    def ShapeType(self, ShapeType: ShapeType) -> None:
        """Set the type of the shape

        Args:
            ShapeType: Shape Type
        """
    @property
    def VouteBack(self) -> float:
        """Get the Voute Back
        """
    @VouteBack.setter
    def VouteBack(self, VouteBack: float) -> None:
        """Set the Voute Back

        Args:
            VouteBack: Voute Back
        """
    @property
    def VouteFront(self) -> float:
        """Get the Voute Front
        """
    @VouteFront.setter
    def VouteFront(self, VouteFront: float) -> None:
        """Set the Voute Front

        Args:
            VouteFront: Voute Front
        """
    @property
    def VouteLeft(self) -> float:
        """Get the Voute Left
        """
    @VouteLeft.setter
    def VouteLeft(self, VouteLeft: float) -> None:
        """Set the Voute Left

        Args:
            VouteLeft: Voute Left
        """
    @property
    def VouteRight(self) -> float:
        """Get the Voute Right
        """
    @VouteRight.setter
    def VouteRight(self, VouteRight: float) -> None:
        """Set the Voute Right

        Args:
            VouteRight: Voute Right
        """

class VerticalOpeningFacingProperties():
    """Implementation of the vertical opening facing properties
    """
    def __init__(self, element: VerticalOpeningFacingProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def LeftDepth(self) -> float:
        """Get the left depth
        """
    @LeftDepth.setter
    def LeftDepth(self, leftDepth: float) -> None:
        """Set the left depth

        Args:
            leftDepth: Left depth
        """
    @property
    def LeftFacing(self) -> bool:
        """Get the left facing state
        """
    @LeftFacing.setter
    def LeftFacing(self, leftFacing: bool) -> None:
        """Set the left facing state

        Args:
            leftFacing: Left facing state
        """
    @property
    def LeftWidth(self) -> float:
        """Get the left width
        """
    @LeftWidth.setter
    def LeftWidth(self, leftWidth: float) -> None:
        """Set the left width

        Args:
            leftWidth: Left width
        """
    @property
    def OpeningSide(self) -> OpeningSide:
        """Get the opening side
        """
    @OpeningSide.setter
    def OpeningSide(self, openingSide: OpeningSide) -> None:
        """Set the opening side

        Args:
            openingSide: Opening side
        """
    @property
    def RightDepth(self) -> float:
        """Get the right depth
        """
    @RightDepth.setter
    def RightDepth(self, rightDepth: float) -> None:
        """Set the right depth

        Args:
            rightDepth: Right depth
        """
    @property
    def RightFacing(self) -> bool:
        """Get the right facing state
        """
    @RightFacing.setter
    def RightFacing(self, rightFacing: bool) -> None:
        """Set the right facing state

        Args:
            rightFacing: Right facing state
        """
    @property
    def RightWidth(self) -> float:
        """Get the right width
        """
    @RightWidth.setter
    def RightWidth(self, rightWidth: float) -> None:
        """Set the right width

        Args:
            rightWidth: Right width
        """
    @property
    def TopDepth(self) -> float:
        """Get the top depth
        """
    @TopDepth.setter
    def TopDepth(self, topDepth: float) -> None:
        """Set the top depth

        Args:
            topDepth: Top depth
        """
    @property
    def TopFacing(self) -> bool:
        """Get the top facing state
        """
    @TopFacing.setter
    def TopFacing(self, topFacing: bool) -> None:
        """Set the top facing state

        Args:
            topFacing: Top facing state
        """
    @property
    def TopWidth(self) -> float:
        """Get the top width
        """
    @TopWidth.setter
    def TopWidth(self, topWidth: float) -> None:
        """Set the top width

        Args:
            topWidth: Top width
        """

class VerticalOpeningGeometryProperties():
    """Implementation of the vertical opening geometry properties
    """
    def __init__(self, element: VerticalOpeningGeometryProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def Depth(self) -> float:
        """Get the depth
        """
    @Depth.setter
    def Depth(self, depth: float) -> None:
        """Set the depth

        Args:
            depth: Set the depth
        """
    @property
    def ProfilePath(self) -> str:
        """Get the full name of the profile
        """
    @ProfilePath.setter
    def ProfilePath(self, profilePath: str) -> None:
        """Set the full name of the profile

        Args:
            profilePath: Path and name of the profile
        """
    @property
    def RiseAtBottom(self) -> float:
        """Get the rise at the bottom
        """
    @RiseAtBottom.setter
    def RiseAtBottom(self, riseAtBottom: float) -> None:
        """Set the rise at the bottom

        Args:
            riseAtBottom: Rise at the bottom
        """
    @property
    def RiseAtTop(self) -> float:
        """Get the rise at the top
        """
    @RiseAtTop.setter
    def RiseAtTop(self, riseAtTop: float) -> None:
        """Set the rise at the top

        Args:
            riseAtTop: Rise at the top
        """
    @property
    def SegmentsAtBottom(self) -> int:
        """Get the segments of rise at bottom
        """
    @SegmentsAtBottom.setter
    def SegmentsAtBottom(self, segmentsBottom: int) -> None:
        """Set the segments of rise at bottom

        Args:
            segmentsBottom: Segments of rise at bottom
        """
    @property
    def SegmentsAtTop(self) -> int:
        """Get the segments of rise at top
        """
    @SegmentsAtTop.setter
    def SegmentsAtTop(self, segmentsTop: int) -> None:
        """Set the segments of rise at top

        Args:
            segmentsTop: Segments of rise at top
        """
    @property
    def Shape(self) -> VerticalOpeningShapeType:
        """Get the opening shape type
        """
    @Shape.setter
    def Shape(self, shape: VerticalOpeningShapeType) -> None:
        """Set the opening shape type

        Args:
            shape: Opening shape type
        """
    @property
    def ShapePolygon(self) -> NemAll_Python_Geometry.Polygon2D:
        """Get the shape polygon
        """
    @ShapePolygon.setter
    def ShapePolygon(self, shapePol: NemAll_Python_Geometry.Polygon2D) -> None:
        """Set the shape polygon

        Args:
            shapePol: Shape polygon
        """
    @property
    def Width(self) -> float:
        """Get the width
        """
    @Width.setter
    def Width(self, width: float) -> None:
        """Set the width

        Args:
            width: Set the width
        """

class VerticalOpeningRevealProperties():
    """Properties of the door/window reveal
    """
    def __init__(self, element: VerticalOpeningRevealProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def Depth(self) -> float:
        """Door/Window depth"""
    @Depth.setter
    def Depth(self, depth: float) -> None:
        """Set the depth

        Args:
            depth: Set the depth
        """
    @property
    def InnerOffset(self) -> float:
        """Offset to inner face (in case of inner reveal)"""
    @InnerOffset.setter
    def InnerOffset(self, innerOffset: float) -> None:
        """Set the inner offset

        Args:
            innerOffset: Inner offset
        """
    @property
    def OuterOffset(self) -> float:
        """Offset to outer face (in case of inner reveal)"""
    @OuterOffset.setter
    def OuterOffset(self, outerOffset: float) -> None:
        """Set the outer offset

        Args:
            outerOffset: Set the outer offset
        """
    @property
    def SideOffset(self) -> float:
        """Side offset (aka projection, in case of outer reveal)"""
    @SideOffset.setter
    def SideOffset(self, sideOffset: float) -> None:
        """Set the side offset

        Args:
            sideOffset: Set the side offset
        """
    @property
    def Type(self) -> VerticalOpeningRevealType:
        """Get the reveal Type
        """
    @Type.setter
    def Type(self, type: VerticalOpeningRevealType) -> None:
        """Set the reveal type

        Args:
            type: Reveal type
        """

class VerticalOpeningRevealType(enum.Enum):
    """Type of the reveal
    """
    eEmbedded = 1
    """Inner reveal object"""
    eExterior = 3
    """Outer reveal object - exterior reveal^"""
    eInterior = 2
    """Outer reveal object - interior reveal"""
    eNone = 0
    """no reveal"""

    names = {eNone: eNone,
             eEmbedded: eEmbedded,
             eInterior: eInterior,
             eExterior: eExterior}

    values = {0: eNone,
              1: eEmbedded,
              2: eInterior,
              3: eExterior}

    def __getitem__(self, key: (str | int | float)) -> VerticalOpeningRevealType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class VerticalOpeningShapeType(enum.Enum):
    """Shape of vertical opening (door or window)
    """
    eArbitrary = 6
    """Arbitrary shape"""
    eCircle = 2
    """Circle"""
    eDiamond = 1
    """Diamond"""
    eRectangle = 0
    """Rectangle"""
    eRiseBottomTop = 5
    """Rise at bottom and/or top"""
    eSemiCircle = 4
    """Semi circle"""
    eSemiDiamond = 3
    """Semi diamond"""

    names = {eRectangle: eRectangle,
             eDiamond: eDiamond,
             eCircle: eCircle,
             eSemiDiamond: eSemiDiamond,
             eSemiCircle: eSemiCircle,
             eRiseBottomTop: eRiseBottomTop,
             eArbitrary: eArbitrary}

    values = {0: eRectangle,
              1: eDiamond,
              2: eCircle,
              3: eSemiDiamond,
              4: eSemiCircle,
              5: eRiseBottomTop,
              6: eArbitrary}

    def __getitem__(self, key: (str | int | float)) -> VerticalOpeningShapeType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class VerticalOpeningSillProperties():
    """Implementation of the vertical opening properties
    """
    def __init__(self, element: VerticalOpeningSillProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, comProp: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties

        Args:
            comProp: Common properties
        """
    @property
    def Type(self) -> VerticalOpeningSillType:
        """Get the sill Type
        """
    @Type.setter
    def Type(self, type: VerticalOpeningSillType) -> None:
        """Set the sill type

        Args:
            type: Sill type                 Is polygonal state
        """

class VerticalOpeningSillType(enum.Enum):
    """Type of the sill

    eNone     : No sill
    eOuter    : Sill at the outer side
    eInner    : Sill at the inner side
    eBothsides: Sill on both sides
    """
    eBothsides = 3
    eInner = 2
    eNone = 0
    eOuter = 1

    names = {eNone: eNone,
             eOuter: eOuter,
             eInner: eInner,
             eBothsides: eBothsides}

    values = {0: eNone,
              1: eOuter,
              2: eInner,
              3: eBothsides}

    def __getitem__(self, key: (str | int | float)) -> VerticalOpeningSillType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class VerticalOpeningTierOffsetProperties():
    """Implementation of the vertical opening tier offset properties
    """
    def GetFacingProperties(self) -> VerticalOpeningFacingProperties:
        """Get the facing properties

        Returns:
            Facing properties reference
        """
    def __init__(self, element: VerticalOpeningTierOffsetProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @property
    def BottomOffset(self) -> float:
        """Get the bottom offset
        """
    @BottomOffset.setter
    def BottomOffset(self, bottomOffset: float) -> None:
        """Set the bottom offset

        Args:
            bottomOffset: Bottom offset
        """
    @property
    def BottomOffsets(self) -> list[float]:
        """Get the bottom offsets
        """
    @BottomOffsets.setter
    def BottomOffsets(self, bottomOffsets: list[float]) -> None:
        """Set the bottom offsets

        Args:
            bottomOffsets: Bottom offsets
        """
    @property
    def LeftOffset(self) -> float:
        """Get the left offset
        """
    @LeftOffset.setter
    def LeftOffset(self, leftOffset: float) -> None:
        """Set the left offset

        Args:
            leftOffset: Left offset
        """
    @property
    def LeftOffsets(self) -> list[float]:
        """Get the left offset
        """
    @LeftOffsets.setter
    def LeftOffsets(self, leftOffsets: list[float]) -> None:
        """Set the left offsets

        Args:
            leftOffsets: Left offsets
        """
    @property
    def RightOffset(self) -> float:
        """Get the right offset
        """
    @RightOffset.setter
    def RightOffset(self, rightOffset: float) -> None:
        """Set the right offset

        Args:
            rightOffset: Right offset
        """
    @property
    def RightOffsets(self) -> list[float]:
        """Get the right offsets
        """
    @RightOffsets.setter
    def RightOffsets(self, rightOffsets: list[float]) -> None:
        """Set the right offsets

        Args:
            rightOffsets: Right offsets
        """
    @property
    def TopOffset(self) -> float:
        """Get the top offset
        """
    @TopOffset.setter
    def TopOffset(self, topOffset: float) -> None:
        """Set the top offset

        Args:
            topOffset: Top offset
        """
    @property
    def TopOffsets(self) -> list[float]:
        """Get the top offsets
        """
    @TopOffsets.setter
    def TopOffsets(self, topOffsets: list[float]) -> None:
        """Set the top offsets

        Args:
            topOffsets: Top offsets
        """
    @property
    def Type(self) -> VerticalOpeningTierOffsetType:
        """Get the tier offset type
        """
    @Type.setter
    def Type(self, type: VerticalOpeningTierOffsetType) -> None:
        """Set the tier offset type

        Args:
            type: Tier offset type
        """

class VerticalOpeningTierOffsetType(enum.Enum):
    """Type of offset settings

    eNone           : No offset
    eOuterSide      : Offset at outer side
    eInnerSide      : Offset at inner side
    eAdvanced       : Advanced offset
    eWithOuterFacing: With outer facing
    eWithInnerFacing: With inner facing
    eUnsupported    : Unsupported
    """
    eAdvanced = 3
    """Advanced offset"""
    eInnerSide = 2
    """Offset at inner side"""
    eNone = 0
    """No offset"""
    eOuterSide = 1
    """Offset at outer side"""
    eUnsupported = 6
    """Unsupported"""
    eWithInnerFacing = 5
    """With inner facing"""
    eWithOuterFacing = 4
    """With outer facing"""

    names = {eNone: eNone,
             eOuterSide: eOuterSide,
             eInnerSide: eInnerSide,
             eAdvanced: eAdvanced,
             eWithOuterFacing: eWithOuterFacing,
             eWithInnerFacing: eWithInnerFacing,
             eUnsupported: eUnsupported}

    values = {0: eNone,
              1: eOuterSide,
              2: eInnerSide,
              3: eAdvanced,
              4: eWithOuterFacing,
              5: eWithInnerFacing,
              6: eUnsupported}

    def __getitem__(self, key: (str | int | float)) -> VerticalOpeningTierOffsetType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class WallAxisPosition(enum.Enum):
    """Position of the axis relative to the architectural component (any linear component, not only
    wall as the name might suggest).

    Following descriptions assume that:

    - the axis origins in (0,0)
    - it points in +X direction
    - _Extension_ property is set to -1

    """
    eCenter = 2
    """Axis is in the center of the architectural component. Set the _Distance_ property to the half of the component width!"""
    eFree = 8
    """Position is defined by in the _Distance_ property"""
    eLeft = 1
    """Axis is on the left side of the component (on the +Y side). Set the _Distance_ property to 0!"""
    eRight = 4
    """Axis is on the right side of the component (on the -Y side). Set the _Distance_ property to the width of the component!"""
    eUnknown = 0

    names = {eUnknown: eUnknown,
             eLeft: eLeft,
             eCenter: eCenter,
             eRight: eRight,
             eFree: eFree}

    values = {0: eUnknown,
              1: eLeft,
              2: eCenter,
              4: eRight,
              8: eFree}

    def __getitem__(self, key: (str | int | float)) -> WallAxisPosition:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class WallElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of a multilayer wall
    """
    def GetProperties(self) -> WallProperties:
        """Get the wall properties

        Returns:
            Wall properties
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetProperties(self, wallProp: WallProperties):
        """Set the wall properties

        Args:
            wallProp: Wall properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, wallProp: WallProperties, axis: object):
        """Constructor

        Args:
            wallProp: Wall properties
            axis:     Axis
        """
    @typing.overload
    def __init__(self, element: WallElement):
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
    @property
    def Properties(self) -> WallProperties:
        """Properties of the wall"""
    @Properties.setter
    def Properties(self, wallProp: WallProperties) -> None:
        """Set the wall properties

        Args:
            wallProp: Wall properties
        """

class WallProperties():
    """Representation of properties of a multi layer wall
    """
    def GetAxis(self) -> AxisProperties:
        """Get the axis properties

        Returns:
            Axis properties
        """
    def GetPathElementAxisType(self) -> int:
        """Get the axis type of the path element

        Returns:
            Axis type of the path element
        """
    def GetThickness(self) -> float:
        """Get the thickness

        Returns:
            Thickness
        """
    def GetTierCount(self) -> int:
        """Get the tier count

        Returns:
            Tier count
        """
    def GetWallTierProperties(self, tierIndex: int) -> WallTierProperties:
        """Get the properties of a specified wall tier

        Args:
            tierIndex: Tier index. **First tier has the index 1!**

        Returns:
            Wall tier properties
        """
    def LoadFromFavoriteFile(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Load the properties from the favorite file

        Args:
            doc: Document
        """
    def SetAxis(self, axis: AxisProperties):
        """Set the axis

        Args:
            axis: Axis properties
        """
    def SetPathElementAxisType(self, pathEleAxisType: int):
        """Set the axis type of the path element

        Args:
            pathEleAxisType: Axis type of the path element
        """
    def SetTierCount(self, tierCount: int):
        """Set the tier count

        Args:
            tierCount: Tier count
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, wallProp: WallProperties):
        """Copy constructor

        Args:
            wallProp: Wall properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Axis(self) -> AxisProperties:
        """Get the axis properties
        """
    @Axis.setter
    def Axis(self, axis: AxisProperties) -> None:
        """Set the axis

        Args:
            axis: Axis properties
        """
    @property
    def PathElementAxisType(self) -> int:
        """Get the axis type of the path element
        """
    @PathElementAxisType.setter
    def PathElementAxisType(self, pathEleAxisType: int) -> None:
        """Set the axis type of the path element

        Args:
            pathEleAxisType: Axis type of the path element
        """
    @property
    def StartNewJoinedWallGroup(self) -> bool:
        """Get the state for starting a new joined wall group

        All walls in a group are used for to create a continues join
        between the walls.
        """
    @StartNewJoinedWallGroup.setter
    def StartNewJoinedWallGroup(self, startNewJoinedWallGroup: bool) -> None:
        """Set the state for starting a new joined wall group.
        All walls in a group are used for to create a continues join
        between the walls.

        Args:
            startNewJoinedWallGroup: Start new path group
        """
    @property
    def TierCount(self) -> int:
        """Get the tier count
        """
    @TierCount.setter
    def TierCount(self, tierCount: int) -> None:
        """Set the tier count

        Args:
            tierCount: Tier count
        """

class WallTierProperties(ArchBaseProperties):
    """Representation of the properties of a single layer of a multi layer wall
    """
    def GetThickness(self) -> float:
        """Get the wall layer thickness

        Returns:
            Thickness
        """
    def SetThickness(self, thickness: float):
        """Set the wall layer thickness

        Args:
            thickness:  Thickness
        """
    def __init__(self, tierProp: WallTierProperties):
        """Copy constructor

        Args:
            tierProp: Tier properties to copy
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Thickness(self) -> float:
        """Tier thickness"""
    @Thickness.setter
    def Thickness(self, thickness: float) -> None:
        """Set the thickness

        Args:
            thickness: Thickness
        """

class WindowOpeningElement(ArchElement, NemAll_Python_BasisElements.AllplanElement):
    """Representation of window opening
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, openingProp: WindowOpeningProperties, generalEle: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                 startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D, drawPlacementPreview: bool):
        """Constructor

        Args:
            openingProp:          Opening properties
            generalEle:           General element which includes the opening
            startPnt:             Start point of the opening
            endPnt:               End point
            drawPlacementPreview: Draw as placement preview (no wall adaptions) state
        """
    @typing.overload
    def __init__(self, element: WindowOpeningElement):
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
    @property
    def EndPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the end point
        """
    @EndPoint.setter
    def EndPoint(self, endPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the end point

        Args:
            endPoint: End point
        """
    @property
    def Properties(self) -> WindowOpeningProperties:
        """Window opening properties"""
    @Properties.setter
    def Properties(self, WindowOpeningProp: WindowOpeningProperties) -> None:
        """Set the WindowOpening properties

        Args:
            WindowOpeningProp: General opening properties
        """
    @property
    def StartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the start point
        """
    @StartPoint.setter
    def StartPoint(self, startPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the start point

        Args:
            startPoint: Start point
        """

class WindowOpeningProperties():
    """Properties of window opening
    """
    def GetGeometryProperties(self) -> VerticalOpeningGeometryProperties:
        """Get a reference of the geometry properties

        Returns:
            Geometry properties reference
        """
    def GetOpeningSymbolsProperties(self) -> OpeningSymbolsProperties:
        """Get a reference of the opening symbols properties

        Returns:
            Opening symbols properties reference
        """
    def GetRevealProperties(self) -> VerticalOpeningRevealProperties:
        """Get a reference of the reveal properties

        Returns:
            Reveal properties reference
        """
    def GetSillProperties(self) -> VerticalOpeningSillProperties:
        """Get a reference of the sill properties

        Returns:
            Sill properties reference
        """
    def GetTierOffsetProperties(self) -> VerticalOpeningTierOffsetProperties:
        """Get a reference of the tier offset properties

        Returns:
            Tier offset properties reference
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, windowProp: WindowOpeningProperties):
        """Copy constructor

        Args:
            windowProp: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Independent2DInteraction(self) -> bool:
        """Set to True, when the opening is above/below the section plane and should therefor NOT interact with the hatching/filling of the parent architectural element in ground view. Defaults to False."""
    @Independent2DInteraction.setter
    def Independent2DInteraction(self, isIndependent2DInteraction: bool) -> None:
        """Set the independent 2D interaction state

        Args:
            isIndependent2DInteraction: Independent 2D interaction state
        """
    @property
    def PlaneReferences(self) -> PlaneReferences:
        """Get the plane references
        """
    @PlaneReferences.setter
    def PlaneReferences(self, planeRef: PlaneReferences) -> None:
        """Set the plane references

        Args:
            planeRef: Plane references
        """


```