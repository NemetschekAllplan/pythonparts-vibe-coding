---
title: "NemAll_Python_BaseElements"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_BaseElements.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_BaseElements

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_BaseElements.pyi`  
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

"""Exposed classes and functions from NemAll_Python_BaseElements"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_BasisElements
import NemAll_Python_Geometry
import NemAll_Python_IFW_ElementAdapter
import NemAll_Python_IFW_Input
import NemAll_Python_Utility


__all__ = [
    "ATTRNR_HASH",
    "ATTRNR_PYTHONPART_CHECK",
    "ATTRNR_PYTHONPART_DISPLAY_NAME",
    "ATTRNR_PYTHONPART_MATRIX",
    "ATTRNR_PYTHONPART_OBJECT",
    "ATTRNR_PYTHONPART_PATH",
    "ATTRNR_PYTHONPART_UUID",
    "ATTRNR_SUB_PYTHONPART_KEY",
    "ATTRNR_UUID",
    "ATTRNR_VOLUME",
    "ActiveBackground",
    "ActiveForeground",
    "AskForLocation",
    "AssociationService",
    "Attribute",
    "AttributeByteVec",
    "AttributeDataManager",
    "AttributeDate",
    "AttributeDouble",
    "AttributeDoubleVec",
    "AttributeEnum",
    "AttributeInteger",
    "AttributeIntegerVec",
    "AttributeService",
    "AttributeSet",
    "AttributeString",
    "AttributeStringVec",
    "Attributes",
    "CadDataFileReader",
    "ClearElementPreview",
    "CloseElementPreview",
    "Color",
    "ColorByLayer",
    "CommonProperties",
    "CopyElements",
    "CopyElementsToDrawingFile",
    "CreateAssociativeViews",
    "CreateBarCoupler",
    "CreateElements",
    "CreateLayer",
    "CreateLibraryElement",
    "CreateSectionsAndViews",
    "CreateSubPath",
    "DTMService",
    "DTMServiceResult",
    "DeleteElements",
    "DoNotRead",
    "DocumentResourceService",
    "DrawElementPreview",
    "DrawingFileLoadState",
    "DrawingFileService",
    "DrawingService",
    "DrawingTypeService",
    "ElementTransform",
    "ElementsAttributeService",
    "ElementsByAttributeService",
    "ElementsLayerService",
    "ElementsPropertyService",
    "ElementsSelectService",
    "ExecutePreviewDraw",
    "ExplodeIFCSmartSymbols",
    "ExplodeSmartSymbols",
    "ExportImportService",
    "FaceSelectService",
    "FaceStyle",
    "GetColorById",
    "GetElement",
    "GetElements",
    "GetIdByColor",
    "GetMinMaxBox",
    "GetViewMatrices",
    "Hatching",
    "IFC_Version",
    "Ifc_2x3",
    "Ifc_4",
    "Ifc_XML_2x3",
    "Ifc_XML_4",
    "InformationPaletteService",
    "InformationPaletteSettingsHelper",
    "Layer",
    "LayerService",
    "LayoutBorderDefinition",
    "LayoutFileService",
    "LayoutMargin",
    "LayoutMasterData",
    "LayoutMasterLegendData",
    "LayoutMasterStampData",
    "LayoutSize",
    "ModifyElements",
    "ModifyElementsWithSaveAndRestoreSelection",
    "ModifyPropertyID",
    "MoveElementsToDrawingFile",
    "OverrideFiles",
    "PassiveBackground",
    "PathDefaultID",
    "PathID",
    "PathOfficeID",
    "PathPrivateID",
    "PathProjectID",
    "Pen",
    "PenByLayer",
    "PlaneService",
    "ProjectAttributeService",
    "ProjectService",
    "PythonPartService",
    "ReadAll",
    "ReadAllAndComputable",
    "ReadWithoutGeometry",
    "RotateElements",
    "ScaleElements",
    "ShowElements",
    "Stroke",
    "StrokeByLayer",
    "ViewSectionPreview",
    "ZoomService",
    "eAttibuteReadState",
    "eDesignPathLocation"
]


class AssociationService():
    """Implementation of the association service
    """
    @staticmethod
    def AssociateElementsWithPythonPart(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, elementUUIDs: list,
                                        pythonPartUUID: NemAll_Python_IFW_ElementAdapter.GUID, connectAsChild: bool = False):
        """Associate the elements with the PythonPart

        Args:
            doc:            Document
            elementUUIDs:   List with the element UUIDs as string
            pythonPartUUID: UUID of the PythonPart
            connectAsChild: Connect the PythonPart as child to the first elemen
        """
    @staticmethod
    def DeletePythonPartAssociation(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                                    pythonPartUUID: NemAll_Python_IFW_ElementAdapter.GUID):
        """Delete the PythonPart association

        Args:
            doc:            Document
            pythonPartUUID: UUID of the PythonPart
        """
    @staticmethod
    def ExecuteUpdate(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Execute the association update

        Args:
            doc: Document
        """
    @staticmethod
    def GetObservedElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                            dependentElementUUID: NemAll_Python_IFW_ElementAdapter.GUID) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Get the observed elements

        Args:
            doc:                  Document
            dependentElementUUID: UUID of the dependent element

        Returns:
            Observed elements
        """
    @staticmethod
    def RemoveElementsFromPythonPartAssociation(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, elementUUIDs: list,
                                                pythonPartUUID: NemAll_Python_IFW_ElementAdapter.GUID):
        """Remove the elements from the PythonPart association

        Args:
            doc:            Document
            elementUUIDs:   List with the element UUIDs as string
            pythonPartUUID: UUID of the PythonPart
        """

class Attribute():
    """Base for all attribute definitions
    """
    def __eq__(self, element: Attribute) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @property
    def Id(self) -> int:
        """Get the attribute Id
        """
    @Id.setter
    def Id(self, id: int) -> None:
        """Set the attribute Id

        Args:
            id: Attribute id
        """
    @property
    def Undefined(self) -> bool:
        """Get the undefined state
        """
    @Undefined.setter
    def Undefined(self, value: bool) -> None:
        """Set the undefined state
        """

class AttributeByteVec(Attribute):
    """ByteVec attribute
    """
    def __eq__(self, element: AttributeByteVec) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: NemAll_Python_Utility.VecByteList):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeByteVec):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeByteVec) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> (list[int] | NemAll_Python_Utility.VecIntList):
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: (list[int] | NemAll_Python_Utility.VecIntList)) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class AttributeDataManager():

    @staticmethod
    def GetAttributeName(attributeID: int) -> str:
        """Get the attribute name from the ID

        Args:
            attributeID: Attribute ID

        Returns:
             Attribute name
        """

class AttributeDate(Attribute):
    """Date attribute
    """
    def __eq__(self, element: AttributeDate) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, day: int, month: int, year: int):
        """Constructor

        Args:
            id:    Attribute id
            day:   Day
            month: Month
            year:  Year
        """
    @typing.overload
    def __init__(self, element: AttributeDate):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeDate) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Day(self) -> int:
        """Get the day value
        """
    @Day.setter
    def Day(self, day: int) -> None:
        """Set the day value

        Args:
            day: Attribute day value
        """
    @property
    def Month(self) -> int:
        """Get the month value
        """
    @Month.setter
    def Month(self, month: int) -> None:
        """Set the month value

        Args:
            month: Attribute month value
        """
    @property
    def Year(self) -> int:
        """Get the year value
        """
    @Year.setter
    def Year(self, year: int) -> None:
        """Set the year value

        Args:
            year: Attribute year value
        """

class AttributeDouble(Attribute):
    """Double attribute
    """
    def __eq__(self, element: AttributeDouble) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: float):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeDouble):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeDouble) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> float:
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: float) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class AttributeDoubleVec(Attribute):
    """DoubleVec attribute
    """
    def __eq__(self, element: AttributeDoubleVec) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: NemAll_Python_Utility.VecDoubleList):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeDoubleVec):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeDoubleVec) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> NemAll_Python_Utility.VecDoubleList:
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: NemAll_Python_Utility.VecDoubleList) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class AttributeEnum(Attribute):
    """Enum attribute
    """
    def __eq__(self, element: AttributeEnum) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: int):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeEnum):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeEnum) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> int:
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: int) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class AttributeInteger(Attribute):
    """Integer attribute
    """
    def __eq__(self, element: AttributeInteger) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: int):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeInteger):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeInteger) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> int:
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: int) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class AttributeIntegerVec(Attribute):
    """IntegerVec attribute
    """
    def __eq__(self, element: AttributeIntegerVec) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: (list[int] | NemAll_Python_Utility.VecIntList)):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeIntegerVec):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeIntegerVec) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> (list[int] | NemAll_Python_Utility.VecIntList):
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: (list[int] | NemAll_Python_Utility.VecIntList)) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class AttributeService():

    """Service for reading existing attributes definitions and creating new user-defined attributes
    """
    class AttributeControlType(enum.Enum):
        """Attribute control types
        """
        Calculate = 66
        CheckBox = 67
        ComboBox = 76
        ComboBoxFilling = 70
        ComboBoxFixed = 88
        ComboBoxHatch = 83
        ComboBoxPattern = 77
        Edit = 69
        Undef = 48

        names = {Undef: Undef,
                 Edit: Edit,
                 ComboBox: ComboBox,
                 ComboBoxFixed: ComboBoxFixed,
                 ComboBoxHatch: ComboBoxHatch,
                 ComboBoxPattern: ComboBoxPattern,
                 ComboBoxFilling: ComboBoxFilling,
                 CheckBox: CheckBox,
                 Calculate: Calculate}

        values = {48: Undef,
                  69: Edit,
                  76: ComboBox,
                  88: ComboBoxFixed,
                  83: ComboBoxHatch,
                  77: ComboBoxPattern,
                  70: ComboBoxFilling,
                  67: CheckBox,
                  66: Calculate}

        def __getitem__(self, key: (str | int | float)) -> AttributeService.AttributeControlType:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class AttributeSelectionDialogType(enum.Enum):
        """Type of the attribute selection dialog

        eAllAttributes    :
        eInsertAttributes :
        eProjectAttributes:
        """
        eAllAttributes = 0
        eInsertAttributes = 1
        eProjectAttributes = 2

        names = {eAllAttributes: eAllAttributes,
                 eInsertAttributes: eInsertAttributes,
                 eProjectAttributes: eProjectAttributes}

        values = {0: eAllAttributes,
                  1: eInsertAttributes,
                  2: eProjectAttributes}

        def __getitem__(self, key: (str | int | float)) -> AttributeService.AttributeSelectionDialogType:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    class AttributeType(enum.Enum):
        """Attribute types
        """
        ByteVec = 66
        Date = 68
        Double = 82
        DoubleVec = 80
        Enum = 69
        Integer = 73
        IntegerVec = 89
        String = 67
        StringVec = 83
        Undef = 48
        WString = 87

        names = {Undef: Undef,
                 String: String,
                 WString: WString,
                 Double: Double,
                 Integer: Integer,
                 Date: Date,
                 DoubleVec: DoubleVec,
                 IntegerVec: IntegerVec,
                 ByteVec: ByteVec,
                 StringVec: StringVec,
                 Enum: Enum}

        values = {48: Undef,
                  67: String,
                  87: WString,
                  82: Double,
                  73: Integer,
                  68: Date,
                  80: DoubleVec,
                  89: IntegerVec,
                  66: ByteVec,
                  83: StringVec,
                  69: Enum}

        def __getitem__(self, key: (str | int | float)) -> AttributeService.AttributeType:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    @staticmethod
    def AddUserAttribute(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeType: AttributeType, attributeName: str,
                         attributeDefaultValue: str, attributeMinValue: float, attributeMaxValue: float, attributeDimension: str, attributeCtrlType: AttributeControlType, attributeListValues: NemAll_Python_Utility.VecStringList) -> int:
        """Add a user attribute

        Args:
            doc:                   Document
            attributeType:         Type
            attributeName:         Name
            attributeDefaultValue: Default value
            attributeMinValue:     Minimal value
            attributeMaxValue:     Maximal value
            attributeDimension:    Dimension
            attributeCtrlType:     Control type
            attributeListValues:   List with the allowed attribute values

        Returns:
            ID of the added user attribute, -1 = not possible to add
        """
    @staticmethod
    def GetAttributeControlType(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeID: int) -> AttributeControlType:
        """Get the control type of the attribute

        Args:
            doc:         Document
            attributeID: Attribute ID

        Returns:
            Control type of the attribute
        """
    @staticmethod
    def GetAttributeID(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeName: str) -> int:
        """Get the attribute ID

        Args:
            doc:           Document
            attributeName: Attribute name

        Returns:
            Attribute ID
        """
    @staticmethod
    def GetAttributeName(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeID: int) -> str:
        """Get the attribute name

        Args:
            doc:         Document
            attributeID: Attribute ID

        Returns:
            Attribute name
        """
    @staticmethod
    def GetAttributeType(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeID: int) -> AttributeType:
        """Get the attribute type

        Args:
            doc:         Document
            attributeID: Attribute ID

        Returns:
            Attribute type
        """
    @staticmethod
    def GetAttributeUnit(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeID: int) -> str:
        """Get the attribute unit

        Args:
            doc:         Document
            attributeID: Attribute ID

        Returns:
            Attribute unit
        """
    @staticmethod
    def GetDefaultValue(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeID: int) -> (int | float | str):
        """Get the default value of an attribute

        Args:
            doc:         Document
            attributeID: Attribute ID

        Returns:
             Default value of the attribute
        """
    @staticmethod
    def GetEnumIDFromValueString(attributeID: int, valueString: str) -> int:
        """Get the enumeration ID from the value string

        Args:
            attributeID: Attribute ID
            valueString: Value string

        Returns:
            Enumeration ID
        """
    @staticmethod
    def GetEnumValueStringFromID(attributeID: int, enumID: int) -> str:
        """Get the enumeration value string from the enumeration ID

        Args:
            attributeID: Attribute ID
            enumID:      Enumeration ID

        Returns:
            Enumeration value string
        """
    @staticmethod
    def GetEnumValues(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeID: int) -> NemAll_Python_Utility.VecStringList:
        """Get the enum attribute values

        Args:
            doc:         Document
            attributeID: Attribute ID

        Returns:
            Default attribute value
        """
    @staticmethod
    def GetGroupAttributeIDs(ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, attributes: list[tuple[int, (int | float | str)]],
                             excludeHidden: bool) -> list[tuple[str, (list[int] | NemAll_Python_Utility.VecIntList)]]:
        """Get the attribute IDs and the name of the attribute groups

        Args:
            ele:           Element for the attributes
            attributes:    Attributes of the element
            excludeHidden: Exclude the hidden attributes

        Returns:
            Group name, group IDs
        """
    @staticmethod
    def GetInputListValues(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, attributeID: int) -> NemAll_Python_Utility.VecStringList:
        """Get the input list values

        Args:
            doc:         Document
            attributeID: Attribute ID

        Returns:
            Attribute input list values
        """
    @staticmethod
    def OpenAttributeSelectionDialog(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                                     dialogType: AttributeSelectionDialogType) -> int:
        """Open the attribute selection dialog

        Args:
            doc:        Document
            dialogType: Dialog type

        Returns:
            Attribute ID
        """
    ByteVec = AttributeType.ByteVec
    Calculate = AttributeControlType.Calculate
    CheckBox = AttributeControlType.CheckBox
    ComboBox = AttributeControlType.ComboBox
    ComboBoxFilling = AttributeControlType.ComboBoxFilling
    ComboBoxFixed = AttributeControlType.ComboBoxFixed
    ComboBoxHatch = AttributeControlType.ComboBoxHatch
    ComboBoxPattern = AttributeControlType.ComboBoxPattern
    Date = AttributeType.Date
    Double = AttributeType.Double
    DoubleVec = AttributeType.DoubleVec
    Edit = AttributeControlType.Edit
    Enum = AttributeType.Enum
    Integer = AttributeType.Integer
    IntegerVec = AttributeType.IntegerVec
    String = AttributeType.String
    StringVec = AttributeType.StringVec
    Undef = AttributeControlType.Undef
    WString = AttributeType.WString

class AttributeSet():
    """Attribute set
    """
    def GetAttributes(self) -> list[(AttributeByteVec | AttributeDate | AttributeDouble |  AttributeDoubleVec | AttributeEnum | AttributeInteger | AttributeIntegerVec | AttributeString | AttributeStringVec)]:
        """Get the AttributeSet vector

        Returns:
            Vector of Attribute elements
        """
    def SetAttributes(self,
                      elements: list[(AttributeByteVec | AttributeDate | AttributeDouble | AttributeDoubleVec | AttributeEnum | AttributeInteger | AttributeIntegerVec | AttributeString | AttributeStringVec)]):
        """Set the AttributeSet vector

        Args:
            elements: Attribute elements
        """
    def __eq__(self, element: AttributeSet) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, elements: list):
        """Constructor

        Args:
            elements: Attribute elements
        """
    @typing.overload
    def __init__(self, element: AttributeSet):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeSet) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Attributes(self) -> list[(AttributeByteVec | AttributeDate | AttributeDouble |  AttributeDoubleVec | AttributeEnum | AttributeInteger | AttributeIntegerVec | AttributeString | AttributeStringVec)]:
        """Get the AttributeSet vector
        """
    @Attributes.setter
    def Attributes(self, elements: list[(AttributeByteVec | AttributeDate | AttributeDouble |  AttributeDoubleVec | AttributeEnum | AttributeInteger | AttributeIntegerVec | AttributeString | AttributeStringVec)]) -> None:
        """Set the AttributeSet vector

        Args:
            elements: Attribute elements
        """

class AttributeString(Attribute):
    """String attribute
    """
    def __eq__(self, element: AttributeString) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: str):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeString):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeString) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> str:
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: str) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class AttributeStringVec(Attribute):
    """StringVec attribute
    """
    def __eq__(self, element: AttributeStringVec) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, id: int, value: NemAll_Python_Utility.VecStringList):
        """Constructor

        Args:
            id:    Attribute id
            value: Attribute value
        """
    @typing.overload
    def __init__(self, element: AttributeStringVec):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __ne__(self, element: AttributeStringVec) -> bool:
        """Unequal operator

        Args:
            element: Element to compare

        Returns:
            Elements are unequal: true/false
        """
    def __repr__(self) -> str:
        """Convert to string
        """
    @property
    def Value(self) -> NemAll_Python_Utility.VecStringList:
        """Get the attribute value
        """
    @Value.setter
    def Value(self, value: NemAll_Python_Utility.VecStringList) -> None:
        """Set the attribute value

        Args:
            value: Attribute value
        """

class Attributes():
    """Attributes class
    """
    def GetAttributeSets(self) -> list:
        """Get the AttributeSet vector

        Returns:
             Attribute value
        """
    def SetAttributeSets(self, sets: list):
        """Set the AttributeSet vector

        Args:
            sets: AttributeSet vector
        """
    def __eq__(self, props: Attributes) -> bool:
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
    def __init__(self, elements: list):
        """Constructor

        Args:
            elements: Attribute set element list
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
    def AttributeSets(self) -> None:
        """Property for attribute set vector

        :type: None
        """

class CadDataFileReader():

    """Utility for reading data from common CAD files, like IFC or DWG, and converting them into Python objects (like ModelElement3D), but without creating these objects in the drawing file. In this way, the objects can be processed further inside the script e.g., become a part of the created PythonPart.
    """
    @staticmethod
    def ReadIFC(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str) -> list[tuple[str,
                list[NemAll_Python_BasisElements.ModelElement3D]]]:
        """Import the data from an IFC file and return it as Python objects, without creating them
        in the drawing file.

        The method groups objects, that are sub objects of an _IfcElementAssembly_, into
        tuples. If there is no _IfcElementAssembly_ entity in the IFC file, one tuple with all objects is returned.

        **IMPORTANT**: Only objects with the IfcType of _IfcBuildingElementProxy_ are read!

        Args:
            doc:             Document
            fileName:        Full path to the IFC file

        Returns:
            Tuples like (group name, model elements)
        """
    @staticmethod
    def ReadOBJ(fileName: str, designPathLocation: eDesignPathLocation) -> list[NemAll_Python_BasisElements.ModelElement3D]:
        """Import an OBJ file

        Args:
            fileName:              Full file name of the OBJ file
            designPathLocation:    Location of the design path

        Returns:
            List with the model elements
        """
    @staticmethod
    def ReadSKP(fileName: str, designPathLocation: eDesignPathLocation) -> list[NemAll_Python_BasisElements.ModelElement3D]:
        """Import an SKP file

        Args:
            fileName:              Full file name of the SKP file
            designPathLocation:    Location of the design path

        Returns:
            List with the model elements
        """

class CommonProperties():
    """Representation of format properties, common for all kind of Allplan elements, such as General elements, architectural components or reinforcement. This class contains information about e.g. pen thickness, stroke type and color, with which an Allplan element is drawn in the viewport.
    """
    @staticmethod
    def GetColorPenStrokeByLayerFromLayerNumber(layernumber: int) -> (list[int] | NemAll_Python_Utility.VecIntList):
        """Layer number

        Returns:
             [0] = pen,[1] = stroke, [2] color
        """
    def GetGlobalProperties(self):
        """Get the global properties
        """
    def __eq__(self, props: CommonProperties) -> object:
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
    def __init__(self, element: CommonProperties):
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
    def Activated(self) -> bool:
        """Get the activated state
        """
    @Activated.setter
    def Activated(self, value: bool) -> None:
        """Set the activated flag
        """
    @property
    def Color(self) -> int:
        """Get the color
        """
    @Color.setter
    def Color(self, value: int) -> None:
        """Set the color
        """
    @property
    def ColorByLayer(self) -> bool:
        """Get the color by layer state
        """
    @ColorByLayer.setter
    def ColorByLayer(self, value: bool) -> None:
        """Set the color by layer flag
        """
    @property
    def ConstructionLine(self) -> bool:
        """Get the construction line state
        """
    @ConstructionLine.setter
    def ConstructionLine(self, value: bool) -> None:
        """Set the construction line mode
        """
    @property
    def DrawOrder(self) -> int:
        """Get the drawOrder
        """
    @DrawOrder.setter
    def DrawOrder(self, value: int) -> None:
        """Set the drawOrder
        """
    @property
    def ForceColor(self) -> bool:
        """Get flag if force color is set
        """
    @ForceColor.setter
    def ForceColor(self, value: bool) -> None:
        """Set flag - force color to graphic engine
        """
    @property
    def HelpConstruction(self) -> bool:
        """Get flag if pen and stroke is help construction
        """
    @HelpConstruction.setter
    def HelpConstruction(self, value: bool) -> None:
        """Set flag - is help construction
        """
    @property
    def InSpecialWindow(self) -> bool:
        """Get the special window visibility
        """
    @InSpecialWindow.setter
    def InSpecialWindow(self, value: bool) -> None:
        """Set the special window visibility flag
        """
    @property
    def Layer(self) -> int:
        """Get the layer
        """
    @Layer.setter
    def Layer(self, value: int) -> None:
        """Set the layer
        """
    @property
    def Marked(self) -> bool:
        """Get the marked state
        """
    @Marked.setter
    def Marked(self, value: bool) -> None:
        """Set the marked flag
        """
    @property
    def PageNumber(self) -> int:
        """Get the page number
        """
    @PageNumber.setter
    def PageNumber(self, value: int) -> None:
        """Set the page number
        """
    @property
    def Pen(self) -> int:
        """Get the pen
        """
    @Pen.setter
    def Pen(self, value: int) -> None:
        """Set the pen
        """
    @property
    def PenByLayer(self) -> bool:
        """Get the pen by layer state
        """
    @PenByLayer.setter
    def PenByLayer(self, value: bool) -> None:
        """Set the pen by layer flag
        """
    @property
    def Printable(self) -> bool:
        """Get the printable state
        """
    @Printable.setter
    def Printable(self, value: bool) -> None:
        """Set the printable mode
        """
    @property
    def Stroke(self) -> int:
        """Get the stroke
        """
    @Stroke.setter
    def Stroke(self, value: int) -> None:
        """Set the stroke
        """
    @property
    def StrokeByLayer(self) -> bool:
        """Get the stroke by layer state
        """
    @StrokeByLayer.setter
    def StrokeByLayer(self, value: bool) -> None:
        """Set the stroke by layer flag
        """
    @property
    def Visible(self) -> bool:
        """Get the visible flag state
        """
    @Visible.setter
    def Visible(self, value: bool) -> None:
        """Set the visibility
        """
    @property
    def VisibleInsideZoomwindows(self) -> bool:
        """Get the visible inside zoom window state
        """
    @VisibleInsideZoomwindows.setter
    def VisibleInsideZoomwindows(self, value: bool) -> None:
        """Set the visible inside zoom windows flag
        """
    @property
    def VisibleOutsideZoomwindows(self) -> bool:
        """Get the visible outside zoom window state
        """
    @VisibleOutsideZoomwindows.setter
    def VisibleOutsideZoomwindows(self, value: bool) -> None:
        """Set the visible outside zoom windows flag
        """

class DTMService():
    """Implementation of the DTM service
    """
    def GetAllSurfaces(self) -> list[tuple[str, str]]:
        """Get all surfaces

        Returns:
            vector with the surface ID and name
        """
    def GetBorderPolyline(self) -> NemAll_Python_Geometry.Polyline3D:
        """Get the border polyline of the top surfaces

        Returns:
            Border polyline
        """
    def GetEdges(self) -> NemAll_Python_Geometry.Line3DList:
        """Get the edges used for the merge

        Returns:
            Edges used for the merge
        """
    def GetSolid(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, dtmID: str, cutPolygon: NemAll_Python_Geometry.Polygon2D,
                 bottomDistance: float, cutCrossedTriangles: bool) -> bool:
        """Get a solid from the DTM

        Args:
            doc:                 Document
            dtmID:               DTM ID
            cutPolygon:          Cutting polygon
            bottomDistance:      Distance from the DTM to the bottom of the solid
            cutCrossedTriangles: Cut crossed triangles state

        Returns:
            Solid created state
        """
    def GetTopFacePolygons(self) -> NemAll_Python_Geometry.Polygon3DList:
        """Get the top surface polygons

        Returns:
            Top surface polygons
        """
    @typing.overload
    def MergeTopSurface(self, dtmID: str, polyhed: NemAll_Python_Geometry.Polyhedron3D, verticalFacesOffset: float) -> DTMServiceResult:
        """Merge the top surfaces to the DTM

        Args:
            dtmID:               DTM ID
            polyhed:             Polyhedron to merge
            verticalFacesOffset: Bottom offset for vertical faces with 90 degree

        Returns:
            Successfull state
        """
    @typing.overload
    def MergeTopSurface(self, dtmID: str, brep: NemAll_Python_Geometry.BRep3D, verticalFacesOffset: float) -> DTMServiceResult:
        """Merge the top surfaces to the DTM

        Args:
            dtmID:               DTM ID
            brep:                BRep to merge
            verticalFacesOffset: Bottom offset for vertical faces with 90 degree

        Returns:
            Successful state
        """
    def MergeTopSurface(self) -> DTMServiceResult:
        """ Overloaded function. See individual overloads.
        """
    def __init__(self):
        """Initialize
        """

class DTMServiceResult(enum.Enum):
    """Result for the merge of the top surface to the DTM

    eMerged          : Merged
    eMergedWithOffset: Merged by using the vertical faces offset
    eNotMerged       : Not merged
    """
    eMerged = 0
    eMergedWithOffset = 1
    eNotMerged = 2

    names = {eMerged: eMerged,
             eMergedWithOffset: eMergedWithOffset,
             eNotMerged: eNotMerged}

    values = {0: eMerged,
              1: eMergedWithOffset,
              2: eNotMerged}

    def __getitem__(self, key: (str | int | float)) -> DTMServiceResult:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class DocumentResourceService():

    @staticmethod
    def CreateSurface(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, surfaceDirectoryPath: str, localPathAndName: str,
                      surfaceDef: NemAll_Python_BasisElements.SurfaceDefinition, createUniqueName: bool = True, bitmapDefinitions: typing.Dict[NemAll_Python_BasisElements.SurfaceDefinition.SurfaceTextureID, NemAll_Python_BasisElements.BitmapDefinition] = {}) -> str:
        """Create a surface resource with a unique name

        Args:
            doc:                  Document
            surfaceDirectoryPath: Path to the surface directory (e.g. ...\std\design)
            localPathAndName:     Local path and name (extends the surface directory path)
            surfaceDef:           Surface definition
            createUniqueName:     create a unique name state
            bitmapDefinitions:    Bitmap definitions

        Returns:
            Unique name extension of the surface
        """

class DrawingFileLoadState(enum.Enum):
    """Load state of the drawing file
    """
    ActiveBackground = 2
    ActiveForeground = 3
    PassiveBackground = 1

    names = {PassiveBackground: PassiveBackground,
             ActiveBackground: ActiveBackground,
             ActiveForeground: ActiveForeground}

    values = {1: PassiveBackground,
              2: ActiveBackground,
              3: ActiveForeground}

    def __getitem__(self, key: (str | int | float)) -> DrawingFileLoadState:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class ExportImportService():
    """Service for exporting/importing CAD data in common formats, like IFC or DWG.

    During the import, the objects are directly created in the current drawing file.
    To prevent that and get Python objects first, use the utility _CadDataFileReader_. 

    """
    def ExportDWG(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str, configFileName: str, version: int):
        """Export the data to a DWG file by a configuration file

        Args:
            doc:            Document
            fileName:       Name of the DWG file
            configFileName: Name of the DWG configuration file
            version:        Version numer
        """
    def ExportDWGByTheme(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str, themeFileName: str,
                         version: int = 2018):
        """Export the data to a DWG file by a theme file

        Args:
            doc:           Document
            fileName:      Name of the DWG file
            themeFileName: Name of the DWG theme file
            version:       DWG version
        """
    def ExportIFC(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileNumbers: (list[int] | NemAll_Python_Utility.VecIntList),
                  ifcVersion: IFC_Version, fileName: str, ifcThemeFileName: str = ''):
        """Export the data to an IFC file

        Args:
            doc:              Document
            fileNumbers:      Numbers of the drawing files to export
            ifcVersion:       IFC version
            fileName:         Name of the IFC file
            ifcThemeFileName: Name of the theme file
        """
    def ExportXPlan(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                    fileNumbers: (list[int] | NemAll_Python_Utility.VecIntList), xplanFilePath: str):
        """Export the data to a XPlan file

        Args:
            doc:           Document
            fileNumbers:   Numbers of the drawing files to export
            xplanFilePath: Path and name of the XPlan file
        """
    def ImportDWG(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str, configFileName: str,
                  placePnt: NemAll_Python_Geometry.Point3D) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Import the data from a DWG file

        Args:
            doc:            Document
            fileName:       Name of the DWG file
            configFileName: Name of the DWG configuration file
            placePnt:       Placement point of the data
        """
    def ImportIFC(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileNumber: int,
                  fileName: str) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Import the data from an IFC file

        Args:
            doc:        Document
            fileNumber: Number of the drawing file for the data import
            fileName:   Name of the IFC file

        Returns:
            List with the imported elements
        """
    def ImportXPlan(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, xplanFilePath: str, drawingFileNumber: int):
        """Import the data from a XPlan file

        Args:
            doc:               Document
            xplanFilePath:     Path and name of the XPlan file to import
            drawingFileNumber: Starting number of destination drawing file(s)
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: ExportImportService):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class DrawingService():

    """
    """
    @staticmethod
    def LockGraphicsEngineUpdate(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, lockUpdate: bool):
        """Lock the update of the graphics engine

        Args:
            doc:        Document
            lockUpdate: Set to True to lock the update of the graphics engine. Set to False to unlock and update it.
        """
    @staticmethod
    def RedrawAll(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Redraw all
        Args:
             doc        Document
        """
    @staticmethod
    def ResetAndDrawHiddenElement(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                                  hiddenElement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Reset and draw the hidden elements
        Args:
             doc           Document
             hiddenElement Hidden element
        """
    @staticmethod
    def SaveWindowToImageFile(fileName: str, pixelWidth: int = 0, pixelHeight: int = 0) -> bool:
        """Save the window to an image file

        Args:
             fileName        Full file name of the image file
             pixelWidth      Pixel width,  0 = current width
             pixelHeight     Pixel height, 0 = current height
            e:for success
        """
    @staticmethod
    def UpdateAllWindows():
        """Update the drawing in all windows
        """
    @staticmethod
    def UpdateGraphicsEngine(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Update the graphics engine
        Args:
             doc        Document
        """

class DrawingTypeService():
    """Utility for processing the **drawing type**.

    This class provides methods for processing the settings regarding drawing types, such as
    changing the current drawing type or getting the drawing type description based on the ID

    """
    class DefaultDrawingTypes(enum.Enum):
        """Definition of the default drawing types
        """
        eBuildingAlterationDrawing = 309
        eBuildingAlterationDrawingColored = 310
        eBuildingDrawing = 303
        eDesignDrawing = 302
        eGeneralArrangementDrawing = 307
        eKeyPlan = 306
        ePresentationDrawing = 305
        eReinforcementDrawing = 308
        eSchematicDesignDrawing = 301
        eWorkingDrawing = 304

        names = {eSchematicDesignDrawing: eSchematicDesignDrawing,
                 eDesignDrawing: eDesignDrawing,
                 eBuildingDrawing: eBuildingDrawing,
                 eWorkingDrawing: eWorkingDrawing,
                 ePresentationDrawing: ePresentationDrawing,
                 eKeyPlan: eKeyPlan,
                 eGeneralArrangementDrawing: eGeneralArrangementDrawing,
                 eReinforcementDrawing: eReinforcementDrawing,
                 eBuildingAlterationDrawing: eBuildingAlterationDrawing,
                 eBuildingAlterationDrawingColored: eBuildingAlterationDrawingColored}

        values = {301: eSchematicDesignDrawing,
                  302: eDesignDrawing,
                  303: eBuildingDrawing,
                  304: eWorkingDrawing,
                  305: ePresentationDrawing,
                  306: eKeyPlan,
                  307: eGeneralArrangementDrawing,
                  308: eReinforcementDrawing,
                  309: eBuildingAlterationDrawing,
                  310: eBuildingAlterationDrawingColored}

        def __getitem__(self, key: (str | int | float)) -> DrawingTypeService.DefaultDrawingTypes:
            """ get the item for a key

            Args:
                key: value key

            Returns:
                value for the key
            """
            return self.values[key]


    @staticmethod
    def GetCurrentDrawingTypeDescription(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> str:
        """Get the description of the current drawing type

        Args:
            doc: Document

        Returns:
            Description of the current drawing type
        """
    @staticmethod
    def GetCurrentDrawingTypeId(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> int:
        """Get the current drawing type ID

        Args:
            doc: Document

        Returns:
            Current drawing type ID
        """
    @staticmethod
    def GetDrawingTypeDescription(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, drawingTypeId: int) -> str:
        """Get the description of the drawing type

        Args:
            doc:           Document
            drawingTypeId: Drawing type ID

        Returns:
            Description of the drawing type
        """
    @staticmethod
    def GetDrawingTypeDescriptions(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> NemAll_Python_Utility.VecStringList:
        """Get the description of the drawing types

        Args:
            doc: Document

        Returns:
            Drawing type desccriptions
        """
    @staticmethod
    def GetDrawingTypeIdFromDescription(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, typeDescription: str) -> int:
        """Get the ID of the drawing type from the description

        Args:
            doc:             Document
            typeDescription: Drawing type description

        Returns:
            ID of the drawing type
        """
    @staticmethod
    def SetDrawingTypeId(drawingTypeId: int):
        """Set the drawing type ID

        Args:
            drawingTypeId: ID of the drawing type
        """
    eBuildingAlterationDrawing = DefaultDrawingTypes.eBuildingAlterationDrawing
    eBuildingAlterationDrawingColored = DefaultDrawingTypes.eBuildingAlterationDrawingColored
    eBuildingDrawing = DefaultDrawingTypes.eBuildingDrawing
    eDesignDrawing = DefaultDrawingTypes.eDesignDrawing
    eGeneralArrangementDrawing = DefaultDrawingTypes.eGeneralArrangementDrawing
    eKeyPlan = DefaultDrawingTypes.eKeyPlan
    ePresentationDrawing = DefaultDrawingTypes.ePresentationDrawing
    eReinforcementDrawing = DefaultDrawingTypes.eReinforcementDrawing
    eSchematicDesignDrawing = DefaultDrawingTypes.eSchematicDesignDrawing
    eWorkingDrawing = DefaultDrawingTypes.eWorkingDrawing

class ElementsAttributeService():

    """Service for processing **attributes of existing model elements**. The service provides methods to e.g. read or modify attribute values.
    """
    @staticmethod
    def ChangeAttribute(attributeNumber: int, newValue: object, elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList,
                        setUndefAttrib: bool = False, setDeleteAttrib: bool = False) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Change an attribute

        Args:
            attributeNumber:    Attribute number
            newValue:           New value
            elements:           Elements
            setUndefAttrib:     Set Attribute undefined (optional)
            setDeleteAttrib:    Delete Attribute (optional)

        Returns:
             Adapted elements
        """
    @staticmethod
    def ChangeAttributes(attributeDataList: list, elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList,
                         setUndefAttrib: bool = False, setDeleteAttrib: bool = False) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Change an attribute

        Args:
            attributeDataList:  List with the attribute data as tuple(number, value)
            elements:           Elements as BaseElementAdapterList
            setUndefAttrib:     Set Attribute undefined (optional)
            setDeleteAttrib:    Delete Attribute (optional)

        Returns:
             Modified elements
        """
    @staticmethod
    def GetAttributes(ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                      readState: eAttibuteReadState = eAttibuteReadState.ReadAll) -> list:
        """Get the attributes from an element

        Args:
            ele:        Element adapter
            readState:  What attributes to read

        Returns:
            Attributes
        """

class ElementsByAttributeService():
    """Service for selecting elements in the current document based on the value of a specific
    attribute. The ID of this attribute must be given during the service initialization. The service
    is a singleton, meaning that there can only exist one instance of it.

    Examples:
      Initialize the service as follows:
  
      >>> AllplanBaseElements.ElementsByAttributeService.GetInstance().Init(attribute_id, document)

      Then select elements whose attribute value is equal to the desired one, as follows:

      >>> elements = AllplanBaseElements.ElementsByAttributeService.GetInstance().GetElements(attribute_value)

    """
    @typing.overload
    def GetElements(self, attributeValue: float) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Get the elements for the double attribute value

        Args:
            attributeValue: Attribute value

        Returns:
            Elements
        """
    @typing.overload
    def GetElements(self, attributeValue: int) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Get the elements for the integer attribute value

        Args:
            attributeValue: Attribute value

        Returns:
            Elements
        """
    @typing.overload
    def GetElements(self, attributeValue: str) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Get the elements for the string attribute value

        Args:
            attributeValue: Attribute value

        Returns:
            Elements
        """
    def GetElements(self) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def GetInstance() -> ElementsByAttributeService:
        """Get the instance

        Returns:
            Instance of the singleton
        """
    def Init(self, attributeID: int, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Initialize the service.

        Args:
            attributeID: Attribute ID. Used for creating fast element access by an attribute value of this ID
            doc:         Document
        """

class ElementsLayerService():

    """Service for processing (changing) the **layer of existing model elements**.
    """
    @staticmethod
    def ChangeLayer(elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList,
                    newValue: str) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Change the Layer

        Args:
            elements:          Elements to change
            newValue:          New value

        Returns:
             List with the modified elements
        """

class ElementsPropertyService():

    """Service for modifying various properties of existing model elements, such as surface.

    """
    @staticmethod
    def ModifyFormatProperties(arg2: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """
        """
    @staticmethod
    def ModifySurface(surfacePathFile: str,
                      elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Change the surface

        Args:
            surfacePathFile:   New surface path and file
            elements:          Elements to modify

        Returns:
             Modified elements
        """

class ElementsSelectService():

    @staticmethod
    def SelectAllElements(ele: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Select all elements from the document

        Args:
            doc: Document

        Returns:
             All elements from the document
        """
    @staticmethod
    def SelectElementsByIfcGuid(ele: list) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Select elements by IFC guids

        Args:
            doc:        Document
            ifcGuids:   List with the IFC GUIDs

        Returns:
             Elements
        """

class DrawingFileService(ExportImportService):
    """Service for processing the **drawing files**

    This class provides methods for changing the load state of drawing files (active in foreground,
    active in background or passive), as well as for changing the drawing-file-specific properties,
    such as scale.

    """
    def CreateBendingSchedule(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, refPnt: NemAll_Python_Geometry.Point2D):
        """Create a bending schedule

        Args:
            doc:        Document
            refPnt:     Reference point of the bending schedule
        """
    def DeleteDocument(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Delete the context of the active document
        Args:
            doc:        Document
        """
    def ExportBendingMachine(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str, project: str, plan: str,
                             index: str, bSplitGroups: bool):
        """Export the reinforcement data for the bending machine

        Args:
            doc:            Document
            fileName:       Name of the output file
            project:        Name of the project
            plan:           Name of the plan
            index:          Index as text
            bSplitGroups:   Split the reinforcement groups
        """
    def ExportBendingMachinePerPrecast(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str, project: str, plan: str,
                                       index: str, bSplitGroups: bool, precastelement: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter):
        """Export the reinforcement data for the bending machine per PrecastElement

        Args:
            doc:            Document
            fileName:       Name of the output file
            project:        Name of the project
            plan:           Name of the plan
            index:          Index as text
            bSplitGroups:   Split the reinforcement groups           precastelement  precastelement from which the reinforcement should be exported
        """
    @staticmethod
    def GetActiveFileNumber() -> int:
        """Get the drawing file number of the active document
        """
    @staticmethod
    def GetDrawingFileName(DrawingFileNumber: int) -> tuple[bool, str]:
        """Args:
            int:            DrawingFileNumber

        Returns:
            tuple(bool,str)    (Success ,Name of the drawing file)
        """
    def GetFileState(self) -> list[tuple[int, DrawingFileLoadState]]:
        """Get the file state of all loaded drawing files
        Returns:
            list with a tuple(file index, drawing file load state)
        """
    def LoadFile(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileIndex: int, loadState: DrawingFileLoadState):
        """Load a drawing file

        Args:
            doc:        Document
            fileIndex:  Index of the drawing file
            loadState:  File load state
        """
    @staticmethod
    def RenameDrawingFile(DrawingFileNumber: int, NewName: str) -> bool:
        """RenameDrawingFile

        Args:
            int:           DrawingFileNumber
            string:        NewName

        Returns:
            bool              Success
        """
    def SetScalingFactor(self, arg2: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, arg3: float):
        """Set the scaling factor of the current document

        Args:
            arg2: Document adapter
            arg3: Scaling factor. For a scale of 1:20, set 20.0. For a scale 2:1, set 0.5
        """
    @staticmethod
    def ShowDrawingFileDialog(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, singleSelection: bool,
                              deactivateDerived: bool) -> list:
        """Show a dialog to select drawing files.

        Args:
            doc:                Document adapter providing context for available drawing files.
            singleSelection:    If true, only a single file can be selected; otherwise, multiple selection is allowed.
            deactivateDerived:  If true derived structure is deactivated.

        Returns:
            list               Indices of the selected drawing files.
        """
    def UnloadAll(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Unload all drawing files

        Args:
            doc:        Document
        """
    def UnloadFile(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileIndex: int):
        """Unload a drawing file

        Args:
            doc:        Document
            fileIndex:  Index of the drawing file
        """
    def __init__(self):
        """Initialize
        """

class FaceSelectService():

    @staticmethod
    def SelectPolyhedronFace(polyhedron: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, pnt: NemAll_Python_Geometry.Point2D,
                             highlightFace: bool, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, includeUVSSelection: bool) -> tuple[bool, NemAll_Python_Geometry.Polygon3D, NemAll_Python_Geometry.IntersectionRayPolyhedron]:
        """Select a polyhedron face

        Args:
            polyhedron:          Polyhedron
            pnt:                 Selection view point
            highlightFace:       Highlight the face state
            viewProj:            View world projection of the selected view
            doc:                 Document
            includeUVSSelection: Include an UVS selection for the face

        Returns:
            select state, face polygon, intersection result
        """
    @staticmethod
    def SelectPolyhedronFaceInUVS(polyhedron: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, pnt: NemAll_Python_Geometry.Point2D,
                                  highlightFace: bool, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> tuple[bool, NemAll_Python_Geometry.Polygon3D, NemAll_Python_Geometry.IntersectionRayPolyhedron, NemAll_Python_Geometry.Matrix3D]:
        """Select a polyhedron face in an UVS

        Args:
            polyhedron:    Polyhedron
            pnt:           Selection view point
            highlightFace: Highlight the face state
            viewProj:      View world projection of the selected view
            doc:           Document

        Returns:
            select state, face polygon, intersection result, UVS matrix
        """
    @staticmethod
    def SelectWallFace(wallTier: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, pnt: NemAll_Python_Geometry.Point2D,
                       highlightFace: bool, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, includeUVSSelection: bool) -> tuple[bool, NemAll_Python_Geometry.Polygon3D, NemAll_Python_Geometry.IntersectionRayPolyhedron]:
        """Select a wall face

        Args:
            wallTier:            Wall tier
            pnt:                 Selection view point
            highlightFace:       Highlight the face state
            viewProj:            View world projection of the selected view
            doc:                 Document
            includeUVSSelection: Include an UVS selection for the face

        Returns:
            select state, face polygon, intersection result
        """
    @staticmethod
    def SelectWallFaceInUVS(wallTier: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, pnt: NemAll_Python_Geometry.Point2D,
                            highlightFace: bool, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> tuple[bool, NemAll_Python_Geometry.Polygon3D, NemAll_Python_Geometry.IntersectionRayPolyhedron, NemAll_Python_Geometry.Matrix3D]:
        """Select a wall face in an UVS

        Args:
            wallTier:      Wall tier
            pnt:           Selection view point
            highlightFace: Highlight the face state
            viewProj:      View world projection of the selected view
            doc:           Document

        Returns:
            select state, face polygon, intersection result, UVS matrix
        """

class IFC_Version(enum.Enum):
    """IFC version
    """
    Ifc_2x3 = 4
    Ifc_4 = 7
    Ifc_XML_2x3 = 5
    Ifc_XML_4 = 8

    names = {Ifc_2x3: Ifc_2x3,
             Ifc_XML_2x3: Ifc_XML_2x3,
             Ifc_4: Ifc_4,
             Ifc_XML_4: Ifc_XML_4}

    values = {4: Ifc_2x3,
              5: Ifc_XML_2x3,
              7: Ifc_4,
              8: Ifc_XML_4}

    def __getitem__(self, key: (str | int | float)) -> IFC_Version:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class InformationPaletteService():
    """Implementation of the exposed fill buton for information palette
    """
    @staticmethod
    def FillBaseObjectList(document: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                           elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList):
        """Execute call of function FillBaseObjectList from InformationPaletteManagerImpl - Open and fill information palette with passed elements

        Args:
            document: Element's document
            elements: Passed elements

        Returns:
            Call function fill from informationPaletteManagerImpl
        """
    @staticmethod
    def SetSettings(settings: InformationPaletteSettingsHelper):
        """Set settings for information palette (AttributeOrder, VisibleAttributes, ....)

        Args:
            settings
        """

class InformationPaletteSettingsHelper():
    """Settings for InformationPalette.
    """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: InformationPaletteSettingsHelper):
        """Copy constructor

        Args:
            element: Element to copy
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @property
    def AttributeOrder(self) -> list[int:
        """attribute order
        """
    @AttributeOrder.setter
    def AttributeOrder(self, value: list[int) -> None:
        """attribute order
        """
    @property
    def AttributeSorting(self) -> list[NemAll_Python_Utility.wstring]:
        """attribute sorting
        """
    @AttributeSorting.setter
    def AttributeSorting(self, value: list[NemAll_Python_Utility.wstring]) -> None:
        """attribute sorting
        """
    @property
    def FilterTags(self) -> list[NemAll_Python_Utility.wstring]:
        """filter tags
        """
    @FilterTags.setter
    def FilterTags(self, value: list[NemAll_Python_Utility.wstring]) -> None:
        """filter tags
        """
    @property
    def GroupSortDirection(self) -> bool:
        """group sort direction
        """
    @GroupSortDirection.setter
    def GroupSortDirection(self, value: bool) -> None:
        """group sort direction
        """
    @property
    def GroupingTags(self) -> list[NemAll_Python_Utility.wstring]:
        """grouping tags
        """
    @GroupingTags.setter
    def GroupingTags(self, value: list[NemAll_Python_Utility.wstring]) -> None:
        """grouping tags
        """
    @property
    def SearchTags(self) -> list[NemAll_Python_Utility.wstring]:
        """search tags
        """
    @SearchTags.setter
    def SearchTags(self, value: list[NemAll_Python_Utility.wstring]) -> None:
        """search tags
        """
    @property
    def SelectedAttributesForTotals(self) -> list[int:
        """selected attributes for totals
        """
    @SelectedAttributesForTotals.setter
    def SelectedAttributesForTotals(self, value: list[int) -> None:
        """selected attributes for totals
        """
    @property
    def VisibleAttributes(self) -> list[int:
        """visible attributes
        """
    @VisibleAttributes.setter
    def VisibleAttributes(self, value: list[int) -> None:
        """visible attributes
        """

class LayerService():

    """Utility for processing the **layer definitions**.

    This class provides method to retrieve data specific for layer definition e.g.,
    the name of the layer based on its ID or the layer ID based on its name. It can also
    export/import the layer definitions to/from a file.

    """
    @staticmethod
    def GetIDByShortName(shortName: str, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter) -> int:
        """Get the ID by the short name

        Args:
            shortName:  Short name of the layer
            doc:        Document

        Returns:
             ID by name
        """
    @staticmethod
    def GetNameByID(layerID: int, documentID: int) -> str:
        """Get the name by the ID

        Args:
            layerID:    Layer ID
            documentID: Document ID

        Returns:
             Name by ID
        """
    @staticmethod
    def GetShortNameByID(layerID: int, documentID: int) -> str:
        """Get the short name by the ID

        Args:
            layerID:    Layer ID
            documentID: Document ID

        Returns:
             Name by ID
        """
    @staticmethod
    def LoadFromFavoriteFile(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str) -> bool:
        """Load the layer data from a favorite file

        Args:
            doc:      Document
            fileName: File name

        Returns:
             Data are loaded: true/false
        """
    @staticmethod
    def SaveToFavoriteFile(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str) -> bool:
        """Save the layer data to a favorite file

        Args:
            doc:      Document
            fileName: File name

        Returns:
             Data are saved: true/false
        """

class LayoutBorderDefinition():
    """Representation of the print layout border.

    This class represents the properties and settings of the border around a print layout.

    """
    def __init__(self):
        """Initialize
        """
    @property
    def DistanceBinding(self) -> None:
        """Set/get the distance binding

        :type: None
        """
    @property
    def DistanceDefault(self) -> None:
        """Set/get the default distance

        :type: None
        """
    @property
    def ExtraLineColor(self) -> None:
        """Set/get the extra line color

        :type: None
        """
    @property
    def ExtraLinePen(self) -> None:
        """Set/get the extra line peb

        :type: None
        """
    @property
    def ExtraLineStroke(self) -> None:
        """Set/get the extra line stroke

        :type: None
        """
    @property
    def FoldingBindingWidth(self) -> None:
        """Set/get the

        :type: None
        """
    @property
    def FoldingPageHeight(self) -> None:
        """Set/get the folding - height of the pages

        :type: None
        """
    @property
    def FoldingPageHeightTolNeg(self) -> None:
        """Set/get the folding - max. negative tolerance of page height

        :type: None
        """
    @property
    def FoldingPageHeightTolPlus(self) -> None:
        """Set/get the folding - max. positive tolerance of page height

        :type: None
        """
    @property
    def FoldingPageWidth(self) -> None:
        """Set/get the folding - width of the pages

        :type: None
        """
    @property
    def FoldingPageWidthTolNeg(self) -> None:
        """Set/get the folding - max. negative tolerance of page width

        :type: None
        """
    @property
    def FoldingPageWidthTolPlus(self) -> None:
        """Set/get the folding - max. positive tolerance of page width

        :type: None
        """
    @property
    def FoldingType(self) -> None:
        """Set/get the folding type

        :type: None
        """
    @property
    def Index(self) -> None:
        """Set/get the index

        :type: None
        """
    @property
    def InnerLineColor(self) -> None:
        """Set/get the inner line color

        :type: None
        """
    @property
    def InnerLinePen(self) -> None:
        """Set/get the inner line pen

        :type: None
        """
    @property
    def InnerLineStroke(self) -> None:
        """Set/get the inner line stroke

        :type: None
        """
    @property
    def Name(self) -> None:
        """Get/set the name

        :type: None
        """
    @property
    def OuterLineColor(self) -> None:
        """Set/get the outer line color

        :type: None
        """
    @property
    def OuterLinePen(self) -> None:
        """Set/get the outer line pen

        :type: None
        """
    @property
    def OuterLineStroke(self) -> None:
        """Set/get the outer line stroke

        :type: None
        """
    @property
    def UseExtraLine(self) -> None:
        """Set/get the extra line state

        :type: None
        """
    @property
    def UseInnerLine(self) -> None:
        """Set/get the inner line state

        :type: None
        """
    @property
    def UserDefined(self) -> None:
        """Set/get the user defined state

        :type: None
        """

class LayoutFileService():

    """Service for processing the **print layout files**

    This class provides methods for processing the print layouts, such as loading a specific
    print layout, assigning a print profile to it or exporting CAD data.

    """
    def AssignPrintProfile(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, printProfile: str):
        """Set the print profile of the active document

        Args:
            doc:            Document
            printProfile:   Full name of the print profile
        """
    def CreateMasterLayoutElement(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, layoutMasterData: LayoutMasterData):
        """Create the master layout element

        Args:
            doc:              Document
            layoutMasterData: Layout master data
        """
    def DeleteDocument(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Delete the content of the active document

        Args:
            doc:        Document
        """
    def ExportDWG(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, layoutFileIndex: int, fileName: str, configFileName: str):
        """Export the data to a DWG file

        Args:
            doc:            Document
            layoutFileIndex:Index of the layout file
            fileName:       Name of the DWG file
            configFileName: Name of the DWG configuration file
        """
    def ExportPDF(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, layoutFileIndex: int, fileName: str, configFileName: str):
        """Export the data to a PDF file

        Args:
            doc:            Document
            layoutFileIndex:Index of the layout file
            fileName:       Name of the PDF file
            configFileName: Name of the PDF configuration file
        """
    @staticmethod
    def GetLayoutFileName(LayoutFileNumber: int) -> tuple:
        """GetLayoutFileName

        Args:
            int:            LayoutFileNumber

        Returns:
            tuple(bool,str)    (Success, Name of the layout file)
        """
    def ImportDWG(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, fileName: str, configFileName: str,
                  placePnt: NemAll_Python_Geometry.Point2D) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
        """Import the data from an DWG file

        Args:
            doc:            Document
            fileName:       Name of the DWG file
            configFileName: Name of the DWG configuration file
            placePnt:       Placement point of the data
        """
    def InsertDrawingFile(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, doc: list,
                          fileIndexList: NemAll_Python_Geometry.Point2D, placePnt: float, rotationAngle: float, scale: NemAll_Python_Geometry.Point2D, clipBoxLeftBottom: NemAll_Python_Geometry.Point2D, clipBoxRightTop: (list[int] | NemAll_Python_Utility.VecIntList), layerList: float, textFactor: bool, bUseRefPnt: NemAll_Python_Geometry.Point2D, refPnt: NemAll_Python_Geometry.MinMax3D):
        """Insert drawing files in the layout file

        Args:
            doc:                     Document
            fileIndexList:           List with the drawing file indices           placePnt                 Placement point
            rotationAngle:           Rotation angle
            scale:                   Scale
            clipBoxLeftBottom:       Left bottom point of the clipping box
            clipBoxRightTop:         Top right point of the clipping box
            layerList:               List with the insertion layers
            textFactor:              Text factor
            bUseRefPnt:              Use the reference point for the placement
            refPnt:                  Reference point of the drawing file
            drawingMinMaxClipping:   Min/max coordinates of the clipping area from the drawing file
        """
    @staticmethod
    def LoadFile(doc: LayoutFileService, fileIndex: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, loadState: int):
        """Load a layout file

        Args:
            doc:        Document
            fileIndex:  Index of the layout file
        """
    @staticmethod
    def RenameLayoutFile(LayoutFileNumber: int, NewName: str) -> bool:
        """RenameLayoutFile

        Args:
            int:           LayoutFileNumber
            string:        NewName

        Returns:
            bool              Success
        """
    def __init__(self):
        """Initialize
        """

class LayoutMargin():
    """Representation of the print layout margins
    """
    def __init__(self):
        """Initialize
        """
    @property
    def Bottom(self) -> None:
        """Bottom margin"""
    @property
    def Left(self) -> None:
        """Left margin"""
    @property
    def Right(self) -> None:
        """Right margin"""
    @property
    def Top(self) -> None:
        """Top margin"""

class LayoutMasterData():
    """Representation of a **print layout**

    This class is a representation of a print layout and contains all the main settings 
    specific for it, such as sheet size, margins or type of layout header.

    """
    def __init__(self):
        """Initialize
        """
    @property
    def BackgroundType(self) -> None:
        """Set/get the background type (0-none, 1- color, 2-filling/gradient filling, 3 texture)

        :type: None
        """
    @property
    def Border(self) -> None:
        """Set/get the border

        :type: None
        """
    @property
    def Filling(self) -> None:
        """Set/get the filling

        :type: None
        """
    @property
    def LayoutHeaderOffsetX(self) -> None:
        """Set/get the horizontal distance between legend frame and inner line of border

        :type: None
        """
    @property
    def LayoutHeaderOffsetY(self) -> None:
        """Set/get the vertical  distance between legend frame and inner line of border

        :type: None
        """
    @property
    def LayoutHeaderType(self) -> None:
        """Set/get the header type (0-none, 1-stamp, 2-legend)

        :type: None
        """
    @property
    def Legend(self) -> None:
        """Set/get the legend

        :type: None
        """
    @property
    def Margin(self) -> None:
        """Set/get the margin

        :type: None
        """
    @property
    def SheetSize(self) -> None:
        """Set/get the size of the sheet

        :type: None
        """
    @property
    def Stamp(self) -> None:
        """Set/get the stamp

        :type: None
        """
    @property
    def Texture(self) -> None:
        """Set/get the texture

        :type: None
        """
    @property
    def UseBorder(self) -> None:
        """Set/get the use border state

        :type: None
        """
    @property
    def UseMargins(self) -> None:
        """Set/get the use margins state

        :type: None
        """
    @property
    def UseProperties(self) -> None:
        """Set/get the use properties state

        :type: None
        """

class LayoutMasterLegendData():
    """Representation of a **legend inside a print layout**.

    This data class contains information about the legend, which is to be used inside a print layout
    """
    def __init__(self):
        """Initialize
        """
    @property
    def FileID(self) -> None:
        """Set/get the file ID

        :type: None
        """
    @property
    def ItemID(self) -> None:
        """Set/get the item ID

        :type: None
        """
    @property
    def LegendName(self) -> None:
        """Get/set the legend name

        :type: None
        """
    @property
    def PathID(self) -> None:
        """Set/get the path ID

        :type: None
        """

class LayoutMasterStampData():
    """Representation of a **stamp** (aka label) **inside a print layout**.

    This data class contains information about the stamp (in Allplan also referred to as _label_), which
    is to be used inside a print layout.
    """
    def __init__(self):
        """Initialize
        """
    @property
    def FileID(self) -> None:
        """Set/get the file ID

        :type: None
        """
    @property
    def ItemID(self) -> None:
        """Set/get the item ID

        :type: None
        """
    @property
    def PathID(self) -> None:
        """Set/get the path ID

        :type: None
        """
    @property
    def StampName(self) -> None:
        """Get/set the stamp name

        :type: None
        """

class LayoutSize():
    """Data class containing information about the sheet size of a print layout.
    """
    def __init__(self):
        """Initialize
        """
    @property
    def Height(self) -> None:
        """Layout height"""
    @property
    def Index(self) -> None:
        """Index"""
    @property
    def Name(self) -> None:
        """Name of the layout size, e.g. "DIN A4""""
    @property
    def UserDefined(self) -> None:
        """Whether the size of the print layout should be defined freely by width & height, or to use predefined size defined in the property _name_."""
    @property
    def Width(self) -> None:
        """Layout width"""

class ModifyPropertyID(enum.Enum):
    """Property ID for the modification
    """
    Color = 8
    ColorByLayer = 1003
    FaceStyle = 19
    Hatching = 1
    Layer = 14
    Pen = 6
    PenByLayer = 1001
    Stroke = 7
    StrokeByLayer = 1002

    names = {Pen: Pen,
             Stroke: Stroke,
             Color: Color,
             PenByLayer: PenByLayer,
             StrokeByLayer: StrokeByLayer,
             ColorByLayer: ColorByLayer,
             Layer: Layer,
             Hatching: Hatching,
             FaceStyle: FaceStyle}

    values = {6: Pen,
              7: Stroke,
              8: Color,
              1001: PenByLayer,
              1002: StrokeByLayer,
              1003: ColorByLayer,
              14: Layer,
              1: Hatching,
              19: FaceStyle}

    def __getitem__(self, key: (str | int | float)) -> ModifyPropertyID:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PathID(enum.Enum):
    """Path IDs for the stamp
    """
    PathDefaultID = 20
    PathOfficeID = 30
    PathPrivateID = 8
    PathProjectID = 1

    names = {PathProjectID: PathProjectID,
             PathOfficeID: PathOfficeID,
             PathDefaultID: PathDefaultID,
             PathPrivateID: PathPrivateID}

    values = {1: PathProjectID,
              30: PathOfficeID,
              20: PathDefaultID,
              8: PathPrivateID}

    def __getitem__(self, key: (str | int | float)) -> PathID:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class PlaneService():
    """Implementation of the plane service
    """
    @staticmethod
    def CreateBRepSurfacePlane(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, planeSurface: NemAll_Python_Geometry.BRep3D,
                               surfaceName: str, isVisible: bool) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Create a BRep3D surface plane

        Args:
            doc:          Document
            planeSurface: Plane surface
            surfaceName:  Name of the surface
            isVisible:    Visible state

        Returns:
            Plane element
        """
    @staticmethod
    def CreatePolyhedronSurfacePlane(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                                     planeSurface: NemAll_Python_Geometry.Polyhedron3D, surfaceName: str, isVisible: bool) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Create a Polyhedron3D surface plane

        Args:
            doc:          Document
            planeSurface: Plane surface
            surfaceName:  Name of the surface
            isVisible:    Visible state

        Returns:
            Plane element
        """
    def GetCurrentLevelModelGuid(self) -> NemAll_Python_IFW_ElementAdapter.GUID:
        """Get the current level model GUID of the active drawing file

        Returns:
            Level modle GUID
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Constructor

        Args:
            doc: Document
        """
    @typing.overload
    def __init__(self, element: PlaneService):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class ProjectAttributeService():
    """Utility for processing the values of **project-specific attributes**

    This utility class provides methods for processing the project-specific attributes, such as
    reading or modifying the attribute values of the current project or reading all the attributes
    from all available projects.

    """
    @staticmethod
    @typing.overload
    def ChangeAttributeFromCurrentProject(attributeNumber: int, newValue: int, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Change a project attribute from the current file

        Args:
            attributeNumber: Attribute number
            newValue:        Attribute value
            doc:             Document
        """
    @staticmethod
    @typing.overload
    def ChangeAttributeFromCurrentProject(attributeNumber: int, newValue: float, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Change a project attribute from the current file

        Args:
            attributeNumber: Attribute number
            newValue:        Attribute value
            doc:             Document
        """
    @staticmethod
    @typing.overload
    def ChangeAttributeFromCurrentProject(attributeNumber: int, newValue: str, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Change a project attribute from the current file

        Args:
            attributeNumber: Attribute number
            newValue:        Attribute value
            doc:             Document
        """
    @staticmethod
    def ChangeAttributeFromCurrentProject():
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def ChangeAttributesFromCurrentProject(attributes: list[tuple[int, (int | float | str)]],
                                           doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
        """Change attributes from the current project

        Args:
            attributes: Attributes
            doc:        Document
        """
    @staticmethod
    def GetAttributesFromAllProjects() -> list[tuple[int, (int | float | str)]]:
        """Get the attributes from all projects

        Returns:
            Attributes from all projects
        """
    @staticmethod
    def GetAttributesFromCurrentProject() -> list[tuple[int, (int | float | str)]]:
        """Get the attributes from the current project

        Returns:
            Attributes from the current project
        """

class ProjectService():

    """Utility for processing the **Allplan project**

    This utility class provides methods for processing the Allplan project, such as switching
    between projects or getting the project path.

    """
    @staticmethod
    def CloseAllplan():
        """Close Allplan
        """
    @staticmethod
    def GetCurrentProjectNameAndHost() -> tuple:
        """Get the project and host name

        Returns:
               tuple(project name, host name)
        """
    @staticmethod
    def GetCurrentUserAsBwsPath() -> str:
        """Get the current user as BWS path

        Returns:
               User as BWS path
        """
    @staticmethod
    def GetProjectPath(projectName: str, hostName: str) -> tuple:
        """Get the project path

        Args:
            hostName:    Host name
            projectName: Project name

        Returns:
               tuple(Error, project path)
        """
    @staticmethod
    def OpenProject(hostName: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, projectName: str, doc: str) -> str:
        """Open the project

        Args:
            doc:          Document
            hostName:     Host name
            projectName:  Project name

        Returns:
            String with the result the attempt to open the project. Possible results are:

                -   Active project
                -   Project not exist
                -   Not possible to open the project
                -   Project opened
        """

class PythonPartService():

    """Utility for processing **PythonParts** existing in the drawing file

    This utility class provides methods for processing the PythonParts, that exist
    in the drawing file, such as reading and modifying their parameter values.

    """
    @staticmethod
    def GetParameter(ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, WithProxyIDsForLongValues: bool = False) -> tuple:
        """Get the parameter of the PythonPart

        Args:
            ele:                            Element
            WithProxyIDsForLongValues:   bool (optional)

        Returns:
            True, when reading was successful. False otherwise.
            Name of the PythonPart
            Parameter list
        """
    @staticmethod
    def GetPlacementMatrix(ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> tuple:
        """Get the placement matrix of the PythonPart

        Args:
            ele:  Element

        Returns:
            True, when reading was successful. False otherwise.
            Placement matrix
        """
    @staticmethod
    def IsPythonPartElement(ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> bool:
        """Check for a PythonPart element

        Args:
            ele: Element

        Returns:
            PythonPart element state
        """
    @staticmethod
    def IsPythonPartGroupElement(ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> bool:
        """Check for a PythonPart group element

        Args:
            ele: Element

        Returns:
            PythonPart groupd element state
        """
    @staticmethod
    def SetParameter(ele: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter, name: str,
                     paramList: list) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapter:
        """Set the parameter of the PythonPart

        Args:
            ele:        Element
            paramList:  Parameter list

        Returns:
               Modified element
        """

class ViewSectionPreview():

    def CollectPreviewElements(self, doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                               generalsectionProperties: NemAll_Python_BasisElements.SectionGeneralProperties):
        """Rotate the elements

        Args:
            doc:                        Document
            generalsectionProperties:   General section properties
        """
    def DrawPreview(self, placementPoint: NemAll_Python_Geometry.Point2D, placementPoint: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                    doc: NemAll_Python_BasisElements.SectionGeneralProperties, generalsectionProperties: bool) -> NemAll_Python_Geometry.Point3D:
        """Rotate the elements

        Args:
            placementPoint:             Placement point
        """
    def __init__(self):
        """Initialize
        """

class ZoomService():
    """Implementation of the zoom service
    """
    def ZoomToElement(self, element: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                      viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, inflateValue: float, bZoomAll: bool):
        """Zoom to the element

        Args:
            element:      Element
            viewProj:     View world projection
            inflateValue: Inflate value for the min/max box
            bZoomAll:     Zoom in all views state
        """
    def ZoomToElementWithFactor(self, element: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter,
                                viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, factor: float, bZoomAll: bool):
        """Zoom to the element

        Args:
            element:  Element
            viewProj: View world projection
            factor:   Factor for zooming, 0.5 means 50% zooming
            bZoomAll: Zoom in all views state
        """
    def ZoomToElements(self, elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList,
                       viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, inflateValue: float, bZoomAll: bool):
        """Zoom to the elements

        Args:
            elements:     Elements
            viewProj:     View world projection
            inflateValue: Inflate value for the min/max box
            bZoomAll:     Zoom in all views state
        """
    def ZoomToElementsWithFactor(self, elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList,
                                 viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, factor: float, bZoomAll: bool):
        """Zoom to the elements

        Args:
            elements: Elements
            viewProj: View world projection
            factor:   Factor for zooming, 0.5 means 50% zooming
            bZoomAll: Zoom in all views state
        """
    @typing.overload
    def ZoomToMinMaxBox(self, minMaxBox: NemAll_Python_Geometry.MinMax3D, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection,
                        inflateValue: float, bZoomAll: bool):
        """Zoom to the min/max box

        Args:
            minMaxBox:    Zoom area
            viewProj:     View world projection
            inflateValue: Inflate value for the min/max box
            bZoomAll:     Zoom in all views state
        """
    @typing.overload
    def ZoomToMinMaxBox(self, minMaxBox: NemAll_Python_Geometry.MinMax3D, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection,
                        inflateValueX: float, inflateValueY: float, inflateValueZ: float, bZoomAll: bool):
        """Zoom to the min/max box

        Args:
            minMaxBox:     Zoom area
            viewProj:      View world projection
            inflateValueX: Inflate value for the min/max box in x direction
            inflateValueY: Inflate value for the min/max box in y direction
            inflateValueZ: Inflate value for the min/max box in z direction
            bZoomAll:      Zoom in all views state
        """
    def ZoomToMinMaxBox(self):
        """ Overloaded function. See individual overloads.
        """
    def ZoomToMinMaxBoxWithFactor(self, minMaxBox: NemAll_Python_Geometry.MinMax3D, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection,
                                  factor: float, bZoomAll: bool):
        """Zoom to the min/max box

        Args:
            minMaxBox: Zoom area
            viewProj:  View world projection
            factor:    Factor for zooming, 0.5 means 50% zooming
            bZoomAll:  Zoom in all views state
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: ZoomService):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class eAttibuteReadState(enum.Enum):
    """Enumeration of possible attribute reading modes of the ElementAttributeService
    """
    DoNotRead = 2
    """Do not read any attributes"""
    ReadAll = 1
    """Read all attributes, without computed ones"""
    ReadAllAndComputable = 3
    """Read all the attributes, also the computed ones"""
    ReadWithoutGeometry = 0
    """Read all non-geometrical attributes"""

    names = {ReadWithoutGeometry: ReadWithoutGeometry,
             ReadAll: ReadAll,
             DoNotRead: DoNotRead,
             ReadAllAndComputable: ReadAllAndComputable}

    values = {0: ReadWithoutGeometry,
              1: ReadAll,
              2: DoNotRead,
              3: ReadAllAndComputable}

    def __getitem__(self, key: (str | int | float)) -> eAttibuteReadState:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class eDesignPathLocation(enum.Enum):
    """Location of the design path
    """
    AskForLocation = 0
    CreateSubPath = 2
    OverrideFiles = 1

    names = {AskForLocation: AskForLocation,
             OverrideFiles: OverrideFiles,
             CreateSubPath: CreateSubPath}

    values = {0: AskForLocation,
              1: OverrideFiles,
              2: CreateSubPath}

    def __getitem__(self, key: (str | int | float)) -> eDesignPathLocation:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


def ClearElementPreview():
    """Clear the element preview
    """
def CloseElementPreview():
    """Close the element preview
    """
def CopyElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                 elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, fromPoint: NemAll_Python_Geometry.Point3D, distanceVector: NemAll_Python_Geometry.Vector3D, rotationVector: NemAll_Python_Geometry.Vector3D, rotationAngle: float, numberOfCopies: int, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
    """Copy the elements

    Returns:
           List with the copied elements

    Args:
        doc:            Document
        elements:       List with the elements
        fromPoint:      From point
        distanceVector: Distance vector
        rotationVector: Rotation vector
        rotationAngle:  Rotation angle in radian
        numberOfCopies: Number for copies
        viewProj:       View world projection
    """
def CopyElementsToDrawingFile(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                              elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, targetDrawingFiletNr: int, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection):
    """Copy the elements to document

    Args:
        doc:            Document
        elements:       List with the elements
        int:            Target document number
        viewProj:       View world projection
    """
def CreateAssociativeViews(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, insertionMat: NemAll_Python_Geometry.Matrix3D,
                           elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, assoViewList: list, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection) -> NemAll_Python_Geometry.MinMax2DList:
    """Create associative views

    Args:
        doc:             Document
        insertionMat:    Placment matrix
        elements:        List with the elements
        assoViewList:    List with the associative views
        viewProj:        View world projection
    """
def CreateBarCoupler(arg2: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, arg3: str, arg4: str, arg5: str, arg6: str,
                     arg7: bool):
    """
    """
def CreateElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, insertionMat: NemAll_Python_Geometry.Matrix3D,
                   modelEleList: list, modelUuidList: list, assoRefObj: object, appendReinfPosNr: bool = True, createUndoStep: bool = True) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
    """Create the elements in the drawing file

    Args:
        doc:                Document
        insertionMat:       Matrix with the placement point and the rotation
        modelEleList:       List with the model elements           modelUuidList      List with the model UUIDS in modification mode
        assoRefObj:         reference to an associative view
        appendReinfPosNr:   Set to True to append the reinforcement position numbers to the existing position numbers.
                            Set to False to try to use the original reinforcement position numbers
        createUndoStep:     Create an undo step after the creation of the PythonPart

    Returns:
        List with the created elements
    """
def CreateLayer(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, groupName: str, subGroupName: str, longName: str, shortName: str,
                lineColorID: int, lineThicknessID: int, lineStyleID: int, bVisible: bool, bModifiable: bool) -> int:
    """Create a new layer

    Args:
        doc:                Document
        groupName:          Group name
        subGroupName:       Subgroup name
        lineColorID:        Line color ID of the layer
        lineThicknessID:    Line thickness ID of the layer
        lineStyleID:        Line style ID of the layer
        bVisible:           Layer is visible
        bModifiable:        Layer is modifiable

    Returns:
        Created layer number
    """
def CreateLibraryElement(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, insertionMat: NemAll_Python_Geometry.Matrix3D,
                         path: str, elementName: str) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
    """Create a library element in the data base

    Returns:
           List with the created elements

    Args:
        doc:            Document
        insertionMat:   Matrix with the placement point and the rotation
        path:           Path of the library element
        elementName:    Name of the library element
    """
def CreateSectionsAndViews(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, insertionMat: NemAll_Python_Geometry.Matrix3D,
                           elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, sectionViewList: list, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection, undoRedoService: (object | None) = None) -> NemAll_Python_Geometry.MinMax2DList:
    """Create a unified section or view

    Args:
        doc:              Document
        insertionMat:     Placement matrix
        elements:         List with the elements
        sectionViewList:  List with the sections and views
        viewProj:         View world projection
        undoRedoService:  Undo redo service

    Returns:
        list of boundaries of the created views and sections 
    """
def DeleteElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                   elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList):
    """Delete the elements

    Args:
        doc:            Document
        elements:       List with the elements
    """
def DrawElementPreview(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, insertionMat: NemAll_Python_Geometry.Matrix3D,
                       modelEleList: list, bDirectDraw: int, assoRefObj: object, asStaticPreview: bool = False, addToPreviewBoundingBox: bool = True):
    """Draw the preview of the elements

    Args:
        doc:                         Document
        insertionMat:                Matrix with the placement point and the rotation
        modelEleList:                List with the model elements
        bDirectDraw:                 Direct draw of the preview elements to the screen
        assoRefObj:                  Associative view reference object
        asStaticPreview:             Draw as static preview: true/false
        addToPreviewBoundingBox:     Add the elements to the bounding box of the preview
    """
@typing.overload
def ElementTransform(transMat: NemAll_Python_Geometry.Matrix3D, modelEleList: list):
    """Transform the model elements

    Args:
        transMat:       Transformation matrix
        modelEleList:   List with the model elements
    """
@typing.overload
def ElementTransform(transVec: NemAll_Python_Geometry.Vector3D, xAngle: float, yAngle: float, zAngle: float, modelEleList: list):
    """Transform the model elements

    Args:
        transVec:       Transformation vector
        xAngle:         Rotation angle around the x-axis
        yAngle:         Rotation angle around the y-axis
        zAngle:         Rotation angle around the z-axis
        modelEleList:   List with the model elements
    """
def ElementTransform(self):
    """ Overloaded function. See individual overloads.
    """
def ExecutePreviewDraw(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
    """Trigger the draw of the preview in the viewport

    Args:
      doc:  document
    """
def ExplodeIFCSmartSymbols(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                           elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
    """Explode smart symbols with an existing IFC ID oder IFC object type

    Returns:
           List with the exploded elements

    Args:
        doc:        Document
        elements:   Elements to explode
    """
def ExplodeSmartSymbols(elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
    """Explode the smart symbols

    Returns:
           List with the exploded elements

    Args:
        elements:               Elements to explode
    """
def GetColorById(id: int) -> NemAll_Python_BasisElements.ARGB:
    """Get the ARGB color by the color ID

    Args:
        id: color ID

    Returns:
         ARGB color
    """
def GetElement(element: NemAll_Python_IFW_ElementAdapter.BaseElementAdapter) -> object:
    """Get the PythonParts element

    Returns:
           PythonParts element

    Args:
        element:   Element as BaseElementAdapter
    """
def GetElements(elementsList: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList) -> list:
    """Get Python objects out of element adapters

    Args:
        elementsList:    List of element adapters

    Returns:
        List of python objects
    """
def GetIdByColor(color: NemAll_Python_BasisElements.ARGB) -> int:
    """Get the color ID by the ARGB color

    Args:
        color: ARGB color

    Returns:
         color ID
    """
def GetMinMaxBox(elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, axisAngle: float = 0.0,
                 only3DElements: bool = False) -> NemAll_Python_Geometry.MinMax3D:
    """Get the min/max box of the elements

    Args:
        elements:        List with the elements
        axisAngle:       Angle of the x axis for the min/max calculation
        only3DElements:  Use only 3D elements

    Returns:
        Min/max box of the elements
    """
def GetViewMatrices(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter):
    """Get the associative view matrices

    Returns:
           Associative view matrices

    Args:
        doc:    Document
    """
def ModifyElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, modelEleList: list):
    """Modify the elements

    Args:
        doc:            Document
        modelEleList:   Elements
    """
def ModifyElementsWithSaveAndRestoreSelection(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter, modelEleList: list):
    """ModifyElementsWithSaveAndRestoreSelection

    Args:
        doc:            Document
        modelEleList:   Elements
    """
def MoveElementsToDrawingFile(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                              elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, targetDrawingFiletNr: int, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection):
    """Copy the elements to document

    Args:
        doc:            Document
        elements:       List with the elements
        int:            Target document number
        viewProj:       View world projection
    """
def RotateElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                   elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, refPnt: NemAll_Python_Geometry.Point2D, rotAngle: float, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection):
    """Rotate the elements

    Args:
        doc:            Document
        elements:       List with the elements
        refPnt:         Reference point of the rotation
        rotAngle:       Rotation angle
        viewProj:       View world projection
    """
def ScaleElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                  elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, refPnt: NemAll_Python_Geometry.Point3D, scaleX: float, scaleY: float, scaleZ: float, theta: NemAll_Python_Geometry.Angle, viewProj: NemAll_Python_IFW_Input.ViewWorldProjection):
    """Scale the elements

    Args:
        doc:            Document
        elements:       List with the elements
        refPnt:         Reference point of the scaling
        scaleX:         Scale factor in x direction
        scaleY:         Scale factor in y direction
        scaleX:         Scale factor in x direction
        theta:          Rotation angle in Z-axis
        viewProj:       View world projection
    """
def ShowElements(doc: NemAll_Python_IFW_ElementAdapter.DocumentAdapter,
                 elements: NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList, show: bool):
    """Hide the elements

    Args:
        doc:            Document
        elements:       List with the elements
        show:           Show state
    """
ATTRNR_HASH = 607
ATTRNR_PYTHONPART_CHECK = 539
ATTRNR_PYTHONPART_DISPLAY_NAME = 18229
ATTRNR_PYTHONPART_MATRIX = 1034
ATTRNR_PYTHONPART_OBJECT = 538
ATTRNR_PYTHONPART_PATH = 611
ATTRNR_PYTHONPART_UUID = 18228
ATTRNR_SUB_PYTHONPART_KEY = 18230
ATTRNR_UUID = 606
ATTRNR_VOLUME = 223

```