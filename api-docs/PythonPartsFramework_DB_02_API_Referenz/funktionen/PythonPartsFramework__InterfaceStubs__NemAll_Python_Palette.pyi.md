---
title: "NemAll_Python_Palette"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_Palette.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_Palette

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_Palette.pyi`  
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

"""Exposed classes and functions from NemAll_Python_Palette"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_ArchElements
import NemAll_Python_IFW_ElementAdapter
import NemAll_Python_Precast
import NemAll_Python_Utility


__all__ = [
    "FixtureProperties",
    "GetPaletteDataColumnWidth",
    "Orientation",
    "PaletteValueType",
    "PythonWpfPalette",
    "PythonWpfPaletteBuilder",
    "RefPointButtonType",
    "RefPointPosition"
]


class FixtureProperties():

    def GetElement(self) -> str:
        """Get the element

        Returns:
             Element
        """
    def GetGroup(self) -> str:
        """Get the group

        Returns:
             Group
        """
    @staticmethod
    def GetLastFixturePath() -> str:
        """Get the last fixture path

        Returns:
             Last fixture path
        """
    def GetPath(self) -> str:
        """Get the path

        Returns:
             Path
        """
    @staticmethod
    def OpenFixtureDialog(fixturePath: str) -> str:
        """Open the symbol library dialog

        Returns:
               result path

        Args:
            fixturePath:Path to .sym file
        """
    def __eq__(self, other: FixtureProperties) -> object:
        """Comparison of fixture properties.

        Args:
            other: Compared fixture properties.

        Returns:
            True when fixture properties are equal, otherwise false.
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, pathShortcut: str, group: str, element: str):
        """Constructor

        Args:
            pathShortcut: Path shortcut (Office/Project/Privat)
            group:        Group name
            element:      Element name
        """
    @typing.overload
    def __init__(self, FixtureProperties: FixtureProperties):
        """Copy Constructor

        Args:
            FixtureProperties
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
    def Element(self) -> None:
        """Property access for the element

        :type: None
        """
    @property
    def Group(self) -> None:
        """Property access for the group

        :type: None
        """
    @property
    def Path(self) -> None:
        """Property access for the path

        :type: None
        """
    @property
    def PathShortcut(self) -> None:
        """Property access for the path shortcut

        :type: None
        """

class Orientation(enum.Enum):
    """Definition of the orientations

    eLeft  :
    eRight :
    eCenter:
    """
    eCenter = 2
    eLeft = 0
    eRight = 1

    names = {eLeft: eLeft,
             eRight: eRight,
             eCenter: eCenter}

    values = {0: eLeft,
              1: eRight,
              2: eCenter}

    def __getitem__(self, key: (str | int | float)) -> Orientation:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PaletteValueType(enum.Enum):
    """Types of the palette values
    """
    ANGLE = 2
    DOUBLE = 6
    INTEGER = 5
    LENGTH = 1
    STRING = 3

    names = {LENGTH: LENGTH,
             STRING: STRING,
             INTEGER: INTEGER,
             DOUBLE: DOUBLE,
             ANGLE: ANGLE}

    values = {1: LENGTH,
              3: STRING,
              5: INTEGER,
              6: DOUBLE,
              2: ANGLE}

    def __getitem__(self, key: (str | int | float)) -> PaletteValueType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PythonWpfPalette():
    """Implementation of the WPF palette for python
    """
    def Close(self) -> str:
        """Close the palette

        Returns:
            Name of the active page
        """
    def EnableControl(self, name: str, iPage: int, bEnabled: bool):
        """Enable/disable a control

        Args:
            name:     Name of the control
            iPage:    Page index
            bEnabled: Enabled: true/false
        """
    def GetPythonWpfPaletteBuilder(self) -> PythonWpfPaletteBuilder:
        """Get the palette builder

        Returns:
            Palette builder
        """
    def Open(self, title: str, partName: str, dataColumnWidth: int, showCloseButton: bool, showFavoriteButtons: bool,
             doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, activePageText: str):
        """Open the palette

        Args:
            title:               Title
            partName:            Name of the PythonPart
            dataColumnWidth:     Width of the data column
            showCloseButton:     Show the close button state
            showFavoriteButtons: Show the favorites button state
            doc:                 Document
            activePageText:      Page text of the active page
        """
    def Reset(self, clearOnlyPages: bool = False):
        """Reset the palette for a full refresh

        Args:
            clearOnlyPages: Reset only pages, keep other dialog data settings
        """
    def UpdateDialogData(self, activePage: int):
        """Refresh palette with current dialog data

        Args:
            activePage: Index of the active page: (-1 = use current)
        """
    def __init__(self):
        """Constructor
        """
    def __repr__(self) -> str:
        """Convert to string
        """

class PythonWpfPaletteBuilder():
    """Implementation of the Python WPF palette builder
    """
    def AddAngleValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                      minValue: float, maxValue: float, intervalValue: float, asSlider: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add a angle value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            minValue:        Minimal value
            maxValue:        Maximal value
            intervalValue:   Interval value for the slider
            asSlider:        Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color of the control as red, green, blue
        """
    def AddAreaFixtureCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                                 height: int, width: int, fontFaceCode: int):
        """Add an area fixture precastcatalog reference - all, only point, line or area

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddAreaValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                     minValue: float, maxValue: float, intervalValue: float, asSlider: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add a area value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            minValue:        Minimal value
            maxValue:        Maximal value
            intervalValue:   Interval value for the slider
            asSlider:        Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color of the control as red, green, blue
        """
    def AddBarDiameter(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                       height: int, width: int, fontFaceCode: int):
        """Add an bar diameter value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddBendingRollerValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                              height: int, width: int, fontFaceCode: int):
        """Add a bending roller value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddBrickTileCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                               height: int, width: int, fontFaceCode: int):
        """Add a brick/tile reference

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddButton(self, description: str, name: str, eventId: int, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int,
                  width: int, fontStyle: int, fontFaceCode: int):
        """Add a button to the palette

        Args:
            description:  Description
            name:         Value name
            eventId:      Value holds the event ID pressing the button
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontStyle:    Font size: 0=small, 1=extra small, 2=large
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddCheckboxValue(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                         height: int, width: int, fontFaceCode: int):
        """Add a checkbox value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddColorValue(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                      height: int, width: int, fontFaceCode: int):
        """Add a color value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    @staticmethod
    def AddComboBoxValue(description: PythonWpfPaletteBuilder, name: str, value: str, listValues: str, ctrlType: str,
                         valueType: PaletteValueType, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList), isEditable: bool):
        """Add a combo box value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            listValues:      List values
            ctrlType:        Control type
            valueType:       Value type
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color
            isEditable:      Is editable state
        """
    def AddConcreteCoverValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                              height: int, width: int, fontFaceCode: int):
        """Add a concrete cover value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddConcreteGrade(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                         height: int, width: int, fontFaceCode: int):
        """Add a concrete grade value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddConcreteGradeCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str,
                                   bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a concreteGrade reference

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddDoubleValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                       minValue: float, maxValue: float, intervalValue: float, asSlider: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add a double value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            minValue:        Minimal value
            maxValue:        Maximal value
            intervalValue:   Interval value for the slider
            asSlider:        Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color of the control as red, green, blue
        """
    def AddFaceStyleValue(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                          height: int, width: int, fontFaceCode: int):
        """Add a face style combobox to the palette

        Args:
            description:  Description
            name:         ID name
            value:        Selected value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddFactoryCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                             height: int, width: int, fontFaceCode: int):
        """Add a factory precastcatalog reference

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddFixtureCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                             height: int, width: int, fontFaceCode: int):
        """Add a fixture precastcatalog reference - all, only point, line or area

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddFixtureValues(self, descriptionPath: str, descriptionGroup: str, descriptionElement: str, name: str, fixture: FixtureProperties,
                         page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add the fixture values

        Args:
            descriptionPath:    Description of the path value
            descriptionGroup:   Description of the group value
            descriptionElement: Description of the element value
            name:               Value name
            fixture:            Properties of the fixture
            page:               Pate
            expanderName:       Expander section name
            rowName:            Name of the row
            bEnabled:           Control is enabled: true/false
            height:             Control height, only used for a row
            width:              Control width, only used for a row
            fontFaceCode:       Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddHatchValue(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                      height: int, width: int, fontFaceCode: int):
        """Add a hatch combobox to the palette

        Args:
            description:  Description
            name:         ID name
            value:        Selected value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddInsulationCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                                height: int, width: int, fontFaceCode: int):
        """Add a insulation reference

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddIntValue(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                    minValue: float, maxValue: float, intervalValue: float, asSlider: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add an integer value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            minValue:        Minimal value
            maxValue:        Maximal value
            intervalValue:   Interval value for the slider
            asSlider:        Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color of the control as red, green, blue
        """
    def AddLayer(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int,
                 width: int, fontFaceCode: int):
        """Add a layer value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddLengthValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                       minValue: float, maxValue: float, intervalValue: float, asSlider: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add a length value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            minValue:        Minimal value
            maxValue:        Maximal value
            intervalValue:   Interval value for the slider
            asSlider:        Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color of the control as red, green, blue
        """
    def AddLineFixtureCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                                 height: int, width: int, fontFaceCode: int):
        """Add a line fixture precastcatalog reference - all, only point, line or area

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddMaterialButton(self, description: str, name: str, value: str, buttonType: int, page: int, expanderName: str, rowName: str,
                          bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a material button to the palette

        Args:
            description:  Description
            name:         Value name
            value:        String of material
            buttonType:   Button type (0: simple material button, 1: mat button + switch off button)
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddMeshGroup(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int,
                     width: int, fontFaceCode: int):
        """Add a mesh group value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddMeshType(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                    meshGroup: int, height: int, width: int, fontFaceCode: int):
        """Add a mesh type value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            meshGroup:    Mesh group
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddMultiMaterialLayoutCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str,
                                         bEnabled: bool, height: int, width: int, fontFaceCode: int) -> int:
        """Add a multimaterial layout catalog reference

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
            ex:of layout
        """
    def AddNormCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                          height: int, width: int, fontFaceCode: int):
        """Add a norm catalog reference

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPage(self, name: str, description: str):
        """Add a page to the palette

        Args:
            name:        ID name
            description: Description text (localized)
        """
    def AddPatternValue(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                        height: int, width: int, fontFaceCode: int):
        """Add a pattern combobox to the palette

        Args:
            description:  Description
            name:         ID name
            value:        Selected value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPenValue(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int,
                    width: int, fontFaceCode: int):
        """Add a pen value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPicture(self, description: str, name: str, pictureName: str, libPath: str, orientation: Orientation, page: int,
                   expanderName: str, rowName: str):
        """Add a picture to the palette

        Args:
            description:  Description used for the tooltip
            name:         ID name
            pictureName:  Name of the picture
            libPath:      Library path
            orientation:  Orientation (0:LEFT, 1:MIDDLE, 2:RIGHT)
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
        """
    def AddPictureButton(self, description: str, name: str, value: str, eventId: int, page: int, expanderName: str, rowName: str,
                         bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a picture button to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            eventId:      Value holds the event ID pressing the button
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPictureButtonList(self, description: str, name: str, value: int, picturePath: str, pictureList: str, valueList: str,
                             textList: str, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a picture button list to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value holds the selected picture button in buttons
            picturePath:  Path of pictures
            pictureList:  Picture list holds the images for the buttons - example: a.png|b.png|c.png
            valueList:    Value list of possible values - example: 0|1|2
            textList:     Text list for the tooltips
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPictureComboBox(self, description: str, name: str, value: int, picturePath: str, pictureList: str, valueList: str, textList: str,
                           page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a picture combobox to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value holds the selected picture button in buttons
            picturePath:  Path of pictures
            pictureList:  Picture list holds the images for the buttons - example: a.png|b.png|c.png
            valueList:    Value list of possible values - example: 0|1|2
            textList:     Text list for the tooltips
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPictureResourceButton(self, description: str, name: str, value: int, eventId: int, page: int, expanderName: str, rowName: str,
                                 bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a picture button to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value holds the resource ID
            eventId:      Value holds the event ID pressing the button
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPictureResourceButtonList(self, description: str, name: str, value: int, pictureList: str, valueList: str, textList: str,
                                     page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a picture resource button list to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value holds the selected picture button in buttons
            pictureList:  Picture list holds the images for the buttons - example: 16433|16441|16449
            valueList:    Value list of possible values - example: 0|1|2
            textList:     Text list for the tooltips
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPictureResourceComboBox(self, description: str, name: str, value: int, pictureList: str, valueList: str, textList: str,
                                   page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a picture resource combobox to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value holds the selected picture button in buttons
            pictureList:  Picture list holds the images for the buttons - example: 16433|16441|16449
            valueList:    Value list of possible values - example: 0|1|2
            textList:     Text list for the tooltips
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPictureResourceToggleButton(self, description: str, name: str, value: int, pictureList: str, valueList: str, textList: str,
                                       page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a picture toggle button to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value holds the selected picture button in buttons
            pictureList:  Picture list holds the images for the buttons - example: a.png|b.png|c.png
            valueList:    Value list of possible values - example: 0|1|2
            textList:     Text list for the tooltips
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPlaneReferencesButton(self, description: str, name: str, planeRefs: NemAll_Python_ArchElements.BasePlaneReferences, page: int,
                                 expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a plane references button to the palette

        Args:
            description:  Description
            name:         Value name
            planeRefs:    Plane references
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPointFixtureCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                                  height: int, width: int, fontFaceCode: int):
        """Add a point fixture precastcatalog reference - all, only point, line or area

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddPrecastElementTypeCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str,
                                        bEnabled: bool, height: int, width: int, fontFaceCode: int) -> str:
        """Add a precastElementType catalog reference

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddRadioButton(self, radioButtonGroupDescription: str, radioButtonGroupName: str, radioButtonDescription: str, value: object,
                       selectedValueInGroup: object, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a radio button to the palette

        Args:
            radioButtonGroupDescription: Radio button group description
            radioButtonGroupName:        Radio button group ID name
            radioButtonDescription:      Radio button description
            value:                       Double value of this radio button
            selectedValueInGroup:        Selected value of radio button group
            page:                        Page index
            expanderName:                Expander section name
            rowName:                     Name of the row
            bEnabled:                    Control is enabled: true/false
            height:                      Control height, only used for a row
            width:                       Control width, only used for a row
            fontFaceCode:                Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddRefPointButton(self, description: str, name: str, refPointPosition: RefPointPosition, refPointType: RefPointButtonType,
                          page: int, expanderName: str, rowName: str, bEnabled: bool, height: int, width: int, fontFaceCode: int):
        """Add a reference point button to the palette

        Args:
            description:      Description
            name:             Value name
            refPointPosition: Reference point ID (1,...,9)
            refPointType:     Reference point type
            page:             Page index
            expanderName:     Expander section name
            rowName:          Name of the row
            bEnabled:         Control is enabled: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            fontFaceCode:     Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddResourcePicture(self, description: str, name: str, pictureResourceID: int, page: int, expanderName: str, rowName: str,
                           height: int, width: int):
        """Add a picture from a resource to the palette

        Args:
            description:       Description used for the tooltip
            name:              ID name
            pictureResourceID: Resource id of the picture
            page:              Page index
            expanderName:      Expander section name
            rowName:           Name of the row
            height:            Control height, only used for a row
            width:             Control width, only used for a row
        """
    def AddSeparator(self, page: int, expanderName: str):
        """Add a separator to the palette

        Args:
            page:         Page index
            expanderName: Expander section name
        """
    def AddSteelGrade(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool,
                      height: int, width: int, fontFaceCode: int):
        """Add a steel grade value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddStringValue(self, description: str, name: str, str: str, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int,
                       width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add a string value to the palette

        Args:
            description:     Description
            name:            Value name
            str:             String
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor
        """
    def AddStroke(self, description: str, name: str, value: int, page: int, expanderName: str, rowName: str, bEnabled: bool, height: int,
                  width: int, fontFaceCode: int):
        """Add a stroke value to the palette

        Args:
            description:  Description
            name:         Value name
            value:        Value
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddSurfaceCatalogRef(self, description: str, name: str, value: str, page: int, expanderName: str, rowName: str, bEnabled: bool,
                             height: int, width: int, fontFaceCode: int):
        """Add a Surface catalog reference

        Args:
            description:  Description
            name:         Value name
            value:        Value string
            page:         Page index
            expanderName: Expander section name
            rowName:      Name of the row
            bEnabled:     Control is enabled: true/false
            height:       Control height, only used for a row
            width:        Control width, only used for a row
            fontFaceCode: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
    def AddText(self, description: str, value: str, orientation: Orientation, page: int, expanderName: str, rowName: str, bEnabled: bool,
                height: int, width: int, fontStyle: int, fontFaceCode: int):
        """Add a text

        Args:
            description:  Description
            value:        Value
            orientation:  Page index
            page:         Expander section name
            expanderName: Name of the row
            rowName:      Control is enabled: true/false
            bEnabled:     Control height, only used for a row
            height:       Control width, only used for a row
            width:        Font size: 0=small, 1=extra small, 2=large
            fontStyle:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            fontFaceCode
        """
    def AddVolumeValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                       minValue: float, maxValue: float, intervalValue: float, asSlider: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add a volume value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            minValue:        Minimal value
            maxValue:        Maximal value
            intervalValue:   Interval value for the slider
            asSlider:        Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color of the control as red, green, blue
        """
    def AddWeightValue(self, description: str, name: str, value: float, page: int, expanderName: str, rowName: str, bEnabled: bool,
                       minValue: float, maxValue: float, intervalValue: float, asSlider: bool, height: int, width: int, fontFaceCode: int, backgroundColor: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Add a weight value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expanderName:    Expander section name
            rowName:         Name of the row
            bEnabled:        Control is enabled: true/false
            minValue:        Minimal value
            maxValue:        Maximal value
            intervalValue:   Interval value for the slider
            asSlider:        Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            fontFaceCode:    Face code: 0=normal, 1=bold, 2=italic, 4=underline
            backgroundColor: Background color of the control as red, green, blue
        """
    def IsConcreteCoverPaletteUpdate(self, cover: float) -> bool:
        """Check for a palette update due to a new concrete cover

        Args:
            cover: Concrete cover

        Returns:
            Palette update: true/false
        """
    def Reset(self):
        """Reset the data
        """
    def __init__(self, element: PythonWpfPaletteBuilder):
        """Copy constructor

        Args:
            element: Element to copy
        """

class RefPointButtonType(enum.Enum):
    """Definition of available positions of the reference point on a reference point button.
    """
    eAllNinePositions = 0
    """All nine positions of the reference point are available."""
    eAllTenPositions = 6
    """All nine positions of the reference point are available, plus tenth option. of an undefined point."""
    eCorners = 2
    """Only four positions in the corners possible."""
    eCornersCenter = 3
    """Five positions possible. Four in the corners plus in the center."""
    eLeftRightCenter = 4
    """Three positions possible. Center-left, center-center and center-right."""
    eNoCorners = 1
    """Five positions possible. In the middle and on the center of each edge."""
    eTopBottomCenter = 5
    """Three positions possible. Top-center, center-center and bottom-center."""

    names = {eAllNinePositions: eAllNinePositions,
             eNoCorners: eNoCorners,
             eCorners: eCorners,
             eCornersCenter: eCornersCenter,
             eLeftRightCenter: eLeftRightCenter,
             eTopBottomCenter: eTopBottomCenter,
             eAllTenPositions: eAllTenPositions}

    values = {0: eAllNinePositions,
              1: eNoCorners,
              2: eCorners,
              3: eCornersCenter,
              4: eLeftRightCenter,
              5: eTopBottomCenter,
              6: eAllTenPositions}

    def __getitem__(self, key: (str | int | float)) -> RefPointButtonType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class RefPointPosition(enum.Enum):
    """Definition of the reference point positions get from the RefPointButton

    eNone        :
    eTopLeft     :
    eTopCenter   :
    eTopRight    :
    eCenterLeft  :
    eCenterCenter:
    eCenterRight :
    eBottomLeft  :
    eBottomCenter:
    eBottomRight :
    """
    eBottomCenter = 8
    eBottomLeft = 7
    eBottomRight = 9
    eCenterCenter = 5
    eCenterLeft = 4
    eCenterRight = 6
    eNone = 0
    eTopCenter = 2
    eTopLeft = 1
    eTopRight = 3

    names = {eNone: eNone,
             eTopLeft: eTopLeft,
             eTopCenter: eTopCenter,
             eTopRight: eTopRight,
             eCenterLeft: eCenterLeft,
             eCenterCenter: eCenterCenter,
             eCenterRight: eCenterRight,
             eBottomLeft: eBottomLeft,
             eBottomCenter: eBottomCenter,
             eBottomRight: eBottomRight}

    values = {0: eNone,
              1: eTopLeft,
              2: eTopCenter,
              3: eTopRight,
              4: eCenterLeft,
              5: eCenterCenter,
              6: eCenterRight,
              7: eBottomLeft,
              8: eBottomCenter,
              9: eBottomRight}

    def __getitem__(self, key: (str | int | float)) -> RefPointPosition:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


def GetPaletteDataColumnWidth() -> int:
    """Get the width of the property palette data column

    Returns:
        Width of the property palette data column
    """

```