---
name: ui-design
description: Use this skill to design and build the property palette (the PYP file) for a PythonPart. The palette is the primary UI the user interacts with to input parameters that drive the PythonPart's output.
---

# Skill: Property Palette

## Overview

The **property palette** is the standard UI framework of a PythonPart. It unifies two concepts: a **parameter** and a **UI control**. Declaring a `<Parameter>` block defines both — the framework picks the right input control based on `<ValueType>`.

The palette has a fixed two-column layout: the **label** on the left, the **input control** on the right. Each parameter occupies one row. There is no free-form layout — the framework constructs the palette automatically from the parameter definitions in the PYP file.

For the rare cases where the palette's capabilities are insufficient, a custom UI can be built using .NET/WPF assemblies loaded via `pythonnet` (delivered with ALLPLAN; see example **UsingClrInteractor**).

## PYP file structure

The palette is defined inside the **PYP file** — an XML document. A minimal PYP file with one palette page:

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

> **Always include `xsi:noNamespaceSchemaLocation`** in the `<Element>` tag. It enables XML validation and autocompletion in editors. Without it, typos in tag names will go undetected until runtime.

- Replace `{ALLPLAN_VERSION}` in the schema URL with the actual version, e.g. `2026`.
- `<Script>/<Name>` is the path to the `.py` file **relative to the `PythonPartsScripts\` directory**.
- `<Version>` must be a value convertible to `float` (e.g. `"1.0"`).
- Every `<Parameter>` `<Name>` must be PascalCase with no spaces — it becomes a Python attribute on `build_ele`.
- The full list of supported tags is in the XSD schema: `https://pythonparts.allplan.com/{ALLPLAN_VERSION}/schemas/PythonPart.xsd`

## Pages

Parameters are grouped into `<Page>` nodes. Each page becomes a **tab** in the palette. If only one page is defined, no tab is shown.

```xml
<Page>
    <Name>Page1</Name>
    <Text>Geometry</Text>
    <Parameters>
        ...
    </Parameters>
</Page>
```

| Tag | Required | Default | Description |
|-----|----------|---------|-------------|
| `<Name>` | yes | — | Internal identifier. Referenced in the script to handle page-switch events. |
| `<Text>` | yes | — | Label shown on the tab. |
| `<TextId>` | no | — | ID of a translated string resource to localise `<Text>`. |
| `<Visible>` | no | `True` | Condition to show/hide the entire page. |
| `<Enable>` | no | `True` | Condition to enable/disable all controls on the page. |

> If a page has no visible parameters, its tab is not shown at all.

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
    <Text>My parameter</Text>  <!-- label shown on the left -->
    <Value>123</Value>         <!-- default value -->
    <ValueType>Integer</ValueType>
</Parameter>
```

The order of `<Parameter>` blocks inside `<Parameters>` determines the display order top-to-bottom.

### Accessing a parameter in the script

```python
width = self.build_ele.Width.value      # read
self.build_ele.Width.value = 500.0      # write
```

### Showing and hiding individual parameters

Add `<Visible>` or `<Enable>` to any `<Parameter>`. The value is a Python expression evaluated against other parameter names:

```xml
<Parameter>
    <Name>Offset</Name>
    <Text>Offset</Text>
    <Value>100</Value>
    <ValueType>Length</ValueType>
    <Visible>UseOffset</Visible>    <!-- shown only when the UseOffset checkbox is True -->
    <Enable>UseOffset</Enable>
</Parameter>
```

For complex dynamic behavior — hiding groups of parameters, runtime text changes, script-controlled visibility — see [dynamic-palette.md](references/dynamic-palette.md).

## Parameter type reference

Choose a reference based on the kind of input the user needs:

| Category | Use when… | Reference |
|---|---|---|
| Input controls | User types a numeric, text, or date value | [input-controls.md](references/input-controls.md) |
| Selection controls | User picks from a list, checkbox, or radio button | [selection-controls.md](references/selection-controls.md) |
| Layout controls | Organizing or grouping controls visually | [layout-controls.md](references/layout-controls.md) |
| Button | User triggers an action | [button-control.md](references/button-control.md) |
| Geometry | User inputs a point, vector, line, arc, or other geometry | [geometry-controls.md](references/geometry-controls.md) |
| ALLPLAN resource controls | User picks pen, stroke, colour, layer, or format properties | [allplan-resource-controls.md](references/allplan-resource-controls.md) |
| Dialog controls | User selects via a pop-up picker (library, file, colour, …) | [dialog-controls.md](references/dialog-controls.md) |
| Attribute controls | Parameter value is bound to an ALLPLAN attribute | [attribute-controls.md](references/attribute-controls.md) |
| Collections | Parameter holds a list or tuple of values; fully dynamic palette | [collection-parameters.md](references/collection-parameters.md) |
| Reinforcement controls | Rebar-specific pickers (steel grade, bar diameter, …) | [reinforcement-controls.md](references/reinforcement-controls.md) |
| Precast controls | Precast catalog references and fixture selection | [precast-controls.md](references/precast-controls.md) |
| Dynamic palette | Controls show/hide or change based on other parameter values | [dynamic-palette.md](references/dynamic-palette.md) |

---

## Related guides

- [PythonPart Script](skill://pythonpart-script) — how to read palette parameters in the script via `build_ele`
- [Create a New PythonPart](skill://create-new-pythonpart) — end-to-end workflow placing both the PYP and PY files
