---
title: "NemAll_Python_BasisElements"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_BasisElements.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_BasisElements

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_BasisElements.pyi`  
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

"""Exposed classes and functions from NemAll_Python_BasisElements"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_Geometry
import NemAll_Python_BaseElements
import NemAll_Python_IFW_ElementAdapter
import NemAll_Python_IFW_Input
import NemAll_Python_Utility


__all__ = [
    "ARGB",
    "AllplanElement",
    "AssociativeViewAllElements",
    "AssociativeViewConcreteShape",
    "AssociativeViewElement",
    "AssociativeViewElementRepresentation",
    "AssociativeViewProperties",
    "AttributeContainer",
    "BasisElement",
    "BasisPropertyDialogs",
    "BitmapAreaElement",
    "BitmapAreaProperties",
    "BitmapDefinition",
    "ClippingPathProperties",
    "CombinationType",
    "ConsiderType",
    "DimensionLineElement",
    "DimensionProperties",
    "DimensionSegmentProperties",
    "DimensionSegmentPropertiesList",
    "Dimensioning",
    "ElementGroupElement",
    "ElementGroupProperties",
    "ElementNodeElement",
    "ElevationElement",
    "EndSymbolsProperties",
    "FaceStyleElement",
    "FaceStyleProperties",
    "FillingElement",
    "FillingProperties",
    "HatchingElement",
    "HatchingProperties",
    "HeightDefinitionType",
    "HiddenSectionLinesProperties",
    "LabelElement",
    "LabelType",
    "LabelingProperties",
    "LibraryElement",
    "LibraryElementProperties",
    "LibraryElementType",
    "LightProperties",
    "LinkType",
    "MacroElement",
    "MacroGroupElement",
    "MacroGroupProperties",
    "MacroPlacementElement",
    "MacroPlacementProperties",
    "MacroProperties",
    "MacroSlideElement",
    "MacroSlideProperties",
    "MacroSlideType",
    "ModelElement2D",
    "ModelElement3D",
    "PYTHON_PART_DOMAIN_TYPE",
    "PYTHON_PART_SUB_TYPE",
    "PatternCurveAlignment",
    "PatternCurveIntersectionType",
    "PatternCurveProperties",
    "PatternElement",
    "PatternProperties",
    "PlacementType",
    "ScaleProperties",
    "SectionAlongPathClippingPathProperties",
    "SectionAlongPathClippingPathViewProperties",
    "SectionAlongPathElement",
    "SectionAlongPathElevationSpecifications",
    "SectionAlongPathFilterProperties",
    "SectionAlongPathFormatProperties",
    "SectionAlongPathGeneralSectionProperties",
    "SectionAlongPathLabelingStripSetting",
    "SectionAlongPathProperties",
    "SectionAlongPathScaleProperties",
    "SectionAlongPathSectionLabelingProperties",
    "SectionAlongPathSectionViewProperties",
    "SectionAlongPathTextParameterProperties",
    "SectionDefinitionData",
    "SectionDefinitionProperties",
    "SectionDrawingFilesProperties",
    "SectionFilterProperties",
    "SectionFormatProperties",
    "SectionGeneralProperties",
    "SectionLayerProperties",
    "ShadingType",
    "SubType",
    "SurfaceDefinition",
    "Symbol2DElement",
    "Symbol2DProperties",
    "Symbol3DElement",
    "Symbol3DProperties",
    "TextAlignment",
    "TextElement",
    "TextElementList",
    "TextLocation",
    "TextProperties",
    "TextType",
    "TextureDefinition",
    "TextureMapping",
    "TextureMappingType",
    "TransitionType",
    "VariantType",
    "ViewSectionElement",
    "VisibleHiddenEdgesProperties",
    "eAverage",
    "eCenter",
    "eCode",
    "eComponent",
    "eConsiderAutomatic",
    "eConsiderCeilingOpening",
    "eConsiderCeilingRecess",
    "eConsiderCeilingSurface",
    "eConsiderDoorOpening",
    "eConsiderFloorSurface",
    "eConsiderNiche",
    "eConsiderNothing",
    "eConsiderRecess",
    "eConsiderWindowOpening",
    "eDisabled",
    "eExtension",
    "eFitting",
    "eFixture",
    "eFixtureSingleFile",
    "eFormularText",
    "eGeometry",
    "eInsideFitting",
    "eJoint",
    "eLabelArchDimensionLine",
    "eLabelBftSlabElementation",
    "eLabelBftWallElementation",
    "eLabelEng3DBarReinforcement",
    "eLabelNoText",
    "eLabelNormalText",
    "eLabelVariableText",
    "eLeft",
    "eLeftBottom",
    "eLeftMiddle",
    "eLeftTop",
    "eLinkNothing",
    "eLinkToCeilingSurface",
    "eLinkToFloorSurface",
    "eLinkToRoofSlab",
    "eLinkToRoom",
    "eMacro",
    "eMiddleBottom",
    "eMiddleMiddle",
    "eMiddleTop",
    "eMiter",
    "eMultiLine3D",
    "eMultiLine3D_Group",
    "eNone",
    "eNormalText",
    "eOutsideFitting",
    "eReinforcement",
    "eReport",
    "eRight",
    "eRightBottom",
    "eRightMiddle",
    "eRightTop",
    "eSeamless",
    "eSmartSymbol",
    "eSymbol",
    "eUndergroundCadaster",
    "eUseNoSpecialSubType",
    "eVariableText",
    "eVx",
    "eVy",
    "eVz"
]


class ARGB():
    """Represents true color with transparency
    """
    def GetARGB(self) -> int:
        """returns color as unsigned long

        Returns:
            color as long
        """
    def __eq__(self, argb: ARGB) -> bool:
        """equal operator

        Args:
            argb: color to compare

        Returns:
            true if they are equal
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, argb: int):
        """constructor from unsigned long

        Args:
            argb: windows argb value
        """
    @typing.overload
    def __init__(self, red: int, green: int, blue: int, alpha: int):
        """constructor with RGBA components

        Args:
            red:   red component
            green: green component
            blue:  blue component
            alpha: alpha component
        """
    @typing.overload
    def __init__(self, argb: ARGB):
        """copy constructor

        Args:
            argb: copy from
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def ABGR(self) -> int:
        """returns color as ABGR

        sets color from unsigned long ABGR value
        """
    @ABGR.setter
    def ABGR(self, abgr: int) -> None:
        """returns color as ABGR

        sets color from unsigned long ABGR value

        Args:
            abgr: ABGR color
        """
    @property
    def ARGB(self) -> int:
        """returns color as unsigned long

        sets color from ARGB
        """
    @ARGB.setter
    def ARGB(self, argb: int) -> None:
        """returns color as unsigned long

        sets color from ARGB

        Args:
            argb: ARGB color
        """
    @property
    def Alpha(self) -> int:
        """returns alpha component
        """
    @Alpha.setter
    def Alpha(self, alpha: int) -> None:
        """returns alpha component

        set alpha component

        Args:
            alpha: alpha component
        """
    @property
    def BGR(self) -> int:
        """returns color as BGR

        sets only RGB values from unsigned long BGR format
        """
    @BGR.setter
    def BGR(self, bgr: int) -> None:
        """returns color as BGR

        sets only RGB values from unsigned long BGR format

        Args:
            bgr: BGR color
        """
    @property
    def Blue(self) -> int:
        """returns blue component
        """
    @Blue.setter
    def Blue(self, blue: int) -> None:
        """returns blue component

        set blue component

        Args:
            blue: blue component
        """
    @property
    def Green(self) -> int:
        """returns green component
        """
    @Green.setter
    def Green(self, green: int) -> None:
        """returns green component

        set green component

        Args:
            green: green component
        """
    @property
    def IRGB(self) -> int:
        """Get the indexed rgb color representation of the ARGB color

        If color not found in the index table, the rgb color converted to integer value is returned
        """
    @IRGB.setter
    def IRGB(self, irgb: int) -> None:
        """Set the ARGB color from an indexed rgb color
        If color not found in the index table, the rgb color converted to integer value is returned

        Args:
            irgb: Indexed rgb color
        """
    @property
    def Red(self) -> int:
        """returns red component
        """
    @Red.setter
    def Red(self, red: int) -> None:
        """returns red component

        set red component

        Args:
            red: red component
        """

class AllplanElement():
    """Implementation of the Allplan element
    """
    def GetAttributes(self) -> object:
        """Get the attributes object

        Returns:
            Attributes object
        """
    def GetBaseElementAdapter(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Get the model element

        Returns:
            Model element
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties

        Returns:
            Common properties
        """
    def GetGeometryObject(self) -> object:
        """Get the geometry object

        Returns:
            Geometry object
        """
    def GetLabelElements(self) -> list:
        """Get the label elements

        Returns:
            LabelElements
        """
    def GetSubElementID(self) -> type:
        """Get the SubElementID

        Returns:
            SubElementID
        """
    def SetAttributes(self, attributeContainer: object):
        """Set the attributes object

        Args:
            attributeContainer: Attributes object
        """
    def SetBaseElementAdapter(self, ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Sel the model element

        Args:
            ele: Model element
        """
    def SetCommonProperties(self, commonProp: NemAll_Python_BaseElements.CommonProperties):
        """Set the common properties

        Args:
            commonProp: Common properties
        """
    def SetDockingPointsKey(self, dockingPointsKey: str):
        """Set the docking points key

        Args:
            dockingPointsKey: Docking points key
        """
    def SetGeometryObject(self, geoObject: object):
        """Set the geometry object

        Args:
            geoObject: Geometry object
        """
    def SetLabelElements(self, labelElements: list):
        """Set the label elements

        Args:
            labelElements: Label elements
        """
    @property
    def Attributes(self) -> object:
        """Get the attributes object
        """
    @Attributes.setter
    def Attributes(self, attributeContainer: object) -> None:
        """Set the attributes object

        Args:
            attributeContainer: Attributes object
        """
    @property
    def BaseElementAdapter(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Get the model element

        Sel the model element
        """
    @BaseElementAdapter.setter
    def BaseElementAdapter(self, ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> None:
        """Sel the model element

        Args:
            ele: Model element
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
    def GeometryObject(self) -> object:
        """Get the geometry object
        """
    @GeometryObject.setter
    def GeometryObject(self, geoObject: object) -> None:
        """Set the geometry object

        Args:
            geoObject: Geometry object
        """
    @property
    def LabelElements(self) -> list:
        """Get the label elements
        """
    @LabelElements.setter
    def LabelElements(self, labelElements: list) -> None:
        """Set the label elements

        Args:
            labelElements: Label elements
        """

class AssociativeViewElement(AllplanElement):
    """Representation of the associative views and sections

    **WARNING!!**: Associative views and sections are deprecated and not supported in
    Allplan >=2023! Use UVSs instead (represented by _ViewSectionElement_ class)

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
    def ClippingPathProperties(self) -> None:
        """Property for the clipping path properties

        :type: None
        """
    @property
    def DimensionElements(self) -> None:
        """Property for the dimension elements

        :type: None
        """
    @property
    def PlacementAngle(self) -> None:
        """Property for the placement angle

        :type: None
        """
    @property
    def PlacementPoint(self) -> None:
        """Property for the placement point

        :type: None
        """
    @property
    def ReinforcementLabels(self) -> None:
        """Property for the reinforcement labels

        :type: None
        """
    @property
    def SectionAngle(self) -> None:
        """Property for the section angle

        :type: None
        """
    @property
    def SectionPolyhedron(self) -> None:
        """Property for the section polyhedron

        :type: None
        """
    @property
    def TextElements(self) -> None:
        """Property for the text elements

        :type: None
        """
    @property
    def ViewMatrix(self) -> None:
        """Property for the view matrix

        :type: None
        """
    @property
    def ViewProperties(self) -> None:
        """Property for the view properties

        :type: None
        """

class AssociativeViewElementRepresentation(enum.Enum):
    """Element representation of the associative view
    """
    AssociativeViewAllElements = 0
    AssociativeViewConcreteShape = 3

    names = {AssociativeViewAllElements: AssociativeViewAllElements,
             AssociativeViewConcreteShape: AssociativeViewConcreteShape}

    values = {0: AssociativeViewAllElements,
              3: AssociativeViewConcreteShape}

    def __getitem__(self, key: (str | int | float)) -> AssociativeViewElementRepresentation:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class AssociativeViewProperties():

    """Properties of the associative views and sections

    **WARNING!!**: Associative views and sections are deprecated and not supported in
    Allplan >=2023! Use UVSs instead (represented by _ViewSectionElement_ class)

    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, arg2: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Constructor
        """
    @typing.overload
    def __init__(self, arg2: AssociativeViewProperties):
        """Constructor
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def AdjacentEdges(self) -> None:
        """Set/get the adjacent edges state

        :type: None
        """
    @property
    def ColorHiddenEdge(self) -> None:
        """Set/get the color of the hidden edges

        :type: None
        """
    @property
    def ColorVisibleEdge(self) -> None:
        """Set/get the color of the visible edges

        :type: None
        """
    @property
    def ConvertTo2D(self) -> None:
        """Set/get the convert to 2D state

        :type: None
        """
    @property
    def ElementRepresentation(self) -> None:
        """Set/get the element representation

        :type: None
        """
    @property
    def Hidden(self) -> None:
        """Set/get the hidden state

        :type: None
        """
    @property
    def LayerBoundaryLine(self) -> None:
        """Set/get the layer of the boundary line

        :type: None
        """
    @property
    def LayerFinishLine(self) -> None:
        """Set/get the layer of the finish line

        :type: None
        """
    @property
    def LayerHiddenEdge(self) -> None:
        """Set/get the layer of the hidden edges

        :type: None
        """
    @property
    def LayerHiddenSectionLine(self) -> None:
        """Set/get the layer of the hidden section line

        :type: None
        """
    @property
    def LayerSectionLine(self) -> None:
        """Set/get the layer of the section line

        :type: None
        """
    @property
    def LayerVisibleEdge(self) -> None:
        """Set/get the layer of the visible edges

        :type: None
        """
    @property
    def PenHiddenEdge(self) -> None:
        """Set/get the pen of the hidden edges

        :type: None
        """
    @property
    def PenVisibleEdge(self) -> None:
        """Set/get the pen of the visible edges

        :type: None
        """
    @property
    def RemoveAdjacentEdges(self) -> None:
        """Set/get the remove adjacent edges state

        :type: None
        """
    @property
    def ShowHiddenEdges(self) -> None:
        """Set/get the show hidden edges state

        :type: None
        """
    @property
    def ShowSectionBody(self) -> None:
        """:type: None
        """
    @property
    def ShowVisibleEdges(self) -> None:
        """Set/get the show visible edges state

        :type: None
        """
    @property
    def StrokeHiddenEdge(self) -> None:
        """Set/get the stroke of the hidden edges

        :type: None
        """
    @property
    def StrokeVisibleEdge(self) -> None:
        """Set/get the stroke of the visible edges

        :type: None
        """

class BasisElement(AllplanElement):

    """Abstract base class representing **general elements** in Allplan.

    General elements may have geometrical representation, such as _3D objects_ (represented by _ModelElement3D_),
    but may also be non-geometrical, such as _element group_ (represented by ElementGroupElement)

    """

class AttributeContainer(BasisElement, AllplanElement):
    """AttributeContainer class
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, attributesObject: object):
        """Constructor

        Args:
            butesObject:    Attributes object
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class BasisPropertyDialogs():

    @staticmethod
    def OpenBitmapResourceDialog(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, bitmapPath: str) -> str:
        """Open the bitmap resource dialog

        Args:
            doc:        Document
            bitmapPath: Initial path

        Returns:
             Selected bitmap path
        """
    @staticmethod
    def OpenRGBColorDialog(doc,color: int) -> int:
        """Open the RGB color dialog

        Args:
                doc     Document
                color   Current color
        """

class BitmapAreaElement(BasisElement, AllplanElement):
    """Representation of the **bitmap area** in Allplan.
    """
    def GetBitmapAreaProperties(self) -> BitmapAreaProperties:
        """Get the BitmapArea properties

        Returns:
             BitmapArea properties
        """
    def SetBitmapAreaProperties(self, bitmapAreaProp: BitmapAreaProperties):
        """Set the bitmapArea properties

        Args:
            bitmapAreaProp: BitmapArea properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, bitmapAreaProp: BitmapAreaProperties,
                 geometryObject: object):
        """Constructor

        Args:
            commonProp:     Common properties
            bitmapAreaProp: BitmapArea properties
            geometryObject: Geometry element
        """
    @typing.overload
    def __init__(self, BitmapAreaElement: BitmapAreaElement):
        """Copy constructor

        Args:
            bitmpaAreaElement:   Bitmap area element element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class BitmapAreaProperties():
    """Properties of the bitmap area.
    """
    def __eq__(self, prop: BitmapAreaProperties) -> bool:
        """equal operator

        Args:
            prop: BitmapProperties to compare

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
    def BitmapName(self) -> None:
        """Property for bitmap name of the bitmap area

        :type: None
        """
    @property
    def DirectionToReferenceLine(self) -> None:
        """Property for direction to reference line

        :type: None
        """
    @property
    def ReferencePoint(self) -> None:
        """Property for reference point

        :type: None
        """
    @property
    def RotationAngle(self) -> None:
        """Property for rotation angle

        :type: None
        """
    @property
    def TransparentColor(self) -> None:
        """Property for transparent color

        :type: None
        """
    @property
    def TransparentColorTolerance(self) -> None:
        """Property for transparent color tolerance

        :type: None
        """
    @property
    def UseDirectionToReferenceLine(self) -> None:
        """Property for usage of direction to reference line

        :type: None
        """
    @property
    def UseMetricalValues(self) -> None:
        """Property for metrical values

        :type: None
        """
    @property
    def UsePixelMask(self) -> None:
        """Property for usage of mask black pixels

        :type: None
        """
    @property
    def UseReferencePoint(self) -> None:
        """Property for usage of reference point

        :type: None
        """
    @property
    def UseRepeatTile(self) -> None:
        """Property for repeat tile

        :type: None
        """
    @property
    def XOffset(self) -> None:
        """Property for X offset value

        :type: None
        """
    @property
    def XScalingFactor(self) -> None:
        """Property for X scaling factor

        :type: None
        """
    @property
    def YOffset(self) -> None:
        """Property for Y offset value

        :type: None
        """
    @property
    def YScalingFactor(self) -> None:
        """Property for Y scaling factor

        :type: None
        """

class BitmapDefinition():

    """
    """
    @staticmethod
    def Create(bitmapName: str) -> BitmapDefinition:
        """Create a bitmap definition

        Returns:
               Bitmap definition

        Args:
            bitmapName: Path and name of the bitmap
        """
    def Dump(self, deep: bool):
        """Dump the bitmap definition

        Args:
            deep:   True for a deep dump
        """
    def GetBitmapName(self) -> str:
        """Get the name

        Returns:
            Name
        """
    def GetHeight(self) -> int:
        """Get bitmap height

        Returns:
            height in pixels
        """
    def GetPixel(self, x: int, y: int) -> int:
        """Get the color of a specific pixel

        Args:
            x:  horizontal position
            y:  vertical position

        Returns:
            Color as ARGB
        """
    def GetWidth(self) -> int:
        """Get bitmap width

        Returns:
            Width in pixels
        """
    def IsHDRI(self) -> bool:
        """Is High Dynamic Range Image

        Returns:
            Bitmap is a HDR image
        """
    def LoadBitmap(self) -> bool:
        """Load bitmap

        Returns:
            True, when loading was successful
        """
    def setName(self, resourceName: str):
        """Set the name of the bitmap

        Args:
            resourceName:   name to assign
        """
    @property
    def AbsolutePath(self) -> str:
        """Absolute path of the bitmap"""
    @AbsolutePath.setter
    def AbsolutePath(self, value: str) -> None:
        """Set the value
        """
    @property
    def RelativeName(self) -> str:
        """Relative name of the bitmap"""
    @RelativeName.setter
    def RelativeName(self, value: str) -> None:
        """Set the value
        """

class ClippingPathProperties():
    """Representation if the properties of a clipping path of a UVS
    """
    def __init__(self):
        """Initialize
        """
    @property
    def BottomLevel(self) -> None:
        """The bottom elevation of the section"""
    @property
    def IsClippingLineOn(self) -> None:
        """Whether to draw the clipping line"""
    @property
    def IsHeightFromElementOn(self) -> None:
        """Whether to get the section height from elements"""
    @property
    def SectionIdentifier(self) -> None:
        """the section identifier"""
    @property
    def TopLevel(self) -> None:
        """The top elevation of the section"""

class CombinationType(enum.Enum):
    """Definition of the combination type

    eVx:
    eVy:
    eVz:
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

    def __getitem__(self, key: (str | int | float)) -> CombinationType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ConsiderType(enum.Enum):
    """Possible options for how a smart symbol (macro) placed in a room with finishing surfaces is displayed in animation and in sections
    """
    eConsiderAutomatic = 3
    """Automatic to nearest (floor or ceiling) surface - !!! don't use this value at the moment, it's only for internal usage"""
    eConsiderCeilingOpening = 8
    """Adapts to ceiling opening"""
    eConsiderCeilingRecess = 9
    """Adapts to ceiling recess"""
    eConsiderCeilingSurface = 2
    """Adapts to the height of the ceiling in animation and sections."""
    eConsiderDoorOpening = 5
    """Adapts to door opening"""
    eConsiderFloorSurface = 1
    """Adapts to the height of the floor"""
    eConsiderNiche = 6
    """Adapts to niche opening"""
    eConsiderNothing = 0
    """No adaptation"""
    eConsiderRecess = 7
    """Adapts to recess opening"""
    eConsiderWindowOpening = 4
    """Adapts to window opening"""

    names = {eConsiderNothing: eConsiderNothing,
             eConsiderFloorSurface: eConsiderFloorSurface,
             eConsiderCeilingSurface: eConsiderCeilingSurface,
             eConsiderAutomatic: eConsiderAutomatic,
             eConsiderWindowOpening: eConsiderWindowOpening,
             eConsiderDoorOpening: eConsiderDoorOpening,
             eConsiderNiche: eConsiderNiche,
             eConsiderRecess: eConsiderRecess,
             eConsiderCeilingOpening: eConsiderCeilingOpening,
             eConsiderCeilingRecess: eConsiderCeilingRecess}

    values = {0: eConsiderNothing,
              1: eConsiderFloorSurface,
              2: eConsiderCeilingSurface,
              3: eConsiderAutomatic,
              4: eConsiderWindowOpening,
              5: eConsiderDoorOpening,
              6: eConsiderNiche,
              7: eConsiderRecess,
              8: eConsiderCeilingOpening,
              9: eConsiderCeilingRecess}

    def __getitem__(self, key: (str | int | float)) -> ConsiderType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class DimensionLineElement(BasisElement, AllplanElement):
    """Representation of the **dimension line** in Allplan.

    This class is also a base class for the **elevation points**.

    """
    def GetDimensionPoints(self) -> NemAll_Python_Geometry.Point3DList:
        """Get the dimension points

        Returns:
             Dimension points
        """
    def GetDirectionVector(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the direction vector

        Returns:
             Direction vector
        """
    def GetPlacementVector(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the placement vector

        Returns:
             Placement vector
        """
    def GetProperties(self) -> DimensionProperties:
        """Get the properties

        Returns:
            properties
        """
    def GetSegmentProperties(self) -> DimensionSegmentPropertiesList:
        """Get the segment properties

        Returns:
            Segment properties
        """
    def SetDimensionPoints(self, Dimension points: NemAll_Python_Geometry.Point3DList):
        """Set the dimension points

        Args:
             Dimension points
        """
    def SetDirectionVector(self, Direction vector: NemAll_Python_Geometry.Vector2D):
        """Set the direction vector

        Args:
             Direction vector
        """
    def SetPlacementVector(self, Placement vector: NemAll_Python_Geometry.Vector2D):
        """Set the placement vector

        Args:
             Placement vector
        """
    def SetProperties(self, Prop: DimensionProperties):
        """Set the properties

        Args:
            Prop:properties
        """
    def SetSegmentProperties(self, Prop: DimensionSegmentPropertiesList):
        """Set the segment properties

        Args:
            Segement:properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, dimensionPoints: NemAll_Python_Geometry.Point3DList, dimensionPoints: NemAll_Python_Geometry.Vector2D,
                 placementPoint: NemAll_Python_Geometry.Vector2D, directionVector: DimensionProperties):
        """Constructor

        Args:
            dimensionPoints:      Dimension points
            placementVector:      Placement vector to the first dimension point
            directionVector:      Direction vector
            dimensionProperties:  Dimension properties
        """
    @typing.overload
    def __init__(self, dimensionPoints: NemAll_Python_Geometry.Point3DList, arg3: NemAll_Python_Geometry.Vector2D,
                 dimensionPoints: NemAll_Python_Geometry.Vector2D, placementPoint: DimensionProperties, directionVector: DimensionSegmentPropertiesList):
        """Constructor

        Args:
            dimensionPoints:              Dimension points
            placementVector:              Placement vector to the first dimension point
            directionVector:              Direction vector
            dimensionProperties:          Dimension properties
            dimensionSegmentProperties:   Dimension segment properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class DimensionProperties():
    """Properties of the dimension line as well as the elevation points.
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, arg2: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, arg3: Dimensioning):
        """Default constructor
        """
    @typing.overload
    def __init__(self, arg2: DimensionProperties):
        """Constructor
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def AdditionalNumberIsBold(self) -> bool:
        """Additional number is Bold
        """
    @AdditionalNumberIsBold.setter
    def AdditionalNumberIsBold(self, value: bool) -> None:
        """Additional number is Bold
        """
    @property
    def AdditionalNumberIsItalic(self) -> bool:
        """Additional number is Italic
        """
    @AdditionalNumberIsItalic.setter
    def AdditionalNumberIsItalic(self, value: bool) -> None:
        """Additional number is Italic
        """
    @property
    def AdditionalNumberIsUnderline(self) -> bool:
        """Additional Text is Underline
        """
    @AdditionalNumberIsUnderline.setter
    def AdditionalNumberIsUnderline(self, value: bool) -> None:
        """Additional Text is Underline
        """
    @property
    def AdditionalNumberIsVisible(self) -> bool:
        """Additional number is visible
        """
    @AdditionalNumberIsVisible.setter
    def AdditionalNumberIsVisible(self, value: bool) -> None:
        """Additional number is visible
        """
    @property
    def AdditionalTextIsBold(self) -> bool:
        """Additional text is Bold
        """
    @AdditionalTextIsBold.setter
    def AdditionalTextIsBold(self, value: bool) -> None:
        """Additional text is Bold
        """
    @property
    def AdditionalTextIsItalic(self) -> bool:
        """Additional text is Italic
        """
    @AdditionalTextIsItalic.setter
    def AdditionalTextIsItalic(self, value: bool) -> None:
        """Additional text is Italic
        """
    @property
    def AdditionalTextIsUnderline(self) -> bool:
        """Additional text is Underline
        """
    @AdditionalTextIsUnderline.setter
    def AdditionalTextIsUnderline(self, value: bool) -> None:
        """Additional text is Underline
        """
    @property
    def AdditionalTextIsVisible(self) -> bool:
        """Additional Text is visible
        """
    @AdditionalTextIsVisible.setter
    def AdditionalTextIsVisible(self, value: bool) -> None:
        """Additional Text is visible
        """
    @property
    def AuxPenIDDimLineFlag(self) -> bool:
        """Dimension Line Pen ID like construction line
        """
    @AuxPenIDDimLineFlag.setter
    def AuxPenIDDimLineFlag(self, value: bool) -> None:
        """Dimension Line Pen ID like construction line
        """
    @property
    def AuxPenIDExtensionLineFlag(self) -> bool:
        """Extension Line Pen ID like construction line
        """
    @AuxPenIDExtensionLineFlag.setter
    def AuxPenIDExtensionLineFlag(self, value: bool) -> None:
        """Extension Line Pen ID like construction line
        """
    @property
    def AuxPenIDNumberTextFlag(self) -> bool:
        """Numbers/text Pen ID like construction line
        """
    @AuxPenIDNumberTextFlag.setter
    def AuxPenIDNumberTextFlag(self, value: bool) -> None:
        """Numbers/text Pen ID like construction line
        """
    @property
    def AuxPenIDPointSymbolFlag(self) -> bool:
        """Symbol Pen ID like construction line
        """
    @AuxPenIDPointSymbolFlag.setter
    def AuxPenIDPointSymbolFlag(self, value: bool) -> None:
        """Symbol Pen ID like construction line
        """
    @property
    def DecimalPlaces(self) -> int:
        """Decimal Places
        """
    @DecimalPlaces.setter
    def DecimalPlaces(self, value: int) -> None:
        """Decimal Places
        """
    @property
    def DimensionLineIsVisible(self) -> bool:
        """Dimension Line visible
        """
    @DimensionLineIsVisible.setter
    def DimensionLineIsVisible(self, value: bool) -> None:
        """Dimension Line visible
        """
    @property
    def DimensionNumberIsBold(self) -> bool:
        """Dimension number is Bold
        """
    @DimensionNumberIsBold.setter
    def DimensionNumberIsBold(self, value: bool) -> None:
        """Dimension number is Bold
        """
    @property
    def DimensionNumberIsItalic(self) -> bool:
        """Dimension number is Italic
        """
    @DimensionNumberIsItalic.setter
    def DimensionNumberIsItalic(self, value: bool) -> None:
        """Dimension number is Italic
        """
    @property
    def DimensionNumberIsUnderline(self) -> bool:
        """Dimension number is Underline
        """
    @DimensionNumberIsUnderline.setter
    def DimensionNumberIsUnderline(self, value: bool) -> None:
        """Dimension number is Underline
        """
    @property
    def DimensionNumberIsVisible(self) -> bool:
        """Dimension number is visible
        """
    @DimensionNumberIsVisible.setter
    def DimensionNumberIsVisible(self, value: bool) -> None:
        """Dimension number is visible
        """
    @property
    def ElevationBaseOffset(self) -> float:
        """Property for the elevation base offset
        """
    @ElevationBaseOffset.setter
    def ElevationBaseOffset(self, value: float) -> None:
        """Property for the elevation base offset
        """
    @property
    def FontIDAdditionalNumber(self) -> int:
        """Property for the font ID of the Additional number
        """
    @FontIDAdditionalNumber.setter
    def FontIDAdditionalNumber(self, value: int) -> None:
        """Property for the font ID of the Additional number
        """
    @property
    def FontIDAdditionalText(self) -> int:
        """Property for the font ID of the Additional text
        """
    @FontIDAdditionalText.setter
    def FontIDAdditionalText(self, value: int) -> None:
        """Property for the font ID of the Additional text
        """
    @property
    def FontIDDimensionNumber(self) -> int:
        """Property for the font ID of the dimension number
        """
    @FontIDDimensionNumber.setter
    def FontIDDimensionNumber(self, value: int) -> None:
        """Property for the font ID of the dimension number
        """
    @property
    def IsAbsoluteElevation(self) -> bool:
        """Whether to use the absolute elevation values"""
    @IsAbsoluteElevation.setter
    def IsAbsoluteElevation(self, value: bool) -> None:
        """Property for the elevation base offset
        """
    @property
    def IsExponentFormat(self) -> bool:
        """Exponent Format
        """
    @IsExponentFormat.setter
    def IsExponentFormat(self, value: bool) -> None:
        """Exponent Format
        """
    @property
    def IsLineColorFromLayer(self) -> bool:
        """Is Line color from layer
        """
    @IsLineColorFromLayer.setter
    def IsLineColorFromLayer(self, value: bool) -> None:
        """Is Line color from layer
        """
    @property
    def IsLineStyleFromLayer(self) -> bool:
        """Is Line sytle from layer
        """
    @IsLineStyleFromLayer.setter
    def IsLineStyleFromLayer(self, value: bool) -> None:
        """Is Line sytle from layer
        """
    @property
    def IsPenFromLayer(self) -> bool:
        """Is Pen from layer
        """
    @IsPenFromLayer.setter
    def IsPenFromLayer(self, value: bool) -> None:
        """Is Pen from layer
        """
    @property
    def IsTextOpaque(self) -> bool:
        """Text is upside down
        """
    @IsTextOpaque.setter
    def IsTextOpaque(self, value: bool) -> None:
        """Text is upside down
        """
    @property
    def LayerIDDimLine(self) -> int:
        """Dimension Line Layer ID
        """
    @LayerIDDimLine.setter
    def LayerIDDimLine(self, value: int) -> None:
        """Dimension Line Layer ID
        """
    @property
    def LeadingCharacter(self) -> string:
        """Property for the leading characters
        """
    @LeadingCharacter.setter
    def LeadingCharacter(self, value: string) -> None:
        """Property for the leading characters
        """
    @property
    def LineColorIDDimLine(self) -> int:
        """Dimension Line Color ID
        """
    @LineColorIDDimLine.setter
    def LineColorIDDimLine(self, value: int) -> None:
        """Dimension Line Color ID
        """
    @property
    def LineColorIDExtensionLine(self) -> int:
        """Extension Line Color ID
        """
    @LineColorIDExtensionLine.setter
    def LineColorIDExtensionLine(self, value: int) -> None:
        """Extension Line Color ID
        """
    @property
    def LineColorIDNumberText(self) -> int:
        """Numbers/text Color ID
        """
    @LineColorIDNumberText.setter
    def LineColorIDNumberText(self, value: int) -> None:
        """Numbers/text Color ID
        """
    @property
    def LineColorIDPointSymbol(self) -> int:
        """Symbol Color ID
        """
    @LineColorIDPointSymbol.setter
    def LineColorIDPointSymbol(self, value: int) -> None:
        """Symbol Color ID
        """
    @property
    def LineStyleIDDimLine(self) -> int:
        """Dimension Line Line Style ID
        """
    @LineStyleIDDimLine.setter
    def LineStyleIDDimLine(self, value: int) -> None:
        """Dimension Line Line Style ID
        """
    @property
    def LineStyleIDExtensionLine(self) -> int:
        """Extension Line Line Style ID
        """
    @LineStyleIDExtensionLine.setter
    def LineStyleIDExtensionLine(self, value: int) -> None:
        """Extension Line Line Style ID
        """
    @property
    def LineStyleIDNumberText(self) -> int:
        """Numbers/text Line Style ID
        """
    @LineStyleIDNumberText.setter
    def LineStyleIDNumberText(self, value: int) -> None:
        """Numbers/text Line Style ID
        """
    @property
    def LineStyleIDPointSymbol(self) -> int:
        """Symbol Line Style ID
        """
    @LineStyleIDPointSymbol.setter
    def LineStyleIDPointSymbol(self, value: int) -> None:
        """Symbol Line Style ID
        """
    @property
    def MeasuredValueUnit(self) -> int:
        """Measured Value Unit
        """
    @MeasuredValueUnit.setter
    def MeasuredValueUnit(self, value: int) -> None:
        """Measured Value Unit
        """
    @property
    def PenIDDimLine(self) -> int:
        """Dimension Line Pen ID
        """
    @PenIDDimLine.setter
    def PenIDDimLine(self, value: int) -> None:
        """Dimension Line Pen ID
        """
    @property
    def PenIDExtensionLine(self) -> int:
        """Extension Line Pen ID
        """
    @PenIDExtensionLine.setter
    def PenIDExtensionLine(self, value: int) -> None:
        """Extension Line Pen ID
        """
    @property
    def PenIDNumberText(self) -> int:
        """Numbers/text Pen ID
        """
    @PenIDNumberText.setter
    def PenIDNumberText(self, value: int) -> None:
        """Numbers/text Pen ID
        """
    @property
    def PenIDPointSymbol(self) -> int:
        """Symbol Pen ID
        """
    @PenIDPointSymbol.setter
    def PenIDPointSymbol(self, value: int) -> None:
        """Symbol Pen ID
        """
    @property
    def PointSymbol(self) -> int:
        """Property for the point symbol of the elevation
        """
    @PointSymbol.setter
    def PointSymbol(self, value: int) -> None:
        """Property for the point symbol of the elevation
        """
    @property
    def PointSymbolEnd(self) -> int:
        """Property for the point symbol at the start of the dimension line
        """
    @PointSymbolEnd.setter
    def PointSymbolEnd(self, value: int) -> None:
        """Property for the point symbol at the start of the dimension line
        """
    @property
    def PointSymbolSize(self) -> float:
        """Size of Point Symbol
        """
    @PointSymbolSize.setter
    def PointSymbolSize(self, value: float) -> None:
        """Size of Point Symbol
        """
    @property
    def PointSymbolStart(self) -> int:
        """Property for the point symbol at the start of the dimension line
        """
    @PointSymbolStart.setter
    def PointSymbolStart(self, value: int) -> None:
        """Property for the point symbol at the start of the dimension line
        """
    @property
    def RoundOffFeet(self) -> float:
        """Rounf Off Feet
        """
    @RoundOffFeet.setter
    def RoundOffFeet(self, value: float) -> None:
        """Rounf Off Feet
        """
    @property
    def RoundOffInch(self) -> float:
        """Round Off Inch
        """
    @RoundOffInch.setter
    def RoundOffInch(self, value: float) -> None:
        """Round Off Inch
        """
    @property
    def RoundOffNormal(self) -> float:
        """Round Off Normal
        """
    @RoundOffNormal.setter
    def RoundOffNormal(self, value: float) -> None:
        """Round Off Normal
        """
    @property
    def TailingCharacters(self) -> string:
        """Property for the tailing characters
        """
    @TailingCharacters.setter
    def TailingCharacters(self, value: string) -> None:
        """Property for the tailing characters
        """
    @property
    def TailingZeros(self) -> int:
        """Tailing Zeros
        """
    @TailingZeros.setter
    def TailingZeros(self, value: int) -> None:
        """Tailing Zeros
        """
    @property
    def TextHeightAdditionalNumber(self) -> float:
        """Property for the height of the Additional number
        """
    @TextHeightAdditionalNumber.setter
    def TextHeightAdditionalNumber(self, value: float) -> None:
        """Property for the height of the Additional number
        """
    @property
    def TextHeightAdditionalText(self) -> float:
        """Property for the height of the Additional text
        """
    @TextHeightAdditionalText.setter
    def TextHeightAdditionalText(self, value: float) -> None:
        """Property for the height of the Additional text
        """
    @property
    def TextHeightDimensionNumber(self) -> float:
        """Property for the height of the dimension number
        """
    @TextHeightDimensionNumber.setter
    def TextHeightDimensionNumber(self, value: float) -> None:
        """Property for the height of the dimension number
        """
    @property
    def TextIsEqual(self) -> bool:
        """Text Is Equal
        """
    @TextIsEqual.setter
    def TextIsEqual(self, value: bool) -> None:
        """Text Is Equal
        """
    @property
    def TextIsFlipped(self) -> bool:
        """Text is flipped
        """
    @TextIsFlipped.setter
    def TextIsFlipped(self, value: bool) -> None:
        """Text is flipped
        """
    @property
    def TextIsUpSideDown(self) -> bool:
        """Text is upside down
        """
    @TextIsUpSideDown.setter
    def TextIsUpSideDown(self, value: bool) -> None:
        """Text is upside down
        """
    @property
    def TextLocation(self) -> eTextLocation:
        """The location of the dimension number"""
    @TextLocation.setter
    def TextLocation(self, value: eTextLocation) -> None:
        """Property for the elevation base offset
        """
    @property
    def TextOffset(self) -> float:
        """Offset of text from dimension line
        """
    @TextOffset.setter
    def TextOffset(self, value: float) -> None:
        """Offset of text from dimension line
        """
    @property
    def TextWidthAdditionalNumberFactor(self) -> float:
        """Additional Number Text Width Factor
        """
    @TextWidthAdditionalNumberFactor.setter
    def TextWidthAdditionalNumberFactor(self, value: float) -> None:
        """Additional Number Text Width Factor
        """
    @property
    def TextWidthAdditionalTextFactor(self) -> float:
        """Dimension Number Text Width Factor
        """
    @TextWidthAdditionalTextFactor.setter
    def TextWidthAdditionalTextFactor(self, value: float) -> None:
        """Dimension Number Text Width Factor
        """
    @property
    def TextWidthDimensionNumberFactor(self) -> float:
        """Dimension Number Text Width Factor
        """
    @TextWidthDimensionNumberFactor.setter
    def TextWidthDimensionNumberFactor(self, value: float) -> None:
        """Dimension Number Text Width Factor
        """

class DimensionSegmentProperties():
    """DimensionSegmentProperties class
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, arg2: DimensionSegmentProperties):
        """Constructor
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def AdditionalNumber(self) -> float:
        """Get segment additional number
        """
    @AdditionalNumber.setter
    def AdditionalNumber(self, AdditionalNumber: float) -> None:
        """Set segment additional number

        Args:
            AdditionalNumber: segment additional number
        """
    @property
    def AdditionalNumberIsBold(self) -> bool:
        """Get segment additional number is bold
        """
    @AdditionalNumberIsBold.setter
    def AdditionalNumberIsBold(self, AdditionalNumberIsBold: bool) -> None:
        """Set segment additional number is bold

        Args:
            AdditionalNumberIsBold: segment additional number is bold
        """
    @property
    def AdditionalNumberIsItalic(self) -> bool:
        """Get segment additional number is italic
        """
    @AdditionalNumberIsItalic.setter
    def AdditionalNumberIsItalic(self, AdditionalNumberIsItalic: bool) -> None:
        """Set segment additional number is italic

        Args:
            AdditionalNumberIsItalic: segment additional number is italic
        """
    @property
    def AdditionalNumberIsUnderline(self) -> bool:
        """Get segment additional number is underline
        """
    @AdditionalNumberIsUnderline.setter
    def AdditionalNumberIsUnderline(self, AdditionalNumberIsUnderline: bool) -> None:
        """Set segment additional number is underline

        Args:
            AdditionalNumberIsUnderline: segment additional number is underline
        """
    @property
    def AdditionalNumberIsVisible(self) -> bool:
        """Get segment segment additional number is visible
        """
    @AdditionalNumberIsVisible.setter
    def AdditionalNumberIsVisible(self, AdditionalNumberIsVisible: bool) -> None:
        """Set segment segment additional number is visible

        Args:
            AdditionalNumberIsVisible: segment segment additional number is visible
        """
    @property
    def AdditionalText(self) -> string:
        """Get segment additional text
        """
    @AdditionalText.setter
    def AdditionalText(self, AdditionalText: string) -> None:
        """Set segment additional text

        Args:
            AdditionalText: segment additional text
        """
    @property
    def AdditionalTextIsBold(self) -> bool:
        """Get segment additional text is bold
        """
    @AdditionalTextIsBold.setter
    def AdditionalTextIsBold(self, AdditionalTextIsBold: bool) -> None:
        """Set segment additional text is bold

        Args:
            AdditionalTextIsBold: segment additional text is bold
        """
    @property
    def AdditionalTextIsItalic(self) -> bool:
        """Get segment additional text is italic
        """
    @AdditionalTextIsItalic.setter
    def AdditionalTextIsItalic(self, AdditionalTextIsItalic: bool) -> None:
        """Set segment additional text is italic

        Args:
            AdditionalTextIsItalic: segment additional text is italic
        """
    @property
    def AdditionalTextIsUnderline(self) -> bool:
        """Get segment additional text is underline
        """
    @AdditionalTextIsUnderline.setter
    def AdditionalTextIsUnderline(self, AdditionalTextIsUnderline: bool) -> None:
        """Set segment additional text is underline

        Args:
            AdditionalTextIsUnderline: segment additional text is underline
        """
    @property
    def AdditionalTextIsVisible(self) -> bool:
        """Get segment segment additional text is visible
        """
    @AdditionalTextIsVisible.setter
    def AdditionalTextIsVisible(self, AdditionalTextIsVisible: bool) -> None:
        """Set segment segment additional text is visible

        Args:
            AdditionalTextIsVisible: segment segment additional text is visible
        """
    @property
    def DimensionNumberIsBold(self) -> bool:
        """Get segment dimension number is bold
        """
    @DimensionNumberIsBold.setter
    def DimensionNumberIsBold(self, DimensionNumberIsBold: bool) -> None:
        """Set segment dimension number is bold

        Args:
            DimensionNumberIsBold: segment dimension number is bold
        """
    @property
    def DimensionNumberIsItalic(self) -> bool:
        """Get segment dimension number is italic
        """
    @DimensionNumberIsItalic.setter
    def DimensionNumberIsItalic(self, DimensionNumberIsItalic: bool) -> None:
        """Set segment dimension number is italic

        Args:
            DimensionNumberIsItalic: segment dimension number is italic
        """
    @property
    def DimensionNumberIsUnderline(self) -> bool:
        """Get segment dimension number is underline
        """
    @DimensionNumberIsUnderline.setter
    def DimensionNumberIsUnderline(self, DimensionNumberIsUnderline: bool) -> None:
        """Set segment dimension number is underline

        Args:
            DimensionNumberIsUnderline: segment dimension number is underline
        """
    @property
    def DimensionNumberIsVisible(self) -> bool:
        """Get segment dimension number is visible
        """
    @DimensionNumberIsVisible.setter
    def DimensionNumberIsVisible(self, DimensionNumberIsVisible: bool) -> None:
        """Set segment dimension number is visible

        Args:
            DimensionNumberIsVisible: segment dimension number is visible
        """
    @property
    def PointSymbolEnd(self) -> int:
        """Get point symbol end
        """
    @PointSymbolEnd.setter
    def PointSymbolEnd(self, PointSymbolStart: int) -> None:
        """Set point symbol end

        Args:
            PointSymbolStart: Point symbol end
        """
    @property
    def PointSymbolStart(self) -> int:
        """Get point symbol start
        """
    @PointSymbolStart.setter
    def PointSymbolStart(self, PointSymbolStart: int) -> None:
        """Set point symbol start

        Args:
            PointSymbolStart: Point symbol start
        """
    @property
    def SegmentNumber(self) -> int:
        """Get segment number
        """
    @SegmentNumber.setter
    def SegmentNumber(self, SegmentNumber: int) -> None:
        """Set segment number

        Args:
            SegmentNumber: segment number
        """

class DimensionSegmentPropertiesList():
    """List for DimensionSegmentProperties objects
    """
    def __contains__(self, value: DimensionSegmentProperties) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: DimensionSegmentProperties):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: DimensionSegmentPropertiesList) -> bool:
        """Compare two lists

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> DimensionSegmentProperties:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, eleList: list) -> DimensionSegmentPropertiesList:
        """Add a list

        Args:
            eleList: DimensionSegmentProperties list

        Returns:
            Lists with the added elements
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ele: DimensionSegmentProperties):
        """Constructor with a DimensionSegmentProperties

        Args:
            ele: DimensionSegmentProperties
        """
    @typing.overload
    def __init__(self, eleList: list):
        """Constructor with a list of DimensionSegmentProperties

        Args:
            eleList: DimensionSegmentProperties list
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
    def __setitem__(self, index: int | slice, value: DimensionSegmentProperties):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: DimensionSegmentProperties):
        """Append a list item

        Args:
            value: Value to append
        """
    @typing.overload
    def extend(self, iterable: DimensionSegmentPropertiesList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    @typing.overload
    def extend(self, eleList: list):
        """Extend the list

        Args:
            eleList: DimensionSegmentProperties list
        """
    def extend(self):
        """ Overloaded function. See individual overloads.
        """

class Dimensioning(enum.Enum):
    """Type of the dimensioning
    """
    eDimensionLine = 1
    """As a dimension line"""
    eElevation = 2
    """As elevation points"""

    names = {eDimensionLine: eDimensionLine,
             eElevation: eElevation}

    values = {1: eDimensionLine,
              2: eElevation}

    def __getitem__(self, key: (str | int | float)) -> Dimensioning:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ElementGroupElement(BasisElement, AllplanElement):
    """Representation of the **element group** in Allplan.

    Element group can be used to organize model elements of any kind 
    (architectural components, general elements...) into groups with a Parent-Child
    relationship, where the group is the parent, and all elements are children.

    """
    def GetElementGroupProperties(self) -> ElementGroupProperties:
        """Get the ElementGroup properties

        Returns:
             ElementGroup properties
        """
    def GetObjectList(self) -> list:
        """Get the list of element group objects

        Returns:
             Element group object list
        """
    def SetElementGroupProperties(self, ElementGroupProp: ElementGroupProperties):
        """Set the ElementGroup properties

        Args:
            ElementGroupProp: ElementGroup properties
        """
    @typing.overload
    def __init__(self):
        """Initialize"""
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, elementGroupProp: ElementGroupProperties,
                 elementGroupObjectList: list):
        """Constructor

        Args:
            commonProp:             Common properties
            elementGroupProp:       ElementGroup properties
            elementGroupObjectList: ElementGroup object list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class ElementGroupProperties():
    """Representation of the **elevation point** in Allplan
    """
    def __eq__(self, prop: ElementGroupProperties) -> bool:
        """equal operator

        Args:
            prop: ElementGroupProperties to compare

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
    def ModifiableFlag(self) -> None:
        """Property for modifiable flag

        :type: None
        """
    @property
    def Name(self) -> None:
        """Property for name of element group

        :type: None
        """
    @property
    def SubType(self) -> None:
        """Property for macro sub type

        :type: None
        """

class ElementNodeElement(BasisElement, AllplanElement):
    """ElementNodeElement class
    """
    def GetObjectList(self) -> list:
        """Get the list of element node objects

        Returns:
             Element node object list
        """
    def GetParentID(self) -> type:
        """Get parent ID

        Returns:
            UUID
        """
    def SetParentID(self, ParentID: type):
        """Set the parent element id to this object

        Args:
            ParentID:(UUID) sub element id
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, elementNodeId: type, elementNodeObjectList: list):
        """Constructor

        Args:
            commonProp:             Common properties
            elementGroupProp:       ElementGroup properties
            elementGroupObjectList: ElementGroup object list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class ElevationElement(DimensionLineElement, BasisElement, AllplanElement):
    """ElevationElement class
    """
    def GetDimensionPoints(self) -> NemAll_Python_Geometry.Point3DList:
        """Get the dimension points

        Returns:
             Dimension points
        """
    def GetDirectionVector(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the direction vector

        Returns:
             Direction vector
        """
    def GetPlacementVector(self) -> NemAll_Python_Geometry.Vector2D:
        """Get the placement vector

        Returns:
             Placement vector
        """
    def GetProperties(self) -> DimensionProperties:
        """Get the properties

        Returns:
            properties
        """
    def GetSegmentProperties(self) -> DimensionSegmentPropertiesList:
        """Get the segment properties

        Returns:
            Segment properties
        """
    def SetDimensionPoints(self, Dimension points: NemAll_Python_Geometry.Point3DList):
        """Set the dimension points

        Args:
             Dimension points
        """
    def SetDirectionVector(self, Direction vector: NemAll_Python_Geometry.Vector2D):
        """Set the direction vector

        Args:
             Direction vector
        """
    def SetPlacementVector(self, Placement vector: NemAll_Python_Geometry.Vector2D):
        """Set the placement vector

        Args:
             Placement vector
        """
    def SetProperties(self, Prop: DimensionProperties):
        """Set the properties

        Args:
            Prop:properties
        """
    def SetSegmentProperties(self, Prop: DimensionSegmentPropertiesList):
        """Set the segment properties

        Args:
            Segement:properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, dimensionPoints: NemAll_Python_Geometry.Point3DList, placementVector: NemAll_Python_Geometry.Vector2D,
                 directionVector: NemAll_Python_Geometry.Vector2D, settings: DimensionProperties):
        """Constructor

        Args:
            dimensionPoints:       Elevation points
            placementVector:       Placement vector to the first elevation point
            directionVector:       Direction vector
            DimensionProperties:   Dimension properties
        """
    @typing.overload
    def __init__(self, dimensionPoints: NemAll_Python_Geometry.Point3DList, arg3: NemAll_Python_Geometry.Vector2D,
                 dimensionPoints: NemAll_Python_Geometry.Vector2D, placementPoint: DimensionProperties, directionVector: DimensionSegmentPropertiesList):
        """Constructor

        Args:
            dimensionPoints:                Dimension points
            placementVector:                Placement vector to the first dimension point
            directionVector:                Direction vector
            DimensionProperties:            Dimension properties
            DimensionSegmentProperties:     Dimension segment properties
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class EndSymbolsProperties():
    """Properties of start an end symbols of a ModelElement2D (line, polyline, etc...)
    """
    def __eq__(self, prop: EndSymbolsProperties) -> bool:
        """equal operator

        Args:
            prop: EndSymbolsProperties to compare

        Returns:
                  true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, startID: int, startSize: float, endID: int, endSize: float):
        """Constructor

        Args:
            startID:   ID of the start symbol
            startSize: Size of the start symbol
            endID:     ID of the end symbol
            endSize:   Size of the end symbol
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
    def EndID(self) -> None:
        """Property for end symbol ID

        :type: None
        """
    @property
    def EndSize(self) -> None:
        """Property for end symbol size

        :type: None
        """
    @property
    def StartID(self) -> None:
        """Property for start symbol ID

        :type: None
        """
    @property
    def StartSize(self) -> None:
        """Property for start symbol size

        :type: None
        """

class FaceStyleElement(BasisElement, AllplanElement):
    """Representation of the **style area** in Allplan
    """
    def GetFaceStyleProperties(self) -> FaceStyleProperties:
        """Get the face style properties

        Returns:
             face style properties
        """
    def SetFaceStyleProperties(self, faceStyleProp: FaceStyleProperties):
        """Set the FaceStyle properties

        Args:
            faceStyleProp: face style properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, faceStyleProp: FaceStyleProperties, geometryObject: object):
        """Constructor

        Args:
            commonProp:     Common properties
            faceStyleProp:  Face style properties
            geometryObject: Geometry element
        """
    @typing.overload
    def __init__(self, FaceStyleElement: FaceStyleElement):
        """Copy constructor

        Args:
            faceStyleElement:   FaceStyle element element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class FaceStyleProperties():
    """Properties of the style area
    """
    def __eq__(self, prop: FaceStyleProperties) -> bool:
        """equal operator

        Args:
            prop: FaceStyleProperties to compare

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
    def DirectionToReferenceLine(self) -> None:
        """Index of the edge of the outline polyline, to align the style area to, when the property UseDirectionToReferenceLine is set to True."""
    @property
    def FaceStyleID(self) -> None:
        """ID of style area"""
    @property
    def ReferencePoint(self) -> None:
        """the point of origin, when property UseReferencePoint is set to True"""
    @property
    def RotationAngle(self) -> None:
        """Rotation angle"""
    @property
    def UseDirectionToReferenceLine(self) -> None:
        """Whether to align the direction of the style area to a certain edge.

        When set to true, the index of the edge is to be specified in the property DirectionToReferenceLine.  
        """
    @property
    def UseReferencePoint(self) -> None:
        """Whether to use a specific point as the origin of the style area.

        When set to False, the origin is (0,0). When set to True, the point is to be specified in the
        property ReferencePoint.
        """

class FillingElement(BasisElement, AllplanElement):
    """Representation of the **filling** in Allplan
    """
    def GetFillingProperties(self) -> FillingProperties:
        """Get the filling properties

        Returns:
            Filling properties
        """
    def SetFillingProperties(self, gradientFillingProp: FillingProperties):
        """Set the filling properties

        Args:
            gradientFillingProp:  Filling properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, gradientFillingProp: FillingProperties,
                 geometryObject: object):
        """Constructor

        Args:
            commonProp:          Common properties
            gradientFillingProp: GradientFilling properties
            geometryObject:      Geometry element
        """
    @typing.overload
    def __init__(self, FillingElement: FillingElement):
        """Copy constructor

        Args:
            fillingElement:   Filling element element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class FillingProperties():
    """Properties of the filling
    """
    def __eq__(self, prop: FillingProperties) -> bool:
        """equal operator

        Args:
            prop: GradientFillingProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: FillingProperties):
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
    def DirectionToReferenceLine(self) -> int:
        """The edge index of the outline polyline to align the filling to. Relevant, when the property UseDirectionToReferenceLine is set to true."""
    @DirectionToReferenceLine.setter
    def DirectionToReferenceLine(self, directionToReferenceLine: int) -> None:
        """Set the direction to reference line state

        Args:
            directionToReferenceLine: Index of the direction line
        """
    @property
    def FirstColor(self) -> ARGB:
        """First color"""
    @FirstColor.setter
    def FirstColor(self, value: ARGB) -> None:
        """Set the first color

        Args:
            value: ARGB color value
        """
    @property
    def RotationAngle(self) -> NemAll_Python_Geometry.Angle:
        """Rotation angle. Relevant, when _UseGradientFilling_ is set to True."""
    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: NemAll_Python_Geometry.Angle) -> None:
        """Set the rotation angle

        Args:
            rotationAngle: Rotation angle: true/false
        """
    @property
    def SecondColor(self) -> ARGB:
        """Second color. Relevant, when _UseGradientFilling_ is set to True."""
    @SecondColor.setter
    def SecondColor(self, value: ARGB) -> None:
        """Set the second color

        Args:
            value: Second color
        """
    @property
    def ShadingType(self) -> Style:
        """Shading style. Relevant, when the _UseGradientFilling_ is set to True."""
    @ShadingType.setter
    def ShadingType(self, shadingType: Style) -> None:
        """Set the shading type

        Args:
            shadingType: Shading type
        """
    @property
    def TranslationType(self) -> ColorMode:
        """Color gradients type. Relevant, when _UseGradientFilling_ is set to True."""
    @TranslationType.setter
    def TranslationType(self, colorType: ColorMode) -> None:
        """Set the color type

        Args:
            colorType: Color type
        """
    @property
    def UseDirectionToReferenceLine(self) -> bool:
        """Whether to align the direction of the filling to a certain edge of the outline polyline. When set to True, the index of the edge is to be specified in _DirectionToReferenceLine_."""
    @UseDirectionToReferenceLine.setter
    def UseDirectionToReferenceLine(self, bDirectionToReferenceLine: bool) -> None:
        """Set the direction to reference line state

        Args:
            bDirectionToReferenceLine: Direction to reference line: true/false
        """
    @property
    def UseGradientFilling(self) -> bool:
        """Whether to use gradient filling."""
    @UseGradientFilling.setter
    def UseGradientFilling(self, bGradientFilling: bool) -> None:
        """Set the gradient filling

        Args:
            bGradientFilling: Gradient filling: true/false
        """
    @property
    def VariantType(self) -> Variant:
        """Gradient variant type. Relevant, when _UseGradientFilling_ is set to True."""
    @VariantType.setter
    def VariantType(self, variantType: Variant) -> None:
        """Set the variant type

        Args:
            variantType: Variant type
        """

class HatchingElement(BasisElement, AllplanElement):
    """Representation of the **hatching** in Allplan
    """
    def GetHatchingProperties(self) -> HatchingProperties:
        """Get the hatching properties

        Returns:
            Hatching properties
        """
    def SetHatchingProperties(self, hatchingProp: HatchingProperties):
        """Set the hatching properties

        Args:
            hatchingProp: Hatching properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, hatchingProp: HatchingProperties,
                 polygon: NemAll_Python_Geometry.Polygon2D):
        """Constructor

        Args:
            commonProp:   Common properties
            hatchingProp: Hatching properties
            polygon:      Geometry element
        """
    @typing.overload
    def __init__(self, element: HatchingElement):
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
    def HatchingProperties(self) -> HatchingProperties:
        """Get the hatching properties
        """
    @HatchingProperties.setter
    def HatchingProperties(self, hatchingProp: HatchingProperties) -> None:
        """Set the hatching properties

        Args:
            hatchingProp: Hatching properties
        """

class HatchingProperties():
    """Properties of the hatching
    """
    def SetBackgroundColorBGR(self, value: int):
        """Set the background color

        Args:
            value: Color value as BGR
        """
    def SetBackgroundColorIRGB(self, value: int):
        """Set the background color

        Args:
            value: Color value as IRGB
        """
    def __eq__(self, prop: HatchingProperties) -> bool:
        """equal operator

        Args:
            prop: HatchingProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: HatchingProperties):
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
    def BackgroundColor(self) -> ARGB:
        """Background color. Relevant, when _UseBackgroundColor_ is set to True."""
    @BackgroundColor.setter
    def BackgroundColor(self, value: ARGB) -> None:
        """Set the background color

        Args:
            value: ARGB color
        """
    @property
    def DirectionToReferenceLine(self) -> int:
        """The edge index of the outline polyline to align the hatching to."""
    @DirectionToReferenceLine.setter
    def DirectionToReferenceLine(self, directionToReferenceLine: int) -> None:
        """Set the direction to reference line state

        Args:
            directionToReferenceLine: Index of the direction line
        """
    @property
    def ExistAlignment(self) -> bool:
        """Whether to align the hatching to a certain edge of the outline polyline. When set to True, the index of the edge is to be specified in _DirectionToReferenceLine_."""
    @ExistAlignment.setter
    def ExistAlignment(self, bExistAlignment: bool) -> None:
        """Set the alignment state

        Args:
            bExistAlignment: Alignment exist: true/false
        """
    @property
    def HatchID(self) -> int:
        """ID of the hatch"""
    @HatchID.setter
    def HatchID(self, hatchID: int) -> None:
        """Set the hatch ID

        Args:
            hatchID: Hatch ID
        """
    @property
    def IsScaleDependent(self) -> bool:
        """Whether the hatch is to be scaled according to drawing file scale"""
    @IsScaleDependent.setter
    def IsScaleDependent(self, bScaleDependent: bool) -> None:
        """Set the scale dependent state

        Args:
            bScaleDependent: Scale dependent: true/false
        """
    @property
    def ReferencePoint(self) -> NemAll_Python_Geometry.Point2D:
        """the point of origin, when property UseReferencePoint is set to True"""
    @ReferencePoint.setter
    def ReferencePoint(self, pnt: NemAll_Python_Geometry.Point2D) -> None:
        """Set the the reference point

        Args:
            pnt: Reference point
        """
    @property
    def RotationAngle(self) -> NemAll_Python_Geometry.Angle:
        """Rotation angle"""
    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: NemAll_Python_Geometry.Angle) -> None:
        """Set the rotation angle

        Args:
            rotationAngle: Rotation angle: true/false
        """
    @property
    def UseBackgroundColor(self) -> bool:
        """Whether to use background color"""
    @UseBackgroundColor.setter
    def UseBackgroundColor(self, bUseBackgroundColor: bool) -> None:
        """Set the use background color state

        Args:
            bUseBackgroundColor: Use the background color: true/false
        """
    @property
    def UseReferencePoint(self) -> bool:
        """Whether to use a specific point as the origin of the hatching.

        When set to False, the origin is (0,0).
        When set to True, the point is to be specified in the property ReferencePoint.
        """
    @UseReferencePoint.setter
    def UseReferencePoint(self, bUseReferencePoint: bool) -> None:
        """Set the use reference point state

        Args:
            bUseReferencePoint: Use the reference point: true/false
        """

class HeightDefinitionType(enum.Enum):
    """Enumeration of height definition types of a macro placement
    """
    eAverage = 3
    """Average"""
    eComponent = 2
    """Component"""
    eMacro = 1
    """Macro"""
    eNone = 0
    """Not defined"""

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


class HiddenSectionLinesProperties():
    """Properties of hidden section lines in a UVS
    """
    def __init__(self):
        """Initialize
        """
    @property
    def HiddenSectionLinesColor(self) -> None:
        """Color ID of hidden section lines"""
    @property
    def HiddenSectionLinesLayer(self) -> None:
        """Layer ID of hidden section lines"""
    @property
    def HiddenSectionLinesLineType(self) -> None:
        """Stroke ID of hidden section lines"""
    @property
    def HiddenSectionLinesPen(self) -> None:
        """Pen ID of hidden section lines"""
    @property
    def IsHiddenSectionLinesColorFromLayer(self) -> None:
        """Whether to get the color ID from the layer definition"""
    @property
    def IsHiddenSectionLinesLineTypeFromLayer(self) -> None:
        """Whether to get the stroke ID from the layer definition"""
    @property
    def IsHiddenSectionLinesOn(self) -> None:
        """Whether to draw hidden section lines"""
    @property
    def IsHiddenSectionLinesPenFromLayer(self) -> None:
        """Whether to get the pen ID from the layer definition"""

class LabelElement(BasisElement, AllplanElement):
    """Representation of the **label** in Allplan
    """
    def AddTextElement(self, text: TextElement):
        """Add a text element

        Args:
            text: Text element
        """
    def SetLabeledElement(self, labeledElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Set the labeled element

        Args:
            labeledElement: Labeled element
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, text: TextElement, labelType: LabelType):
        """Constructor

        Args:
            text:      Text element
            labelType: Default text
        """
    @typing.overload
    def __init__(self, textElements: TextElementList, labelType: LabelType):
        """Constructor

        Args:
            textElements: Text elements
            labelType:    Label type
        """
    @typing.overload
    def __init__(self, element: LabelElement):
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
    def TextElements(self) -> TextElementList:
        """Get the text elements
        """
    @TextElements.setter
    def TextElements(self, value: TextElementList) -> None:
        """Set  the text elements
        """

class LabelType(enum.Enum):
    """Type of the label
    """
    eLabelArchDimensionLine = 3
    """Architectural dimension line"""
    eLabelBftSlabElementation = 5
    """Precast slab elementation label"""
    eLabelBftWallElementation = 4
    """Precast wall elementation label"""
    eLabelEng3DBarReinforcement = 2
    """3D reinforcement bar label"""
    eLabelNoText = 7
    """Label with no text"""
    eLabelNormalText = 0
    """Fixed text"""
    eLabelVariableText = 1
    """Variable text"""

    names = {eLabelNormalText: eLabelNormalText,
             eLabelVariableText: eLabelVariableText,
             eLabelEng3DBarReinforcement: eLabelEng3DBarReinforcement,
             eLabelArchDimensionLine: eLabelArchDimensionLine,
             eLabelBftWallElementation: eLabelBftWallElementation,
             eLabelBftSlabElementation: eLabelBftSlabElementation,
             eLabelNoText: eLabelNoText}

    values = {0: eLabelNormalText,
              1: eLabelVariableText,
              2: eLabelEng3DBarReinforcement,
              3: eLabelArchDimensionLine,
              4: eLabelBftWallElementation,
              5: eLabelBftSlabElementation,
              7: eLabelNoText}

    def __getitem__(self, key: (str | int | float)) -> LabelType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class LabelingProperties():
    """Representation of labeling settings of a UVS
    """
    def __init__(self):
        """Initialize
        """
    @property
    def AddProjectionName(self) -> None:
        """Whether to display the section identifier"""
    @property
    def HeadingOn(self) -> None:
        """Whether to display the heading"""
    @property
    def HeadingText(self) -> None:
        """Additional heading text, prior to the section identifier"""
    @property
    def IsScaleOn(self) -> None:
        """Whether to display the UVS scale"""

class LibraryElement(BasisElement, AllplanElement):
    """Representation of an **element from the Allplan library**

    An element from Allplan library can be a symbol, smart symbol or fixture.
    This class represents also fixtures from fixture catalogs

    """
    def GetCount(self) -> int:
        """Get the element count

        Returns:
            Element count
        """
    def GetGeometryElements(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> list:
        """Get the geometry elements

        Args:
            doc: Document

        Returns:
            Geometry elements
        """
    def GetMinMax(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> NemAll_Python_Geometry.MinMax3D:
        """Get the min/max box of the element

        Args:
            doc: Document

        Returns:
            Min/max box of the element
        """
    def GetProperties(self) -> LibraryElementProperties:
        """Get the properties

        Returns:
            Properties
        """
    def GetReferencePoint(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> NemAll_Python_Geometry.Point3D:
        """Get the reference point

        Args:
            doc: Document

        Returns:
            Reference point
        """
    def Move(self, moveVec: NemAll_Python_Geometry.Vector3D):
        """Move the element

        Args:
            moveVec: Move vector
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, libEleProp: LibraryElementProperties):
        """Constructor

        Args:
            libEleProp: Library element properties
        """
    @typing.overload
    def __init__(self, libEle: LibraryElement):
        """Copy constructor

        Args:
            libEle: Library element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """

class LibraryElementProperties():
    """Properties of the library element
    """
    def GetElement(self) -> str:
        """Get the element

        Returns:
            Element
        """
    def GetElementType(self) -> LibraryElementType:
        """Get the element type

        Returns:
            Element type
        """
    def GetGroup(self) -> str:
        """Get the group

        Returns:
            Group
        """
    def GetPath(self) -> str:
        """Get the path

        Returns:
            Path
        """
    def GetPlacementMatrices(self) -> NemAll_Python_Geometry.Matrix3DList:
        """Get the placement matrices

        Returns:
            Placement matrices
        """
    def GetPlacementMatrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """Get the placement matrix

        Returns:
            Placement matrix
        """
    def GetPolyline(self) -> NemAll_Python_Geometry.Polyline3D:
        """Get the polygon points in case of a line fixture

        Returns:
            Polyline points of the line fixture
        """
    def GetProducer(self) -> str:
        """Get the producer

        Returns:
            Producer
        """
    def GetSingleFilePath(self) -> str:
        """Get the Single File Path

        Returns:
            SingleFilePath
        """
    def SetPlacementMatrices(self, placementMatrices: NemAll_Python_Geometry.Matrix3DList):
        """Set the placement matrices

        Args:
            placementMatrices: Placement matrices
        """
    def SetPlacementMatrix(self, placementMatrix: NemAll_Python_Geometry.Matrix3D):
        """Set the placement matrix

        Args:
            placementMatrix: Placement matrix
        """
    def SetPolyline(self, polyline: NemAll_Python_Geometry.Polyline3D):
        """Set the polygon points in case of a line fixture

        Args:
            polyline: Polyline of a line fixture
        """
    def SetProducer(self, producer: str):
        """Set the producer

        Args:
            producer: Producer
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, fullPathName: str, elementType: LibraryElementType, placementMatrix: NemAll_Python_Geometry.Matrix3D):
        """Constructor

        Args:
            fullPathName:    Full path and file name
            elementType:     Element type
            placementMatrix: Placement matrix
        """
    @typing.overload
    def __init__(self, fullPathName: str, elementType: LibraryElementType, placementMatrices: NemAll_Python_Geometry.Matrix3DList):
        """Constructor

        Args:
            fullPathName:      Full path and file name
            elementType:       Element type
            placementMatrices: Placement matrices
        """
    @typing.overload
    def __init__(self, path: str, group: str, element: str, elementType: LibraryElementType,
                 placementMatrix: NemAll_Python_Geometry.Matrix3D):
        """Constructor

        Args:
            path:            Path name
            group:           Group name
            element:         Element name
            elementType:     Element type
            placementMatrix: Placement matrix
        """
    @typing.overload
    def __init__(self, path: str, group: str, element: str, elementType: LibraryElementType,
                 placementMatrices: NemAll_Python_Geometry.Matrix3DList):
        """Constructor

        Args:
            path:              Path name
            group:             Group name
            element:           Element name
            elementType:       Element type
            placementMatrices: Placement matrices
        """
    @typing.overload
    def __init__(self, path: str, path: str, group: str, element: str, elementType: LibraryElementType,
                 placementMatrix: NemAll_Python_Geometry.Matrix3D):
        """Constructor

        Args:
            path:            Path name
            group:           Group name
            element:         Element name
            SingleFilePath:    SingleFilePath
            elementType:     Element type
            placementMatrix: Placement matrix
        """
    @typing.overload
    def __init__(self, path: str, path: str, group: str, element: str, elementType: LibraryElementType,
                 placementMatrices: NemAll_Python_Geometry.Matrix3DList):
        """Constructor

        Args:
            path:              Path name
            group:             Group name
            element:           Element name
            SingleFilePath:    SingleFilePath
            elementType:       Element type
            placementMatrices: Placement matrices
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def PlacementMatrices(self) -> NemAll_Python_Geometry.Matrix3DList:
        """Get the placement matrices
        """
    @PlacementMatrices.setter
    def PlacementMatrices(self, placementMatrices: NemAll_Python_Geometry.Matrix3DList) -> None:
        """Set the placement matrices

        Args:
            placementMatrices: Placement matrices
        """
    @property
    def PlacementMatrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """Get the placement matrix
        """
    @PlacementMatrix.setter
    def PlacementMatrix(self, placementMatrix: NemAll_Python_Geometry.Matrix3D) -> None:
        """Set the placement matrix

        Args:
            placementMatrix: Placement matrix
        """
    @property
    def Polyline(self) -> NemAll_Python_Geometry.Polyline3D:
        """Get the polygon points in case of a line fixture
        """
    @Polyline.setter
    def Polyline(self, polyline: NemAll_Python_Geometry.Polyline3D) -> None:
        """Set the polygon points in case of a line fixture

        Args:
            polyline: Polyline of a line fixture
        """
    @property
    def Producer(self) -> str:
        """Get the producer
        """
    @Producer.setter
    def Producer(self, producer: str) -> None:
        """Set the producer

        Args:
            producer: Producer
        """

class LibraryElementType(enum.Enum):

    """Types of library elements
    """
    eFixture = 1
    """Fixture from fixture catalog"""
    eFixtureSingleFile = 3
    """Fixture from Allplan library"""
    eSmartSymbol = 0
    """Smart symbol"""
    eSymbol = 2
    """Symbol"""

    names = {eSmartSymbol: eSmartSymbol,
             eFixture: eFixture,
             eSymbol: eSymbol,
             eFixtureSingleFile: eFixtureSingleFile}

    values = {0: eSmartSymbol,
              1: eFixture,
              2: eSymbol,
              3: eFixtureSingleFile}

    def __getitem__(self, key: (str | int | float)) -> LibraryElementType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class LightProperties():
    """Light properties
    """
    def __init__(self):
        """Initialize
        """
    @property
    def ConsiderLight(self) -> bool:
        """Get the consider light
        """
    @ConsiderLight.setter
    def ConsiderLight(self, value: bool) -> None:
        """Set the consider light
        """

class LinkType(enum.Enum):
    """Definition of link type

    eLinkNothing         : Link to nothing
    eLinkToRoom          : Link to a room object
    eLinkToRoofSlab      : Link to a roof slab object
    eLinkToCeilingSurface: Link to a ceiling surface object
    eLinkToFloorSurface  : Link to a floor surface object
    """
    eLinkNothing = 0
    eLinkToCeilingSurface = 3
    eLinkToFloorSurface = 4
    eLinkToRoofSlab = 2
    eLinkToRoom = 1

    names = {eLinkNothing: eLinkNothing,
             eLinkToRoom: eLinkToRoom,
             eLinkToRoofSlab: eLinkToRoofSlab,
             eLinkToCeilingSurface: eLinkToCeilingSurface,
             eLinkToFloorSurface: eLinkToFloorSurface}

    values = {0: eLinkNothing,
              1: eLinkToRoom,
              2: eLinkToRoofSlab,
              3: eLinkToCeilingSurface,
              4: eLinkToFloorSurface}

    def __getitem__(self, key: (str | int | float)) -> LinkType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class MacroElement(BasisElement, AllplanElement):
    """Representation of the **macro definition (smart symbol)** in Allplan
    """
    def GetAttributesForSubElementInStrucutredContainer(self, subElementID: type) -> object:
        """Get attributes for sub element in StructuredContainer

        Args:
            subElementID: Sub element id
            tributeSet
        """
    def GetHash(self) -> str:
        """Get the hash value

        Returns:
             Hash value
        """
    def GetMacroProperties(self) -> MacroProperties:
        """Get the Macro properties

        Returns:
             Macro properties
        """
    def GetSlideList(self) -> list:
        """Get the slide object list

        Returns:
             Slide object list
        """
    def SetAttributesForSubElementInStrucutredContainer(self, attributeContainer: object, subElementID: type):
        """Set attributes to sub element in StructuredContainer

        Args:
            attributeContainer: AttributeSet
            subElementID:       Sub element id
        """
    def SetHash(self, hash: str):
        """Set the hash value

        Args:
            hash:Hash value
        """
    def SetMacroProperties(self, MacroProp: MacroProperties):
        """Set the Macro properties

        Args:
            MacroProp: Macro properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, macroProp: MacroProperties, slideList: list):
        """Constructor

        Args:
            macroProp:      Macro properties
            slideList:      Slide list of macro definition
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class MacroGroupElement(BasisElement, AllplanElement):
    """Representation of the **macro group** (group of smart symbols) in Allplan
    """
    def GetGeometryParameterValueList(self) -> list:
        """Get the geometry parameter value list

        Returns:
            Geometry parameter value list
        """
    def GetMacroGroupProperties(self) -> MacroGroupProperties:
        """Get the macro group properties

        Returns:
            MacroGroup properties
        """
    def GetPlacementList(self) -> typing.List[MacroPlacementElement]:
        """Get the placement list

        Returns:
            Placements of macro group
        """
    def SetGeometryParameterValueList(self, geometryParameterValueList: list):
        """Set the geometry parameter value list

        Args:
            geometryParameterValueList: Geometry parameter value list
        """
    def SetMacroGroupProperties(self, macroGroupProp: MacroGroupProperties):
        """Set the macro group properties

        Args:
            macroGroupProp: MacroGroup properties
        """
    def TransformElement(self, transMat: NemAll_Python_Geometry.Matrix3D):
        """Args:
            transMat
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, macroGroupProp: MacroGroupProperties, placementList: list):
        """Constructor

        Args:
            macroGroupProp: MacroGroup properties
            placementList:  typing.List[MacroPlacementElement]    Placements list of macro group
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, macroGroupProp: MacroGroupProperties, placementList: list):
        """Constructor

        Args:
            commonProp:     Common properties
            macroGroupProp: MacroGroup properties
            placementList:  typing.List[MacroPlacementElement]   Placements list of macro group
        """
    @typing.overload
    def __init__(self, element: MacroGroupElement):
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
    def GeometryParameterValueList(self) -> list:
        """Get the geometry parameter value list
        """
    @GeometryParameterValueList.setter
    def GeometryParameterValueList(self, geometryParameterValueList: list) -> None:
        """Set the geometry parameter value list

        Args:
            geometryParameterValueList: Geometry parameter value list
        """
    @property
    def MacroGroupProperties(self) -> MacroGroupProperties:
        """Get the macro group properties
        """
    @MacroGroupProperties.setter
    def MacroGroupProperties(self, macroGroupProp: MacroGroupProperties) -> None:
        """Set the macro group properties

        Args:
            macroGroupProp: MacroGroup properties
        """

class MacroGroupProperties():
    """Properties of the macro group.
    """
    def __eq__(self, prop: MacroGroupProperties) -> bool:
        """equal operator

        Args:
            prop: MacroGroupProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: MacroGroupProperties):
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
    def Name(self) -> str:
        """Name"""
    @Name.setter
    def Name(self, value: str) -> None:
        """Set the Name
        """

class MacroPlacementElement(BasisElement, AllplanElement):
    """Representation of the **macro placement**. In Allplan referred to as _instance of a smart symbol_
    """
    def GetArchitectureElementsList(self) -> list:
        """Get the architecture elements

        Returns:
            Architecture elements
        """
    def GetAssemblyGoupList(self) -> list:
        """Get the assembly group elements

        Returns:
            Assembly group elements
        """
    def GetAttributesList(self) -> typing.List[NemAll_Python_BaseElements.AttributeSet]:
        """Get the attributes list

        Returns:
            Attributes list
        """
    def GetFixtureElementsList(self) -> list:
        """Get the fixture elements

        Returns:
            Fixture elements
        """
    def GetGeometryParameterValueList(self) -> list:
        """Get the geometry parameter value list

        Returns:
            Geometry parameter value list
        """
    def GetLibraryElementsList(self) -> list:
        """Get the library elements

        Returns:
            Library elements
        """
    def GetMacro(self) -> MacroElement:
        """Get the corresponding macro definition

        Returns:
            Macro definition element
        """
    def GetMacroPlacementProperties(self) -> MacroPlacementProperties:
        """Get the macro placement properties

        Returns:
            MacroPlacement properties
        """
    def GetPrecastMWSList(self) -> list:
        """Get the Precast MWS elements

        Returns:
            Precast MWS elements
        """
    def GetReinforcementList(self) -> list:
        """Get the reinforcement elements

        Returns:
            Reinforcement elements
        """
    def SetGeometryParameterValueList(self, geometryParameterValueList: list):
        """Set the geometry parameter value list

        Args:
            geometryParameterValueList: Geometry parameter value list
        """
    def SetMacroPlacementProperties(self, macroPlacementProp: MacroPlacementProperties):
        """Set the macro placement properties

        Args:
            macroPlacementProp: MacroPlacement properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, macroPlacementProp: MacroPlacementProperties, macro: object,
                 reinforcementList: list, libraryElementList: list = [], architectureElementsList: list = [], fixtureElementsList: list = [], assemblyGroupList: list = [], precastMWSList: list = []):
        """Constructor

        Args:
            commonProp:               Common properties
            macroPlacementProp:       MacroPlacement properties
            macro:                    Macro definition element
            reinforcementList:        Reinforcement elements
            libraryElementList:       Library elements list
            architectureElementsList: Architecture elements list
            fixtureElementsList:      Fixture elements list
            assemblyGroupList:        Assembly group list
            precastMWSList:           Precas MWS list
        """
    @typing.overload
    def __init__(self, placement: MacroPlacementElement):
        """Copy constructor

        Args:
            placement: Placement to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def GeometryParameterValueList(self) -> list:
        """Get the geometry parameter value list
        """
    @GeometryParameterValueList.setter
    def GeometryParameterValueList(self, geometryParameterValueList: list) -> None:
        """Set the geometry parameter value list

        Args:
            geometryParameterValueList: Geometry parameter value list
        """
    @property
    def MacroPlacementProperties(self) -> MacroPlacementProperties:
        """Properties of the macro placement"""
    @MacroPlacementProperties.setter
    def MacroPlacementProperties(self, macroPlacementProp: MacroPlacementProperties) -> None:
        """Set the macro placement properties

        Args:
            macroPlacementProp: MacroPlacement properties
        """

class MacroPlacementProperties():
    """Properties of the macro placement
    """
    def __eq__(self, prop: MacroPlacementProperties) -> bool:
        """equal operator

        Args:
            prop: MacroPlacementProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: MacroPlacementProperties):
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
    def BillingCategory(self) -> int:
        """Get the Billing category
        """
    @BillingCategory.setter
    def BillingCategory(self, value: int) -> None:
        """Set the Billing category
        """
    @property
    def ConsiderType(self) -> ConsiderType:
        """The type of adaptation behavior of the smart symbol relative to finishing surfaces"""
    @ConsiderType.setter
    def ConsiderType(self, value: ConsiderType) -> None:
        """Set the Consider type
        """
    @property
    def Craft(self) -> int:
        """Get the Craft
        """
    @Craft.setter
    def Craft(self, value: int) -> None:
        """Set the Craft
        """
    @property
    def DistortionState(self) -> bool:
        """Whether to allow the resize of the smart symbol"""
    @DistortionState.setter
    def DistortionState(self, value: bool) -> None:
        """Set the Distortion state
        """
    @property
    def DomainType(self) -> int:
        """Get the Domain type?
        """
    @DomainType.setter
    def DomainType(self, value: int) -> None:
        """Set the Domain type?
        """
    @property
    def HasParentModificationBehaviour(self) -> bool:
        """Get the Specific behavior for modification
        """
    @HasParentModificationBehaviour.setter
    def HasParentModificationBehaviour(self, value: bool) -> None:
        """Set the Specific behavior for modification
        """
    @property
    def HeightDefinitionType(self) -> HeightDefinitionType:
        """Get the Height definition type
        """
    @HeightDefinitionType.setter
    def HeightDefinitionType(self, value: HeightDefinitionType) -> None:
        """Set the Height definition type
        """
    @property
    def InOpeningState(self) -> bool:
        """Get the Is the macro placement inside opening ?
        """
    @InOpeningState.setter
    def InOpeningState(self, value: bool) -> None:
        """Set the Is the macro placement inside opening ?
        """
    @property
    def LeadingMacro(self) -> bool:
        """Is the macro placement a leading macro"""
    @LeadingMacro.setter
    def LeadingMacro(self, value: bool) -> None:
        """Set the leading macro (post activation flag for connected elements - iseg1)
        """
    @property
    def LinkType(self) -> LinkType:
        """Get the Link type
        """
    @LinkType.setter
    def LinkType(self, value: LinkType) -> None:
        """Set the Link type
        """
    @property
    def Mass_V6(self) -> float:
        """Get the Mass attribute V6
        """
    @Mass_V6.setter
    def Mass_V6(self, value: float) -> None:
        """Set the Mass attribute V6
        """
    @property
    def Mass_V7(self) -> float:
        """Get the Mass attribute V7
        """
    @Mass_V7.setter
    def Mass_V7(self, value: float) -> None:
        """Set the Mass attribute V7
        """
    @property
    def Mass_V8(self) -> float:
        """Get the Mass attribute V8
        """
    @Mass_V8.setter
    def Mass_V8(self, value: float) -> None:
        """Set the Mass attribute V8
        """
    @property
    def Mass_V9(self) -> float:
        """Get the Mass attribute V9
        """
    @Mass_V9.setter
    def Mass_V9(self, value: float) -> None:
        """Set the Mass attribute V9
        """
    @property
    def Matrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """Get the Matrix for location in world coordinate system
        """
    @Matrix.setter
    def Matrix(self, value: NemAll_Python_Geometry.Matrix3D) -> None:
        """Set the Matrix for location in world coordinate system
        """
    @property
    def MirrorState(self) -> bool:
        """Get the Was the macro placement mirrored ?
        """
    @MirrorState.setter
    def MirrorState(self, value: bool) -> None:
        """Set the Was the macro placement mirrored ?
        """
    @property
    def Name(self) -> str:
        """Get the Name
        """
    @Name.setter
    def Name(self, value: str) -> None:
        """Set the Name
        """
    @property
    def PositionNr(self) -> int:
        """Get the Unit factor
        """
    @PositionNr.setter
    def PositionNr(self, value: int) -> None:
        """Set the Unit factor
        """
    @property
    def SubType(self) -> int:
        """Get the Subtype?
        """
    @SubType.setter
    def SubType(self, value: int) -> None:
        """Set the Subtype?
        """
    @property
    def Type(self) -> int:
        """Get the Type?
        """
    @Type.setter
    def Type(self, value: int) -> None:
        """Set the Type?
        """
    @property
    def UnitFactor(self) -> float:
        """Get the Unit factor
        """
    @UnitFactor.setter
    def UnitFactor(self, value: float) -> None:
        """Set the Unit factor
        """
    @property
    def UseAlways2DRepInGroundView(self) -> bool:
        """Get the Use always 2D representation in ground view
        """
    @UseAlways2DRepInGroundView.setter
    def UseAlways2DRepInGroundView(self, value: bool) -> None:
        """Set the Use always 2D representation in ground view
        """
    @property
    def UseDrawOrder(self) -> bool:
        """Set to True to use the draw order (sequence) setting of the smart symbol's instance. Set to False to use the setting of elements included in the macro slide"""
    @UseDrawOrder.setter
    def UseDrawOrder(self, value: bool) -> None:
        """Set the Uses the draw order setting of the placement or the elements of the macro ?
        """
    @property
    def UseFormat(self) -> bool:
        """Set to True to use the format setting (pen, stroke, color) of the smart symbol's instance. Set to False to use the settings of the elements included in the macro slide."""
    @UseFormat.setter
    def UseFormat(self, value: bool) -> None:
        """Set the Uses the format setting (pen, stroke, color) of the placement or the elements of the macro ?
        """

class MacroProperties():
    """Properties of the macro definition
    """
    def __eq__(self, prop: MacroProperties) -> bool:
        """equal operator

        Args:
            prop: MacroProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: MacroProperties):
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
    def CatalogName(self) -> str:
        """Get the Catalog name
        """
    @CatalogName.setter
    def CatalogName(self, value: str) -> None:
        """Set the Catalog name
        """
    @property
    def DomainType(self) -> int:
        """Get the Domain type
        """
    @DomainType.setter
    def DomainType(self, value: int) -> None:
        """Set the Domain type
        """
    @property
    def InsertionPoint(self) -> NemAll_Python_Geometry.Point3D:
        """Macro reference point"""
    @InsertionPoint.setter
    def InsertionPoint(self, value: NemAll_Python_Geometry.Point3D) -> None:
        """Set the Insertion point
        """
    @property
    def IsScaleDependent(self) -> bool:
        """Whether the macro should be scale dependent"""
    @IsScaleDependent.setter
    def IsScaleDependent(self, value: bool) -> None:
        """Set the Is macro scale dependent ?
        """
    @property
    def Name(self) -> str:
        """Get the Name
        """
    @Name.setter
    def Name(self, value: str) -> None:
        """Set the Name
        """
    @property
    def PositionNr(self) -> int:
        """Get the Position number
        """
    @PositionNr.setter
    def PositionNr(self, value: int) -> None:
        """Set the Position number
        """
    @property
    def SubType(self) -> int:
        """Get the Sub type
        """
    @SubType.setter
    def SubType(self, value: int) -> None:
        """Set the Sub type
        """
    @property
    def UnitFactor(self) -> float:
        """Get the Unit factor
        """
    @UnitFactor.setter
    def UnitFactor(self, value: float) -> None:
        """Set the Unit factor
        """

class MacroSlideElement(BasisElement, AllplanElement):
    """Representation of a **macro slide**. In Allplan referred to as _foil of a smart symbol_
    """
    def GetMacroSlideProperties(self) -> MacroSlideProperties:
        """Get the MacroSlide properties

        Returns:
             MacroSlide properties
        """
    def GetObjectList(self) -> list:
        """Get the slide object list

        Returns:
             Slide object list
        """
    def SetMacroSlideProperties(self, MacroSlideProp: MacroSlideProperties):
        """Set the MacroSlide properties

        Args:
            MacroSlideProp: MacroSlide properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, macroSlideProp: MacroSlideProperties, objectList: list):
        """Constructor

        Args:
            macroSlideProp: MacroSlide properties
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

class MacroSlideProperties():
    """Properties of the macro slide
    """
    def __eq__(self, prop: MacroSlideProperties) -> bool:
        """equal operator

        Args:
            prop: MacroSlideProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: MacroSlideProperties):
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
    def AllDrawingTypes(self) -> bool:
        """Get the all drawing types state
        """
    @AllDrawingTypes.setter
    def AllDrawingTypes(self, allDrawingTypes: bool) -> None:
        """Set the all drawing types state

        Args:
            allDrawingTypes: All drawing types state
        """
    @property
    def DrawingTypes(self) -> (list[int] | NemAll_Python_Utility.VecIntList):
        """Get the drawing types
        """
    @DrawingTypes.setter
    def DrawingTypes(self, drawingTypes: (list[int] | NemAll_Python_Utility.VecIntList)) -> None:
        """Set the drawing types

        Args:
            drawingTypes: Drawing types
        """
    @property
    def EndScaleRange(self) -> float:
        """The upper limit of the scale range in which the slide will be drawn"""
    @EndScaleRange.setter
    def EndScaleRange(self, value: float) -> None:
        """Set the Start reference scale of slide
        """
    @property
    def OffsetOfReferencePoint1(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the First offset value to reference point
        """
    @OffsetOfReferencePoint1.setter
    def OffsetOfReferencePoint1(self, value: NemAll_Python_Geometry.Vector3D) -> None:
        """Set the First offset value to reference point
        """
    @property
    def OffsetOfReferencePoint2(self) -> NemAll_Python_Geometry.Vector3D:
        """Get the Second offset value to reference point
        """
    @OffsetOfReferencePoint2.setter
    def OffsetOfReferencePoint2(self, value: NemAll_Python_Geometry.Vector3D) -> None:
        """Set the Second offset value to reference point
        """
    @property
    def ReferencePoint(self) -> NemAll_Python_Geometry.Point3D:
        """Get the Reference point of this slide
        """
    @ReferencePoint.setter
    def ReferencePoint(self, value: NemAll_Python_Geometry.Point3D) -> None:
        """Set the Reference point of this slide
        """
    @property
    def ResizeSettingVx(self) -> CombinationType:
        """The resizing combination setting for x direction"""
    @ResizeSettingVx.setter
    def ResizeSettingVx(self, value: CombinationType) -> None:
        """Set the Resize setting for x direction
        """
    @property
    def ResizeSettingVy(self) -> CombinationType:
        """The resizing combination setting for y direction"""
    @ResizeSettingVy.setter
    def ResizeSettingVy(self, value: CombinationType) -> None:
        """Set the Resize setting for y direction
        """
    @property
    def ResizeSettingVz(self) -> CombinationType:
        """The resizing combination setting for z direction"""
    @ResizeSettingVz.setter
    def ResizeSettingVz(self, value: CombinationType) -> None:
        """Set the Resize setting for z direction
        """
    @property
    def StartScaleRange(self) -> float:
        """The lower limit of the scale range in which the slide will be drawn"""
    @StartScaleRange.setter
    def StartScaleRange(self, value: float) -> None:
        """Set the Start reference scale of slide
        """
    @property
    def Type(self) -> MacroSlideType:
        """Get the Type of macro slide
        """
    @Type.setter
    def Type(self, value: MacroSlideType) -> None:
        """Set the Type of macro slide
        """
    @property
    def VisibilityGeo2D(self) -> bool:
        """Whether the slide should be considered as 2D element (ex. to be visible in ground view)"""
    @VisibilityGeo2D.setter
    def VisibilityGeo2D(self, value: bool) -> None:
        """Set the Geometry 2D visibility of slide
        """
    @property
    def VisibilityGeo3D(self) -> bool:
        """Whether the slide should be considered as 3D element (ex. to be visible in isometric view)"""
    @VisibilityGeo3D.setter
    def VisibilityGeo3D(self, value: bool) -> None:
        """Set the Geometry 3D visibility of slide
        """
    @property
    def VisibilityLayerA(self) -> bool:
        """Whether the slide should be visible on the smart symbol foil A"""
    @VisibilityLayerA.setter
    def VisibilityLayerA(self, value: bool) -> None:
        """Set the Layer A visibility of slide
        """
    @property
    def VisibilityLayerB(self) -> bool:
        """Whether the slide should be visible on the smart symbol foil B"""
    @VisibilityLayerB.setter
    def VisibilityLayerB(self, value: bool) -> None:
        """Set the Layer B visibility of slide
        """
    @property
    def VisibilityLayerC(self) -> bool:
        """Whether the slide should be visible on the smart symbol foil C"""
    @VisibilityLayerC.setter
    def VisibilityLayerC(self, value: bool) -> None:
        """Set the Layer C visibility of slide
        """

class MacroSlideType(enum.Enum):
    """Definition of the macro slide type

    eGeometry           : Macro slide has type geometry
    eCode               : Macro slide has type code
    eReinforcement      : Macro slide has type reinforcement
    eReport             : Macro slide has type report
    eUndergroundCadaster: Macro slide has type underground cadaster
    eExtension          : Macro slide has type extension
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

    def __getitem__(self, key: (str | int | float)) -> MacroSlideType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ModelElement2D(BasisElement, AllplanElement):
    """Representation of a general two-dimensional model element, such as line, arc or polyline.
    """
    def GetEndSymbolsProperties(self) -> EndSymbolsProperties:
        """Get the end symbols properties

        Returns:
            End symbols properties
        """
    def GetPatternCurveProperties(self) -> PatternCurveProperties:
        """Get the pattern curve properties

        Returns:
            Pattern curve properties
        """
    def GetTransformationList(self) -> list:
        """Get transformation list

        Returns:
            List with the transformations
        """
    def SetEndSymbolsProperties(self, endSymbolsProp: EndSymbolsProperties):
        """Set the end symbols properties

        Args:
            endSymbolsProp: End symbols properties
        """
    def SetPatternCurveProperties(self, patternCurveProp: PatternCurveProperties):
        """Set the pattern curve properties

        Args:
            patternCurveProp: Pattern curve properties
        """
    def SetTransformationList(self, transformationList: list):
        """Set the transformation list

        Args:
            transformationList: List with the transformations
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, geometryObject: object):
        """Constructor

        Args:
            commonProp:     Common properties
            geometryObject: Geometry element
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, patternCurveProp: PatternCurveProperties,
                 endSymbolProp: EndSymbolsProperties, geometryObject: object):
        """Constructor

        Args:
            commonProp:       Common properties
            patternCurveProp: End symbols properties
            endSymbolProp:    Pattern curve properties
            geometryObject:   Geometry element
        """
    @typing.overload
    def __init__(self, element: ModelElement2D):
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
    def EndSymbolsProperties(self) -> EndSymbolsProperties:
        """Get the end symbols properties
        """
    @EndSymbolsProperties.setter
    def EndSymbolsProperties(self, value: EndSymbolsProperties) -> None:
        """Set the end symbols properties
        """
    @property
    def PatternCurveProperties(self) -> PatternCurveProperties:
        """Get the pattern curve properties
        """
    @PatternCurveProperties.setter
    def PatternCurveProperties(self, value: PatternCurveProperties) -> None:
        """Set the pattern curve properties
        """
    @property
    def TransformationList(self) -> list:
        """Get transformation list
        """
    @TransformationList.setter
    def TransformationList(self, value: list) -> None:
        """Set the transformation list
        """

class ModelElement3D(BasisElement, AllplanElement):
    """Representation of a general three-dimensional model element, such as 3D curve, surface or solid
    """
    def GetTextureDefinition(self) -> TextureDefinition:
        """Get the texture definition

        Returns:
            Texture definition (surface filename)
        """
    def GetTextureMapping(self) -> TextureMapping:
        """Get the texture mapping

        Returns:
            Texture mapping properties
        """
    def GetTransformationList(self) -> list:
        """Get transformation list

        Returns:
            List with the transformations
        """
    def IsValidateGeometry(self) -> bool:
        """Get the validate geometry state

        Returns:
            Validate the geometry state
        """
    def SetTextureDefinition(self, textureDefinition: TextureDefinition):
        """Set the texture definition

        Args:
            textureDefinition: Texture definition (surface filename)
        """
    def SetTextureMapping(self, textureMapping: TextureMapping):
        """Set the texture mapping

        Args:
            textureMapping: Texture mapping properties
        """
    def SetTransformationList(self, transformationList: list):
        """Set the transformation list

        Args:
            transformationList: List with the transformations
        """
    def SetValidateGeometry(self, validateGeometry: bool):
        """Set the validate geometry state

        Args:
            validateGeometry: Validate the geometry
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, geometryObject: object):
        """Constructor

        Args:
            commonProp:     Common properties
            geometryObject: Geometry element
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, BrepIsoLinesU: int, BrepIsoLinesV: int,
                 geometryObject: object):
        """Constructor

        Args:
            commonProp:     Common properties
            BrepIsoLinesU:  Count of Isolines U for a Berep
            BrepIsoLinesV:  Count of Isolines V for a Berep
            geometryObject: Geometry element
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, textureDefinition: TextureDefinition,
                 geometryObject: object):
        """Constructor

        Args:
            commonProp:        Common properties
            textureDefinition: Texture definition (surface filename)
            geometryObject:    Geometry element
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, textureDefinition: TextureDefinition, BrepIsoLinesU: int,
                 BrepIsoLinesV: int, geometryObject: object):
        """Constructor

        Args:
            commonProp:        Common properties
            textureDefinition: Texture definition (surface filename)
            BrepIsoLinesU:     Count of Isolines U for a Berep
            BrepIsoLinesV:     Count of Isolines V for a Berep
            geometryObject:    Geometry element
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, textureDefinition: TextureDefinition,
                 textureMapping: TextureMapping, geometryObject: object):
        """Constructor

        Args:
            commonProp:        Common properties
            textureDefinition: Texture definition (surface filename)
            textureMapping:    Texture mapping properties
            geometryObject:    Geometry element
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, textureDefinition: TextureDefinition,
                 textureMapping: TextureMapping, BrepIsoLinesU: int, BrepIsoLinesV: int, geometryObject: object):
        """Constructor

        Args:
            commonProp:        Common properties
            textureDefinition: Texture definition (surface filename)
            textureMapping:    Texture mapping properties
            BrepIsoLinesU:     Count of Isolines U for a Berep
            BrepIsoLinesV:     Count of Isolines V for a Berep
            geometryObject:    Geometry element
        """
    @typing.overload
    def __init__(self, element: ModelElement3D):
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
    def TextureDefinition(self) -> TextureDefinition:
        """Get the texture definition
        """
    @TextureDefinition.setter
    def TextureDefinition(self, value: TextureDefinition) -> None:
        """Set the texture definition
        """
    @property
    def TextureMapping(self) -> TextureMappingProperties:
        """Get the texture mapping
        """
    @TextureMapping.setter
    def TextureMapping(self, value: TextureMappingProperties) -> None:
        """Set the texture mapping
        """
    @property
    def TransformationList(self) -> list:
        """Get transformation list
        """
    @TransformationList.setter
    def TransformationList(self, value: list) -> None:
        """Set the transformation list
        """

class PatternCurveAlignment(enum.Enum):
    """Pattern curve alignment types of the pattern curve property
    """
    eCenter = 1
    eLeft = 0
    eRight = 2

    names = {eLeft: eLeft,
             eCenter: eCenter,
             eRight: eRight}

    values = {0: eLeft,
              1: eCenter,
              2: eRight}

    def __getitem__(self, key: (str | int | float)) -> PatternCurveAlignment:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PatternCurveIntersectionType(enum.Enum):
    """Pattern intersection types of the pattern curve property
    """
    eDisabled = 0
    eJoint = 2
    eMiter = 1
    eSeamless = 3

    names = {eDisabled: eDisabled,
             eMiter: eMiter,
             eJoint: eJoint,
             eSeamless: eSeamless}

    values = {0: eDisabled,
              1: eMiter,
              2: eJoint,
              3: eSeamless}

    def __getitem__(self, key: (str | int | float)) -> PatternCurveIntersectionType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PatternCurveProperties():
    """PatternCurveProperties class
    """
    def __eq__(self, prop: PatternCurveProperties) -> bool:
        """equal operator

        Args:
            prop: PatternCurveProperties to compare

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
    def AlignmentType(self) -> None:
        """the position of the pattern relative to the reference curve"""
    @property
    def Height(self) -> None:
        """Property for height of pattern

        :type: None
        """
    @property
    def IntersectionType(self) -> None:
        """Property for intersection type

        :type: None
        """
    @property
    def IsDrawReferenceCurve(self) -> None:
        """Whether to draw the reference curve"""
    @property
    def IsLockedToCorner(self) -> None:
        """Whether to lock the corner"""
    @property
    def IsMirrorPattern(self) -> None:
        """Whether to mirror the pattern"""
    @property
    def IsScaleDependent(self) -> None:
        """Whether the pattern is to be scale dependent"""
    @property
    def PatternID(self) -> None:
        """Property for pattern ID

        :type: None
        """
    @property
    def Width(self) -> None:
        """Property for width of pattern

        :type: None
        """

class PatternElement(BasisElement, AllplanElement):
    """Representation of **pattern** in Allplan
    """
    def GetPatternProperties(self) -> PatternProperties:
        """Get the Pattern properties

        Returns:
            Pattern properties
        """
    def SetPatternProperties(self, patternProp: PatternProperties):
        """Set the Pattern properties

        Args:
            patternProp: Pattern properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, patternProp: PatternProperties,
                 polygon: NemAll_Python_Geometry.Polygon2D):
        """Constructor

        Args:
            commonProp:  Common properties
            patternProp: Pattern properties
            polygon:     Geometry element
        """
    @typing.overload
    def __init__(self, element: PatternElement):
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
    def PatternProperties(self) -> PatternProperties:
        """Get the Pattern properties
        """
    @PatternProperties.setter
    def PatternProperties(self, patternProp: PatternProperties) -> None:
        """Set the Pattern properties

        Args:
            patternProp: Pattern properties
        """

class PatternProperties():
    """Properties of the pattern
    """
    def SetBackgroundColorBGR(self, value: int):
        """Set the background color

        Args:
            value: Color value as BGR
        """
    def SetBackgroundColorIRGB(self, value: int):
        """Set the background color

        Args:
            value: Color value as IRGB
        """
    def __eq__(self, prop: PatternProperties) -> bool:
        """equal operator

        Args:
            prop: PatternProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: PatternProperties):
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
    def BackgroundColor(self) -> ARGB:
        """Background color. Relevant if _UseBackgroundColor_ is set to True"""
    @BackgroundColor.setter
    def BackgroundColor(self, value: ARGB) -> None:
        """Set the background color

        Args:
            value: ARGB color
        """
    @property
    def IsScaleDependent(self) -> bool:
        """Whether the pattern is to be scale dependent"""
    @IsScaleDependent.setter
    def IsScaleDependent(self, bScaleDependent: bool) -> None:
        """Set the scale dependent state

        Args:
            bScaleDependent: Scale dependent: true/false
        """
    @property
    def PatternID(self) -> int:
        """Get the pattern ID
        """
    @PatternID.setter
    def PatternID(self, patternID: int) -> None:
        """Set the pattern ID

        Args:
            patternID: Pattern ID
        """
    @property
    def PlacementType(self) -> PlacementType:
        """Placing mode"""
    @PlacementType.setter
    def PlacementType(self, placement: PlacementType) -> None:
        """Set the placement type

        Args:
            placement: Placement type
        """
    @property
    def ReferencePoint(self) -> NemAll_Python_Geometry.Point2D:
        """reference point. Relevant if _UseReferencePoint_ is set to True."""
    @ReferencePoint.setter
    def ReferencePoint(self, pnt: NemAll_Python_Geometry.Point2D) -> None:
        """Set the the reference point

        Args:
            pnt: Reference point
        """
    @property
    def RotationAngle(self) -> NemAll_Python_Geometry.Angle:
        """Rotation angle"""
    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: NemAll_Python_Geometry.Angle) -> None:
        """Set the rotation angle

        Args:
            rotationAngle: Rotation angle
        """
    @property
    def UseBackgroundColor(self) -> bool:
        """Whether to use a background color in the pattern"""
    @UseBackgroundColor.setter
    def UseBackgroundColor(self, bUseBackgroundColor: bool) -> None:
        """Set the use background color state

        Args:
            bUseBackgroundColor: Use the background color: true/false
        """
    @property
    def UseReferencePoint(self) -> bool:
        """Whether to use the reference point from _ReferencePoint_ property for the pattern origin"""
    @UseReferencePoint.setter
    def UseReferencePoint(self, bUseReferencePoint: bool) -> None:
        """Set the use reference point state

        Args:
            bUseReferencePoint: Use the reference point: true/false
        """
    @property
    def XScalingFactor(self) -> float:
        """Get the scaling factor in x direction
        """
    @XScalingFactor.setter
    def XScalingFactor(self, scalingFactorX: float) -> None:
        """Set the scaling factor in x direction

        Args:
            scalingFactorX: Scaling factor in x direction
        """
    @property
    def YScalingFactor(self) -> float:
        """Get the scaling factor in y direction
        """
    @YScalingFactor.setter
    def YScalingFactor(self, scalingFactorY: float) -> None:
        """Set the scaling factor in y direction

        Args:
            scalingFactorY: Scaling factor in y direction
        """

class PlacementType(enum.Enum):
    """Trimming modes of a pattern (PatternElement)
    """
    eFitting = 1
    """Trim pattern along boundary"""
    eInsideFitting = 2
    """Trim pattern to full segments"""
    eOutsideFitting = 0
    """No trim"""

    names = {eOutsideFitting: eOutsideFitting,
             eFitting: eFitting,
             eInsideFitting: eInsideFitting}

    values = {0: eOutsideFitting,
              1: eFitting,
              2: eInsideFitting}

    def __getitem__(self, key: (str | int | float)) -> PlacementType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ScaleProperties():
    """Scale properties
    """
    def __init__(self):
        """Initialize
        """
    @property
    def Factor_X_direction(self) -> float:
        """Property for factor for x-direction
        """
    @Factor_X_direction.setter
    def Factor_X_direction(self, value: float) -> None:
        """Property for factor for x-direction
        """
    @property
    def Factor_Y_direction(self) -> float:
        """Property for factor for y-direction
        """
    @Factor_Y_direction.setter
    def Factor_Y_direction(self, value: float) -> None:
        """Property for factor for y-direction
        """

class SectionAlongPathClippingPathProperties():
    """Clipping path properties
    """
    @staticmethod
    def GetClippingPathGeometryTolerance() -> float:
        """Access tolerances

        Returns:
            ClippingPathGeometryTolerance
        """
    def GetPathLength(self) -> float:
        """Get length of path
        """
    def GetResultPathLength(self) -> float:
        """Get length of the part of path limited by EndCoord and StartCoord
        """
    def RestrictEmptySectionId(self):
        """
        """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathClippingPathProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def BottomLevel(self) -> float:
        """Get the BottomLevel for section Vertical or Horizontal_From_Top
        """
    @BottomLevel.setter
    def BottomLevel(self, value: float) -> None:
        """Set the BottomLevel for section Vertical or Horizontal_From_Top
        """
    @property
    def ClippingPathViewProperties(self) -> SectionAlongPathClippingPathViewProperties:
        """Get the SectionAlongPathClippingPathViewProperties
        """
    @ClippingPathViewProperties.setter
    def ClippingPathViewProperties(self, value: SectionAlongPathClippingPathViewProperties) -> None:
        """Set the SectionAlongPathClippingPathViewProperties
        """
    @property
    def EndCoord(self) -> float:
        """Get the EndCoord value
        """
    @EndCoord.setter
    def EndCoord(self, value: float) -> None:
        """Set the EndCoord value
        """
    @property
    def IsChangeViewDirectionOn(self) -> bool:
        """Get the IsChangeViewDirectionOn status : ON/OFF
        """
    @IsChangeViewDirectionOn.setter
    def IsChangeViewDirectionOn(self, value: bool) -> None:
        """Set the IsChangeViewDirectionOn status : ON/OFF
        """
    @property
    def IsClippingLineOn(self) -> bool:
        """Get the Is clipping path line on
        """
    @IsClippingLineOn.setter
    def IsClippingLineOn(self, value: bool) -> None:
        """Set the Is clipping path line on
        """
    @property
    def IsHeightFromElementOn(self) -> bool:
        """Get the IsHeightFromElementOn status : ON/OFF
        """
    @IsHeightFromElementOn.setter
    def IsHeightFromElementOn(self, value: bool) -> None:
        """Set the IsHeightFromElementOn status : ON/OFF
        """
    @property
    def SectionIdentifier(self) -> str:
        """Get the Section identifier
        """
    @SectionIdentifier.setter
    def SectionIdentifier(self, value: str) -> None:
        """Set the Section identifier
        """
    @property
    def StartCoord(self) -> float:
        """Get the StartCoord value
        """
    @StartCoord.setter
    def StartCoord(self, value: float) -> None:
        """Set the StartCoord value
        """
    @property
    def StationingEnd(self) -> float:
        """Get end stationing
        """
    @StationingEnd.setter
    def StationingEnd(self, value: float) -> None:
        """Set end stationing
        """
    @property
    def StationingStart(self) -> float:
        """Get start stationing
        """
    @StationingStart.setter
    def StationingStart(self, value: float) -> None:
        """Set start stationing
        """
    @property
    def TopLevel(self) -> float:
        """Get the TopLevel for section Vertical  or Horizontal_From_Bottom
        """
    @TopLevel.setter
    def TopLevel(self, value: float) -> None:
        """Set the TopLevel for section Vertical  or Horizontal_From_Bottom
        """

class SectionAlongPathClippingPathViewProperties():
    """Clipping path view properties
    """
    def ConvertDirectionSymbolNumberFromViewModel(self, iPaletteIconNum: int, iPaletteIconNum: bool):
        """Convert icon number used in WPF palette to symbol number used in Allplan
        for the same graphical representation

        Args:
            iPaletteIconNum: number of icon from palette (view model)
        """
    def ConvertDirectionSymbolNumberToViewModel(self, arg2: bool) -> int:
        """Convert symbol number used in Allplan to icon number used in WPF palette
        for the same graphical representation

        Returns:
            icon number used in WPF
        """
    @staticmethod
    def GetDirectionSymbolHeightTolerance() -> float:
        """Access tolerances

        Returns:
            symbol height tolerance
        """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathClippingPathViewProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def DirectionSymbolHeight(self) -> float:
        """Get the DirectionSymbolHeight
        """
    @DirectionSymbolHeight.setter
    def DirectionSymbolHeight(self, value: float) -> None:
        """Set the DirectionSymbolHeight
        """
    @property
    def DirectionSymbolNr(self) -> int:
        """Get the DirectionSymbolNr
        """
    @DirectionSymbolNr.setter
    def DirectionSymbolNr(self, value: int) -> None:
        """Set the DirectionSymbolNr
        """
    @property
    def IsDirectionSymbolOn(self) -> bool:
        """Get the IsDirectionSymbolOn
        """
    @IsDirectionSymbolOn.setter
    def IsDirectionSymbolOn(self, value: bool) -> None:
        """Set the IsDirectionSymbolOn
        """
    @property
    def TextParameterProperties(self) -> SectionAlongPathTextParameterProperties:
        """Access text params

        Get the SectionAlongPathTextParameterProperties
        """
    @TextParameterProperties.setter
    def TextParameterProperties(self, value: SectionAlongPathTextParameterProperties) -> None:
        """Access text params
        """

class SectionAlongPathElement(BasisElement, AllplanElement):
    """Implementation of the section along path element
    """
    @typing.overload
    def __init__(self, sectionAlongPathProperties: SectionAlongPathProperties,
                 sectionPathElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Default constructor

        Args:
            sectionAlongPathProperties: Section along path properties
            sectionPathElement:         Section path element
        """
    @typing.overload
    def __init__(self, sectionAlongPathProperties: SectionAlongPathProperties, sectionPath: NemAll_Python_Geometry.Path2D,
                 comProp: NemAll_Python_BaseElements.CommonProperties):
        """Constructor

        Args:
            sectionAlongPathProperties: Section along path properties
            sectionPath:                Section path
            comProp:                    Common properties
        """
    @typing.overload
    def __init__(self, element: SectionAlongPathElement):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class SectionAlongPathElevationSpecifications():
    """Elevation specifications
    """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathElevationSpecifications):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def DecimalPlaces(self) -> int:
        """Get the number of places after decimal point
        """
    @DecimalPlaces.setter
    def DecimalPlaces(self, value: int) -> None:
        """Set the number of places after decimal point
        """
    @property
    def FontHeight(self) -> float:
        """Get the Height of the character set
        """
    @FontHeight.setter
    def FontHeight(self, value: float) -> None:
        """Set the Height of the character set
        """
    @property
    def FontNameStrg(self) -> str:
        """Get the Name the the character set
        """
    @FontNameStrg.setter
    def FontNameStrg(self, value: str) -> None:
        """Set the Name the the character set
        """
    @property
    def HeightWidthFactor(self) -> float:
        """Get the height/width ratio
        """
    @HeightWidthFactor.setter
    def HeightWidthFactor(self, value: float) -> None:
        """Set the height/width ratio
        """
    @property
    def IsAbsoluteElevation(self) -> bool:
        """Get the Absolute elevation
        """
    @IsAbsoluteElevation.setter
    def IsAbsoluteElevation(self, value: bool) -> None:
        """Set the Absolute elevation
        """
    @property
    def IsDimensionLineVisible(self) -> bool:
        """Get the visibility of dimension line
        """
    @IsDimensionLineVisible.setter
    def IsDimensionLineVisible(self, value: bool) -> None:
        """Set the visibility of dimension line
        """
    @property
    def IsDimensionNumberVisible(self) -> bool:
        """Get the Dimension number is visible
        """
    @IsDimensionNumberVisible.setter
    def IsDimensionNumberVisible(self, value: bool) -> None:
        """Set the Dimension number is visible
        """
    @property
    def IsFixFraction(self) -> bool:
        """Get the Fix fraction
        """
    @IsFixFraction.setter
    def IsFixFraction(self, value: bool) -> None:
        """Set the Fix fraction
        """
    @property
    def IsFontBold(self) -> bool:
        """Get the character set Bold
        """
    @IsFontBold.setter
    def IsFontBold(self, value: bool) -> None:
        """Set the character set Bold
        """
    @property
    def IsFontItalic(self) -> bool:
        """Get the character set Italic
        """
    @IsFontItalic.setter
    def IsFontItalic(self, value: bool) -> None:
        """Set the character set Italic
        """
    @property
    def IsFontUnderline(self) -> bool:
        """Get the character set Underline
        """
    @IsFontUnderline.setter
    def IsFontUnderline(self, value: bool) -> None:
        """Set the character set Underline
        """
    @property
    def IsFreeElevation(self) -> bool:
        """Get the Free elevation
        """
    @IsFreeElevation.setter
    def IsFreeElevation(self, value: bool) -> None:
        """Set the Free elevation
        """
    @property
    def IsLineColorFromLayer(self) -> bool:
        """Get the settings from layers three checkboxes on third page in layer dialog  like in  BBasisDimSettings.h   (do not know, why is it is doubled)
        """
    @IsLineColorFromLayer.setter
    def IsLineColorFromLayer(self, value: bool) -> None:
        """Set the settings from layers three checkboxes on third page in layer dialog  like in  BBasisDimSettings.h   (do not know, why is it is doubled)
        """
    @property
    def IsLineColorSameForAll(self) -> bool:
        """Get the the same line color for DMline,auxiliary line and number/texts
        """
    @IsLineColorSameForAll.setter
    def IsLineColorSameForAll(self, value: bool) -> None:
        """Set the the same line color for DMline,auxiliary line and number/texts
        """
    @property
    def IsLineColorTake(self) -> bool:
        """Get the settings from layers three checkboxes on third page in layer dialog
        """
    @IsLineColorTake.setter
    def IsLineColorTake(self, value: bool) -> None:
        """Set the settings from layers three checkboxes on third page in layer dialog
        """
    @property
    def IsModifiedIsTextOpaque(self) -> bool:
        """Get the is text opaque
        """
    @IsModifiedIsTextOpaque.setter
    def IsModifiedIsTextOpaque(self, value: bool) -> None:
        """Set the is text opaque
        """
    @property
    def IsPenFromLayer(self) -> bool:
        """Get the settings from layers three checkboxes on third page in layer dialog  like in  BasisDimSettings.h    (do not know, why is it is doubled)
        """
    @IsPenFromLayer.setter
    def IsPenFromLayer(self, value: bool) -> None:
        """Set the settings from layers three checkboxes on third page in layer dialog  like in  BasisDimSettings.h    (do not know, why is it is doubled)
        """
    @property
    def IsPenSameForAll(self) -> bool:
        """Get the the same pen for DMline,auxiliary line and number/texts
        """
    @IsPenSameForAll.setter
    def IsPenSameForAll(self, value: bool) -> None:
        """Set the the same pen for DMline,auxiliary line and number/texts
        """
    @property
    def IsPenSymbolFlag(self) -> bool:
        """Get the when true ->  pen for symbol as help construction line
        """
    @IsPenSymbolFlag.setter
    def IsPenSymbolFlag(self, value: bool) -> None:
        """Set the when true ->  pen for symbol as help construction line
        """
    @property
    def IsPenTake(self) -> bool:
        """Get the settings from layers three checkboxes on third page in layer dialog
        """
    @IsPenTake.setter
    def IsPenTake(self, value: bool) -> None:
        """Set the settings from layers three checkboxes on third page in layer dialog
        """
    @property
    def IsPlusMinusSign(self) -> bool:
        """Get the Draw +- sign before zero number
        """
    @IsPlusMinusSign.setter
    def IsPlusMinusSign(self, value: bool) -> None:
        """Set the Draw +- sign before zero number
        """
    @property
    def IsPositiveSign(self) -> bool:
        """Get the Draw +s ign before positive number
        """
    @IsPositiveSign.setter
    def IsPositiveSign(self, value: bool) -> None:
        """Set the Draw +s ign before positive number
        """
    @property
    def IsTextSymbolFlag(self) -> bool:
        """Get the when true ->  pen for text as help construction line
        """
    @IsTextSymbolFlag.setter
    def IsTextSymbolFlag(self, value: bool) -> None:
        """Set the when true ->  pen for text as help construction line
        """
    @property
    def LayerId(self) -> int:
        """Get the Layer Number
        """
    @LayerId.setter
    def LayerId(self, value: int) -> None:
        """Set the Layer Number
        """
    @property
    def LeadingCharacters(self) -> str:
        """Get the prefix of dimension number/additional number(16)
        """
    @LeadingCharacters.setter
    def LeadingCharacters(self, value: str) -> None:
        """Set the prefix of dimension number/additional number(16)
        """
    @property
    def MeasuredValueUnit(self) -> int:
        """Get the Unit of the measured value
        """
    @MeasuredValueUnit.setter
    def MeasuredValueUnit(self, value: int) -> None:
        """Set the Unit of the measured value
        """
    @property
    def PointSymbol(self) -> int:
        """Get the Point symbol
        """
    @PointSymbol.setter
    def PointSymbol(self, value: int) -> None:
        """Set the Point symbol
        """
    @property
    def PointSymbolSize(self) -> float:
        """Get the symbol size in mm/inch
        """
    @PointSymbolSize.setter
    def PointSymbolSize(self, value: float) -> None:
        """Set the symbol size in mm/inch
        """
    @property
    def RoundOffInch(self) -> float:
        """Get the round of number inch units
        """
    @RoundOffInch.setter
    def RoundOffInch(self, value: float) -> None:
        """Set the round of number inch units
        """
    @property
    def RoundOffNormal(self) -> float:
        """Get the round of number metric units
        """
    @RoundOffNormal.setter
    def RoundOffNormal(self, value: float) -> None:
        """Set the round of number metric units
        """
    @property
    def SymbolColorId(self) -> int:
        """Get the Symbol color
        """
    @SymbolColorId.setter
    def SymbolColorId(self, value: int) -> None:
        """Set the Symbol color
        """
    @property
    def SymbolPenId(self) -> int:
        """Get the Symbol pen
        """
    @SymbolPenId.setter
    def SymbolPenId(self, value: int) -> None:
        """Set the Symbol pen
        """
    @property
    def TailingCharacters(self) -> str:
        """Get the suffix of dimension number/additional number(16)
        """
    @TailingCharacters.setter
    def TailingCharacters(self, value: str) -> None:
        """Set the suffix of dimension number/additional number(16)
        """
    @property
    def TailingZeros(self) -> int:
        """Get the number of zeros after decimal point
        """
    @TailingZeros.setter
    def TailingZeros(self, value: int) -> None:
        """Set the number of zeros after decimal point
        """
    @property
    def TextColorId(self) -> int:
        """Get the Text color
        """
    @TextColorId.setter
    def TextColorId(self, value: int) -> None:
        """Set the Text color
        """
    @property
    def TextLocation(self) -> int:
        """Get the text location from position / location of texts (up to enum eTextLocation)
        """
    @TextLocation.setter
    def TextLocation(self, value: int) -> None:
        """Set the text location from position / location of texts (up to enum eTextLocation)
        """
    @property
    def TextOffset(self) -> float:
        """Get the distance     -> offset of texts from dimension line
        """
    @TextOffset.setter
    def TextOffset(self, value: float) -> None:
        """Set the distance     -> offset of texts from dimension line
        """
    @property
    def TextPenId(self) -> int:
        """Get the Text pen
        """
    @TextPenId.setter
    def TextPenId(self, value: int) -> None:
        """Set the Text pen
        """

class SectionAlongPathFilterProperties():
    """Filter properties
    """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathFilterProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def DrawingFilesProperties(self) -> SectionDrawingFilesProperties:
        """Access drawing file params

        Get the SectionDrawingFilesProperties
        """
    @DrawingFilesProperties.setter
    def DrawingFilesProperties(self, value: SectionDrawingFilesProperties) -> None:
        """Access drawing file params
        """
    @property
    def IsAssociativityOn(self) -> bool:
        """Get the When the section is frozen / associativity is OFF -, no updates are available for it
        """
    @IsAssociativityOn.setter
    def IsAssociativityOn(self, value: bool) -> None:
        """Set the When the section is frozen / associativity is OFF -, no updates are available for it
        """
    @property
    def IsSelectionFilterOn(self) -> bool:
        """Get the when == true - only selected elements are included to UVS model / when == false (default value) - selected elements are excluded from UVS model
        """
    @IsSelectionFilterOn.setter
    def IsSelectionFilterOn(self, value: bool) -> None:
        """Set the when == true - only selected elements are included to UVS model / when == false (default value) - selected elements are excluded from UVS model
        """
    @property
    def LayerProperties(self) -> SectionLayerProperties:
        """Access layer params

        Get the SectionLayerProperties
        """
    @LayerProperties.setter
    def LayerProperties(self, value: SectionLayerProperties) -> None:
        """Access layer params
        """

class SectionAlongPathFormatProperties():
    """Format properties
    """
    @staticmethod
    def GetEliminationAngleTolerance() -> float:
        """Access tolerances

        Returns:
            elimination angle tolerance
        """
    @staticmethod
    def GetOverhangTolerance() -> float:
        """Access tolerances

        Returns:
            overhang tolerance
        """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathFormatProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def AdjacentEdgeTypeSwitcher(self) -> int:
        """Get the 0=material, 1=surface, we set a tooltip and description in palette
        """
    @AdjacentEdgeTypeSwitcher.setter
    def AdjacentEdgeTypeSwitcher(self, value: int) -> None:
        """Set the 0=material, 1=surface, we set a tooltip and description in palette
        """
    @property
    def BoundaryLineColor(self) -> int:
        """Get the Border: Boundary Line color index
        """
    @BoundaryLineColor.setter
    def BoundaryLineColor(self, value: int) -> None:
        """Set the Border: Boundary Line color index
        """
    @property
    def BoundaryLineLayer(self) -> int:
        """Get the Border: Boundary Line Layer number
        """
    @BoundaryLineLayer.setter
    def BoundaryLineLayer(self, value: int) -> None:
        """Set the Border: Boundary Line Layer number
        """
    @property
    def BoundaryLineLayerKenner(self) -> int:
        """Gets layer kenner for Boundary Line

        Sets layer kenner for Boundary Line
        """
    @BoundaryLineLayerKenner.setter
    def BoundaryLineLayerKenner(self, newValue: int) -> None:
        """Gets layer kenner for Boundary Line

        Sets layer kenner for Boundary Line

        Args:
            newValue: newValue
        """
    @property
    def BoundaryLinePen(self) -> int:
        """Get the Border: Boundary Line pen index (0== not used)
        """
    @BoundaryLinePen.setter
    def BoundaryLinePen(self, value: int) -> None:
        """Set the Border: Boundary Line pen index (0== not used)
        """
    @property
    def BoundaryLineType(self) -> int:
        """Get the Border: Boundary Line stroke index
        """
    @BoundaryLineType.setter
    def BoundaryLineType(self, value: int) -> None:
        """Set the Border: Boundary Line stroke index
        """
    @property
    def EdgesVisibility(self) -> bool:
        """Get the Outer edges/All edges Visible     0, 1
        """
    @EdgesVisibility.setter
    def EdgesVisibility(self, value: bool) -> None:
        """Set the Outer edges/All edges Visible     0, 1
        """
    @property
    def EliminationAngle(self) -> float:
        """Get the Angle of the Adjacent Edge elimination, //always in degree
        """
    @EliminationAngle.setter
    def EliminationAngle(self, value: float) -> None:
        """Set the Angle of the Adjacent Edge elimination, //always in degree
        """
    @property
    def IsBetweenDifferentSurfacesOn(self) -> bool:
        """Get the Adjacent Edge Between Different Surfaces
        """
    @IsBetweenDifferentSurfacesOn.setter
    def IsBetweenDifferentSurfacesOn(self, value: bool) -> None:
        """Set the Adjacent Edge Between Different Surfaces
        """
    @property
    def IsBoundaryLineColorFromLayer(self) -> bool:
        """Get the Border: IsBoundaryLineColorFromLayer
        """
    @IsBoundaryLineColorFromLayer.setter
    def IsBoundaryLineColorFromLayer(self, value: bool) -> None:
        """Set the Border: IsBoundaryLineColorFromLayer
        """
    @property
    def IsBoundaryLinePenFromLayer(self) -> bool:
        """Get the Border: IsBoundaryLinePenFromLayer
        """
    @IsBoundaryLinePenFromLayer.setter
    def IsBoundaryLinePenFromLayer(self, value: bool) -> None:
        """Set the Border: IsBoundaryLinePenFromLayer
        """
    @property
    def IsBoundaryLineTypeFromLayer(self) -> bool:
        """Get the Border: IsBoundaryLineTypeFromLayer
        """
    @IsBoundaryLineTypeFromLayer.setter
    def IsBoundaryLineTypeFromLayer(self, value: bool) -> None:
        """Set the Border: IsBoundaryLineTypeFromLayer
        """
    @property
    def IsBoundaryLineVisible(self) -> bool:
        """Get the BoundaryLine visibility
        """
    @IsBoundaryLineVisible.setter
    def IsBoundaryLineVisible(self, value: bool) -> None:
        """Set the BoundaryLine visibility
        """
    @property
    def IsEliminationOn(self) -> bool:
        """Get the Adjacent Edge elimination
        """
    @IsEliminationOn.setter
    def IsEliminationOn(self, value: bool) -> None:
        """Set the Adjacent Edge elimination
        """
    @property
    def IsSectionLineColorFromLayer(self) -> bool:
        """Get the Section: IsSectionLineColorFromLayer
        """
    @IsSectionLineColorFromLayer.setter
    def IsSectionLineColorFromLayer(self, value: bool) -> None:
        """Set the Section: IsSectionLineColorFromLayer
        """
    @property
    def IsSectionLinePenFromLayer(self) -> bool:
        """Get the Section: IsSectionLinePenFromLayer
        """
    @IsSectionLinePenFromLayer.setter
    def IsSectionLinePenFromLayer(self, value: bool) -> None:
        """Set the Section: IsSectionLinePenFromLayer
        """
    @property
    def IsSectionLineThicknessVisible(self) -> bool:
        """Get the SectionLineThickness visibility
        """
    @IsSectionLineThicknessVisible.setter
    def IsSectionLineThicknessVisible(self, value: bool) -> None:
        """Set the SectionLineThickness visibility
        """
    @property
    def IsSectionLineTypeFromLayer(self) -> bool:
        """Get the Section: IsSectionLineTypeFromLayer
        """
    @IsSectionLineTypeFromLayer.setter
    def IsSectionLineTypeFromLayer(self, value: bool) -> None:
        """Set the Section: IsSectionLineTypeFromLayer
        """
    @property
    def IsSurfaceFromObjectOn(self) -> bool:
        """Get the Display Surface From Object
        """
    @IsSurfaceFromObjectOn.setter
    def IsSurfaceFromObjectOn(self, value: bool) -> None:
        """Set the Display Surface From Object
        """
    @property
    def Overhang(self) -> float:
        """Get the Overhang
        """
    @Overhang.setter
    def Overhang(self, value: float) -> None:
        """Set the Overhang
        """
    @property
    def SectionLineColor(self) -> int:
        """Get the Section: Boundary Line color index
        """
    @SectionLineColor.setter
    def SectionLineColor(self, value: int) -> None:
        """Set the Section: Boundary Line color index
        """
    @property
    def SectionLineLayer(self) -> int:
        """Get the Section: Section Line Layer number
        """
    @SectionLineLayer.setter
    def SectionLineLayer(self, value: int) -> None:
        """Set the Section: Section Line Layer number
        """
    @property
    def SectionLineLayerKenner(self) -> int:
        """Gets layer kenner for Section Line

        Sets layer kenner for Section Line
        """
    @SectionLineLayerKenner.setter
    def SectionLineLayerKenner(self, newValue: int) -> None:
        """Gets layer kenner for Section Line

        Sets layer kenner for Section Line

        Args:
            newValue: newValue
        """
    @property
    def SectionLinePen(self) -> int:
        """Get the Section: Boundary Line pen index (0== not used)
        """
    @SectionLinePen.setter
    def SectionLinePen(self, value: int) -> None:
        """Set the Section: Boundary Line pen index (0== not used)
        """
    @property
    def SectionLineType(self) -> int:
        """Get the Section: Boundary Line stroke index
        """
    @SectionLineType.setter
    def SectionLineType(self, value: int) -> None:
        """Set the Section: Boundary Line stroke index
        """

class SectionAlongPathGeneralSectionProperties():
    """General section properties
    """
    def GetOffset(self) -> tuple[bool, float, float]:
        """Get offset

        Returns:
            tuple(true if it was read from 55th element,
                  X coordinate of  section's left bottom corner,
                  Y coordinate of  section's left bottom corner)
        """
    def IsOffsetValid(self) -> bool:
        """Get offset state
        """
    def SetOffset(self, dOffset_X: float, dOffset_Y: float):
        """Set offset

        Args:
            dOffset_X: X coordinate of  section's left bottom corner
            dOffset_Y: Y coordinate of  section's left bottom corner
        """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathGeneralSectionProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def ElevationSpecifications(self) -> SectionAlongPathElevationSpecifications:
        """Get the SectionAlongPathElevationSpecifications
        """
    @ElevationSpecifications.setter
    def ElevationSpecifications(self, value: SectionAlongPathElevationSpecifications) -> None:
        """Set the SectionAlongPathElevationSpecifications
        """
    @property
    def FormatProperties(self) -> SectionAlongPathFormatProperties:
        """Get the SectionAlongPathFormatProperties
        """
    @FormatProperties.setter
    def FormatProperties(self, value: SectionAlongPathFormatProperties) -> None:
        """Set the SectionAlongPathFormatProperties
        """
    @property
    def LabelingStripSetting(self) -> SectionAlongPathLabelingStripSetting:
        """Get the SectionAlongPathLabelingStripSetting
        """
    @LabelingStripSetting.setter
    def LabelingStripSetting(self, value: SectionAlongPathLabelingStripSetting) -> None:
        """Set the SectionAlongPathLabelingStripSetting
        """
    @property
    def Offset_X(self) -> float:
        """Get the X coordinate of left bottom corner
        """
    @Offset_X.setter
    def Offset_X(self, value: float) -> None:
        """Set the X coordinate of left bottom corner
        """
    @property
    def Offset_Y(self) -> float:
        """Get the Y coordinate of left bottom corner
        """
    @Offset_Y.setter
    def Offset_Y(self, value: float) -> None:
        """Set the Y coordinate of left bottom corner
        """
    @property
    def SectionLabelingProperties(self) -> SectionAlongPathSectionLabelingProperties:
        """Get the SectionAlongPathSectionLabelingProperties
        """
    @SectionLabelingProperties.setter
    def SectionLabelingProperties(self, value: SectionAlongPathSectionLabelingProperties) -> None:
        """Set the SectionAlongPathSectionLabelingProperties
        """
    @property
    def SectionViewProperties(self) -> SectionAlongPathSectionViewProperties:
        """Get the SectionAlongPathSectionViewProperties
        """
    @SectionViewProperties.setter
    def SectionViewProperties(self, value: SectionAlongPathSectionViewProperties) -> None:
        """Set the SectionAlongPathSectionViewProperties
        """

class SectionAlongPathLabelingStripSetting():
    """Labeling strip settings
    """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathLabelingStripSetting):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Distance_1(self) -> float:
        """Get the Distance 1 in mm
        """
    @Distance_1.setter
    def Distance_1(self, value: float) -> None:
        """Set the Distance 1 in mm
        """
    @property
    def Distance_2(self) -> float:
        """Get the Distance 2 in mm
        """
    @Distance_2.setter
    def Distance_2(self, value: float) -> None:
        """Set the Distance 2 in mm
        """
    @property
    def Distance_3(self) -> float:
        """Get the Distance 3 in mm
        """
    @Distance_3.setter
    def Distance_3(self, value: float) -> None:
        """Set the Distance 3 in mm
        """
    @property
    def Distance_4(self) -> float:
        """Get the Distance 4 in mm
        """
    @Distance_4.setter
    def Distance_4(self, value: float) -> None:
        """Set the Distance 4 in mm
        """
    @property
    def Distance_5(self) -> float:
        """Get the Distance 5 in mm
        """
    @Distance_5.setter
    def Distance_5(self, value: float) -> None:
        """Set the Distance 5 in mm
        """
    @property
    def Distance_6(self) -> float:
        """Get the Distance 6 in mm
        """
    @Distance_6.setter
    def Distance_6(self, value: float) -> None:
        """Set the Distance 6 in mm
        """
    @property
    def Distance_7(self) -> float:
        """Get the Distance 7 in mm
        """
    @Distance_7.setter
    def Distance_7(self, value: float) -> None:
        """Set the Distance 7 in mm
        """
    @property
    def HeightLines_Color(self) -> int:
        """Get the Height lines color
        """
    @HeightLines_Color.setter
    def HeightLines_Color(self, value: int) -> None:
        """Set the Height lines color
        """
    @property
    def HeightLines_HeightZone(self) -> int:
        """Get the Height lines height zone
        """
    @HeightLines_HeightZone.setter
    def HeightLines_HeightZone(self, value: int) -> None:
        """Set the Height lines height zone
        """
    @property
    def HeightLines_LineType(self) -> int:
        """Get the Height lines line type
        """
    @HeightLines_LineType.setter
    def HeightLines_LineType(self, value: int) -> None:
        """Set the Height lines line type
        """
    @property
    def HeightLines_Pen(self) -> int:
        """Get the Height lines pen
        """
    @HeightLines_Pen.setter
    def HeightLines_Pen(self, value: int) -> None:
        """Set the Height lines pen
        """
    @property
    def HeightLines_ProfileZone(self) -> int:
        """Get the Height lines profile zone
        """
    @HeightLines_ProfileZone.setter
    def HeightLines_ProfileZone(self, value: int) -> None:
        """Set the Height lines profile zone
        """
    @property
    def HeightLines_Splay(self) -> int:
        """Get the Height lines splay
        """
    @HeightLines_Splay.setter
    def HeightLines_Splay(self, value: int) -> None:
        """Set the Height lines splay
        """
    @property
    def HeightLines_StationZone(self) -> int:
        """Get the Height lines station zone
        """
    @HeightLines_StationZone.setter
    def HeightLines_StationZone(self, value: int) -> None:
        """Set the Height lines station zone
        """
    @property
    def HeightText_Color(self) -> int:
        """Get the Height text color
        """
    @HeightText_Color.setter
    def HeightText_Color(self, value: int) -> None:
        """Set the Height text color
        """
    @property
    def HeightText_Distance(self) -> float:
        """Get the Height text distance in mm
        """
    @HeightText_Distance.setter
    def HeightText_Distance(self, value: float) -> None:
        """Set the Height text distance in mm
        """
    @property
    def HeightText_Height(self) -> float:
        """Get the Height text height in mm
        """
    @HeightText_Height.setter
    def HeightText_Height(self, value: float) -> None:
        """Set the Height text height in mm
        """
    @property
    def HeightText_Pen(self) -> int:
        """Get the Height text pen
        """
    @HeightText_Pen.setter
    def HeightText_Pen(self, value: int) -> None:
        """Set the Height text pen
        """
    @property
    def HeightText_Precision(self) -> int:
        """Get the Height text decimals
        """
    @HeightText_Precision.setter
    def HeightText_Precision(self, value: int) -> None:
        """Set the Height text decimals
        """
    @property
    def HeightText_Width(self) -> float:
        """Get the Height text width in mm
        """
    @HeightText_Width.setter
    def HeightText_Width(self, value: float) -> None:
        """Set the Height text width in mm
        """
    @property
    def ProfileAx_Color(self) -> int:
        """Get the Profile axis color
        """
    @ProfileAx_Color.setter
    def ProfileAx_Color(self, value: int) -> None:
        """Set the Profile axis color
        """
    @property
    def ProfileAx_LineType(self) -> int:
        """Get the Profile axis line type
        """
    @ProfileAx_LineType.setter
    def ProfileAx_LineType(self, value: int) -> None:
        """Set the Profile axis line type
        """
    @property
    def ProfileAx_Pen(self) -> int:
        """Get the Profile axis pen
        """
    @ProfileAx_Pen.setter
    def ProfileAx_Pen(self, value: int) -> None:
        """Set the Profile axis pen
        """
    @property
    def ProfileFrame_Color(self) -> int:
        """Get the Profile frame color
        """
    @ProfileFrame_Color.setter
    def ProfileFrame_Color(self, value: int) -> None:
        """Set the Profile frame color
        """
    @property
    def ProfileFrame_LineType(self) -> int:
        """Get the Profile frame line type
        """
    @ProfileFrame_LineType.setter
    def ProfileFrame_LineType(self, value: int) -> None:
        """Set the Profile frame line type
        """
    @property
    def ProfileFrame_Pen(self) -> int:
        """Get the Profile frame pen
        """
    @ProfileFrame_Pen.setter
    def ProfileFrame_Pen(self, value: int) -> None:
        """Set the Profile frame pen
        """
    @property
    def ProfileLine_Color(self) -> int:
        """Get the Profile line color
        """
    @ProfileLine_Color.setter
    def ProfileLine_Color(self, value: int) -> None:
        """Set the Profile line color
        """
    @property
    def ProfileLine_LineType(self) -> int:
        """Get the Profile line line type
        """
    @ProfileLine_LineType.setter
    def ProfileLine_LineType(self, value: int) -> None:
        """Set the Profile line line type
        """
    @property
    def ProfileLine_Muster(self) -> int:
        """Get the Profile line pattern
        """
    @ProfileLine_Muster.setter
    def ProfileLine_Muster(self, value: int) -> None:
        """Set the Profile line pattern
        """
    @property
    def ProfileLine_Pen(self) -> int:
        """Get the Profile line pen
        """
    @ProfileLine_Pen.setter
    def ProfileLine_Pen(self, value: int) -> None:
        """Set the Profile line pen
        """
    @property
    def RefererenzeHeight_Distance(self) -> float:
        """Get the Reference height text distance in mm
        """
    @RefererenzeHeight_Distance.setter
    def RefererenzeHeight_Distance(self, value: float) -> None:
        """Set the Reference height text distance in mm
        """
    @property
    def RefererenzeHeight_Height(self) -> float:
        """Get the Reference height text height in mm
        """
    @RefererenzeHeight_Height.setter
    def RefererenzeHeight_Height(self, value: float) -> None:
        """Set the Reference height text height in mm
        """
    @property
    def RefererenzeHeight_TextColor(self) -> int:
        """Get the Reference height text color
        """
    @RefererenzeHeight_TextColor.setter
    def RefererenzeHeight_TextColor(self, value: int) -> None:
        """Set the Reference height text color
        """
    @property
    def RefererenzeHeight_TextPen(self) -> int:
        """Get the Reference height text pen
        """
    @RefererenzeHeight_TextPen.setter
    def RefererenzeHeight_TextPen(self, value: int) -> None:
        """Set the Reference height text pen
        """
    @property
    def RefererenzeHeight_TextPrecision(self) -> int:
        """Get the Reference height text decimals
        """
    @RefererenzeHeight_TextPrecision.setter
    def RefererenzeHeight_TextPrecision(self, value: int) -> None:
        """Set the Reference height text decimals
        """
    @property
    def RefererenzeHeight_Width(self) -> float:
        """Get the Reference height text width in mm
        """
    @RefererenzeHeight_Width.setter
    def RefererenzeHeight_Width(self, value: float) -> None:
        """Set the Reference height text width in mm
        """
    @property
    def StationText_Color(self) -> int:
        """Get the Station text color
        """
    @StationText_Color.setter
    def StationText_Color(self, value: int) -> None:
        """Set the Station text color
        """
    @property
    def StationText_Distance(self) -> float:
        """Get the Station text distance in mm
        """
    @StationText_Distance.setter
    def StationText_Distance(self, value: float) -> None:
        """Set the Station text distance in mm
        """
    @property
    def StationText_Height(self) -> float:
        """Get the Station text height in mm
        """
    @StationText_Height.setter
    def StationText_Height(self, value: float) -> None:
        """Set the Station text height in mm
        """
    @property
    def StationText_Pen(self) -> int:
        """Get the Station text pen
        """
    @StationText_Pen.setter
    def StationText_Pen(self, value: int) -> None:
        """Set the Station text pen
        """
    @property
    def StationText_Precision(self) -> int:
        """Get the Station text decimals
        """
    @StationText_Precision.setter
    def StationText_Precision(self, value: int) -> None:
        """Set the Station text decimals
        """
    @property
    def StationText_Width(self) -> float:
        """Get the Station text width in mm
        """
    @StationText_Width.setter
    def StationText_Width(self, value: float) -> None:
        """Set the Station text width in mm
        """

class SectionAlongPathProperties():
    """Section along path properties
    """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def ClippingPathProperties(self) -> SectionAlongPathClippingPathProperties:
        """Get the SectionAlongPathClippingPathProperties
        """
    @ClippingPathProperties.setter
    def ClippingPathProperties(self, value: SectionAlongPathClippingPathProperties) -> None:
        """Set the SectionAlongPathClippingPathProperties
        """
    @property
    def FilterProperties(self) -> SectionAlongPathFilterProperties:
        """Get the SectionAlongPathFilterProperties
        """
    @FilterProperties.setter
    def FilterProperties(self, value: SectionAlongPathFilterProperties) -> None:
        """Set the SectionAlongPathFilterProperties
        """
    @property
    def GeneralSectionProperties(self) -> SectionAlongPathGeneralSectionProperties:
        """Get the SectionAlongPathGeneralSectionProperties
        """
    @GeneralSectionProperties.setter
    def GeneralSectionProperties(self, value: SectionAlongPathGeneralSectionProperties) -> None:
        """Set the SectionAlongPathGeneralSectionProperties
        """
    @property
    def ScaleProperties(self) -> SectionAlongPathScaleProperties:
        """Get the SectionAlongPathScaleProperties
        """
    @ScaleProperties.setter
    def ScaleProperties(self, value: SectionAlongPathScaleProperties) -> None:
        """Set the SectionAlongPathScaleProperties
        """

class SectionAlongPathScaleProperties():
    """Scale properties
    """
    @staticmethod
    def GetScaleFactorTolerance() -> float:
        """Access tolerance

        Returns:
            scale factor tolerance
        """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathScaleProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def ScaleFactorX(self) -> float:
        """Get the resizing factor X in  Longitudinal direction
        """
    @ScaleFactorX.setter
    def ScaleFactorX(self, value: float) -> None:
        """Set the resizing factor X in  Longitudinal direction
        """
    @property
    def ScaleFactorY(self) -> float:
        """Get the resizing factor Y in  Transversal  direction
        """
    @ScaleFactorY.setter
    def ScaleFactorY(self, value: float) -> None:
        """Set the resizing factor Y in  Transversal  direction
        """

class SectionAlongPathSectionLabelingProperties():
    """Section labeling properties
    """
    class SAAPLabelingPosition_Enum(enum.Enum):
        """enum for Reference point position

        Nothing: Calculated like before this implementation
        """
        BottomCenter = 5
        BottomLeft = 4
        BottomRight = 6
        Nothing = 0
        TopCenter = 2
        TopLeft = 1
        TopRight = 3

        names = {Nothing: Nothing,
                 TopLeft: TopLeft,
                 TopCenter: TopCenter,
                 TopRight: TopRight,
                 BottomLeft: BottomLeft,
                 BottomCenter: BottomCenter,
                 BottomRight: BottomRight}

        values = {0: Nothing,
                  1: TopLeft,
                  2: TopCenter,
                  3: TopRight,
                  4: BottomLeft,
                  5: BottomCenter,
                  6: BottomRight}

        def __getitem__(self, key: (str | int | float)) -> SectionAlongPathSectionLabelingProperties.SAAPLabelingPosition_Enum:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathSectionLabelingProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def HeadingText(self) -> str:
        """Get the HeadingText  "longitudinal profile", "transversal profile", "elevation", "section", "Unfold", . and "none" (expandable)
        """
    @HeadingText.setter
    def HeadingText(self, value: str) -> None:
        """Set the HeadingText  "longitudinal profile", "transversal profile", "elevation", "section", "Unfold", . and "none" (expandable)
        """
    @property
    def HeadingTextParameters(self) -> SectionAlongPathTextParameterProperties:
        """Get the SectionAlongPathTextParameterProperties
        """
    @HeadingTextParameters.setter
    def HeadingTextParameters(self, value: SectionAlongPathTextParameterProperties) -> None:
        """Set the SectionAlongPathTextParameterProperties
        """
    @property
    def IsHeadingOn(self) -> bool:
        """Get the IsHeadingOn
        """
    @IsHeadingOn.setter
    def IsHeadingOn(self, value: bool) -> None:
        """Set the IsHeadingOn
        """
    @property
    def IsScaleOn(self) -> bool:
        """Get the IsScaleOn
        """
    @IsScaleOn.setter
    def IsScaleOn(self, value: bool) -> None:
        """Set the IsScaleOn
        """
    @property
    def LabelingOffset(self) -> float:
        """Get the Distance of the labeling from its content's min/max box
        """
    @LabelingOffset.setter
    def LabelingOffset(self, value: float) -> None:
        """Set the Distance of the labeling from its content's min/max box
        """
    @property
    def LabelingPosition(self) -> int:
        """Get the Position of the labeling with respect to its content's min/max box
        """
    @LabelingPosition.setter
    def LabelingPosition(self, value: int) -> None:
        """Set the Position of the labeling with respect to its content's min/max box
        """
    @property
    def LabelingsDistance(self) -> float:
        """Get the Distance between scale text and heading text
        """
    @LabelingsDistance.setter
    def LabelingsDistance(self, value: float) -> None:
        """Set the Distance between scale text and heading text
        """
    @property
    def ScaleTextParameters(self) -> SectionAlongPathTextParameterProperties:
        """Get the SectionAlongPathTextParameterProperties
        """
    @ScaleTextParameters.setter
    def ScaleTextParameters(self, value: SectionAlongPathTextParameterProperties) -> None:
        """Set the SectionAlongPathTextParameterProperties
        """
    BottomCenter = SAAPLabelingPosition_Enum.BottomCenter
    BottomLeft = SAAPLabelingPosition_Enum.BottomLeft
    BottomRight = SAAPLabelingPosition_Enum.BottomRight
    Nothing = SAAPLabelingPosition_Enum.Nothing
    TopCenter = SAAPLabelingPosition_Enum.TopCenter
    TopLeft = SAAPLabelingPosition_Enum.TopLeft
    TopRight = SAAPLabelingPosition_Enum.TopRight

class SectionAlongPathSectionViewProperties():
    """Section view properties
    """
    @staticmethod
    def GetHorizontTolerance() -> float:
        """Access tolerances
        """
    @staticmethod
    def GetOffsetTolerance() -> float:
        """Access tolerances
        """
    @typing.overload
    def __init__(self, bInitFromSTW: bool = False):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, B: SectionAlongPathSectionViewProperties):
        """copy constructor

        Args:
            B: - object to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def Horizont(self) -> float:
        """Get the Horizon
        """
    @Horizont.setter
    def Horizont(self, value: float) -> None:
        """Set the Horizon
        """
    @property
    def IsElementedgesDisplayed(self) -> bool:
        """Get the Is element edges displayed
        """
    @IsElementedgesDisplayed.setter
    def IsElementedgesDisplayed(self, value: bool) -> None:
        """Set the Is element edges displayed
        """
    @property
    def IsElementedges_BottomLabeling(self) -> bool:
        """Get the Is element edges bottom labeling
        """
    @IsElementedges_BottomLabeling.setter
    def IsElementedges_BottomLabeling(self, value: bool) -> None:
        """Set the Is element edges bottom labeling
        """
    @property
    def IsElementedges_MiddleLabeling(self) -> bool:
        """Get the Is element edges middle labeling
        """
    @IsElementedges_MiddleLabeling.setter
    def IsElementedges_MiddleLabeling(self, value: bool) -> None:
        """Set the Is element edges middle labeling
        """
    @property
    def IsElementedges_TopLabeling(self) -> bool:
        """Get the Is element edges top labeling
        """
    @IsElementedges_TopLabeling.setter
    def IsElementedges_TopLabeling(self, value: bool) -> None:
        """Set the Is element edges top labeling
        """
    @property
    def IsHorizontalPositionPointDisplayed(self) -> bool:
        """Get the Is horizontal position point displayed
        """
    @IsHorizontalPositionPointDisplayed.setter
    def IsHorizontalPositionPointDisplayed(self, value: bool) -> None:
        """Set the Is horizontal position point displayed
        """
    @property
    def IsHorizontalPositionPoint_BottomLabeling(self) -> bool:
        """Get the Is horizontal position point bottom labeling
        """
    @IsHorizontalPositionPoint_BottomLabeling.setter
    def IsHorizontalPositionPoint_BottomLabeling(self, value: bool) -> None:
        """Set the Is horizontal position point bottom labeling
        """
    @property
    def IsHorizontalPositionPoint_MiddleLabeling(self) -> bool:
        """Get the Is horizontalPositionPoint_Middle labeling
        """
    @IsHorizontalPositionPoint_MiddleLabeling.setter
    def IsHorizontalPositionPoint_MiddleLabeling(self, value: bool) -> None:
        """Set the Is horizontalPositionPoint_Middle labeling
        """
    @property
    def IsHorizontalPositionPoint_TopLabeling(self) -> bool:
        """Get the Is horizontal position point top labeling
        """
    @IsHorizontalPositionPoint_TopLabeling.setter
    def IsHorizontalPositionPoint_TopLabeling(self, value: bool) -> None:
        """Set the Is horizontal position point top labeling
        """
    @property
    def IsStationPointDisplayed(self) -> bool:
        """Get the Is station point displayed
        """
    @IsStationPointDisplayed.setter
    def IsStationPointDisplayed(self, value: bool) -> None:
        """Set the Is station point displayed
        """
    @property
    def IsStationPoint_BottomLabeling(self) -> bool:
        """Get the Is station point bottom labeling
        """
    @IsStationPoint_BottomLabeling.setter
    def IsStationPoint_BottomLabeling(self, value: bool) -> None:
        """Set the Is station point bottom labeling
        """
    @property
    def IsStationPoint_MiddleLabeling(self) -> bool:
        """Get the Is station point middle labeling
        """
    @IsStationPoint_MiddleLabeling.setter
    def IsStationPoint_MiddleLabeling(self, value: bool) -> None:
        """Set the Is station point middle labeling
        """
    @property
    def IsStationPoint_TopLabeling(self) -> bool:
        """Get the Is station point_Top labeling
        """
    @IsStationPoint_TopLabeling.setter
    def IsStationPoint_TopLabeling(self, value: bool) -> None:
        """Set the Is station point_Top labeling
        """
    @property
    def IsZeroAxDisplayed(self) -> bool:
        """Get the Is zero axis displayed
        """
    @IsZeroAxDisplayed.setter
    def IsZeroAxDisplayed(self, value: bool) -> None:
        """Set the Is zero axis displayed
        """
    @property
    def IsZeroAx_BottomLabeling(self) -> bool:
        """Get the Is zero Axis bottom labeling
        """
    @IsZeroAx_BottomLabeling.setter
    def IsZeroAx_BottomLabeling(self, value: bool) -> None:
        """Set the Is zero Axis bottom labeling
        """
    @property
    def IsZeroAx_MiddleLabeling(self) -> bool:
        """Get the Is zero axis middle labeling
        """
    @IsZeroAx_MiddleLabeling.setter
    def IsZeroAx_MiddleLabeling(self, value: bool) -> None:
        """Set the Is zero axis middle labeling
        """
    @property
    def IsZeroAx_TopLabeling(self) -> bool:
        """Get the Is zero Axis top labeling
        """
    @IsZeroAx_TopLabeling.setter
    def IsZeroAx_TopLabeling(self, value: bool) -> None:
        """Set the Is zero Axis top labeling
        """
    @property
    def LabelingType(self) -> int:
        """Get the LabelingType
        """
    @LabelingType.setter
    def LabelingType(self, value: int) -> None:
        """Set the LabelingType
        """
    @property
    def Offset(self) -> float:
        """Get the Offset
        """
    @Offset.setter
    def Offset(self, value: float) -> None:
        """Set the Offset
        """

class SectionAlongPathTextParameterProperties():
    """Text parameter properties
    """
    class TextEmphasis_Enum(enum.Enum):
        """enum for Section type

        eUVS_ClippingPath             : Clipping line with Allplan style symbols
        eUVS_AdvancedStyleClippingPath: Clipping line with advanced symbols(US Standard)
        eUVS_USStyleHeading           : Heading for sections created with advanced symbols(US Standard)
        eUVS_USStyleScale             : Scale for sections created with advanced symbols(US Standard)

        eBold                         : according to N_FONTSTYLE_BOLD
        eItalic                       : according to N_FONTSTYLE_ITALIC
        eUnderline                    : according to N_FONTSTYLE_UNDERLINE
        eStrikethrough                : according to N_FONTSTYLE_STRIKETHROUGH
        """
        eBold = 1
        eItalic = 2
        eNone = 0
        eStrikethrough = 8
        eUnderline = 4

        names = {eNone: eNone,
                 eBold: eBold,
                 eItalic: eItalic,
                 eUnderline: eUnderline,
                 eStrikethrough: eStrikethrough}

        values = {0: eNone,
                  1: eBold,
                  2: eItalic,
                  4: eUnderline,
                  8: eStrikethrough}

        def __getitem__(self, key: (str | int | float)) -> SectionAlongPathTextParameterProperties.TextEmphasis_Enum:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class TextPropertiesSource_Enum(enum.Enum):
        """enum for Section type

        eUVS_ClippingPath             : Clipping line with Allplan style symbols
        eUVS_AdvancedStyleClippingPath: Clipping line with advanced symbols(US Standard)
        eUVS_USStyleHeading           : Heading for sections created with advanced symbols(US Standard)
        eUVS_USStyleScale             : Scale for sections created with advanced symbols(US Standard)

        eBold                         : according to N_FONTSTYLE_BOLD
        eItalic                       : according to N_FONTSTYLE_ITALIC
        eUnderline                    : according to N_FONTSTYLE_UNDERLINE
        eStrikethrough                : according to N_FONTSTYLE_STRIKETHROUGH
        """
        eLabel = 1
        eSaaP_ClippingPath = 29
        eSaaP_Heading = 30
        eSaaP_Scale = 31
        eUVS_AdvancedStyleClippingPath = 35
        eUVS_ClippingPath = 32
        eUVS_Heading = 33
        eUVS_Scale = 34
        eUVS_USStyleHeading = 36
        eUVS_USStyleScale = 37

        names = {eLabel: eLabel,
                 eSaaP_ClippingPath: eSaaP_ClippingPath,
                 eSaaP_Heading: eSaaP_Heading,
                 eSaaP_Scale: eSaaP_Scale,
                 eUVS_ClippingPath: eUVS_ClippingPath,
                 eUVS_Heading: eUVS_Heading,
                 eUVS_Scale: eUVS_Scale,
                 eUVS_AdvancedStyleClippingPath: eUVS_AdvancedStyleClippingPath,
                 eUVS_USStyleHeading: eUVS_USStyleHeading,
                 eUVS_USStyleScale: eUVS_USStyleScale}

        values = {1: eLabel,
                  29: eSaaP_ClippingPath,
                  30: eSaaP_Heading,
                  31: eSaaP_Scale,
                  32: eUVS_ClippingPath,
                  33: eUVS_Heading,
                  34: eUVS_Scale,
                  35: eUVS_AdvancedStyleClippingPath,
                  36: eUVS_USStyleHeading,
                  37: eUVS_USStyleScale}

        def __getitem__(self, key: (str | int | float)) -> SectionAlongPathTextParameterProperties.TextPropertiesSource_Enum:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    @staticmethod
    def DetectBackgroundColorType(bHasBgColor: bool, bgColor: int, backgroundIsTransparent: bool) -> tuple[int, int]:
        """Args:
            bHasBgColor
            bgColor
            backgroundIsTransparent
        """
    def FillPropertiesFromAllplanTextParameters(self, richTextFlags: int, layerId: int, byLayerFlags: int) -> object:
        """Args:
            richTextFlags
            layerId
            byLayerFlags
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, iTextParameterID: int, bInitFromSTW: bool = False):
        """constructor

        Args:
            iTextParameterID: - type of text parameter
            bInitFromSTW:     - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, bInitFromSTW: bool):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    @typing.overload
    def __init__(self, A: SectionAlongPathTextParameterProperties):
        """copy constructor

        Args:
            A
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def BackgroundColorType(self) -> int:
        """Get the when =0 : no background color (transparency), when = 1 color is according to Allplan's view, when = 2, custom defined in CustomBackgroundColor
        """
    @BackgroundColorType.setter
    def BackgroundColorType(self, value: int) -> None:
        """Set the when =0 : no background color (transparency), when = 1 color is according to Allplan's view, when = 2, custom defined in CustomBackgroundColor
        """
    @property
    def BorderColor(self) -> int:
        """Get the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @BorderColor.setter
    def BorderColor(self, value: int) -> None:
        """Set the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @property
    def BorderLineType(self) -> int:
        """Get the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @BorderLineType.setter
    def BorderLineType(self, value: int) -> None:
        """Set the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @property
    def BorderOffset(self) -> int:
        """Get the BorderOffset  0 it represents value -1; 4 repres. -0.5; 2 repres. 0.0; 1 repres.1.0; 5 repres. 2.0
        """
    @BorderOffset.setter
    def BorderOffset(self, value: int) -> None:
        """Set the BorderOffset  0 it represents value -1; 4 repres. -0.5; 2 repres. 0.0; 1 repres.1.0; 5 repres. 2.0
        """
    @property
    def BorderThickness(self) -> int:
        """Get the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @BorderThickness.setter
    def BorderThickness(self, value: int) -> None:
        """Set the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @property
    def ColumnAngle(self) -> float:
        """Get the ColumnAngle
        """
    @ColumnAngle.setter
    def ColumnAngle(self, value: float) -> None:
        """Set the ColumnAngle
        """
    @property
    def CustomBackgroundColor(self) -> int:
        """Get the when =0 : no background color (transparency), when = 1 color is according to Allplan's view, when = 2, custom defined in CustomBackgroundColor
        """
    @CustomBackgroundColor.setter
    def CustomBackgroundColor(self, value: int) -> None:
        """Set the when =0 : no background color (transparency), when = 1 color is according to Allplan's view, when = 2, custom defined in CustomBackgroundColor
        """
    @property
    def FontAngle(self) -> float:
        """Get the FontAngle   //ONLY for italic
        """
    @FontAngle.setter
    def FontAngle(self, value: float) -> None:
        """Set the FontAngle   //ONLY for italic
        """
    @property
    def FontColor(self) -> int:
        """Get the ColumnAngle
        """
    @FontColor.setter
    def FontColor(self, value: int) -> None:
        """Set the ColumnAngle
        """
    @property
    def FontEmphasis(self) -> int:
        """Get the Font emphasis
        """
    @FontEmphasis.setter
    def FontEmphasis(self, value: int) -> None:
        """Set the Font emphasis
        """
    @property
    def FontHeight(self) -> float:
        """Get the FontHeight
        """
    @FontHeight.setter
    def FontHeight(self, value: float) -> None:
        """Set the FontHeight
        """
    @property
    def FontID(self) -> int:
        """Get the FontType
        """
    @FontID.setter
    def FontID(self, value: int) -> None:
        """Set the FontType
        """
    @property
    def FontLayer(self) -> int:
        """Get the ColumnAngle
        """
    @FontLayer.setter
    def FontLayer(self, value: int) -> None:
        """Set the ColumnAngle
        """
    @property
    def FontThickness(self) -> int:
        """Get the pen of the text, never serialized, not in standard values, it is  a working property only
        """
    @FontThickness.setter
    def FontThickness(self, value: int) -> None:
        """Set the pen of the text, never serialized, not in standard values, it is  a working property only
        """
    @property
    def FontWidth(self) -> float:
        """Get the FontWidth
        """
    @FontWidth.setter
    def FontWidth(self, value: float) -> None:
        """Set the FontWidth
        """
    @property
    def IsFontColorFromLayer(self) -> bool:
        """Get the When False: it means scale dependent
        """
    @IsFontColorFromLayer.setter
    def IsFontColorFromLayer(self, value: bool) -> None:
        """Set the When False: it means scale dependent
        """
    @property
    def IsFontLineTypeFromLayer(self) -> bool:
        """Get the When False: it means scale dependent
        """
    @IsFontLineTypeFromLayer.setter
    def IsFontLineTypeFromLayer(self, value: bool) -> None:
        """Set the When False: it means scale dependent
        """
    @property
    def IsFontPenFromLayer(self) -> bool:
        """Get the When False: it means scale dependent
        """
    @IsFontPenFromLayer.setter
    def IsFontPenFromLayer(self, value: bool) -> None:
        """Set the When False: it means scale dependent
        """
    @property
    def RowDistance(self) -> float:
        """Get the RowDistance //Line spacing
        """
    @RowDistance.setter
    def RowDistance(self, value: float) -> None:
        """Set the RowDistance //Line spacing
        """
    @property
    def TextAngle(self) -> float:
        """Get the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @TextAngle.setter
    def TextAngle(self, value: float) -> None:
        """Set the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @property
    def TextParameterID(self) -> TextPropertiesSource_Enum:
        """Initialize the class with Usable Values
        """
    @TextParameterID.setter
    def TextParameterID(self, value: TextPropertiesSource_Enum) -> None:
        """Initialize the class with Usable Values

        Set the value
        """
    @property
    def TextParameterId(self) -> int:
        """Get the Text parameter ID
        """
    @TextParameterId.setter
    def TextParameterId(self, value: int) -> None:
        """Set the Text parameter ID
        """
    @property
    def TextPlacementPointType(self) -> int:
        """Get the text placement point, see in NA_Data_TextDefines.h
        """
    @TextPlacementPointType.setter
    def TextPlacementPointType(self, value: int) -> None:
        """Set the text placement point, see in NA_Data_TextDefines.h
        """
    @property
    def UseBorderAroundTheText(self) -> bool:
        """Get the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @UseBorderAroundTheText.setter
    def UseBorderAroundTheText(self, value: bool) -> None:
        """Set the rotation of the text in radians, never serialized, not in standard values, it is  a working property only
        """
    @property
    def UseConstantSizeInLayout(self) -> bool:
        """Get the When False: it means scale dependent
        """
    @UseConstantSizeInLayout.setter
    def UseConstantSizeInLayout(self, value: bool) -> None:
        """Set the When False: it means scale dependent
        """
    eBold = TextEmphasis_Enum.eBold
    eItalic = TextEmphasis_Enum.eItalic
    eLabel = TextPropertiesSource_Enum.eLabel
    eNone = TextEmphasis_Enum.eNone
    eSaaP_ClippingPath = TextPropertiesSource_Enum.eSaaP_ClippingPath
    eSaaP_Heading = TextPropertiesSource_Enum.eSaaP_Heading
    eSaaP_Scale = TextPropertiesSource_Enum.eSaaP_Scale
    eStrikethrough = TextEmphasis_Enum.eStrikethrough
    eUVS_AdvancedStyleClippingPath = TextPropertiesSource_Enum.eUVS_AdvancedStyleClippingPath
    eUVS_ClippingPath = TextPropertiesSource_Enum.eUVS_ClippingPath
    eUVS_Heading = TextPropertiesSource_Enum.eUVS_Heading
    eUVS_Scale = TextPropertiesSource_Enum.eUVS_Scale
    eUVS_USStyleHeading = TextPropertiesSource_Enum.eUVS_USStyleHeading
    eUVS_USStyleScale = TextPropertiesSource_Enum.eUVS_USStyleScale
    eUnderline = TextEmphasis_Enum.eUnderline

class SectionDefinitionData():
    """Section definition data
    """
    def __init__(self):
        """Initialize
        """
    @property
    def ClippingPath(self) -> None:
        """Set/get the clipping path

        :type: None
        """
    @property
    def DefinitionProperties(self) -> None:
        """Set/Get the definition properties

        :type: None
        """
    @property
    def DirectionVector(self) -> None:
        """Set/get the direction vector

        :type: None
        """

class SectionDefinitionProperties():
    """Section definition properties
    """
    class RefMode_Enum(enum.Enum):
        """View input type
        """
        eFolded = 1
        eObserver = 0

        names = {eObserver: eObserver,
                 eFolded: eFolded}

        values = {0: eObserver,
                  1: eFolded}

        def __getitem__(self, key: (str | int | float)) -> SectionDefinitionProperties.RefMode_Enum:
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
    @property
    def ClippingPathProperties(self) -> None:
        """Set/Get the clipping path properties

        :type: None
        """
    @property
    def IsSectionBodyOn(self) -> None:
        """Property for show the section body

        :type: None
        """
    @property
    def RefMode(self) -> None:
        """Property for the reference mode

        :type: None
        """
    eFolded = RefMode_Enum.eFolded
    eObserver = RefMode_Enum.eObserver

class SectionDrawingFilesProperties():
    """Class containing settings regarding which drawing files to be considered in a UVS
    """
    def __eq__(self, A: SectionDrawingFilesProperties) -> bool:
        """operator ==

        Args:
            A
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, A: SectionDrawingFilesProperties):
        """copy constructor

        Args:
            A
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def DrawingNumbers(self) -> (list[int] | NemAll_Python_Utility.VecIntList):
        """Numbers of the drawing files to consider in a UVS"""
    @DrawingNumbers.setter
    def DrawingNumbers(self, value: (list[int] | NemAll_Python_Utility.VecIntList)) -> None:
        """Set the drawing file numbers
        """

class SectionFilterProperties():
    """Representation of filter settings of a UVS
    """
    def __init__(self):
        """Initialize
        """
    @property
    def DrawingFilesProperties(self) -> None:
        """Settings regarding which drawing files are to be considered in the UVS"""
    @property
    def IsAssociativityOn(self) -> None:
        """Whether to update the UVS automatically"""
    @property
    def LayerProperties(self) -> None:
        """Settings regarding which layer are to be considered in the UVS"""

class SectionFormatProperties():
    """Section format properties
    """
    class SurfaceElements_Enum(enum.Enum):
        """Type of surface element
        """
        eFills = 2
        eFillsBitmaps = 3
        eNoElements = 1

        names = {eNoElements: eNoElements,
                 eFills: eFills,
                 eFillsBitmaps: eFillsBitmaps}

        values = {1: eNoElements,
                  2: eFills,
                  3: eFillsBitmaps}

        def __getitem__(self, key: (str | int | float)) -> SectionFormatProperties.SurfaceElements_Enum:
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
    def __init__(self, bInitFromSTW: bool):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def CosiderTransparancy(self) -> bool:
        """Get the property for the transparancy
        """
    @CosiderTransparancy.setter
    def CosiderTransparancy(self, value: bool) -> None:
        """Set the property for the transparancy
        """
    @property
    def EliminationAngle(self) -> float:
        """Boundary angle from which the adjacent edges are eliminated"""
    @EliminationAngle.setter
    def EliminationAngle(self, value: float) -> None:
        """Set the Adjacent Edge elimination angle
        """
    @property
    def FixtureAsWireframe(self) -> bool:
        """Get the fixture as wireframe
        """
    @FixtureAsWireframe.setter
    def FixtureAsWireframe(self, value: bool) -> None:
        """Set the fixture as wireframe
        """
    @property
    def IsEliminationOn(self) -> bool:
        """Whether to eliminate the adjacent edges"""
    @IsEliminationOn.setter
    def IsEliminationOn(self, value: bool) -> None:
        """Set the Adjacent Edge elimination
        """
    @property
    def SurfaceElements(self) -> SurfaceElements_Enum:
        """Get the surface elements
        """
    @SurfaceElements.setter
    def SurfaceElements(self, value: SurfaceElements_Enum) -> None:
        """Set the surface elements
        """
    eFills = SurfaceElements_Enum.eFills
    eFillsBitmaps = SurfaceElements_Enum.eFillsBitmaps
    eNoElements = SurfaceElements_Enum.eNoElements

class SectionGeneralProperties():
    """General properties of the UVS
    """
    class PlacementPointPosition(enum.Enum):
        """Placement point position
        """
        BottomCenter = 6
        BottomLeft = 1
        BottomRight = 2
        CenterCenter = 5
        CenterLeft = 9
        CenterRight = 7
        Offset = 0
        TopLeft = 4
        TopRight = 3

        names = {TopLeft: TopLeft,
                 TopRight: TopRight,
                 CenterLeft: CenterLeft,
                 CenterCenter: CenterCenter,
                 CenterRight: CenterRight,
                 BottomLeft: BottomLeft,
                 BottomCenter: BottomCenter,
                 BottomRight: BottomRight,
                 Offset: Offset}

        values = {4: TopLeft,
                  3: TopRight,
                  9: CenterLeft,
                  5: CenterCenter,
                  7: CenterRight,
                  1: BottomLeft,
                  6: BottomCenter,
                  2: BottomRight,
                  0: Offset}

        def __getitem__(self, key: (str | int | float)) -> SectionGeneralProperties.PlacementPointPosition:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class State(enum.Enum):
        """Drawing state of the section
        """
        AcceleratedHidden = 2
        Hidden = 0
        Wire = 1

        names = {Hidden: Hidden,
                 Wire: Wire,
                 AcceleratedHidden: AcceleratedHidden}

        values = {0: Hidden,
                  1: Wire,
                  2: AcceleratedHidden}

        def __getitem__(self, key: (str | int | float)) -> SectionGeneralProperties.State:
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
    def __init__(self, bInitFromSTW: bool):
        """constructor

        Args:
            bInitFromSTW: - is structure initialized from standard values
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def FilterProperties(self) -> FilterProperties:
        """Filtering settings of the UVS"""
    @FilterProperties.setter
    def FilterProperties(self, value: FilterProperties) -> None:
        """Property for the filter properties
        """
    @property
    def FormatProperties(self) -> SectionFormatProperties:
        """Format settings of a UVS"""
    @FormatProperties.setter
    def FormatProperties(self, value: SectionFormatProperties) -> None:
        """Property for the format properties
        """
    @property
    def HiddenSectionLinesProperties(self) -> HiddenSectionLinesProperties:
        """Settings regarding hidden section lines in the UVS"""
    @HiddenSectionLinesProperties.setter
    def HiddenSectionLinesProperties(self, value: HiddenSectionLinesProperties) -> None:
        """Property for the hidden section line properties
        """
    @property
    def LabelingProperties(self) -> LabelingProperties:
        """Settings regarding labeling the UVS"""
    @LabelingProperties.setter
    def LabelingProperties(self, value: LabelingProperties) -> None:
        """Property for the labeling properties
        """
    @property
    def LightProperties(self) -> LightProperties:
        """Property for the light properties
        """
    @LightProperties.setter
    def LightProperties(self, value: LightProperties) -> None:
        """Property for the light properties
        """
    @property
    def PlacementAngle(self) -> None:
        """Property for the placement angle

        :type: None
        """
    @property
    def PlacementPoint(self) -> None:
        """Property for the placement point

        :type: None
        """
    @property
    def ReferenceScale(self) -> float:
        """Property for the reference scale
        """
    @ReferenceScale.setter
    def ReferenceScale(self, value: float) -> None:
        """Property for the reference scale
        """
    @property
    def ScaleProperties(self) -> ScaleProperties:
        """Property for the scale properties
        """
    @ScaleProperties.setter
    def ScaleProperties(self, value: ScaleProperties) -> None:
        """Property for the scale properties
        """
    @property
    def ShowSectionBody(self) -> None:
        """Whether to show the section body in the UVS"""
    @property
    def Status(self) -> None:
        """Type of the UVS calculation"""
    @property
    def VisibleHiddenEdgesProperties(self) -> VisibleHiddenEdgesProperties:
        """Settings regarding hidden and visible lines in the UVS"""
    @VisibleHiddenEdgesProperties.setter
    def VisibleHiddenEdgesProperties(self, value: VisibleHiddenEdgesProperties) -> None:
        """Property for the visible and hidden edge properties
        """
    AcceleratedHidden = State.AcceleratedHidden
    BottomCenter = PlacementPointPosition.BottomCenter
    BottomLeft = PlacementPointPosition.BottomLeft
    BottomRight = PlacementPointPosition.BottomRight
    CenterCenter = PlacementPointPosition.CenterCenter
    CenterLeft = PlacementPointPosition.CenterLeft
    CenterRight = PlacementPointPosition.CenterRight
    Hidden = State.Hidden
    Offset = PlacementPointPosition.Offset
    TopLeft = PlacementPointPosition.TopLeft
    TopRight = PlacementPointPosition.TopRight
    Wire = State.Wire

class SectionLayerProperties():
    """Class containing settings regarding which layers are to be considered in a UVS
    """
    class eVisibilityFilterMode(enum.Enum):
        """Visible filter mode
        """
        eVisibilityFilterMode_ACTUAL = 2
        eVisibilityFilterMode_ALL_LAYERS = 3
        eVisibilityFilterMode_CUSTOM = 0
        eVisibilityFilterMode_Undefined = -1
        eVisibilityFilter_Modus_LAYERSET = 1

        names = {eVisibilityFilterMode_Undefined: eVisibilityFilterMode_Undefined,
                 eVisibilityFilterMode_CUSTOM: eVisibilityFilterMode_CUSTOM,
                 eVisibilityFilter_Modus_LAYERSET: eVisibilityFilter_Modus_LAYERSET,
                 eVisibilityFilterMode_ACTUAL: eVisibilityFilterMode_ACTUAL,
                 eVisibilityFilterMode_ALL_LAYERS: eVisibilityFilterMode_ALL_LAYERS}

        values = {-1: eVisibilityFilterMode_Undefined,
                  0: eVisibilityFilterMode_CUSTOM,
                  1: eVisibilityFilter_Modus_LAYERSET,
                  2: eVisibilityFilterMode_ACTUAL,
                  3: eVisibilityFilterMode_ALL_LAYERS}

        def __getitem__(self, key: (str | int | float)) -> SectionLayerProperties.eVisibilityFilterMode:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def SetLayerProperties(self, iVisibilityFilterMode: int, bAreInvisibleLyersStored: bool,
                           layerIdVector: NemAll_Python_Utility.VecUShortList):
        """Set the layer properties

        Args:
            iVisibilityFilterMode:     Type of selected filter mode (only for GUI)
            bAreInvisibleLyersStored:  When set to True, elements from layers in layerIdVector are filtered out. Otherwise elements from layers in layerIdVector are taken into consideration
            layerIdVector:             Elements belonging to these Layers should be filtered from source up to flag bAreInvisibleLyersStored
        """
    def __init__(self):
        """Initialize
        """
    eVisibilityFilterMode_ACTUAL = eVisibilityFilterMode.eVisibilityFilterMode_ACTUAL
    eVisibilityFilterMode_ALL_LAYERS = eVisibilityFilterMode.eVisibilityFilterMode_ALL_LAYERS
    eVisibilityFilterMode_CUSTOM = eVisibilityFilterMode.eVisibilityFilterMode_CUSTOM
    eVisibilityFilterMode_Undefined = eVisibilityFilterMode.eVisibilityFilterMode_Undefined
    eVisibilityFilter_Modus_LAYERSET = eVisibilityFilterMode.eVisibilityFilter_Modus_LAYERSET

class ShadingType(enum.Enum):
    """Shading style of filling
    """
    eFromCenter = 2
    eFromCorner = 1
    eLinear = 0
    eRound = 3

    names = {eLinear: eLinear,
             eFromCorner: eFromCorner,
             eFromCenter: eFromCenter,
             eRound: eRound}

    values = {0: eLinear,
              1: eFromCorner,
              2: eFromCenter,
              3: eRound}

    def __getitem__(self, key: (str | int | float)) -> ShadingType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SubType(enum.Enum):
    """Sub types of the element group property
    """
    eMultiLine3D = 1
    eMultiLine3D_Group = 2
    eUseNoSpecialSubType = 0

    names = {eUseNoSpecialSubType: eUseNoSpecialSubType,
             eMultiLine3D: eMultiLine3D,
             eMultiLine3D_Group: eMultiLine3D_Group}

    values = {0: eUseNoSpecialSubType,
              1: eMultiLine3D,
              2: eMultiLine3D_Group}

    def __getitem__(self, key: (str | int | float)) -> SubType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class SurfaceDefinition():
    """Surface resource definition
    """
    class SurfaceTextureID(enum.Enum):

        BUMP = 4
        DIFFUSE_AUTUMN = 2
        DIFFUSE_SPRING = 0
        DIFFUSE_SUMMER = 1
        DIFFUSE_WINTER = 3
        REFLECTION = 6
        ROUGHNESS = 5
        TEXTURE_NR = 7

        names = {DIFFUSE_SPRING: DIFFUSE_SPRING,
                 DIFFUSE_SUMMER: DIFFUSE_SUMMER,
                 DIFFUSE_AUTUMN: DIFFUSE_AUTUMN,
                 DIFFUSE_WINTER: DIFFUSE_WINTER,
                 BUMP: BUMP,
                 ROUGHNESS: ROUGHNESS,
                 REFLECTION: REFLECTION,
                 TEXTURE_NR: TEXTURE_NR}

        values = {0: DIFFUSE_SPRING,
                  1: DIFFUSE_SUMMER,
                  2: DIFFUSE_AUTUMN,
                  3: DIFFUSE_WINTER,
                  4: BUMP,
                  5: ROUGHNESS,
                  6: REFLECTION,
                  7: TEXTURE_NR}

        def __getitem__(self, key: (str | int | float)) -> SurfaceDefinition.SurfaceTextureID:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    def CompareData(self, ldef: SurfaceDefinition) -> bool:
        """compare the surface properties

        Args:
            ldef
        """
    def CopyData(self, pSrcSurface: SurfaceDefinition, bCopyName: bool = True):
        """copy the data from an other surface

        Args:
            pSrcSurface
            bCopyName
        """
    @staticmethod
    def Create() -> SurfaceDefinition:
        """Create a surface definition
        """
    def Dump(self, deep: bool):
        """Dumps content of the resource

        Args:
            deep
        """
    def GetDiffuseFactor(self) -> float:
        """get the diffuse factor calculated from diffuse color intensity, reflection intensity and the transparency intensity
        """
    def GetHash(self) -> int:
        """get the hash of the surface definition data
        """
    def GetReflectionFactor(self) -> float:
        """calculate the reflection factor from transparency and reflection intensity
        """
    def GetScaleU(self) -> float:
        """get the texture u scale factor
        """
    def GetScaleV(self) -> float:
        """get the texture v scale factor
        """
    def GetSeasonStatus(self) -> bool:
        """get the surface season flag , true - not all color texture are the same
        """
    def GetSurfaceName(self) -> str:
        """get the surface name
        """
    def GetTextureID(self, tex: SurfaceTextureID) -> int:
        """get the bitmap id of the texture

        Args:
            tex
        """
    def GetTranslateU(self) -> float:
        """get the texture u offset
        """
    def GetTranslateV(self) -> float:
        """get the texture v offset
        """
    def IsDefault(self) -> bool:
        """check whether the surface properties has default values
        """
    def LoadSurfaceData(self, surfacePath: str):
        """load surface properties only

        Args:
            surfacePath
        """
    def PreviewCalculationSkipped(self) -> bool:
        """
        """
    def Save(self, surfacePath: str, bitmapDict: typing.Dict[SurfaceDefinition.SurfaceTextureID, BitmapDefinition]) -> bool:
        """Create a surface definition

        Returns:
               Creation successful state

        Args:
            surfacePath:        Path of the bitmap
            bitmapDefinitions:  Dict with the bitmap definitions
        """
    def SetScale(self, u: float, v: float):
        """set the texture scaling factors -10000 to 10000

        Args:
            u
            v
        """
    def SetTextureID(self, tex: SurfaceTextureID, bitmapID: int):
        """set the bitmapID for one texture

        Args:
            tex
            bitmapID
        """
    def SetTranslate(self, u: float, v: float):
        """set the texture offset -INT_MAX to INT_MAX

        Args:
            u
            v
        """
    @property
    def AbsolutePath(self) -> str:
        """get the absolute path of the surface, outside from the design path
        """
    @AbsolutePath.setter
    def AbsolutePath(self, value: str) -> None:
        """set the absolute path for the surface, used when the surface is outside from the design folder
        """
    @property
    def AlphaFromTextureStatus(self) -> bool:
        """get the flag for using alpha channel from the color bitmap
        """
    @AlphaFromTextureStatus.setter
    def AlphaFromTextureStatus(self, value: bool) -> None:
        """set the flag for using alpha channel from the color bitmap
        """
    @property
    def BumpAmplitude(self) -> float:
        """get bump mapping amplitude
        """
    @BumpAmplitude.setter
    def BumpAmplitude(self, value: float) -> None:
        """set bump mapping amplitude -1000 to 1000
        """
    @property
    def ColorKey(self) -> ARGB:
        """get the color key color
        """
    @ColorKey.setter
    def ColorKey(self, value: ARGB) -> None:
        """set the color key color
        """
    @property
    def ColorKeyStatus(self) -> bool:
        """get the flag for using color key
        """
    @ColorKeyStatus.setter
    def ColorKeyStatus(self, value: bool) -> None:
        """Set the value
        """
    @property
    def ColorKeyTolerance(self) -> int:
        """get the color key tolerance 0-255
        """
    @ColorKeyTolerance.setter
    def ColorKeyTolerance(self, value: int) -> None:
        """set the color key tolerance 0-255
        """
    @property
    def ColorMixingFactor(self) -> int:
        """get the color mixing factor, 0 - 100
        """
    @ColorMixingFactor.setter
    def ColorMixingFactor(self, value: int) -> None:
        """set the color mixing factor, 0 - 100
        """
    @property
    def ColorMixingMode(self) -> int:
        """get the color mixing mode.
        """
    @ColorMixingMode.setter
    def ColorMixingMode(self, value: int) -> None:
        """set the color mixing mode. 0 - normal, 1 - multiply
        """
    @property
    def DiffuseColor(self) -> ARGB:
        """get the diffuse color
        """
    @DiffuseColor.setter
    def DiffuseColor(self, value: ARGB) -> None:
        """set the diffuse color
        """
    @property
    def DiffuseReflectivity(self) -> int:
        """get the diffuse color intensity
        """
    @DiffuseReflectivity.setter
    def DiffuseReflectivity(self, value: int) -> None:
        """set the diffuse color intensity
        """
    @property
    def Emission(self) -> float:
        """get the color emission intensity
        """
    @Emission.setter
    def Emission(self, value: float) -> None:
        """set the color emission intensity, 0 - 10
        """
    @property
    def MetricStatus(self) -> bool:
        """get the flag for texture scale dependency from the object size. true - texture is scaled independently from the object size
        """
    @MetricStatus.setter
    def MetricStatus(self, value: bool) -> None:
        """set the flag for texture scale dependency from the object size. true - texture is scaled independently from the object size
        """
    @property
    def MultiToneFactor(self) -> float:
        """get the coating reflection intensity
        """
    @MultiToneFactor.setter
    def MultiToneFactor(self, value: float) -> None:
        """set the coating reflection intensity 0 - 100
        """
    @property
    def NormalMapStatus(self) -> bool:
        """get the flag for using normal map texture in bump map, otherwise it will be height map
        """
    @NormalMapStatus.setter
    def NormalMapStatus(self, value: bool) -> None:
        """set the flag for using normal map texture in bump map, otherwise it will be height map
        """
    @property
    def NotFound(self) -> bool:
        """get the flag for not found surface file
        """
    @NotFound.setter
    def NotFound(self, value: bool) -> None:
        """set the flag indicating, that the surface file was not found
        """
    @property
    def ParallaxOffset(self) -> float:
        """get the parallax offset
        """
    @ParallaxOffset.setter
    def ParallaxOffset(self, value: float) -> None:
        """set the parallax offset -1000 to 1000
        """
    @property
    def ParallaxSamples(self) -> int:
        """get parallax samples
        """
    @ParallaxSamples.setter
    def ParallaxSamples(self, value: int) -> None:
        """set parallax samples 2 - 200
        """
    @property
    def Reflection(self) -> int:
        """get the reflection amplitude
        """
    @Reflection.setter
    def Reflection(self, value: int) -> None:
        """set the reflection amplitude 0 - 100
        """
    @property
    def Refraction(self) -> float:
        """get the IOR
        """
    @Refraction.setter
    def Refraction(self, value: float) -> None:
        """set the IOR 1 - 2.5
        """
    @property
    def RelativeName(self) -> str:
        """get the relative path and name of the surface, under the design folder
        """
    @RelativeName.setter
    def RelativeName(self, value: str) -> None:
        """set the relative name of the surface, relative path under the design folder and the file name
        """
    @property
    def RepeatStatus(self) -> bool:
        """get the flag for texture repeating
        """
    @RepeatStatus.setter
    def RepeatStatus(self, value: bool) -> None:
        """set the flag for texture repeating
        """
    @property
    def Rotation(self) -> float:
        """get the texture rotation angle in degrees
        """
    @Rotation.setter
    def Rotation(self, value: float) -> None:
        """set the texture rotation angle in degrees -180 to 180
        """
    @property
    def Roughness(self) -> float:
        """get the roughness amplitude
        """
    @Roughness.setter
    def Roughness(self, value: float) -> None:
        """set the roughness amplitude 0 - 100
        """
    @property
    def Transparency(self) -> int:
        """get the transparency intensity
        """
    @Transparency.setter
    def Transparency(self, value: int) -> None:
        """set the transparency intensity 0 - 100
        """
    BUMP = SurfaceTextureID.BUMP
    DIFFUSE_AUTUMN = SurfaceTextureID.DIFFUSE_AUTUMN
    DIFFUSE_SPRING = SurfaceTextureID.DIFFUSE_SPRING
    DIFFUSE_SUMMER = SurfaceTextureID.DIFFUSE_SUMMER
    DIFFUSE_WINTER = SurfaceTextureID.DIFFUSE_WINTER
    REFLECTION = SurfaceTextureID.REFLECTION
    ROUGHNESS = SurfaceTextureID.ROUGHNESS
    TEXTURE_NR = SurfaceTextureID.TEXTURE_NR

class Symbol2DElement(BasisElement, AllplanElement):
    """Representation of the **point symbol** in Allplan
    """
    def GetSymbol2DProperties(self) -> Symbol2DProperties:
        """Get the Symbol2D properties

        Returns:
             Symbol2D properties
        """
    def SetSymbol2DProperties(self, symbol2DProp: Symbol2DProperties):
        """Set the Symbol2D properties

        Args:
            symbol2DProp: Symbol2D properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, Symbol2DProp: Symbol2DProperties, geometryObject: object):
        """Constructor

        Args:
            commonProp:        Common properties
            Symbol2DProp:      Symbol2D properties
            geometryObject:    Geometry element
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class Symbol2DProperties():
    """Properties of the point symbol
    """
    def __eq__(self, prop: Symbol2DProperties) -> bool:
        """equal operator

        Args:
            prop: Symbol2DProperties to compare

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
    def Height(self) -> None:
        """Symbol height"""
    @property
    def IsScaleDependent(self) -> None:
        """Whether the symbol should be scale dependent"""
    @property
    def PrimaryPointNumber(self) -> None:
        """Primary point number"""
    @property
    def RotationAngle(self) -> None:
        """Rotation angle"""
    @property
    def SecondaryPointNumber(self) -> None:
        """Secondary point number"""
    @property
    def SymbolID(self) -> None:
        """Symbol ID"""
    @property
    def Width(self) -> None:
        """Symbol width"""

class Symbol3DElement(BasisElement, AllplanElement):
    """Representation of the **terrain point** in Allplan
    """
    def GetSymbol3DProperties(self) -> Symbol3DProperties:
        """Get the Symbol3D properties

        Returns:
             Symbol3D properties
        """
    def SetSymbol3DProperties(self, symbol3DProp: Symbol3DProperties):
        """Set the Symbol3D properties

        Args:
            symbol3DProp: Symbol3D properties
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, Symbol3DProp: Symbol3DProperties, geometryObject: object):
        """Constructor

        Args:
            commonProp:        Common properties
            symbol3DProp:      Symbol3D properties
            geometryObject:    Geometry element
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

class Symbol3DProperties():
    """Properties of the terrain point
    """
    def __eq__(self, prop: Symbol3DProperties) -> bool:
        """equal operator

        Args:
            prop: Symbol3DProperties to compare

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
    def ControlPointOffset(self) -> None:
        """Control point offset"""
    @property
    def DescriptionText(self) -> None:
        """Description text (label)"""
    @property
    def Height(self) -> None:
        """Symbol height"""
    @property
    def IsScaleDependent(self) -> None:
        """Whether the point is to be scale dependent"""
    @property
    def IsStation(self) -> None:
        """Whether the point is a station"""
    @property
    def PrimaryPointNumber(self) -> None:
        """Primary point number"""
    @property
    def RotationAngle(self) -> None:
        """Rotation angle"""
    @property
    def SecondaryPointNumber(self) -> None:
        """Secondary point number"""
    @property
    def StationCode(self) -> None:
        """Point code or station depending on the value of _IsStation_ property."""
    @property
    def SymbolID(self) -> None:
        """Symbol ID"""
    @property
    def Width(self) -> None:
        """Symbol width"""

class TextAlignment(enum.Enum):
    """Types of text alignments

    eTextAlignment is alignment related to first line.
    This point is anchor in case of resizing or rotating of element.
    Placement point of text is set on this point.
    """
    eLeftBottom = 1
    eLeftMiddle = 9
    eLeftTop = 4
    eMiddleBottom = 6
    eMiddleMiddle = 5
    eMiddleTop = 8
    eRightBottom = 2
    eRightMiddle = 7
    eRightTop = 3

    names = {eLeftBottom: eLeftBottom,
             eRightBottom: eRightBottom,
             eRightTop: eRightTop,
             eLeftTop: eLeftTop,
             eMiddleMiddle: eMiddleMiddle,
             eMiddleBottom: eMiddleBottom,
             eRightMiddle: eRightMiddle,
             eMiddleTop: eMiddleTop,
             eLeftMiddle: eLeftMiddle}

    values = {1: eLeftBottom,
              2: eRightBottom,
              3: eRightTop,
              4: eLeftTop,
              5: eMiddleMiddle,
              6: eMiddleBottom,
              7: eRightMiddle,
              8: eMiddleTop,
              9: eLeftMiddle}

    def __getitem__(self, key: (str | int | float)) -> TextAlignment:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextElement(BasisElement, AllplanElement):
    """Representation of **text** in Allplan
    """
    def GetDimensions(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> NemAll_Python_Geometry.Vector2D:
        """Get the dimensions of the text

        Args:
            doc: Document

        Returns:
            Text dimensions
        """
    def GetText(self) -> str:
        """Get the text string

        Returns:
            Text string
        """
    def GetTextPoints(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                      refPnt: NemAll_Python_Geometry.Point2D) -> NemAll_Python_Geometry.Point2DList:
        """Get the list of text points composed as follows:

        -   0:  Bottom left point
        -   1:  Bottom right point
        -   2:  Top right point
        -   3:  Top left point
        -   4:  Middle bottom point
        -   5:  Middle right point
        -   6:  Middle top point
        -   7:  Middle left point

        Args:
            doc:     Document
            refPnt:  Reference point

        Returns:
            Text points
        """
    def GetTextProperties(self) -> TextProperties:
        """Get the Text properties

        Returns:
            Text properties
        """
    def SetText(self, text: str):
        """Set the text string

        Args:
            text: Text string
        """
    def SetTextProperties(self, textProp: TextProperties):
        """Set the Text properties

        Args:
            textProp: Text properties
        """
    def __eq__(self, textEle: TextElement) -> bool:
        """Comparison operator

        Args:
            textEle: Text element to compare

        Returns:
            Comparison state
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, commonProp: NemAll_Python_BaseElements.CommonProperties, textProp: TextProperties, text: str,
                 textPnt: NemAll_Python_Geometry.Point2D):
        """Constructor

        Args:
            commonProp: Common properties
            textProp:   Text properties
            text:       Text string
            textPnt:    Text point
        """
    @typing.overload
    def __init__(self, element: TextElement):
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
    def Text(self) -> str:
        """Representation of **text** in Allplan"""
    @Text.setter
    def Text(self, text: str) -> None:
        """Set the text string

        Args:
            text: Text string
        """
    @property
    def TextProperties(self) -> TextProperties:
        """Get the Text properties
        """
    @TextProperties.setter
    def TextProperties(self, textProp: TextProperties) -> None:
        """Set the Text properties

        Args:
            textProp: Text properties
        """

class TextElementList():
    """List for TextElement objects
    """
    def __contains__(self, value: TextElement) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: TextElement):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: TextElementList) -> bool:
        """Compare two lists

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> TextElement:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, eleList: list) -> TextElementList:
        """Add a list

        Args:
            eleList: TextElement list

        Returns:
            Lists with the added elements
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, ele: TextElement):
        """Constructor with a TextElement

        Args:
            ele: TextElement
        """
    @typing.overload
    def __init__(self, eleList: list):
        """Constructor with a list of TextElement

        Args:
            eleList: TextElement list
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
    def __setitem__(self, index: int | slice, value: TextElement):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: TextElement):
        """Append a list item

        Args:
            value: Value to append
        """
    @typing.overload
    def extend(self, iterable: TextElementList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    @typing.overload
    def extend(self, eleList: list):
        """Extend the list

        Args:
            eleList: TextElement list
        """
    def extend(self):
        """ Overloaded function. See individual overloads.
        """

class TextLocation(enum.Enum):
    """Location of the dimension text relative to the dimension line
    """
    eBASIS_DIM_BOTTOM_CENTER = -2
    """Below the line, in the middle"""
    eBASIS_DIM_BOTTOM_LEFT = -1
    """Below the line, at the start"""
    eBASIS_DIM_BOTTOM_RIGHT = -3
    """Below the line, at the end"""
    eBASIS_DIM_CENTER = 0
    """On the line, in the middle"""
    eBASIS_DIM_CENTER_LEFT = -4
    """On the line, at the start"""
    eBASIS_DIM_CENTER_RIGHT = -5
    """On the line, at the end"""
    eBASIS_DIM_NONE = 10
    """Undefined"""
    eBASIS_DIM_TOP_CENTER = 2
    """Above the line, in the middle"""
    eBASIS_DIM_TOP_LEFT = 1
    """Above the line, at the start"""
    eBASIS_DIM_TOP_RIGHT = 3
    """Above the line, at the end"""

    names = {eBASIS_DIM_CENTER_LEFT: eBASIS_DIM_CENTER_LEFT,
             eBASIS_DIM_CENTER: eBASIS_DIM_CENTER,
             eBASIS_DIM_CENTER_RIGHT: eBASIS_DIM_CENTER_RIGHT,
             eBASIS_DIM_BOTTOM_LEFT: eBASIS_DIM_BOTTOM_LEFT,
             eBASIS_DIM_BOTTOM_CENTER: eBASIS_DIM_BOTTOM_CENTER,
             eBASIS_DIM_BOTTOM_RIGHT: eBASIS_DIM_BOTTOM_RIGHT,
             eBASIS_DIM_TOP_LEFT: eBASIS_DIM_TOP_LEFT,
             eBASIS_DIM_TOP_CENTER: eBASIS_DIM_TOP_CENTER,
             eBASIS_DIM_TOP_RIGHT: eBASIS_DIM_TOP_RIGHT,
             eBASIS_DIM_NONE: eBASIS_DIM_NONE}

    values = {-4: eBASIS_DIM_CENTER_LEFT,
              0: eBASIS_DIM_CENTER,
              -5: eBASIS_DIM_CENTER_RIGHT,
              -1: eBASIS_DIM_BOTTOM_LEFT,
              -2: eBASIS_DIM_BOTTOM_CENTER,
              -3: eBASIS_DIM_BOTTOM_RIGHT,
              1: eBASIS_DIM_TOP_LEFT,
              2: eBASIS_DIM_TOP_CENTER,
              3: eBASIS_DIM_TOP_RIGHT,
              10: eBASIS_DIM_NONE}

    def __getitem__(self, key: (str | int | float)) -> TextLocation:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextProperties():
    """Implementation of the text properties
    """
    def GetRatio(self) -> float:
        """Get text height/width ratio

        Returns:
          height/width ratio
        """
    def Init(self):
        """Init section properties with default values
        """
    def IsDraftText(self) -> bool:
        """Check if the text is a draft text (unprintable)

        Returns:
          True if text is unprintable, otherwise False
        """
    def SetHasBackgroundColorAndTransparentBackgroundColor(self, value: bool):
        """Setting for filling the text background with the color of the viewport

        Args:
            value:  Set to to True to turn the background filling on.
        """
    def __eq__(self, prop: TextProperties) -> bool:
        """equal operator

        Args:
            prop: TextProperties to compare

        Returns:
            true if they are equal, false otherwise
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: TextProperties):
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
    def Alignment(self) -> TextAlignment:
        """Text alignment"""
    @Alignment.setter
    def Alignment(self, value: TextAlignment) -> None:
        """Set the Alignment of text
        """
    @property
    def BackgroundColor(self) -> int:
        """Background color of the text"""
    @BackgroundColor.setter
    def BackgroundColor(self, value: int) -> None:
        """Set the Background color of text
        """
    @property
    def ColumnSlopeAngle(self) -> NemAll_Python_Geometry.Angle:
        """Slope angle of columns in [rad]"""
    @ColumnSlopeAngle.setter
    def ColumnSlopeAngle(self, value: NemAll_Python_Geometry.Angle) -> None:
        """Set the Angle of columns in [rad]
        """
    @property
    def Expansion(self) -> int:
        """Text expansion"""
    @Expansion.setter
    def Expansion(self, value: int) -> None:
        """Set the Background color of text
        """
    @property
    def Font(self) -> int:
        """Font ID"""
    @Font.setter
    def Font(self, value: int) -> None:
        """Set the Default font name
        """
    @property
    def FontAngle(self) -> NemAll_Python_Geometry.Angle:
        """Angle of characters (italic) in [rad]"""
    @FontAngle.setter
    def FontAngle(self, value: NemAll_Python_Geometry.Angle) -> None:
        """Set the Angle of characters (italic) in [rad]
        """
    @property
    def FontStyles(self) -> int:
        """Font style (Bold, Italic, Underline, Crossed out) via bits, where:

        -   the first bit from right indicates the bold state
        -   the second bit from right indicates the italic state
        -   the third bit from right indicates the underlined state
        -   the fourth bit from right indicates the crossed out state
        """
    @FontStyles.setter
    def FontStyles(self, value: int) -> None:
        """Set the FontStyles Bold, Italic, Underline, Crossed out via bits
        """
    @property
    def HasBackgroundColor(self) -> bool:
        """Whether the text has a background color"""
    @HasBackgroundColor.setter
    def HasBackgroundColor(self, value: bool) -> None:
        """check eHasTextBgColor property flag

        return true if eHasTextBgColor is set otherwise return false

        Set eHasTextBgColor flag

        Args:
            value: eHasTextBgColor flag
        """
    @property
    def HasReferencePoint(self) -> bool:
        """Whether the text has a reference point"""
    @HasReferencePoint.setter
    def HasReferencePoint(self, value: bool) -> None:
        """check eHasReferencePoint property flag

        return true if eHasReferencePoint is set otherwise return false

        Set eHasReferencePoint flag

        Args:
            value: eHasReferencePoint flag
        """
    @property
    def HasTextFrame(self) -> bool:
        """Whether to draw border around text"""
    @HasTextFrame.setter
    def HasTextFrame(self, value: bool) -> None:
        """check text frame active

        return true if text frame is active otherwise return false

        Set text frame active

        Args:
            value: text frame active
        """
    @property
    def HasTransparentBackground(self) -> bool:
        """Whether the text background is to be transparent"""
    @HasTransparentBackground.setter
    def HasTransparentBackground(self, value: bool) -> None:
        """check eHasTransparentBackground property flag

        return true if eHasTransparentBackground is set otherwise return false

        Set eHasTransparentBackground flag
        """
    @property
    def Height(self) -> float:
        """Height of text in [mm]"""
    @Height.setter
    def Height(self, value: float) -> None:
        """Set the Height of text in [mm]
        """
    @property
    def IsScaleDependent(self) -> bool:
        """Whether the text is to be scale dependent"""
    @IsScaleDependent.setter
    def IsScaleDependent(self, value: bool) -> None:
        """check eIsScaleDependent property flag

        return true if eIsScaleDependent is set otherwise return false

        Set scale dependent flag

        Args:
            value: scale dependent flag
        """
    @property
    def IsUserModifiable(self) -> bool:
        """Whether the text should be modifiable by the user"""
    @IsUserModifiable.setter
    def IsUserModifiable(self, value: bool) -> None:
        """Check if user can modify text

        return true if user can modify text

        Set negation of the eNotUserModifiable flag

        Args:
            value: negation of the eNotUserModifiable flag
        """
    @property
    def LineFeed(self) -> float:
        """Line feed of text in [mm]"""
    @LineFeed.setter
    def LineFeed(self, value: float) -> None:
        """Set the Line feed of text in [mm]
        """
    @property
    def TextAngle(self) -> NemAll_Python_Geometry.Angle:
        """Angle of whole text in [rad]"""
    @TextAngle.setter
    def TextAngle(self, value: NemAll_Python_Geometry.Angle) -> None:
        """Set the Angle of hole text in [rad]
        """
    @property
    def TextFrameColor(self) -> int:
        """Color ID of the text frame color"""
    @TextFrameColor.setter
    def TextFrameColor(self, value: int) -> None:
        """Set text frame color value

        Args:
            value: Text frame color value
        """
    @property
    def TextFramePen(self) -> int:
        """Pen ID of the text frame"""
    @TextFramePen.setter
    def TextFramePen(self, value: int) -> None:
        """Set text frame pen value

        Args:
            value: Text frame pen value
        """
    @property
    def TextFrameStroke(self) -> int:
        """Stroke ID of the text frame"""
    @TextFrameStroke.setter
    def TextFrameStroke(self, value: int) -> None:
        """Set text frame stroke value

        Args:
            value: Text frame stroke value
        """
    @property
    def Type(self) -> TextType:
        """Text type (0 - normal text, >1 variable text)"""
    @Type.setter
    def Type(self, value: TextType) -> None:
        """Set the Text type (0 - normal text, >1 variable text)
        """
    @property
    def Width(self) -> float:
        """Text width in [mm]"""
    @Width.setter
    def Width(self, value: float) -> None:
        """Set the Width of text in [mm]
        """
    @property
    def WrappedText(self) -> bool:
        """Whether to use text wrapping."""
    @WrappedText.setter
    def WrappedText(self, value: bool) -> None:
        """Set the Wrapping on/off used when wrappingWidth > 0
        """
    @property
    def WrappingWidth(self) -> float:
        """Wrapping width. Used when wrapping is active"""
    @WrappingWidth.setter
    def WrappingWidth(self, value: float) -> None:
        """Set the Wrapping width used when wrapping is on
        """

class TextType(enum.Enum):
    """Types of text element
    """
    eFormularText = 1
    eNormalText = 0
    eVariableText = 2

    names = {eNormalText: eNormalText,
             eFormularText: eFormularText,
             eVariableText: eVariableText}

    values = {0: eNormalText,
              1: eFormularText,
              2: eVariableText}

    def __getitem__(self, key: (str | int | float)) -> TextType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextureDefinition():
    """Representation of the texture definition
    """
    def __eq__(self, props: TextureDefinition) -> bool:
        """Compare operator

        Args:
            props: Properties to compare

        Returns:
             Properties a equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, surfacePath: str):
        """Constructor

        Args:
            surfacePath: Surface path of texture definition
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
    def SurfacePath(self) -> None:
        """Property for surface path

        :type: None
        """

class TextureMapping():
    """Texture mapping property class
    """
    def FromSurfaceMapping(self, mapping: object):
        """Get the properties from the surface mapping object

        Args:
            mapping: Surface mapping
        """
    def __eq__(self, props: TextureMapping) -> bool:
        """Compare operator

        Args:
            props: Properties to compare

        Returns:
            Properties a equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, mappingType: TextureMappingType, mappingAngle: float, scaleX: float, scaleY: float, offsetX: float, offsetY: float,
                 phongAngle: float, refFace: int, refEdge: int):
        """Constructor

        Args:
            mappingType:  Mapping type
            mappingAngle: Mapping angle
            scaleX:       Mapping scale in X-axis
            scaleY:       Mapping scale in Y-axis
            offsetX:      X offset
            offsetY:      Y offset
            phongAngle:   Angle for Phong light model
            refFace:      Reference face
            refEdge:      Reference edge
        """
    @typing.overload
    def __init__(self, mappingType: TextureMappingType, mappingAngle: float, scaleX: float, scaleY: float, offsetX: float, offsetY: float,
                 phongAngle: float, refFace: int, refEdge: int, uvCoords: NemAll_Python_Utility.VecDoubleList):
        """Constructor

        Args:
            mappingType:  Mapping type
            mappingAngle: Mapping angle
            scaleX:       Mapping scale in X-axis
            scaleY:       Mapping scale in Y-axis
            offsetX:      X offset
            offsetY:      Y offset
            phongAngle:   Angle for Phong light model
            refFace:      Reference face
            refEdge:      Reference edge
            uvCoords:     UV coordinates
        """
    @typing.overload
    def __init__(self, uvCoords: NemAll_Python_Utility.VecDoubleList):
        """Constructor, set the type to eUV

        Args:
            uvCoords: UV coordinates
        """
    @typing.overload
    def __init__(self, element: TextureMapping):
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
    def MappingAngle(self) -> float:
        """Get mapping angle
        """
    @MappingAngle.setter
    def MappingAngle(self, value: float) -> None:
        """Set mapping angle
        """
    @property
    def MappingType(self) -> eMappingType:
        """Get mapping type
        """
    @MappingType.setter
    def MappingType(self, value: eMappingType) -> None:
        """Set mapping type
        """
    @property
    def PhongAngle(self) -> float:
        """Get angle for Phong light model
        """
    @PhongAngle.setter
    def PhongAngle(self, value: float) -> None:
        """Set angle for Phong light model
        """
    @property
    def ReferenceEdge(self) -> int:
        """Get reference edge
        """
    @ReferenceEdge.setter
    def ReferenceEdge(self, value: int) -> None:
        """Set reference edge
        """
    @property
    def ReferenceFace(self) -> int:
        """Get reference face
        """
    @ReferenceFace.setter
    def ReferenceFace(self, value: int) -> None:
        """Set reference face
        """
    @property
    def UVCoordinates(self) -> list[float]:
        """Get UV texture mapping coordinates
        """
    @UVCoordinates.setter
    def UVCoordinates(self, value: list[float]) -> None:
        """Set UV texture mapping coordinates
        """
    @property
    def UValueForIsoLines(self) -> int:
        """Get U count of isolines
        """
    @UValueForIsoLines.setter
    def UValueForIsoLines(self, value: int) -> None:
        """Set U count of isolines
        """
    @property
    def VValueForIsoLines(self) -> int:
        """Get V count of isolines
        """
    @VValueForIsoLines.setter
    def VValueForIsoLines(self, value: int) -> None:
        """Set V count of isolines
        """
    @property
    def XOffset(self) -> float:
        """Get X offset
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None:
        """Set X offset
        """
    @property
    def XScale(self) -> float:
        """Get mapping X scale
        """
    @XScale.setter
    def XScale(self, value: float) -> None:
        """Set mapping X scale
        """
    @property
    def YOffset(self) -> float:
        """Get Y offset
        """
    @YOffset.setter
    def YOffset(self, value: float) -> None:
        """Set Y offset
        """
    @property
    def YScale(self) -> float:
        """Get mapping Y scale
        """
    @YScale.setter
    def YScale(self, value: float) -> None:
        """Set mapping Y scale
        """

class TextureMappingType(enum.Enum):
    """Types of texture mapping
    """
    eCube = 0
    """From each side"""
    eCylinder = 4
    """Cylindrical mapping"""
    eGround = 3
    """Only from the top view"""
    eRoof = 2
    """Mainly from the top view"""
    eSphere = 5
    """Spherical mapping"""
    eUV = 6
    """UV mapping"""
    eWall = 1
    """Mainly from the front view"""

    names = {eCube: eCube,
             eWall: eWall,
             eRoof: eRoof,
             eGround: eGround,
             eCylinder: eCylinder,
             eSphere: eSphere,
             eUV: eUV}

    values = {0: eCube,
              1: eWall,
              2: eRoof,
              3: eGround,
              4: eCylinder,
              5: eSphere,
              6: eUV}

    def __getitem__(self, key: (str | int | float)) -> TextureMappingType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TransitionType(enum.Enum):
    """Transition types of the color gradients of filling
    """
    eNoTransition = 0
    """Without gradients"""
    eOneColorTransition = 1
    """Single-colored gradients"""
    eTwoColorTransition = 2
    """Two-colored gradients"""

    names = {eNoTransition: eNoTransition,
             eOneColorTransition: eOneColorTransition,
             eTwoColorTransition: eTwoColorTransition}

    values = {0: eNoTransition,
              1: eOneColorTransition,
              2: eTwoColorTransition}

    def __getitem__(self, key: (str | int | float)) -> TransitionType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class VariantType(enum.Enum):
    """Variant types of the filling color gradient
    """
    eVariant1 = 0
    """Color1 to Color2"""
    eVariant2 = 1
    """Color2 to Color1"""
    eVariant3 = 2
    """Color2 to Color1 to Color2"""
    eVariant4 = 3
    """Color1 to Color2 to Color1"""

    names = {eVariant1: eVariant1,
             eVariant2: eVariant2,
             eVariant3: eVariant3,
             eVariant4: eVariant4}

    values = {0: eVariant1,
              1: eVariant2,
              2: eVariant3,
              3: eVariant4}

    def __getitem__(self, key: (str | int | float)) -> VariantType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ViewSectionElement(AllplanElement):
    """Representation of a **Unified View and Section (UVS)** in Allplan
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, param: ViewSectionElement):
        """Implementation of the view section element

        Args:
            param
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def BarLabels(self) -> NemAll_Python_Reinforcement.BarLabel]:
        """Get the bar labels
        """
    @BarLabels.setter
    def BarLabels(self, barLabels: NemAll_Python_Reinforcement.BarLabel]) -> None:
        """Set the bar labels

        Args:
            barLabels: Bar labels
        """
    @property
    def DimensionElements(self) -> list:
        """Dimension elements"""
    @DimensionElements.setter
    def DimensionElements(self, dimensionElements: list) -> None:
        """Set the dimension elements

        Args:
            dimensionElements: Dimension elements
        """
    @property
    def GeneralSectionProperties(self) -> UVS_GeneralSectionProperties:
        """General section properties"""
    @GeneralSectionProperties.setter
    def GeneralSectionProperties(self, generalSectionProperties: UVS_GeneralSectionProperties) -> None:
        """Set the general properties

        Args:
            generalSectionProperties: General properties
        """
    @property
    def MeshLabels(self) -> NemAll_Python_Reinforcement.MeshLabel]:
        """Get the mesh labels
        """
    @MeshLabels.setter
    def MeshLabels(self, meshLabels: NemAll_Python_Reinforcement.MeshLabel]) -> None:
        """Set the mesh labels

        Args:
            meshLabels: Mesh labels
        """
    @property
    def ReinforcementLabels(self) -> NemAll_Python_Reinforcement.BarLabel]:
        """Reinforcement labels"""
    @ReinforcementLabels.setter
    def ReinforcementLabels(self, reinforcementLabels: NemAll_Python_Reinforcement.BarLabel]) -> None:
        """Set the bar labels (deprecated: use SetBarLabels)

        Args:
            reinforcementLabels: reinforcementLabels
        """
    @property
    def SectionDefinitionData(self) -> UnifiedSectionDefinitionData:
        """Section definition data"""
    @SectionDefinitionData.setter
    def SectionDefinitionData(self, sectionDefinitionData: UnifiedSectionDefinitionData) -> None:
        """Set the section definition data

        Args:
            sectionDefinitionData: Section definition data
        """
    @property
    def TextElements(self) -> list:
        """Labels"""
    @TextElements.setter
    def TextElements(self, textElements: list) -> None:
        """Set the text elements

        Args:
            textElements: Text elements
        """
    @property
    def ViewMatrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """View transformation matrix"""
    @ViewMatrix.setter
    def ViewMatrix(self, viewMatrix: NemAll_Python_Geometry.Matrix3D) -> None:
        """Set the view matrix

        Args:
            viewMatrix: View matrix
        """

class VisibleHiddenEdgesProperties():
    """Properties of the visible and hidden edges in a UVS
    """
    def __init__(self):
        """Initialize
        """
    @property
    def HiddenEdgesColor(self) -> None:
        """Color ID of hidden edges"""
    @property
    def HiddenEdgesLayer(self) -> None:
        """layer ID for hidden edges"""
    @property
    def HiddenEdgesLineType(self) -> None:
        """stroke ID for hidden edges"""
    @property
    def HiddenEdgesPen(self) -> None:
        """pen ID for hidden edges"""
    @property
    def IsHiddenEdgesColorFromLayer(self) -> None:
        """Whether to get the color ID of the hidden edges from the layer definition"""
    @property
    def IsHiddenEdgesColorUsed(self) -> None:
        """Whether to use the color specified in HiddenEdgesColor for drawing the hidden edges (True) or the color of the model elements (False)"""
    @property
    def IsHiddenEdgesLayerUsed(self) -> None:
        """Whether to use the layer specified in HiddenEdgesLayer for drawing the hidden edges (True) or the layer of the model elements (False)"""
    @property
    def IsHiddenEdgesLineTypeFromLayer(self) -> None:
        """Whether to get the stroke ID of the hidden edges from the layer definition"""
    @property
    def IsHiddenEdgesLineTypeUsed(self) -> None:
        """Whether to use the stroke specified in HiddenEdgesLineType for drawing the hidden edges (True) or the stroke of the model elements (False)"""
    @property
    def IsHiddenEdgesOn(self) -> None:
        """Whether to draw hidden edges"""
    @property
    def IsHiddenEdgesPenFromLayer(self) -> None:
        """Whether to get the pen ID of the hidden edges from the layer definition"""
    @property
    def IsHiddenEdgesPenUsed(self) -> None:
        """Whether to use the pen specified in HiddenEdgesPen for drawing the hidden edges (True) or the pen of the model elements (False)"""
    @property
    def IsVisibleEdgesColorFromLayer(self) -> None:
        """Whether to get the color ID of the visible edges from the layer definition"""
    @property
    def IsVisibleEdgesColorUsed(self) -> None:
        """Whether to use the color specified in VisibleEdgesColor for drawing the visible edges (True) or the color of the model elements (False)"""
    @property
    def IsVisibleEdgesLayerUsed(self) -> None:
        """Whether to use the layer specified in VisibleEdgesLayer for drawing the visible edges (True) or the layer of the model elements (False)"""
    @property
    def IsVisibleEdgesLineTypeFromLayer(self) -> None:
        """Whether to get the stroke ID of the visible edges from the layer definition"""
    @property
    def IsVisibleEdgesLineTypeUsed(self) -> None:
        """Whether to use the stroke specified in VisibleEdgesLineType for drawing the visible edges (True) or the stroke of the model elements (False)"""
    @property
    def IsVisibleEdgesOn(self) -> None:
        """Whether to draw visible edges"""
    @property
    def IsVisibleEdgesPenFromLayer(self) -> None:
        """Whether to get the pen ID of the visible edges from the layer definition"""
    @property
    def IsVisibleEdgesPenUsed(self) -> None:
        """Whether to use the pen specified in VisibleEdgesPen for drawing the visible edges (True) or the pen of the model elements (False)"""
    @property
    def VisibleEdgesColor(self) -> None:
        """Color ID for visible edges"""
    @property
    def VisibleEdgesLayer(self) -> None:
        """Layer ID for visible edges"""
    @property
    def VisibleEdgesLineType(self) -> None:
        """Stroke ID for visible edges"""
    @property
    def VisibleEdgesPen(self) -> None:
        """Pen ID for visible edges"""

PYTHON_PART_DOMAIN_TYPE = 21400
PYTHON_PART_SUB_TYPE = 1780

```