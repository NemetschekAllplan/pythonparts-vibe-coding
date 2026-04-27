---
title: "PrecastLayerPropertiesImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Precast\PrecastLayerPropertiesImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PrecastLayerPropertiesImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Precast\PrecastLayerPropertiesImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the PrecastLayerProperties value type

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Palette`
- `NemAll_Python_Precast`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.PropertyPaletteControlTextUtil`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `copy`
- `typing`

## Klassen

### `PrecastLayerPropertiesImpl`

implementation of the CommonProperties value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: AllplanPrecast.PrecastLayerProperties` | `str` | convert the common properties to a string  Args:     value: common properties  Returns:     common properties as string |
| `get_value` | `value_str: str` | `AllplanPrecast.PrecastLayerProperties` | get the common properties from a string  Args:     value_str: common properties string  Returns:     common properties from the string |
| `add_to_palette` | `wpf_palette: AllplanPalette.PythonWpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the control to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `update_enable_by_constraint` | `build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties` | `None` | update the enable state by a constraint  Args:     build_ele:  building element with the parameter properties     prop:       parameter property to update     ctrl_props: control properties |
| `is_default_init_by_constraint` | `build_ele: BuildingElement, ctrl_props: ControlProperties` | `bool` | check, whether the default value must be initialized by the constraint  Args:     build_ele:  building element with the parameter properties     ctrl_props: control properties  Returns:     default init by the constraint state |
| `copyPrecastLayerSettings` | `prop: AllplanPrecast.PrecastLayerProperties` | `AllplanPrecast.PrecastLayerProperties` | copy the precast layer settings  Args:     prop: parameter property |
| `update_by_constraint` | `build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties, _name: str` | `None` | update by a constraint  Args:     build_ele:  building element with the parameter properties     prop:       parameter property to update     ctrl_props: control properties     _name:      name of the modified value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PrecastLayerProperties value type
"""

from __future__ import annotations

from copy import copy
from typing import Any, TYPE_CHECKING, cast

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Palette as AllplanPalette
import NemAll_Python_Precast as AllplanPrecast

from ControlProperties import ControlProperties

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil
from ..ValueTypeUtils.PropertyPaletteControlTextUtil import PropertyPaletteControlTextData


if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PrecastLayerPropertiesImpl(ParameterPropertyValueType):
    """ implementation of the CommonProperties value type
    """

    @staticmethod
    def set_property_value(prop : ParameterProperty,
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

        prop.is_modified = True

        if GeneralConstants.SUB_NAME_SEPARATOR not in name:
            return ParameterPropertyListUtil.set_item_value(prop, name, value)

        layer_prop = cast(AllplanPrecast.PrecastLayerProperties, ParameterPropertyListUtil.get_item_value(prop, name))

        sub_name = name.split(".")[1]

        setattr(layer_prop, sub_name, value)

        return True

    @staticmethod
    def to_string(value: AllplanPrecast.PrecastLayerProperties) -> str:
        """ convert the common properties to a string

        Args:
            value: common properties

        Returns:
            common properties as string
        """

        return ValueToStringUtil.trim_value_string(str(value))


    @staticmethod
    def get_value(value_str: str) -> AllplanPrecast.PrecastLayerProperties:
        """ get the common properties from a string

        Args:
            value_str: common properties string

        Returns:
            common properties from the string
        """

        def get_precast_layer_properties(value_str: str) -> AllplanPrecast.PrecastLayerProperties:
            """ get the common properties from the value string

            Args:
                value_str: value string

            Returns:
                common properties
            """

            layer_prop = AllplanPrecast.PrecastLayerProperties()

            if not value_str:
                return layer_prop

            val_str_2 = str(value_str)

            layer_prop.LayerName = StringToValueUtil.get_property_string(val_str_2, "LayerName", "")
            val_str_2 = val_str_2.replace("LayerName", "")
            layer_prop.LayerNumber = StringToValueUtil.get_property_int(val_str_2, "LayerNumber", 1)
            val_str_2 = val_str_2.replace("LayerNumber", "")
            layer_prop.CalculateLayerThickness  = StringToValueUtil.get_property_bool(val_str_2, "CalculateLayerThickness", 0)
            val_str_2 = val_str_2.replace("CalculateLayerThickness", "")
            layer_prop.LayerThickness  = StringToValueUtil.get_property_float(val_str_2, "LayerThickness", 0)
            val_str_2 = val_str_2.replace("LayerThickness", "")
            layer_prop.MaterialCatAddressOffset  = StringToValueUtil.get_property_int(val_str_2, "MaterialCatAddressOffset", 0)
            val_str_2 = val_str_2.replace("MaterialCatAddressOffset", "")
            layer_prop.MaterialType  = StringToValueUtil.get_property_int(val_str_2, "MaterialType", 0)
            val_str_2 = val_str_2.replace("MaterialType", "")
            layer_prop.Material  = StringToValueUtil.get_property_string(val_str_2, "Material", "")
            val_str_2 = val_str_2.replace("Material", "")

            return layer_prop

        return BaseStringToValueConverter.to_value_by_type_converter(get_precast_layer_properties, value_str)


    @staticmethod
    def add_to_palette(wpf_palette          : AllplanPalette.PythonWpfPaletteBuilder,
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

        layer_prop = cast(AllplanPrecast.PrecastLayerProperties, prop.value)

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.LayerName",  prop_visible_dict):
            orientation = prop.selected_value if isinstance(prop.selected_value, AllplanPalette.Orientation) else \
                      AllplanPalette.Orientation.eLeft

            wpf_palette.AddText(ctrl_props.text, prop.value.LayerName, orientation, prop_pal_ctrl_service.page_index,
                                ctrl_props.expander_name + ctrl_props.expander_state_key,
                                str(layer_prop.LayerNumber) + ctrl_props.row_state_key,
                                prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                ctrl_props.height, ctrl_props.width,
                                ctrl_props.font_style, ctrl_props.font_face_code)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.LayerNumber",  prop_visible_dict):
            orientation = prop.selected_value if isinstance(prop.selected_value, AllplanPalette.Orientation) else \
                      AllplanPalette.Orientation.eLeft

            wpf_palette.AddText(ctrl_props.text, str(prop.value.LayerNumber), orientation, prop_pal_ctrl_service.page_index,
                                ctrl_props.expander_name + ctrl_props.expander_state_key,
                                str(layer_prop.LayerNumber) + ctrl_props.row_state_key,
                                prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                ctrl_props.height, ctrl_props.width,
                                ctrl_props.font_style, ctrl_props.font_face_code)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.LayerThickness",  prop_visible_dict):
            prop_pal_ctrl_service.add_length_edit_control(wpf_palette, f"{prop.name}.LayerThickness", ctrl_props,
                                                          getattr(prop.value, "LayerThickness"), ctrl_props.min_value, ctrl_props.max_value,
                                                          PropertyPaletteControlTextData(str(layer_prop.LayerNumber), ""))

        if ParameterPropertyValueType.is_visible(f"{prop.name}.CalculateLayerThickness",  prop_visible_dict):
            prop_pal_ctrl_service.add_sub_control(wpf_palette.AddCheckboxValue, prop, ctrl_props, "CalculateLayerThickness",
                                                  str(layer_prop.LayerNumber), True)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.MaterialType",  prop_visible_dict):
            orientation = prop.selected_value if isinstance(prop.selected_value, AllplanPalette.Orientation) else \
                      AllplanPalette.Orientation.eLeft

            wpf_palette.AddText(ctrl_props.text, str(prop.value.MaterialType), orientation, prop_pal_ctrl_service.page_index,
                                ctrl_props.expander_name + ctrl_props.expander_state_key,
                                str(layer_prop.LayerNumber) + ctrl_props.row_state_key,
                                prop_pal_ctrl_service.is_control_enabled(ctrl_props),
                                ctrl_props.height, ctrl_props.width,
                                ctrl_props.font_style, ctrl_props.font_face_code)

        if ParameterPropertyValueType.is_visible(f"{prop.name}.Material",  prop_visible_dict):
            if layer_prop.MaterialType == 0:
                prop_pal_ctrl_service.add_sub_control(wpf_palette.AddConcreteGradeCatalogRef, prop, ctrl_props, "Material",
                                                      str(layer_prop.LayerNumber), True)
            if layer_prop.MaterialType == 1:
                prop_pal_ctrl_service.add_sub_control(wpf_palette.AddInsulationCatalogRef, prop, ctrl_props, "Material",
                                                      str(layer_prop.LayerNumber), True)
            if layer_prop.MaterialType == 2:
                prop_pal_ctrl_service.add_sub_control(wpf_palette.AddConcreteGradeCatalogRef, prop, ctrl_props, "Material",
                                                      str(layer_prop.LayerNumber), True)
            if layer_prop.MaterialType == 3:
                prop_pal_ctrl_service.add_sub_control(wpf_palette.AddBrickTileCatalogRef, prop, ctrl_props, "Material",
                                                      str(layer_prop.LayerNumber), True)
    @staticmethod
    def update_enable_by_constraint(build_ele : BuildingElement,
                                    prop      : ParameterProperty,
                                    ctrl_props: ControlProperties):
        """ update the enable state by a constraint

        Args:
            build_ele:  building element with the parameter properties
            prop:       parameter property to update
            ctrl_props: control properties
        """

        PrecastLayerPropertiesImpl.update_by_constraint(build_ele, prop, ctrl_props, "")

    @staticmethod
    def is_default_init_by_constraint(build_ele : BuildingElement,
                                      ctrl_props: ControlProperties) -> bool:
        """ check, whether the default value must be initialized by the constraint

        Args:
            build_ele:  building element with the parameter properties
            ctrl_props: control properties

        Returns:
            default init by the constraint state
        """

        constraints = ctrl_props.constraint

        element_id       = build_ele.get_property(constraints[0])
        layerDefs = AllplanPrecast.PrecastElement.GetPrecastLayersFromCatalog(element_id.value)

        if len(layerDefs) > 0:
            return True
        else:
            return False

    @staticmethod
    def copyPrecastLayerSettings(prop : AllplanPrecast.PrecastLayerProperties) -> AllplanPrecast.PrecastLayerProperties:
        """ copy the precast layer settings

        Args:
            prop: parameter property
        """
        if not prop:
            return

        lyr_prop_val = AllplanPrecast.PrecastLayerProperties()
        lyr_prop_val.LayerName = copy(prop.LayerName)
        lyr_prop_val.LayerNumber = copy(prop.LayerNumber)
        lyr_prop_val.CalculateLayerThickness = copy(prop.CalculateLayerThickness)
        lyr_prop_val.LayerThickness = copy(prop.LayerThickness)
        lyr_prop_val.MaterialCatAddressOffset = copy(prop.MaterialCatAddressOffset)
        lyr_prop_val.MaterialType = copy(prop.MaterialType)
        lyr_prop_val.Material = copy(prop.Material)

        return lyr_prop_val

    @staticmethod
    def update_by_constraint(build_ele : BuildingElement,
                             prop      : ParameterProperty,
                             ctrl_props: ControlProperties,
                             _name     : str):
        """ update by a constraint

        Args:
            build_ele:  building element with the parameter properties
            prop:       parameter property to update
            ctrl_props: control properties
            _name:      name of the modified value
        """

        constraints = ctrl_props.constraint

        element_id       = build_ele.get_property(constraints[0])

        layerDefs = AllplanPrecast.PrecastElement.GetPrecastLayersFromCatalog(element_id.value)
        layernumber = 1
        ctrl_props.visible_condition = "|Layer.LayerName:True|Layer.LayerNumber:False|Layer.LayerThickness:False|Layer.CalculateLayerThickness:False|Layer.MaterialType:False|Layer.Material:True"

        lyr_prop_val = AllplanPrecast.PrecastLayerProperties()
        if len(layerDefs) <= 0:
            ctrl_props.visible_condition = "False"
            prop.value = []
            return

        if len(layerDefs) == 1:
            if isinstance(prop.value, list):
                for prop_val in prop.value:
                    if prop_val.MaterialType == layerDefs[0][1]:
                        lyr_prop_val = PrecastLayerPropertiesImpl.copyPrecastLayerSettings(prop_val)
                        break
            elif prop.value.MaterialType == layerDefs[0][1]:
                lyr_prop_val = PrecastLayerPropertiesImpl.copyPrecastLayerSettings(prop.value)
            else:
                lyr_prop_val.MaterialType = layerDefs[0][1]
            lyr_prop_val.LayerName = layerDefs[0][0]
            lyr_prop_val.LayerNumber = layernumber
            prop.value = [lyr_prop_val]
            return

        ctrl_props.visible_condition = "|Layer.LayerName:True|Layer.LayerNumber:False|Layer.LayerThickness:True|Layer.CalculateLayerThickness:True|Layer.MaterialType:False|Layer.Material:True"
        old_prop_value = (prop.value)
        prop.value = []
        for lyr in layerDefs:
            lyr_prop_val = AllplanPrecast.PrecastLayerProperties()
            lyr_prop_val.LayerName = lyr[0]
            lyr_prop_val.MaterialType = lyr[1]

            if isinstance(old_prop_value, list):
                for prop_val in old_prop_value:
                    if prop_val.MaterialType == lyr_prop_val.MaterialType and prop_val.LayerName == lyr_prop_val.LayerName:
                        lyr_prop_val = PrecastLayerPropertiesImpl.copyPrecastLayerSettings(prop_val)
                        break
                    elif  prop_val.MaterialType == lyr_prop_val.MaterialType:
                        lyr_prop_val.Material = copy(prop_val.Material)
                        lyr_prop_val.MaterialCatAddressOffset = copy(prop_val.MaterialCatAddressOffset)
            else:
                if old_prop_value.MaterialType == lyr[1] and prop_val.LayerName == lyr[0]:
                    lyr_prop_val = PrecastLayerPropertiesImpl.copyPrecastLayerSettings(old_prop_value)
                elif  prop_val.MaterialType == lyr_prop_val.MaterialType:
                    lyr_prop_val.Material = copy(prop_val.Material)
                    lyr_prop_val.MaterialCatAddressOffset = copy(prop_val.MaterialCatAddressOffset)

            lyr_prop_val.LayerNumber = layernumber
            prop.value.append(lyr_prop_val)
            layernumber += 1

```

</details>