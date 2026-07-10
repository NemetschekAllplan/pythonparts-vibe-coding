# Button Control

A button triggers an action in the script when clicked. Because a button needs both a label (left column) and button text (right column), it **must be placed inside a [Row](layout-controls.md#row)**.

## Basic button

```xml
<Parameter>
    <Name>ApplyRow</Name>
    <Text>Apply defaults</Text>   <!-- label on the left side -->
    <ValueType>Row</ValueType>

    <Parameters>
        <Parameter>
            <Name>ApplyButton</Name>
            <Text>Apply</Text>    <!-- text on the button itself -->
            <EventId>1000</EventId>
            <ValueType>Button</ValueType>
        </Parameter>
    </Parameters>
</Parameter>
```

When clicked, the framework calls `on_control_event` on the script object and passes the `<EventId>` value:

```python
def on_control_event(self, event_id: int):
    if event_id == 1000:
        self.build_ele.Width.value = 1000.0   # reset to default
    elif event_id == 1001:
        pass  # handle second button
```

Multiple buttons can share the same `<EventId>` to trigger the same handler.

> If the button text is too long to fit, only the end is displayed directly on the button. The full text appears as a tooltip.

---

## Hyperlink button

Set `<Value>` to a URL — clicking opens it in the system browser. No `on_control_event` call is made.

```xml
<Parameter>
    <Name>HelpRow</Name>
    <Text>Documentation</Text>
    <ValueType>Row</ValueType>
    <Parameters>
        <Parameter>
            <Name>HelpButton</Name>
            <Text>Open docs</Text>
            <EventId>0</EventId>
            <ValueType>Button</ValueType>
            <Value>https://pythonparts.allplan.com</Value>
        </Parameter>
    </Parameters>
</Parameter>
```

---

## Button with icon (PictureResourceButton)

Renders a button showing an ALLPLAN internal icon instead of text. The `<Text>` tag is used as a tooltip.

```xml
<Parameter>
    <Name>ResetRow</Name>
    <Text>Reset</Text>
    <ValueType>Row</ValueType>
    <Parameters>
        <Parameter>
            <Name>ResetButton</Name>
            <Text>Reset to defaults</Text>   <!-- shown as tooltip -->
            <EventId>1001</EventId>
            <Value>17027</Value>              <!-- ALLPLAN internal icon ID -->
            <ValueType>PictureResourceButton</ValueType>
        </Parameter>
    </Parameters>
</Parameter>
```
