---
name: property-palette
description: >
  Use this skill to design and build the property palette for a PythonPart.
  The palette is defined in the PYP file and is the primary UI the user interacts with
  to input parameters that drive the PythonPart's output.
---

# Skill: Property Palette

## Introduction

The **property palette** is the primary UI of a PythonPart. It has a fixed two-column layout:
the **label** on the left, the **input control** on the right. There is no free-form layout — the
framework constructs the palette automatically from the parameter definitions in the PYP file.

The core idea is that a **parameter** and a **UI control** are the same thing: you declare a
`<Parameter>` block, and the framework picks the right control based on `<ValueType>`. You never
write UI code.

---

## File structure

The property palette is defined inside the **PYP file** — an XML document. A minimal PYP file
with one palette page looks like this (see also `templates/MyPythonPart.pyp`):

```xml
<?xml version="1.0" encoding="utf-8"?>
<Element
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/{ALLPLAN_VERSION}/schemas/PythonPart.xsd">

    <Script>
        <Name>MyPythonParts\MyPythonPart.py</Name>
        <Title>My PythonPart</Title>
        <Version>1.0</Version>
    </Script>

    <Page>
        <Name>Page1</Name>
        <Text>Parameters</Text>
        <Parameters>

            <Parameter>
                <Name>Width</Name>
                <Text>Width</Text>
                <Value>1000</Value>
                <ValueType>Length</ValueType>
            </Parameter>

        </Parameters>
    </Page>

</Element>
```

### Key rules

- The root tag is `<Element>`. Always include the `xsi:noNamespaceSchemaLocation` attribute — it enables XML validation and autocompletion.
- Replace `{ALLPLAN_VERSION}` in the schema URL with the actual version, e.g. `2026`.
- `<Script>/<Name>` is the path to the `.py` file **relative to the `PythonPartsScripts\` directory**.
- `<Version>` must be a value convertible to `float` (e.g. `"1.0"`).
- The complete list of all supported tags and their descriptions is in the XSD schema at:  
  `https://pythonparts.allplan.com/{ALLPLAN_VERSION}/schemas/PythonPart.xsd`  
  Refer to it when in doubt about an optional tag.

### Pages

Parameters are grouped into `<Page>` nodes. Each page becomes a **tab** in the palette.

```xml
<Page>
    <Name>Page1</Name>      <!-- used to identify the page in the script -->
    <Text>Geometry</Text>   <!-- label shown on the tab -->
    <Parameters>
        ...
    </Parameters>
</Page>
```

| Tag | Required | Description |
|-----|----------|-------------|
| `<Name>` | yes | Internal identifier. Referenced in the script to handle page-switch events. |
| `<Text>` | yes | Label shown on the tab. |
| `<Visible>` | no | Condition expression to show/hide the entire page. |
| `<Enable>` | no | Condition expression to enable/disable all controls on the page. |

If only one page is defined, no tab control is shown — the parameters fill the palette directly.

#### Hidden page

Use the reserved name `__HiddenPage__` for a page that is invisible to the user but whose
parameters are accessible in the script (useful for persisting internal state):

```xml
<Page>
    <Name>__HiddenPage__</Name>
    <Text></Text>
    <Parameters>
        <Parameter>
            <Name>InternalState</Name>
            <Text></Text>
            <Value>0</Value>
            <ValueType>Integer</ValueType>
        </Parameter>
    </Parameters>
</Page>
```

---

## Parameters

Each `<Parameter>` block defines one input control. The minimum required tags are:

```xml
<Parameter>
    <Name>MyParameter</Name>   <!-- PascalCase, no spaces; becomes build_ele.MyParameter -->
    <Text>My parameter</Text>  <!-- label shown in the palette -->
    <Value>123</Value>         <!-- default value -->
    <ValueType>Integer</ValueType>
</Parameter>
```

The order of `<Parameter>` blocks inside `<Parameters>` determines the order of controls
in the palette top-to-bottom.

### Accessing a parameter in the script

For each parameter declared in the PYP file, the framework creates a `ParameterProperty`
attribute on the `BuildingElement` object with the same name as `<Name>`. Read its value with:

```python
width = self.build_ele.Width.value
```

Setting it is equally simple:

```python
self.build_ele.Width.value = 500.0
```

---

## Parameter types reference

| `<ValueType>` | Python type (`.value`) | Palette control | Notes |
|---------------|------------------------|-----------------|-------|
| `Length` | `float` | length input + unit selector | value in mm internally |
| `Integer` | `int` | integer input | |
| `Double` | `float` | decimal input | |
| `String` | `str` | text input | |
| `Checkbox` | `bool` | checkbox | |
| `Angle` | `float` | angle input + unit selector | value in radians internally |
| `StringComboBox` | `str` | dropdown | requires `<ValueList>` |
| `IntegerComboBox` | `int` | dropdown | requires `<ValueList>` |
| `Point3D` | `AllplanGeometry.Point3D` | three coordinate inputs | |
| `Color` | `int` | color picker | |

### Combo box — required extra tags

Both `StringComboBox` and `IntegerComboBox` need `<ValueList>` (stored values, pipe-separated)
and optionally `<ValueTextList>` (display labels):

```xml
<Parameter>
    <Name>Shape</Name>
    <Text>Shape</Text>
    <Value>rect</Value>
    <ValueType>StringComboBox</ValueType>
    <ValueList>rect|circle|triangle</ValueList>
    <ValueTextList>Rectangle|Circle|Triangle</ValueTextList>
</Parameter>
```

For `IntegerComboBox` the `<Value>` and entries in `<ValueList>` must be integers:

```xml
<Parameter>
    <Name>Segments</Name>
    <Text>Segments</Text>
    <Value>4</Value>
    <ValueType>IntegerComboBox</ValueType>
    <ValueList>3|4|6|8</ValueList>
    <ValueTextList>Triangle|Square|Hexagon|Octagon</ValueTextList>
</Parameter>
```


