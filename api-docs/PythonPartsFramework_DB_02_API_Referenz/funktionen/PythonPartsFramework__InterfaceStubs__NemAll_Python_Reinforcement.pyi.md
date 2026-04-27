---
title: "NemAll_Python_Reinforcement"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_Reinforcement.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_Reinforcement

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_Reinforcement.pyi`  
> **Typ:** `stub`  
> **Tags:** `bewehrung`

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

"""Exposed classes and functions from NemAll_Python_Reinforcement"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_BaseElements
import NemAll_Python_BasisElements
import NemAll_Python_Geometry
import NemAll_Python_IFW_ElementAdapter
import NemAll_Python_IFW_Input
import NemAll_Python_Utility


__all__ = [
    "AnchorageLengthService",
    "AnchorageType",
    "Bar",
    "BarAreaPlacementProperties",
    "BarAreaPlacementService",
    "BarLabel",
    "BarLabelList",
    "BarLabelPointerProperties",
    "BarLabelProperties",
    "BarPlacement",
    "BarPlacementSection",
    "BarPositionData",
    "BarSchema",
    "BarSpacer",
    "BarWithArc",
    "BarsOperations",
    "BarsRepresentation",
    "BendingRollerService",
    "BendingShape",
    "BendingShapeList",
    "BendingShapeType",
    "CircleStirrup",
    "CircularAreaElement",
    "Column",
    "ColumnStirrup",
    "CreateReinforcementLabeling",
    "CrossBars",
    "Diamond",
    "DivideBarsParameters",
    "EngCatCrossSection",
    "EngCatDiameter",
    "EngCatMesh",
    "EngCatMeshGroup",
    "EngCatSteel",
    "ExtrudeBarPlacement",
    "Freeform",
    "FullCircle",
    "GeometryExpansionUtil",
    "HookLengthService",
    "HookType",
    "InitApplicationtest",
    "InitUnitTest",
    "LShapedBar",
    "LabelType",
    "LabelWithComb",
    "LabelWithComb2Pointer",
    "LabelWithComb3Pointer",
    "LabelWithDimensionLine",
    "LabelWithFan",
    "LabelWithFanStartCenterEnd",
    "LabelWithFanStartEnd",
    "LabelWithPointer",
    "LongitudinalBar",
    "LongitudinalBarDoubleBentOff",
    "LongitudinalBarFourTimesBentOff",
    "LongitudinalBarProperties",
    "LongitudinalBarPropertiesList",
    "LongitudinalBarSingleBentOff",
    "LongitudinalBars",
    "Mesh",
    "MeshAreaPlacementProperties",
    "MeshAreaPlacementService",
    "MeshBendingDirection",
    "MeshData",
    "MeshLabel",
    "MeshLabelList",
    "MeshLabelPointerProperties",
    "MeshLabelProperties",
    "MeshOperations",
    "MeshPlacement",
    "NormType",
    "Normal",
    "OpenStirrup",
    "PlaneMeshPlacement",
    "ReinfElement",
    "ReinforcementLabel",
    "ReinforcementLabelList",
    "ReinforcementLabelPointerProperties",
    "ReinforcementLabelProperties",
    "ReinforcementLabelTextProperties",
    "ReinforcementService",
    "ReinforcementSettings",
    "ReinforcementShapeBuilder",
    "ReinforcementType",
    "ReinforcementUtil",
    "SHook",
    "SchemaMirror",
    "SchemaStirrupUnfold",
    "SpiralElement",
    "Stirrup",
    "StirrupType",
    "SweepBarPlacement",
    "Torsion",
    "TorsionStirrup",
    "UninitUnitTest",
    "eAnchorage",
    "eAnchorageHook",
    "eAnchorageHookOneCrossBar",
    "eAnchorageStraight",
    "eAnchorageStraightOneCrossBar",
    "eAnchorageStraightTwoCrossBars",
    "eAngle",
    "eNORM_AS",
    "eNORM_BS",
    "eNORM_DIN",
    "eNORM_DIN_1",
    "eNORM_DIN_H",
    "eNORM_EC2",
    "eNORM_EHE",
    "eNORM_NEN",
    "eNORM_NF",
    "eNORM_OE",
    "eNORM_SIA",
    "eNORM_SNIP",
    "eNORM_SNIP2003",
    "eNormNo",
    "eStirrup"
]


class AnchorageLengthService():
    """Service class for the anchorage length calculation
    """
    def Calculate(self, concreteGrade: int, steelGrade: int, diameter: float, asMesh: float, bDoubleBar: bool, meshBarDistCross: float,
                  bMesh: bool, barDistance: float, roundLength: float):
        """Calculation of the anchorage length

        Args:
            concreteGrade:    Concrete grade index (starting from 1)
            steelGrade:       Steel grade
            diameter:         Diameter
            asMesh:           asMesh of the mesh
            bDoubleBar:       Double bar
            meshBarDistCross: Distance of the mesh bars cross to the anchorage direction
            bMesh:            Anchorage for a mesh
            barDistance:      Bar distance
            roundLength:      Rounding length
        """
    def CalculateBar(self, concreteGrade: int, steelGrade: int, diameter: float, bDoubleBar: bool, barDistance: float, roundLength: float):
        """Calculation of the anchorage length for a bar

        Args:
            concreteGrade: Concrete grade index (starting from 1)
            steelGrade:    Steel grade
            diameter:      Diameter
            bDoubleBar:    Double bar
            barDistance:   Bar distance
            roundLength:   Rounding length
        """
    def GetAnchorageLength(self) -> float:
        """Get the anchorage length

        Returns:
             Anchorage length
        """
    def GetAnchorageType(self) -> AnchorageType:
        """Get the anchorage type

        Returns:
             Anchorage type
        """
    def GetAsFactor(self) -> float:
        """Get the as factor required / available

        Returns:
             As mesh factor
        """
    def GetCompositionZone(self) -> int:
        """Get the composition zone

        Returns:
             Composition zone
        """
    def GetHookAngle(self) -> float:
        """Get the hook angle

        Returns:
             Hook angle
        """
    def GetL1(self) -> float:
        """Get length L1

        Returns:
             Length L1
        """
    def GetL2(self) -> float:
        """Get length L2

        Returns:
             Length L2
        """
    def GetL3(self) -> float:
        """Get length L3

        Returns:
             Length L3
        """
    def GetLongitudinalOffset(self) -> float:
        """Get the longitudinal offset

        Returns:
             Longitudinal offset
        """
    def GetOverlapLength(self) -> float:
        """Get the overlap length

        Returns:
             Overlap length
        """
    def IsCompressionBar(self) -> bool:
        """Get the compression bar state

        Returns:
             Compression bar: true/false
        """
    def SetAnchorageType(self, anchorageType: AnchorageType):
        """Set the anchorage type

        Args:
            anchorageType: Anchorage type
        """
    def SetAsFactor(self, AsFactor: float):
        """Set the as factor required / available

        Args:
            AsFactor: As facto required / availabler
        """
    def SetCompositionZone(self, compositionZone: int):
        """Set the composition zone

        Args:
            compositionZone: Composition zone
        """
    def SetCompressionBar(self, bCompressionBar: bool):
        """Set the compression bar state

        Args:
            bCompressionBar: Compression bar: true/false
        """
    def SetHookAngle(self, hookAngle: float):
        """Set the hook angle

        Args:
            hookAngle: Hook angle
        """
    def SetLongitudinalOffset(self, longitudinalOffset: float):
        """Set the longitudinal offset

        Args:
            longitudinalOffset: longitudinal offset
        """
    def __init__(self):
        """Initialize
        """

class AnchorageType(enum.Enum):
    """Types of the anchorage
    """
    eAnchorageHook = 2
    eAnchorageHookOneCrossBar = 4
    eAnchorageStraight = 1
    eAnchorageStraightOneCrossBar = 3
    eAnchorageStraightTwoCrossBars = 5

    names = {eAnchorageStraight: eAnchorageStraight,
             eAnchorageHook: eAnchorageHook,
             eAnchorageStraightOneCrossBar: eAnchorageStraightOneCrossBar,
             eAnchorageHookOneCrossBar: eAnchorageHookOneCrossBar,
             eAnchorageStraightTwoCrossBars: eAnchorageStraightTwoCrossBars}

    values = {1: eAnchorageStraight,
              2: eAnchorageHook,
              3: eAnchorageStraightOneCrossBar,
              4: eAnchorageHookOneCrossBar,
              5: eAnchorageStraightTwoCrossBars}

    def __getitem__(self, key: (str | int | float)) -> AnchorageType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class BarAreaPlacementProperties():

    class Benching(enum.Enum):
        """Benching type
        """
        HorizontalBenching = 1
        NoBenching = 0
        VerticalBenching = 2

        names = {NoBenching: NoBenching,
                 HorizontalBenching: HorizontalBenching,
                 VerticalBenching: VerticalBenching}

        values = {0: NoBenching,
                  1: HorizontalBenching,
                  2: VerticalBenching}

        def __getitem__(self, key: (str | int | float)) -> BarAreaPlacementProperties.Benching:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class PlacementStrategy(enum.Enum):
        """PlacementStrategy type
        """
        Centered = 2
        FromEnd = 3
        FromStart = 1

        names = {FromStart: FromStart,
                 Centered: Centered,
                 FromEnd: FromEnd}

        values = {1: FromStart,
                  2: Centered,
                  3: FromEnd}

        def __getitem__(self, key: (str | int | float)) -> BarAreaPlacementProperties.PlacementStrategy:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, diameter: float, distance: float, overlapping: float, isMoveOverlapping: bool, maxBarLength: float,
                 startBarLength: float, maxPlacementLength: float, firstBarEdgeDistance: float, placementStrategy: PlacementStrategy, benching: Benching, benchingLength: float, isPolygonalPlacement: bool):
        """Constructor

        Args:
            diameter:             Diameter
            distance:             Distance
            overlapping:          Overlapping
            isMoveOverlapping:    Is overlapping moved: true/false
            maxBarLength:         Maximal bar length
            startBarLength:       Start bar length
            maxPlacementLength:   Maximal placement length, 0 = will be calculated
            firstBarEdgeDistance: First bar edge distance, <0 = will be calculated
            placementStrategy:    Placement strategy
            benching:             Benching
            benchingLength:       Benching length
            isPolygonalPlacement: Place in polygon: true / place per meter: false
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class BarAreaPlacementService():

    def AddOpeningPolygon(self, openingPol: NemAll_Python_Geometry.Polygon3D, openingPol: float):
        """Add an opening polygon

        Args:
            openingPol: Opening polygon
        """
    def Calculate(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, barPlacementProp: BarAreaPlacementProperties,
                  placementMatrix: NemAll_Python_Geometry.Matrix3D, concreteCoverZDir: float) -> list:
        """Calculate the meshes

        Args:
            doc:                 Document
            barPlacementProp:    Placement properties
            placementMatrix:     Placement matrix
            concreteCoverZDir:   Concrete cover in the local z direction
        """
    def SetOuterPolygon(self, placementPol: NemAll_Python_Geometry.Polygon3D, placementPol: float):
        """Constructor

        Args:
            placementPol: Placement polygon
        """
    def __init__(self):
        """Initialize
        """

class BarLabel():
    """Implementation of the bar label
    """
    def GetAdditionalText(self) -> str:
        """Get the additional text

        Returns:
            Additional text
        """
    def GetAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get the angle

        Returns:
            Angle
        """
    def GetDimensionLineOffset(self) -> float:
        """Get the dimension line offset

        Returns:
            Dimension line offset
        """
    def GetLabelOffset(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the label offset for the text pointer

        Returns:
            Label offset for the text pointer from the shape side
        """
    def GetLabelPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the label point

        Returns:
            Label point
        """
    def GetLabelProperties(self) -> BarLabelProperties:
        """Get the label properties

        Returns:
            Label properties
        """
    def GetPointerProperties(self) -> ReinforcementLabelPointerProperties:
        """Get the pointer properties

        Returns:
            Pointer Properties
        """
    def GetPointerStartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the start point of the text pointer

        Returns:
            Start point of the text pointer
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def GetShapeSide(self) -> int:
        """Get the shape side for the text pointer

        Returns:
            Shape side for the text pointer
        """
    def GetShapeSideFactor(self) -> float:
        """Get the factor for the text pointer at the shape side

        Returns:
            Factor for the text pointer at the shape side
        """
    def GetTextProperties(self) -> NemAll_Python_Precast.TextProperties:
        """Get the text properties

        Returns:
            Text properties
        """
    def GetType(self) -> LabelType:
        """Get the label type

        Returns:
            Type of the label
        """
    def GetVisibleBars(self) -> (list[int] | NemAll_Python_Utility.VecIntList):
        """Get the vector with the visible bars

        Returns:
            Vector with the visible bars
        """
    def IsDimensionLineAtShapeStart(self) -> bool:
        """Get the placement state of the dimension line

        Returns:
            Placement of the dimension line as placement start state
        """
    def IsLabelWithComb(self) -> bool:
        """Check for a label with a comb

        Returns:
            Label with a comb: true/false
        """
    def IsLabelWithFan(self) -> bool:
        """Check for a label with a fan

        Returns:
            Label with a fan: true/false
        """
    def IsPointerStartPoint(self) -> bool:
        """Get the state of the start point from the text pointer

        Returns:
            Defined start point exist: true/false
        """
    def IsShowAllBars(self) -> bool:
        """Get the show all bars state

        Returns:
            Show all bars inside the dimension lines, ...
        """
    def IsShowTextPointer(self) -> bool:
        """Get the state for showing the text pointer

        Returns:
            Show the text pointer: true/false
        """
    @PythonPartPylintDecorator.deprecated(replace = " use ShowTextPointerEndSymbol from BarLabelPointerProperties")
    def IsShowTextPointerEndSymbol(self) -> bool:
        """Deprecated: use ShowTextPointerEndSymbol from BarLabelPointerProperties
        """
    def SetAdditionalText(self, additionalText: str):
        """Set the additional text

        Args:
            additionalText: Additional text
        """
    def SetDimensionLineAtShapeStart(self, dimLineAtShapeStart: bool):
        """Set the placement state of the dimension line

        Args:
            dimLineAtShapeStart
        """
    def SetDimensionLineOffset(self, dimLineOffset: float):
        """Set the dimension line offset

        Args:
            dimLineOffset

        Returns:
            Dimension line offset
        """
    def SetLabelOffset(self, labelOffset: NemAll_Python_Geometry.Vector2D):
        """Set the label offset

        Args:
            labelOffset: Label offset
        """
    def SetLabelPoint(self, labelPoint: NemAll_Python_Geometry.Point2D):
        """Set the label point

        Args:
            labelPoint: Label point
        """
    def SetPointerProperties(self, pointerProperties: ReinforcementLabelPointerProperties):
        """Set the pointer properties

        Args:
            pointerProperties: Pointer properties
        """
    def SetPointerStartPoint(self, pointerStartPoint: NemAll_Python_Geometry.Point2D):
        """Set the start pointer of the text pointer

        Args:
            pointerStartPoint: Start point of the text pointer
        """
    def SetShowTextPointer(self, showTextPointer: bool):
        """Set the state for showing the text pointer

        Args:
            showTextPointer: Show the text pointer: true/false
        """
    @PythonPartPylintDecorator.deprecated(replace = " use ShowTextPointerEndSymbol from BarLabelPointerProperties")
    def SetShowTextPointerEndSymbol(self, showTextPointerEndSymbol: bool):
        """Deprecated: use ShowTextPointerEndSymbol from BarLabelPointerProperties

        Args:
            showTextPointerEndSymbol: showTextPointerEndSymbol
        """
    def SetTextProperties(self, textProperties: NemAll_Python_Precast.TextProperties):
        """Set the text properties

        Args:
            textProperties: Text properties
        """
    def SetVisibleBars(self, visibleBars: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Set the vector with the visible bars

        Args:
            visibleBars: Vector with the visible bars: 1, 2, 3, .. index from left; -1, -2, -3, ... index from right, 0 = center
        """
    def ShowAllBars(self, bShowAllBars: bool):
        """Set the all bars inside the dimension line, ... state

        Args:
            bShowAllBars: Show all bars in the dimension lines, ...: true/false
        """
    def ToString(self) -> str:
        """Convert the label data to a string

        Returns:
            String from the label data
        """
    def __eq__(self, label: BarLabel) -> bool:
        """Compare operator

        Args:
            label: Labels to compare

        Returns:
            Labels are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, type: LabelType, positionNumber: int, labelProp: BarLabelProperties, labelPoint: NemAll_Python_Geometry.Point2D,
                 angle: NemAll_Python_Geometry.Angle):
        """Constructor

        Args:
            type:           Label type
            positionNumber: Position number
            labelProp:      Label properties
            labelPoint:     Label placement point
            angle:          Angle
        """
    @typing.overload
    def __init__(self, type: LabelType, positionNumber: int, labelProp: BarLabelProperties, shapeSide: int, shapeSideFactor: float,
                 labelOffset: NemAll_Python_Geometry.Vector2D, angle: NemAll_Python_Geometry.Angle):
        """Constructor

        Args:
            type:            Label type
            positionNumber:  Position number
            labelProp:       Label properties
            shapeSide:       Shape side for the text pointer, starting from 1
            shapeSideFactor: Factor for the text pointer at the shape side
            labelOffset:     Label offset for the text pointer from the shape side
            angle:           Angle
        """
    @typing.overload
    def __init__(self, type: LabelType, positionNumber: int, labelProp: BarLabelProperties, bDimLineAtShapeStart: bool,
                 dimLineOffset: float):
        """Constructor

        Args:
            type:                 Label type
            positionNumber:       Position number
            labelProp:            Label properties
            bDimLineAtShapeStart: Placement of the dimension line: at shape start = true / at shape end = false
            dimLineOffset:        Offset of the dimension line from the placement
        """
    @typing.overload
    def __init__(self, type: LabelType, positionNumber: int, labelProp: BarLabelProperties,
                 pointerProp: ReinforcementLabelPointerProperties, bDimLineAtShapeStart: bool, dimLineOffset: float):
        """Constructor

        Args:
            type:                 Label type
            positionNumber:       Position number
            labelProp:            Label properties
            pointerProp:          Pointer properties
            bDimLineAtShapeStart: Placement of the dimension line: at shape start = true / at shape end = false
            dimLineOffset:        Offset of the dimension line from the placement
        """
    @typing.overload
    def __init__(self, element: BarLabel):
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
    def AdditionalText(self) -> str:
        """Get the additional text
        """
    @AdditionalText.setter
    def AdditionalText(self, additionalText: str) -> None:
        """Set the additional text

        Args:
            additionalText: Additional text
        """
    @property
    def DimensionLineAtShapeStart(self) -> bool:
        """Get the placement state of the dimension line
        """
    @DimensionLineAtShapeStart.setter
    def DimensionLineAtShapeStart(self, value: bool) -> None:
        """Set the placement state of the dimension line
        """
    @property
    def DimensionLineOffset(self) -> float:
        """Get the dimension line offset
        """
    @DimensionLineOffset.setter
    def DimensionLineOffset(self, value: float) -> None:
        """Set the dimension line offset
        """
    @property
    def LabelOffset(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the label offset for the text pointer
        """
    @LabelOffset.setter
    def LabelOffset(self, labelOffset: NemAll_Python_Geometry.Vector2D) -> None:
        """Set the label offset

        Args:
            labelOffset: Label offset
        """
    @property
    def LabelPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the label point
        """
    @LabelPoint.setter
    def LabelPoint(self, labelPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the label point

        Args:
            labelPoint: Label point
        """
    @property
    def PointerProperties(self) -> BarLabelPointerProperties:
        """Get the pointer properties
        """
    @PointerProperties.setter
    def PointerProperties(self, pointerProperties: BarLabelPointerProperties) -> None:
        """Set the pointer properties

        Args:
            pointerProperties: Pointer properties
        """
    @property
    def PointerStartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the start point of the text pointer
        """
    @PointerStartPoint.setter
    def PointerStartPoint(self, pointerStartPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the start pointer of the text pointer

        Args:
            pointerStartPoint: Start point of the text pointer
        """
    @property
    def ShowTextPointer(self) -> bool:
        """Get the state for showing the text pointer
        """
    @ShowTextPointer.setter
    def ShowTextPointer(self, showTextPointer: bool) -> None:
        """Set the state for showing the text pointer

        Args:
            showTextPointer: Show the text pointer: true/false
        """
    @property
    def ShowTextPointerEndSymbol(self) -> bool:
        """Deprecated: use ShowTextPointerEndSymbol from BarLabelPointerProperties
        """
    @ShowTextPointerEndSymbol.setter
    def ShowTextPointerEndSymbol(self, value: bool) -> None:
        """Deprecated: use ShowTextPointerEndSymbol from BarLabelPointerProperties

        Set the value
        """
    @property
    def TextProperties(self) -> NemAll_Python_Precast.TextProperties:
        """Get the text properties
        """
    @TextProperties.setter
    def TextProperties(self, textProperties: NemAll_Python_Precast.TextProperties) -> None:
        """Set the text properties

        Args:
            textProperties: Text properties
        """
    @property
    def VisibleBars(self) -> (list[int] | NemAll_Python_Utility.VecIntList):
        """Get the vector with the visible bars
        """
    @VisibleBars.setter
    def VisibleBars(self, visibleBars: (list[int] | NemAll_Python_Utility.VecIntList)) -> None:
        """Set the vector with the visible bars

        Args:
            visibleBars: Vector with the visible bars: 1, 2, 3, .. index from left; -1, -2, -3, ... index from right, 0 = center
        """

class BarLabelList():
    """List for BarLabel objects
    """
    def __contains__(self, value: BarLabel) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: BarLabel):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: BarLabelList) -> bool:
        """Compare two lists

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> BarLabel:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, eleList: list) -> BarLabelList:
        """Add a list

        Args:
            eleList: BarLabel list

        Returns:
            Lists with the added elements
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ele: BarLabel):
        """Constructor with a BarLabel

        Args:
            ele: BarLabel
        """
    @typing.overload
    def __init__(self, eleList: list):
        """Constructor with a list of BarLabel

        Args:
            eleList: BarLabel list
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
    def __repr__(self) -> str:
        """Create a string from the elements of the list
        """
    def __setitem__(self, index: int | slice, value: BarLabel):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: BarLabel):
        """Append a list item

        Args:
            value: Value to append
        """
    @typing.overload
    def extend(self, iterable: BarLabelList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    @typing.overload
    def extend(self, eleList: list):
        """Extend the list

        Args:
            eleList: BarLabel list
        """
    def extend(self):
        """ Overloaded function. See individual overloads.
        """

class BarLabelPointerProperties():
    """Implementation of the bar label pointer properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, combLineAngle: float, bCombLineByLength: bool, combLineValue: float):
        """Constructor

        Args:
            combLineAngle:     Comb line angle (deg)
            bCombLineByLength: Define the comb line by length = true, by distance = false
            combLineValue:     Value for the comb line length/distance
        """
    @typing.overload
    def __init__(self, element: ReinforcementLabelPointerProperties):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def __repr__() -> str:
        """Convert to string
        """
    @property
    def Color(self) -> int:
        """Get the color
        """
    @Color.setter
    def Color(self, color: int) -> None:
        """Set the color

        Args:
            color: Color
        """
    @property
    def CombLineAngle(self) -> float:
        """Get the comb line angle
        """
    @CombLineAngle.setter
    def CombLineAngle(self, combLineAngle: float) -> None:
        """Set the comb line angle

        Args:
            combLineAngle: Comb line angle
        """
    @property
    def CombLineByLength(self) -> bool:
        """Get the comb line length state
        """
    @CombLineByLength.setter
    def CombLineByLength(self, combLineLengthState: bool) -> None:
        """Set the comb line length state

        Args:
            combLineLengthState: Comb line length state
        """
    @property
    def CombLineValue(self) -> float:
        """Get the comb line length/distance
        """
    @CombLineValue.setter
    def CombLineValue(self, combLineValue: float) -> None:
        """Set the comb line length/distance

        Args:
            combLineValue: Comb line length/distance
        """
    @property
    def EndSymbol(self) -> int:
        """Get the end symbol
        """
    @EndSymbol.setter
    def EndSymbol(self, endSymbol: int) -> None:
        """Set the end symbol

        Args:
            endSymbol: End symbol
        """
    @property
    def EndSymbolSize(self) -> float:
        """Get the end symbol size
        """
    @EndSymbolSize.setter
    def EndSymbolSize(self, endSymbolSize: float) -> None:
        """Set the end symbol size

        Args:
            endSymbolSize: End symbol size
        """
    @property
    def Pen(self) -> int:
        """Get the pen
        """
    @Pen.setter
    def Pen(self, pen: int) -> None:
        """Set the pen

        Args:
            pen: Pen
        """
    @property
    def ShowTextPointerEndSymbol(self) -> bool:
        """Get the state for showing the text pointer end symbol
        """
    @ShowTextPointerEndSymbol.setter
    def ShowTextPointerEndSymbol(self, showTextPointerEndSymbol: bool) -> None:
        """Set the state for showing the text pointer end symbol

        Args:
            showTextPointerEndSymbol: Show the text pointer end symbol: true/false
        """
    @property
    def Stroke(self) -> int:
        """Get the stroke
        """
    @Stroke.setter
    def Stroke(self, stroke: int) -> None:
        """Set the stroke

        Args:
            stroke: Stroke
        """

class BarLabelProperties():
    """Implementation of the reinforcement label properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, prop: BarLabelProperties):
        """Copy constructor

        Args:
            prop: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def ShowBarCount(self) -> bool:
        """Get the show bar count state

        Se the show state for the bar count
        """
    @ShowBarCount.setter
    def ShowBarCount(self, bShowBarCount: bool) -> None:
        """Se the show state for the bar count

        Args:
            bShowBarCount: Show the bar count: true/false
        """
    @property
    def ShowBarDiameter(self) -> bool:
        """Get the show bar diameter state
        """
    @ShowBarDiameter.setter
    def ShowBarDiameter(self, bShowBarDiameter: bool) -> None:
        """Set the show state for the bar diameter

        Args:
            bShowBarDiameter: Show the bar diameter: true/false
        """
    @property
    def ShowBarDistance(self) -> bool:
        """Get the show bar distance state
        """
    @ShowBarDistance.setter
    def ShowBarDistance(self, bShowBarDistance: bool) -> None:
        """Set the show state for the bar distance

        Args:
            bShowBarDistance: Show the bar distance: true/false
        """
    @property
    def ShowBarLayer(self) -> bool:
        """Get the show bar layer state
        """
    @ShowBarLayer.setter
    def ShowBarLayer(self, bShowBarLayer: bool) -> None:
        """Set the show state for the bar layer

        Args:
            bShowBarLayer: Show the bar layer: true/false
        """
    @property
    def ShowBarLength(self) -> bool:
        """Get the show bar length state
        """
    @ShowBarLength.setter
    def ShowBarLength(self, bShowBarLength: bool) -> None:
        """Set the show bar length state

        Args:
            bShowBarLength: Show the bar length: true/false
        """
    @property
    def ShowBarPlace(self) -> bool:
        """Get the show bar place state
        """
    @ShowBarPlace.setter
    def ShowBarPlace(self, bShowBarPlace: bool) -> None:
        """Set the show state for the bar place

        Args:
            bShowBarPlace: Show the bar place: true/false
        """
    @property
    def ShowBendingShape(self) -> bool:
        """Get the show state for the bending shape
        """
    @ShowBendingShape.setter
    def ShowBendingShape(self, bShowBendingShape: bool) -> None:
        """Set the show bending shape state

        Args:
            bShowBendingShape: Show the bending shape: true/false
        """
    @property
    def ShowPositionAtEnd(self) -> bool:
        """Get the position at the end state
        """
    @ShowPositionAtEnd.setter
    def ShowPositionAtEnd(self, bShowPositionAtEnd: bool) -> None:
        """Set the state for position number at the end of the label

        Args:
            bShowPositionAtEnd: Show position number at the end of the label: true/false
        """
    @property
    def ShowPositionNumber(self) -> bool:
        """Get the show position state
        """
    @ShowPositionNumber.setter
    def ShowPositionNumber(self, bShowPositionNumber: bool) -> None:
        """Set the show state for the position number

        Args:
            bShowPositionNumber: Show the position number: true/false
        """
    @property
    def ShowSteelGrade(self) -> bool:
        """Get the show steel grade state

        Show the steel grade
        """
    @ShowSteelGrade.setter
    def ShowSteelGrade(self, bStellGrade: bool) -> None:
        """Show the steel grade

        Args:
            bStellGrade: Show the steel grade: true/false
        """
    @property
    def ShowTwoLineText(self) -> bool:
        """Get the two line text state
        """
    @ShowTwoLineText.setter
    def ShowTwoLineText(self, bShowTwoLineText: bool) -> None:
        """Set the state for the two line text

        Args:
            bShowTwoLineText: Show two line text: true/false
        """

class ReinfElement(NemAll_Python_BasisElements.AllplanElement):


class BarPlacementSection():
    """Implementation of the bar placement section class
    """
    def GetDistance(self) -> float:
        """Get the distance

        Returns:
            Distance
        """
    def GetLength(self) -> float:
        """Get the length

        Returns:
            Length
        """
    def IsEnabled(self) -> bool:
        """Get the enabled state

        Returns:
            Enable state
        """
    @typing.overload
    def __init__(self, isEnabled: bool, length: float, distance: float):
        """Constructor

        Args:
            isEnabled: Section enabled state
            length:    Section length
            distance:  Bar distance
        """
    @typing.overload
    def __init__(self, element: BarPlacementSection):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class BendingShape():
    """Implementation of the reinforcement shape
    """
    def GetBendingRoller(self) -> NemAll_Python_Utility.VecDoubleList:
        """Get the bending roller

        Returns:
            Bending roller
        """
    def GetBendingShapeType(self) -> BendingShapeType:
        """Get the bending shape type

        Returns:
            Bending shape type
        """
    def GetConcreteGrade(self) -> int:
        """Get the concrete grade

        Returns:
            Concrete grade  (index of the global list starting from 0, -1 = use global value from the Allplan settings)
        """
    def GetDiameter(self) -> float:
        """Get the diameter

        Returns:
            Diameter
        """
    def GetHookAngleEnd(self) -> float:
        """Get the hook angle a the end of the shape

        Returns:
            Hook angle at the end of the shape
        """
    def GetHookAngleStart(self) -> float:
        """Get the hook angle a the start of the shape

        Returns:
            Hook angle at the start of the shape
        """
    def GetHookLengthEnd(self) -> float:
        """Get the hook length a the end of the shape

        Returns:
            Hook length at the end of the shape
        """
    def GetHookLengthStart(self) -> float:
        """Get the hook length a the start of the shape

        Returns:
            Hook length at the start of the shape
        """
    def GetHookTypeEnd(self) -> HookType:
        """Get the hook type a the end of the shape

        Returns:
            Hook type a the end of the shape
        """
    def GetHookTypeStart(self) -> HookType:
        """Get the hook type a the start of the shape

        Returns:
            Hook type a the start of the shape
        """
    def GetMeshBendingDirection(self) -> MeshBendingDirection:
        """Get the mesh bending direction

        Returns:
            Mesh bending direction
        """
    def GetMeshType(self) -> str:
        """Get the mesh type

        Returns:
            Mesh type
        """
    def GetShapePolyline(self) -> NemAll_Python_Geometry.Polyline3D:
        """Get the shape polyline

        Returns:
            Shape polyline
        """
    def GetSteelGrade(self) -> int:
        """Get the steel grade

        Returns:
            Steel grade
        """
    def IsValid(self) -> bool:
        """Get the state of the shape

        Returns:
            Shape is valid: true/false
        """
    def Move(self, transVec: NemAll_Python_Geometry.Vector3D):
        """Move the shape

        Args:
            transVec: Move vector
        """
    @typing.overload
    def Rotate(self, modelAngles: object, refPnt: NemAll_Python_Geometry.Point3D):
        """Rotate the shape

        Args:
            modelAngles: Model angles
            refPnt:      Reference point of the rotation
        """
    @typing.overload
    def Rotate(self, modelAngles: object):
        """Rotate the shape

        Args:
            modelAngles: Model angles
        """
    def Rotate(self):
        """ Overloaded function. See individual overloads.
        """
    def SetBendingRoller(self, bendingRoller: NemAll_Python_Utility.VecDoubleList):
        """Set the bending roller

        Args:
            bendingRoller: Bending roller
        """
    def SetDiameter(self, diameter: float):
        """Set the diameter

        Args:
            diameter: diameter
        """
    def SetHookAngleEnd(self, hookAngleEnd: float):
        """Set the hook angle at the end of the shape

        Args:
            hookAngleEnd: Hook angle
        """
    def SetHookAngleStart(self, hookAngleStart: float):
        """Set the hook angle at the start of the shape

        Args:
            hookAngleStart: Hook angle
        """
    def SetHookLengthEnd(self, hookLengthEnd: float):
        """Set the end length of the hook

        Args:
            hookLengthEnd: End length of the hook
        """
    def SetHookLengthStart(self, hookLengthStart: float):
        """Set the start length of the hook

        Args:
            hookLengthStart: Start length of the hook
        """
    def SetHookTypeEnd(self, hookTypeEnd: HookType):
        """Set the hook type at the end of the shape

        Args:
            hookTypeEnd: Hook type
        """
    def SetHookTypeStart(self, hookTypeStart: HookType):
        """Set the hook type at the start of the shape

        Args:
            hookTypeStart: Hook type
        """
    def SetShapePolyline(self, shapePol: NemAll_Python_Geometry.Polyline3D):
        """Set the shape polyline

        Args:
            shapePol: Shape polyline
        """
    def SetSteelGrade(self, steelGrade: int):
        """Set the steel grade

        Args:
            steelGrade: steel grade
        """
    def Transform(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Transform the shape

        Args:
            transMat: Transformation matrix
        """
    def __eq__(self, shape: BendingShape) -> bool:
        """Compare operator

        Args:
            shape: Shape to compare

        Returns:
            Shapes are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, shapePol: NemAll_Python_Geometry.Polyline3D, bendingRoller: NemAll_Python_Utility.VecDoubleList, diameter: float,
                 steelGrade: int, concreteGrade: int, bendingShapeType: BendingShapeType):
        """Constructor

        Args:
            shapePol:         Shape polyline
            bendingRoller:    Bending roller
            diameter:         Diameter
            steelGrade:       Steel grade
            concreteGrade:    Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            bendingShapeType: Bending shape type
        """
    @typing.overload
    def __init__(self, shapePoint: NemAll_Python_Geometry.Point3D, diameter: float, steelGrade: int, concreteGrade: int):
        """Constructor for a point placement

        Args:
            shapePoint:    Shape placement point
            diameter:      Diameter
            steelGrade:    Steel grade
            concreteGrade: Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
        """
    @typing.overload
    def __init__(self, shapePol: NemAll_Python_Geometry.Polyline3D, bendingRoller: NemAll_Python_Utility.VecDoubleList, meshType: str,
                 meshBendingDirection: MeshBendingDirection, steelGrade: int, concreteGrade: int, bendingShapeType: BendingShapeType):
        """Constructor

        Args:
            shapePol:             Shape polyline
            bendingRoller:        Bending roller
            meshType:             Mesh type
            meshBendingDirection: Mesh bending direction
            steelGrade:           Steel grade
            concreteGrade:        Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            bendingShapeType:     Bending shape type
        """
    @typing.overload
    def __init__(self, shapePol: NemAll_Python_Geometry.Polyline3D, bendingRoller: NemAll_Python_Utility.VecDoubleList, diameter: float,
                 steelGrade: int, concreteGrade: int, bendingShapeType: BendingShapeType, hookLengthStart: float, hookAngleStart: float, hookTypeStart: HookType, hookLengthEnd: float, hookAngleEnd: float, hookTypeEnd: HookType):
        """Constructor

        Args:
            shapePol:         Shape polyline
            bendingRoller:    Bending roller
            diameter:         Diameter
            steelGrade:       Steel grade
            concreteGrade:    Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            bendingShapeType: Bending shape type
            hookLengthStart:  Hook length at the start of the shape
            hookAngleStart:   Hook angle at the start of the shape
            hookTypeStart:    Hook type at the start of the shape
            hookLengthEnd:    Hook length at the end of the shape
            hookAngleEnd:     Hook angle at the end of the shape
            hookTypeEnd:      Hook type at the end of the shape
        """
    @typing.overload
    def __init__(self, shapePol: NemAll_Python_Geometry.Polyline3D, bendingRoller: NemAll_Python_Utility.VecDoubleList, meshType: str,
                 meshBendingDirection: MeshBendingDirection, steelGrade: int, concreteGrade: int, bendingShapeType: BendingShapeType, hookLengthStart: float, hookAngleStart: float, hookTypeStart: HookType, hookLengthEnd: float, hookAngleEnd: float, hookTypeEnd: HookType):
        """Constructor

        Args:
            shapePol:             Shape polyline
            bendingRoller:        Bending roller
            meshType:             Mesh type
            meshBendingDirection: Mesh bending direction
            steelGrade:           Steel grade
            concreteGrade:        Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            bendingShapeType:     Bending shape type
            hookLengthStart:      Hook length at the start of the shape
            hookAngleStart:       Hook angle at the start of the shape
            hookTypeStart:        Hook type at the start of the shape
            hookLengthEnd:        Hook length at the end of the shape
            hookAngleEnd:         Hook angle at the end of the shape
            hookTypeEnd:          Hook type at the end of the shape
        """
    @typing.overload
    def __init__(self, element: BendingShape):
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
    def BendingRoller(self) -> list[float]:
        """Get the bending roller
        """
    @BendingRoller.setter
    def BendingRoller(self, bendingRoller: list[float]) -> None:
        """Set the bending roller

        Args:
            bendingRoller: Bending roller
        """
    @property
    def Diameter(self) -> float:
        """Get the diameter
        """
    @Diameter.setter
    def Diameter(self, diameter: float) -> None:
        """Set the diameter

        Args:
            diameter: diameter
        """
    @property
    def HookAngleEnd(self) -> float:
        """Get the hook angle a the end of the shape
        """
    @HookAngleEnd.setter
    def HookAngleEnd(self, hookAngleEnd: float) -> None:
        """Set the hook angle at the end of the shape

        Args:
            hookAngleEnd: Hook angle
        """
    @property
    def HookAngleStart(self) -> float:
        """Get the hook angle a the start of the shape
        """
    @HookAngleStart.setter
    def HookAngleStart(self, hookAngleStart: float) -> None:
        """Set the hook angle at the start of the shape

        Args:
            hookAngleStart: Hook angle
        """
    @property
    def HookLengthEnd(self) -> float:
        """Get the hook length a the end of the shape
        """
    @HookLengthEnd.setter
    def HookLengthEnd(self, hookLengthEnd: float) -> None:
        """Set the end length of the hook

        Args:
            hookLengthEnd: End length of the hook
        """
    @property
    def HookLengthStart(self) -> float:
        """Get the hook length a the start of the shape
        """
    @HookLengthStart.setter
    def HookLengthStart(self, hookLengthStart: float) -> None:
        """Set the start length of the hook

        Args:
            hookLengthStart: Start length of the hook
        """
    @property
    def HookTypeEnd(self) -> HookType:
        """Get the hook type a the end of the shape
        """
    @HookTypeEnd.setter
    def HookTypeEnd(self, hookTypeEnd: HookType) -> None:
        """Set the hook type at the end of the shape

        Args:
            hookTypeEnd: Hook type
        """
    @property
    def HookTypeStart(self) -> HookType:
        """Get the hook type a the start of the shape
        """
    @HookTypeStart.setter
    def HookTypeStart(self, hookTypeStart: HookType) -> None:
        """Set the hook type at the start of the shape

        Args:
            hookTypeStart: Hook type
        """
    @property
    def ShapePolyline(self) -> NemAll_Python_Geometry.Polyline3D:
        """Get the shape polyline
        """
    @ShapePolyline.setter
    def ShapePolyline(self, shapePol: NemAll_Python_Geometry.Polyline3D) -> None:
        """Set the shape polyline

        Args:
            shapePol: Shape polyline
        """
    @property
    def SteelGrade(self) -> int:
        """Get the steel grade
        """
    @SteelGrade.setter
    def SteelGrade(self, steelGrade: int) -> None:
        """Set the steel grade

        Args:
            steelGrade: steel grade
        """

class BarSchema(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the bar schema element
    """
    def GetPlacementPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the placement point

        Returns:
            Placement point
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def Transform(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Transform the schema

        Args:
            transMat: Transformation matrix
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, schema: BarSchema):
        """Implementation of the bar schema element

        Args:
            schema
        """
    @typing.overload
    def __init__(self, positionNumber: int, placementPoint: NemAll_Python_Geometry.Point2D):
        """Constructor

        Args:
            positionNumber: Position number
            placementPoint: Placement point
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def AngleDimensioning(self) -> bool:
        """Get the angle dimensioning state
        """
    @AngleDimensioning.setter
    def AngleDimensioning(self, angleDimensioning: bool) -> None:
        """Set the angle dimensioning state

        Args:
            angleDimensioning: Angle dimensioning state
        """
    @property
    def BendingDimensioning(self) -> bool:
        """Get the bending dimensioning state
        """
    @BendingDimensioning.setter
    def BendingDimensioning(self, bendingDimensioning: bool) -> None:
        """Set the bending dimensioning state

        Args:
            bendingDimensioning: Bending dimensioning state
        """
    @property
    def Dimensioning(self) -> bool:
        """Get the dimensioning state
        """
    @Dimensioning.setter
    def Dimensioning(self, dimensioning: bool) -> None:
        """Set the dimensioning state

        Args:
            dimensioning: Dimensioning state
        """
    @property
    def Mirroring(self) -> SchemaMirror:
        """Get the mirroring
        """
    @Mirroring.setter
    def Mirroring(self, mirror: SchemaMirror) -> None:
        """Set the mirroring

        Args:
            mirror: Mirroring
        """
    @property
    def PlanarView(self) -> bool:
        """Get the planar view state
        """
    @PlanarView.setter
    def PlanarView(self, planarView: bool) -> None:
        """Set the planar view state

        Args:
            planarView: Planar view state
        """
    @property
    def RotationAngle(self) -> float:
        """Get the rotation angle
        """
    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: float) -> None:
        """Set the rotation angle

        Args:
            rotationAngle: Rotation angle in degree
        """
    @property
    def SegmentDimensioning(self) -> bool:
        """Get the segment dimensioning state
        """
    @SegmentDimensioning.setter
    def SegmentDimensioning(self, segmentDimensioning: bool) -> None:
        """Set the segment dimensioning state

        Args:
            segmentDimensioning: Segment dimensioning state
        """
    @property
    def StirrupUnfold(self) -> SchemaStirrupUnfold:
        """Get the mirroring
        """
    @StirrupUnfold.setter
    def StirrupUnfold(self, stirrupUnfold: SchemaStirrupUnfold) -> None:
        """Set the mirroring

        Args:
            stirrupUnfold: Stirrup unfold
        """
    @property
    def ToScale(self) -> bool:
        """Get the to scale state
        """
    @ToScale.setter
    def ToScale(self, toScale: bool) -> None:
        """Set the to scale state

        Args:
            toScale: To scale state
        """

class BarsOperations():

    @staticmethod
    def DivideBarsPlacement(placement: DivideBarsParameters, divisionPolyline: NemAll_Python_Geometry.Polyline2D) -> str:
        """Divide the bars placement

        Returns:
              Result message

        Args:
            placement:           BaseElementAdapter with the placement
            divideBarsParameter: Divide bars parameters
            divisionPolyline:    Divison polyline
        """
    @staticmethod
    def JoinBarsPlacements(placement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, fillEdges: bool) -> str:
        """Join the bars placements

        Returns:
              Result message

        Args:
            placements:          BaseElementAdapterList with the placements
            fillEdges:           Fill the edges: True/False
        """
    def __init__(self):
        """Initialize
        """

class BarsRepresentation(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the bar representation element
    """
    def GetBarPlacement(self) -> BarPlacement:
        """Get the bar placement

        Returns:
            Bar placement
        """
    def GetLabel(self) -> BarLabel:
        """Get the label

        Returns:
            Label
        """
    def GetLabelTextLength(self) -> float:
        """Get the text length of the label

        Returns:
            Text length
        """
    def GetPlacement(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Get the placement

        Returns:
            Placement
        """
    def GetPlacementLine(self) -> NemAll_Python_Geometry.Line2D:
        """Get the placement angle of the representation

        Returns:
            Placement angle
        """
    def GetViewBoundingPolyline(self) -> NemAll_Python_Geometry.Polyline2D:
        """
        """
    def GetirstRepresentationLine(self) -> NemAll_Python_Geometry.Line2D:
        """Get the represenation line of the first bar

        Returns:
            Placement line
        """
    def SetLabel(self, label: BarLabel):
        """Set the label

        Args:
            label: Label                  Associative view for the label
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, representation: BarsRepresentation):
        """Copy constructor

        Args:
            representation: Representation to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Label(self) -> ReinforcementLabel:
        """Get the label
        """
    @Label.setter
    def Label(self, label: ReinforcementLabel) -> None:
        """Set the label

        Args:
            label: Label                  Associative view for the label
        """

class BendingRollerService():
    """Service class for the bending roller calculation
    """
    @staticmethod
    def GetBendBendingRollerFactor(diameter: float, steelGrade: int, concreteGrade: int) -> float:
        """Get the bend bending roller factor

        Args:
            diameter:      Diameter
            steelGrade:    Steel grade
            concreteGrade: Concrete grade

        Returns:
             Bending roller factor
        """
    @staticmethod
    def GetBendingRoller(diameter: float, steelGrade: int, concreteGrade: int, bStirrup: bool) -> float:
        """Get the bending roller

        Args:
            diameter:      Diameter
            steelGrade:    Steel grade
            concreteGrade: Concrete grade
            bStirrup:      Shape is a stirrup: true/false

        Returns:
             Bending roller factor
        """
    @staticmethod
    def GetBendingRollerFactor(diameter: float, steelGrade: int, concreteGrade: int, bStirrup: bool) -> float:
        """Get the bending roller factor

        Args:
            diameter:      Diameter
            steelGrade:    Steel grade
            concreteGrade: Concrete grade
            bStirrup:      Shape is a stirrup: true/false

        Returns:
             Bending roller factor
        """
    @staticmethod
    def GetDefaultBendingRollers(norm: NormType) -> NemAll_Python_Utility.VecDoubleList:
        """Get the default bending rollers for the norm

        Args:
            norm: Norm. If set to -1, the current norm is used

        Returns:
             Default bending rollers for specified norm
        """

class BarPositionData(BendingShape):
    """Implementation of the bar position data
    """
    def GetCount(self) -> int:
        """Get the count

        Returns:
            Count
        """
    def GetLength(self) -> float:
        """Get the length

        Returns:
            length
        """
    def GetPosition(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def GetSubPosition(self) -> int:
        """Get the sub position number

        Returns:
            Sub position number
        """
    def SetCount(self, count: int):
        """Set the count

        Args:
            count: Count
        """
    def SetLength(self, length: float):
        """Set the length

        Args:
            length: length
        """
    def SetPosition(self, position: int):
        """Set the position number

        Args:
            position: Position
        """
    def SetSubPosition(self, subPosition: int):
        """Set the sub position number

        Args:
            subPosition: Sub position
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, barElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Constructor

        Args:
            barElement: Bar element
        """
    @typing.overload
    def __init__(self, param: BarPositionData):
        """Copy constructor

        Args:
            param
        """
    @typing.overload
    def __init__(self, bendingShape: BendingShape):
        """Constructor

        Args:
            bendingShape: Bending shape
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Count(self) -> int:
        """Get the count
        """
    @Count.setter
    def Count(self, count: int) -> None:
        """Set the count

        Args:
            count: Count
        """
    @property
    def Length(self) -> float:
        """Get the length
        """
    @Length.setter
    def Length(self, length: float) -> None:
        """Set the length

        Args:
            length: length
        """
    @property
    def Position(self) -> int:
        """Get the position number
        """
    @Position.setter
    def Position(self, position: int) -> None:
        """Set the position number

        Args:
            position: Position
        """
    @property
    def SubPosition(self) -> int:
        """Get the sub position number
        """
    @SubPosition.setter
    def SubPosition(self, subPosition: int) -> None:
        """Set the sub position number

        Args:
            subPosition: Sub position
        """

class BendingShapeList():
    """List for BendingShape objects
    """
    def __contains__(self, value: BendingShape) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: BendingShape):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: BendingShapeList) -> bool:
        """Compare two lists

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> BendingShape:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, eleList: list) -> BendingShapeList:
        """Add a list

        Args:
            eleList: BendingShape list

        Returns:
            Lists with the added elements
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ele: BendingShape):
        """Constructor with a BendingShape

        Args:
            ele: BendingShape
        """
    @typing.overload
    def __init__(self, eleList: list):
        """Constructor with a list of BendingShape

        Args:
            eleList: BendingShape list
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
    def __repr__(self) -> str:
        """Create a string from the elements of the list
        """
    def __setitem__(self, index: int | slice, value: BendingShape):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: BendingShape):
        """Append a list item

        Args:
            value: Value to append
        """
    @typing.overload
    def extend(self, iterable: BendingShapeList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    @typing.overload
    def extend(self, eleList: list):
        """Extend the list

        Args:
            eleList: BendingShape list
        """
    def extend(self):
        """ Overloaded function. See individual overloads.
        """

class BendingShapeType(enum.Enum):
    """Type of the bending shape
    """
    BarSpacer = 113
    BarWithArc = 115
    CircleStirrup = 67
    ColumnStirrup = 110
    Freeform = 99
    LShapedBar = 11
    LongitudinalBar = 0
    LongitudinalBarDoubleBentOff = 26
    LongitudinalBarFourTimesBentOff = 44
    LongitudinalBarSingleBentOff = 15
    OpenStirrup = 21
    SHook = 112
    Stirrup = 51
    TorsionStirrup = 111

    names = {LongitudinalBar: LongitudinalBar,
             LShapedBar: LShapedBar,
             OpenStirrup: OpenStirrup,
             LongitudinalBarSingleBentOff: LongitudinalBarSingleBentOff,
             LongitudinalBarDoubleBentOff: LongitudinalBarDoubleBentOff,
             LongitudinalBarFourTimesBentOff: LongitudinalBarFourTimesBentOff,
             ColumnStirrup: ColumnStirrup,
             Stirrup: Stirrup,
             TorsionStirrup: TorsionStirrup,
             SHook: SHook,
             BarSpacer: BarSpacer,
             CircleStirrup: CircleStirrup,
             BarWithArc: BarWithArc,
             Freeform: Freeform}

    values = {0: LongitudinalBar,
              11: LShapedBar,
              21: OpenStirrup,
              15: LongitudinalBarSingleBentOff,
              26: LongitudinalBarDoubleBentOff,
              44: LongitudinalBarFourTimesBentOff,
              110: ColumnStirrup,
              51: Stirrup,
              111: TorsionStirrup,
              112: SHook,
              113: BarSpacer,
              67: CircleStirrup,
              115: BarWithArc,
              99: Freeform}

    def __getitem__(self, key: (str | int | float)) -> BendingShapeType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class CircularAreaElement(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the bar placement element
    """
    def GetConcreteCoverContour(self) -> float:
        """Get the concrete cover from the contour

        Returns:
            Concrete cover from the contour
        """
    def GetConcreteCoverEnd(self) -> float:
        """Get the concrete cover from the end

        Returns:
            Concrete cover from the end
        """
    def GetConcreteCoverStart(self) -> float:
        """Get the concrete cover from the start

        Returns:
            Concrete cover from the start
        """
    def GetConcreteGrade(self) -> int:
        """Get the concrete grade

        Returns:
            Concrete grade  (index of the global list starting from 0, -1 = use global value from the Allplan settings)
        """
    def GetContourPoints(self) -> NemAll_Python_Geometry.Polyline3D:
        """Get the contour points

        Returns:
            Contour points
        """
    def GetDiameter(self) -> float:
        """Get the diameter

        Returns:
            Diameter
        """
    def GetDistance(self) -> float:
        """Get the distance

        Returns:
            Distance
        """
    def GetEvenFirstLength(self) -> float:
        """Get the first length for the even ring number

        Returns:
            First length for the even ring number
        """
    def GetEvenOverlapEnd(self) -> float:
        """Get the overlap length at the end for the even ring number

        Returns:
            Overlap length at the end for the even ring number
        """
    def GetEvenOverlapStart(self) -> float:
        """Get the overlap length at the start for the even ring number

        Returns:
            Overlap length at the start for the even ring number
        """
    def GetLengthFactor(self) -> float:
        """Get the length factor

        Returns:
            Length factor
        """
    def GetMaxBarLength(self) -> float:
        """Get the maximal bar length

        Returns:
            Maximal bar length
        """
    def GetMaxBarRise(self) -> float:
        """Get the maximal bar radius

        Returns:
            Maximal bar radius
        """
    def GetMinBarLength(self) -> float:
        """Get the minimal bar length

        Returns:
            Minimal bar length
        """
    def GetMinBarRadius(self) -> float:
        """Get the minimal bar radius

        Returns:
            Minimal bar radius
        """
    def GetOddFirstLength(self) -> float:
        """Get the first length for the odd ring number

        Returns:
            First length for the odd ring number
        """
    def GetOddOverlapEnd(self) -> float:
        """Get the overlap length at the end for the odd ring number

        Returns:
            Overlap length at the end for the odd ring number
        """
    def GetOddOverlapStart(self) -> float:
        """Get the overlap length at the start for the even ring number

        Returns:
            Overlap length at the start for the odd ring number
        """
    def GetOuterAngleEnd(self) -> float:
        """Get the outer angle at the end

        Returns:
            Outer angle at the end
        """
    def GetOuterAngleStart(self) -> float:
        """Get the outer angle at the start

        Returns:
            Outer angle at the start
        """
    def GetOverlapLength(self) -> float:
        """Get the overlap length

        Returns:
            Overlap length
        """
    def GetPlacementRule(self) -> int:
        """Get the placement rule

        Returns:
            Placement rule
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def GetRotationAxis(self) -> NemAll_Python_Geometry.Line3D:
        """Get the rotation axis

        Returns:
            Rotation axis
        """
    def GetSteelGrade(self) -> int:
        """Get the steel grade

        Returns:
            Steel grade
        """
    def GetinnerAngleEnd(self) -> float:
        """Get the inner angle at the end

        Returns:
            Inner angle at the end
        """
    def GetinnerAngleStart(self) -> float:
        """Get the inner angle at the start

        Returns:
            Inner angle at the start
        """
    def IsPlacePerLinearMeter(self) -> bool:
        """Get the place per linear meter state

        Returns:
            Place per linear meter: true/false
        """
    def IsbOverlapEndAsCircle(self) -> bool:
        """Get the overlap state at the end

        Returns:
            Overlap length at the end as circle = true, as tangent = false
        """
    def IsbOverlapStartAsCircle(self) -> bool:
        """Get the overlap state at the start

        Returns:
            Overlap length at the start as circle = true, as tangent = false
        """
    def SetBarProperties(self, distance: float, maxBarLength: float, minBarLength: float, placementRule: int, oddFirstLength: float,
                         evenFirstLength: float, minBarRadius: float, maxBarRise: float):
        """Set the bar properties

        Args:
            distance:        Distance
            maxBarLength:    Maximal bar length
            minBarLength:    Minimal bar length
            placementRule:   Placement rule
            oddFirstLength:  First length for the odd ring number
            evenFirstLength: First bar length for the event ring number
            minBarRadius:    Minimal bar radius
            maxBarRise:      Maximal bar rise
        """
    def SetLengthFactor(self, lengthFactor: float):
        """Set the length factor

        Args:
            lengthFactor: Length factor
        """
    def SetOverlap(self, oddOverlapStart: float, evenOverlapStart: float, bOverlapStartAsCircle: bool, oddOverlapEnd: float,
                   evenOverlapEnd: float, bOverlapEndAsCircle: bool, overlapLength: float):
        """Set the overlap

        Args:
            oddOverlapStart:       Overlap length at the start for the odd ring number
            evenOverlapStart:      Overlap length at the start for the even ring number
            bOverlapStartAsCircle: Overlap length at the start as circle = true, as tangent = false
            oddOverlapEnd:         Overlap length at the end for the odd ring number
            evenOverlapEnd:        Overlap length at the end for the even ring number
            bOverlapEndAsCircle:   Overlap length at the end as circle = true, as tangent = false
            overlapLength:         Overlap length
        """
    def SetPlacePerLinearMeter(self, bPlacePerLinearMeter: bool):
        """Set the place per linear meter state

        Args:
            bPlacePerLinearMeter: Place per linear meter: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, positionNumber: int, diameter: float, steelGrade: int, concreteGrade: int,
                 rotationAxis: NemAll_Python_Geometry.Line3D, contourPoints: NemAll_Python_Geometry.Polyline3D, outerAngleStart: float, outerAngleEnd: float, innerAngleStart: float, innerAngleEnd: float, concreteCoverStart: float, concreteCoverEnd: float, concreteCoverContour: float):
        """Constructor

        Args:
            positionNumber:       Position number
            diameter:             Diameter
            steelGrade:           Steel grade
            concreteGrade:        Concrete grade
            rotationAxis:         Rotation axis
            contourPoints:        Contour points
            outerAngleStart:      Outer angle at the start
            outerAngleEnd:        Outer angle at the end
            innerAngleStart:      Inner angle at the start
            innerAngleEnd:        Inner angle at the end
            concreteCoverStart:   Concrete cover at the start
            concreteCoverEnd:     Concrete cover at the end
            concreteCoverContour: Concrete cover of the contour
        """
    @typing.overload
    def __init__(self, element: CircularAreaElement):
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
    def LengthFactor(self) -> float:
        """Get the length factor
        """
    @LengthFactor.setter
    def LengthFactor(self, lengthFactor: float) -> None:
        """Set the length factor

        Args:
            lengthFactor: Length factor
        """
    @property
    def PlacePerLinearMeter(self) -> bool:
        """Get the place per linear meter state
        """
    @PlacePerLinearMeter.setter
    def PlacePerLinearMeter(self, bPlacePerLinearMeter: bool) -> None:
        """Set the place per linear meter state

        Args:
            bPlacePerLinearMeter: Place per linear meter: true/false
        """

class DivideBarsParameters():
    """Parameters for dividing engineering geometry
    """
    class eDivideMode(enum.Enum):
        """Information of Divide Mode
        """
        GAP = 2
        OVERLAP = 0
        PLANE = 1

        names = {OVERLAP: OVERLAP,
                 PLANE: PLANE,
                 GAP: GAP}

        values = {0: OVERLAP,
                  1: PLANE,
                  2: GAP}

        def __getitem__(self, key: (str | int | float)) -> DivideBarsParameters.eDivideMode:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class eInputMode(enum.Enum):
        """Information of input mode
        """
        ELEMENT2D = 2
        OPENING = 1
        POLYGON = 0

        names = {POLYGON: POLYGON,
                 OPENING: OPENING,
                 ELEMENT2D: ELEMENT2D}

        values = {0: POLYGON,
                  1: OPENING,
                  2: ELEMENT2D}

        def __getitem__(self, key: (str | int | float)) -> DivideBarsParameters.eInputMode:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class eLengthPosition(enum.Enum):
        """Information of position of Overlap-/Gap-Length
        """
        LEFT = 0
        MIDDLE = 1
        RIGHT = 2

        names = {LEFT: LEFT,
                 MIDDLE: MIDDLE,
                 RIGHT: RIGHT}

        values = {0: LEFT,
                  1: MIDDLE,
                  2: RIGHT}

        def __getitem__(self, key: (str | int | float)) -> DivideBarsParameters.eLengthPosition:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def GetTrimLens(self) -> tuple[float, float]:
        """Get necessary length to lengthen/shorten bar parts

        Returns:
            tuple(lengthen/shorten left bar part,
                  lengthen/shorten right bar part)
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, DivideMode: eDivideMode, OverlapPosition: eLengthPosition, OverlapLength: float, GapPosition: eLengthPosition,
                 GapLength: float):
        """Constructor

        Args:
            DivideMode:      Mode of division
            OverlapPosition: Position of Overlap
            OverlapLength:   Overlap length
            GapPosition:     Position of Gap
            GapLength:       Gap length
        """
    @typing.overload
    def __init__(self, element: DivideBarsParameters):
        """Copy constructor

        Args:
            element: Element to copy
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
    def DivideMode(self) -> DivideBarsParameters.eDivideMode:
        """Get the mode of division
        """
    @DivideMode.setter
    def DivideMode(self, DivideMode: DivideBarsParameters.eDivideMode) -> None:
        """Set the mode of division

        Args:
            DivideMode: Mode of division
        """
    @property
    def GapLength(self) -> float:
        """Get the gap length
        """
    @GapLength.setter
    def GapLength(self, GapLength: float) -> None:
        """Set the gap length

        Args:
            GapLength: Gap length
        """
    @property
    def GapPosition(self) -> DivideBarsParameters.eLengthPosition:
        """Get the position of gap
        """
    @GapPosition.setter
    def GapPosition(self, GapPosition: DivideBarsParameters.eLengthPosition) -> None:
        """Set the position of gap

        Args:
            GapPosition: Position of gap
        """
    @property
    def OverlapLength(self) -> float:
        """Get the overlap length
        """
    @OverlapLength.setter
    def OverlapLength(self, OverlapLength: float) -> None:
        """Set the overlap length

        Args:
            OverlapLength: Overlap length
        """
    @property
    def OverlapPosition(self) -> DivideBarsParameters.eLengthPosition:
        """Get the position of overlap
        """
    @OverlapPosition.setter
    def OverlapPosition(self, OverlapPosition: DivideBarsParameters.eLengthPosition) -> None:
        """Set the position of overlap

        Args:
            OverlapPosition: Position of overlap
        """
    ELEMENT2D = eInputMode.ELEMENT2D
    GAP = eDivideMode.GAP
    LEFT = eLengthPosition.LEFT
    MIDDLE = eLengthPosition.MIDDLE
    OPENING = eInputMode.OPENING
    OVERLAP = eDivideMode.OVERLAP
    PLANE = eDivideMode.PLANE
    POLYGON = eInputMode.POLYGON
    RIGHT = eLengthPosition.RIGHT

class EngCatCrossSection():
    """Implementation of engineering catalog cross section
    """
    def __init__(self):
        """Initialize
        """
    @property
    def Name(self) -> None:
        """:type: None
        """
    @property
    def Steelname(self) -> None:
        """:type: None
        """

class EngCatDiameter():
    """Implementation of engineering catalog Diameter
    """
    def __init__(self):
        """Initialize
        """
    @property
    def Area(self) -> None:
        """:type: None
        """
    @property
    def Comment(self) -> None:
        """:type: None
        """
    @property
    def Diameter(self) -> None:
        """:type: None
        """
    @property
    def ID(self) -> None:
        """:type: None
        """
    @property
    def Weight(self) -> None:
        """:type: None
        """

class EngCatMesh():
    """Implementation of engineering catalog Mesh
    """
    def __init__(self):
        """Initialize
        """
    @property
    def ID(self) -> None:
        """:type: None
        """
    @property
    def Length(self) -> None:
        """:type: None
        """
    @property
    def Width(self) -> None:
        """:type: None
        """

class EngCatMeshGroup(EngCatCrossSection):
    """Implementation of engineering catalog mesh group
    """
    def __init__(self):
        """Initialize
        """

class EngCatSteel(EngCatCrossSection):
    """Implementation of engineering catalog steel
    """
    def __init__(self):
        """Initialize
        """
    @property
    def Index(self) -> None:
        """:type: None
        """
    @property
    def Shortname(self) -> None:
        """:type: None
        """
    @property
    def Strength(self) -> None:
        """:type: None
        """

class ExtrudeBarPlacement(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the extrude bar placement element
    """
    class eEdgeOffsetType(enum.Enum):
        """Edge offset type
        """
        eMajorValueAtEnd = 3
        eMajorValueAtStart = 1
        eStartEqualEnd = 2
        eZeroAtEnd = 4
        eZeroAtStart = 0

        names = {eZeroAtStart: eZeroAtStart,
                 eMajorValueAtStart: eMajorValueAtStart,
                 eStartEqualEnd: eStartEqualEnd,
                 eMajorValueAtEnd: eMajorValueAtEnd,
                 eZeroAtEnd: eZeroAtEnd}

        values = {0: eZeroAtStart,
                  1: eMajorValueAtStart,
                  2: eStartEqualEnd,
                  3: eMajorValueAtEnd,
                  4: eZeroAtEnd}

        def __getitem__(self, key: (str | int | float)) -> ExtrudeBarPlacement.eEdgeOffsetType:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class eProfileRotation(enum.Enum):
        """Profile rotation
        """
        eNoRotation = 0
        eStandard = 1
        eZ_Axis = 2

        names = {eNoRotation: eNoRotation,
                 eStandard: eStandard,
                 eZ_Axis: eZ_Axis}

        values = {0: eNoRotation,
                  1: eStandard,
                  2: eZ_Axis}

        def __getitem__(self, key: (str | int | float)) -> ExtrudeBarPlacement.eProfileRotation:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def AddCrossBendingShape(self, shape: BendingShape):
        """Add a cross bending shape

        Args:
            shape: Reinforcement shape
        """
    def AddLongitudinalBarProp(self, longitudinalBarProp: LongitudinalBarProperties):
        """Add the longitudinal bar properties

        Args:
            longitudinalBarProp: longitudinal bar properties
        """
    def AddPlacementSection(self, placementSection: BarPlacementSection) -> bool:
        """Add a placement section

        Args:
            placementSection: Section

        Returns:
            Section is added: true/false
        """
    def Extrude(self):
        """Extrude the bars
        """
    def GetBarOffset(self) -> float:
        """Get the bar offset

        Returns:
            Bar offset
        """
    def GetBendingShapeViewVector(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the view vector of the bending shape

        Returns:
            View vector of the bending shape
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetConcreteCoverEnd(self) -> float:
        """Get the concrete cover at the end of the path

        Returns:
            Concrete cover at the end of the path
        """
    def GetConcreteCoverStart(self) -> float:
        """Get the concrete cover at the start of the path

        Returns:
            Concrete cover at the start of the path
        """
    def GetCrossBarDistance(self) -> float:
        """Get the cross bar distance

        Returns:
            Cross bar distance
        """
    def GetCrossBendingShapes(self) -> BendingShapeList:
        """Get the cross bending shapes

        Returns:
            Cross bending shapes
        """
    def GetEdgeOffsetEnd(self) -> float:
        """Get the edge offset at the end of the path

        Returns:
            Edge offset at the end of the path
        """
    def GetEdgeOffsetStart(self) -> float:
        """Get the edge offset at the start of the path

        Returns:
            Edge offset at the start of the path
        """
    def GetEdgeOffsetType(self) -> eEdgeOffsetType:
        """Get the edge offset type

        Returns:
            Edge offset type
        """
    def GetEdgeOffsets(self) -> tuple:
        """Get the edge offsets

        Returns:
            Edge offsets
        """
    def GetMaxBreakAngle(self) -> float:
        """Get the maximal break angle

        Returns:
            Maximal break angle
        """
    def GetPlacementPath(self) -> NemAll_Python_Geometry.Path3D:
        """Get the placement path

        Returns:
            Placement path
        """
    def GetPlacementSections(self) -> object:
        """Get the placement sections

        Returns:
            Placement sections
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def GetProfileRoation(self) -> eProfileRotation:
        """Get the profile rotation

        Returns:
            Profile rotation
        """
    def IsBreakElimination(self) -> bool:
        """Get the break eliminination state

        Returns:
            Break elimination state
        """
    def Move(self, transVec: NemAll_Python_Geometry.Vector3D):
        """Move the placement

        Args:
            transVec: Move vector
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def Transform(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Transform the placement

        Args:
            transMat: Transformation matrix
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, placement: ExtrudeBarPlacement):
        """Copy constructor

        Args:
            placement: Placement to copy
        """
    @typing.overload
    def __init__(self, positionNumber: int, path: NemAll_Python_Geometry.Path3D, profileRotation: eProfileRotation, breakElimination: bool,
                 maxBreakAngle: float, crossBarDistance: float, concreteCoverStart: float, concreteCoverEnd: float, edgeOffsetType: eEdgeOffsetType, edgeOffsetStart: float, edgeOffsetEnd: float, barOffset: float, bendingShapeViewVector: NemAll_Python_Geometry.Vector3D):
        """Constructor for cross bars

        Args:
            positionNumber:         Position number
            path:                   Path
            profileRotation:        Profile rotation
            breakElimination:       Break elemination
            maxBreakAngle:          Maximal break angle
            crossBarDistance:       Cross bar distance
            concreteCoverStart:     Concrete cover at the start of the path
            concreteCoverEnd:       Concrete cover at the end of the path
            edgeOffsetType:         Get the edge offset type of the path
            edgeOffsetStart:        Edge offset at the start of the path
            edgeOffsetEnd:          Edge offset at the end of the path
            barOffset:              Bar offset
            bendingShapeViewVector: View vector of the bending shape
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, value: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties
        """
    @property
    def PositionNumber(self) -> int:
        """Get the position number
        """
    @PositionNumber.setter
    def PositionNumber(self, value: int) -> None:
        """Set the position number
        """
    eMajorValueAtEnd = eEdgeOffsetType.eMajorValueAtEnd
    eMajorValueAtStart = eEdgeOffsetType.eMajorValueAtStart
    eNoRotation = eProfileRotation.eNoRotation
    eStandard = eProfileRotation.eStandard
    eStartEqualEnd = eEdgeOffsetType.eStartEqualEnd
    eZ_Axis = eProfileRotation.eZ_Axis
    eZeroAtEnd = eEdgeOffsetType.eZeroAtEnd
    eZeroAtStart = eEdgeOffsetType.eZeroAtStart

class GeometryExpansionUtil():

    def GetLineAbove(self, arg2: NemAll_Python_Geometry.Point2D, arg3: NemAll_Python_Geometry.Line2D, arg4: bool, arg5: int) -> tuple:
        """Get the line above the base line and the placement point
        """
    def GetLineAtPoint(self, arg2: NemAll_Python_Geometry.Point2D, arg3: NemAll_Python_Geometry.Vector2D, arg4: bool, arg5: float) -> tuple:
        """Get the line at the defined point of the reference line
        """
    def GetLineFromPoint(self, arg2: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, arg3: NemAll_Python_Geometry.Point2D,
                         arg4: NemAll_Python_IFW_Input.ViewWorldProjection, arg5: bool) -> tuple:
        """Get the line near to the input point
        """
    def GetLineLeft(self, arg2: NemAll_Python_Geometry.Point2D, arg3: NemAll_Python_Geometry.Line2D, arg4: bool, arg5: int) -> tuple:
        """Get the line left from the base line and the placement point
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, pMsgInfo: NemAll_Python_IFW_Input.AddMsgInfo, use3DGeometry: bool):
        """Constructor

        Args:
            pMsgInfo:      Additional message info
            use3DGeometry: Use the 3D geometry for the expansione: true/false
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class HookLengthService():
    """Service class for the hook length calculation
    """
    def GetHookLength(self, hookAngle: float, hookType: HookType, diameter: float) -> float:
        """Calculate the hook length

        Args:
            hookAngle: Hook angle
            hookType:  Hook type
            diameter:  Diameter

        Returns:
             Hook length
        """
    def GetHookLengthPartFromBendingRoller(self, hookAngle: float, hookType: HookType, diameter: float) -> float:
        """Calculate the hook length part from the beginning of the bending roller

        Args:
            hookAngle: Hook angle
            hookType:  Hook type
            diameter:  Diameter

        Returns:
             Hook length part from the beginning of the bending roller
        """
    def GetHookLengthPartOfBendingRoller(self, hookAngle: float, hookType: HookType, diameter: float) -> float:
        """Calculate the hook length part of the bending roller

        Args:
            hookAngle: Hook angle
            hookType:  Hook type
            diameter:  Diameter

        Returns:
             Hook length part of the bending roller
        """
    def GetStandardAnchorageHookLength(self, diameter: float) -> float:
        """Calculate the standard anchorage hook length

        Args:
            diameter: Diameter

        Returns:
             Standard anchorage hook length
        """
    def __init__(self, norm: int, concreteGrade: int, steelGrade: int, bExactLength: bool):
        """Constructor

        Args:
            norm:          Norm
            concreteGrade: Concrete grade
            steelGrade:    Steel grade
            bExactLength:  Calculate the exact length
        """

class HookType(enum.Enum):
    """Types of the hooks
    """
    eAnchorage = 3
    eAngle = 2
    eStirrup = 1

    names = {eStirrup: eStirrup,
             eAngle: eAngle,
             eAnchorage: eAnchorage}

    values = {1: eStirrup,
              2: eAngle,
              3: eAnchorage}

    def __getitem__(self, key: (str | int | float)) -> HookType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class LabelType(enum.Enum):
    """Definition of the label types

    LabelWithPointer          :
    LabelWithDimensionLine    :
    LabelWithComb             :
    LabelWithComb2Pointer     :
    LabelWithComb3Pointer     :
    LabelWithFan              :
    LabelWithFanStartEnd      :
    LabelWithFanStartCenterEnd:
    """
    LabelWithComb = 2
    LabelWithComb2Pointer = 3
    LabelWithComb3Pointer = 4
    LabelWithDimensionLine = 1
    LabelWithFan = 5
    LabelWithFanStartCenterEnd = 7
    LabelWithFanStartEnd = 6
    LabelWithPointer = 0

    names = {LabelWithPointer: LabelWithPointer,
             LabelWithDimensionLine: LabelWithDimensionLine,
             LabelWithComb: LabelWithComb,
             LabelWithComb2Pointer: LabelWithComb2Pointer,
             LabelWithComb3Pointer: LabelWithComb3Pointer,
             LabelWithFan: LabelWithFan,
             LabelWithFanStartEnd: LabelWithFanStartEnd,
             LabelWithFanStartCenterEnd: LabelWithFanStartCenterEnd}

    values = {0: LabelWithPointer,
              1: LabelWithDimensionLine,
              2: LabelWithComb,
              3: LabelWithComb2Pointer,
              4: LabelWithComb3Pointer,
              5: LabelWithFan,
              6: LabelWithFanStartEnd,
              7: LabelWithFanStartCenterEnd}

    def __getitem__(self, key: (str | int | float)) -> LabelType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class LongitudinalBarProperties():
    """Implementation of the longitudinal bar properties
    """
    class eDeliveryShapeType(enum.Enum):
        """Delivery shape types
        """
        eRound = 1
        eStraight = 0

        names = {eStraight: eStraight,
                 eRound: eRound}

        values = {0: eStraight,
                  1: eRound}

        def __getitem__(self, key: (str | int | float)) -> LongitudinalBarProperties.eDeliveryShapeType:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class eInsideBarsState(enum.Enum):
        """Inside bar state
        """
        eExact = 0
        eOverlapped = 2
        eShortened = 1

        names = {eExact: eExact,
                 eShortened: eShortened,
                 eOverlapped: eOverlapped}

        values = {0: eExact,
                  1: eShortened,
                  2: eOverlapped}

        def __getitem__(self, key: (str | int | float)) -> LongitudinalBarProperties.eInsideBarsState:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def GetBendingShape(self) -> BendingShape:
        """Get the bending shape

        Returns:
            Bending shape
        """
    def GetDeliveryShapeType(self) -> eDeliveryShapeType:
        """Get the delivery shape type

        Returns:
            Delivery shape type
        """
    def GetInsideBarsState(self) -> eInsideBarsState:
        """Get the insid bars state

        Returns:
            Inside bars state
        """
    def GetMinBarDistance(self) -> float:
        """Get the minimal bar distance

        Returns:
            Minimal bar distance
        """
    def GetOverlappingAtEnd(self) -> float:
        """Get the overlapping at end

        Returns:
            Overlapping at end
        """
    def GetOverlappingAtStart(self) -> float:
        """Get the overlapping at start

        Returns:
            Overlapping at start
        """
    def GetOverlappingLength(self) -> float:
        """Get the overlapping length

        Returns:
            Overlapping length
        """
    def GetStartLength(self) -> float:
        """Get the start length

        Returns:
            Start length
        """
    def IsOverlappingAtEndTurnedOn(self) -> bool:
        """Get the overlapping at end state

        Returns:
            Overlapping at end state
        """
    def IsOverlappingAtStartTurnedOn(self) -> bool:
        """Get the overlapping at start state

        Returns:
            Overlapping at start state
        """
    def SetBendingShape(self, shape: BendingShape):
        """Set the bending shape

        Args:
            shape: Shape

        Returns:
            Bending shape
        """
    def __eq__(self, : LongitudinalBarProperties) -> bool:
        """Compare operator

        Args:

        Returns:
            Bars are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, shape: BendingShape, overlappingAtStartTurnedOn: bool, overlappingAtStart: float, overlappingAtEndTurnedOn: bool,
                 overlappingAtEnd: float, overlappingLength: float, minBarDistance: float, deliveryShapeType: eDeliveryShapeType, insideBarsState: eInsideBarsState, startLength: float):
        """Constructor

        Args:
            shape:                      Bar shape
            overlappingAtStartTurnedOn: Overlapping at start start
            overlappingAtStart:         Overlapping at start
            overlappingAtEndTurnedOn:   Overlapping at end state
            overlappingAtEnd:           Overlapping at end
            overlappingLength:          Overlapping length
            minBarDistance:             Minimal bar distance
            deliveryShapeType:          Delivery shape type
            insideBarsState:            Inside bars state
            startLength:                Start length
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def BendingShape(self) -> BendingShape:
        """Get the bending shape
        """
    @BendingShape.setter
    def BendingShape(self, value: BendingShape) -> None:
        """Set the bending shape
        """
    eExact = eInsideBarsState.eExact
    eOverlapped = eInsideBarsState.eOverlapped
    eRound = eDeliveryShapeType.eRound
    eShortened = eInsideBarsState.eShortened
    eStraight = eDeliveryShapeType.eStraight

class LongitudinalBarPropertiesList():
    """List for LongitudinalBarProperties objects
    """
    def __contains__(self, value: LongitudinalBarProperties) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: LongitudinalBarProperties):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: LongitudinalBarPropertiesList) -> bool:
        """Compare two lists
        """
    def __getitem__(self, index: int) -> LongitudinalBarProperties:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __init__(self):
        """Initialize
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
    def __setitem__(self, index: int | slice, value: LongitudinalBarProperties):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: LongitudinalBarProperties):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: LongitudinalBarPropertiesList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class MeshAreaPlacementProperties():

    class MeshPlacementDirection(enum.Enum):
        """Mesh placement direction
        """
        Cross = 1
        Longitudinal = 0

        names = {Longitudinal: Longitudinal,
                 Cross: Cross}

        values = {0: Longitudinal,
                  1: Cross}

        def __getitem__(self, key: (str | int | float)) -> MeshAreaPlacementProperties.MeshPlacementDirection:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """
    @property
    def LapJointOffset(self) -> None:
        """Get/set the lap joint offset state

        :type: None
        """
    @property
    def MeshSizeRound(self) -> None:
        """Get/set the mesh size round state

        :type: None
        """
    @property
    def OverlapCross(self) -> None:
        """Get/set the cross overlap

        :type: None
        """
    @property
    def OverlapLongitudinal(self) -> None:
        """Get/set the longitudinal overlap

        :type: None
        """
    @property
    def PlacementDirection(self) -> None:
        """Get/set the placement direction

        :type: None
        """
    @property
    def PlacementEndJustified(self) -> None:
        """Get/set the placement end justified state

        :type: None
        """
    @property
    def PlacementStartChange(self) -> None:
        """Get/set the placement start change state

        :type: None
        """
    @property
    def StartLength(self) -> None:
        """Get/set the start length

        :type: None
        """
    @property
    def StartWidth(self) -> None:
        """Get/set the start width

        :type: None
        """

class MeshAreaPlacementService():

    def AddOpeningPolygon(self, openingPol: NemAll_Python_Geometry.Polygon3D, openingPol: float):
        """Add an opening polygon

        Args:
            openingPol: Opening polygon
        """
    def Calculate(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, doc: MeshData, mesh: MeshAreaPlacementProperties,
                  placementMatrix: NemAll_Python_Geometry.Matrix3D, startPositionNumber: int, concreteCoverZDir: float) -> list:
        """Calculate the meshes

        Args:
            doc:                 Document
            mesh:                Mesh data
            placementMatrix:     Placement matrix
            startPositionNumber: Start position number
            concreteCoverZDir:   Concrete cover in the local z direction
        """
    def SetOuterPolygon(self, placementPol: NemAll_Python_Geometry.Polygon3D, placementPol: float):
        """Constructor

        Args:
            placementPol: Placement polygon
        """
    def __init__(self):
        """Initialize
        """

class MeshBendingDirection(enum.Enum):
    """Types of the mesh bending direction
    """
    CrossBars = 0
    LongitudinalBars = 1

    names = {LongitudinalBars: LongitudinalBars,
             CrossBars: CrossBars}

    values = {1: LongitudinalBars,
              0: CrossBars}

    def __getitem__(self, key: (str | int | float)) -> MeshBendingDirection:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class MeshData():
    """Implementation of the mesh data
    """
    def CreateLabel(self):
        """Create the label
        """
    @staticmethod
    def Format(type: str, length: float, width: float) -> str:
        """Get the mesh text

        Args:
            type:   Mesh type
            length: Mesh length
            width:  Mesh width

        Returns:
            Mesh text
        """
    def GetAsBendingDirection(self, bendingDirection: MeshBendingDirection) -> float:
        """Get the as in bending direction

        Args:
            bendingDirection: Bending direction

        Returns:
            As in bending direction
        """
    def GetDiameterBendingDirection(self, bendingDirection: MeshBendingDirection) -> tuple[float, bool]:
        """Get the diameter in bending direction

        Args:
            bendingDirection: Bending direction

        Returns:
            tuple(Diameter in bending direction,
                  Double bar state)
        """
    def GetDimensions(self) -> tuple[float, float]:
        """Get the mesh dimensions

        Returns:
            tuple(Mesh length,
                  Mesh width)
        """
    def GetDistanceBendingDirection(self, bendingDirection: MeshBendingDirection) -> float:
        """Get the distance in bending direction

        Args:
            bendingDirection: Bending direction

        Returns:
            Distance in bending direction
        """
    def GetOverlapBendingDirection(self, bendingDirection: MeshBendingDirection) -> float:
        """Get the overlap in bending direction

        Args:
            bendingDirection: Bending direction

        Returns:
            Overlap in bending direction
        """
    def SetType(self, type: str):
        """Set the mesh type

        Args:
            type: Mesh type
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, type: str, length: float, width: float, diameterLongitudinal: float, diameterCross: float, asLongitudinal: float,
                 asCross: float, distanceLongitudinal: float, distanceCross: float, bDoubleBarLongitudinal: bool, bDoubleBarCross: bool, overlapLongitudinal: float, overlapCross: float, weight: float):
        """Constructor

        Args:
            type:                   Mesh type
            length:                 Mesh length
            width:                  Mesh width
            diameterLongitudinal:   Diameter in longitudinal direction
            diameterCross:          Diameter in cross direction
            asLongitudinal:         As in longitudinal direction
            asCross:                As in cross direction
            distanceLongitudinal:   Distance in longitudinal direction
            distanceCross:          Distance in cross direction
            bDoubleBarLongitudinal: Double bar in longitudinal direction
            bDoubleBarCross:        Double bar in cross direction
            overlapLongitudinal:    Overlap in longitudinal direction
            overlapCross:           Overlap in cross direction
            weight:                 Mesh weight
        """
    @typing.overload
    def __init__(self, element: MeshData):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def AsBendingDirection(self) -> float:
        """Get the as in bending direction
        """
    @property
    def AsCross(self) -> float:
        """Get the as in cross direction
        """
    @property
    def AsLongitudinal(self) -> float:
        """Get the as in longitudinal direction
        """
    @property
    def DiameterCross(self) -> float:
        """Get the diameter in cross direction
        """
    @property
    def DiameterLongitudinal(self) -> float:
        """Get the diameter in longitudinal direction
        """
    @property
    def DistanceBendingDirection(self) -> float:
        """Get the distance in bending direction
        """
    @property
    def DistanceCross(self) -> float:
        """Get the distance in cross direction
        """
    @property
    def DistanceLongitudinal(self) -> float:
        """Get the distance in longitudinal direction
        """
    @property
    def IsDoubleBarCross(self) -> bool:
        """Get the double bar state in cross direction
        """
    @property
    def IsDoubleBarLongitudinal(self) -> bool:
        """Get the double bar state in longitudinal direction
        """
    @property
    def Label(self) -> str:
        """Get the mesh label
        """
    @property
    def Length(self) -> float:
        """Get the mesh length
        """
    @property
    def OverlapBendingDirection(self) -> float:
        """Get the overlap in bending direction
        """
    @property
    def OverlapCross(self) -> float:
        """Get the overlap in cross direction
        """
    @property
    def OverlapLongitudinal(self) -> float:
        """Get the overlap in longitudinal direction
        """
    @property
    def Type(self) -> str:
        """Get the mesh type
        """
    @Type.setter
    def Type(self, type: str) -> None:
        """Set the mesh type

        Args:
            type: Mesh type
        """
    @property
    def Weight(self) -> float:
        """Get the mesh weight
        """
    @property
    def Width(self) -> float:
        """Get the mesh width
        """

class MeshLabel():
    """Implementation of the reinforcement label
    """
    def ToString(self) -> str:
        """Convert the label data to a string

        Returns:
            String from the label data
        """
    def __eq__(self, label: MeshLabel) -> bool:
        """Compare operator

        Args:
            label: Labels to compare

        Returns:
            Labels are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, positionNumber: int, labelProp: MeshLabelProperties, labelPoint: NemAll_Python_Geometry.Point2D):
        """Constructor

        Args:
            positionNumber: Position number
            labelProp:      Label properties
            labelPoint:     Label placement point
        """
    @typing.overload
    def __init__(self, positionNumber: int, labelProp: MeshLabelProperties, shapeSide: int, shapeSideFactor: float,
                 labelOffset: NemAll_Python_Geometry.Vector2D):
        """Constructor

        Args:
            positionNumber:  Position number
            labelProp:       Label properties
            shapeSide:       Shape side for the text pointer, starting from 1
            shapeSideFactor: Factor for the text pointer at the shape side
            labelOffset:     Label offset for the text pointer from the shape side
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def AutomaticTextPointer(self) -> bool:
        """Get the state for create the text pointer automatically
        """
    @AutomaticTextPointer.setter
    def AutomaticTextPointer(self, automaticTextPointer: bool) -> None:
        """Set the state for create the text pointer automatically

        Args:
            automaticTextPointer: Screate the text pointer automatically: true/false
        """
    @property
    def LabelOffset(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the label offset for the text pointer
        """
    @LabelOffset.setter
    def LabelOffset(self, labelOffset: NemAll_Python_Geometry.Vector2D) -> None:
        """Set the label offset

        Args:
            labelOffset: Label offset
        """
    @property
    def LabelPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the label point
        """
    @LabelPoint.setter
    def LabelPoint(self, labelPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the label point

        Args:
            labelPoint: Label point
        """
    @property
    def LabelProperties(self) -> MeshLabelProperties:
        """Get the label properties
        """
    @property
    def PointerProperties(self) -> MeshLabelPointerProperties:
        """Get the pointer properties
        """
    @PointerProperties.setter
    def PointerProperties(self, pointerProperties: MeshLabelPointerProperties) -> None:
        """Set the pointer properties

        Args:
            pointerProperties: Text properties
        """
    @property
    def PointerStartPoint(self) -> NemAll_Python_Geometry.Point2D:
        """Get the start point of the text pointer
        """
    @PointerStartPoint.setter
    def PointerStartPoint(self, pointerStartPoint: NemAll_Python_Geometry.Point2D) -> None:
        """Set the start pointer of the text pointer

        Args:
            pointerStartPoint: Start point of the text pointer
        """
    @property
    def PositionNumber(self) -> int:
        """Get the position number
        """
    @property
    def ShapeSide(self) -> int:
        """Get the shape side for the text pointer
        """
    @property
    def ShapeSideFactor(self) -> float:
        """Get the factor for the text pointer at the shape side
        """
    @property
    def ShowTextPointer(self) -> bool:
        """Get the state for showing the text pointer
        """
    @ShowTextPointer.setter
    def ShowTextPointer(self, showTextPointer: bool) -> None:
        """Set the state for showing the text pointer

        Args:
            showTextPointer: Show the text pointer: true/false
        """
    @property
    def TextProperties(self) -> ReinforcementLabelTextProperties:
        """Get the text properties
        """
    @TextProperties.setter
    def TextProperties(self, textProperties: ReinforcementLabelTextProperties) -> None:
        """Set the text properties

        Args:
            textProperties: Text properties
        """

class MeshLabelList():
    """List for MeshLabel objects
    """
    def __contains__(self, value: MeshLabel) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: MeshLabel):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: MeshLabelList) -> bool:
        """Compare two lists

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> MeshLabel:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, eleList: list) -> MeshLabelList:
        """Add a list

        Args:
            eleList: MeshLabel list

        Returns:
            Lists with the added elements
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ele: MeshLabel):
        """Constructor with a MeshLabel

        Args:
            ele: MeshLabel
        """
    @typing.overload
    def __init__(self, eleList: list):
        """Constructor with a list of MeshLabel

        Args:
            eleList: MeshLabel list
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
    def __repr__(self) -> str:
        """Create a string from the elements of the list
        """
    def __setitem__(self, index: int | slice, value: MeshLabel):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: MeshLabel):
        """Append a list item

        Args:
            value: Value to append
        """
    @typing.overload
    def extend(self, iterable: MeshLabelList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    @typing.overload
    def extend(self, eleList: list):
        """Extend the list

        Args:
            eleList: MeshLabel list
        """
    def extend(self):
        """ Overloaded function. See individual overloads.
        """

class MeshLabelPointerProperties():
    """Implementation of the mesh label pointer properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: MeshLabelPointerProperties):
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
    def Color(self) -> int:
        """Get the color
        """
    @Color.setter
    def Color(self, color: int) -> None:
        """Set the color

        Args:
            color: Color
        """
    @property
    def EndSymbol(self) -> int:
        """Get the end symbol
        """
    @EndSymbol.setter
    def EndSymbol(self, endSymbol: int) -> None:
        """Set the end symbol

        Args:
            endSymbol: End symbol
        """
    @property
    def EndSymbolSize(self) -> float:
        """Get the end symbol size
        """
    @EndSymbolSize.setter
    def EndSymbolSize(self, endSymbolSize: float) -> None:
        """Set the end symbol size

        Args:
            endSymbolSize: End symbol size
        """
    @property
    def Pen(self) -> int:
        """Get the pen
        """
    @Pen.setter
    def Pen(self, pen: int) -> None:
        """Set the pen

        Args:
            pen: Pen
        """
    @property
    def ShowTextPointerEndSymbol(self) -> bool:
        """Get the state for showing the text pointer end symbol
        """
    @ShowTextPointerEndSymbol.setter
    def ShowTextPointerEndSymbol(self, showTextPointerEndSymbol: bool) -> None:
        """Set the state for showing the text pointer end symbol

        Args:
            showTextPointerEndSymbol: Show the text pointer end symbol: true/false
        """
    @property
    def Stroke(self) -> int:
        """Get the stroke
        """
    @Stroke.setter
    def Stroke(self, stroke: int) -> None:
        """Set the stroke

        Args:
            stroke: Stroke
        """

class MeshLabelProperties():
    """Implementation of the reinforcement label properties
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, prop: MeshLabelProperties):
        """Copy constructor

        Args:
            prop: Properties to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def ShowMeshCount(self) -> bool:
        """Get the show mesh count state

        Se the show state for the bar count
        """
    @ShowMeshCount.setter
    def ShowMeshCount(self, bShowMeshCount: bool) -> None:
        """Se the show state for the bar count

        Args:
            bShowMeshCount: Show the bar count: true/false
        """
    @property
    def ShowMeshDimensions(self) -> bool:
        """Get the show mesh dimensions state
        """
    @ShowMeshDimensions.setter
    def ShowMeshDimensions(self, bShowMeshDimensions: bool) -> None:
        """Set the show mesh dimensions state

        Args:
            bShowMeshDimensions: Show the mesh dimensions: true/false
        """
    @property
    def ShowMeshType(self) -> bool:
        """Get the show mesh type state
        """
    @ShowMeshType.setter
    def ShowMeshType(self, bShowMeshType: bool) -> None:
        """Set the show state for the mesh type

        Args:
            bShowMeshType: Show the mesh type: true/false
        """
    @property
    def ShowPositionAtEnd(self) -> bool:
        """Get the position at the end state
        """
    @ShowPositionAtEnd.setter
    def ShowPositionAtEnd(self, bShowPositionAtEnd: bool) -> None:
        """Set the state for position number at the end of the label

        Args:
            bShowPositionAtEnd: Show position number at the end of the label: true/false
        """
    @property
    def ShowPositionNumber(self) -> bool:
        """Get the show position state
        """
    @ShowPositionNumber.setter
    def ShowPositionNumber(self, bShowPositionNumber: bool) -> None:
        """Set the show state for the position number

        Args:
            bShowPositionNumber: Show the position number: true/false
        """

class MeshOperations():

    @staticmethod
    def CutMesh(placements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, divisionLine: NemAll_Python_Geometry.Polygon2D) -> str:
        """Divide the bars placement

        Returns:
              Result message

        Args:
            placement:     BaseElementAdapter with the placement
            cutPolygon:    Cut polygon
        """
    def __init__(self):
        """Initialize
        """

class MeshPlacement(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the mesh placement element
    """
    def GetBendingShape(self) -> BendingShape:
        """Get the shape polyline

        Returns:
            Shape polyline
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def GetWidthVector(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the width vector

        Returns:
            Width vector
        """
    def Move(self, transVec: NemAll_Python_Geometry.Vector3D):
        """Move the placement

        Args:
            transVec: Move vector
        """
    def SetBendingShape(self, shape: BendingShape):
        """Set the reinforcement shape

        Args:
            shape: Reinforcement shape
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetLabel(self, label: MeshLabel, labelAssocView: NemAll_Python_IFW_ElementAdapter.AssocViewElementAdapter):
        """Set the label

        Args:
            label:          Label
            labelAssocView: Associative view for the label
        """
    def SetPositionNumber(self, positionNumber: int):
        """Set the position number

        Args:
            positionNumber: Position number
        """
    def SetWidthVector(self, widthVec: NemAll_Python_Geometry.Vector3D):
        """Set the width vector

        Args:
            widthVec: Width vector
        """
    def Transform(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Transform the placement

        Args:
            transMat: Transformation matrix
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, positionNumber: int, widthVec: NemAll_Python_Geometry.Vector3D, bendingShape: BendingShape):
        """Constructor

        Args:
            positionNumber: Position number
            widthVec:       Width vector of the mesh
            bendingShape:   Mesh shape
        """
    @typing.overload
    def __init__(self, element: MeshPlacement):
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
    def BendingShape(self) -> BendingShape:
        """Get the shape polyline
        """
    @BendingShape.setter
    def BendingShape(self, shape: BendingShape) -> None:
        """Set the reinforcement shape

        Args:
            shape: Reinforcement shape
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    @property
    def PositionNumber(self) -> int:
        """Get the position number
        """
    @PositionNumber.setter
    def PositionNumber(self, positionNumber: int) -> None:
        """Set the position number

        Args:
            positionNumber: Position number
        """
    @property
    def WidthVector(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the width vector
        """
    @WidthVector.setter
    def WidthVector(self, widthVec: NemAll_Python_Geometry.Vector3D) -> None:
        """Set the width vector

        Args:
            widthVec: Width vector
        """

class NormType(enum.Enum):
    """Types of the norms
    """
    eNORM_AS = 8
    eNORM_BS = 5
    eNORM_DIN = 0
    eNORM_DIN_1 = 10
    eNORM_DIN_H = 4
    eNORM_EC2 = 6
    eNORM_EHE = 7
    eNORM_NEN = 9
    eNORM_NF = 3
    eNORM_OE = 2
    eNORM_SIA = 1
    eNORM_SNIP = 11
    eNORM_SNIP2003 = 12
    eNormNo = -1

    names = {eNormNo: eNormNo,
             eNORM_DIN: eNORM_DIN,
             eNORM_SIA: eNORM_SIA,
             eNORM_OE: eNORM_OE,
             eNORM_NF: eNORM_NF,
             eNORM_DIN_H: eNORM_DIN_H,
             eNORM_BS: eNORM_BS,
             eNORM_EC2: eNORM_EC2,
             eNORM_EHE: eNORM_EHE,
             eNORM_AS: eNORM_AS,
             eNORM_NEN: eNORM_NEN,
             eNORM_DIN_1: eNORM_DIN_1,
             eNORM_SNIP: eNORM_SNIP,
             eNORM_SNIP2003: eNORM_SNIP2003}

    values = {-1: eNormNo,
              0: eNORM_DIN,
              1: eNORM_SIA,
              2: eNORM_OE,
              3: eNORM_NF,
              4: eNORM_DIN_H,
              5: eNORM_BS,
              6: eNORM_EC2,
              7: eNORM_EHE,
              8: eNORM_AS,
              9: eNORM_NEN,
              10: eNORM_DIN_1,
              11: eNORM_SNIP,
              12: eNORM_SNIP2003}

    def __getitem__(self, key: (str | int | float)) -> NormType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PlaneMeshPlacement(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the mesh placement element
    """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetMeshData(self) -> MeshData:
        """Get the mesh data

        Returns:
            Mesh data
        """
    def GetMeshLength(self) -> float:
        """Get the mesh length

        Returns:
            Mesh length
        """
    def GetMeshPolygon(self) -> NemAll_Python_Geometry.Polygon3D:
        """Get the shape polyline

        Returns:
            Shape polyline
        """
    def GetMeshWidth(self) -> float:
        """Get the mesh width

        Returns:
            Mesh width
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def IsValid(self) -> bool:
        """Get the state of the shape

        Returns:
            Shape is valid: true/false
        """
    def Move(self, transVec: NemAll_Python_Geometry.Vector3D):
        """Move the placement

        Args:
            transVec: Move vector
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetMeshPolygon(self, shape: NemAll_Python_Geometry.Polygon3D):
        """Set the reinforcement shape

        Args:
            shape: Reinforcement shape
        """
    def SetPositionNumber(self, positionNumber: int):
        """Set the position number

        Args:
            positionNumber: Position number
        """
    def Transform(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Transform the placement

        Args:
            transMat: Transformation matrix
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, placement: PlaneMeshPlacement):
        """Copy constructor

        Args:
            placement: Placement to copy
        """
    @typing.overload
    def __init__(self, positionNumber: int, meshData: MeshData, meshLength: float, meshWidth: float,
                 meshPolygon: NemAll_Python_Geometry.Polygon3D):
        """Constructor

        Args:
            positionNumber: Position number
            meshData:       Mesh data
            meshLength:     Mesh length
            meshWidth:      Mesh width
            meshPolygon:    Mesh polygon
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    @property
    def MeshPolygon(self) -> NemAll_Python_Geometry.Polygon3D:
        """Get the shape polyline
        """
    @MeshPolygon.setter
    def MeshPolygon(self, shape: NemAll_Python_Geometry.Polygon3D) -> None:
        """Set the reinforcement shape

        Args:
            shape: Reinforcement shape
        """
    @property
    def PositionNumber(self) -> int:
        """Get the position number
        """
    @PositionNumber.setter
    def PositionNumber(self, positionNumber: int) -> None:
        """Set the position number

        Args:
            positionNumber: Position number
        """

class BarPlacement(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the bar placement element
    """
    def GetBarCount(self) -> int:
        """Get the bar count

        Returns:
            Bar count
        """
    def GetBendingShape(self) -> BendingShape:
        """Get the shape polyline

        Returns:
            Shape polyline
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetDistanceVector(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the distance vector

        Returns:
            Distance vector
        """
    def GetEndBendingShape(self) -> BendingShape:
        """Get the shape polyline at the end of a polygonal placement

        Returns:
            Shape polyline
        """
    def GetEndPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the end point of the placement at the placement line

        Returns:
            End point of the placement at the placement line
        """
    def GetLabel(self) -> BarLabel:
        """Get the label

        Returns:
            Label
        """
    def GetLengthFactor(self) -> float:
        """Get the length factor

        Returns:
            Length factor
        """
    def GetPlacementMatrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """Get the placement matrix of the first bar

        Returns:
            Placement matrix
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def GetRotationAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get the rotation angle

        Returns:
            Rotation angle
        """
    def GetRotationAxis(self) -> NemAll_Python_Geometry.Line3D:
        """Get the rotation axis

        Returns:
            Rotation axis
        """
    def GetStartPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get start point of the placement at the placement line

        Returns:
            Start point of the placement at the placement line
        """
    def IsPlacePerLinearMeter(self) -> bool:
        """Get the place per linear meter state

        Returns:
            Place per linear meter: true/false
        """
    def IsPolygonalPlacement(self) -> bool:
        """Get the polygonal placement state

        Returns:
            Polygonal placement: true/false
        """
    def IsRotationalPlacement(self) -> bool:
        """Get the rotational placement state

        Returns:
            Rotational placement: true/false
        """
    def Move(self, transVec: NemAll_Python_Geometry.Vector3D):
        """Move the placement

        Args:
            transVec: Move vector
        """
    def SetBarCount(self, barCount: int):
        """Set the bar count

        Args:
            barCount: Bar count
        """
    def SetBendingShape(self, shape: BendingShape):
        """Set the reinforcement shape

        Args:
            shape: Reinforcement shape
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetDistanceVector(self, distVec: NemAll_Python_Geometry.Vector3D):
        """Set the distance vector

        Args:
            distVec: Distance vector
        """
    def SetEndBendingShape(self, shape: BendingShape):
        """Set the reinforcement shape at the end

        Args:
            shape: Reinforcement shape
        """
    def SetLabel(self, label: BarLabel, labelAssocView: NemAll_Python_IFW_ElementAdapter.AssocViewElementAdapter):
        """Set the label

        Args:
            label:          Label
            labelAssocView: Associative view for the label
        """
    def SetLengthFactor(self, lengthFactor: float):
        """Set the length factor

        Args:
            lengthFactor: Length factor
        """
    def SetPartialSchema(self, schema: BarSchema):
        """Set the partial schema for the placement

        Args:
            schema: Schema
        """
    def SetPlacePerLinearMeter(self, bPlacePerLinearMeter: bool):
        """Set the place per linear meter state

        Args:
            bPlacePerLinearMeter: Place per linear meter: true/false
        """
    def SetPositionNumber(self, positionNumber: int):
        """Set the position number

        Args:
            positionNumber: Position number
        """
    def SetRotationAngle(self, rotationAngle: float):
        """Set the rotation angle

        Args:
            rotationAngle: Rotation angle
        """
    def SetRotationAxis(self, rotationAxis: NemAll_Python_Geometry.Line3D):
        """Set the rotation axis

        Args:
            rotationAxis: Rotation axis
        """
    def SetRotationalPlacement(self, bRotationalPlacement: bool):
        """Set the rotational placement state

        Args:
            bRotationalPlacement: Rotational placement state
        """
    def Transform(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Transform the placement

        Args:
            transMat: Transformation matrix
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, placement: BarPlacement):
        """Copy constructor

        Args:
            placement: Placement to copy
        """
    @typing.overload
    def __init__(self, positionNumber: int, barCount: int, distVec: NemAll_Python_Geometry.Vector3D,
                 startPnt: NemAll_Python_Geometry.Point3D, endPnt: NemAll_Python_Geometry.Point3D, bendingShape: BendingShape):
        """Constructor

        Args:
            positionNumber: Position number
            barCount:       Bar count
            distVec:        Distance vector
            startPnt:       Start point of the placement at the placement line
            endPnt:         End point of the placement at the placement line
            bendingShape:   Bending shape
        """
    @typing.overload
    def __init__(self, positionNumber: int, barCount: int, startBendingShape: BendingShape, endBendingShape: BendingShape):
        """Constructor

        Args:
            positionNumber:    Position number
            barCount:          Bar count
            startBendingShape: Start shape of the polygonal placement
            endBendingShape:   End shape of the polygonal placement
        """
    @typing.overload
    def __init__(self, positionNumber: int, barCount: int, rotationAxis: NemAll_Python_Geometry.Line3D,
                 rotationAngle: NemAll_Python_Geometry.Angle, bendingShape: BendingShape):
        """Constructor for the rotational placement

        Args:
            positionNumber: Position number
            barCount:       Bar count
            rotationAxis:   Rotation point
            rotationAngle:  Rotation angle
            bendingShape:   Bending shape
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def BarCount(self) -> int:
        """Get the bar count
        """
    @BarCount.setter
    def BarCount(self, barCount: int) -> None:
        """Set the bar count

        Args:
            barCount: Bar count
        """
    @property
    def BendingShape(self) -> BendingShape:
        """Get the shape polyline
        """
    @BendingShape.setter
    def BendingShape(self, shape: BendingShape) -> None:
        """Set the reinforcement shape

        Args:
            shape: Reinforcement shape
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    @property
    def DistanceVector(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the distance vector
        """
    @DistanceVector.setter
    def DistanceVector(self, distVec: NemAll_Python_Geometry.Vector3D) -> None:
        """Set the distance vector

        Args:
            distVec: Distance vector
        """
    @property
    def EndBendingShape(self) -> BendingShape:
        """Get the shape polyline at the end of a polygonal placement
        """
    @EndBendingShape.setter
    def EndBendingShape(self, shape: BendingShape) -> None:
        """Set the reinforcement shape at the end

        Args:
            shape: Reinforcement shape
        """
    @property
    def LengthFactor(self) -> float:
        """Get the length factor
        """
    @LengthFactor.setter
    def LengthFactor(self, lengthFactor: float) -> None:
        """Set the length factor

        Args:
            lengthFactor: Length factor
        """
    @property
    def PlacePerLinearMeter(self) -> bool:
        """Get the place per linear meter state
        """
    @PlacePerLinearMeter.setter
    def PlacePerLinearMeter(self, bPlacePerLinearMeter: bool) -> None:
        """Set the place per linear meter state

        Args:
            bPlacePerLinearMeter: Place per linear meter: true/false
        """
    @property
    def PositionNumber(self) -> int:
        """Get the position number
        """
    @PositionNumber.setter
    def PositionNumber(self, positionNumber: int) -> None:
        """Set the position number

        Args:
            positionNumber: Position number
        """
    @property
    def RotationAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get the rotation angle
        """
    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: NemAll_Python_Geometry.Angle) -> None:
        """Set the rotation angle

        Args:
            rotationAngle: Rotation angle
        """
    @property
    def RotationAxis(self) -> NemAll_Python_Geometry.Line3D:
        """Get the rotation axis
        """
    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: NemAll_Python_Geometry.Line3D) -> None:
        """Set the rotation axis

        Args:
            rotationAxis: Rotation axis
        """
    @property
    def RotationalPlacement(self) -> bool:
        """Get the rotational placement state
        """
    @RotationalPlacement.setter
    def RotationalPlacement(self, bRotationalPlacement: bool) -> None:
        """Set the rotational placement state

        Args:
            bRotationalPlacement: Rotational placement state
        """

class ReinforcementLabel(BarLabel):
    """Deprecated: use BarLabel instead!
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, reinforcementType: ReinforcementType, type: LabelType, positionNumber: int, labelProp: ReinforcementLabelProperties,
                 labelPoint: NemAll_Python_Geometry.Point2D, angle: NemAll_Python_Geometry.Angle):
        """Constructor

        Args:
            reinforcementType: Reinforcement type
            type:              Label type
            positionNumber:    Position number
            labelProp:         Label properties
            labelPoint:        Label placement point
            angle:             Angle
        """
    @typing.overload
    def __init__(self, reinforcementType: ReinforcementType, type: LabelType, positionNumber: int, labelProp: ReinforcementLabelProperties,
                 shapeSide: int, shapeSideFactor: float, labelOffset: NemAll_Python_Geometry.Vector2D, angle: NemAll_Python_Geometry.Angle):
        """Constructor

        Args:
            reinforcementType: Reinforcement type
            type:              Label type
            positionNumber:    Position number
            labelProp:         Label properties
            shapeSide:         Shape side for the text pointer
            shapeSideFactor:   Factor for the text pointer at the shape side
            labelOffset:       Label offset for the text pointer from the shape side
            angle:             Angle
        """
    @typing.overload
    def __init__(self, reinforcementType: ReinforcementType, type: LabelType, positionNumber: int, labelProp: ReinforcementLabelProperties,
                 bDimLineAtShapeStart: bool, dimLineOffset: float):
        """Constructor

        Args:
            reinforcementType:    Reinforcement type
            type:                 Label type
            positionNumber:       Position number
            labelProp:            Label properties
            bDimLineAtShapeStart: Placement of the dimension line: at shape start = true / at shape end = false
            dimLineOffset:        Offset of the dimension line from the placement
        """
    @typing.overload
    def __init__(self, reinforcementType: ReinforcementType, type: LabelType, positionNumber: int, labelProp: ReinforcementLabelProperties,
                 pointerProp: ReinforcementLabelPointerProperties, bDimLineAtShapeStart: bool, dimLineOffset: float):
        """Constructor

        Args:
            reinforcementType:    Reinforcement type
            type:                 Label type
            positionNumber:       Position number
            labelProp:            Label properties
            pointerProp:          Pointer properties
            bDimLineAtShapeStart: Placement of the dimension line: at shape start = true / at shape end = false
            dimLineOffset:        Offset of the dimension line from the placement
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class ReinforcementLabelList():
    """List for ReinforcementLabel objects
    """
    def __contains__(self, value: ReinforcementLabel) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: ReinforcementLabel):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: ReinforcementLabelList) -> bool:
        """Compare two lists

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> ReinforcementLabel:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, eleList: list) -> ReinforcementLabelList:
        """Add a list

        Args:
            eleList: ReinforcementLabel list

        Returns:
            Lists with the added elements
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ele: ReinforcementLabel):
        """Constructor with a ReinforcementLabel

        Args:
            ele: ReinforcementLabel
        """
    @typing.overload
    def __init__(self, eleList: list):
        """Constructor with a list of ReinforcementLabel

        Args:
            eleList: ReinforcementLabel list
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
    def __repr__(self) -> str:
        """Create a string from the elements of the list
        """
    def __setitem__(self, index: int | slice, value: ReinforcementLabel):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: ReinforcementLabel):
        """Append a list item

        Args:
            value: Value to append
        """
    @typing.overload
    def extend(self, iterable: ReinforcementLabelList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    @typing.overload
    def extend(self, eleList: list):
        """Extend the list

        Args:
            eleList: ReinforcementLabel list
        """
    def extend(self):
        """ Overloaded function. See individual overloads.
        """

class ReinforcementLabelPointerProperties():
    """Deprecated: use BarLabelPointerProperties instead!
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, combLineAngle: float, bCombLineByLength: bool, combLineValue: float):
        """Initialize
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class ReinforcementLabelProperties(BarLabelProperties):
    """Deprecated: use BarLabelProperties instead!
    """
    def __init__(self):
        """Initialize
        """

class ReinforcementLabelTextProperties():
    """Implementation of the reinforcement label Text properties
    """
    def ToString(self) -> str:
        """Convert the properties to a string

        Returns:
            String with the properties
        """
    def __eq__(self, prop: ReinforcementLabelTextProperties) -> bool:
        """Compare the properties

        Args:
            prop: Properties to compare

        Returns:
            Properties are equal
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: ReinforcementLabelTextProperties):
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
    def Alignment(self) -> NemAll_Python_Precast.TextAlignment:
        """Get the
        """
    @Alignment.setter
    def Alignment(self, value: NemAll_Python_Precast.TextAlignment) -> None:
        """Set the
        """
    @property
    def Font(self) -> int:
        """Get the
        """
    @Font.setter
    def Font(self, value: int) -> None:
        """Set the
        """
    @property
    def FontAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get the
        """
    @FontAngle.setter
    def FontAngle(self, value: NemAll_Python_Geometry.Angle) -> None:
        """Set the
        """
    @property
    def HasTransparentBackground(self) -> bool:
        """check eHasTransparentBackground property flag

        return true if eHasTransparentBackground is set otherwise return false
        """
    @HasTransparentBackground.setter
    def HasTransparentBackground(self, value: bool) -> None:
        """check eHasTransparentBackground property flag

        return true if eHasTransparentBackground is set otherwise return false

        Set eHasTransparentBackground flag
        """
    @property
    def Height(self) -> float:
        """Get the
        """
    @Height.setter
    def Height(self, value: float) -> None:
        """Set the
        """
    @property
    def MarkNumberBorderColor(self) -> int:
        """Get the mark number border color
        """
    @MarkNumberBorderColor.setter
    def MarkNumberBorderColor(self, markNumberBorderColor: int) -> None:
        """Set the mark number border color

        Args:
            markNumberBorderColor: Mark number border color
        """
    @property
    def MarkNumberBorderColorFromElement(self) -> int:
        """Get the mark number border color from the element
        """
    @MarkNumberBorderColorFromElement.setter
    def MarkNumberBorderColorFromElement(self, markNumberBorderColorFromElement: int) -> None:
        """Set the mark number border color from the element

        Args:
            markNumberBorderColorFromElement: Mark number border color from the element
        """
    @property
    def MarkNumberBorderPen(self) -> int:
        """Get the mark number border pen
        """
    @MarkNumberBorderPen.setter
    def MarkNumberBorderPen(self, markNumberBorderPen: int) -> None:
        """Set the mark number border pen

        Args:
            markNumberBorderPen: Mark number border pen
        """
    @property
    def MarkNumberColor(self) -> int:
        """Get the mark number color
        """
    @MarkNumberColor.setter
    def MarkNumberColor(self, markNumberColor: int) -> None:
        """Set the mark number color

        Args:
            markNumberColor: Mark number color
        """
    @property
    def MarkNumberPen(self) -> int:
        """Get the mark number pen
        """
    @MarkNumberPen.setter
    def MarkNumberPen(self, markNumberPen: int) -> None:
        """Set the mark number pen

        Args:
            markNumberPen: Mark number pen
        """
    @property
    def TextAngle(self) -> NemAll_Python_Geometry.Angle:
        """Get the
        """
    @TextAngle.setter
    def TextAngle(self, value: NemAll_Python_Geometry.Angle) -> None:
        """Set the
        """
    @property
    def TextColor(self) -> int:
        """Get the mark text color
        """
    @TextColor.setter
    def TextColor(self, markTextColor: int) -> None:
        """Set the mark text color

        Args:
            markTextColor: Mark text color
        """
    @property
    def TextPen(self) -> int:
        """Get the mark text pen
        """
    @TextPen.setter
    def TextPen(self, markTextPen: int) -> None:
        """Set the mark text pen

        Args:
            markTextPen: Mark text pen
        """
    @property
    def Width(self) -> float:
        """Get the
        """
    @Width.setter
    def Width(self, value: float) -> None:
        """Set the
        """

class ReinforcementService():
    """Reinforcement service
    """
    class BarShapeCodeStandard(enum.Enum):
        """Standard for the bar shape code
        """
        eACI = 4
        eBS = 2
        eIso3766 = 1
        eIso4066 = 0
        eSANS = 3

        names = {eIso4066: eIso4066,
                 eIso3766: eIso3766,
                 eBS: eBS,
                 eSANS: eSANS,
                 eACI: eACI}

        values = {0: eIso4066,
                  1: eIso3766,
                  2: eBS,
                  3: eSANS,
                  4: eACI}

        def __getitem__(self, key: (str | int | float)) -> ReinforcementService.BarShapeCodeStandard:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    @staticmethod
    def GetACIBarMark(barsDefinitionElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, showIndex: bool) -> list:
        """Get the bar mark

        Args:
            barsDefinitionElement:    Bars definition element
            showIndex:                Show the index

        Returns:
             bar mark for ACI
        """
    @staticmethod
    def GetACIPlacementBarMark(barsPlacementElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, showIndex: bool) -> tuple:
        """Get the bar mark for a placement

        Args:
            barsPlacementElement:     Bars placement element
            showIndex:                Show the index

        Returns:
             tuple(bar mark for ACI, bar count)
        """
    @staticmethod
    def GetBarPositionData(elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> list:
        """Get the bar position data

        Args:
            elements:    List with the elements

        Returns:
             List with the bar position data
        """
    @staticmethod
    def GetBarShapeCode(barsDefinitionElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                        barShapeCopdeStandard: BarShapeCodeStandard) -> tuple:
        """Get the bar shape code

        Args:
            barsDefinitionElement:    Bars definition element
            barShapeCopdeStandard:    Standard for the bar shape code

        Returns:
             shape code count, list of (shape codes, bar length), list of (segment name, segment lengths))  for ACI
             shape code count, list of shape codes, list of lengths)  for all other
        """
    eACI = BarShapeCodeStandard.eACI
    eBS = BarShapeCodeStandard.eBS
    eIso3766 = BarShapeCodeStandard.eIso3766
    eIso4066 = BarShapeCodeStandard.eIso4066
    eSANS = BarShapeCodeStandard.eSANS

class ReinforcementSettings():

    """Implementation of Reinforcement settings
    """
    @staticmethod
    def CheckBarDiameter() -> float:
        """Check, whether the diameter is included in the diameter list of the current steel grade

        Returns:
            Bar diameter (original or nearest value)
        """
    @staticmethod
    def CheckMeshGroup() -> int:
        """Check, whether the mesh group is included in the group list

        Returns:
            Mesh group (original or first)
        """
    @staticmethod
    def GetBarDiameter() -> float:
        """Get the current bar diameter

        Returns:
            Bar diameter
        """
    @staticmethod
    def GetBarFactorForDiameter() -> float:
        """Get Factor for Diameter

        Returns:
            Factor for Diameter

        Examples:
            >>> ReinforcementSettings.GetBarFactorForDiameter()
            1.0
        """
    @staticmethod
    def GetBarWeight(steelGrade: int, barDiameter: float) -> float:
        """Get the weight for a bar diameter

        Args:
            steelGrade:     Steel grade
            barDiameter:    Bar diameter

        Returns:
            Weight for a bar diameter
        """
    @staticmethod
    def GetBendingRoller() -> float:
        """Get the current bending roller

        Returns:
            Bending roller
        """
    @staticmethod
    def GetConcreteGrade() -> int:
        """Get the current concrete grade

        Returns:
            Concrete grade
        """
    @staticmethod
    def GetConcreteGradesForNorm(NormID: int) -> list[tuple[int, str]]:
        """Get the concrete grades for norm

        Args:
            NormID:     Norm ID

        Returns:
            List with the concrete grades for Norm as tuple[ID, Name]
        """
    @staticmethod
    def GetEngCatCrossSections() -> list[EngCatCrossSection]:
        """Get the cross sections from engineering catalog

        Returns:
            List with the cross sections
        """
    @staticmethod
    def GetEngCatDiameters(EngCatSteel: EngCatSteel) -> list[EngCatDiameter]:
        """Get the diameters for cross section

        Returns:
            List with the diameters
        """
    @staticmethod
    def GetEngCatMeshGroups() -> list[EngCatMeshGroup]:
        """Get the mesh groups from engineering catalog

        Returns:
            List with the mesh groups
        """
    @staticmethod
    def GetEngCatMeshes(EngCatMeshGroup: EngCatMeshGroup) -> list[EngCatMesh]:
        """Get the meshes for cross section

        Returns:
            List with the concrete cross sections
        """
    @staticmethod
    def GetEngCatSteels() -> list[EngCatSteel]:
        """Get the steels from engineering catalog

        Returns:
            List with the steels
        """
    @staticmethod
    def GetMaxBarLength() -> float:
        """Get the maximal bar length

        Returns:
            Maximal bar length
        """
    @staticmethod
    def GetMeshCutOffPlacementLimit() -> float:
        """Get the limit

        Returns:
            Limit

        Examples:
            >>> ReinforcementSettings.GetMeshCutOffPlacementLimit()
            200.0
        """
    @staticmethod
    def GetMeshGroup() -> int:
        """Get the current mesh group

        Returns:
            Mesh group
        """
    @staticmethod
    def GetMeshType() -> str:
        """Get the current mesh type

        Returns:
            Mesh type
        """
    @staticmethod
    def GetNorm() -> int:
        """Get the current norm

        Returns:
            Norm
        """
    @staticmethod
    def GetNorms() -> list[tuple[int, str]]:
        """Get the Reinforcement norms

        Returns:
            List with the Reinforcement norms as tuple[ID, Name]
        """
    @staticmethod
    def GetSteelGrade() -> int:
        """Get the current steel grade

        Returns:
            Steel grade
        """
    @staticmethod
    def Is3DReinforcement() -> bool:
        """Get the 3D-Reinforcement state

        Returns:
            Create 3D-Reinforcement: true/false
        """
    def __init__(self):
        """Initialize
        """

class ReinforcementShapeBuilder():
    """Implementation of the reinforcement shape builder
    """
    @typing.overload
    def AddPoint(self, pnt: NemAll_Python_Geometry.Point2D, concreteCover: float, bendingRoller: float, zCoordBar: float = 0):
        """Add an end point of a geometry side

        Args:
            pnt:           End point of the side
            concreteCover: Concrete cover
            bendingRoller: Bending roller
            zCoordBar:     Bar coordinate in z direction of the local shape coordinate system
        """
    @typing.overload
    def AddPoint(self, pnt: NemAll_Python_Geometry.Point3D, concreteCover: float, bendingRoller: float):
        """Add an end point of a geometry side

        Args:
            pnt:           End point of the side
            concreteCover: Concrete cover
            bendingRoller: Bending roller
        """
    def AddPoint(self):
        """ Overloaded function. See individual overloads.
        """
    def AddPoints(self, pointList: object):
        """Add the shape geometry points

        Args:
            pointList: Point list
        """
    @typing.overload
    def AddSide(self, startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D, concreteCover: float,
                bendingRoller: float, zCoordBar: float = 0):
        """Add a geometry side of the shape

        Args:
            startPnt:      Start point of the geometry side
            endPnt:        End point of the geometry side
            concreteCover: Concrete cover
            bendingRoller: Bending roller between the last and current side
            zCoordBar:     Bar coordinate in z direction of the local shape coordinate system
        """
    @typing.overload
    def AddSide(self, startPnt: NemAll_Python_Geometry.Point3D, endPnt: NemAll_Python_Geometry.Point3D, concreteCover: float,
                bendingRoller: float):
        """Add a geometry side of the shape

        Args:
            startPnt:      Start point of the geometry side
            endPnt:        End point of the geometry side
            concreteCover: Concrete cover
            bendingRoller: Bending roller between the last and current side
        """
    def AddSide(self):
        """ Overloaded function. See individual overloads.
        """
    def AddSides(self, sideList: object):
        """Add the geometry sides of a shape

        Args:
            sideList: Side list
        """
    @typing.overload
    def CreateShape(self, diameter: float, bendingRoller: float, steelGrade: int, concreteGrade: int,
                    bendingShapeType: BendingShapeType) -> BendingShape:
        """Create the shape

        Args:
            diameter:         Diameter
            bendingRoller:    Default bending roller
            steelGrade:       Steel grade
            concreteGrade:    Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            bendingShapeType: Bending shape type

        Returns:
            Creation successful: true/false
        """
    @typing.overload
    def CreateShape(self, meshType: str, meshBendingDirection: MeshBendingDirection, bendingRoller: float, steelGrade: int,
                    concreteGrade: int, bendingShapeType: BendingShapeType) -> BendingShape:
        """Create the shape

        Args:
            meshType:             Mesh type
            meshBendingDirection: Mesh bending direction
            bendingRoller:        Default bending roller
            steelGrade:           Steel grade
            concreteGrade:        Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            bendingShapeType:     Bending shape type

        Returns:
            Creation successful: true/false
        """
    @typing.overload
    def CreateShape(self, shapeProps: object) -> BendingShape:
        """Create the shape

        Args:
            shapeProps: Shape properties

        Returns:
            Creation successful: true/false
        """
    def CreateShape(self) -> BendingShape:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def CreateStirrup(self, diameter: float, bendingRoller: float, steelGrade: int, concreteGrade: int,
                      stirrupType: StirrupType) -> BendingShape:
        """Create the stirrup shape

        Args:
            diameter:      Diameter
            bendingRoller: Default bending roller
            steelGrade:    Steel grade
            concreteGrade: Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            stirrupType:   Type of the stirrup

        Returns:
            Creation successful: true/false
        """
    @typing.overload
    def CreateStirrup(self, meshType: str, meshBendingDirection: MeshBendingDirection, bendingRoller: float, steelGrade: int,
                      concreteGrade: int, stirrupType: StirrupType) -> BendingShape:
        """Create the stirrup shape

        Args:
            meshType:             Mesh type
            meshBendingDirection: Mesh bending direction
            bendingRoller:        Default bending roller
            steelGrade:           Steel grade
            concreteGrade:        Concrete grade (index of the global list starting from 0, -1 = use global value from the Allplan settings)
            stirrupType:          Type of the stirrup

        Returns:
            Creation successful: true/false
        """
    @typing.overload
    def CreateStirrup(self, shapeProps: object, stirrupType: StirrupType) -> BendingShape:
        """Create the stirrup shape

        Args:
            shapeProps:  Shape properties
            stirrupType: Type of the stirrup

        Returns:
            Creation successful: true/false
        """
    def CreateStirrup(self) -> BendingShape:
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def GetMeshData(meshType: str) -> MeshData:
        """Get the mesh data

        Args:
            meshType: Mesh type

        Returns:
            Mesh data
        """
    def SetAnchorageHookEnd(self, angle: float):
        """Set an anchorage hook at the end of the shape

        Args:
            angle: Hook angle
        """
    def SetAnchorageHookEndFromSide(self):
        """Set an anchorage hook at the end of the shape, get the angle from the side
        """
    def SetAnchorageHookStart(self, angle: float):
        """Set an anchorage hook at the start of the shape

        Args:
            angle: Hook angle
        """
    def SetAnchorageHookStartFromSide(self):
        """Set an anchorage hook at the start of the shape, get the angle from the side
        """
    def SetAnchorageLengthEnd(self, anchorageLength: float):
        """Set the anchorage length at the end of the shape

        Args:
            anchorageLength: Anchorage length at the end of the shape
        """
    def SetAnchorageLengthStart(self, anchorageLength: float):
        """Set the anchorage length at the start of the shape

        Args:
            anchorageLength: Anchorage length at the start of the shape
        """
    def SetConcreteCoverEnd(self, concreteCover: float):
        """Set the concrete cover at the end of the shape

        Args:
            concreteCover: Concrete cover
        """
    @typing.overload
    def SetConcreteCoverLineEnd(self, startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D,
                                concreteCover: float):
        """Set the concrete cover line at the end of the shape

        Args:
            startPnt:      Start point of the concrete cover line at the end of the shape
            endPnt:        Endpoint of the concrete cover line at the end of the shape
            concreteCover: Concrete cover
        """
    @typing.overload
    def SetConcreteCoverLineEnd(self, startPnt: NemAll_Python_Geometry.Point3D, endPnt: NemAll_Python_Geometry.Point3D,
                                concreteCover: float):
        """Set the concrete cover line at the end of the shape

        Args:
            startPnt:      Start point of the concrete cover line at the end of the shape
            endPnt:        Endpoint of the concrete cover line at the end of the shape
            concreteCover: Concrete cover
        """
    def SetConcreteCoverLineEnd(self):
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def SetConcreteCoverLineStart(self, startPnt: NemAll_Python_Geometry.Point2D, endPnt: NemAll_Python_Geometry.Point2D,
                                  concreteCover: float):
        """Set the concrete cover line at the start of the shape

        Args:
            startPnt:      Start point of the concrete cover line at the start of the shape
            endPnt:        Endpoint of the concrete cover line at the start of the shape
            concreteCover: Concrete cover
        """
    @typing.overload
    def SetConcreteCoverLineStart(self, startPnt: NemAll_Python_Geometry.Point3D, endPnt: NemAll_Python_Geometry.Point3D,
                                  concreteCover: float):
        """Set the concrete cover line at the start of the shape

        Args:
            startPnt:      Start point of the concrete cover line at the start of the shape
            endPnt:        Endpoint of the concrete cover line at the start of the shape
            concreteCover: Concrete cover
        """
    def SetConcreteCoverLineStart(self):
        """ Overloaded function. See individual overloads.
        """
    def SetConcreteCoverStart(self, concreteCover: float):
        """Set the concrete cover at the start of the shape

        Args:
            concreteCover: Concrete cover
        """
    def SetFullCircleOverlap(self, fullCircleOverlap: float):
        """Set the overlap length for the full circle stirrup

        Args:
            fullCircleOverlap: Overlap length
        """
    def SetHookEnd(self, length: float, angle: float, type: HookType):
        """Set the hook at the end of the shape

        Args:
            length: Hook length (0 = calculate)
            angle:  Hook angle
            type:   Hook type
        """
    def SetHookStart(self, length: float, angle: float, type: HookType):
        """Set the hook at the start of the shape

        Args:
            length: Hook length (0 = calculate)
            angle:  Hook angle
            type:   Hook type
        """
    def SetOverlapLengthEnd(self):
        """Set an overlap length a the end of the shape
        """
    def SetOverlapLengthStart(self):
        """Set an overlap length a the start of the shape
        """
    def SetSideLengthEnd(self, sideLength: float):
        """Set the side length at the end of the shape

        Args:
            sideLength: Side length
        """
    def SetSideLengthStart(self, sideLength: float):
        """Set the side length at the start of the shape

        Args:
            sideLength: Side length
        """
    @typing.overload
    def SetStartPoint(self, startPnt: NemAll_Python_Geometry.Point2D):
        """Set a start point of a geometry side

        Args:
            startPnt: Start point
        """
    @typing.overload
    def SetStartPoint(self, startPnt: NemAll_Python_Geometry.Point3D):
        """Set a start point of a geometry side

        Args:
            startPnt: Start point
        """
    def SetStartPoint(self):
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, shapePlaneMatrix: NemAll_Python_Geometry.Matrix3D):
        """Constructor

        Args:
            shapePlaneMatrix: Matrix of the plane for the real shape calculation
        """
    @typing.overload
    def __init__(self, shapePlaneMatrix: NemAll_Python_Geometry.Matrix3D, create3DShape: bool, localZCoverFront: float,
                 localZCoverBack: float):
        """Constructor

        Args:
            shapePlaneMatrix: Matrix of the plane for the real shape calculation
            create3DShape:    Create a 3D shape
            localZCoverFront: Concrete cover in the front of the local z direction of the shape (needed for 3D shape)
            localZCoverBack:  Concrete cover in the back of the local z direction of the shape (needed for 3D shape)
        """
    @typing.overload
    def __init__(self, element: ReinforcementShapeBuilder):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class ReinforcementType(enum.Enum):
    """Definition of the reinforcement types

    Bar :
    Mesh:
    """
    Bar = 0
    Mesh = 1

    names = {Bar: Bar,
             Mesh: Mesh}

    values = {0: Bar,
              1: Mesh}

    def __getitem__(self, key: (str | int | float)) -> ReinforcementType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ReinforcementUtil():

    @staticmethod
    def GetNextBarPositionNumber(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> int:
        """Get the the next bar position number

        Returns:
             Next bar position number
            r: doc              Document
        """
    @staticmethod
    def GetNextMeshPositionNumber(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> int:
        """Get the the next mesh position number

        Returns:
             Next mesh position number
            r: doc              Document
        """
    @staticmethod
    def MergeIdenticalMarks(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                            elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, tolerance: float = 1.0, rearrangedLock: bool = False, identicalShapes: bool = False, identicalPrefix: bool = False) -> int:
        """Rearrange some bar marks only

        Args:
            doc:              Document
            elements:         List of elements to rearrange
            tolerance:        Tolerance
            rearrangedLock:   Rearranged positions are locked state
            identicalShapes:  Rearrange identical shapes state
            identicalPrefix:  Rearrange identical prefix state
        """
    @staticmethod
    def Rearrange(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fromBarPosition: int = 1, fromMeshPosition: int = 1,
                  toBarPosition: int = 99999, toMeshPosition: int = 99999, afterBarPosition: int = 1, aftgerMeshPosition: int = 1, tolerance: float = 1.0, rearrangedLock: bool = False, identicalShapes: bool = False, identicalPrefix: bool = False, createUndoStep: bool = True):
        """Rearrange the reinforcement

        Args:
            doc:              Document
            fromBarPosition:  Rearrange from bar position
            fromMeshPosition: Rearrange from mesh position
            toBarPosition:    Rearrange to bar position
            toMeshPosition:   Rearrange to mesh position
            afterBarPosition: Rearrange after bar position
            afterMeshPosition:Rearrange after mesh position
            tolerance:        Tolerance
            rearrangedLock:   Rearranged positions are locked state
            identicalShapes:  Rearrange identical shapes state
            identicalPrefix:  Rearrange identical prefix state
            createUndoStep:   Create the undo step state
        """
    def __init__(self):
        """Initialize
        """

class SchemaMirror(enum.Enum):
    """Definition of the schema mirroring states

    eNo    : Mirror no
    eXAxis : Mirror around the X axis
    eYAxis : Mirror around the Y axis
    eXYAxis: Mirror around the X and Y axis
    """
    eNo = 0
    eXAxis = 7
    eXYAxis = -5
    eYAxis = 2

    names = {eNo: eNo,
             eXAxis: eXAxis,
             eYAxis: eYAxis,
             eXYAxis: eXYAxis}

    values = {0: eNo,
              7: eXAxis,
              2: eYAxis,
              -5: eXYAxis}

    def __getitem__(self, key: (str | int | float)) -> SchemaMirror:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SchemaStirrupUnfold(enum.Enum):
    """Definition of the schema stirrup unfold

    eNo              : No unfold
    eFirstSegment    : First segment unfold
    eFirstLastSegment: First and last segment unfold
    eLastSegment     : Last segment unfold
    """
    eFirstLastSegment = 3
    eFirstSegment = 2
    eLastSegment = 4
    eNo = 1

    names = {eNo: eNo,
             eFirstSegment: eFirstSegment,
             eFirstLastSegment: eFirstLastSegment,
             eLastSegment: eLastSegment}

    values = {1: eNo,
              2: eFirstSegment,
              3: eFirstLastSegment,
              4: eLastSegment}

    def __getitem__(self, key: (str | int | float)) -> SchemaStirrupUnfold:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SpiralElement(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the bar placement element
    """
    def GetLengthSections(self) -> NemAll_Python_Utility.VecDoubleList:
        """Get the length for the sections

        Returns:
            Length for the sections
        """
    def GetPitchSections(self) -> NemAll_Python_Utility.VecDoubleList:
        """Get the pitch for the sections

        Returns:
            Pitch for the sections
        """
    def SetLengthFactor(self, lengthFactor: float):
        """Set the length factor

        Args:
            lengthFactor: Length factor
        """
    def SetNumberLoopsEnd(self, numberLoopsEnd: int):
        """Set the loops at the end

        Args:
            numberLoopsEnd
        """
    def SetNumberLoopsStart(self, numberLoopsStart: int):
        """Set the loops at the start

        Args:
            numberLoopsStart
        """
    def SetPitchSections(self, pitch1: float, length1: float, pitch2: float, length2: float, pitch3: float, length3: float, pitch4: float,
                         length4: float):
        """Set the pitch section

        Args:
            pitch1:  Pitch section 1
            length1: Length section 1
            pitch2:  Pitch section 2
            length2: Length section 2
            pitch3:  Pitch section 3
            length3: Length section 3
            pitch4:  Pitch section 4
            length4: Length section 4
        """
    def SetPlacePerLinearMeter(self, bPlacePerLinearMeter: bool):
        """Set the place per linear meter state

        Args:
            bPlacePerLinearMeter: Place per linear meter: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, positionNumber: int, diameter: float, steelGrade: int, concreteGrade: int,
                 rotationAxis: NemAll_Python_Geometry.Line3D, contourPoints: NemAll_Python_Geometry.Polyline3D, pitch: float, hookLengthStart: float, hookAngleStart: float, hookLengthEnd: float, hookAngleEnd: float, concreteCoverStart: float, concreteCoverEnd: float, concreteCoverContour: float):
        """Constructor

        Args:
            positionNumber:       Position number
            diameter:             Diameter
            steelGrade:           Steel grade
            concreteGrade:        Concrete grade
            rotationAxis:         Rotation axis
            contourPoints:        Contour points
            pitch:                Pitch
            hookLengthStart:      Hook length at the start
            hookAngleStart:       Hook angle at the start
            hookLengthEnd:        Hook length at the end
            hookAngleEnd:         Hook angle at the end
            concreteCoverStart:   Concrete cover at the start
            concreteCoverEnd:     Concrete cover at the end
            concreteCoverContour: Concrete cover of the contour
        """
    @typing.overload
    def __init__(self, param: SpiralElement):
        """Args:
            param
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def ConcreteCoverContour(self) -> float:
        """Get the concrete cover from the contour
        """
    @ConcreteCoverContour.setter
    def ConcreteCoverContour(self, concreteCoverContour: float) -> None:
        """Set the concrete cover from the contour

        Args:
            concreteCoverContour: Concrete cover from the contour
        """
    @property
    def ConcreteCoverEnd(self) -> float:
        """Get the concrete cover from the end
        """
    @ConcreteCoverEnd.setter
    def ConcreteCoverEnd(self, concreteCoverEnd: float) -> None:
        """Set the concrete cover from the end

        Args:
            concreteCoverEnd: Concrete cover from the end
        """
    @property
    def ConcreteCoverStart(self) -> float:
        """Get the concrete cover from the start
        """
    @ConcreteCoverStart.setter
    def ConcreteCoverStart(self, concreteCoverStart: float) -> None:
        """Set the concrete cover from the start

        Args:
            concreteCoverStart: Concrete cover from the start
        """
    @property
    def ContourPoints(self) -> NemAll_Python_Geometry.Polyline3D:
        """Get the contour points
        """
    @ContourPoints.setter
    def ContourPoints(self, contourPoints: NemAll_Python_Geometry.Polyline3D) -> None:
        """Set the contour points

        Args:
            contourPoints: Contour points
        """
    @property
    def Diameter(self) -> float:
        """Get the diameter
        """
    @Diameter.setter
    def Diameter(self, diameter: float) -> None:
        """Set the diameter

        Args:
            diameter: Diameter
        """
    @property
    def HookAngleEnd(self) -> float:
        """Get the hook angle at the end
        """
    @HookAngleEnd.setter
    def HookAngleEnd(self, hookAngleEnd: float) -> None:
        """Set the hook angle end

        Args:
            hookAngleEnd: Hook angle end
        """
    @property
    def HookAngleStart(self) -> float:
        """Get the hook angle at the start
        """
    @HookAngleStart.setter
    def HookAngleStart(self, hookAngleStart: float) -> None:
        """Set the hook angle start

        Args:
            hookAngleStart: Hook angle start
        """
    @property
    def HookLengthEnd(self) -> float:
        """Get the hook length at the end
        """
    @HookLengthEnd.setter
    def HookLengthEnd(self, hookLengthEnd: float) -> None:
        """Set the hook length end

        Args:
            hookLengthEnd: Hook length end
        """
    @property
    def HookLengthStart(self) -> float:
        """Get the hook length at the start
        """
    @HookLengthStart.setter
    def HookLengthStart(self, hookLengthStart: float) -> None:
        """Set the hook length start

        Args:
            hookLengthStart: Hook length start
        """
    @property
    def LengthFactor(self) -> float:
        """Get the length factor
        """
    @LengthFactor.setter
    def LengthFactor(self, lengthFactor: float) -> None:
        """Set the length factor

        Args:
            lengthFactor: Length factor
        """
    @property
    def NumberLoopsEnd(self) -> int:
        """Get the loops at the end
        """
    @NumberLoopsEnd.setter
    def NumberLoopsEnd(self, value: int) -> None:
        """Set the loops at the end
        """
    @property
    def NumberLoopsStart(self) -> int:
        """Get the loops at the start
        """
    @NumberLoopsStart.setter
    def NumberLoopsStart(self, value: int) -> None:
        """Set the loops at the start
        """
    @property
    def Pitch(self) -> float:
        """Get the pitch
        """
    @Pitch.setter
    def Pitch(self, pitch: float) -> None:
        """Set the pitch

        Args:
            pitch: Pitch
        """
    @property
    def PlacePerLinearMeter(self) -> bool:
        """Get the place per linear meter state
        """
    @PlacePerLinearMeter.setter
    def PlacePerLinearMeter(self, bPlacePerLinearMeter: bool) -> None:
        """Set the place per linear meter state

        Args:
            bPlacePerLinearMeter: Place per linear meter: true/false
        """
    @property
    def RotationAxis(self) -> NemAll_Python_Geometry.Line3D:
        """Get the rotation axis
        """
    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: NemAll_Python_Geometry.Line3D) -> None:
        """Set the rotation axis

        Args:
            rotationAxis: Rotation axis
        """
    @property
    def SteelGrade(self) -> int:
        """Get the steel grade
        """
    @SteelGrade.setter
    def SteelGrade(self, steelGrade: int) -> None:
        """Set the steel grade

        Args:
            steelGrade: SteelGrade
        """

class StirrupType(enum.Enum):
    """Types of the stirrups
    """
    Column = 3
    Diamond = 4
    FullCircle = 5
    Normal = 1
    Torsion = 2

    names = {Normal: Normal,
             Torsion: Torsion,
             Column: Column,
             Diamond: Diamond,
             FullCircle: FullCircle}

    values = {1: Normal,
              2: Torsion,
              3: Column,
              4: Diamond,
              5: FullCircle}

    def __getitem__(self, key: (str | int | float)) -> StirrupType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SweepBarPlacement(ReinfElement, NemAll_Python_BasisElements.AllplanElement):
    """Implementation of the sweep bar placement element
    """
    class eEdgeOffsetType(enum.Enum):
        """Edge offset types
        """
        eMajorValueAtEnd = 3
        eMajorValueAtStart = 1
        eStartEqualEnd = 2
        eZeroAtEnd = 4
        eZeroAtStart = 0

        names = {eZeroAtStart: eZeroAtStart,
                 eMajorValueAtStart: eMajorValueAtStart,
                 eStartEqualEnd: eStartEqualEnd,
                 eMajorValueAtEnd: eMajorValueAtEnd,
                 eZeroAtEnd: eZeroAtEnd}

        values = {0: eZeroAtStart,
                  1: eMajorValueAtStart,
                  2: eStartEqualEnd,
                  3: eMajorValueAtEnd,
                  4: eZeroAtEnd}

        def __getitem__(self, key: (str | int | float)) -> SweepBarPlacement.eEdgeOffsetType:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def AddPlacementSection(self, placementSection: BarPlacementSection) -> bool:
        """Add a placement section

        Args:
            placementSection: Section

        Returns:
            Section is added: true/false
        """
    def AddSectionBars(self, bendingShapes: BendingShapeList, sectionsLongitudinalBarsProp: LongitudinalBarPropertiesList,
                       sectionPlane: NemAll_Python_Geometry.Plane3D):
        """Add the bars and the section plane for a section

        bendingShapeViewVector  View vector of the bending shape

        Args:
            bendingShapes:                Bending shapes of the section
            sectionsLongitudinalBarsProp: Longitudinal bars properties
            sectionPlane:                 Section plane
        """
    def GetBarOffset(self) -> float:
        """Get the bar offset

        Returns:
            Bar offset
        """
    def GetBenchingAngle(self) -> float:
        """Get the benching angle

        Returns:
            Benching angle
        """
    def GetBenchingLength(self) -> float:
        """Get the benching length

        Returns:
            Benching length
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetConcreteCoverEnd(self) -> float:
        """Get the concrete cover at the end of the path

        Returns:
            Concrete cover at the end of the path
        """
    def GetConcreteCoverStart(self) -> float:
        """Get the concrete cover at the start of the path

        Returns:
            Concrete cover at the start of the path
        """
    def GetCrossBarDistance(self) -> float:
        """Get the cross bar distance

        Returns:
            Cross bar distance
        """
    def GetEdgeOffsetEnd(self) -> float:
        """Get the edge offset at the end of the path

        Returns:
            Edge offset at the end of the path
        """
    def GetEdgeOffsetStart(self) -> float:
        """Get the edge offset at the start of the path

        Returns:
            Edge offset at the start of the path
        """
    def GetEdgeOffsetType(self) -> eEdgeOffsetType:
        """Get the edge offset type

        Returns:
            Edge offset type
        """
    def GetEdgeOffsets(self) -> tuple:
        """Get the edge offsets

        Returns:
            Edge offsets
        """
    def GetPlacementSections(self) -> object:
        """Get the placement sections

        Returns:
            Placement sections
        """
    def GetPositionNumber(self) -> int:
        """Get the position number

        Returns:
            Position number
        """
    def IsFirstPathIsSweepPath(self) -> bool:
        """Get the first path is sweep path state

        Returns:
            First path is sweep path state
        """
    def IsInterpolation(self) -> bool:
        """Get the interpolation state

        Returns:
            Interpolation state
        """
    def IsInterpolationOfAllPoints(self) -> bool:
        """Get the interpolation of all points state

        Returns:
            Interpolation of all points state
        """
    def IsRoation(self) -> bool:
        """Get the rotation state

        Returns:
            Rotation state
        """
    def Move(self, transVec: NemAll_Python_Geometry.Vector3D):
        """Move the placement

        Args:
            transVec: Move vector
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetPositionNumber(self, positionNumber: int):
        """Set the position number

        Args:
            positionNumber: Position number
        """
    def Sweep(self):
        """Sweep the bars
        """
    def Transform(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Transform the placement

        Args:
            transMat: Transformation matrix
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, placement: SweepBarPlacement):
        """Copy constructor

        Args:
            placement: Placement to copy
        """
    @typing.overload
    def __init__(self, positionNumber: int, sweepPaths: NemAll_Python_Geometry.Path3DList, rotation: bool, firstPathIsSweepPath: bool,
                 interpolation: bool, interpolationOfAllPoints: bool, crossBarDistance: float, concreteCoverStart: float, concreteCoverEnd: float, edgeOffsetType: eEdgeOffsetType, edgeOffsetStart: float, edgeOffsetEnd: float, barOffset: float, benchingLength: float, benchingAngle: float):
        """Constructor for cross bars

        Args:
            positionNumber:           Position number
            sweepPaths:               Path
            rotation:                 Rotation
            firstPathIsSweepPath:     First path is also sweep path
            interpolation:            Interpolation
            interpolationOfAllPoints: Interpolation of all points
            crossBarDistance:         Cross bar distance
            concreteCoverStart:       Concrete cover at the start of the path
            concreteCoverEnd:         Concrete cover at the end of the path
            edgeOffsetType:           Get the edge offset type of the path
            edgeOffsetStart:          Edge offset at the start of the path
            edgeOffsetEnd:            Edge offset at the end of the path
            barOffset:                Bar offset
            benchingLength:           Benching length
            benchingAngle:            Benching angle
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def CommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties
        """
    @CommonProperties.setter
    def CommonProperties(self, value: NemAll_Python_BaseElements.CommonProperties) -> None:
        """Set the common properties
        """
    @property
    def PositionNumber(self) -> int:
        """Get the position number
        """
    @PositionNumber.setter
    def PositionNumber(self, value: int) -> None:
        """Set the position number
        """
    eMajorValueAtEnd = eEdgeOffsetType.eMajorValueAtEnd
    eMajorValueAtStart = eEdgeOffsetType.eMajorValueAtStart
    eStartEqualEnd = eEdgeOffsetType.eStartEqualEnd
    eZeroAtEnd = eEdgeOffsetType.eZeroAtEnd
    eZeroAtStart = eEdgeOffsetType.eZeroAtStart

def CreateReinforcementLabeling(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, insertionMat: NemAll_Python_Geometry.Matrix3D,
                                modelEleList: list, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, undoRedoService: (object | None) = None):
    """Create the reinforcement labels

    Args:
        doc:            Document
        insertionMat:   Insertion matrix
        modelEleList:   List with the model elements
        viewProj:       View projection
        undoRedoService:Undo redo service
    """
def InitApplicationtest() -> NemAll_Python_IFW_ElementAdapter.DocumentAdapter:
    """
    """
def InitUnitTest():
    """
    """
def UninitUnitTest():
    """
    """

```