---
title: "TextProperties"
source: "PythonPartsFramework\ParameterIncludes\TextProperties.incl"
type: "include"
category: "02_API_Referenz"
tags:
  - parameter
related:
  -
last_updated: "2026-02-20"
---


# TextProperties

> **Pfad:** `PythonPartsFramework\ParameterIncludes\TextProperties.incl`  
> **Typ:** `include`  
> **Tags:** `parameter`

## Inhalt

```text
<?xml version='1.0' encoding='UTF-8'?>
<Include xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPartInclude.xsd">
  <Parameter>
    <Name>TextFrameExp</Name>
    <Text>Frame</Text>
    <TextId>e_TEXT_FRAME</TextId>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>HasTextFrame</Name>
        <Text>Border around paragraph text</Text>
        <TextId>e_HAS_TEXT_FRAME</TextId>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
      </Parameter>
      <Parameter>
        <Name>FrameColor</Name>
        <Text>Color for border</Text>
        <TextId>e_FRAME_COLOR</TextId>
        <Value>1</Value>
        <ValueType>Color</ValueType>
        <Visible>HasTextFrame$ == True</Visible>
      </Parameter>
      <Parameter>
        <Name>FramePen</Name>
        <Text>Pen thickness for border</Text>
        <TextId>e_FRAME_PEN</TextId>
        <Value>1</Value>
        <ValueType>Pen</ValueType>
        <Visible>HasTextFrame$ == True</Visible>
      </Parameter>
      <Parameter>
        <Name>FrameStroke</Name>
        <Text>Line type for border</Text>
        <TextId>e_FRAME_STROKE</TextId>
        <Value>1</Value>
        <ValueType>Stroke</ValueType>
        <Visible>HasTextFrame$ == True</Visible>
      </Parameter>
    </Parameters>
  </Parameter>
  <Parameter>
    <Name>TextPropExp</Name>
    <Text>Text properties</Text>
    <TextId>e_TEXT_PROP</TextId>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>TextHeight</Name>
        <Text>Height</Text>
        <TextId>e_HEIGHT</TextId>
        <Value>4.</Value>
        <ValueType>Double</ValueType>
      </Parameter>
      <Parameter>
        <Name>TextWidth</Name>
        <Text>Width</Text>
        <TextId>e_WIDTH</TextId>
        <Value>4.</Value>
        <ValueType>Double</ValueType>
      </Parameter>
      <Parameter>
        <Name>Font</Name>
        <Text>Font</Text>
        <TextId>e_FONT</TextId>
        <Value>21</Value>
        <ValueType>Font</ValueType>
      </Parameter>
      <Parameter>
        <Name>FontStyles</Name>
        <Text>Emphasis</Text>
        <TextId>e_FONT_STYLES</TextId>
        <Value>0</Value>
        <ValueType>FontEmphasis</ValueType>
        <Constraint>Font$</Constraint>
      </Parameter>
      <Parameter>
        <Name>FontAngle</Name>
        <Text>Angle for italic text</Text>
        <TextId>e_FONT_ANGLE</TextId>
        <Value>90</Value>
        <ValueType>Angle</ValueType>
        <Enabled>False</Enabled>
        <Constraint>Font$;FontStyles$</Constraint>
      </Parameter>
      <Parameter>
        <Name>ColumnSlopeAngle</Name>
        <Text>Column angle</Text>
        <TextId>e_COLUMN_SLOPE_ANGLE</TextId>
        <Value>90</Value>
        <ValueType>Angle</ValueType>
      </Parameter>
      <Parameter>
        <Name>TextAngle</Name>
        <Text>Text rotation angle</Text>
        <TextId>e_TEXT_ANGLE</TextId>
        <Value>0</Value>
        <ValueType>Angle</ValueType>
      </Parameter>
      <Parameter>
        <Name>RefPointButtonRow</Name>
        <Text>Reference point</Text>
        <ValueType>Row</ValueType>
        <Parameters>
          <Parameter>
            <Name>Alignment</Name>
            <Text>Alignment</Text>
            <TextId>e_ALIGNMENT</TextId>
            <Value>AllplanPalette.RefPointPosition.eCenterCenter</Value>
            <ValueType>RefPointButton</ValueType>
            <EnumList2>AllplanPalette.RefPointButtonType.eAllNinePositions</EnumList2>
          </Parameter>
        </Parameters>
      </Parameter>
    </Parameters>
  </Parameter>
  <Parameter>
    <Name>BackgroundExp</Name>
    <Text>Background</Text>
    <TextId>e_BACKGROUND</TextId>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>BackgroundFillOfViewport</Name>
        <Text>Background fill of viewport</Text>
        <TextId>e_BACKGROUND_FILL_OF_VIEWPORT</TextId>
        <Value>false</Value>
        <ValueType>CheckBox</ValueType>
        <Constraint>HasBackgroundColor$</Constraint>
      </Parameter>
      <Parameter>
        <Name>HasBackgroundColor</Name>
        <Text>Background color</Text>
        <TextId>e_HAS_BACKGROUND_COLOR</TextId>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
        <Constraint>BackgroundFillOfViewport$</Constraint>
      </Parameter>
      <Parameter>
        <Name>BackgroundColor</Name>
        <Text>Color</Text>
        <TextId>e_BACKGROUND_COLOR</TextId>
        <Value>255</Value>
        <ValueType>Integer</ValueType>
        <ValueDialog>RGBColorDialog</ValueDialog>
        <Visible>HasBackgroundColor$ == True</Visible>
      </Parameter>
    </Parameters>
  </Parameter>
  <Parameter>
    <Name>LayoutExp</Name>
    <Text>Layout</Text>
    <TextId>e_LAYOUT</TextId>
    <ValueType>Expander</ValueType>
    <Parameters>
      <Parameter>
        <Name>LineFeed</Name>
        <Text>Line feed</Text>
        <TextId>e_LINE_FEED</TextId>
        <Value>2.</Value>
        <ValueType>Double</ValueType>
      </Parameter>
      <Parameter>
        <Name>WrappedText</Name>
        <Text>Text wrapping</Text>
        <TextId>e_WRAPPED_TEXT</TextId>
        <Value>False</Value>
        <ValueType>CheckBox</ValueType>
      </Parameter>
      <Parameter>
        <Name>IsScaleDependent</Name>
        <Text>Scale dependent</Text>
        <TextId>e_IS_SCALE_DEPENDENT</TextId>
        <Value>True</Value>
        <ValueType>CheckBox</ValueType>
      </Parameter>
    </Parameters>
  </Parameter>
</Include>

```