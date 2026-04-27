---
title: "VerticalOpeningGeometryProperties"
source: "PythonPartsFramework\ParameterIncludes\VerticalOpeningGeometryProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - geometrie
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# VerticalOpeningGeometryProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\VerticalOpeningGeometryProperties.incl`  
> **Typ:** `include`  
> **Tags:** `geometrie`, `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>ProfileRow</Name>
    <Text>Select geometry</Text>
    <ValueType>Row</ValueType>
    <Visible>Shape == AllplanArchEle.VerticalOpeningShapeType.eArbitrary</Visible>
    <Parameters>
      <Parameter>
        <Name>Profile</Name>
        <Text>Selection</Text>
        <Value/>
        <ValueType>String</ValueType>
        <ValueDialog>SymbolDialog</ValueDialog>
      </Parameter>
    </Parameters>
  </Parameter>
  <Parameter>
    <Name>Width</Name>
    <Text>Opening width</Text>
    <Value>1010</Value>
    <ValueType>Length</ValueType>
    <MinValue>10</MinValue>
    <Enable>Shape != AllplanArchEle.VerticalOpeningShapeType.eArbitrary</Enable>
  </Parameter>
  <Parameter>
    <Name>RiseAtTop</Name>
    <Text>Rise at top</Text>
    <Value>200</Value>
    <ValueType>Length</ValueType>
    <Visible>Shape in [AllplanArchEle.VerticalOpeningShapeType.eSemiDiamond,
                            AllplanArchEle.VerticalOpeningShapeType.eSemiCircle,
                            AllplanArchEle.VerticalOpeningShapeType.eRiseBottomTop]</Visible>
    <MinValue>0</MinValue>
    <MaxValue>HeightSettings.Height</MaxValue>
  </Parameter>
  <Parameter>
    <Name>SegmentsAtTop</Name>
    <Text>Segments at top</Text>
    <Value>30</Value>
    <ValueType>Integer</ValueType>
    <Visible>Shape == AllplanArchEle.VerticalOpeningShapeType.eRiseBottomTop</Visible>
    <MinValue>1</MinValue>
  </Parameter>
  <Parameter>
    <Name>HeightToRise</Name>
    <Text>Height to rise</Text>
    <Value/>
    <ValueType>Length</ValueType>
    <Visible>Shape in [AllplanArchEle.VerticalOpeningShapeType.eSemiDiamond,
                           AllplanArchEle.VerticalOpeningShapeType.eSemiCircle,
                           AllplanArchEle.VerticalOpeningShapeType.eRiseBottomTop]</Visible>
    <MinValue>0</MinValue>
    <Constraint>HeightSettings.Height - (RiseAtTop if Shape != AllplanArchEle.VerticalOpeningShapeType.eRiseBottomTop else RiseAtBottom + RiseAtTop)</Constraint>
    <Persistent>NO</Persistent>
  </Parameter>
  <Parameter>
    <Name>RiseAtBottom</Name>
    <Text>Rise at bottom</Text>
    <Value>200</Value>
    <ValueType>Length</ValueType>
    <Visible>Shape == AllplanArchEle.VerticalOpeningShapeType.eRiseBottomTop</Visible>
    <MinValue>0</MinValue>
    <MaxValue>HeightSettings.Height</MaxValue>
  </Parameter>
  <Parameter>
    <Name>SegmentsAtBottom</Name>
    <Text>Segments at bottom</Text>
    <Value>30</Value>
    <ValueType>Integer</ValueType>
    <Visible>Shape == AllplanArchEle.VerticalOpeningShapeType.eRiseBottomTop</Visible>
    <MinValue>1</MinValue>
  </Parameter>
</Include>

```