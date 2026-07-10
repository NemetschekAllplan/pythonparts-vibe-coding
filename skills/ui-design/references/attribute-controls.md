# Attribute Controls

These value types bind a PythonPart parameter to an ALLPLAN attribute definition.

## Static attribute

`<ValueType>Attribute</ValueType>` with `<AttributeId>` — the input control type and value type are derived automatically from the attribute's definition in ALLPLAN (can be `str`, `int`, or `float`).

```xml
<Parameter>
    <Name>FireRiskFactor</Name>
    <Text>Fire risk factor</Text>
    <Value>A1</Value>
    <ValueType>Attribute</ValueType>
    <AttributeId>1398</AttributeId>
</Parameter>
```

---

## Dynamic attribute (AttributeIdValue)

Shows both a value input and an attribute selection button. The user picks the attribute at runtime. Result is an `AttributeIdValue.AttributeIdValue` object containing both the attribute ID and its value.

```xml
<Parameter>
    <Name>DynAttribute</Name>
    <Text>Attribute</Text>
    <Value>(1398,A2)</Value>   <!-- tuple: (int AttributeId, Any value) -->
    <ValueType>AttributeIdValue</ValueType>
    <ValueDialog>AttributeSelection</ValueDialog>
</Parameter>
```

```python
from AttributeIdValue import AttributeIdValue

attr: AttributeIdValue = self.build_ele.DynAttribute.value
attr_id    = attr.attribute_id   # int
attr_value = attr.value
```

---

## Dynamic attribute list

Set `<Value>` to a Python list to allow the user to select and configure **multiple** attributes. Result is a `List[AttributeIdValue.AttributeIdValue]`.

```xml
<Parameter>
    <Name>AttributeList</Name>
    <Text>Attributes</Text>
    <Value>[(0,)]</Value>
    <ValueType>AttributeIdValue</ValueType>
    <ValueDialog>AttributeSelection</ValueDialog>
</Parameter>
```

```python
from AttributeIdValue import AttributeIdValue
from typing import List

attrs: List[AttributeIdValue] = self.build_ele.AttributeList.value
for attr in attrs:
    print(attr.attribute_id, attr.value)
```
