---
title: "OpeningTierOffsetProperties"
source: "PythonPartsFramework\ParameterIncludes\OpeningTierOffsetProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# OpeningTierOffsetProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\OpeningTierOffsetProperties.incl`  
> **Typ:** `include`  
> **Tags:** `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>TierOffsetExp</Name>
    <Text>Stop</Text>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>LayerOffsetTypeRow</Name>
        <Text>Type of stop</Text>
        <ValueType>Row</ValueType>
        <Parameters>
          <Parameter>
            <Name>LayerOffsetType</Name>
            <Text>None|Exterior side|Interior side|Advanced offset entry|With outer facing|With inner facing</Text>
            <Value>AllplanArchEle.VerticalOpeningTierOffsetType.eNone</Value>
            <EnumList>AllplanArchEle.VerticalOpeningTierOffsetType.eNone|
                            AllplanArchEle.VerticalOpeningTierOffsetType.eOuterSide|
                            AllplanArchEle.VerticalOpeningTierOffsetType.eInnerSide|
                            AllplanArchEle.VerticalOpeningTierOffsetType.eAdvanced|
                            AllplanArchEle.VerticalOpeningTierOffsetType.eWithOuterFacing|
                            AllplanArchEle.VerticalOpeningTierOffsetType.eWithInnerFacing</EnumList>
            <ValueTextIdList>AllplanSettings.TextResTierOffsetType.eNone|
                                AllplanSettings.TextResTierOffsetType.eOuterSide|
                                AllplanSettings.TextResTierOffsetType.eInnerSide|
                                AllplanSettings.TextResTierOffsetType.eAdvanced|
                                AllplanSettings.TextResTierOffsetType.eWithOuterFacing|
                                AllplanSettings.TextResTierOffsetType.eWithInnerFacing</ValueTextIdList>
            <EnumList2>AllplanSettings.PictResTierOffsetType.eNone|
                            AllplanSettings.PictResTierOffsetType.eOuterSide|
                            AllplanSettings.PictResTierOffsetType.eInnerSide|
                            AllplanSettings.PictResTierOffsetType.eAdvanced|
                            AllplanSettings.PictResTierOffsetType.eWithOuterFacing|
                            AllplanSettings.PictResTierOffsetType.eWithInnerFacing</EnumList2>
            <ValueType>PictureResourceButtonList</ValueType>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <ValueType>ConditionGroup</ValueType>
        <Visible>LayerOffsetType not in [AllplanArchEle.VerticalOpeningTierOffsetType.eNone, AllplanArchEle.VerticalOpeningTierOffsetType.eAdvanced]</Visible>
        <Parameters>
          <Parameter>
            <Name>LeftOffset</Name>
            <Text>Offset on the left</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
          </Parameter>
          <Parameter>
            <Name>RightOffset</Name>
            <Text>Offset on the right</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
          </Parameter>
          <Parameter>
            <Name>TopOffset</Name>
            <Text>Offset on the top</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <ValueType>ConditionGroup</ValueType>
        <Visible>LayerOffsetType in [AllplanArchEle.VerticalOpeningTierOffsetType.eWithOuterFacing, AllplanArchEle.VerticalOpeningTierOffsetType.eWithInnerFacing]</Visible>
        <Parameters>
          <Parameter>
            <Name>HasLeftFacing</Name>
            <Text>Facing on the left</Text>
            <Value>0</Value>
            <ValueType>CheckBox</ValueType>
          </Parameter>
          <Parameter>
            <Name>LeftWidth</Name>
            <Text>Width on the left</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
            <Visible>HasLeftFacing</Visible>
          </Parameter>
          <Parameter>
            <Name>LeftDepth</Name>
            <Text>Depth on the left</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
            <Visible>HasLeftFacing</Visible>
          </Parameter>
          <Parameter>
            <Name>HasRightFacing</Name>
            <Text>Facing on the right</Text>
            <Value>0</Value>
            <ValueType>CheckBox</ValueType>
          </Parameter>
          <Parameter>
            <Name>RightWidth</Name>
            <Text>Width on the right</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
            <Visible>HasRightFacing</Visible>
          </Parameter>
          <Parameter>
            <Name>RightDepth</Name>
            <Text>Depth on the right</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
            <Visible>HasRightFacing</Visible>
          </Parameter>
          <Parameter>
            <Name>HasTopFacing</Name>
            <Text>Facing on the top</Text>
            <Value>0</Value>
            <ValueType>CheckBox</ValueType>
          </Parameter>
          <Parameter>
            <Name>TopWidth</Name>
            <Text>Width on the top</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
            <Visible>HasTopFacing</Visible>
          </Parameter>
          <Parameter>
            <Name>TopDepth</Name>
            <Text>Depth on the top</Text>
            <Value>0</Value>
            <ValueType>Length</ValueType>
            <Visible>HasTopFacing</Visible>
          </Parameter>
          <Parameter>
            <Name>OpeningWidthDefinedBy</Name>
            <Text>Input side of opening width</Text>
            <Value>Interior side</Value>
            <ValueList>Interior side|Exterior side</ValueList>
            <ValueType>StringComboBox</ValueType>
          </Parameter>
        </Parameters>
      </Parameter>
      <Parameter>
        <ValueType>ConditionGroup</ValueType>
        <Visible>LayerOffsetType == AllplanArchEle.VerticalOpeningTierOffsetType.eAdvanced</Visible>
        <Parameters>
          <Parameter>
            <Name>TierIndexRow</Name>
            <Text>Layer</Text>
            <ValueType>Row</ValueType>
            <Value>OVERALL:1</Value>
            <Parameters>
              <Parameter>
                <Name>InfoPicture</Name>
                <Text>Enter the layer numer in the box. For example,
enter 1-4 or 1,3. Use the arrow keys to select the
previous or next layer.</Text>
                <TextId>1005</TextId>
                <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                <ValueType>Picture</ValueType>
              </Parameter>
              <Parameter>
                <Name>TierIndex</Name>
                <Text/>
                <Value>1</Value>
                <ValueType>MultiIndex</ValueType>
                <MinValue>1</MinValue>
                <MaxValue>ElementTierCount</MaxValue>
              </Parameter>
            </Parameters>
          </Parameter>
          <Parameter>
            <Name>LeftOffsets</Name>
            <Text>Offset on the left</Text>
            <Value>[0]</Value>
            <ValueType>Length</ValueType>
            <Dimensions>ElementTierCount</Dimensions>
            <ValueIndexName>TierIndex</ValueIndexName>
          </Parameter>
          <Parameter>
            <Name>RightOffsets</Name>
            <Text>Offset on the right</Text>
            <Value>[0]</Value>
            <ValueType>Length</ValueType>
            <Dimensions>ElementTierCount</Dimensions>
            <ValueIndexName>TierIndex</ValueIndexName>
          </Parameter>
          <Parameter>
            <Name>BottomOffsets</Name>
            <Text>Offset on the bottom</Text>
            <Value>[0]</Value>
            <ValueType>Length</ValueType>
            <Dimensions>ElementTierCount</Dimensions>
            <ValueIndexName>TierIndex</ValueIndexName>
          </Parameter>
          <Parameter>
            <Name>TopOffsets</Name>
            <Text>Offset on the top</Text>
            <Value>[0]</Value>
            <ValueType>Length</ValueType>
            <Dimensions>ElementTierCount</Dimensions>
            <ValueIndexName>TierIndex</ValueIndexName>
          </Parameter>
        </Parameters>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```