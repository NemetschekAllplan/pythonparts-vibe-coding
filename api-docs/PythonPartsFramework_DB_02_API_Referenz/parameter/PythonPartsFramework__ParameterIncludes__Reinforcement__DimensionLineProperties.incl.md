---
title: "DimensionLineProperties"
source: "PythonPartsFramework\ParameterIncludes\Reinforcement\DimensionLineProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - bewehrung
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# DimensionLineProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\Reinforcement\DimensionLineProperties.incl`  
> **Typ:** `include`  
> **Tags:** `bewehrung`, `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>ReinforcementDimensionPropertiesExpander</Name>
    <Text>Reinforcement dimension properties</Text>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>SetLabelOffset</Name>
        <Text>Set label offset</Text>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
      </Parameter>
      <Parameter>
        <Name>LabelOffset</Name>
        <Text>Label offset</Text>
        <Value>Vector2D(0, 200)</Value>
        <ValueType>Vector2D</ValueType>
        <Visible>SetLabelOffset$</Visible>
      </Parameter>
      <Parameter>
        <Name>SetVisibleBarsRow</Name>
        <Text>Set visible bars</Text>
        <ValueType>Row</ValueType>
        <Parameters>
          <Parameter>
            <Name>SetVisibleBars</Name>
            <Value>False</Value>
            <ValueType>CheckBox</ValueType>
          </Parameter>
          <Parameter>
            <Name>VisibleBars</Name>
            <Text>Visible bars</Text>
            <Value>1,0,-1</Value>
            <ValueType>String</ValueType>
            <Visible>SetVisibleBars$</Visible>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <Name>ShowAllBars</Name>
        <Text>Show all bars</Text>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
      </Parameter>
      <Parameter>
        <Name>ShowTextPointer</Name>
        <Text>Show text pointer</Text>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
      </Parameter>
      <Parameter>
        <Name>ShowTextPointerEndSymbol</Name>
        <Text>Show text pointer end symbol</Text>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
        <Visible>ShowTextPointer$</Visible>
      </Parameter>
      <Parameter>
        <Name>AdditionalTextRow</Name>
        <Text>Set additional text</Text>
        <ValueType>Row</ValueType>
        <Parameters>
          <Parameter>
            <Name>SetAdditionalText</Name>
            <Value>False</Value>
            <ValueType>CheckBox</ValueType>
          </Parameter>
          <Parameter>
            <Name>AdditionalText</Name>
            <Value/>
            <ValueType>String</ValueType>
            <Visible>SetAdditionalText$</Visible>
          </Parameter>
        </Parameters>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```