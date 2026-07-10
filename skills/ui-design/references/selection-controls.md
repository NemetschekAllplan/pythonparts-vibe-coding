# Selection Controls

Use these value types when the user must choose from a finite set of options.

## Combo boxes

A combo box shows a dropdown list. `<ValueList>` is required for all combo box types — entries are separated by `|`. An optional `<ValueTextList>` provides display labels that differ from the stored values.

| `<ValueType>` | Python type (`.value`) | Notes |
|---|---|---|
| `StringComboBox` | `str` | Stored value and display label can differ via `<ValueTextList>` |
| `IntegerComboBox` | `int` | `<Value>` and all `<ValueList>` entries must be integers |
| `DoubleComboBox` | `float` | — |
| `LengthComboBox` | `float` | Values in **mm**; displayed in current ALLPLAN unit |
| `AngleComboBox` | `float` | Displayed in current ALLPLAN angle unit; stored in **degrees** |
| `PictureResourceComboBox` | `int` | Displays ALLPLAN internal icons; `<ValueList2>` holds icon resource IDs |

### StringComboBox

```xml
<Parameter>
    <Name>Material</Name>
    <Text>Material</Text>
    <Value>concrete</Value>
    <ValueType>StringComboBox</ValueType>
    <ValueList>concrete|steel|timber</ValueList>
    <ValueTextList>Concrete|Steel|Timber</ValueTextList>
</Parameter>
```

### IntegerComboBox

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

### PictureResourceComboBox

Displays ALLPLAN internal icons in the dropdown. `<ValueList>` holds the stored values (integers), `<ValueList2>` holds the icon resource IDs:

```xml
<Parameter>
    <Name>EdgeOffsetType</Name>
    <Text>Offset type</Text>
    <Value>0</Value>
    <ValueList>0|1|2|3|4</ValueList>
    <ValueTextList>Zero at start|Major at start|Equal|Major at end|Zero at end</ValueTextList>
    <ValueList2>12151|12147|12149|12153|12145</ValueList2>
    <ValueType>PictureResourceComboBox</ValueType>
</Parameter>
```

---

## Check box

Returns `bool`. Use `<Constraint>` to make another checkbox deselect automatically when this one is selected (mutual exclusion):

```xml
<Parameter>
    <Name>ShowGrid</Name>
    <Text>Show grid</Text>
    <Value>False</Value>
    <ValueType>CheckBox</ValueType>
</Parameter>
```

### Mutually exclusive checkboxes

```xml
<Parameter>
    <Name>OptionA</Name>
    <Text>Option A</Text>
    <Value>True</Value>
    <ValueType>CheckBox</ValueType>
    <Constraint>OptionB</Constraint>
</Parameter>

<Parameter>
    <Name>OptionB</Name>
    <Text>Option B</Text>
    <Value>False</Value>
    <ValueType>CheckBox</ValueType>
    <Constraint>OptionA</Constraint>
</Parameter>
```

---

## Radio buttons

`RadioButtonGroup` is the value holder; it wraps child `RadioButton` parameters. The selected button's `<Value>` is assigned to the group parameter.

```xml
<Parameter>
    <Name>Alignment</Name>
    <Text>Alignment</Text>
    <Value>1</Value>
    <ValueType>RadioButtonGroup</ValueType>

    <Parameter>
        <Name>AlignLeft</Name>
        <Text>Left</Text>
        <Value>1</Value>
        <ValueType>RadioButton</ValueType>
    </Parameter>
    <Parameter>
        <Name>AlignCenter</Name>
        <Text>Center</Text>
        <Value>2</Value>
        <ValueType>RadioButton</ValueType>
    </Parameter>
    <Parameter>
        <Name>AlignRight</Name>
        <Text>Right</Text>
        <Value>3</Value>
        <ValueType>RadioButton</ValueType>
    </Parameter>
</Parameter>
```

In the script, read the selected value from the group parameter:

```python
alignment = self.build_ele.Alignment.value   # returns 1, 2, or 3
```
