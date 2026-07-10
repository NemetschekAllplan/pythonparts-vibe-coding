# Collection Parameters

## Python list

For most value types, setting `<Value>` to a Python list creates a list parameter. Each item appears as a separate row in the palette.

### One-dimensional list

```xml
<Parameter>
    <Name>CubeDimensions</Name>
    <Text>Dimension</Text>
    <Value>[1000., 1200., 1400., 1600., 1800.]</Value>
    <ValueType>Length</ValueType>
</Parameter>
```

List comprehensions work as default values: `[1000.0 + x * 200.0 for x in range(5)]`

### Two-dimensional list

```xml
<Parameter>
    <Name>Grid</Name>
    <Text>Row</Text>
    <Value>[[0 for x in range(3)] for y in range(5)]</Value>
    <ValueType>Length</ValueType>
</Parameter>
```

### Separator syntax

For simple types (int, str) use `,` as separator. For complex objects (Point2D, etc.) use `;`:

```xml
<Value>[Point2D(0,500);Point2D(0,0);Point2D(400,20)]</Value>
```

### MultiIndex — navigate to a specific item

Instead of displaying all list rows at once, use a `MultiIndex` parameter to expose a compact single-item editor. The user can access specific items by index number, ranges (`1-5`), or comma lists (`1,3,5`).

```xml
<Parameter>
    <Name>SizeIndex</Name>
    <Text>Index</Text>
    <Value>1</Value>
    <ValueType>MultiIndex</ValueType>
    <MinValue>1</MinValue>
    <MaxValue>5</MaxValue>
</Parameter>

<Parameter>
    <Name>CubeDimensions</Name>
    <Text>Size</Text>
    <Value>[1000., 1200., 1400., 1600., 1800.]</Value>
    <ValueType>Length</ValueType>
    <ValueIndexName>SizeIndex</ValueIndexName>   <!-- link to the MultiIndex parameter -->
</Parameter>
```

---

## Tuple

Defines a parameter with multiple fields of (optionally) different types. Field labels are pipe-separated in `<Text>`. The `<ValueList>` entries correspond positionally to each field (leave blank for non-combo fields):

```xml
<Parameter>
    <Name>Sizes</Name>
    <Text>Length|Width|Height</Text>
    <Value>(1000,2000,3000)</Value>
    <ValueType>Tuple(Length,LengthComboBox,Length)</ValueType>
    <ValueList>,1000|2000|3000|4000|5000,</ValueList>
</Parameter>
```

```python
from typing import Tuple

length, width, height = self.build_ele.Sizes.value  # each is float (mm)
```

To display all fields in a single row, wrap the tuple parameter in a [Row](layout-controls.md#row).

---

## AnyValueByType — fully dynamic palette

Use `AnyValueByType` when the palette parameters are determined at runtime (e.g. loaded from a file or database). The `<Value>` is initialised as an empty list; the script populates it.

```xml
<Parameter>
    <Name>DynamicParams</Name>
    <Text> </Text>
    <Value>[_]</Value>
    <ValueType>AnyValueByType</ValueType>
</Parameter>
```

```python
from AnyValueByType import AnyValueByType
from typing import List

params: List[AnyValueByType] = self.build_ele.DynamicParams.value

if not params:
    params.append(AnyValueByType("Length",        "Width",    1000, min_value="0"))
    params.append(AnyValueByType("Integer",       "Count",    3))
    params.append(AnyValueByType("CheckBox",      "Active",   False))
    params.append(AnyValueByType("StringComboBox","Material", "concrete",
                                  "concrete|steel|timber"))
```

> A typical use case: read parameter definitions from a file in create mode, then restore them from the saved PythonPart in modification mode.
