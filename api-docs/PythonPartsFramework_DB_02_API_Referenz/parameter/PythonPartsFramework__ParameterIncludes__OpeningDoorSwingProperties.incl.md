---
title: "OpeningDoorSwingProperties"
source: "PythonPartsFramework\ParameterIncludes\OpeningDoorSwingProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# OpeningDoorSwingProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\OpeningDoorSwingProperties.incl`  
> **Typ:** `include`  
> **Tags:** `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>DoorSwingExp</Name>
    <Text>Door swing</Text>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>DoorSwingSymbol</Name>
        <Text>Door swing symbol</Text>
        <Value>AllplanArchEle.DoorSwingType.eSingleSwingCircular</Value>
        <EnumList>AllplanArchEle.DoorSwingType.eNone|
                      AllplanArchEle.DoorSwingType.eSingleSwingCircular|
                      AllplanArchEle.DoorSwingType.eDoubleSwingCircular|
                      AllplanArchEle.DoorSwingType.ePendulumSingleSwingCircular|
                      AllplanArchEle.DoorSwingType.ePendulumDoubleSwingCircular|
                      AllplanArchEle.DoorSwingType.eSingleSwingLinear|
                      AllplanArchEle.DoorSwingType.eDoubleSwingLinear|
                      AllplanArchEle.DoorSwingType.ePendulumSingleSwingLinear|
                      AllplanArchEle.DoorSwingType.ePendulumDoubleSwingLinear|
                      AllplanArchEle.DoorSwingType.eOneSidedRevolving|
                      AllplanArchEle.DoorSwingType.eTwoSidedRevolving|
                      AllplanArchEle.DoorSwingType.eOneSidedDoubleRevolving|
                      AllplanArchEle.DoorSwingType.eTwoSidedDoubleRevolving|
                      AllplanArchEle.DoorSwingType.eLiftingSingleSwingCircular|
                      AllplanArchEle.DoorSwingType.eLiftingSingleSwingLinear|
                      AllplanArchEle.DoorSwingType.eOneSidedSwingOptional|
                      AllplanArchEle.DoorSwingType.eTwoSidedSwingOptional|
                      AllplanArchEle.DoorSwingType.eSlidingSingleSwing|
                      AllplanArchEle.DoorSwingType.eSlidingDoubleSwing|
                      AllplanArchEle.DoorSwingType.eLiftingSliding|
                      AllplanArchEle.DoorSwingType.eLifting|
                      AllplanArchEle.DoorSwingType.eDoubleOppositeSwingCircular|
                      AllplanArchEle.DoorSwingType.eDoubleOppositeSwingLinear|
                      AllplanArchEle.DoorSwingType.eFolding|
                      AllplanArchEle.DoorSwingType.eTwoSidedFolding|
                      AllplanArchEle.DoorSwingType.eRevolving|
                      AllplanArchEle.DoorSwingType.eSwing</EnumList>
        <ValueTextIdList>AllplanSettings.TextResDoorSwingType.eNone|
                             AllplanSettings.TextResDoorSwingType.eSingleSwingCircular|
                             AllplanSettings.TextResDoorSwingType.eDoubleSwingCircular|
                             AllplanSettings.TextResDoorSwingType.ePendulumSingleSwingCircular|
                             AllplanSettings.TextResDoorSwingType.ePendulumDoubleSwingCircular|
                             AllplanSettings.TextResDoorSwingType.eSingleSwingLinear|
                             AllplanSettings.TextResDoorSwingType.eDoubleSwingLinear|
                             AllplanSettings.TextResDoorSwingType.ePendulumSingleSwingLinear|
                             AllplanSettings.TextResDoorSwingType.ePendulumDoubleSwingLinear|
                             AllplanSettings.TextResDoorSwingType.eOneSidedRevolving|
                             AllplanSettings.TextResDoorSwingType.eTwoSidedRevolving|
                             AllplanSettings.TextResDoorSwingType.eOneSidedDoubleRevolving|
                             AllplanSettings.TextResDoorSwingType.eTwoSidedDoubleRevolving|
                             AllplanSettings.TextResDoorSwingType.eLiftingSingleSwingCircular|
                             AllplanSettings.TextResDoorSwingType.eLiftingSingleSwingLinear|
                             AllplanSettings.TextResDoorSwingType.eOneSidedSwingOptional|
                             AllplanSettings.TextResDoorSwingType.eTwoSidedSwingOptional|
                             AllplanSettings.TextResDoorSwingType.eSlidingSingleSwing|
                             AllplanSettings.TextResDoorSwingType.eSlidingDoubleSwing|
                             AllplanSettings.TextResDoorSwingType.eLiftingSliding|
                             AllplanSettings.TextResDoorSwingType.eLifting|
                             AllplanSettings.TextResDoorSwingType.eDoubleOppositeSwingCircular|
                             AllplanSettings.TextResDoorSwingType.eDoubleOppositeSwingLinear|
                             AllplanSettings.TextResDoorSwingType.eFolding|
                             AllplanSettings.TextResDoorSwingType.eTwoSidedFolding|
                             AllplanSettings.TextResDoorSwingType.eRevolving|
                             AllplanSettings.TextResDoorSwingType.eSwing</ValueTextIdList>
        <EnumList2>AllplanSettings.PictResDoorSwingType.eNone|
                       AllplanSettings.PictResDoorSwingType.eSingleSwingCircular|
                       AllplanSettings.PictResDoorSwingType.eDoubleSwingCircular|
                       AllplanSettings.PictResDoorSwingType.ePendulumSingleSwingCircular|
                       AllplanSettings.PictResDoorSwingType.ePendulumDoubleSwingCircular|
                       AllplanSettings.PictResDoorSwingType.eSingleSwingLinear|
                       AllplanSettings.PictResDoorSwingType.eDoubleSwingLinear|
                       AllplanSettings.PictResDoorSwingType.ePendulumSingleSwingLinear|
                       AllplanSettings.PictResDoorSwingType.ePendulumDoubleSwingLinear|
                       AllplanSettings.PictResDoorSwingType.eOneSidedRevolving|
                       AllplanSettings.PictResDoorSwingType.eTwoSidedRevolving|
                       AllplanSettings.PictResDoorSwingType.eOneSidedDoubleRevolving|
                       AllplanSettings.PictResDoorSwingType.eTwoSidedDoubleRevolving|
                       AllplanSettings.PictResDoorSwingType.eLiftingSingleSwingCircular|
                       AllplanSettings.PictResDoorSwingType.eLiftingSingleSwingLinear|
                       AllplanSettings.PictResDoorSwingType.eOneSidedSwingOptional|
                       AllplanSettings.PictResDoorSwingType.eTwoSidedSwingOptional|
                       AllplanSettings.PictResDoorSwingType.eSlidingSingleSwing|
                       AllplanSettings.PictResDoorSwingType.eSlidingDoubleSwing|
                       AllplanSettings.PictResDoorSwingType.eLiftingSliding|
                       AllplanSettings.PictResDoorSwingType.eLifting|
                       AllplanSettings.PictResDoorSwingType.eDoubleOppositeSwingCircular|
                       AllplanSettings.PictResDoorSwingType.eDoubleOppositeSwingLinear|
                       AllplanSettings.PictResDoorSwingType.eFolding|
                       AllplanSettings.PictResDoorSwingType.eTwoSidedFolding|
                       AllplanSettings.PictResDoorSwingType.eRevolving|
                       AllplanSettings.PictResDoorSwingType.eSwing</EnumList2>
        <ValueType>PictureResourceComboBox</ValueType>
      </Parameter>
      <Parameter>
        <Name>OpeningSymbolOffset</Name>
        <Text>Offset</Text>
        <Value>0</Value>
        <ValueType>Length</ValueType>
      </Parameter>
      <Parameter>
        <Name>OpeningSymbolAngle</Name>
        <Text>Angle</Text>
        <Value>45</Value>
        <ValueType>Angle</ValueType>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```