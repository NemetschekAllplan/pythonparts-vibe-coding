---
title: "TextPointerProperties"
source: "PythonPartsFramework\ParameterIncludes\Reinforcement\TextPointerProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - bewehrung
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# TextPointerProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\Reinforcement\TextPointerProperties.incl`  
> **Typ:** `include`  
> **Tags:** `bewehrung`, `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>LabelPositionDefinition</Name>
    <Text>Define label position by</Text>
    <Value>2</Value>
    <ValueType>RadioButtonGroup</ValueType>
    <Parameters>
      <Parameter>
        <Name>LabelPositionByPoint</Name>
        <Text>point</Text>
        <Value>1</Value>
        <ValueType>RadioButton</ValueType>
      </Parameter>
      <Parameter>
        <Name>LabelPositionByOffset</Name>
        <Text>shape side and offset</Text>
        <Value>2</Value>
        <ValueType>RadioButton</ValueType>
      </Parameter>
    </Parameters>
  </Parameter>
  <Parameter>
    <Name>Separator</Name>
    <ValueType>Separator</ValueType>
  </Parameter>
  <Parameter>
    <Name>LabelPoint</Name>
    <Text>Label point</Text>
    <Value>Point2D(-200, 500)</Value>
    <XYZinRow>True</XYZinRow>
    <ValueType>Point2D</ValueType>
    <Visible>LabelPositionDefinition$ == 1</Visible>
  </Parameter>
  <Parameter>
    <Name>ShapeSide</Name>
    <Text>Shape side</Text>
    <Value>1</Value>
    <MinValue>1</MinValue>
    <MaxValue>6</MaxValue>
    <ValueType>Integer</ValueType>
    <Visible>LabelPositionDefinition$ == 2</Visible>
  </Parameter>
  <Parameter>
    <Name>ShapeSideFactor</Name>
    <Text>Shape side factor</Text>
    <Value>.3</Value>
    <MinValue>0</MinValue>
    <MaxValue>1</MaxValue>
    <ValueType>Double</ValueType>
    <Visible>LabelPositionDefinition$ == 2</Visible>
  </Parameter>
  <Parameter>
    <Name>LabelOffset</Name>
    <Text>Label offset</Text>
    <Value>Vector2D(-200, 0)</Value>
    <XYZinRow>True</XYZinRow>
    <ValueType>Vector2D</ValueType>
    <Visible>LabelPositionDefinition$ == 2</Visible>
  </Parameter>
  <Parameter>
    <Name>Angle</Name>
    <Text>Angle</Text>
    <Value>0</Value>
    <ValueType>Angle</ValueType>
  </Parameter>
  <Parameter>
    <Name>Separator</Name>
    <ValueType>Separator</ValueType>
  </Parameter>
  <Parameter>
    <Name>ShowTextPointer</Name>
    <Text>Show text pointer</Text>
    <Value>True</Value>
    <ValueType>CheckBox</ValueType>
  </Parameter>
  <Parameter>
    <Name>ShowTextPointerEndSymbol</Name>
    <Text>Show text pointer end symbol</Text>
    <Value>True</Value>
    <ValueType>CheckBox</ValueType>
    <Visible>ShowTextPointer$</Visible>
  </Parameter>
  <Parameter>
    <Name>SetPointerStartPointRow</Name>
    <Text>Set pointer start point</Text>
    <ValueType>Row</ValueType>
    <Visible>ShowTextPointer$</Visible>
    <Parameters>
      <Parameter>
        <Name>SetPointerStartPoint</Name>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
      </Parameter>
      <Parameter>
        <Name>PointerStartPoint</Name>
        <Value>Point2D(0,300)</Value>
        <ValueType>Point2D</ValueType>
        <Visible>SetPointerStartPoint$</Visible>
      </Parameter>
    </Parameters>
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
</Include>

```