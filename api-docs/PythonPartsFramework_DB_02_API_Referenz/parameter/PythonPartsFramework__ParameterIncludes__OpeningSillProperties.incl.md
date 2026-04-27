---
title: "OpeningSillProperties"
source: "PythonPartsFramework\ParameterIncludes\OpeningSillProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# OpeningSillProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\OpeningSillProperties.incl`  
> **Typ:** `include`  
> **Tags:** `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>SillExp</Name>
    <Text>Sill</Text>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>Sill</Name>
        <Text>Type of sill</Text>
        <Value>AllplanArchEle.VerticalOpeningSillType.eBothsides</Value>
        <EnumList>AllplanArchEle.VerticalOpeningSillType.eNone|
                      AllplanArchEle.VerticalOpeningSillType.eOuter|
                      AllplanArchEle.VerticalOpeningSillType.eInner|
                      AllplanArchEle.VerticalOpeningSillType.eBothsides</EnumList>
        <ValueTextIdList>AllplanSettings.TextResSillType.eNone|
                             AllplanSettings.TextResSillType.eOuter|
                             AllplanSettings.TextResSillType.eInner|
                             AllplanSettings.TextResSillType.eBothsides</ValueTextIdList>
        <EnumList2>AllplanSettings.PictResSillType.eNone|
                       AllplanSettings.PictResSillType.eOuter|
                       AllplanSettings.PictResSillType.eInner|
                       AllplanSettings.PictResSillType.eBothsides</EnumList2>
        <ValueType>PictureResourceButtonList</ValueType>
      </Parameter>
      <Parameter>
        <ValueType>ConditionGroup</ValueType>
        <Visible>Sill != AllplanArchEle.VerticalOpeningSillType.eNone</Visible>
        <Parameters>
          <Parameter>
            <Name>Layer</Name>
            <Text>Layer</Text>
            <Value/>
            <ValueType>Layer</ValueType>
          </Parameter>
          <Parameter>
            <Name>Pen</Name>
            <Text>Pen thickness</Text>
            <Value>1</Value>
            <ValueType>Pen</ValueType>
          </Parameter>
          <Parameter>
            <Name>Stroke</Name>
            <Text>Line type</Text>
            <Value>1</Value>
            <ValueType>Stroke</ValueType>
          </Parameter>
          <Parameter>
            <Name>Color</Name>
            <Text>Line color</Text>
            <Value>1</Value>
            <ValueType>Color</ValueType>
          </Parameter>
        </Parameters>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```