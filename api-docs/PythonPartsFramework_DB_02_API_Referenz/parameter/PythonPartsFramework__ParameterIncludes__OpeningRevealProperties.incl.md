---
title: "OpeningRevealProperties"
source: "PythonPartsFramework\ParameterIncludes\OpeningRevealProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# OpeningRevealProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\OpeningRevealProperties.incl`  
> **Typ:** `include`  
> **Tags:** `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>RevealExp</Name>
    <Text>Reveal</Text>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>Reveal</Name>
        <Text>Type of reveal</Text>
        <Value>AllplanArchEle.VerticalOpeningRevealType.eNone</Value>
        <EnumList>AllplanArchEle.VerticalOpeningRevealType.eNone|
                      AllplanArchEle.VerticalOpeningRevealType.eEmbedded|
                      AllplanArchEle.VerticalOpeningRevealType.eInterior|
                      AllplanArchEle.VerticalOpeningRevealType.eExterior</EnumList>
        <ValueTextIdList>AllplanSettings.TextResRevealType.eNone|
                             AllplanSettings.TextResRevealType.eEmbedded|
                             AllplanSettings.TextResRevealType.eInterior|
                             AllplanSettings.TextResRevealType.eExterior</ValueTextIdList>
        <EnumList2>AllplanSettings.PictResRevealType.eNone|
                       AllplanSettings.PictResRevealType.eEmbedded|
                       AllplanSettings.PictResRevealType.eInterior|
                       AllplanSettings.PictResRevealType.eExterior</EnumList2>
        <ValueType>PictureResourceButtonList</ValueType>
      </Parameter>
      <Parameter>
        <Name>Depth</Name>
        <Text>Depth</Text>
        <Value/>
        <ValueType>Length</ValueType>
        <Visible>Reveal != AllplanArchEle.VerticalOpeningRevealType.eNone</Visible>
        <MinValue>0</MinValue>
      </Parameter>
      <Parameter>
        <Name>OuterOffset</Name>
        <Text>Outer offset</Text>
        <Value/>
        <ValueType>Length</ValueType>
        <Visible>Reveal == AllplanArchEle.VerticalOpeningRevealType.eEmbedded</Visible>
        <MinValue>-Depth</MinValue>
        <MaxValue>ElementThickness</MaxValue>
        <Constraint>ElementThickness - InnerOffset</Constraint>
      </Parameter>
      <Parameter>
        <Name>InnerOffset</Name>
        <Text>Inner offset</Text>
        <Value/>
        <ValueType>Length</ValueType>
        <Visible>Reveal == AllplanArchEle.VerticalOpeningRevealType.eEmbedded</Visible>
        <Constraint>ElementThickness - OuterOffset</Constraint>
      </Parameter>
      <Parameter>
        <Name>SideOffset</Name>
        <Text>Projection</Text>
        <Value/>
        <ValueType>Length</ValueType>
        <Visible>Reveal in {AllplanArchEle.VerticalOpeningRevealType.eInterior, AllplanArchEle.VerticalOpeningRevealType.eExterior}</Visible>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```