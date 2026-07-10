# Layout Controls

These parameter types organize the palette visually. They do not produce a value accessible in the script.

## Expander

Groups controls under a collapsible heading. Supports up to **3 levels** of nesting. The child `<Parameters>` block holds the enclosed controls.

```xml
<Parameter>
    <Name>GeometryExpander</Name>
    <Text>Geometry</Text>
    <Value>False</Value>    <!-- True = starts collapsed -->
    <ValueType>Expander</ValueType>
    <Parameters>
        <Parameter>
            <Name>Width</Name>
            <Text>Width</Text>
            <Value>1000</Value>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Height</Name>
            <Text>Height</Text>
            <Value>500</Value>
            <ValueType>Length</ValueType>
        </Parameter>
    </Parameters>
</Parameter>
```

> If no child parameters are visible, the entire expander is hidden automatically.

---

## Separator

Draws a horizontal dividing line between controls:

```xml
<Parameter>
    <Name>Sep1</Name>
    <ValueType>Separator</ValueType>
</Parameter>
```

---

## Row

By default, each parameter is displayed in its own row. Wrapping parameters inside a `Row` displays the label text of the `Row` parameter on the left, and controls of all child parameters in a single horizontal row on the right. The `<Parameters>` block holds the child parameters. Their labels are not displayed.

```xml
<Parameter>
    <Name>DimensionsRow</Name>
    <Text>Dimensions</Text>
    <ValueType>Row</ValueType>
    <Parameters>
        <Parameter>
            <Name>Width</Name>
            <Text>W</Text>
            <Value>1000</Value>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Height</Name>
            <Text>H</Text>
            <Value>500</Value>
            <ValueType>Length</ValueType>
        </Parameter>
    </Parameters>
</Parameter>
```

Wrapping parameters inside a `Row` is also the **required container** for [buttons](button-control.md).

### Control width

By default all controls in a row share equal width. Override with `<WidthInRow>` (default weight = 30). A value of 60 makes the control twice as wide:

```xml
<Parameter>
    <Name>LargeControl</Name>
    ...
    <WidthInRow>60</WidthInRow>
</Parameter>
```

### Full palette width (OVERALL)

Set `<Value>OVERALL</Value>` on the Row to span controls across the full palette width, bypassing the label/value column split. The label text of the `Row` is not shown.

```xml
<Parameter>
    <Name>FullRow</Name>
    <Text>Label</Text>
    <Value>OVERALL</Value>
    <ValueType>Row</ValueType>
    <Parameters>
        ...
    </Parameters>
</Parameter>
```

### Control on the left side (OVERALL:N)

Set `<Value>OVERALL:N</Value>` to place the first N controls on the label (left) side. Useful for a checkbox that enables the control next to it:

```xml
<Parameter>
    <Name>NameRow</Name>
    <Text>Name</Text>
    <ValueType>Row</ValueType>
    <Value>OVERALL:1</Value>   <!-- first control goes on the left -->
    <Parameters>
        <Parameter>
            <Name>NameEnabled</Name>
            <Text></Text>
            <Value>False</Value>
            <ValueType>CheckBox</ValueType>
        </Parameter>
        <Parameter>
            <Name>NameValue</Name>
            <Text></Text>
            <Value></Value>
            <ValueType>String</ValueType>
            <Enable>NameEnabled</Enable>
        </Parameter>
    </Parameters>
</Parameter>
```

---

## Picture

Embeds a static image in the palette. Does not produce a parameter value.

```xml
<!-- Your own image — path relative to the PYP file -->
<Parameter>
    <Name>Preview</Name>
    <Value>preview.png</Value>
    <Orientation>Middle</Orientation>   <!-- Left | Middle | Right -->
    <ValueType>Picture</ValueType>
</Parameter>
```
