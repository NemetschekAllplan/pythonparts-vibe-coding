---
title: "NemAll_Python_Precast"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_Precast.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_Precast

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_Precast.pyi`  
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

"""Exposed classes and functions from NemAll_Python_Precast"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_BaseElements
import NemAll_Python_Geometry
import NemAll_Python_IFW_ElementAdapter
import NemAll_Python_IFW_Input


__all__ = [
    "AlignmentProperties",
    "AllowedElements",
    "Anchor",
    "AnchorBorderPosition",
    "AssemblyGroupElement",
    "Cell",
    "ClippingPathProperties",
    "CreateElementplan",
    "CreatePrecastElements",
    "DimensioningProperties",
    "Direction",
    "DirectionMode",
    "DirectionProperties",
    "FileEntryPath",
    "FinishProperties",
    "FixtureCombinationType",
    "FixtureElement",
    "FixtureGroupElement",
    "FixtureGroupProperties",
    "FixturePlacementElement",
    "FixturePlacementProperties",
    "FixtureProperties",
    "FixtureSlideElement",
    "FixtureSlideProperties",
    "FixtureSlideType",
    "FixtureSlideViewType",
    "FormatProperties",
    "GetLayoutNameFromOffset",
    "GetPagePropertiesFromCatalog",
    "GetPrecastMandant",
    "HeadingProperties",
    "HeightDefinitionType",
    "LabelStyle",
    "LabelStyleProperties",
    "LabelingProperties",
    "Legend",
    "LegendProperties",
    "LightProperties",
    "LineProperties",
    "Location",
    "LockPrecastUpdate",
    "MacroGroupType",
    "MacroSubType",
    "MacroType",
    "OutlineShape",
    "OutlineType",
    "OutlineTypeInGroup",
    "Page",
    "PageProperties",
    "PagePropertiesList",
    "Plan",
    "Position",
    "PrecastCatalogService",
    "PrecastElement",
    "PrecastElementProperties",
    "PrecastLayer",
    "PrecastLayerProperties",
    "PrecastMWSElement",
    "PrecastProperties",
    "ProcessListGen",
    "ProfilType",
    "RepresentationProperties",
    "Rotation",
    "ScaleProperties",
    "SectionProperties",
    "SubType",
    "SurfaceProperties",
    "TextAlignment",
    "TextParameters",
    "TextProperties",
    "TriggerPrecastUpdate",
    "Type",
    "UnlockPrecastUpdate",
    "View",
    "ViewProperties",
    "VisibilityProperties",
    "e2D_BACK_VIEW",
    "e2D_FRONT_VIEW",
    "e2D_LEFT_VIEW",
    "e2D_NO_VIEW",
    "e2D_RIGHT_VIEW",
    "e2D_SYMBOL",
    "e2D_TOP_VIEW",
    "e3D_VIEW",
    "e3D_VIEW_OLD",
    "e3D_VIEW_OUTLINE_AREA",
    "e3D_VIEW_OUTLINE_AREA_ACTUAL",
    "e3D_VIEW_OUTLINE_VOLUME",
    "eAccordingTheUSStandard",
    "eAll",
    "eAnchorPlate",
    "eAnchorage",
    "eAverage",
    "eBOTTOM_VIEW",
    "eBUILTIN_OUTLINE_SHAPE_NOTHING",
    "eBUILTIN_OUTLINE_SHAPE_RECTANGLE",
    "eBUILTIN_OUTLINE_SHAPE_SYMBOL",
    "eBUILTIN_OUTLINE_SHAPE_TRAPEZOID",
    "eBUILTIN_OUTLINE_TYPE_IN_GROUP_MINUS",
    "eBUILTIN_OUTLINE_TYPE_IN_GROUP_NOTHING",
    "eBUILTIN_OUTLINE_TYPE_IN_GROUP_PLUS",
    "eBUILTIN_OUTLINE_TYPE_MINUS",
    "eBUILTIN_OUTLINE_TYPE_NOTHING",
    "eBUILTIN_OUTLINE_TYPE_NO_AFFECT",
    "eBUILTIN_OUTLINE_TYPE_PLUS",
    "eBUILTIN_PROFIL_TYPE_EDGE",
    "eBUILTIN_PROFIL_TYPE_JOINT",
    "eBarAccessory",
    "eBarCoupler",
    "eBarNut",
    "eBarThread",
    "eBorderBottom",
    "eBorderHorizontal",
    "eBorderInnerBottom",
    "eBorderInnerHorizontal",
    "eBorderInnerLeft",
    "eBorderInnerRight",
    "eBorderInnerTop",
    "eBorderInnerVertical",
    "eBorderLeft",
    "eBorderRight",
    "eBorderTop",
    "eBorderVertical",
    "eBottomCenter",
    "eBottomLeft",
    "eBottomRight",
    "eBracingElement",
    "eCONNECTION_POINT",
    "eCONTOUR_CUT",
    "eCatchmentArea",
    "eCenter",
    "eChannel",
    "eCirculationLoadPoint",
    "eCirculationPipeAdapter",
    "eCirculationStartPoint",
    "eCode",
    "eComponent",
    "eConcreteArea",
    "eConcreteBeam",
    "eConcreteBlock",
    "eConnectionModeller",
    "eConnectionWallColumn",
    "eConnectorEBT",
    "eConstPrefabConnection",
    "eCorbel",
    "eCornerInnerLeftBottom",
    "eCornerInnerLeftTop",
    "eCornerInnerRightBottom",
    "eCornerInnerRightTop",
    "eCornerLeftBottom",
    "eCornerLeftTop",
    "eCornerRightBottom",
    "eCornerRightTop",
    "eCoverMountingAngle",
    "eCrossRib",
    "eDirectionI",
    "eDirectionII",
    "eDirectionIII",
    "eDirectionIV",
    "eDirectionV",
    "eDirectionVI",
    "eElectricalBIE",
    "eElectricalLamp",
    "eElectricalRoute",
    "eExtension",
    "eFacility",
    "eFalseJoint",
    "eFileEntryPathLibrary",
    "eFileEntryPathOffice",
    "eFileEntryPathPrivate",
    "eFileEntryPathProject",
    "eFileEntryPathProjectPlus",
    "eFileEntryPathStandard",
    "eFill",
    "eFrame",
    "eFull",
    "eGeometry",
    "eGroupType_CuttedGroup",
    "eGroupType_DynamicGroup",
    "eGroupType_GeneralGroup",
    "eGroupType_LeadingGroup",
    "eGroup_Fixture",
    "eHeatingLoadPoint",
    "eHeatingPipeAdapter",
    "eHeatingStartPoint",
    "eHollowBody",
    "eInsertion",
    "eInsulationArea",
    "eInsulationElement",
    "eInsulationStripe",
    "eJointLength",
    "eJointReinforcement",
    "eLOCK_FIXED",
    "eLOCK_FIXED_P1",
    "eLOCK_UML",
    "eLeftBottom",
    "eLeftCenter",
    "eLeftTop",
    "eLinePointPlacement",
    "eLine_Fixture",
    "eLoadCut",
    "eMEASURE_POINTS",
    "eMacro",
    "eMultiLine3D",
    "eNailer",
    "eNode",
    "eNone",
    "eORGA_ORIGINAL",
    "eOnlyThese",
    "eOverrule",
    "ePipe",
    "ePipePoint",
    "ePlacingLoop",
    "ePlane_Fixture",
    "ePoint_Fixture",
    "ePolyline",
    "ePrefabConnection",
    "ePrefabConnectionCorner",
    "ePrefabModeller",
    "eProfileEdge",
    "eReinforcement",
    "eReinforcement_Cage",
    "eReport",
    "eRestricted",
    "eRevealAnchor",
    "eRevealAnchorVirtual",
    "eRibBody",
    "eRightBottom",
    "eRightCenter",
    "eRightTop",
    "eRingBeam",
    "eRoofLine",
    "eRoofParapetLine",
    "eRoofParapetSupport",
    "eRope",
    "eRotation0",
    "eRotation180",
    "eRotation270",
    "eRotation90",
    "eSTD_Formwork",
    "eSanitationLoadPoint",
    "eSanitationPipeAdapter",
    "eSanitationStartPoint",
    "eSecondaryReinf",
    "eSewageLoadPoint",
    "eSewageNetElement",
    "eSewagePipeAdapter",
    "eSewageStartPoint",
    "eShaft",
    "eSlidingRestraint",
    "eSolidStrip",
    "eSpecialBuilding",
    "eSpecialLoad_Undefined",
    "eSpecialLoad_X",
    "eSpecialLoad_Y",
    "eSpecialLoad_Z",
    "eSphere",
    "eSteelProfile",
    "eStripCorbel",
    "eStructuralRecessFaceSupport",
    "eStructuralRecessLongitudinalSupport",
    "eSurface",
    "eTGA_ADAPTER",
    "eTheseNot",
    "eTieBar",
    "eTileArea",
    "eTileElement",
    "eTopCenter",
    "eTopLeft",
    "eTopRight",
    "eTrimmer",
    "eUndergroundCadaster",
    "eUnknownAlignment",
    "eUseNoSpecialSubType",
    "eUseSameSubType",
    "eUseSameType",
    "eVentilationDuctAdapter",
    "eVentilationLoadPoint",
    "eVentilationStartPoint",
    "eVx",
    "eVy",
    "eVz",
    "eZone"
]


class AlignmentProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def DistanceDimensionLine(self) -> float:
        """Get the distance of the dimension lines between dimension lines
        """
    @DistanceDimensionLine.setter
    def DistanceDimensionLine(self, value: float) -> None:
        """Set the distance of the dimension lines between dimension lines

        Args:
            value: value to set
        """
    @property
    def DistanceToView(self) -> float:
        """Get the distance of the first dimension line to the view
        """
    @DistanceToView.setter
    def DistanceToView(self, value: float) -> None:
        """Set the distance of the first dimension line to the view

        Args:
            value: value to set
        """
    @property
    def UseDynamicDistance(self) -> bool:
        """Get if the distance between dimension lines will be dynamically calculated
        """
    @UseDynamicDistance.setter
    def UseDynamicDistance(self, value: bool) -> None:
        """Set if the distance between dimension lines will be dynamically calculated

        Args:
            value: value to set
        """

class AllowedElements(enum.Enum):
    """allowed elements for visibility
    """
    eAll = 0
    eOnlyThese = 1
    eTheseNot = 2

    names = {eAll: eAll,
             eOnlyThese: eOnlyThese,
             eTheseNot: eTheseNot}

    values = {0: eAll,
              1: eOnlyThese,
              2: eTheseNot}

    def __getitem__(self, key: (str | int | float)) -> AllowedElements:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class Anchor():

    @typing.overload
    def __init__(self, id: int, fromId: int, fromPos: AnchorBorderPosition, toId: int, toPos: AnchorBorderPosition):
        """Constructor

        Args:
            Anchor:ID
            From:cell ID
            From:cell pos
            To:cell ID
            To:cell pos
        """
    @typing.overload
    def __init__(self, id: int, fromId: int, fromPos: AnchorBorderPosition, toId: int, toPos: AnchorBorderPosition, align: bool,
                 offsetX: float, offsetY: float):
        """Constructor

        Args:
            Anchor:ID
            From:cell ID
            From:cell pos
            To:cell ID
            To:cell pos
            Align:
            Offset:x
            Offset:y
        """
    @typing.overload
    def __init__(self, id: int, fromPos: AnchorBorderPosition, toId: int, toPos: AnchorBorderPosition):
        """Constructor

        Args:
            Anchor:ID
            From:cell pos
            To:cell ID
            To:cell pos
        """
    @typing.overload
    def __init__(self, id: int, fromPos: AnchorBorderPosition, toId: int, toPos: AnchorBorderPosition, offsetX: float, offsetY: float):
        """Constructor

        Args:
            Anchor:ID
            From:cell pos
            To:cell ID
            To:cell pos
            Offset:x
            Offset:y
        """
    @typing.overload
    def __init__(self, id: int, fromCell: Cell, fromPos: AnchorBorderPosition, toCell: Cell, toPos: AnchorBorderPosition):
        """Constructor

        Args:
            Anchor:ID
            From:cell
            From:cell pos
            To:cell
            To:cell pos
        """
    @typing.overload
    def __init__(self, id: int, fromCell: Cell, fromPos: AnchorBorderPosition, toCell: Cell, toPos: AnchorBorderPosition, align: bool,
                 offsetX: float, offsetY: float):
        """Constructor

        Args:
            Anchor:ID
            From:cell
            From:cell pos
            To:cell
            To:cell pos
            Align:
            Offset:x
            Offset:y
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class AnchorBorderPosition(enum.Enum):
    """anchor border positions
    """
    eBorderBottom = 2
    eBorderHorizontal = 3
    eBorderInnerBottom = 4098
    eBorderInnerHorizontal = 4099
    eBorderInnerLeft = 4100
    eBorderInnerRight = 4104
    eBorderInnerTop = 4097
    eBorderInnerVertical = 4108
    eBorderLeft = 4
    eBorderRight = 8
    eBorderTop = 1
    eBorderVertical = 12
    eCornerInnerLeftBottom = 4102
    eCornerInnerLeftTop = 4101
    eCornerInnerRightBottom = 4106
    eCornerInnerRightTop = 4105
    eCornerLeftBottom = 6
    eCornerLeftTop = 5
    eCornerRightBottom = 10
    eCornerRightTop = 9

    names = {eBorderLeft: eBorderLeft,
             eBorderTop: eBorderTop,
             eBorderRight: eBorderRight,
             eBorderBottom: eBorderBottom,
             eCornerLeftTop: eCornerLeftTop,
             eCornerLeftBottom: eCornerLeftBottom,
             eCornerRightTop: eCornerRightTop,
             eCornerRightBottom: eCornerRightBottom,
             eBorderHorizontal: eBorderHorizontal,
             eBorderVertical: eBorderVertical,
             eCornerInnerLeftTop: eCornerInnerLeftTop,
             eCornerInnerLeftBottom: eCornerInnerLeftBottom,
             eCornerInnerRightTop: eCornerInnerRightTop,
             eCornerInnerRightBottom: eCornerInnerRightBottom,
             eBorderInnerTop: eBorderInnerTop,
             eBorderInnerBottom: eBorderInnerBottom,
             eBorderInnerLeft: eBorderInnerLeft,
             eBorderInnerRight: eBorderInnerRight,
             eBorderInnerHorizontal: eBorderInnerHorizontal,
             eBorderInnerVertical: eBorderInnerVertical}

    values = {4: eBorderLeft,
              1: eBorderTop,
              8: eBorderRight,
              2: eBorderBottom,
              5: eCornerLeftTop,
              6: eCornerLeftBottom,
              9: eCornerRightTop,
              10: eCornerRightBottom,
              3: eBorderHorizontal,
              12: eBorderVertical,
              4101: eCornerInnerLeftTop,
              4102: eCornerInnerLeftBottom,
              4105: eCornerInnerRightTop,
              4106: eCornerInnerRightBottom,
              4097: eBorderInnerTop,
              4098: eBorderInnerBottom,
              4100: eBorderInnerLeft,
              4104: eBorderInnerRight,
              4099: eBorderInnerHorizontal,
              4108: eBorderInnerVertical}

    def __getitem__(self, key: (str | int | float)) -> AnchorBorderPosition:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PrecastElement(NemAll_Python_BasisElements.AllplanElement):

    @staticmethod
    def GetPrecastLayersFromCatalog(precastElementName: str) -> list[tuple[string, int]]:
        """Returns the list of available layers for the selected PrecastElement

        Args:
            precastElementName: name of the selected Precast element

        Returns:
            list(tuple(Name of the PrecastLayer, Materialtype of the PrecastLayer))
        """
    def __init__(self, Properties: PrecastElementProperties):
        """Constructor

        Args:
            elementProp: Element properties
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Properties(self) -> None:
        """Property for Precast Element Properties
        Value type: PrecastElementProperties


        :type: None
        """
    @property
    def deletePython(self) -> None:
        """Property to delete Python after elementation
        Value type: int


        :type: None
        """

class Cell():

    @typing.overload
    def GetCell(self) -> object:
        """
        """
    @typing.overload
    def GetCell(self):
        """
        """
    def GetCell(self):
        """ Overloaded function. See individual overloads.
        """

class ClippingPathProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def ClippingLineFull(self) -> bool:
        """Get the Clipping line full of the clipping path
        """
    @ClippingLineFull.setter
    def ClippingLineFull(self, value: bool) -> None:
        """Set the Clipping line full of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingLineSegmentLength(self) -> float:
        """Get the Segment length of the clipping path
        """
    @ClippingLineSegmentLength.setter
    def ClippingLineSegmentLength(self, value: float) -> None:
        """Set the Segment length of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineColor(self) -> int:
        """Get the Color of the clipping line
        """
    @ClippingPathLineColor.setter
    def ClippingPathLineColor(self, value: int) -> None:
        """Set the Color of the clipping line

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineEndSymbolHeight(self) -> float:
        """Get the Line end symbol height of the clipping path
        """
    @ClippingPathLineEndSymbolHeight.setter
    def ClippingPathLineEndSymbolHeight(self, value: float) -> None:
        """Set the Line end symbol height of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineEndSymbolNr(self) -> int:
        """Get the Line end symbol number of the clipping path
        """
    @ClippingPathLineEndSymbolNr.setter
    def ClippingPathLineEndSymbolNr(self, value: int) -> None:
        """Set the Line end symbol number of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineEndSymbolOn(self) -> bool:
        """Get the Line end symbol on flag of the clipping path
        """
    @ClippingPathLineEndSymbolOn.setter
    def ClippingPathLineEndSymbolOn(self, value: bool) -> None:
        """Set the Line end symbol on flag of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineSymbolHeight(self) -> float:
        """Get the Line symbol height of the clipping path
        """
    @ClippingPathLineSymbolHeight.setter
    def ClippingPathLineSymbolHeight(self, value: float) -> None:
        """Set the Line symbol height of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineSymbolNr(self) -> int:
        """Get the Line symbol number of the clipping path
        """
    @ClippingPathLineSymbolNr.setter
    def ClippingPathLineSymbolNr(self, value: int) -> None:
        """Set the Line symbol number of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineSymbolOn(self) -> bool:
        """Get the Line symbol on flag of the clipping path
        """
    @ClippingPathLineSymbolOn.setter
    def ClippingPathLineSymbolOn(self, value: bool) -> None:
        """Set the Line symbol on flag of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathLineType(self) -> int:
        """Get the Line type of the clipping path
        """
    @ClippingPathLineType.setter
    def ClippingPathLineType(self, value: int) -> None:
        """Set the Line type of the clipping path

        Args:
            value: value to set
        """
    @property
    def ClippingPathPen(self) -> int:
        """Get the Line pen of the clipping path
        """
    @ClippingPathPen.setter
    def ClippingPathPen(self, value: int) -> None:
        """Set the Line pen of the clipping path

        Args:
            value: value to set
        """
    @property
    def EndTextProps(self) -> TextProperties:
        """Get the End text properties of the clipping path
        """
    @EndTextProps.setter
    def EndTextProps(self, value: TextProperties) -> None:
        """Set the End text properties of the clipping path

        Args:
            value: value to set
        """
    @property
    def PlaceClippingLine(self) -> bool:
        """Get the Place clipping line of the clipping path
        """
    @PlaceClippingLine.setter
    def PlaceClippingLine(self, value: bool) -> None:
        """Set the Place clipping line of the clipping path

        Args:
            value: value to set
        """
    @property
    def SectionsToShow(self) -> list:
        """Get the List of sections to show
        """
    @SectionsToShow.setter
    def SectionsToShow(self, value: list) -> None:
        """Set the List of sections to show

        Args:
            value: value to set
        """
    @property
    def StartTextProps(self) -> TextProperties:
        """Get the Start text properties of the clipping path
        """
    @StartTextProps.setter
    def StartTextProps(self, value: TextProperties) -> None:
        """Set the Start text properties of the clipping path

        Args:
            value: value to set
        """

class DimensioningProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def Associative(self) -> bool:
        """Get if the dimension lines should be created as associative dimension lines
        """
    @Associative.setter
    def Associative(self, value: bool) -> None:
        """Set if the dimension lines should be created as associative dimension lines

        Args:
            value: value to set
        """
    @property
    def Horizontal(self) -> AlignmentProperties:
        """Get the alignment properties for horizontal dimension lines
        """
    @Horizontal.setter
    def Horizontal(self, value: AlignmentProperties) -> None:
        """Set the alignment properties for horizontal dimension lines

        Args:
            value: value to set
        """
    @property
    def Rules(self) -> list:
        """Get the rule which should be used for dimension the elements inside the view
        """
    @Rules.setter
    def Rules(self, value: list) -> None:
        """Set the rule which should be used for dimension the elements inside the view

        Args:
            value: value to set
        """
    @property
    def Vertical(self) -> AlignmentProperties:
        """Get the alignment properties for vertical dimension lines
        """
    @Vertical.setter
    def Vertical(self, value: AlignmentProperties) -> None:
        """Set the alignment properties for vertical dimension lines

        Args:
            value: value to set
        """

class Direction(enum.Enum):
    """directions for views
    """
    eDirectionI = 1
    eDirectionII = 2
    eDirectionIII = 3
    eDirectionIV = 4
    eDirectionV = 5
    eDirectionVI = 6

    names = {eDirectionI: eDirectionI,
             eDirectionII: eDirectionII,
             eDirectionIII: eDirectionIII,
             eDirectionIV: eDirectionIV,
             eDirectionV: eDirectionV,
             eDirectionVI: eDirectionVI}

    values = {1: eDirectionI,
              2: eDirectionII,
              3: eDirectionIII,
              4: eDirectionIV,
              5: eDirectionV,
              6: eDirectionVI}

    def __getitem__(self, key: (str | int | float)) -> Direction:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class DirectionMode(enum.Enum):
    """mode for directions
    """
    eFull = 1
    eRestricted = 0

    names = {eRestricted: eRestricted,
             eFull: eFull}

    values = {0: eRestricted,
              1: eFull}

    def __getitem__(self, key: (str | int | float)) -> DirectionMode:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class DirectionProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def CutPosition(self) -> float:
        """Get the Cut position of the direction props
        """
    @CutPosition.setter
    def CutPosition(self, value: float) -> None:
        """Set the Cut position of the direction props

        Args:
            value: value to set
        """
    @property
    def CutWidth(self) -> float:
        """Get the Cut width of the direction props
        """
    @CutWidth.setter
    def CutWidth(self, value: float) -> None:
        """Set the Cut width of the direction props

        Args:
            value: value to set
        """
    @property
    def Mode(self) -> DirectionMode:
        """Get the Mode of the direction props
        """
    @Mode.setter
    def Mode(self, value: DirectionMode) -> None:
        """Set the Mode of the direction props

        Args:
            value: value to set
        """

class FileEntryPath(enum.Enum):
    """paths
    """
    eFileEntryPathLibrary = 5
    eFileEntryPathOffice = 1
    eFileEntryPathPrivate = 2
    eFileEntryPathProject = 3
    eFileEntryPathProjectPlus = 4
    eFileEntryPathStandard = 0

    names = {eFileEntryPathStandard: eFileEntryPathStandard,
             eFileEntryPathOffice: eFileEntryPathOffice,
             eFileEntryPathPrivate: eFileEntryPathPrivate,
             eFileEntryPathProject: eFileEntryPathProject,
             eFileEntryPathProjectPlus: eFileEntryPathProjectPlus,
             eFileEntryPathLibrary: eFileEntryPathLibrary}

    values = {0: eFileEntryPathStandard,
              1: eFileEntryPathOffice,
              2: eFileEntryPathPrivate,
              3: eFileEntryPathProject,
              4: eFileEntryPathProjectPlus,
              5: eFileEntryPathLibrary}

    def __getitem__(self, key: (str | int | float)) -> FileEntryPath:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class FinishProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def ApplySurfaceElemToFinishSurfaces(self) -> bool:
        """Get the Apply surface elements to finish surfaces flag
        """
    @ApplySurfaceElemToFinishSurfaces.setter
    def ApplySurfaceElemToFinishSurfaces(self, value: bool) -> None:
        """Set the Apply surface elements to finish surfaces flag

        Args:
            value: value to set
        """
    @property
    def FinishLinesColor(self) -> int:
        """Get the Color of the finish lines
        """
    @FinishLinesColor.setter
    def FinishLinesColor(self, value: int) -> None:
        """Set the Color of the finish lines

        Args:
            value: value to set
        """
    @property
    def FinishLinesLayer(self) -> int:
        """Get the Layer of the finish lines
        """
    @FinishLinesLayer.setter
    def FinishLinesLayer(self, value: int) -> None:
        """Set the Layer of the finish lines

        Args:
            value: value to set
        """
    @property
    def FinishLinesLineType(self) -> int:
        """Get the Line type of the finish lines
        """
    @FinishLinesLineType.setter
    def FinishLinesLineType(self, value: int) -> None:
        """Set the Line type of the finish lines

        Args:
            value: value to set
        """
    @property
    def FinishLinesPen(self) -> int:
        """Get the Pen of the finish lines
        """
    @FinishLinesPen.setter
    def FinishLinesPen(self, value: int) -> None:
        """Set the Pen of the finish lines

        Args:
            value: value to set
        """
    @property
    def IsFinishLinesColorFromLayer(self) -> bool:
        """Get the Is color for finish lines from layer flag
        """
    @IsFinishLinesColorFromLayer.setter
    def IsFinishLinesColorFromLayer(self, value: bool) -> None:
        """Set the Is color for finish lines from layer flag

        Args:
            value: value to set
        """
    @property
    def IsFinishLinesLineTypeFromLayer(self) -> bool:
        """Get the Is tpye of line for finish lines from layer flag
        """
    @IsFinishLinesLineTypeFromLayer.setter
    def IsFinishLinesLineTypeFromLayer(self, value: bool) -> None:
        """Set the Is tpye of line for finish lines from layer flag

        Args:
            value: value to set
        """
    @property
    def IsFinishLinesPenFromLayer(self) -> bool:
        """Get the Is pen for finish lines from layer flag
        """
    @IsFinishLinesPenFromLayer.setter
    def IsFinishLinesPenFromLayer(self, value: bool) -> None:
        """Set the Is pen for finish lines from layer flag

        Args:
            value: value to set
        """
    @property
    def ShowCeilingSurfaces(self) -> bool:
        """Get the Show ceiling surfaces flag
        """
    @ShowCeilingSurfaces.setter
    def ShowCeilingSurfaces(self, value: bool) -> None:
        """Set the Show ceiling surfaces flag

        Args:
            value: value to set
        """
    @property
    def ShowEntireStructOnly(self) -> bool:
        """Get the Show show entire struct only flag
        """
    @ShowEntireStructOnly.setter
    def ShowEntireStructOnly(self, value: bool) -> None:
        """Set the Show show entire struct only flag

        Args:
            value: value to set
        """
    @property
    def ShowFloorSurfaces(self) -> bool:
        """Get the Show floor surfaces flag
        """
    @ShowFloorSurfaces.setter
    def ShowFloorSurfaces(self, value: bool) -> None:
        """Set the Show floor surfaces flag

        Args:
            value: value to set
        """
    @property
    def ShowVerticalSurfaces(self) -> bool:
        """Get the Show vertical surfaces flag
        """
    @ShowVerticalSurfaces.setter
    def ShowVerticalSurfaces(self, value: bool) -> None:
        """Set the Show vertical surfaces flag

        Args:
            value: value to set
        """

class FixtureCombinationType(enum.Enum):
    """Fixture combination types
    """
    eVx = 1
    eVy = 2
    eVz = 3

    names = {eVx: eVx,
             eVy: eVy,
             eVz: eVz}

    values = {1: eVx,
              2: eVy,
              3: eVz}

    def __getitem__(self, key: (str | int | float)) -> FixtureCombinationType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class FixtureElement(PrecastElement, NemAll_Python_BasisElements.AllplanElement):
    """FixtureElement class
    """
    def GetFixtureProperties(self) -> FixtureProperties:
        """Get the Fixture properties

        Returns:
             Fixture properties
        """
    def GetHash(self) -> str:
        """Get the hash value

        Returns:
             Hash value
        """
    def GetSlideList(self) -> list:
        """Get the slide object list

        Returns:
             Slide object list
        """
    def SetFixtureProperties(self, fixProp: FixtureProperties):
        """Set the Fixture properties

        Args:
            fixProp: fixture properties
        """
    def SetHash(self, hash: str):
        """Set the hash value

        Args:
            hash:Hash value
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, fixProp: FixtureProperties, slideList: list):
        """Constructor

        Args:
            fixProp:        Fixture properties
            slideList:      Slide list of fixture definition
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class FixtureGroupElement(PrecastElement, NemAll_Python_BasisElements.AllplanElement):
    """FixtureGroupElement class
    """
    def GetFixtureGroupProperties(self) -> FixtureGroupProperties:
        """Get the FixtureGroup properties

        Returns:
             FixtureGroup properties
        """
    def GetFixtureList(self) -> list:
        """Get the fixture object list

        Returns:
             Fixture object list
        """
    def SetFixtureGroupProperties(self, FixtureGroupProp: FixtureGroupProperties):
        """Set the FixtureGroup properties

        Args:
            FixtureGroupProp: FixtureGroup properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, FixtureGroupProp: FixtureGroupProperties, slideList: list):
        """Constructor

        Args:
            FixtureGroupProp: FixtureGroup properties
            placementList:  Placement list of macro group
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, FixtureGroupProp: FixtureGroupProperties, slideList: list):
        """Constructor

        Args:
            commonProp:     Common properties
            FixtureGroupProp: FixtureGroup properties
            placementList:  Placement list of macro group
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class FixtureGroupProperties():
    """FixtureGroupProperties class
    """
    def __eq__(self, prop: FixtureGroupProperties) -> bool:
        """equal operator

        Args:
            prop: FixtureGroupProperties to compare

        Returns:
                  true if they are equal, false otherwise
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
    def LeadingPoint(self) -> None:
        """Leading point of the fixture group

        Value type: Point3D


        :type: None
        """
    @property
    def Name(self) -> None:
        """Name of the fixture group

        Value type: str


        :type: None
        """
    @property
    def Type(self) -> None:
        """Type of the fixture group
        (General|Dynamic|Cutted|Leading)
        Value type: enum


        :type: None
        """

class FixturePlacementElement(PrecastElement, NemAll_Python_BasisElements.AllplanElement):
    """FixturePlacementElement class
    """
    def GetFixturePlacementProperties(self) -> FixturePlacementProperties:
        """Get the MacroPlacement properties

        Returns:
             MacroPlacement properties
        """
    def GetMacro(self) -> object:
        """Get the corresponding macro definition

        Returns:
             Macro definition element
        """
    def SetFixturePlacementProperties(self, MacroPlacementProp: FixturePlacementProperties):
        """Set the MacroPlacement properties

        Args:
            MacroPlacementProp: MacroPlacement properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, macroPlacementProp: FixturePlacementProperties,
                 macro: object):
        """Constructor

        Args:
            commonProp:               Common properties
            macroPlacementProp:       MacroPlacement properties
            macro:                    Macro definition element
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class FixturePlacementProperties():
    """FixturePlacementProperties class
    """
    def __eq__(self, prop: FixturePlacementProperties) -> bool:
        """equal operator

        Args:
            prop: FixturePlacementProperties to compare

        Returns:
                  true if they are equal, false otherwise
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
    def Automation(self) -> None:
        """Value type: bool


        :type: None
        """
    @property
    def ConnectionToAIACatalog(self) -> None:
        """Enable connection to the Precast Fixture catalog of the Fixture placement element

        Value type: bool


        :type: None
        """
    @property
    def ConnectionToAllplanCatalog(self) -> None:
        """Enable connection to the Allplan Catalog of the Fixture placement element

        Value type: bool


        :type: None
        """
    @property
    def CountOfQuestions(self) -> None:
        """Number of active question attributes of the Fixture placement element

        Value type: int


        :type: None
        """
    @property
    def DistortionState(self) -> None:
        """Value type: bool


        :type: None
        """
    @property
    def DomainType(self) -> None:
        """Domaintype of the Fixture placement element

        Value type: None


        :type: None
        """
    @property
    def EnableQuestions(self) -> None:
        """Enables the question attributes of the Fixture placement element

        Value type: bool


        :type: None
        """
    @property
    def HasParentModificationBehaviour(self) -> None:
        """Property for specific behavior for modification state
        Value type: bool


        :type: None
        """
    @property
    def HeightDefinitionType(self) -> HeightDefinitionType:
        """Get the Height definition type
        """
    @HeightDefinitionType.setter
    def HeightDefinitionType(self, value: HeightDefinitionType) -> None:
        """Set the Height definition type

        Args:
            value: value to set
        """
    @property
    def HollowShaft(self) -> None:
        """Value type: bool


        :type: None
        """
    @property
    def Mass_V6(self) -> None:
        """Value type: float


        :type: None
        """
    @property
    def Mass_V7(self) -> None:
        """Value type: float


        :type: None
        """
    @property
    def Mass_V8(self) -> None:
        """Value type: float


        :type: None
        """
    @property
    def Mass_V9(self) -> None:
        """Value type: float


        :type: None
        """
    @property
    def Matrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """Get the Matrix for location in world coordinate system
        """
    @Matrix.setter
    def Matrix(self, value: NemAll_Python_Geometry.Matrix3D) -> None:
        """Set the Matrix for location in world coordinate system

        Args:
            value: value to set
        """
    @property
    def MirrorState(self) -> None:
        """Property for the fixture placement mirrored state
        Value type: bool


        :type: None
        """
    @property
    def Name(self) -> None:
        """Name of the Fixture placement element

        Value type: str


        :type: None
        """
    @property
    def OutlineShape(self) -> None:
        """Value type: OutlineShape


        :type: None
        """
    @property
    def OutlineType(self) -> None:
        """Value type: OutlineType


        :type: None
        """
    @property
    def OutlineTypeInGroup(self) -> None:
        """Value type: OutlineTypeInGroup


        :type: None
        """
    @property
    def PositionNr(self) -> None:
        """Value type: int


        :type: None
        """
    @property
    def ProfilType(self) -> None:
        """Value type: ProfilType


        :type: None
        """
    @property
    def SubType(self) -> None:
        """SubType of the Fixture placement element

        Value type: MacroSubType


        :type: None
        """
    @property
    def Type(self) -> None:
        """Type of the Fixture placement element

        Value type: MacroType


        :type: None
        """
    @property
    def UnitFactor(self) -> None:
        """Value type: int


        :type: None
        """
    @property
    def UseAlways2DRepInGroundView(self) -> None:
        """Value type: bool


        :type: None
        """
    @property
    def UseDrawOrder(self) -> bool:
        """Get the Uses the draw order setting of the placement or the elements of the Fixture ?
        """
    @UseDrawOrder.setter
    def UseDrawOrder(self, value: bool) -> None:
        """Set the Uses the draw order setting of the placement or the elements of the Fixture ?

        Args:
            value: value to set
        """
    @property
    def UseFormat(self) -> bool:
        """Get the Uses the format setting (pen, stroke, color) of the placement or the elements of the Fixture ?
        """
    @UseFormat.setter
    def UseFormat(self, value: bool) -> None:
        """Set the Uses the format setting (pen, stroke, color) of the placement or the elements of the Fixture ?

        Args:
            value: value to set
        """
    @property
    def Visibility(self) -> None:
        """Value type: bool


        :type: None
        """

class FixtureProperties():
    """FixtureProperties class
    """
    def __eq__(self, prop: FixtureProperties) -> bool:
        """equal operator

        Args:
            prop: FixtureProperties to compare

        Returns:
                  true if they are equal, false otherwise
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
    def CatalogName(self) -> None:
        """Value type: str


        :type: None
        """
    @property
    def DomainType(self) -> None:
        """Domaintype of the Fixture element

        Value type: None


        :type: None
        """
    @property
    def InsertionPoint(self) -> None:
        """Value type: Point3D


        :type: None
        """
    @property
    def IsScaleDependent(self) -> None:
        """Value type: bool


        :type: None
        """
    @property
    def Name(self) -> None:
        """Value type: str


        :type: None
        """
    @property
    def PositionNr(self) -> None:
        """Value type: int


        :type: None
        """
    @property
    def SubType(self) -> None:
        """SubType of the Fixture element

        Value type: MacroSubType


        :type: None
        """
    @property
    def Type(self) -> None:
        """Type of the Fixture element

        Value type: MacroType


        :type: None
        """
    @property
    def UnitFactor(self) -> None:
        """Value type: int


        :type: None
        """

class FixtureSlideElement(PrecastElement, NemAll_Python_BasisElements.AllplanElement):
    """FixtureSlideElement class
    """
    def GetFixtureSlideProperties(self) -> FixtureSlideProperties:
        """Get the FixtureSlide properties

        Returns:
             FixtureSlide properties
        """
    def GetObjectList(self) -> list:
        """Get the slide object list

        Returns:
             Slide object list
        """
    def SetFixtureSlideProperties(self, FixtureSlideProp: FixtureSlideProperties):
        """Set the FixtureSlide properties

        Args:
            FixtureSlideProp: FixtureSlide properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, FixtureSlideProp: FixtureSlideProperties, objectList: list):
        """Constructor

        Args:
            FixtureSlideProp: FixtureSlide properties
            objectList:     Object list of slide
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class FixtureSlideProperties():
    """FixtureSlideProperties class
    """
    def __eq__(self, prop: FixtureSlideProperties) -> bool:
        """equal operator

        Args:
            prop: FixtureSlideProperties to compare

        Returns:
                  true if they are equal, false otherwise
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
    def EndScaleRange(self) -> None:
        """Property for end reference scale of slide
        Value type: float


        :type: None
        """
    @property
    def OffsetOfReferencePoint1(self) -> None:
        """Property for first offset value to reference point
        Value type: Vector3D


        :type: None
        """
    @property
    def OffsetOfReferencePoint2(self) -> None:
        """Property for second offset value to reference point
        Value type: Vector3D


        :type: None
        """
    @property
    def ReferencePoint(self) -> None:
        """Property for reference point
        Value type: Point3D


        :type: None
        """
    @property
    def ResizeSettingVx(self) -> None:
        """Property for resize setting for x direction
        Value type: eCombinationType


        :type: None
        """
    @property
    def ResizeSettingVy(self) -> None:
        """Property for resize setting for y direction
        Value type: eCombinationType


        :type: None
        """
    @property
    def ResizeSettingVz(self) -> None:
        """Property for resize setting for z direction
        Value type: eCombinationType


        :type: None
        """
    @property
    def StartScaleRange(self) -> None:
        """Property for start reference scale of slide
        Value type: float


        :type: None
        """
    @property
    def Type(self) -> None:
        """Property for type of slide
        Value type: eSlideType


        :type: None
        """
    @property
    def ViewType(self) -> None:
        """Property for view type of slide
        Value type: eSlideViewType


        :type: None
        """
    @property
    def VisibilityGeo2D(self) -> None:
        """Property for geometry 2D visibility of slide
        Value type: bool


        :type: None
        """
    @property
    def VisibilityGeo3D(self) -> None:
        """Property for geometry 3D visibility of slide
        Value type: bool


        :type: None
        """
    @property
    def VisibilityLayerA(self) -> None:
        """Property for layer A visibility of slide
        Value type: bool


        :type: None
        """
    @property
    def VisibilityLayerB(self) -> None:
        """Property for layer B visibility of slide
        Value type: bool


        :type: None
        """
    @property
    def VisibilityLayerC(self) -> None:
        """Property for layer C visibility of slide
        Value type: bool


        :type: None
        """

class FixtureSlideType(enum.Enum):
    """fixture slide types
    """
    eCode = 1
    eExtension = 5
    eGeometry = 0
    eReinforcement = 2
    eReport = 3
    eUndergroundCadaster = 4

    names = {eGeometry: eGeometry,
             eCode: eCode,
             eReinforcement: eReinforcement,
             eReport: eReport,
             eUndergroundCadaster: eUndergroundCadaster,
             eExtension: eExtension}

    values = {0: eGeometry,
              1: eCode,
              2: eReinforcement,
              3: eReport,
              4: eUndergroundCadaster,
              5: eExtension}

    def __getitem__(self, key: (str | int | float)) -> FixtureSlideType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class FixtureSlideViewType(enum.Enum):
    """Fixture slide view types
    """
    e2D_BACK_VIEW = 6
    e2D_FRONT_VIEW = 5
    e2D_LEFT_VIEW = 3
    e2D_NO_VIEW = 0
    e2D_RIGHT_VIEW = 4
    e2D_SYMBOL = 11
    e2D_TOP_VIEW = 1
    e3D_VIEW = 7
    e3D_VIEW_OLD = 8
    e3D_VIEW_OUTLINE_AREA = 10
    e3D_VIEW_OUTLINE_AREA_ACTUAL = 12
    e3D_VIEW_OUTLINE_VOLUME = 9
    eBOTTOM_VIEW = 2
    eCONNECTION_POINT = 20
    eCONTOUR_CUT = 18
    eLOCK_FIXED = 14
    eLOCK_FIXED_P1 = 16
    eLOCK_UML = 15
    eMEASURE_POINTS = 19
    eORGA_ORIGINAL = 17
    eTGA_ADAPTER = 13

    names = {e2D_NO_VIEW: e2D_NO_VIEW,
             e2D_TOP_VIEW: e2D_TOP_VIEW,
             eBOTTOM_VIEW: eBOTTOM_VIEW,
             e2D_LEFT_VIEW: e2D_LEFT_VIEW,
             e2D_RIGHT_VIEW: e2D_RIGHT_VIEW,
             e2D_FRONT_VIEW: e2D_FRONT_VIEW,
             e2D_BACK_VIEW: e2D_BACK_VIEW,
             e3D_VIEW: e3D_VIEW,
             e3D_VIEW_OLD: e3D_VIEW_OLD,
             e3D_VIEW_OUTLINE_VOLUME: e3D_VIEW_OUTLINE_VOLUME,
             e3D_VIEW_OUTLINE_AREA: e3D_VIEW_OUTLINE_AREA,
             e2D_SYMBOL: e2D_SYMBOL,
             e3D_VIEW_OUTLINE_AREA_ACTUAL: e3D_VIEW_OUTLINE_AREA_ACTUAL,
             eTGA_ADAPTER: eTGA_ADAPTER,
             eLOCK_FIXED: eLOCK_FIXED,
             eLOCK_UML: eLOCK_UML,
             eLOCK_FIXED_P1: eLOCK_FIXED_P1,
             eORGA_ORIGINAL: eORGA_ORIGINAL,
             eCONTOUR_CUT: eCONTOUR_CUT,
             eMEASURE_POINTS: eMEASURE_POINTS,
             eCONNECTION_POINT: eCONNECTION_POINT}

    values = {0: e2D_NO_VIEW,
              1: e2D_TOP_VIEW,
              2: eBOTTOM_VIEW,
              3: e2D_LEFT_VIEW,
              4: e2D_RIGHT_VIEW,
              5: e2D_FRONT_VIEW,
              6: e2D_BACK_VIEW,
              7: e3D_VIEW,
              8: e3D_VIEW_OLD,
              9: e3D_VIEW_OUTLINE_VOLUME,
              10: e3D_VIEW_OUTLINE_AREA,
              11: e2D_SYMBOL,
              12: e3D_VIEW_OUTLINE_AREA_ACTUAL,
              13: eTGA_ADAPTER,
              14: eLOCK_FIXED,
              15: eLOCK_UML,
              16: eLOCK_FIXED_P1,
              17: eORGA_ORIGINAL,
              18: eCONTOUR_CUT,
              19: eMEASURE_POINTS,
              20: eCONNECTION_POINT}

    def __getitem__(self, key: (str | int | float)) -> FixtureSlideViewType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class FormatProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def EliminationAngle(self) -> float:
        """Get the Eliminiation angle
        """
    @EliminationAngle.setter
    def EliminationAngle(self, value: float) -> None:
        """Set the Elimination angle

        Args:
            value: value to set
        """
    @property
    def EliminationOn(self) -> bool:
        """Get the Elimination on flag
        """
    @EliminationOn.setter
    def EliminationOn(self, value: bool) -> None:
        """Set the Elimination on flag

        Args:
            value: value to set
        """
    @property
    def FinishedElementsProps(self) -> FinishProperties:
        """Get the Finished element properties
        """
    @FinishedElementsProps.setter
    def FinishedElementsProps(self, value: FinishProperties) -> None:
        """Set the Finished element properties

        Args:
            value: value to set
        """
    @property
    def FixedAttributesForVisibleEdges(self) -> bool:
        """Get the Fixed atrributes for visible edges flag
        """
    @FixedAttributesForVisibleEdges.setter
    def FixedAttributesForVisibleEdges(self, value: bool) -> None:
        """Set the Fixed atrributes for visible edges flag

        Args:
            value: value to set
        """
    @property
    def HiddenEdgesProps(self) -> LineProperties:
        """Get the Line properties of the hidden edges
        """
    @HiddenEdgesProps.setter
    def HiddenEdgesProps(self, value: LineProperties) -> None:
        """Set the Line properties of the hidden edges

        Args:
            value: value to set
        """
    @property
    def IsBetweenDifferentSurfacesOn(self) -> bool:
        """Get the Is between different surfaces on flag
        """
    @IsBetweenDifferentSurfacesOn.setter
    def IsBetweenDifferentSurfacesOn(self, value: bool) -> None:
        """Set the Is between different surfaces on flag

        Args:
            value: value to set
        """
    @property
    def SetIsSurfaceFromObjectOn(self) -> bool:
        """Get the Set is surface from object on flag
        """
    @SetIsSurfaceFromObjectOn.setter
    def SetIsSurfaceFromObjectOn(self, value: bool) -> None:
        """Set the Set is surface from object on flag

        Args:
            value: value to set
        """
    @property
    def ShowHiddenEdges(self) -> bool:
        """Get the Show hidden edges flag
        """
    @ShowHiddenEdges.setter
    def ShowHiddenEdges(self, value: bool) -> None:
        """Set the Show hidden edges flag

        Args:
            value: value to set
        """
    @property
    def ShowVisibleEdges(self) -> bool:
        """Get the Show visible edges flag
        """
    @ShowVisibleEdges.setter
    def ShowVisibleEdges(self, value: bool) -> None:
        """Set the Show visible edges flag

        Args:
            value: value to set
        """
    @property
    def VisibleEdgesProps(self) -> LineProperties:
        """Get the Line properties of the visible edges
        """
    @VisibleEdgesProps.setter
    def VisibleEdgesProps(self, value: LineProperties) -> None:
        """Set the Line properties of the visible edges

        Args:
            value: value to set
        """

class HeadingProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def AdditionalText(self) -> str:
        """Get the Additional text
        """
    @AdditionalText.setter
    def AdditionalText(self, value: str) -> None:
        """Set the Additional text

        Args:
            value: value to set
        """
    @property
    def IsOn(self) -> bool:
        """Get the Is heading on flag
        """
    @IsOn.setter
    def IsOn(self, value: bool) -> None:
        """Set the Is heading on flag

        Args:
            value: value to set
        """
    @property
    def ProjectionOn(self) -> bool:
        """Get the Projection on flag
        """
    @ProjectionOn.setter
    def ProjectionOn(self, value: bool) -> None:
        """Set the Projection on flag

        Args:
            value: value to set
        """
    @property
    def TextParams(self) -> TextParameters:
        """Get the Text parameters
        """
    @TextParams.setter
    def TextParams(self, value: TextParameters) -> None:
        """Set the Text parameters

        Args:
            value: value to set
        """

class HeightDefinitionType(enum.Enum):
    """Height definition types
    """
    eAverage = 3
    eComponent = 2
    eMacro = 1
    eNone = 0

    names = {eNone: eNone,
             eMacro: eMacro,
             eComponent: eComponent,
             eAverage: eAverage}

    values = {0: eNone,
              1: eMacro,
              2: eComponent,
              3: eAverage}

    def __getitem__(self, key: (str | int | float)) -> HeightDefinitionType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class LabelStyle(Cell):
    """@brief Implementation of the abstract base class LabelStyle
    """
    def SetProps(self, labelStyleProps: LabelStyleProperties):
        """@brief Sets the properties of the labelStyle
        @param labelStyleProps Props

        Args:
            labelStyleProps:props
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, cellId: int, allowOverlapping: bool, labelStyleProps: (LabelStyleProperties | None) = None,
                 conditionTemplate: str = ''):
        """@brief Constructor
        @param cellId
        @param allowOverlapping
        @param labelStyleProps
        @param conditionTemplate

        Args:
            doc:
            cellId:
            allowOverlapping:
            labelStyleProps:
            conditionTemplate:
        """
    @typing.overload
    def __init__(self, element: LabelStyle):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class LabelStyleProperties():
    """@brief Implementation of the abstract base class LabelStyleProperties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, fileEntryPath: FileEntryPath, fileNr: int, entryNr: int):
        """Constructor

        Args:
            fileEntryPath:
            fileNr:
            entryNr:
        """
    @typing.overload
    def __init__(self, fileEntryPath: FileEntryPath, fileNr: int, entryNr: int, location: Location):
        """Constructor

        Args:
            fileEntryPath:
            fileNr:
            entryNr:
            location:
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def EntryNr(self) -> int:
        """Get the Entry number of labelStyle props
        """
    @EntryNr.setter
    def EntryNr(self, value: int) -> None:
        """Set the Entry number of labelStyle props

        Args:
            value: value to set
        """
    @property
    def FileEntryPath(self) -> FileEntryPath:
        """Get the File entry path of labelStyle props
        """
    @FileEntryPath.setter
    def FileEntryPath(self, value: FileEntryPath) -> None:
        """Set the File entry path of labelStyle props

        Args:
            value: value to set
        """
    @property
    def FileNr(self) -> int:
        """Get the File number of labelStyle props
        """
    @FileNr.setter
    def FileNr(self, value: int) -> None:
        """Set the File number of labelStyle props

        Args:
            value: value to set
        """
    @property
    def Location(self) -> Location:
        """Get the Location of labelStyle props
        """
    @Location.setter
    def Location(self, value: Location) -> None:
        """Set the Location of labelStyle props

        Args:
            value: value to set
        """

class LabelingProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def HeadingProps(self) -> HeadingProperties:
        """Get the Heading properties
        """
    @HeadingProps.setter
    def HeadingProps(self, value: HeadingProperties) -> None:
        """Set the Heading properties

        Args:
            value: value to set
        """
    @property
    def LineSpacing(self) -> float:
        """Get the Line spacing
        """
    @LineSpacing.setter
    def LineSpacing(self, value: float) -> None:
        """Set the Line spacing

        Args:
            value: value to set
        """
    @property
    def OffsetFromView(self) -> float:
        """Get the Offset from view
        """
    @OffsetFromView.setter
    def OffsetFromView(self, value: float) -> None:
        """Set the Offset from view

        Args:
            value: value to set
        """
    @property
    def Position(self) -> Position:
        """Get the Position
        """
    @Position.setter
    def Position(self, value: Position) -> None:
        """Set the Position

        Args:
            value: value to set
        """
    @property
    def PrecastProps(self) -> PrecastProperties:
        """Get the Precast properties
        """
    @PrecastProps.setter
    def PrecastProps(self, value: PrecastProperties) -> None:
        """Set the Precast properties

        Args:
            value: value to set
        """
    @property
    def ScaleProps(self) -> ScaleProperties:
        """Get the Scale properties
        """
    @ScaleProps.setter
    def ScaleProps(self, value: ScaleProperties) -> None:
        """Set the Scale properties

        Args:
            value: value to set
        """

class Legend(Cell):
    """Implementation of the abstract base class Legend
    """
    def SetProps(self, legendProps: LegendProperties):
        """@brief Sets the properties of the legend
        @param legendProps Props

        Args:
            legendProps:
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, cellId: int, legendProps: (LegendProperties | None) = None, conditionTemplate: str = ''):
        """@brief Constructor
        @param cellId
        @param legendProps

        Args:
            cellId:
            legendProps:
            conditionTemplate:
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class LegendProperties():
    """Implementation of the abstract base class LegendProperties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, fileEntryPath: FileEntryPath, fileNr: int, entryNr: int, maxHeight: float, maxWidth: float):
        """@brief Constructor
        @param fileEntryPath
        @param fileNr
        @param entryNr
        @param maxHeight
        @param maxWidth

        Args:
            fileEntryPath:
            fileNr:
            entryNr:
            maxHeight:
            maxWidth:
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def EntryNr(self) -> int:
        """Get the Entry number of legend props
        """
    @EntryNr.setter
    def EntryNr(self, value: int) -> None:
        """Set the Entry number of legend props

        Args:
            value: value to set
        """
    @property
    def FileEntryPath(self) -> FileEntryPath:
        """Get the File entry path of legend props
        """
    @FileEntryPath.setter
    def FileEntryPath(self, value: FileEntryPath) -> None:
        """Set the File entry path of legend props

        Args:
            value: value to set
        """
    @property
    def FileNr(self) -> int:
        """Get the File number of legend props
        """
    @FileNr.setter
    def FileNr(self, value: int) -> None:
        """Set the File number of legend props

        Args:
            value: value to set
        """
    @property
    def MaxHeight(self) -> float:
        """Get the Max height of legend props
        """
    @MaxHeight.setter
    def MaxHeight(self, value: float) -> None:
        """Set the Max height of legend props

        Args:
            value: value to set
        """
    @property
    def MaxWidth(self) -> float:
        """Get the Max width of legend props
        """
    @MaxWidth.setter
    def MaxWidth(self, value: float) -> None:
        """Set the Max width of legend props

        Args:
            value: value to set
        """

class LightProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def AmbientLightIntensity(self) -> int:
        """Get the Ambient light intensity
        """
    @AmbientLightIntensity.setter
    def AmbientLightIntensity(self, value: int) -> None:
        """Set the Ambient light intensity

        Args:
            value: value to set
        """
    @property
    def ConsiderLight(self) -> bool:
        """Get the Consider light flag
        """
    @ConsiderLight.setter
    def ConsiderLight(self, value: bool) -> None:
        """Set the Consider light flag

        Args:
            value: value to set
        """
    @property
    def IsShadowsOn(self) -> bool:
        """Get the Is shadow on flag
        """
    @IsShadowsOn.setter
    def IsShadowsOn(self, value: bool) -> None:
        """Set the Is shadow on flag

        Args:
            value: value to set
        """
    @property
    def LightElevationAngle(self) -> int:
        """Get the Light elevation angle
        """
    @LightElevationAngle.setter
    def LightElevationAngle(self, value: int) -> None:
        """Set the Light elevation angle

        Args:
            value: value to set
        """
    @property
    def LightIncidenceAngle(self) -> int:
        """Get the Light incident angle
        """
    @LightIncidenceAngle.setter
    def LightIncidenceAngle(self, value: int) -> None:
        """Set the Light incident angle

        Args:
            value: value to set
        """
    @property
    def LightIntensity(self) -> int:
        """Get the Light intensity
        """
    @LightIntensity.setter
    def LightIntensity(self, value: int) -> None:
        """Set the Light intensity

        Args:
            value: value to set
        """

class LineProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def Color(self) -> int:
        """Get the Color of the line
        """
    @Color.setter
    def Color(self, value: int) -> None:
        """Set the Color of the line

        Args:
            value: value to set
        """
    @property
    def Hatch(self) -> int:
        """Get the Hatch type of the line
        """
    @Hatch.setter
    def Hatch(self, value: int) -> None:
        """Set the Hatch type of the line

        Args:
            value: value to set
        """
    @property
    def Thickness(self) -> int:
        """Get the Thickness of the line
        """
    @Thickness.setter
    def Thickness(self, value: int) -> None:
        """Set the Thickness of the line

        Args:
            value: value to set
        """
    @property
    def Type(self) -> int:
        """Get the Type of the line
        """
    @Type.setter
    def Type(self, value: int) -> None:
        """Set the Type of the line

        Args:
            value: value to set
        """

class Location(enum.Enum):
    """locations
    """
    eLeftBottom = 1
    eLeftTop = 3
    eRightBottom = 0
    eRightTop = 2

    names = {eRightBottom: eRightBottom,
             eLeftBottom: eLeftBottom,
             eRightTop: eRightTop,
             eLeftTop: eLeftTop}

    values = {0: eRightBottom,
              1: eLeftBottom,
              2: eRightTop,
              3: eLeftTop}

    def __getitem__(self, key: (str | int | float)) -> Location:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class MacroGroupType(enum.Enum):
    """types
    """
    eGroupType_CuttedGroup = 2
    eGroupType_DynamicGroup = 1
    eGroupType_GeneralGroup = 0
    eGroupType_LeadingGroup = 3

    names = {eGroupType_GeneralGroup: eGroupType_GeneralGroup,
             eGroupType_DynamicGroup: eGroupType_DynamicGroup,
             eGroupType_CuttedGroup: eGroupType_CuttedGroup,
             eGroupType_LeadingGroup: eGroupType_LeadingGroup}

    values = {0: eGroupType_GeneralGroup,
              1: eGroupType_DynamicGroup,
              2: eGroupType_CuttedGroup,
              3: eGroupType_LeadingGroup}

    def __getitem__(self, key: (str | int | float)) -> MacroGroupType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class MacroSubType(enum.Enum):
    """Sub types
    """
    eAnchorPlate = 13
    eAnchorage = 12
    eBarAccessory = 50
    eBarCoupler = 47
    eBarNut = 48
    eBarThread = 49
    eBracingElement = 44
    eCatchmentArea = 41
    eChannel = 54
    eCirculationLoadPoint = 80
    eCirculationPipeAdapter = 81
    eCirculationStartPoint = 79
    eConcreteArea = 83
    eConcreteBeam = 46
    eConcreteBlock = 45
    eConnectionModeller = 24
    eConnectionWallColumn = 93
    eConnectorEBT = 88
    eConstPrefabConnection = 60
    eCorbel = 10
    eCoverMountingAngle = 53
    eCrossRib = 82
    eElectricalBIE = 67
    eElectricalLamp = 68
    eElectricalRoute = 69
    eFacility = 32
    eFalseJoint = 55
    eFill = 29
    eFrame = 9
    eHeatingLoadPoint = 71
    eHeatingPipeAdapter = 72
    eHeatingStartPoint = 70
    eHollowBody = 25
    eInsertion = 35
    eInsulationArea = 85
    eInsulationElement = 90
    eInsulationStripe = 89
    eJointLength = 22
    eJointReinforcement = 28
    eLinePointPlacement = 58
    eLoadCut = 19
    eMultiLine3D = 42
    eNailer = 92
    eNode = 39
    eOverrule = 86
    ePipe = 30
    ePipePoint = 31
    ePlacingLoop = 26
    ePolyline = 1
    ePrefabConnection = 37
    ePrefabConnectionCorner = 38
    ePrefabModeller = 23
    eProfileEdge = 21
    eReinforcement_Cage = 87
    eRevealAnchor = 8
    eRevealAnchorVirtual = 20
    eRibBody = 59
    eRingBeam = 6
    eRoofLine = 3
    eRoofParapetLine = 4
    eRoofParapetSupport = 5
    eRope = 40
    eSTD_Formwork = 94
    eSanitationLoadPoint = 77
    eSanitationPipeAdapter = 78
    eSanitationStartPoint = 76
    eSecondaryReinf = 27
    eSewageLoadPoint = 65
    eSewageNetElement = 52
    eSewagePipeAdapter = 66
    eSewageStartPoint = 64
    eShaft = 33
    eSlidingRestraint = 7
    eSolidStrip = 56
    eSpecialBuilding = 34
    eSpecialLoad_Undefined = 17
    eSpecialLoad_X = 14
    eSpecialLoad_Y = 15
    eSpecialLoad_Z = 16
    eSphere = 63
    eSteelProfile = 43
    eStripCorbel = 57
    eStructuralRecessFaceSupport = 62
    eStructuralRecessLongitudinalSupport = 61
    eSurface = 51
    eTieBar = 11
    eTileArea = 91
    eTileElement = 84
    eTrimmer = 18
    eUseNoSpecialSubType = 0
    eUseSameSubType = -1
    eVentilationDuctAdapter = 75
    eVentilationLoadPoint = 74
    eVentilationStartPoint = 73
    eZone = 36

    names = {eUseSameSubType: eUseSameSubType,
             eUseNoSpecialSubType: eUseNoSpecialSubType,
             ePolyline: ePolyline,
             eRoofLine: eRoofLine,
             eRoofParapetLine: eRoofParapetLine,
             eRoofParapetSupport: eRoofParapetSupport,
             eRingBeam: eRingBeam,
             eSlidingRestraint: eSlidingRestraint,
             eRevealAnchor: eRevealAnchor,
             eFrame: eFrame,
             eCorbel: eCorbel,
             eTieBar: eTieBar,
             eAnchorage: eAnchorage,
             eAnchorPlate: eAnchorPlate,
             eSpecialLoad_X: eSpecialLoad_X,
             eSpecialLoad_Y: eSpecialLoad_Y,
             eSpecialLoad_Z: eSpecialLoad_Z,
             eSpecialLoad_Undefined: eSpecialLoad_Undefined,
             eTrimmer: eTrimmer,
             eLoadCut: eLoadCut,
             eRevealAnchorVirtual: eRevealAnchorVirtual,
             eProfileEdge: eProfileEdge,
             eJointLength: eJointLength,
             ePrefabModeller: ePrefabModeller,
             eConnectionModeller: eConnectionModeller,
             eHollowBody: eHollowBody,
             ePlacingLoop: ePlacingLoop,
             eSecondaryReinf: eSecondaryReinf,
             eJointReinforcement: eJointReinforcement,
             eFill: eFill,
             ePipe: ePipe,
             ePipePoint: ePipePoint,
             eFacility: eFacility,
             eShaft: eShaft,
             eSpecialBuilding: eSpecialBuilding,
             eInsertion: eInsertion,
             eZone: eZone,
             ePrefabConnection: ePrefabConnection,
             ePrefabConnectionCorner: ePrefabConnectionCorner,
             eNode: eNode,
             eRope: eRope,
             eCatchmentArea: eCatchmentArea,
             eMultiLine3D: eMultiLine3D,
             eSteelProfile: eSteelProfile,
             eBracingElement: eBracingElement,
             eConcreteBlock: eConcreteBlock,
             eConcreteBeam: eConcreteBeam,
             eBarCoupler: eBarCoupler,
             eBarNut: eBarNut,
             eBarThread: eBarThread,
             eBarAccessory: eBarAccessory,
             eSurface: eSurface,
             eSewageNetElement: eSewageNetElement,
             eCoverMountingAngle: eCoverMountingAngle,
             eChannel: eChannel,
             eFalseJoint: eFalseJoint,
             eSolidStrip: eSolidStrip,
             eStripCorbel: eStripCorbel,
             eLinePointPlacement: eLinePointPlacement,
             eRibBody: eRibBody,
             eConstPrefabConnection: eConstPrefabConnection,
             eStructuralRecessLongitudinalSupport: eStructuralRecessLongitudinalSupport,
             eStructuralRecessFaceSupport: eStructuralRecessFaceSupport,
             eSphere: eSphere,
             eSewageStartPoint: eSewageStartPoint,
             eSewageLoadPoint: eSewageLoadPoint,
             eSewagePipeAdapter: eSewagePipeAdapter,
             eElectricalBIE: eElectricalBIE,
             eElectricalLamp: eElectricalLamp,
             eElectricalRoute: eElectricalRoute,
             eHeatingStartPoint: eHeatingStartPoint,
             eHeatingLoadPoint: eHeatingLoadPoint,
             eHeatingPipeAdapter: eHeatingPipeAdapter,
             eVentilationStartPoint: eVentilationStartPoint,
             eVentilationLoadPoint: eVentilationLoadPoint,
             eVentilationDuctAdapter: eVentilationDuctAdapter,
             eSanitationStartPoint: eSanitationStartPoint,
             eSanitationLoadPoint: eSanitationLoadPoint,
             eSanitationPipeAdapter: eSanitationPipeAdapter,
             eCirculationStartPoint: eCirculationStartPoint,
             eCirculationLoadPoint: eCirculationLoadPoint,
             eCirculationPipeAdapter: eCirculationPipeAdapter,
             eCrossRib: eCrossRib,
             eConcreteArea: eConcreteArea,
             eTileElement: eTileElement,
             eInsulationArea: eInsulationArea,
             eOverrule: eOverrule,
             eReinforcement_Cage: eReinforcement_Cage,
             eConnectorEBT: eConnectorEBT,
             eInsulationStripe: eInsulationStripe,
             eInsulationElement: eInsulationElement,
             eTileArea: eTileArea,
             eNailer: eNailer,
             eConnectionWallColumn: eConnectionWallColumn,
             eSTD_Formwork: eSTD_Formwork}

    values = {-1: eUseSameSubType,
              0: eUseNoSpecialSubType,
              1: ePolyline,
              3: eRoofLine,
              4: eRoofParapetLine,
              5: eRoofParapetSupport,
              6: eRingBeam,
              7: eSlidingRestraint,
              8: eRevealAnchor,
              9: eFrame,
              10: eCorbel,
              11: eTieBar,
              12: eAnchorage,
              13: eAnchorPlate,
              14: eSpecialLoad_X,
              15: eSpecialLoad_Y,
              16: eSpecialLoad_Z,
              17: eSpecialLoad_Undefined,
              18: eTrimmer,
              19: eLoadCut,
              20: eRevealAnchorVirtual,
              21: eProfileEdge,
              22: eJointLength,
              23: ePrefabModeller,
              24: eConnectionModeller,
              25: eHollowBody,
              26: ePlacingLoop,
              27: eSecondaryReinf,
              28: eJointReinforcement,
              29: eFill,
              30: ePipe,
              31: ePipePoint,
              32: eFacility,
              33: eShaft,
              34: eSpecialBuilding,
              35: eInsertion,
              36: eZone,
              37: ePrefabConnection,
              38: ePrefabConnectionCorner,
              39: eNode,
              40: eRope,
              41: eCatchmentArea,
              42: eMultiLine3D,
              43: eSteelProfile,
              44: eBracingElement,
              45: eConcreteBlock,
              46: eConcreteBeam,
              47: eBarCoupler,
              48: eBarNut,
              49: eBarThread,
              50: eBarAccessory,
              51: eSurface,
              52: eSewageNetElement,
              53: eCoverMountingAngle,
              54: eChannel,
              55: eFalseJoint,
              56: eSolidStrip,
              57: eStripCorbel,
              58: eLinePointPlacement,
              59: eRibBody,
              60: eConstPrefabConnection,
              61: eStructuralRecessLongitudinalSupport,
              62: eStructuralRecessFaceSupport,
              63: eSphere,
              64: eSewageStartPoint,
              65: eSewageLoadPoint,
              66: eSewagePipeAdapter,
              67: eElectricalBIE,
              68: eElectricalLamp,
              69: eElectricalRoute,
              70: eHeatingStartPoint,
              71: eHeatingLoadPoint,
              72: eHeatingPipeAdapter,
              73: eVentilationStartPoint,
              74: eVentilationLoadPoint,
              75: eVentilationDuctAdapter,
              76: eSanitationStartPoint,
              77: eSanitationLoadPoint,
              78: eSanitationPipeAdapter,
              79: eCirculationStartPoint,
              80: eCirculationLoadPoint,
              81: eCirculationPipeAdapter,
              82: eCrossRib,
              83: eConcreteArea,
              84: eTileElement,
              85: eInsulationArea,
              86: eOverrule,
              87: eReinforcement_Cage,
              88: eConnectorEBT,
              89: eInsulationStripe,
              90: eInsulationElement,
              91: eTileArea,
              92: eNailer,
              93: eConnectionWallColumn,
              94: eSTD_Formwork}

    def __getitem__(self, key: (str | int | float)) -> MacroSubType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class MacroType(enum.Enum):
    """types
    """
    eGroup_Fixture = 3
    eLine_Fixture = 1
    ePlane_Fixture = 2
    ePoint_Fixture = 0
    eUseSameType = -1

    names = {eUseSameType: eUseSameType,
             ePoint_Fixture: ePoint_Fixture,
             eLine_Fixture: eLine_Fixture,
             ePlane_Fixture: ePlane_Fixture,
             eGroup_Fixture: eGroup_Fixture}

    values = {-1: eUseSameType,
              0: ePoint_Fixture,
              1: eLine_Fixture,
              2: ePlane_Fixture,
              3: eGroup_Fixture}

    def __getitem__(self, key: (str | int | float)) -> MacroType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class OutlineShape(enum.Enum):
    """ outline shapes
    """
    eBUILTIN_OUTLINE_SHAPE_NOTHING = 0
    eBUILTIN_OUTLINE_SHAPE_RECTANGLE = 1
    eBUILTIN_OUTLINE_SHAPE_SYMBOL = 3
    eBUILTIN_OUTLINE_SHAPE_TRAPEZOID = 2

    names = {eBUILTIN_OUTLINE_SHAPE_NOTHING: eBUILTIN_OUTLINE_SHAPE_NOTHING,
             eBUILTIN_OUTLINE_SHAPE_RECTANGLE: eBUILTIN_OUTLINE_SHAPE_RECTANGLE,
             eBUILTIN_OUTLINE_SHAPE_TRAPEZOID: eBUILTIN_OUTLINE_SHAPE_TRAPEZOID,
             eBUILTIN_OUTLINE_SHAPE_SYMBOL: eBUILTIN_OUTLINE_SHAPE_SYMBOL}

    values = {0: eBUILTIN_OUTLINE_SHAPE_NOTHING,
              1: eBUILTIN_OUTLINE_SHAPE_RECTANGLE,
              2: eBUILTIN_OUTLINE_SHAPE_TRAPEZOID,
              3: eBUILTIN_OUTLINE_SHAPE_SYMBOL}

    def __getitem__(self, key: (str | int | float)) -> OutlineShape:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class OutlineType(enum.Enum):
    """ outline types
    """
    eBUILTIN_OUTLINE_TYPE_MINUS = 2
    eBUILTIN_OUTLINE_TYPE_NOTHING = 0
    eBUILTIN_OUTLINE_TYPE_NO_AFFECT = 3
    eBUILTIN_OUTLINE_TYPE_PLUS = 1

    names = {eBUILTIN_OUTLINE_TYPE_NOTHING: eBUILTIN_OUTLINE_TYPE_NOTHING,
             eBUILTIN_OUTLINE_TYPE_PLUS: eBUILTIN_OUTLINE_TYPE_PLUS,
             eBUILTIN_OUTLINE_TYPE_MINUS: eBUILTIN_OUTLINE_TYPE_MINUS,
             eBUILTIN_OUTLINE_TYPE_NO_AFFECT: eBUILTIN_OUTLINE_TYPE_NO_AFFECT}

    values = {0: eBUILTIN_OUTLINE_TYPE_NOTHING,
              1: eBUILTIN_OUTLINE_TYPE_PLUS,
              2: eBUILTIN_OUTLINE_TYPE_MINUS,
              3: eBUILTIN_OUTLINE_TYPE_NO_AFFECT}

    def __getitem__(self, key: (str | int | float)) -> OutlineType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class OutlineTypeInGroup(enum.Enum):
    """ outline types in group
    """
    eBUILTIN_OUTLINE_TYPE_IN_GROUP_MINUS = 2
    eBUILTIN_OUTLINE_TYPE_IN_GROUP_NOTHING = 0
    eBUILTIN_OUTLINE_TYPE_IN_GROUP_PLUS = 1

    names = {eBUILTIN_OUTLINE_TYPE_IN_GROUP_NOTHING: eBUILTIN_OUTLINE_TYPE_IN_GROUP_NOTHING,
             eBUILTIN_OUTLINE_TYPE_IN_GROUP_PLUS: eBUILTIN_OUTLINE_TYPE_IN_GROUP_PLUS,
             eBUILTIN_OUTLINE_TYPE_IN_GROUP_MINUS: eBUILTIN_OUTLINE_TYPE_IN_GROUP_MINUS}

    values = {0: eBUILTIN_OUTLINE_TYPE_IN_GROUP_NOTHING,
              1: eBUILTIN_OUTLINE_TYPE_IN_GROUP_PLUS,
              2: eBUILTIN_OUTLINE_TYPE_IN_GROUP_MINUS}

    def __getitem__(self, key: (str | int | float)) -> OutlineTypeInGroup:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class Page():

    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, anchors: list):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Anchors:BaseReferenceModelElements
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, anchors: list, conditionTemplate: str):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Anchors:BaseReferenceModelElements
            ConditionTemplate:
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, anchors: list,
                 size: NemAll_Python_Geometry.MinMax2D, centeringCells: bool):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Anchors:BaseReferenceModelElements
            Size:
            CenteringCells:
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, anchors: list,
                 size: NemAll_Python_Geometry.MinMax2D, centeringCells: bool, conditionTemplate: str):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Anchors:BaseReferenceModelElements
            Size:
            CenteringCells:
            ConditionTemplate:
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, scale: float, anchors: list,
                 size: NemAll_Python_Geometry.MinMax2D, centeringCells: bool):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Scale:
            Anchors:BaseReferenceModelElements
            Size:
            CenteringCells:
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, scale: float, anchors: list,
                 size: NemAll_Python_Geometry.MinMax2D, centeringCells: bool, conditionTemplate: str):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Scale:
            Anchors:BaseReferenceModelElements
            Size:
            CenteringCells:
            ConditionTemplate:
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, scales: list, anchors: list,
                 size: NemAll_Python_Geometry.MinMax2D, centeringCells: bool):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Scales:
            Anchors:BaseReferenceModelElements
            Size:
            CenteringCells:
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, pageNr: int, scales: list, anchors: list,
                 size: NemAll_Python_Geometry.MinMax2D, centeringCells: bool, conditionTemplate: str):
        """Constructor

        Args:
            DocumentAdapter:
            PageNr:
            Scales:
            Anchors:BaseReferenceModelElements
            Size:
            CenteringCells:
            ConditionTemplate:
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def add_anchor(self, anchor: Anchor):
        """Adds an anchor to the page

        Args:
            Anchor:to add
        """
    def add_anchors(self, anchors: list):
        """Adds anchors to the page

        Args:
            Anchors:to add
        """
    def add_cell(self, cell: Cell):
        """Adds a cell (labelStyle/legend/view) to the page

        Args:
            Cell:to add
        """
    @property
    def DrawingFile(self) -> int:
        """Get the Drawing file on which the page should be placed
        """
    @DrawingFile.setter
    def DrawingFile(self, value: int) -> None:
        """Set the Drawing file on which the page should be placed

        Args:
            value: value to set
        """

class PageProperties():
    """@brief Wrapper for page properties of elementplan
    """
    @typing.overload
    def __init__(self, label: str, sizeType: int, scaleType: int, fixedScale: float):
        """@brief Creates a helper to fill python palette for UVS Elementplan
        @param label Label of the page
        @param sizeType Size type of the page (Fixed | AutomaticSelection)
        @param scaleType Scale type of the page (ScaleAutomaticSelection | ScaleFixed | MaximumSize)
        @param fixedScale Fixed scale

        Args:
            label:
            sizeType:
            scaleType:
            fixedScale:
        """
    @typing.overload
    def __init__(self, element: PageProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def FixedScale(self) -> float:
        """Get the Fixed scaleof the page
        """
    @FixedScale.setter
    def FixedScale(self, value: float) -> None:
        """Set the Fixed scaleof the page

        Args:
            value: value to set
        """
    @property
    def Label(self) -> str:
        """Get the Label of the page
        """
    @Label.setter
    def Label(self, value: str) -> None:
        """Set the Label of the page

        Args:
            value: value to set
        """
    @property
    def ScaleType(self) -> int:
        """Get the Scale type of the page
        """
    @ScaleType.setter
    def ScaleType(self, value: int) -> None:
        """Set the Scale type of the page

        Args:
            value: value to set
        """
    @property
    def SizeType(self) -> int:
        """Get the Size type of the page
        """
    @SizeType.setter
    def SizeType(self, value: int) -> None:
        """Set the Size type of the page

        Args:
            value: value to set
        """

class PagePropertiesList():
    """List for PageProperties objects
    """
    def __contains__(self, value: PageProperties) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: PageProperties):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: PagePropertiesList) -> bool:
        """Compare two lists

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> PageProperties:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, eleList: list) -> PagePropertiesList:
        """Add a list

        Args:
            eleList: PageProperties list

        Returns:
            Lists with the added elements
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ele: PageProperties):
        """Constructor with a PageProperties

        Args:
            ele: PageProperties
        """
    @typing.overload
    def __init__(self, eleList: list):
        """Constructor with a list of PageProperties

        Args:
            eleList: PageProperties list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __setitem__(self, index: int | slice, value: PageProperties):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: PageProperties):
        """Append a list item

        Args:
            value: Value to append
        """
    @typing.overload
    def extend(self, iterable: PagePropertiesList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    @typing.overload
    def extend(self, eleList: list):
        """Extend the list

        Args:
            eleList: PageProperties list
        """
    def extend(self):
        """ Overloaded function. See individual overloads.
        """

class Plan():

    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Constructor

        Args:
            DocumentAdapter:
        """
    @typing.overload
    def __init__(self, DocumentAdapter: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                 doc: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList):
        """Constructor

        Args:
            DocumentAdapter:
            BaseElementAdapterList:
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def add_page(self, page: Page):
        """Adds a page to the plan

        Args:
            page:to add
        """
    @typing.overload
    def create(self, elemPlan: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> bool:
        """Creates the elementplan

        Args:
            Allplan::IFW::ElementAdapter::BaseElementAdapter:-> created elementplan
        """
    @typing.overload
    def create(self, elemPlan: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
               baseElements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> bool:
        """Creates the elementplan

        Args:
            Allplan::IFW::ElementAdapter::BaseElementAdapter:-> created elementplan
            Allplan::IFW::ElementAdapter::BaseElementAdapterList:-> elements to create
        """
    def create(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    @property
    def DrawingFile(self) -> int:
        """Get the Drawing file on which the elementplan should be placed
        """
    @DrawingFile.setter
    def DrawingFile(self, value: int) -> None:
        """Set the Drawing file on which the elementplan should be placed

        Args:
            value: value to set
        """
    @property
    def Position(self) -> NemAll_Python_Geometry.Point2D:
        """Get the Position where the elementplan should be placed
        """
    @Position.setter
    def Position(self, value: NemAll_Python_Geometry.Point2D) -> None:
        """Set the Position where the elementplan should be placed

        Args:
            value: value to set
        """

class Position(enum.Enum):
    """position for labeling
    """
    eAccordingTheUSStandard = 7
    eBottomCenter = 5
    eBottomLeft = 4
    eBottomRight = 6
    eNone = 0
    eTopCenter = 2
    eTopLeft = 1
    eTopRight = 3

    names = {eNone: eNone,
             eTopLeft: eTopLeft,
             eTopCenter: eTopCenter,
             eTopRight: eTopRight,
             eBottomLeft: eBottomLeft,
             eBottomCenter: eBottomCenter,
             eBottomRight: eBottomRight,
             eAccordingTheUSStandard: eAccordingTheUSStandard}

    values = {0: eNone,
              1: eTopLeft,
              2: eTopCenter,
              3: eTopRight,
              4: eBottomLeft,
              5: eBottomCenter,
              6: eBottomRight,
              7: eAccordingTheUSStandard}

    def __getitem__(self, key: (str | int | float)) -> Position:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PrecastCatalogService():
    """Implementation of the precast catalog service
    """
    @staticmethod
    def GetAllFixtureCatalogValues() -> list:
        """Get the values of all fixtures from the fixture catalog

        Returns:
            List of all fixture values
        """
    @staticmethod
    def GetAreaFixtureCatalogValues() -> list:
        """Get the values of the area fixtures from the fixture catalog

        Returns:
            List of area fixture descriptions
        """
    @staticmethod
    def GetBrickTileCatalogValues() -> list:
        """Get the values from the tile or brick catalog

        Returns:
            List of tile or brick values
        """
    @staticmethod
    def GetConcreteGradeCatalogValues() -> list:
        """Get the values from the concrete grade catalog

        Returns:
            List of concrete grade descriptions
        """
    @staticmethod
    def GetFactoryCatalogValues() -> list:
        """Get the values from the factory catalog

        Returns:
            List of factory values
        """
    @staticmethod
    def GetFixtureEntryNames(pathIndex: int, fileIndex: int) -> list:
        """Gets the list of fixture entry names for a given path and file index.

        Args:
            pathIndex: The index of the fixture path
            fileIndex: The index of the fixture file

        Returns:
            List of fixture entry names
        """
    @staticmethod
    def GetFixtureGroupNames(pathIndex: int) -> list:
        """Get the list of group names (file names) for a specified fixture path index.

        Args:
            pathIndex: The index of the fixture path

        Returns:
            List of fixture group names
        """
    @staticmethod
    def GetFixturePathShortName(pathString: str) -> str:
        """Gets the short name for a fixture path based on the provided path.

        Args:
            pathString: The fixture path string

        Returns:
            Short name for the fixture path
        """
    @staticmethod
    def GetFixturePathShortNames() -> list:
        """Get the list of path short names where fixtures are stored (Office, Project...)

        Returns:
            List of path short names for fixtures
        """
    @staticmethod
    def GetInsulationCatalogValues() -> list:
        """Get the descriptions from the insulation material catalog

        Returns:
            List of insulation material descriptions
        """
    @staticmethod
    def GetLineFixtureCatalogValues() -> list:
        """Get the values of the line fixtures from the fixture catalog

        Returns:
            List of line fixture values
        """
    @staticmethod
    def GetMultiMaterialLayoutCatalogValues() -> list:
        """Gets the values from the multi material layout catalog

        Returns:
            List of multi material layout values
        """
    @staticmethod
    def GetMultiMaterialLayoutSelectionResult(selectedValue: str) -> int:
        """Get the selection result of a multi material layout, that is used to update the palette

        Args:
            selectedValue: The selected value from the catalog.

        Returns:
            The index in the catalog associated with the selected value
        """
    @staticmethod
    def GetNormCatalogValues(currentNorm: str) -> list:
        """Gets the values from the norm catalog

        Args:
            currentNorm: Current norm that should be set

        Returns:
            List of norm values
        """
    @staticmethod
    def GetPointFixtureCatalogValues() -> list:
        """Get the values of the point fixtures from the fixture catalog

        Returns:
            List of point fixture values
        """
    @staticmethod
    def GetPrecastElementTypeCatalogValues() -> list:
        """Gets the values from the precast element type catalog

        Returns:
            List of precast element types
        """
    @staticmethod
    def GetPrecastElementTypeSelectionResult(selectedValueIndex: int) -> str:
        """Get the selection result of a precast element type, that is used to update the palette

        Args:
            selectedValueIndex: The index of the selected value in the list of precast element types

        Returns:
            A string representing the selection result.
        """
    @staticmethod
    def GetSurfaceCatalogValues() -> list:
        """Get the values from the surface catalog

        Returns:
            List of surface values
        """

class AssemblyGroupElement(PrecastElement, NemAll_Python_BasisElements.AllplanElement):
    """AssemblyGroupElement class
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, name: str, number: int, LibraryElementsList: list, FixtureElementsList: list, ReinforcementList: list):
        """Constructor

        Args:
            name:      Name of the assembly group
            number:    Number of the assembly group
            LibraryElementsList:    List of library fixtures which should be included in the assembly group
            FixtureElementsList:    List of parametric fixtures which should be included in the assembly group
            ReinforcementList:      List of reinforcement placements which should be included in the assembly group
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def FixtureElementsList(self) -> None:
        """List of parametric fixtures which should be included in the assembly group
        Value type: list


        :type: None
        """
    @property
    def LibraryElementsList(self) -> None:
        """List of library fixtures which should be included in the assembly group
        Value type: list


        :type: None
        """
    @property
    def Name(self) -> None:
        """Name of the assembly group
        Value type: str


        :type: None
        """
    @property
    def Number(self) -> None:
        """Number of the assembly group
        Value type: int


        :type: None
        """
    @property
    def ReinforcementList(self) -> None:
        """List of reinforcement placements which should be included in the assembly group
        Value type: list


        :type: None
        """

class PrecastElementProperties():
    """PrecastElementProperties class
    """
    def GetPrecastElementTypeFromIdx(self, arg2: int) -> str:
        """Get the name of the PrecastElementType from Cat Idx

        Returns:
             PrecastElementType Cat Name
        """
    def SetElementTypeCatalogGUID_from_Name(self, arg2: str) -> NemAll_Python_IFW_ElementAdapter.GUID:
        """Set the elementTypeCatGUID

        Returns:
             elementTypeCatGUID
        """
    def SetFactoryCatalogAddressOffset(self, arg2: str) -> int:
        """Set the factoryCatAddressOffset

        Returns:
             factoryCatAddressOffset
        """
    def SetNormCatalogAddressOffset(self, arg2: str) -> int:
        """Set the normCatAddressOffset

        Returns:
             normCatAddressOffset
        """
    def __eq__(self, prop: PrecastElementProperties) -> bool:
        """equal operator

        Args:
            prop: PrecastElementProperties to compare

        Returns:
                  true if they are equal, false otherwise
        """
    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def CreateLabeling(self) -> None:
        """Property for CreateLabeling
        Value type: bool


        :type: None
        """
    @property
    def DimensionCross(self) -> None:
        """Property for DimensionCross
        Value type: float


        :type: None
        """
    @property
    def DimensionSpan(self) -> None:
        """Property for DimensionSpan
        Value type: float


        :type: None
        """
    @property
    def DimensionViewing(self) -> None:
        """Property for DimensionViewing
        Value type: float


        :type: None
        """
    @property
    def ElemTypeAttribut(self) -> None:
        """Property for ElemTypeAttribut
        Value type: str


        :type: None
        """
    @property
    def ElementType(self) -> None:
        """Property for ElementType
        Value type: int


        :type: None
        """
    @property
    def ElementTypeCatGUID(self) -> None:
        """Property for ElementTypeCatGUID
        Value type: GUID


        :type: None
        """
    @property
    def Factory(self) -> None:
        """Property for Factory
        Value type: str


        :type: None
        """
    @property
    def FactoryCatAddressOffset(self) -> None:
        """Property for FactoryCatAddressOffset
        Value type: int


        :type: None
        """
    @property
    def LabelingTextRefPoint(self) -> None:
        """Property for LabelingTextRefPoint
        Value type: int


        :type: None
        """
    @property
    def Layers(self) -> None:
        """Property for Layers
        Value type: list


        :type: None
        """
    @property
    def ManualDimensions(self) -> None:
        """Property for ManualDimensions
        Value type: bool


        :type: None
        """
    @property
    def Norm(self) -> None:
        """Property for Norm
        Value type: str


        :type: None
        """
    @property
    def NormCatAddressOffset(self) -> None:
        """Property for NormCatAddressOffset
        Value type: int


        :type: None
        """
    @property
    def PieceFactor(self) -> None:
        """Property for PieceFactor
        Value type: int


        :type: None
        """
    @property
    def PosNr(self) -> None:
        """Property for PosNr
        Value type: int


        :type: None
        """
    @property
    def PosNrText(self) -> None:
        """Property for PosNrText
        Value type: str


        :type: None
        """
    @property
    def ReferencePoint(self) -> None:
        """Property for ReferencePoint
        Value type: Point3D


        :type: None
        """
    @property
    def SpanDirection(self) -> None:
        """Property for SpanDirection
        Value type: Point3D


        :type: None
        """
    @property
    def ViewDirection(self) -> None:
        """Property for ViewDirection
        Value type: Point3D


        :type: None
        """

class PrecastLayer(NemAll_Python_BasisElements.AllplanElement):
    """PrecastLayer class
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, Properties: PrecastLayerProperties):
        """Constructor

        Args:
            layerProp: Layer properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Properties(self) -> None:
        """Property for Properties
        Value type: PrecastLayerProperties


        :type: None
        """

class PrecastLayerProperties():
    """PrecastLayerProperties class
    """
    @typing.overload
    def SetMaterialCatalogAddressOffset(self, arg2: str, arg3: str) -> int:
        """Set the materialCatAddressOffset

        Returns:
             materialCatAddressOffset
        """
    @typing.overload
    def SetMaterialCatalogAddressOffset(self, arg2: int, arg3: str) -> int:
        """Set the materialCatAddressOffset

        Returns:
             materialCatAddressOffset
        """
    def SetMaterialCatalogAddressOffset(self) -> int:
        """ Overloaded function. See individual overloads.
        """
    def __eq__(self, prop: PrecastLayerProperties) -> bool:
        """equal operator

        Args:
            prop: PrecastLayerProperties to compare

        Returns:
                  true if they are equal, false otherwise
        """
    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def CalculateLayerThickness(self) -> None:
        """Property for CalculateLayerThickness
        Value type: bool


        :type: None
        """
    @property
    def LayerName(self) -> None:
        """Property for LayerName
        Value type: str


        :type: None
        """
    @property
    def LayerNumber(self) -> None:
        """Property for LayerNumber
        Value type: int


        :type: None
        """
    @property
    def LayerThickness(self) -> None:
        """Property for LayerThickness
        Value type: float


        :type: None
        """
    @property
    def Material(self) -> None:
        """Property for Material
        Value type: str


        :type: None
        """
    @property
    def MaterialCatAddressOffset(self) -> None:
        """Property for MaterialCatAddressOffset
        Value type: int


        :type: None
        """
    @property
    def MaterialType(self) -> None:
        """Property for MaterialType
        Value type: int


        :type: None
        """

class PrecastMWSElement(PrecastElement, NemAll_Python_BasisElements.AllplanElement):
    """PrecastMWSElement class
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, factory: str, name: str, number: int, piecefactor: int, longitBarHeight: int, SegmentNumber: int,
                 SegmentVector: NemAll_Python_Geometry.Point3D, SegementPointList: list, ReinforcementList: list):
        """Constructor

        Args:
            factory: factory
            name:    name of the MWS element
            number:    number of the MWS element
            piecefactor:    piecefactor of the MWS element
            longitBarHeight:    longitBarHeight of the MWS element
            SegmentNumber:    SegmentNumber of the MWS element
            SegmentVector:    SegmentVector of the MWS element
            SegementPointList:    SegementPointList of the MWS element
            ReinforcementList:    ReinforcementList of the MWS element
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """
    @property
    def Factory(self) -> None:
        """Property for Factory
        Value type: str


        :type: None
        """
    @property
    def IndexLongitBar(self) -> None:
        """Index of the longitudinal bar in the Reinfrocementlist
        Value type: int


        :type: None
        """
    @property
    def LongitBarHeight(self) -> None:
        """Heightposition of the longitudinal bar (1 = Position 1, 2 = Position 2)
        Value type: int


        :type: None
        """
    @property
    def Name(self) -> None:
        """Property for Name
        Value type: str


        :type: None
        """
    @property
    def Number(self) -> None:
        """Property for Number
        Value type: int


        :type: None
        """
    @property
    def Piecefactor(self) -> None:
        """Property for Piecefactor
        Value type: int


        :type: None
        """
    @property
    def ReinforcementList(self) -> None:
        """list of reinforcement placements
        Value type: list


        :type: None
        """
    @property
    def SegmentNumber(self) -> None:
        """Number of the main segement of the transversal shape
        Value type: int


        :type: None
        """
    @property
    def SegmentPointList(self) -> None:
        """Pointlist of the transversal shape
        Value type: list


        :type: None
        """
    @property
    def SegmentVector(self) -> None:
        """Property for Norm Catalog
        Value type: int


        :type: None
        """

class PrecastProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def Location(self) -> int:
        """Get the Location
        """
    @Location.setter
    def Location(self, value: int) -> None:
        """Set the Location

        Args:
            value: value to set
        """
    @property
    def OverwriteConfiguration(self) -> bool:
        """Get the Overwrite configuration flag
        """
    @OverwriteConfiguration.setter
    def OverwriteConfiguration(self, value: bool) -> None:
        """Set the Overwrite configuration flag

        Args:
            value: value to set
        """
    @property
    def PositionNumberIsOn(self) -> bool:
        """Get the Position number is on flag
        """
    @PositionNumberIsOn.setter
    def PositionNumberIsOn(self, value: bool) -> None:
        """Set the Position number is on flag

        Args:
            value: value to set
        """

class ProfilType(enum.Enum):
    """profil types
    """
    eBUILTIN_PROFIL_TYPE_EDGE = 1
    eBUILTIN_PROFIL_TYPE_JOINT = 0

    names = {eBUILTIN_PROFIL_TYPE_JOINT: eBUILTIN_PROFIL_TYPE_JOINT,
             eBUILTIN_PROFIL_TYPE_EDGE: eBUILTIN_PROFIL_TYPE_EDGE}

    values = {0: eBUILTIN_PROFIL_TYPE_JOINT,
              1: eBUILTIN_PROFIL_TYPE_EDGE}

    def __getitem__(self, key: (str | int | float)) -> ProfilType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class RepresentationProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def BasicReinforcementPrecastElementsActive(self) -> bool:
        """Get the Basic reinforcements active for precast elements flag
        """
    @BasicReinforcementPrecastElementsActive.setter
    def BasicReinforcementPrecastElementsActive(self, value: bool) -> None:
        """Set the Basic reinforcements active for precast elements flag

        Args:
            value: value to set
        """
    @property
    def FixturesAsWireModel(self) -> bool:
        """Get the Fixtures as wire models flag
        """
    @FixturesAsWireModel.setter
    def FixturesAsWireModel(self, value: bool) -> None:
        """Set the Fixtures as wire models flag

        Args:
            value: value to set
        """
    @property
    def ReferenceScaleFor2D3DFoils(self) -> float:
        """Get the Reference scale for 2D,3D foils
        """
    @ReferenceScaleFor2D3DFoils.setter
    def ReferenceScaleFor2D3DFoils(self, value: float) -> None:
        """Set the Reference scale for 2D,3D foils

        Args:
            value: value to set
        """
    @property
    def ReinforcementAsWireModel(self) -> bool:
        """Get the reinforcement as wire models flag
        """
    @ReinforcementAsWireModel.setter
    def ReinforcementAsWireModel(self, value: bool) -> None:
        """Set the reinforcement as wire models flag

        Args:
            value: value to set
        """

class Rotation(enum.Enum):
    """rotations for views
    """
    eRotation0 = 0
    eRotation180 = 2
    eRotation270 = 3
    eRotation90 = 1

    names = {eRotation0: eRotation0,
             eRotation90: eRotation90,
             eRotation180: eRotation180,
             eRotation270: eRotation270}

    values = {0: eRotation0,
              1: eRotation90,
              2: eRotation180,
              3: eRotation270}

    def __getitem__(self, key: (str | int | float)) -> Rotation:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ScaleProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def AdditionalText(self) -> str:
        """Get the Additional text
        """
    @AdditionalText.setter
    def AdditionalText(self, value: str) -> None:
        """Set the Additional text

        Args:
            value: value to set
        """
    @property
    def IsOn(self) -> bool:
        """Get the Is on flag
        """
    @IsOn.setter
    def IsOn(self, value: bool) -> None:
        """Set the Is on flag

        Args:
            value: value to set
        """
    @property
    def TextParams(self) -> TextParameters:
        """Get the Text parameters
        """
    @TextParams.setter
    def TextParams(self, value: TextParameters) -> None:
        """Set the Text parameters

        Args:
            value: value to set
        """

class SectionProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def LimitSectionBodyByElement(self) -> bool:
        """Get the Limit section body by element of the section
        """
    @LimitSectionBodyByElement.setter
    def LimitSectionBodyByElement(self, value: bool) -> None:
        """Set the Limit section body by element of the section

        Args:
            value: value to set
        """
    @property
    def Name(self) -> str:
        """Get the Name of the section
        """
    @Name.setter
    def Name(self, value: str) -> None:
        """Set the Name of the section

        Args:
            value: value to set
        """
    @property
    def Prefix(self) -> str:
        """Get the Prefix of the section
        """
    @Prefix.setter
    def Prefix(self, value: str) -> None:
        """Set the Prefix of the section

        Args:
            value: value to set
        """
    @property
    def ShowLabel(self) -> bool:
        """Get the Show label of the section
        """
    @ShowLabel.setter
    def ShowLabel(self, value: bool) -> None:
        """Set the Show label of the section

        Args:
            value: value to set
        """
    @property
    def XDirectionProps(self) -> DirectionProperties:
        """Get the X-Direction properties of the section
        """
    @XDirectionProps.setter
    def XDirectionProps(self, value: DirectionProperties) -> None:
        """Set the X-Direction properties of the section

        Args:
            value: value to set
        """
    @property
    def YDirectionProps(self) -> DirectionProperties:
        """Get the Y-Direction properties of the section
        """
    @YDirectionProps.setter
    def YDirectionProps(self, value: DirectionProperties) -> None:
        """Set the Y-Direction properties of the section

        Args:
            value: value to set
        """
    @property
    def ZDirectionProps(self) -> DirectionProperties:
        """Get the Z-Direction properties of the section
        """
    @ZDirectionProps.setter
    def ZDirectionProps(self, value: DirectionProperties) -> None:
        """Set the Z-Direction properties of the section

        Args:
            value: value to set
        """

class SubType(enum.Enum):
    """Sub types
    """
    eAnchorPlate = 13
    eAnchorage = 12
    eBarAccessory = 50
    eBarCoupler = 47
    eBarNut = 48
    eBarThread = 49
    eBracingElement = 44
    eCatchmentArea = 41
    eChannel = 54
    eCirculationLoadPoint = 80
    eCirculationPipeAdapter = 81
    eCirculationStartPoint = 79
    eConcreteArea = 83
    eConcreteBeam = 46
    eConcreteBlock = 45
    eConnectionModeller = 24
    eConnectionWallColumn = 93
    eConnectorEBT = 88
    eConstPrefabConnection = 60
    eCorbel = 10
    eCoverMountingAngle = 53
    eCrossRib = 82
    eElectricalBIE = 67
    eElectricalLamp = 68
    eElectricalRoute = 69
    eFacility = 32
    eFalseJoint = 55
    eFill = 29
    eFrame = 9
    eHeatingLoadPoint = 71
    eHeatingPipeAdapter = 72
    eHeatingStartPoint = 70
    eHollowBody = 25
    eInsertion = 35
    eInsulationArea = 85
    eInsulationElement = 90
    eInsulationStripe = 89
    eJointLength = 22
    eJointReinforcement = 28
    eLinePointPlacement = 58
    eLoadCut = 19
    eMultiLine3D = 42
    eNailer = 92
    eNode = 39
    eOverrule = 86
    ePipe = 30
    ePipePoint = 31
    ePlacingLoop = 26
    ePolyline = 1
    ePrefabConnection = 37
    ePrefabConnectionCorner = 38
    ePrefabModeller = 23
    eProfileEdge = 21
    eReinforcement_Cage = 87
    eRevealAnchor = 8
    eRevealAnchorVirtual = 20
    eRibBody = 59
    eRingBeam = 6
    eRoofLine = 3
    eRoofParapetLine = 4
    eRoofParapetSupport = 5
    eRope = 40
    eSTD_Formwork = 94
    eSanitationLoadPoint = 77
    eSanitationPipeAdapter = 78
    eSanitationStartPoint = 76
    eSecondaryReinf = 27
    eSewageLoadPoint = 65
    eSewageNetElement = 52
    eSewagePipeAdapter = 66
    eSewageStartPoint = 64
    eShaft = 33
    eSlidingRestraint = 7
    eSolidStrip = 56
    eSpecialBuilding = 34
    eSpecialLoad_Undefined = 17
    eSpecialLoad_X = 14
    eSpecialLoad_Y = 15
    eSpecialLoad_Z = 16
    eSphere = 63
    eSteelProfile = 43
    eStripCorbel = 57
    eStructuralRecessFaceSupport = 62
    eStructuralRecessLongitudinalSupport = 61
    eSurface = 51
    eTieBar = 11
    eTileArea = 91
    eTileElement = 84
    eTrimmer = 18
    eUseNoSpecialSubType = 0
    eUseSameSubType = -1
    eVentilationDuctAdapter = 75
    eVentilationLoadPoint = 74
    eVentilationStartPoint = 73
    eZone = 36

    names = {eUseSameSubType: eUseSameSubType,
             eUseNoSpecialSubType: eUseNoSpecialSubType,
             ePolyline: ePolyline,
             eRoofLine: eRoofLine,
             eRoofParapetLine: eRoofParapetLine,
             eRoofParapetSupport: eRoofParapetSupport,
             eRingBeam: eRingBeam,
             eSlidingRestraint: eSlidingRestraint,
             eRevealAnchor: eRevealAnchor,
             eFrame: eFrame,
             eCorbel: eCorbel,
             eTieBar: eTieBar,
             eAnchorage: eAnchorage,
             eAnchorPlate: eAnchorPlate,
             eSpecialLoad_X: eSpecialLoad_X,
             eSpecialLoad_Y: eSpecialLoad_Y,
             eSpecialLoad_Z: eSpecialLoad_Z,
             eSpecialLoad_Undefined: eSpecialLoad_Undefined,
             eTrimmer: eTrimmer,
             eLoadCut: eLoadCut,
             eRevealAnchorVirtual: eRevealAnchorVirtual,
             eProfileEdge: eProfileEdge,
             eJointLength: eJointLength,
             ePrefabModeller: ePrefabModeller,
             eConnectionModeller: eConnectionModeller,
             eHollowBody: eHollowBody,
             ePlacingLoop: ePlacingLoop,
             eSecondaryReinf: eSecondaryReinf,
             eJointReinforcement: eJointReinforcement,
             eFill: eFill,
             ePipe: ePipe,
             ePipePoint: ePipePoint,
             eFacility: eFacility,
             eShaft: eShaft,
             eSpecialBuilding: eSpecialBuilding,
             eInsertion: eInsertion,
             eZone: eZone,
             ePrefabConnection: ePrefabConnection,
             ePrefabConnectionCorner: ePrefabConnectionCorner,
             eNode: eNode,
             eRope: eRope,
             eCatchmentArea: eCatchmentArea,
             eMultiLine3D: eMultiLine3D,
             eSteelProfile: eSteelProfile,
             eBracingElement: eBracingElement,
             eConcreteBlock: eConcreteBlock,
             eConcreteBeam: eConcreteBeam,
             eBarCoupler: eBarCoupler,
             eBarNut: eBarNut,
             eBarThread: eBarThread,
             eBarAccessory: eBarAccessory,
             eSurface: eSurface,
             eSewageNetElement: eSewageNetElement,
             eCoverMountingAngle: eCoverMountingAngle,
             eChannel: eChannel,
             eFalseJoint: eFalseJoint,
             eSolidStrip: eSolidStrip,
             eStripCorbel: eStripCorbel,
             eLinePointPlacement: eLinePointPlacement,
             eRibBody: eRibBody,
             eConstPrefabConnection: eConstPrefabConnection,
             eStructuralRecessLongitudinalSupport: eStructuralRecessLongitudinalSupport,
             eStructuralRecessFaceSupport: eStructuralRecessFaceSupport,
             eSphere: eSphere,
             eSewageStartPoint: eSewageStartPoint,
             eSewageLoadPoint: eSewageLoadPoint,
             eSewagePipeAdapter: eSewagePipeAdapter,
             eElectricalBIE: eElectricalBIE,
             eElectricalLamp: eElectricalLamp,
             eElectricalRoute: eElectricalRoute,
             eHeatingStartPoint: eHeatingStartPoint,
             eHeatingLoadPoint: eHeatingLoadPoint,
             eHeatingPipeAdapter: eHeatingPipeAdapter,
             eVentilationStartPoint: eVentilationStartPoint,
             eVentilationLoadPoint: eVentilationLoadPoint,
             eVentilationDuctAdapter: eVentilationDuctAdapter,
             eSanitationStartPoint: eSanitationStartPoint,
             eSanitationLoadPoint: eSanitationLoadPoint,
             eSanitationPipeAdapter: eSanitationPipeAdapter,
             eCirculationStartPoint: eCirculationStartPoint,
             eCirculationLoadPoint: eCirculationLoadPoint,
             eCirculationPipeAdapter: eCirculationPipeAdapter,
             eCrossRib: eCrossRib,
             eConcreteArea: eConcreteArea,
             eTileElement: eTileElement,
             eInsulationArea: eInsulationArea,
             eOverrule: eOverrule,
             eReinforcement_Cage: eReinforcement_Cage,
             eConnectorEBT: eConnectorEBT,
             eInsulationStripe: eInsulationStripe,
             eInsulationElement: eInsulationElement,
             eTileArea: eTileArea,
             eNailer: eNailer,
             eConnectionWallColumn: eConnectionWallColumn,
             eSTD_Formwork: eSTD_Formwork}

    values = {-1: eUseSameSubType,
              0: eUseNoSpecialSubType,
              1: ePolyline,
              3: eRoofLine,
              4: eRoofParapetLine,
              5: eRoofParapetSupport,
              6: eRingBeam,
              7: eSlidingRestraint,
              8: eRevealAnchor,
              9: eFrame,
              10: eCorbel,
              11: eTieBar,
              12: eAnchorage,
              13: eAnchorPlate,
              14: eSpecialLoad_X,
              15: eSpecialLoad_Y,
              16: eSpecialLoad_Z,
              17: eSpecialLoad_Undefined,
              18: eTrimmer,
              19: eLoadCut,
              20: eRevealAnchorVirtual,
              21: eProfileEdge,
              22: eJointLength,
              23: ePrefabModeller,
              24: eConnectionModeller,
              25: eHollowBody,
              26: ePlacingLoop,
              27: eSecondaryReinf,
              28: eJointReinforcement,
              29: eFill,
              30: ePipe,
              31: ePipePoint,
              32: eFacility,
              33: eShaft,
              34: eSpecialBuilding,
              35: eInsertion,
              36: eZone,
              37: ePrefabConnection,
              38: ePrefabConnectionCorner,
              39: eNode,
              40: eRope,
              41: eCatchmentArea,
              42: eMultiLine3D,
              43: eSteelProfile,
              44: eBracingElement,
              45: eConcreteBlock,
              46: eConcreteBeam,
              47: eBarCoupler,
              48: eBarNut,
              49: eBarThread,
              50: eBarAccessory,
              51: eSurface,
              52: eSewageNetElement,
              53: eCoverMountingAngle,
              54: eChannel,
              55: eFalseJoint,
              56: eSolidStrip,
              57: eStripCorbel,
              58: eLinePointPlacement,
              59: eRibBody,
              60: eConstPrefabConnection,
              61: eStructuralRecessLongitudinalSupport,
              62: eStructuralRecessFaceSupport,
              63: eSphere,
              64: eSewageStartPoint,
              65: eSewageLoadPoint,
              66: eSewagePipeAdapter,
              67: eElectricalBIE,
              68: eElectricalLamp,
              69: eElectricalRoute,
              70: eHeatingStartPoint,
              71: eHeatingLoadPoint,
              72: eHeatingPipeAdapter,
              73: eVentilationStartPoint,
              74: eVentilationLoadPoint,
              75: eVentilationDuctAdapter,
              76: eSanitationStartPoint,
              77: eSanitationLoadPoint,
              78: eSanitationPipeAdapter,
              79: eCirculationStartPoint,
              80: eCirculationLoadPoint,
              81: eCirculationPipeAdapter,
              82: eCrossRib,
              83: eConcreteArea,
              84: eTileElement,
              85: eInsulationArea,
              86: eOverrule,
              87: eReinforcement_Cage,
              88: eConnectorEBT,
              89: eInsulationStripe,
              90: eInsulationElement,
              91: eTileArea,
              92: eNailer,
              93: eConnectionWallColumn,
              94: eSTD_Formwork}

    def __getitem__(self, key: (str | int | float)) -> SubType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SurfaceProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def SurfaceElements(self) -> int:
        """Get the Surface elements
        """
    @SurfaceElements.setter
    def SurfaceElements(self, value: int) -> None:
        """Set the Surface elements

        Args:
            value: value to set
        """
    @property
    def Transparency(self) -> bool:
        """Get the Transparency flag
        """
    @Transparency.setter
    def Transparency(self, value: bool) -> None:
        """Set the Transparency flag

        Args:
            value: value to set
        """

class TextAlignment(enum.Enum):
    """Alignments for text of labeling for view
    """
    eBottomCenter = 6
    eCenter = 5
    eLeftBottom = 1
    eLeftCenter = 9
    eLeftTop = 4
    eRightBottom = 2
    eRightCenter = 7
    eRightTop = 3
    eTopCenter = 8
    eUnknownAlignment = 0

    names = {eUnknownAlignment: eUnknownAlignment,
             eLeftTop: eLeftTop,
             eTopCenter: eTopCenter,
             eRightTop: eRightTop,
             eLeftCenter: eLeftCenter,
             eCenter: eCenter,
             eRightCenter: eRightCenter,
             eLeftBottom: eLeftBottom,
             eBottomCenter: eBottomCenter,
             eRightBottom: eRightBottom}

    values = {0: eUnknownAlignment,
              4: eLeftTop,
              8: eTopCenter,
              3: eRightTop,
              9: eLeftCenter,
              5: eCenter,
              7: eRightCenter,
              1: eLeftBottom,
              6: eBottomCenter,
              2: eRightBottom}

    def __getitem__(self, key: (str | int | float)) -> TextAlignment:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextParameters():

    def __init__(self):
        """Initialize
        """
    @property
    def BackgroundColorType(self) -> int:
        """Get the Type of the background color
        """
    @BackgroundColorType.setter
    def BackgroundColorType(self, value: int) -> None:
        """Set the Type of the background color

        Args:
            value: value to set
        """
    @property
    def BorderColor(self) -> int:
        """Get the Border color
        """
    @BorderColor.setter
    def BorderColor(self, value: int) -> None:
        """Set the Border color

        Args:
            value: value to set
        """
    @property
    def BorderLineType(self) -> int:
        """Get the Type of the border line
        """
    @BorderLineType.setter
    def BorderLineType(self, value: int) -> None:
        """Set the Type of the border line

        Args:
            value: value to set
        """
    @property
    def BorderOffset(self) -> int:
        """Get the Offset of the border
        """
    @BorderOffset.setter
    def BorderOffset(self, value: int) -> None:
        """Set the Offset of the border

        Args:
            value: value to set
        """
    @property
    def BorderThickness(self) -> int:
        """Get the Border thickness
        """
    @BorderThickness.setter
    def BorderThickness(self, value: int) -> None:
        """Set the Border thickness

        Args:
            value: value to set
        """
    @property
    def ColumnAngle(self) -> float:
        """Get the Column angle
        """
    @ColumnAngle.setter
    def ColumnAngle(self, value: float) -> None:
        """Set the Column angle

        Args:
            value: value to set
        """
    @property
    def CustomBackgroundColor(self) -> int:
        """Get the Color of the custom background
        """
    @CustomBackgroundColor.setter
    def CustomBackgroundColor(self, value: int) -> None:
        """Set the Color of the custom background

        Args:
            value: value to set
        """
    @property
    def FontAngle(self) -> float:
        """Get the Font angle
        """
    @FontAngle.setter
    def FontAngle(self, value: float) -> None:
        """Set the Font angle

        Args:
            value: value to set
        """
    @property
    def FontColor(self) -> int:
        """Get the Font color
        """
    @FontColor.setter
    def FontColor(self, value: int) -> None:
        """Set the Font color

        Args:
            value: value to set
        """
    @property
    def FontEmphasis(self) -> int:
        """Get the Font emphasis
        """
    @FontEmphasis.setter
    def FontEmphasis(self, value: int) -> None:
        """Set the Font emphasis

        Args:
            value: value to set
        """
    @property
    def FontHeight(self) -> float:
        """Get the Font height
        """
    @FontHeight.setter
    def FontHeight(self, value: float) -> None:
        """Set the Font height

        Args:
            value: value to set
        """
    @property
    def FontID(self) -> int:
        """Get the Font ID
        """
    @FontID.setter
    def FontID(self, value: int) -> None:
        """Set the Font ID

        Args:
            value: value to set
        """
    @property
    def FontLayer(self) -> int:
        """Get the Font layer
        """
    @FontLayer.setter
    def FontLayer(self, value: int) -> None:
        """Set the Font layer

        Args:
            value: value to set
        """
    @property
    def FontWidth(self) -> float:
        """Get the Font widht
        """
    @FontWidth.setter
    def FontWidth(self, value: float) -> None:
        """Set the Font widht

        Args:
            value: value to set
        """
    @property
    def IsFontColorFromLayer(self) -> bool:
        """Get the Is font color from layer flag
        """
    @IsFontColorFromLayer.setter
    def IsFontColorFromLayer(self, value: bool) -> None:
        """Set the Is font color from layer flag

        Args:
            value: value to set
        """
    @property
    def IsFontLineTypeFromLayer(self) -> bool:
        """Get the Is font line type from layer flag
        """
    @IsFontLineTypeFromLayer.setter
    def IsFontLineTypeFromLayer(self, value: bool) -> None:
        """Set the Is font line type from layer flag

        Args:
            value: value to set
        """
    @property
    def IsFontPenFromLayer(self) -> bool:
        """Get the Is font pen from layer flag
        """
    @IsFontPenFromLayer.setter
    def IsFontPenFromLayer(self, value: bool) -> None:
        """Set the Is font pen from layer flag

        Args:
            value: value to set
        """
    @property
    def PositionNumberBorderLine(self) -> int:
        """Get the Border line position number
        """
    @PositionNumberBorderLine.setter
    def PositionNumberBorderLine(self, value: int) -> None:
        """Set the Border line position number

        Args:
            value: value to set
        """
    @property
    def RowDistance(self) -> float:
        """Get the Row distance
        """
    @RowDistance.setter
    def RowDistance(self, value: float) -> None:
        """Set the Row distance

        Args:
            value: value to set
        """
    @property
    def TextPlacementPointType(self) -> TextAlignment:
        """Get the Type of the text placement point
        """
    @TextPlacementPointType.setter
    def TextPlacementPointType(self, value: TextAlignment) -> None:
        """Set the Type of the text placement point

        Args:
            value: value to set
        """
    @property
    def UseBorderAroundTheText(self) -> bool:
        """Get the Use border around text flag
        """
    @UseBorderAroundTheText.setter
    def UseBorderAroundTheText(self, value: bool) -> None:
        """Set the Use border around text flag

        Args:
            value: value to set
        """
    @property
    def UseConstantSizeInLayout(self) -> bool:
        """Get the Use constant size in layout flag
        """
    @UseConstantSizeInLayout.setter
    def UseConstantSizeInLayout(self, value: bool) -> None:
        """Set the Use constant size in layout flag

        Args:
            value: value to set
        """
    @property
    def UseCustomTextParameters(self) -> bool:
        """Get the Use custom text parameters flag
        """
    @UseCustomTextParameters.setter
    def UseCustomTextParameters(self, value: bool) -> None:
        """Set the Use custom text parameters flag

        Args:
            value: value to set
        """

class TextProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def Color(self) -> int:
        """Get the Color of the text
        """
    @Color.setter
    def Color(self, value: int) -> None:
        """Set the Color of the text

        Args:
            value: value to set
        """
    @property
    def FontAngle(self) -> float:
        """Get the Font angle of the text
        """
    @FontAngle.setter
    def FontAngle(self, value: float) -> None:
        """Set the Font angle of the text

        Args:
            value: value to set
        """
    @property
    def FontId(self) -> int:
        """Get the Font ID of the text
        """
    @FontId.setter
    def FontId(self, value: int) -> None:
        """Set the Font ID of the text

        Args:
            value: value to set
        """
    @property
    def Height(self) -> float:
        """Get the Height of the text
        """
    @Height.setter
    def Height(self, value: float) -> None:
        """Set the Height of the text

        Args:
            value: value to set
        """
    @property
    def Width(self) -> float:
        """Get the Width of the text
        """
    @Width.setter
    def Width(self, value: float) -> None:
        """Set the Width of the text

        Args:
            value: value to set
        """

class Type(enum.Enum):
    """types
    """
    eGroup_Fixture = 3
    eLine_Fixture = 1
    ePlane_Fixture = 2
    ePoint_Fixture = 0
    eUseSameType = -1

    names = {eUseSameType: eUseSameType,
             ePoint_Fixture: ePoint_Fixture,
             eLine_Fixture: eLine_Fixture,
             ePlane_Fixture: ePlane_Fixture,
             eGroup_Fixture: eGroup_Fixture}

    values = {-1: eUseSameType,
              0: ePoint_Fixture,
              1: eLine_Fixture,
              2: ePlane_Fixture,
              3: eGroup_Fixture}

    def __getitem__(self, key: (str | int | float)) -> Type:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class View(Cell):

    def SetProps(self, viewProps: ViewProperties):
        """@brief Set the configuration which includes parameters to create the view
        @param viewProps ViewProperties

        Args:
            viewProps:props
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, cellId: int, direction: Direction, rotation: Rotation):
        """Constructor

        Args:
            DocumentAdapter:
            CellId:
            Direction:
            Rotation:
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, cellId: int, direction: Direction, rotation: Rotation,
                 viewProps: ViewProperties):
        """Constructor

        Args:
            DocumentAdapter:
            CellId:
            Direction:
            Rotation:
            View:properties
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, cellId: int, direction: Direction, rotation: Rotation,
                 viewProps: ViewProperties, conditionTemplate: str):
        """@brief Constructor
        @param doc DocumentAdapter
        @param cellId Id of the view
        @param direction Direction of the view
        @param rotation Rotation of the view
        @param viewProps ViewProperties
        @param conditionTemplate iTrigger

        Args:
            DocumentAdapter:
            CellId:
            Direction:
            Rotation:
            View:properties
            Condition:template
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def create(self, elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, position: NemAll_Python_Geometry.Point2D,
               view: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> bool:
        """Creates a standalon local uvs view without plan

        Args:
            Allplan::IFW::ElementAdapter::BaseElementAdapterList:-> elements of the view
            Allplan::Geometry::Point2D:-> position of the view
            Allplan::IFW::ElementAdapter::BaseElementAdapter:-> created view
        """

class ViewProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def ClippingPathProps(self) -> ClippingPathProperties:
        """Get the Clipping path properties
        """
    @ClippingPathProps.setter
    def ClippingPathProps(self, value: ClippingPathProperties) -> None:
        """Set the Clipping path properties

        Args:
            value: value to set
        """
    @property
    def DimensioningProps(self) -> DimensioningProperties:
        """Get the dimensioning properties
        """
    @DimensioningProps.setter
    def DimensioningProps(self, value: DimensioningProperties) -> None:
        """Set the dimensioning properties

        Args:
            value: value to set
        """
    @property
    def FormatProps(self) -> FormatProperties:
        """Get the Format properties
        """
    @FormatProps.setter
    def FormatProps(self, value: FormatProperties) -> None:
        """Set the Format properties

        Args:
            value: value to set
        """
    @property
    def LabelingProps(self) -> LabelingProperties:
        """Get the Labeling properties
        """
    @LabelingProps.setter
    def LabelingProps(self, value: LabelingProperties) -> None:
        """Set the Labeling properties

        Args:
            value: value to set
        """
    @property
    def LightProps(self) -> LightProperties:
        """Get the Light properties
        """
    @LightProps.setter
    def LightProps(self, value: LightProperties) -> None:
        """Set the Light properties

        Args:
            value: value to set
        """
    @property
    def RepresentationProps(self) -> RepresentationProperties:
        """Get the Representation properties
        """
    @RepresentationProps.setter
    def RepresentationProps(self, value: RepresentationProperties) -> None:
        """Set the Representation properties

        Args:
            value: value to set
        """
    @property
    def SectionProps(self) -> SectionProperties:
        """Get the Section properties
        """
    @SectionProps.setter
    def SectionProps(self, value: SectionProperties) -> None:
        """Set the Section properties

        Args:
            value: value to set
        """
    @property
    def SurfaceProps(self) -> SurfaceProperties:
        """Get the Surface properties
        """
    @SurfaceProps.setter
    def SurfaceProps(self, value: SurfaceProperties) -> None:
        """Set theSurface  properties

        Args:
            value: value to set
        """
    @property
    def UpdateAutomatically(self) -> bool:
        """Get the Update automatically flag
        """
    @UpdateAutomatically.setter
    def UpdateAutomatically(self, value: bool) -> None:
        """Set the Update automatically flag

        Args:
            value: value to set
        """
    @property
    def VisibilityProps(self) -> VisibilityProperties:
        """Get the Visibility properties
        """
    @VisibilityProps.setter
    def VisibilityProps(self, value: VisibilityProperties) -> None:
        """Set the Visibility properties

        Args:
            value: value to set
        """
    @property
    def ZoomFactorX(self) -> float:
        """Get the Zoom factor X
        """
    @ZoomFactorX.setter
    def ZoomFactorX(self, value: float) -> None:
        """Set the Zoom factor X

        Args:
            value: value to set
        """
    @property
    def ZoomFactorY(self) -> float:
        """Get the Zoom factor Y
        """
    @ZoomFactorY.setter
    def ZoomFactorY(self, value: float) -> None:
        """Set the Zoom factor Y

        Args:
            value: value to set
        """

class VisibilityProperties():

    def __init__(self):
        """Initialize
        """
    @property
    def AllowedLayers(self) -> AllowedElements:
        """Get the Allowed elements
        """
    @AllowedLayers.setter
    def AllowedLayers(self, value: AllowedElements) -> None:
        """Set the Allowed elements

        Args:
            value: value to set
        """
    @property
    def Printset(self) -> str:
        """Get the Print set
        """
    @Printset.setter
    def Printset(self, value: str) -> None:
        """Set the Print set

        Args:
            value: value to set
        """
    @property
    def SelectedLayers(self) -> list:
        """Get the Selected layers
        """
    @SelectedLayers.setter
    def SelectedLayers(self, value: list) -> None:
        """Set the Selected layers

        Args:
            value: value to set
        """

def CreateElementplan(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, catOffset: int, pageProps: list,
                      elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, position: NemAll_Python_Geometry.Point2D = Point2D(0, 0), distances: NemAll_Python_Geometry.Point2D = Point2D(0, 0), destinationDrawingFile: int = 0):
    """@brief Creates the elementplan
    @param doc DocumentAdapter for ptrArrrayData
    @param catOffset Offset of layout in catalog
    @param elements Elements for plan
    @param position Position of the plan
    @param distances Distances between the pages and plans (x -> pages, y -> plans)
    @param destinationDrawingfile Drawing file, where the plan is placed

    Args:
        doc:
        catOffset:
        pageProps:
        elements:
        position:
        distances:
        destinationDrawingFile:
    """
def CreatePrecastElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, insertionMat: NemAll_Python_Geometry.Matrix3D,
                          elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, modelEleList: list, modelUuidList: list, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, delete_python: bool):
    """Create the precast elements

    Args:
        doc:            Document
        insertionMat:   Insertion matrix
        elements:       List of created elements
        modelEleList:   List of model elements which have to be created
        modelUuidList:  List with the model UUIDS in modification mode
        viewProj:       View projection
        delete_python:  bool weather the python should be deleted after update
    """
def GetLayoutNameFromOffset(catOffset: int) -> str:
    """@brief Gets the name of the layout via catalogOffset
    @param catOffset Offset of layout in catalog
    @return Name of layout

    Args:
        catOffset:
    """
def GetPagePropertiesFromCatalog(catOffset: int) -> list:
    """@brief Gets the pages from selected layout
    @param catOffset Offset of layout in catalog
    @return List of pages

    Args:
        catOffset:
    """
def GetPrecastMandant() -> str:
    """Read the actual precast client from project settings

    Returns:
         Name of the client set in project settings
    """
def LockPrecastUpdate():
    """Lock the precast update
    """
def ProcessListGen(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                   elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, listElementMap: list, templateElementMap: list):
    """Create the precast elements

    Args:
        doc:            Document
        elements:       List of elements which should be handled by ListeGenerator
    """
def TriggerPrecastUpdate(elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> bool:
    """Trigger the precast update

    Args:
        elements:   Elements to update

    Returns:
        update successful: true/false)
    """
def UnlockPrecastUpdate():
    """Lock the precast update
    """

```