---
title: "ShapeGeometryProperties"
source: "PythonPartsFramework\ParameterIncludes\ShapeGeometryProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - geometrie
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# ShapeGeometryProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\ShapeGeometryProperties.incl`  
> **Typ:** `include`  
> **Tags:** `geometrie`, `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>GeometryExp</Name>
    <Text>Geometry</Text>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>Shape</Name>
        <Text>Shape</Text>
        <Value>AllplanArchEle.ShapeType.eRectangular</Value>
        <EnumList>AllplanArchEle.ShapeType.eRectangular|
                      AllplanArchEle.ShapeType.eCircular|
                      AllplanArchEle.ShapeType.eRegularPolygonCircumscribed|
                      AllplanArchEle.ShapeType.eRegularPolygonInscribed|
                      AllplanArchEle.ShapeType.ePolygonal|
                      AllplanArchEle.ShapeType.eArbitrary</EnumList>
        <ValueTextIdList>AllplanSettings.TextResShapeType.eRectangle|
                             AllplanSettings.TextResShapeType.eCircle|
                             AllplanSettings.TextResShapeType.eRegularPolygonCircumscribed|
                             AllplanSettings.TextResShapeType.eRegularPolygonInscribed|
                             AllplanSettings.TextResShapeType.ePolygon|
                             AllplanSettings.TextResShapeType.eArbitrary</ValueTextIdList>
        <EnumList2>AllplanSettings.PictResShapeType.eRectangle|
                       AllplanSettings.PictResShapeType.eCircle|
                       AllplanSettings.PictResShapeType.eRegularPolygonCircumscribed|
                       AllplanSettings.PictResShapeType.eRegularPolygonInscribed|
                       AllplanSettings.PictResShapeType.ePolygon|
                       AllplanSettings.PictResShapeType.eArbitrary</EnumList2>
        <ValueType>PictureResourceButtonList</ValueType>
      </Parameter>
      <Parameter>
        <Visible>Shape == AllplanArchEle.ShapeType.eRectangular</Visible>
        <ValueType>ConditionGroup</ValueType>
        <Parameters>
          <Parameter>
            <Name>Width</Name>
            <Text>Width</Text>
            <Value>1000</Value>
            <ValueType>Length</ValueType>
            <MinValue>10</MinValue>
          </Parameter>
          <Parameter>
            <Name>Depth</Name>
            <Text>Depth</Text>
            <Value>1000</Value>
            <ValueType>Length</ValueType>
            <MinValue>10</MinValue>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <ValueType>ConditionGroup</ValueType>
        <Visible>Shape == AllplanArchEle.ShapeType.eCircular</Visible>
        <Parameters>
          <Parameter>
            <Name>Radius</Name>
            <Text>Radius</Text>
            <Value>500</Value>
            <ValueType>Length</ValueType>
          </Parameter>
          <Parameter>
            <Name>CircleDivision</Name>
            <Text>Segments in circle</Text>
            <Value>20</Value>
            <ValueType>Integer</ValueType>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <ValueType>ConditionGroup</ValueType>
        <Visible>Shape in (AllplanArchEle.ShapeType.eRegularPolygonInscribed,
                               AllplanArchEle.ShapeType.eRegularPolygonCircumscribed)</Visible>
        <Parameters>
          <Parameter>
            <Name>Radius</Name>
            <TextDyn>"Outside radius" if Shape == AllplanArchEle.ShapeType.eRegularPolygonCircumscribed else "Inside radius"</TextDyn>
            <Value>500</Value>
            <ValueType>Length</ValueType>
            <MinValue>10</MinValue>
          </Parameter>
          <Parameter>
            <Name>NumberOfCorners</Name>
            <Text>Number of corners (3-19)</Text>
            <Value>6</Value>
            <ValueType>Integer</ValueType>
            <MinValue>3</MinValue>
            <MaxValue>19</MaxValue>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <Name>ProfileRow</Name>
        <Text>Select geometry</Text>
        <ValueType>Row</ValueType>
        <Visible>Shape == AllplanArchEle.ShapeType.eArbitrary</Visible>
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
        <Name>PlacingAngle</Name>
        <Text>Placing angle</Text>
        <Value/>
        <ValueType>Angle</ValueType>
        <Visible>Shape in {AllplanArchEle.ShapeType.eRectangular,
                               AllplanArchEle.ShapeType.eRegularPolygonCircumscribed,
                               AllplanArchEle.ShapeType.eRegularPolygonInscribed}</Visible>
      </Parameter>
      <Parameter>
        <Name>RefPntIndex</Name>
        <Text>Reference point</Text>
        <Value>AllplanPalette.RefPointPosition.eBottomLeft</Value>
        <ValueType>RefPointButton</ValueType>
        <Visible>Shape != AllplanArchEle.ShapeType.ePolygonal</Visible>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```