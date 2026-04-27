---
title: "OpeningSymbolsProperties"
source: "PythonPartsFramework\ParameterIncludes\OpeningSymbolsProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# OpeningSymbolsProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\OpeningSymbolsProperties.incl`  
> **Typ:** `include`  
> **Tags:** `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>OpeningObjectExp</Name>
    <Text>Opening object</Text>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>DynamicSymbolListIndexRow</Name>
        <Text>Symbol index</Text>
        <ValueType>Row</ValueType>
        <Value>OVERALL:1</Value>
        <Parameters>
          <Parameter>
            <Name>SmartSymbolInfoPictureSymbol</Name>
            <Text>Select the position you want to modify. You can
select several positions to remove or replace
existing symbols. The last available position
is always empty. Select it to add an additional
symbol.</Text>
            <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
            <ValueType>Picture</ValueType>
          </Parameter>
          <Parameter>
            <Name>SymbolIndex</Name>
            <Text/>
            <Value>1</Value>
            <ValueType>MultiIndex</ValueType>
            <MinValue>1</MinValue>
            <MaxValue>len(SmartSymbolGroup) + 1</MaxValue>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <Name>SmartSymbolGroup</Name>
        <Text>Select symbol</Text>
        <Value>[_]</Value>
        <ValueType>DynamicList(String)</ValueType>
        <ValueDialog>OpeningSymbolDialog</ValueDialog>
        <ValueIndexName>SymbolIndex</ValueIndexName>
      </Parameter>
      <Parameter>
        <Name>OpeningSymbolTierIndex</Name>
        <Text>Tier index</Text>
        <Value>1</Value>
        <ValueType>Integer</ValueType>
        <MinValue>1</MinValue>
        <MaxValue>ElementTierCount</MaxValue>
      </Parameter>
      <Parameter>
        <Name>OpeningSymbolRefPntIndex</Name>
        <Text>Reference point</Text>
        <Value>AllplanPalette.RefPointPosition.eBottomLeft</Value>
        <ValueType>RefPointButton</ValueType>
        <EnumList2>AllplanPalette.RefPointButtonType.eCorners</EnumList2>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```