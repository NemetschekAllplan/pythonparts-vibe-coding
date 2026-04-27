---
title: "NemAll_Python_AllplanSettings"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_AllplanSettings.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_AllplanSettings

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_AllplanSettings.pyi`  
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

"""Exposed classes and functions from NemAll_Python_AllplanSettings"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_BaseElements
import NemAll_Python_Geometry


__all__ = [
    "AllplanGlobalSettings",
    "AllplanLocalisationService",
    "AllplanPaths",
    "AllplanVersion",
    "AngleUnits",
    "ExecutionEvent",
    "FontProvider",
    "GetAngleUnit",
    "GetLengthUnit",
    "ImperialUnitService",
    "InputAngleSettings",
    "LengthUnits",
    "PictResDoorSwingType",
    "PictResEdgeOffsetType",
    "PictResPalette",
    "PictResParam",
    "PictResPlaneReferences",
    "PictResRevealType",
    "PictResShapeType",
    "PictResSillType",
    "PictResTierOffsetType",
    "PictResWallTierCount",
    "PythonPartsSettings",
    "TextResDoorSwingType",
    "TextResRevealType",
    "TextResShapeType",
    "TextResSillType",
    "TextResTierOffsetType",
    "UnitService",
    "UpdateIdenticalPythonPartsState",
    "UserService",
    "eAngleGradientUnit"
]


class AllplanGlobalSettings():
    """Utility for reading the current global Allplan settings
    """
    @staticmethod
    def GetCurrentColorId() -> int:
        """Get the current used color ID in Allplan

        Returns:
            Current color ID
        """
    @staticmethod
    def GetCurrentCommonProperties() -> NemAll_Python_BaseElements.CommonProperties:
        """Get the current common properties

        Returns:
            Current common properties
        """
    @staticmethod
    def GetCurrentFaceStyleId() -> int:
        """Get the current used face style ID in Allplan

        Returns:
            Current face style ID
        """
    @staticmethod
    def GetCurrentFontId() -> int:
        """Get the current used font ID in Allplan

        Returns:
            Current font ID
        """
    @staticmethod
    def GetCurrentHatchId() -> int:
        """Get the current used hatch ID in Allplan

        Returns:
            Current hatch ID
        """
    @staticmethod
    def GetCurrentLayerId() -> int:
        """Get the current used layer ID in Allplan

        Returns:
            Current layer ID
        """
    @staticmethod
    def GetCurrentPatternId() -> int:
        """Get the current used pattern ID in Allplan

        Returns:
            Current pattern ID
        """
    @staticmethod
    def GetCurrentPenId() -> int:
        """Get the current used pen ID in Allplan

        Returns:
            Current pen ID
        """
    @staticmethod
    def GetCurrentStrokeId() -> int:
        """Get the current used stroke ID in Allplan

        Returns:
            Current stroke ID
        """
    @staticmethod
    def GetOffsetPoint() -> NemAll_Python_Geometry.Point3D:
        """Get the project offset of the currently active project

        Returns:
            Project offset as point
        """

class AllplanLocalisationService():
    """Utility for reading the current localization settings in Allplan

    Returns:
        Something
    """
    @staticmethod
    def AllplanLanguage() -> str:
        """Get the installed Allplan language

        Returns:
            Currently used language as a three letter description
        
                -    bul - Bulgarian
                -    deu - German
                -    eng - English
                -    fin - Finnish
                -    fra - French
                -    grc - Greek
                -    hol - Dutch
                -    hrv - Croatian
                -    ita - Italian
                -    pol - Polish
                -    rum - Romanian
                -    rus - Russian
                -    slk - Slovak
                -    spa - Spanish
                -    svn - Slovenian
                -    tch - Czech
                -    trk - Turkish
                -    ung - Hungarian
                -    dan - Danish
                -    ser - Serbian
                -    mak - Macedonian
                -    prt - Portuguese
                -    ltu - Lithuanian
                -    lva - Latvian
                -    est - Estonian
                -    ukr - Ukrainian
                -    swe - Swedish
                -    nor - Norwegian
                -    chn - Chinese
                -    kor - Korean
                -    jpn - Japanese
                -    usa - USA - English
                -    vie - Vietnamese
        """
    @staticmethod
    def GetTextResource(textID: int) -> str:
        """Get a text resource

        Args:
            textID: Text ID

        Returns:
             Text from the text ID
        """
    @staticmethod
    def Language() -> str:
        """Get the current Allplan language

        Returns:
            Currently used language as a two letter description
        
                -    bg - Bulgarian
                -    de - German
                -    en - English
                -    fi - Finnish
                -    fr - French
                -    el - Greek
                -    nl - Dutch
                -    hr - Croatian
                -    it - Italian
                -    pl - Polish
                -    ro - Romanian
                -    ru - Russian
                -    sk - Slovak
                -    es - Spanish
                -    sl - Slovenian
                -    cs - Czech
                -    tr - Turkish
                -    hu - Hungarian
                -    da - Danish
                -    sr - Serbian
                -    mk - Macedonian
                -    pt - Portuguese
                -    lt - Lithuanian
                -    lv - Latvian
                -    et - Estonian
                -    uk - Ukrainian
                -    sv - Swedish
                -    no - Norwegian
                -    zh - Chinese
                -    ko - Korean
                -    ja - Japanese
                -    vi - Vietnamese
        """

class AllplanPaths():
    """Class for getting Allplan paths
    """
    @staticmethod
    def GetCurPrjDesignPath() -> str:
        """Get the current project design path

        Returns:
             Current project design path
        """
    @staticmethod
    def GetCurPrjPath() -> str:
        """Get the current project path

        Returns:
             Current project path
        """
    @staticmethod
    def GetEtcPath() -> str:
        """Get the Etc path

        Returns:
             Etc path
        """
    @staticmethod
    def GetPathOfApplication() -> str:
        """Get the path of the application

        Returns:
             Path of the application
        """
    @staticmethod
    def GetPrgPath() -> str:
        """Get the program path

        Returns:
             Program path
        """
    @staticmethod
    def GetPythonPartsEtcPath() -> str:
        """Get the PythonParts Etc path

        Returns:
             Etc path
        """
    @staticmethod
    def GetStdDesignPath() -> str:
        """Get the Std design path

        Returns:
             Std design path
        """
    @staticmethod
    def GetStdPath() -> str:
        """Get the Std path

        Returns:
             Std path
        """
    @staticmethod
    def GetTmpPath() -> str:
        """Get the Tmp path

        Returns:
             Tmp path
        """
    @staticmethod
    def GetUsrPath() -> str:
        """Get the Usr path

        Returns:
             Usr path
        """

class AllplanVersion():
    """Class for extraction of Allplan version information
    """
    @staticmethod
    def MainReleaseName() -> str:
        """Get the Allplan main release name
        Returns:
             Allplan main release name ('2016', '2017', ...)
        """
    @staticmethod
    def SubReleaseName() -> str:
        """Get the Allplan sub release name
        Returns:
             Allplan sub release name ('2016.0', '2016.1', ...)
        """
    @staticmethod
    def Version() -> str:
        """Get the Allplan version as string

        Returns:
            Full Allplan version, e.g. 2025.0
        """
    @staticmethod
    def WindowsReleaseName() -> str:
        """Get the Allplan window release name
        Returns:
            'P' for project version or empty string for the normal version
        """

class AngleUnits(enum.Enum):
    """Angle units
    """
    eDeg = 1
    eGon = 2
    eRad = 0

    names = {eRad: eRad,
             eDeg: eDeg,
             eGon: eGon}

    values = {0: eRad,
              1: eDeg,
              2: eGon}

    def __getitem__(self, key: (str | int | float)) -> AngleUnits:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ExecutionEvent(enum.Enum):
    """Implementation of the execution event state

    eCreation       : creation
    eProperties     : properties modification
    ePropertyPalette: properties modification by the property palette
    eHandles        : create and show the handles
    eImport         : import of a PythonPart
    ePlaneChanges   : plane changes
    eConnection     : connection event
    eAttribute      : attribute event
    eCopy           : copy event
    eDelete         : delete event
    eMove           : move event
    eVisible        : visible event
    eAutoUpdate     : automatic update
    """
    eAttribute = 7
    eAutoUpdate = 12
    eConnection = 6
    eCopy = 8
    eCreation = 0
    eDelete = 9
    eHandles = 3
    eImport = 4
    eMove = 10
    ePlaneChanges = 5
    eProperties = 1
    ePropertyPalette = 2
    eVisible = 11

    names = {eCreation: eCreation,
             eProperties: eProperties,
             ePropertyPalette: ePropertyPalette,
             eHandles: eHandles,
             eImport: eImport,
             ePlaneChanges: ePlaneChanges,
             eConnection: eConnection,
             eAttribute: eAttribute,
             eCopy: eCopy,
             eDelete: eDelete,
             eMove: eMove,
             eVisible: eVisible,
             eAutoUpdate: eAutoUpdate}

    values = {0: eCreation,
              1: eProperties,
              2: ePropertyPalette,
              3: eHandles,
              4: eImport,
              5: ePlaneChanges,
              6: eConnection,
              7: eAttribute,
              8: eCopy,
              9: eDelete,
              10: eMove,
              11: eVisible,
              12: eAutoUpdate}

    def __getitem__(self, key: (str | int | float)) -> ExecutionEvent:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class FontProvider():
    """Provides the methods to obtain the list of the fonts.

    CFontProvider is a singleton so that there is always only one instance of this class.
    This instance can be get with the Instance() method.


    Examples:
        >>> font_provider = FontProvider.Instance()
        >>> type(font_provider)
        <class 'NemAll_Python_AllplanSettings.FontProvider'>
    """
    @staticmethod
    def FontMMToPoints(mmValue: float) -> float:
        """Converts mm to points

        Args:
            mmValue: Value to convert in millimeters 

        Returns:
            Value in points
        """
    @staticmethod
    def FontMMToTwips(mmValue: float) -> float:
        """Font size conversions.

        It is a font special factor (0.714) being applied in order to associate
        the mm unit with the real glyph size (like for vector fonts) without sub and superscripts space.
        So these function do not provide common standard point/twips/millimeter conversions!!!
        Converts mm to twips

        Args:
            mmValue: Value to convert in millimeters 

        Returns:
            Value in twips
        """
    @staticmethod
    def FontPointsToMM(twipsValue: float) -> float:
        """Converts points to mm

        Args:
            twipsValue: Value in points 

        Returns:
            Value in mm
        """
    @staticmethod
    def FontTwipsToMM(twipsValue: float) -> float:
        """Converts twips to mm

        Args:
            twipsValue
        """
    @typing.overload
    def GetCharsetList(self, nFontID: int) -> tuple[bool, list[int]]:
        """Returns the list of available charsets for the given font

        Args:
            nFontID: Font ID 

        Returns:
            True if at least one Charset for the given font ID exists
            Charset list
        """
    @typing.overload
    def GetCharsetList(self, fontName: str) -> tuple[bool, list[int]]:
        """Returns the list of available charsets for the given font

        Args:
            fontName: Font name 

        Returns:
            True if at least one Charset for the given font name exists
            Charset list
        """
    def GetCharsetList(self) -> tuple[bool, list[int]]:
        """ Overloaded function. See individual overloads.
        """
    def GetFirstValidPredefinedFontID(self) -> int:
        """Returns ID of the first existing predefined TTF font

        Returns:
            font ID
        """
    def GetFontID(self, fontName: str, bCheckExistence: int = 1) -> int:
        """Get font ID for the given font name.

        Returned value  | Meaning
        ----------------|---------------------------
        0               | Dialog Font ID
        1-20            | Hardcoded Allplan's fonts
        21-63           | Hardcoded system's fonts


        Args:
            fontName:        Name of the font 
            bCheckExistence: When set to True, the font with the particular ID has to be installed. If it's not the case, the function returns an empty string. When set to False, the function returns the name of the font regardless of whether it is installed or not. 

        Returns:
            font ID
        """
    def GetFontName(self, fontID: int, bCheckExistence: int = 1) -> str:
        """Returns the name of the font

        Returns FontName corresponding to fontID
        If fontID is invalid then the empty string is returned

        Args:
            fontID:          ID of the font 
            bCheckExistence: When set to True, the font with the particular ID has to be installed. If it's not the case, the function returns an empty string. When set to False, the function returns the name of the font regardless of whether it is installed or not. 

        Returns:
            Font name. If fontID is invalid then the empty string is returned.
        """
    def GetNemFontIDs(self) -> tuple[bool, list[int]]:
        """Returns the list of the IDs of all Allplan's fonts

        Returns:
            True when at least one font is installed
            List with font IDs
        """
    def GetNemFonts(self) -> tuple[bool, list[str]]:
        """Returns the list of the names of all Allplan's fonts

        Returns:
            True when at least one font is installed
            List with the font names
        """
    def GetPredefinedFontIDs(self) -> tuple[bool, list[int]]:
        """Returns the list of then IDs of all installed and predefined TTF fonts

        Returns:
            True when at least one font is installed
            List with the font IDs
        """
    def GetPredefinedFonts(self) -> tuple[bool, list[str]]:
        """Returns the list of then names of all installed and predefined TTF fonts

        Returns:
            TRUE when at least one font is installed
            List with the font names
        """
    def GetSystemFontIDs(self) -> tuple[bool, list[int]]:
        """Returns the list of the IDs of all installed TTF fonts

        Returns:
            TRUE when at least one font is installed
            List with the font IDs
        """
    def GetSystemFonts(self) -> tuple[bool, list[str]]:
        """Returns the list of the names of all installed TTF fonts

        Returns:
            True when at least one font is installed
            List with the font names
        """
    def GetTTFFontSubtype(self, fontName: str) -> int:
        """Returns type of checked TTF font

        Args:
            fontName: name of the TTF font

        Returns:
            type of the TTF font
        """
    @staticmethod
    def Instance() -> FontProvider:
        """Get the instance of the font provider

        Returns:
            Instance of the font provider
        """
    def NormalizeFontName(self, fontName: str, CharSet: int = 1) -> str:
        """Removes the script suffix from the font name

        Args:
            fontName: font name 
            CharSet:  Charset 

        Returns:
            Font name without suffix.
        """
    def Refresh(self):
        """Reinitialize the fonts
        It'd be called when some system's font was changed ( added/removed )
        """

class ImperialUnitService():
    """Utility with methods for conversion between imperial and metric units
    """
    @staticmethod
    def ConvertToMM(imperialValue: str) -> tuple:
        """Convert an imperial length unit to mm

        Args:
            imperialValue: Imperial value as string 

        Returns:
            True, when input string was **not recognized** as imperial value
            Length in mm

        Examples:
            >>> ImperialUnitService.ConvertToMM("4\"")
            (False, 101.6)

            >>> ImperialUnitService.ConvertToMM("0\"")
            (False, 0.0)
            >>> ImperialUnitService.ConvertToMM("4 in")
            (True, 0.0)
        """
    @staticmethod
    def ConvertTokg(imperialValue: str) -> tuple:
        """Convert an imperial weight unit to kg

        Args:
            imperialValue: Imperial value as string 

        Returns:
            True when input string was **not recognized** as imperial value
            Weight in kg

        Examples:
            >>> ImperialUnitService.ConvertTokg("4 lb")
            (False, 1.814368)
            >>> ImperialUnitService.ConvertTokg("0 lb")
            (False, 0.0)
            >>> ImperialUnitService.ConvertTokg("4 oz")
            (True, 0.0)
        """
    @staticmethod
    def IsImperialUnit() -> bool:
        """Check whether the current input unit is imperial unit

        Returns:
               Imperial unit input: True/False
        """

class InputAngleSettings():
    """Utility containing functions to control the Allplan settings related to the input angle
    """
    @staticmethod
    def GetAngleInputUnit() -> eAngleGradientUnit:
        """Gets the current setting for **unit of angle**

        Returns:
            Unit for angle
        """
    @staticmethod
    def GetGradientInputUnit() -> eAngleGradientUnit:
        """Gets the current setting for **Inclination as**. If it's set to _Angle_, the result will be the
        current _Unit of angle_ setting

        Returns:
            Units for the inclination
        """
    @staticmethod
    def GetProjectAngle(noCache: bool = False) -> float:
        """Get the project angle

        Args:
            noCache: Use no cache: true/false

        Returns:
            Project angle
        """
    @staticmethod
    def GetSystemAngle() -> float:
        """Get the system angle (rotation angle of the cursor)

        Returns:
            System angle in radian
        """
    @staticmethod
    def SetProjectAngle(angle: float):
        """Set the project angle

        Args:
            angle: Project angle
        """
    @staticmethod
    def SetSystemAngle(angle: float):
        """Set the system angle

        Args:
            angle: New system angle
        """

class LengthUnits(enum.Enum):
    """Length units
    """
    eCentimeters = 1
    eDecimeters = 2
    eFeets = 8
    eFeetsAndInchesDecimal = 9
    eFeetsAndInchesExact = 11
    eFeetsAndInchesFractional = 10
    eInchesDecimal = 5
    eInchesExact = 7
    eInchesFractional = 6
    eKilometers = 4
    eMeters = 3
    eMillimeters = 0

    names = {eMillimeters: eMillimeters,
             eCentimeters: eCentimeters,
             eDecimeters: eDecimeters,
             eMeters: eMeters,
             eKilometers: eKilometers,
             eInchesDecimal: eInchesDecimal,
             eInchesFractional: eInchesFractional,
             eInchesExact: eInchesExact,
             eFeets: eFeets,
             eFeetsAndInchesDecimal: eFeetsAndInchesDecimal,
             eFeetsAndInchesFractional: eFeetsAndInchesFractional,
             eFeetsAndInchesExact: eFeetsAndInchesExact}

    values = {0: eMillimeters,
              1: eCentimeters,
              2: eDecimeters,
              3: eMeters,
              4: eKilometers,
              5: eInchesDecimal,
              6: eInchesFractional,
              7: eInchesExact,
              8: eFeets,
              9: eFeetsAndInchesDecimal,
              10: eFeetsAndInchesFractional,
              11: eFeetsAndInchesExact}

    def __getitem__(self, key: (str | int | float)) -> LengthUnits:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResDoorSwingType(enum.Enum):
    """Picture resources for the door swing type
    """
    eBiFold = -1
    eDoubleOppositeSwingCircular = 19751
    eDoubleOppositeSwingLinear = 19753
    eDoubleSwingCircular = 19747
    eDoubleSwingLinear = 19749
    eFolding = 19775
    eLifting = 19777
    eLiftingSingleSwingCircular = 19763
    eLiftingSingleSwingLinear = 19765
    eLiftingSliding = 19771
    eNone = 0
    eOneSidedDoubleRevolving = 19787
    eOneSidedRevolving = 19783
    eOneSidedSwingOptional = 19791
    ePendulumDoubleSwingCircular = 19759
    ePendulumDoubleSwingLinear = 19761
    ePendulumSingleSwingCircular = 19755
    ePendulumSingleSwingLinear = 19757
    eRevolving = 19773
    eSingleSwingCircular = 19743
    eSingleSwingLinear = 19745
    eSliding = -1
    eSlidingDoubleSwing = 19769
    eSlidingSingleSwing = 19767
    eSwing = 19781
    eTwoSidedDoubleRevolving = 19789
    eTwoSidedFolding = 19779
    eTwoSidedRevolving = 19785
    eTwoSidedSwingOptional = 19793

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
              19743: eSingleSwingCircular,
              19745: eSingleSwingLinear,
              19747: eDoubleSwingCircular,
              19749: eDoubleSwingLinear,
              19751: eDoubleOppositeSwingCircular,
              19753: eDoubleOppositeSwingLinear,
              19755: ePendulumSingleSwingCircular,
              19757: ePendulumSingleSwingLinear,
              19759: ePendulumDoubleSwingCircular,
              19761: ePendulumDoubleSwingLinear,
              19763: eLiftingSingleSwingCircular,
              19765: eLiftingSingleSwingLinear,
              19767: eSlidingSingleSwing,
              19769: eSlidingDoubleSwing,
              -1: eBiFold,
              19771: eLiftingSliding,
              19773: eRevolving,
              19775: eFolding,
              19781: eSwing,
              19783: eOneSidedRevolving,
              19785: eTwoSidedRevolving,
              19787: eOneSidedDoubleRevolving,
              19789: eTwoSidedDoubleRevolving,
              19791: eOneSidedSwingOptional,
              19793: eTwoSidedSwingOptional,
              19777: eLifting,
              19779: eTwoSidedFolding}

    def __getitem__(self, key: (str | int | float)) -> PictResDoorSwingType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResEdgeOffsetType(enum.Enum):
    """Picture resources for edge offset types
    """
    eMajorValueAtEnd = 12151
    eMajorValueAtStart = 12147
    eStartEqualEnd = 12149
    eZeroAtEnd = 12153
    eZeroAtStart = 12145

    names = {eZeroAtStart: eZeroAtStart,
             eMajorValueAtStart: eMajorValueAtStart,
             eStartEqualEnd: eStartEqualEnd,
             eMajorValueAtEnd: eMajorValueAtEnd,
             eZeroAtEnd: eZeroAtEnd}

    values = {12145: eZeroAtStart,
              12147: eMajorValueAtStart,
              12149: eStartEqualEnd,
              12151: eMajorValueAtEnd,
              12153: eZeroAtEnd}

    def __getitem__(self, key: (str | int | float)) -> PictResEdgeOffsetType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResPalette(enum.Enum):
    """Picture resources for the palette
    """
    eCenterOfGravity = 19407
    eCenterOfGravitySelected = 19405
    eClear = 14563
    eHotinfo = 16205
    ePropertyTakeOver = 10641
    eRollLeft = 8543
    eRollRight = 8542

    names = {eRollRight: eRollRight,
             eRollLeft: eRollLeft,
             eHotinfo: eHotinfo,
             eCenterOfGravity: eCenterOfGravity,
             eCenterOfGravitySelected: eCenterOfGravitySelected,
             eClear: eClear,
             ePropertyTakeOver: ePropertyTakeOver}

    values = {8542: eRollRight,
              8543: eRollLeft,
              16205: eHotinfo,
              19407: eCenterOfGravity,
              19405: eCenterOfGravitySelected,
              14563: eClear,
              10641: ePropertyTakeOver}

    def __getitem__(self, key: (str | int | float)) -> PictResPalette:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResParam(enum.Enum):
    """Picture resources for the parameter icons
    """
    eParam01 = 19093
    eParam010 = 19111
    eParam011 = 19113
    eParam012 = 19115
    eParam013 = 19117
    eParam014 = 19119
    eParam015 = 19121
    eParam016 = 19123
    eParam017 = 19125
    eParam018 = 19127
    eParam019 = 19129
    eParam02 = 19095
    eParam020 = 19131
    eParam03 = 19097
    eParam04 = 19099
    eParam05 = 19101
    eParam06 = 19103
    eParam07 = 19105
    eParam08 = 19107
    eParam09 = 19109

    names = {eParam01: eParam01,
             eParam02: eParam02,
             eParam03: eParam03,
             eParam04: eParam04,
             eParam05: eParam05,
             eParam06: eParam06,
             eParam07: eParam07,
             eParam08: eParam08,
             eParam09: eParam09,
             eParam010: eParam010,
             eParam011: eParam011,
             eParam012: eParam012,
             eParam013: eParam013,
             eParam014: eParam014,
             eParam015: eParam015,
             eParam016: eParam016,
             eParam017: eParam017,
             eParam018: eParam018,
             eParam019: eParam019,
             eParam020: eParam020}

    values = {19093: eParam01,
              19095: eParam02,
              19097: eParam03,
              19099: eParam04,
              19101: eParam05,
              19103: eParam06,
              19105: eParam07,
              19107: eParam08,
              19109: eParam09,
              19111: eParam010,
              19113: eParam011,
              19115: eParam012,
              19117: eParam013,
              19119: eParam014,
              19121: eParam015,
              19123: eParam016,
              19125: eParam017,
              19127: eParam018,
              19129: eParam019,
              19131: eParam020}

    def __getitem__(self, key: (str | int | float)) -> PictResParam:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResPlaneReferences(enum.Enum):
    """Picture resources for the plan references
    """
    eAbsElevationBottom = 8530
    eAbsElevationTop = 8531
    eBottomFixed = 8528
    eBottomPlane = 8534
    eBottomPlaneFromTop = 8527
    eComponentsBottomPlane = 8525
    eComponentsTopPlane = 8526
    eTopFixed = 8528
    eTopPlane = 8533
    eTopPlaneFromBottom = 8523

    names = {eAbsElevationBottom: eAbsElevationBottom,
             eAbsElevationTop: eAbsElevationTop,
             eBottomPlaneFromTop: eBottomPlaneFromTop,
             eBottomPlane: eBottomPlane,
             eTopPlaneFromBottom: eTopPlaneFromBottom,
             eTopPlane: eTopPlane,
             eComponentsBottomPlane: eComponentsBottomPlane,
             eComponentsTopPlane: eComponentsTopPlane,
             eTopFixed: eTopFixed,
             eBottomFixed: eBottomFixed}

    values = {8530: eAbsElevationBottom,
              8531: eAbsElevationTop,
              8527: eBottomPlaneFromTop,
              8534: eBottomPlane,
              8523: eTopPlaneFromBottom,
              8533: eTopPlane,
              8525: eComponentsBottomPlane,
              8526: eComponentsTopPlane,
              8528: eBottomFixed}

    def __getitem__(self, key: (str | int | float)) -> PictResPlaneReferences:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResRevealType(enum.Enum):
    """Picture resources for reveal types
    """
    eEmbedded = 19709
    eExterior = 19713
    eInterior = 19711
    eNone = 14563

    names = {eNone: eNone,
             eEmbedded: eEmbedded,
             eInterior: eInterior,
             eExterior: eExterior}

    values = {14563: eNone,
              19709: eEmbedded,
              19711: eInterior,
              19713: eExterior}

    def __getitem__(self, key: (str | int | float)) -> PictResRevealType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResShapeType(enum.Enum):
    """Picture resources for shape types
    """
    eArbitrary = 14601
    eChamfer = 17485
    eCircle = 14587
    eConical = 16193
    eDiamond = 14585
    ePolygon = 14599
    eRectangle = 14583
    eRegularPolygonCircumscribed = 14589
    eRegularPolygonInscribed = 14591
    eRiseBottomTop = 14597
    eSemiCircle = 14595
    eSemiDiamond = 14593
    eStep = 17489

    names = {eRectangle: eRectangle,
             eDiamond: eDiamond,
             eCircle: eCircle,
             eRegularPolygonCircumscribed: eRegularPolygonCircumscribed,
             eRegularPolygonInscribed: eRegularPolygonInscribed,
             eSemiDiamond: eSemiDiamond,
             eSemiCircle: eSemiCircle,
             eRiseBottomTop: eRiseBottomTop,
             eArbitrary: eArbitrary,
             ePolygon: ePolygon,
             eStep: eStep,
             eChamfer: eChamfer,
             eConical: eConical}

    values = {14583: eRectangle,
              14585: eDiamond,
              14587: eCircle,
              14589: eRegularPolygonCircumscribed,
              14591: eRegularPolygonInscribed,
              14593: eSemiDiamond,
              14595: eSemiCircle,
              14597: eRiseBottomTop,
              14601: eArbitrary,
              14599: ePolygon,
              17489: eStep,
              17485: eChamfer,
              16193: eConical}

    def __getitem__(self, key: (str | int | float)) -> PictResShapeType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResSillType(enum.Enum):
    """Picture resources for sill types
    """
    eBothsides = 19707
    eInner = 19703
    eNone = 19701
    eOuter = 19705

    names = {eNone: eNone,
             eOuter: eOuter,
             eInner: eInner,
             eBothsides: eBothsides}

    values = {19701: eNone,
              19705: eOuter,
              19703: eInner,
              19707: eBothsides}

    def __getitem__(self, key: (str | int | float)) -> PictResSillType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResTierOffsetType(enum.Enum):
    """Picture resources for tier offset types
    """
    eAdvanced = 16507
    eInnerSide = 16505
    eNone = 16501
    eOuterSide = 16503
    eWithInnerFacing = 16511
    eWithOuterFacing = 16509

    names = {eNone: eNone,
             eOuterSide: eOuterSide,
             eInnerSide: eInnerSide,
             eAdvanced: eAdvanced,
             eWithOuterFacing: eWithOuterFacing,
             eWithInnerFacing: eWithInnerFacing}

    values = {16501: eNone,
              16503: eOuterSide,
              16505: eInnerSide,
              16507: eAdvanced,
              16509: eWithOuterFacing,
              16511: eWithInnerFacing}

    def __getitem__(self, key: (str | int | float)) -> PictResTierOffsetType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PictResWallTierCount(enum.Enum):
    """Picture resources for edge offset types
    """
    eFiveTiers = 14581
    eFourTiers = 14579
    eOneTier = 14573
    eThreeTiers = 14577
    eTwoTiers = 14575

    names = {eOneTier: eOneTier,
             eTwoTiers: eTwoTiers,
             eThreeTiers: eThreeTiers,
             eFourTiers: eFourTiers,
             eFiveTiers: eFiveTiers}

    values = {14573: eOneTier,
              14575: eTwoTiers,
              14577: eThreeTiers,
              14579: eFourTiers,
              14581: eFiveTiers}

    def __getitem__(self, key: (str | int | float)) -> PictResWallTierCount:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PythonPartsSettings():
    """Implementation of the PythonParts settings
    """
    @staticmethod
    def GetInstance() -> PythonPartsSettings:
        """Get the instance

        Returns:
            Instance of the singleton
        """
    def GetLengthFactor(self) -> float:
        """Get the length factor

        Returns:
            Length factor (value to mm)
        """
    def IsSingleElementModification(self) -> bool:
        """Get the single element modification state

        Returns:
            Single element modification state
        """
    def SetLengthUnit(self, lengthUnit: int):
        """Set the length unit

        Args:
            lengthUnit: Length unit: 3 = m
        """
    def SetShowFullPreview(self, showFullPreview: bool):
        """Show the full preview

        Args:
            showFullPreview: Show full preview: true/false
        """
    @property
    def ShowFullPreview(self) -> bool:
        """Get the full preview state

        Show the full preview
        """
    @ShowFullPreview.setter
    def ShowFullPreview(self, showFullPreview: bool) -> None:
        """Show the full preview

        Args:
            showFullPreview: Show full preview: true/false
        """
    @property
    def UpdateIdenticalPythonParts(self) -> UpdateIdenticalPythonPartsState:
        """Get the update identical PythonParts state
        """
    @UpdateIdenticalPythonParts.setter
    def UpdateIdenticalPythonParts(self, updateIdenticalPythonParts: UpdateIdenticalPythonPartsState) -> None:
        """Set the update identical PythonParts state

        Args:
            updateIdenticalPythonParts: Update identical PythonParts state
        """

class TextResDoorSwingType(enum.Enum):
    """Text resources for the door swing type
    """
    eBiFold = -1
    eDoubleOppositeSwingCircular = 36404
    eDoubleOppositeSwingLinear = 36405
    eDoubleSwingCircular = 36402
    eDoubleSwingLinear = 36403
    eFolding = 36417
    eLifting = 36426
    eLiftingSingleSwingCircular = 36410
    eLiftingSingleSwingLinear = 36411
    eLiftingSliding = 36415
    eNone = 36399
    eOneSidedDoubleRevolving = 36422
    eOneSidedRevolving = 36420
    eOneSidedSwingOptional = 36424
    ePendulumDoubleSwingCircular = 36408
    ePendulumDoubleSwingLinear = 36409
    ePendulumSingleSwingCircular = 36406
    ePendulumSingleSwingLinear = 36407
    eRevolving = 36416
    eSingleSwingCircular = 36400
    eSingleSwingLinear = 36401
    eSliding = -1
    eSlidingDoubleSwing = 36413
    eSlidingSingleSwing = 36412
    eSwing = 36419
    eTwoSidedDoubleRevolving = 36423
    eTwoSidedFolding = 36427
    eTwoSidedRevolving = 36421
    eTwoSidedSwingOptional = 36425

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

    values = {36399: eNone,
              36400: eSingleSwingCircular,
              36401: eSingleSwingLinear,
              36402: eDoubleSwingCircular,
              36403: eDoubleSwingLinear,
              36404: eDoubleOppositeSwingCircular,
              36405: eDoubleOppositeSwingLinear,
              36406: ePendulumSingleSwingCircular,
              36407: ePendulumSingleSwingLinear,
              36408: ePendulumDoubleSwingCircular,
              36409: ePendulumDoubleSwingLinear,
              36410: eLiftingSingleSwingCircular,
              36411: eLiftingSingleSwingLinear,
              36412: eSlidingSingleSwing,
              36413: eSlidingDoubleSwing,
              -1: eBiFold,
              36415: eLiftingSliding,
              36416: eRevolving,
              36417: eFolding,
              36419: eSwing,
              36420: eOneSidedRevolving,
              36421: eTwoSidedRevolving,
              36422: eOneSidedDoubleRevolving,
              36423: eTwoSidedDoubleRevolving,
              36424: eOneSidedSwingOptional,
              36425: eTwoSidedSwingOptional,
              36426: eLifting,
              36427: eTwoSidedFolding}

    def __getitem__(self, key: (str | int | float)) -> TextResDoorSwingType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextResRevealType(enum.Enum):
    """Texture resources for reveal types
    """
    eEmbedded = 36386
    eExterior = 36388
    eInterior = 36387
    eNone = 36385

    names = {eNone: eNone,
             eEmbedded: eEmbedded,
             eInterior: eInterior,
             eExterior: eExterior}

    values = {36385: eNone,
              36386: eEmbedded,
              36387: eInterior,
              36388: eExterior}

    def __getitem__(self, key: (str | int | float)) -> TextResRevealType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextResShapeType(enum.Enum):
    """Texture resouces for shape types
    """
    eArbitrary = 36391
    eChamfer = 36537
    eCircle = 36390
    eConical = 36538
    eDiamond = 36389
    ePolygon = 36496
    eRectangle = 36367
    eRegularPolygonCircumscribed = 36440
    eRegularPolygonInscribed = 36439
    eRiseBottomTop = 36370
    eSemiCircle = 36369
    eSemiDiamond = 36368
    eStep = 36536

    names = {eRectangle: eRectangle,
             eDiamond: eDiamond,
             eCircle: eCircle,
             eRegularPolygonInscribed: eRegularPolygonInscribed,
             eRegularPolygonCircumscribed: eRegularPolygonCircumscribed,
             eSemiDiamond: eSemiDiamond,
             eSemiCircle: eSemiCircle,
             eRiseBottomTop: eRiseBottomTop,
             eArbitrary: eArbitrary,
             ePolygon: ePolygon,
             eStep: eStep,
             eChamfer: eChamfer,
             eConical: eConical}

    values = {36367: eRectangle,
              36389: eDiamond,
              36390: eCircle,
              36439: eRegularPolygonInscribed,
              36440: eRegularPolygonCircumscribed,
              36368: eSemiDiamond,
              36369: eSemiCircle,
              36370: eRiseBottomTop,
              36391: eArbitrary,
              36496: ePolygon,
              36536: eStep,
              36537: eChamfer,
              36538: eConical}

    def __getitem__(self, key: (str | int | float)) -> TextResShapeType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextResSillType(enum.Enum):
    """Texture resources for sill types
    """
    eBothsides = 36384
    eInner = 36382
    eNone = 36381
    eOuter = 36383

    names = {eNone: eNone,
             eOuter: eOuter,
             eInner: eInner,
             eBothsides: eBothsides}

    values = {36381: eNone,
              36383: eOuter,
              36382: eInner,
              36384: eBothsides}

    def __getitem__(self, key: (str | int | float)) -> TextResSillType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class TextResTierOffsetType(enum.Enum):
    """Text resources for tier offset types
    """
    eAdvanced = 36395
    eInnerSide = 36394
    eNone = 36392
    eOuterSide = 36393
    eWithInnerFacing = 36396
    eWithOuterFacing = 36397

    names = {eNone: eNone,
             eOuterSide: eOuterSide,
             eInnerSide: eInnerSide,
             eAdvanced: eAdvanced,
             eWithOuterFacing: eWithOuterFacing,
             eWithInnerFacing: eWithInnerFacing}

    values = {36392: eNone,
              36393: eOuterSide,
              36394: eInnerSide,
              36395: eAdvanced,
              36397: eWithOuterFacing,
              36396: eWithInnerFacing}

    def __getitem__(self, key: (str | int | float)) -> TextResTierOffsetType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class UnitService():
    """Unit service
    """
    @staticmethod
    def ConvertToMM(lengthString: str) -> tuple:
        """Convert a value string to mm

        Args:
            lengthString:    Length as string

        Returns:
               Length in mm
        """
    @staticmethod
    def ToLengthUnitString(length: float) -> str:
        """Convert a length(mm) to a string by the current length unit

        Args:
            length:    Length in mm

        Returns:
               String with the value in the current length unit
        """

class UpdateIdenticalPythonPartsState(enum.Enum):
    """Implementation of the update identical PythonParts state

    eUndefinded          :
    eDoUpdateIdentical   :
    eDoNotUpdateIdentical:
    """
    eDoNotUpdateIdentical = 2
    eDoUpdateIdentical = 1
    eUndefinded = 0

    names = {eUndefinded: eUndefinded,
             eDoUpdateIdentical: eDoUpdateIdentical,
             eDoNotUpdateIdentical: eDoNotUpdateIdentical}

    values = {0: eUndefinded,
              1: eDoUpdateIdentical,
              2: eDoNotUpdateIdentical}

    def __getitem__(self, key: (str | int | float)) -> UpdateIdenticalPythonPartsState:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class UserService():
    """User service
    """
    @staticmethod
    def IsCurrentUserSysAdmin() -> bool:
        """IsCurrentUserSysAdmin

        Returns:
               If user is Sys admin or no workgroup is active returns True otherwise False
        """

class eAngleGradientUnit(enum.Enum):
    """Enumeration of available angle units for input of rotation and inclination
    """
    ANGLE_DEGREE = 1
    """Degrees"""
    ANGLE_GON = 3
    """Gradians"""
    ANGLE_NOTDEF = 0
    """Undefined"""
    ANGLE_PERCENT = 5
    """Inclination as %"""
    ANGLE_PERCENTAGE = 4
    """Inclination as 1:x"""
    ANGLE_PERMILL = 6
    """Inclination as ‰"""
    ANGLE_RADIAN = 2
    """Radians"""

    names = {ANGLE_NOTDEF: ANGLE_NOTDEF,
             ANGLE_DEGREE: ANGLE_DEGREE,
             ANGLE_RADIAN: ANGLE_RADIAN,
             ANGLE_GON: ANGLE_GON,
             ANGLE_PERCENTAGE: ANGLE_PERCENTAGE,
             ANGLE_PERCENT: ANGLE_PERCENT,
             ANGLE_PERMILL: ANGLE_PERMILL}

    values = {0: ANGLE_NOTDEF,
              1: ANGLE_DEGREE,
              2: ANGLE_RADIAN,
              3: ANGLE_GON,
              4: ANGLE_PERCENTAGE,
              5: ANGLE_PERCENT,
              6: ANGLE_PERMILL}

    def __getitem__(self, key: (str | int | float)) -> eAngleGradientUnit:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


def GetAngleUnit() -> AngleUnits:
    """Get the angle unit

    Returns:
           Angle unit
    """
def GetLengthUnit() -> LengthUnits:
    """Get the length unit

    Returns:
           Length unit
    """

```