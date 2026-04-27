---
title: "ControlMinMaxUtil"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ControlMinMaxUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ControlMinMaxUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ValueTypeUtils\ControlMinMaxUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`, `werte`

## Übersicht

implementation of the control min/max utility

## Abhängigkeiten

- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `StringEvaluate`
- `ValueTypeUtil`
- `ValueTypes.ParameterPropertyValueType`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `typing`

## Klassen

### `ControlMinMaxUtil`

implementation of the control min/max utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_min_max_values` | `ctrl_props: ControlProperties, value_type: ParameterPropertyValueType, attribute_id: int, param_dict: dict[str, Any]` | `None` | Set the min/max values of the properties  Args:     ctrl_props:   control properties     value_type:   value type     attribute_id: attribute ID     param_dict:   parameter dictionary |
| `set_min_value` | `ctrl_props: ControlProperties, value_type: ParameterPropertyValueType, param_dict: dict[str, Any]` | `None` | set the min value  Args:     ctrl_props: control properties     value_type: value type     param_dict: parameter dictionary |
| `set_max_value` | `ctrl_props: ControlProperties, value_type: ParameterPropertyValueType, param_dict: dict[str, Any]` | `None` | set the max value  Args:     ctrl_props: control properties     value_type: value type     param_dict: parameter dictionary |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the control min/max utility
"""

from typing import Any

import NemAll_Python_BaseElements as AllplanBaseEle

from ControlProperties import ControlProperties
from DocumentManager import DocumentManager
from StringEvaluate import StringEvaluate
from ValueTypeUtil import ValueTypeUtil

from ValueTypes.ParameterPropertyValueType import ParameterPropertyValueType
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

class ControlMinMaxUtil():
    """ implementation of the control min/max utility
    """

    @staticmethod
    def set_min_max_values(ctrl_props  : ControlProperties,
                           value_type  : ParameterPropertyValueType,
                           attribute_id: int,
                           param_dict  : dict[str, Any]):
        """ Set the min/max values of the properties

        Args:
            ctrl_props:   control properties
            value_type:   value type
            attribute_id: attribute ID
            param_dict:   parameter dictionary
        """

        if value_type.is_tuple_type() or ValueTypeUtil.is_string_input(value_type):
            return

        if (value_type := ParameterPropertyValueTypesImpl.get_value_type_impl(value_type.replace("combobox", ""))) == \
            ParameterPropertyValueTypes.ATTRIBUTE:
            attribute_type_enum = AllplanBaseEle.AttributeService.AttributeType

            doc = DocumentManager.get_instance().document

            if AllplanBaseEle.AttributeService.GetAttributeType(doc, attribute_id) == attribute_type_enum.Double:
                value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.DOUBLE)

        ControlMinMaxUtil.set_min_value(ctrl_props, value_type, param_dict)
        ControlMinMaxUtil.set_max_value(ctrl_props, value_type, param_dict)


    @staticmethod
    def set_min_value(ctrl_props: ControlProperties,
                      value_type: ParameterPropertyValueType,
                      param_dict: dict[str, Any]):
        """ set the min value

        Args:
            ctrl_props: control properties
            value_type: value type
            param_dict: parameter dictionary
        """

        if (min_value_condition := ctrl_props.min_value_condition):
            ctrl_props.min_value = StringEvaluate.eval(min_value_condition, param_dict)

        else:
            ctrl_props.min_value = value_type.get_min_value()


    @staticmethod
    def set_max_value(ctrl_props: ControlProperties,
                      value_type: ParameterPropertyValueType,
                      param_dict: dict[str, Any]):
        """ set the max value

        Args:
            ctrl_props: control properties
            value_type: value type
            param_dict: parameter dictionary
        """

        if (max_value_condition := ctrl_props.max_value_condition):
            ctrl_props.max_value = StringEvaluate.eval(max_value_condition, param_dict)

        else:
            ctrl_props.max_value = value_type.get_max_value()

```

</details>