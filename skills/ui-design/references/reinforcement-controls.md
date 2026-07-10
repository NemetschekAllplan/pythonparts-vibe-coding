# Reinforcement Controls

Reinforcement resource controls create combo boxes pre-populated with values from ALLPLAN reinforcement catalogs. Setting `<Value>-1</Value>` initialises the control with the **current ALLPLAN setting**.

## Reference table

| `<ValueType>` | Python type (`.value`) | Returns |
|---|---|---|
| `ReinfSteelGrade` | `int` | Steel grade ID (from cross-section catalog) |
| `ReinfConcreteGrade` | `int` | Concrete grade ID (from cross-section catalog) |
| `ReinfBarDiameter` | `float` | Bar diameter in **mm** |
| `ReinfConcreteCover` | `float` | Concrete cover in **mm** |
| `ReinfBendingRoller` | `float` | Bending roller diameter factor |
| `ReinfMeshGroup` | `int` | Mesh group ID |

## Example

```xml
<Parameter>
    <Name>SteelGrade</Name>
    <Text>Steel grade</Text>
    <Value>-1</Value>
    <ValueType>ReinfSteelGrade</ValueType>
</Parameter>

<Parameter>
    <Name>BarDiameter</Name>
    <Text>Bar diameter</Text>
    <Value>-1</Value>
    <ValueType>ReinfBarDiameter</ValueType>
</Parameter>

<Parameter>
    <Name>ConcreteCover</Name>
    <Text>Concrete cover</Text>
    <Value>-1</Value>
    <ValueType>ReinfConcreteCover</ValueType>
</Parameter>

<Parameter>
    <Name>ConcreteGrade</Name>
    <Text>Concrete grade</Text>
    <Value>-1</Value>
    <ValueType>ReinfConcreteGrade</ValueType>
</Parameter>
```
