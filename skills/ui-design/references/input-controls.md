# Input Controls

Edit controls allow the user to type a value directly into an input field.

## Value types

| `<ValueType>` | Python type (`.value`) | Unit notes |
|---|---|---|
| `String` | `str` | — |
| `Integer` | `int` | — |
| `Double` | `float` | — |
| `Length` | `float` | Displayed in current ALLPLAN unit; stored in **mm** |
| `Area` | `float` | Displayed in current ALLPLAN unit²; stored in **mm²** |
| `Volume` | `float` | Displayed in current ALLPLAN unit³; stored in **mm³** |
| `Angle` | `float` | Displayed in current ALLPLAN angle unit; stored in **degrees** |
| `Weight` | `float` | Displayed in current ALLPLAN weight unit; stored in **kg** |
| `Date` | `datetime.date` | Built-in Python `date` object |

## Examples

```xml
<Parameter>
    <Name>Width</Name>
    <Text>Width</Text>
    <Value>1000</Value>
    <ValueType>Length</ValueType>
</Parameter>

<Parameter>
    <Name>Count</Name>
    <Text>Count</Text>
    <Value>3</Value>
    <ValueType>Integer</ValueType>
</Parameter>

<Parameter>
    <Name>Label</Name>
    <Text>Label</Text>
    <Value>My PythonPart</Value>
    <ValueType>String</ValueType>
</Parameter>

<Parameter>
    <Name>BuildDate</Name>
    <Text>Build date</Text>
    <Value>date(2024,1,1)</Value>
    <ValueType>Date</ValueType>
</Parameter>
```

## Additional tags

### Min and max values

Constrain any numeric type with `<MinValue>` and `<MaxValue>`:

```xml
<Parameter>
    <Name>Segments</Name>
    <Text>Segments</Text>
    <Value>4</Value>
    <ValueType>Integer</ValueType>
    <MinValue>3</MinValue>
    <MaxValue>12</MaxValue>
</Parameter>
```

### Imperial default value

For `Length` and `Weight`, provide an alternative default for imperial unit environments:

```xml
<Parameter>
    <Name>Height</Name>
    <Text>Height</Text>
    <Value>3000</Value>
    <ValueType>Length</ValueType>
    <ImperialValue>10'</ImperialValue>
</Parameter>
```

### Date with calendar picker

Add `<ValueDialog>DateDialog</ValueDialog>` to show a calendar button alongside the date input field:

```xml
<Parameter>
    <Name>DeliveryDate</Name>
    <Text>Delivery date</Text>
    <Value>date(2024,1,1)</Value>
    <ValueType>Date</ValueType>
    <ValueDialog>DateDialog</ValueDialog>
</Parameter>
```
