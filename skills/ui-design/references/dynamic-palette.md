# Dynamic Palette

> **Load this reference only when the palette needs to respond to parameter changes** — e.g. hiding a control when a checkbox is unchecked, changing label text based on a selection, or showing entirely different parameter sets per input step.

## Visibility and enable state in the PYP file

Add `<Visible>` or `<Enable>` to any `<Parameter>`. The value is a Python expression evaluated against other parameter names:

```xml
<Parameter>
    <Name>Offset</Name>
    <Text>Offset</Text>
    <Value>100</Value>
    <ValueType>Length</ValueType>
    <Visible>UseOffset</Visible>         <!-- shown when UseOffset checkbox is True -->
    <Enable>UseOffset and IsEditable</Enable>
</Parameter>
```

> In XML, use `&lt;` for `<` and `&gt;` for `>` inside condition expressions.

### Condition examples

```xml
<Visible>RadioButtonValue in [1, 5]</Visible>
<Enable>FooParameter == True</Enable>
<Enable>__is_input_mode()</Enable>                         <!-- False during modification mode -->
<Visible>__is_visible_control("OtherParam") and OtherParam > 0</Visible>

<!-- Multi-line expression (must be left-aligned) -->
<Visible>
if FooParameter &lt; 1000:
    return True
if BarParameter &gt; 500:
    return True
return False
</Visible>
```

### ConditionGroup

Apply one condition to multiple consecutive parameters without repeating it on each:

```xml
<Parameter>
    <ValueType>ConditionGroup</ValueType>
    <Visible>ShapeType == 2</Visible>

    <Parameter>
        <Name>Radius</Name>
        <Text>Radius</Text>
        <Value>500</Value>
        <ValueType>Length</ValueType>
    </Parameter>
    <Parameter>
        <Name>Segments</Name>
        <Text>Segments</Text>
        <Value>8</Value>
        <ValueType>Integer</ValueType>
    </Parameter>
</Parameter>
```

---

## Dynamic label text (`<TextDyn>`)

Use `<TextDyn>` to compute the label of a parameter at runtime:

```xml
<TextDyn>__StringTable.get_string(1003, "Placement") + (" right" if RightSide else " left")</TextDyn>
```

Multi-line expressions are supported. Inside list parameters, `$list_row` holds the current row index.

---

## Script-controlled visibility (`ControlPropertiesUtil.ControlPropertiesUtil`)

Use this when the condition is too complex for a PYP expression.

In a **Script Object**, `ControlPropertiesUtil.ControlPropertiesUtil` is available via `BaseScriptObject.BaseScriptObjectData`:

```python
from ControlPropertiesUtil import ControlPropertiesUtil

def create_script_object(build_ele, script_object_data):
    _setup_control_properties(build_ele, script_object_data.ctrl_prop_util)
    return MyPythonPart(build_ele, script_object_data)

def _setup_control_properties(build_ele, ctrl_prop_util: ControlPropertiesUtil):
    ctrl_prop_util.set_visible_function("OffsetParam", lambda: build_ele.UseOffset.value)
    ctrl_prop_util.set_enable_function("ScaleParam",  lambda: build_ele.UseOffset.value)
```

Re-apply after each palette change by overriding `modify_element_property`:

```python
def modify_element_property(self, page, name, value):
    _setup_control_properties(self.build_ele, self.script_object_data.ctrl_prop_util)
```

### Available utility methods

| Method | Effect |
|---|---|
| `set_visible_function(name, fn)` | Control visibility via a callable returning `bool` |
| `set_enable_function(name, fn)` | Control enable state via a callable returning `bool` |
| `set_text(name, text)` | Override the label text at runtime |
| `set_min_value(name, val)` | Change the minimum allowed value |
| `set_max_value(name, val)` | Change the maximum allowed value |
| `set_value_list(name, list)` | Replace combo box options |
| `set_background_color(name, color)` | Set the input field background colour |

The callable signature depends on the parameter type:

| Parameter type | Callable signature |
|---|---|
| Single value | `() -> bool` |
| List parameter | `(row_index: int) -> bool` |
| Single namedtuple | `(field_name: str) -> bool` |
| List of namedtuple | `(row_index: int, field_name: str) -> bool` |

---

## Dynamic palette content (Include)

To show entirely different parameter sets based on context (e.g. per input step), split them into `.incpyp` files and include them conditionally:

```xml
<!-- In the main .pyp file -->
<Parameter>
    <Name>Step1Params</Name>
    <Text/>
    <Value>Step1.incpyp</Value>
    <ValueType>Include</ValueType>
    <Visible>InputStep == 1</Visible>
</Parameter>
<Parameter>
    <Name>Step2Params</Name>
    <Text/>
    <Value>Step2.incpyp</Value>
    <ValueType>Include</ValueType>
    <Visible>InputStep == 2</Visible>
</Parameter>
```

Track the current step in a hidden page parameter:

```xml
<Page>
    <Name>__HiddenPage__</Name>
    <Text></Text>
    <Parameters>
        <Parameter>
            <Name>InputStep</Name>
            <Text/>
            <Value>1</Value>
            <ValueType>Integer</ValueType>
            <Persistent>No</Persistent>   <!-- not saved with the PythonPart element -->
        </Parameter>
    </Parameters>
</Page>
```
