---
title: "GeometryObjectImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\GeometryObjectImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# GeometryObjectImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\GeometryElements\GeometryObjectImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `script`, `werte`

## Übersicht

implementation of the GeometryObject value type

## Abhängigkeiten

- `ControlProperties`
- `NemAll_Python_Geometry`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `ParameterPropertyValueTypesImpl`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `__future__`
- `typing`

## Klassen

### `GeometryObjectImpl`

implementation of the GeometryObject value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `cls, prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `get_value` | `value_str: str` | `list[Any] | Any` | get the geometry object  Args:     value_str: geometry object string  Returns:     geometry object |
| `to_string` | `value: Any` | `str` | convert the geometry object  Args:     value: coordinate value  Returns:     coordinate as string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__get_geometry_value_type` | `value: Any` | `ParameterPropertyValueType | None` | get the value type of the geometry object  Args:     value: geometry object  Returns:     value type |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the GeometryObject value type
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import NemAll_Python_Geometry as AllplanGeo

from ControlProperties import ControlProperties

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

if TYPE_CHECKING:
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class GeometryObjectImpl(ParameterPropertyValueType):
    """ implementation of the GeometryObject value type
    """

    @classmethod
    def set_property_value(cls,
                           prop : ParameterProperty,
                           name : str,
                           value: Any) -> bool:
        """ Set the value of the property

        Args:
            prop:  property
            name:  name of the modified property
            value: new value

        Returns:
            update palette state
        """

        #----------------- 2 dim. list

        if (index_2d := ParameterPropertyListUtil.get_list_index_2dim(name)) is not None:
            if isinstance(prop.value[index_2d[0]], list):
                prop_value = prop.value[index_2d[0]][index_2d[1]]
            else:
                prop_value = prop.value[index_2d[0]]

            if (value_type := GeometryObjectImpl.__get_geometry_value_type(prop_value)) is None:
                return False

            return value_type.set_property_value(prop, name, value)


        #----------------- 2 dim. list

        if (list_index := ParameterPropertyListUtil.get_list_index(name)) is not None:
            if isinstance(prop.value, list):
                if list_index - len(prop.value) >= 0:
                    return False

                prop_value = prop.value[list_index]
            else:
                prop_value = prop.value

            if (value_type := GeometryObjectImpl.__get_geometry_value_type(prop_value)) is None:
                return False

            return value_type.set_property_value(prop, name, value)

        if (value_type := GeometryObjectImpl.__get_geometry_value_type(prop.value)) is None:
            return False

        return value_type.set_property_value(prop, name, value)


    @staticmethod
    def get_value(value_str: str) -> (list[Any] | Any):
        """ get the geometry object

        Args:
            value_str: geometry object string

        Returns:
            geometry object
        """

        def convert_geo(geo_value_str: str) -> Any:
            """ convert the geometry value string

            Args:
                geo_value_str: geometry value string

            Returns:
                geometry object
            """

            if not geo_value_str:
                return None

            if not (geo_type := geo_value_str.split("(")[0]):
                return None

            if getattr(AllplanGeo, geo_type) is None:
                return None

            value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(geo_type)

            return value_type.get_value(geo_value_str)

        return BaseStringToValueConverter.to_value_by_type_converter(convert_geo, value_str)


    @staticmethod
    def to_string(value: Any) -> str:
        """ convert the geometry object

        Args:
            value: coordinate value

        Returns:
            coordinate as string
        """

        if value is None or (value_type := GeometryObjectImpl.__get_geometry_value_type(value)) is None:
            return ""

        return value_type.to_string(value)


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the control to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        if (value_type := GeometryObjectImpl.__get_geometry_value_type(prop.value)) is None:
            return

        if ctrl_props.row_name.isnumeric() and int(ctrl_props.row_name) > ctrl_props.value_list_start_row:
            wpf_palette.AddSeparator(prop_pal_ctrl_service.page_index, ctrl_props.expander_name)

        value_type.add_to_palette(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def __get_geometry_value_type(value: Any) -> (ParameterPropertyValueType | None):
        """ get the value type of the geometry object

        Args:
            value: geometry object

        Returns:
            value type
        """

        geo_type = str(type(value))
        geo_type = geo_type.replace("<class 'NemAll_Python_Geometry.", "")

        if not (geo_type := geo_type.replace("'>", "").lower()):
            return None

        return ParameterPropertyValueTypesImpl.get_value_type_impl(geo_type)

```

</details>