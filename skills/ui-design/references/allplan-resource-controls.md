# ALLPLAN Resource Controls

These value types let the user select ALLPLAN-native formatting resources (pen, stroke, color, layer) or compound property objects. Setting `<Value>-1</Value>` initializes the control with the **current ALLPLAN setting**.

## Individual resource pickers

| `<ValueType>` | Python type (`.value`) | Selects |
|---|---|---|
| `Pen` | `int` | Pen weight |
| `Stroke` | `int` | Line stroke |
| `Color` | `int` | Standard ALLPLAN color (indexed, not arbitrary RGB — use [RGBColorDialog](dialog-controls.md#rgb-color) for full color) |
| `Layer` | `int` | Layer |
| `Hatch` | `int` | Hatching pattern |
| `Pattern` | `int` | Area fill pattern |
| `FaceStyle` | `int` | Face style |

All follow the same pattern:

```xml
<Parameter>
    <Name>Pen</Name>
    <Text>Pen</Text>
    <Value>-1</Value>
    <ValueType>Pen</ValueType>
</Parameter>

<Parameter>
    <Name>Layer</Name>
    <Text>Layer</Text>
    <Value>-1</Value>
    <ValueType>Layer</ValueType>
</Parameter>
```

---

## CommonProperties

Provides a combined editor for pen, stroke, color, and layer — equivalent to ALLPLAN's format properties panel. Returns a `NemAll_Python_BaseElements.CommonProperties` object.

```xml
<Parameter>
    <Name>CommonProp</Name>
    <Text></Text>
    <Value></Value>   <!-- empty = initialise with current ALLPLAN settings -->
    <ValueType>CommonProperties</ValueType>
</Parameter>
```

```python
import NemAll_Python_BaseElements as AllplanBaseElements

common_props: AllplanBaseElements.CommonProperties = self.build_ele.CommonProp.value
```

### Hiding individual sub-controls

Use `<Visible>` with `ControlName:Condition` syntax, separated by `|`, to suppress specific sub-controls:

```xml
<Parameter>
    <Name>CommonProp</Name>
    <Text></Text>
    <Value></Value>
    <ValueType>CommonProperties</ValueType>
    <Visible>|CommonProp.ColorByLayer:False|CommonProp.DrawOrder:False</Visible>
</Parameter>
```

Available control names for `CommonProperties`: `Stroke`, `StrokeByLayer`, `Pen`, `PenByLayer`, `Color`, `ColorByLayer`, `Layer`, `DrawOrder`.

---

## SurfaceElementProperties

Provides a combined editor for hatching, pattern, filling, and face style. Returns a `NemAll_Python_ArchElements.SurfaceElementProperties` object.

```xml
<Parameter>
    <Name>SurfaceProp</Name>
    <Text></Text>
    <Value></Value>
    <ValueType>SurfaceElementProperties</ValueType>
</Parameter>
```

Available control names for `<Visible>`: `BitmapID`, `BitmapSelected`, `FaceStyleID`, `FaceStyleSelected`, `FillingID`, `FillingSelected`, `HatchID`, `HatchSelected`, `PatternID`, `PatternSelected`, `UseAreaInGroundplan`.
