---
title: "BuildingElementParameterPropertyUtil"
source: "PythonPartsFramework\GeneralScripts\BuildingElementParameterPropertyUtil.py"
type: "module"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementParameterPropertyUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementParameterPropertyUtil.py`  
> **Typ:** Modul  
> **Tags:** `parameter`, `script`, `utility`

## Übersicht

Implementation of the building element parameter property utilities

## Abhängigkeiten

- `ParameterProperty`
- `re`
- `typing`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `get_property_value_name(name: str)`

Get the name of the property (remove sub value name, e.g. in case of Point.X)

Args:
    name: name of the modified property

Returns:
    name of the property

**Parameter:**
- `name: str`

**Rückgabe:** `str`

**Beispiel:**
```python
result = get_property_value_name(...)
```

### `set_property_value(prop: ParameterProperty, name: str, value: Any)`

Set the value of the property

Args:
    prop:  property
    name:  property name
    value: property value

Returns:
    palette update state

**Parameter:**
- `prop: ParameterProperty`
- `name: str`
- `value: Any`

**Rückgabe:** `bool`

**Beispiel:**
```python
result = set_property_value(..., ..., ...)
```

### `get_property_value(prop: ParameterProperty, name: str)`

Get the property value by the name.

The name can have a list and/or tuple index like:

  Value
  Value[1]
  Value[1][2]
  Value[1](3)
  Value[1][2](3)
  Value(3)

Args:
    prop: property
    name: property name

Returns:
    property value

**Parameter:**
- `prop: ParameterProperty`
- `name: str`

**Rückgabe:** `Any`

**Beispiel:**
```python
result = get_property_value(..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the building element parameter property utilities
"""

from typing import Any

import re

from ParameterProperty import ParameterProperty

def get_property_value_name(name: str) -> str:
    """ Get the name of the property (remove sub value name, e.g. in case of Point.X)

    Args:
        name: name of the modified property

    Returns:
        name of the property
    """

    if name is None:
        return ""

    to_find = re.compile(r"\[|\(|\.")

    if not (match_obj := to_find.search(name)):
        return name

    return name[:match_obj.start()]


def set_property_value(prop : ParameterProperty,
                       name : str,
                       value: Any) -> bool:
    """ Set the value of the property

    Args:
        prop:  property
        name:  property name
        value: property value

    Returns:
        palette update state
    """

    return prop.value_type.set_property_value(prop, name, value)


def get_property_value(prop: ParameterProperty,
                       name: str) -> Any:
    """ Get the property value by the name.

    The name can have a list and/or tuple index like:

      Value
      Value[1]
      Value[1][2]
      Value[1](3)
      Value[1][2](3)
      Value(3)

    Args:
        prop: property
        name: property name

    Returns:
        property value
    """

    if "[" not in name and "(" not in name:
        return prop.value

    return eval(name.replace("(", "[").replace(")", "]"), {get_property_value_name(name): prop.value})

```

</details>