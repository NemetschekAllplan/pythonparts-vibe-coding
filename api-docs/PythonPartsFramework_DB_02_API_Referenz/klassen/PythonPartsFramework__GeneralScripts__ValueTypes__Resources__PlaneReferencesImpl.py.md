---
title: "PlaneReferencesImpl"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\Resources\PlaneReferencesImpl.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# PlaneReferencesImpl

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\Resources\PlaneReferencesImpl.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

implementation of the PlaneReferences value type

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `DocumentManager`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_ArchElements`
- `NemAll_Python_IFW_ElementAdapter`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `ParameterPropertyValueType`
- `StringEvaluate`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.BaseStringToValueConverter`
- `ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypeUtils.PropertyPaletteControlService`
- `ValueTypeUtils.StringToValueUtil`
- `ValueTypeUtils.ValueToStringUtil`
- `__future__`
- `re`
- `typing`

## Klassen

### `PlaneReferencesImpl`

implementation of the PlaneReferences value type
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_property_value` | `prop: ParameterProperty, name: str, value: Any` | `bool` | Set the value of the property  Args:     prop:  property     name:  name of the modified property     value: new value  Returns:     update palette state |
| `to_string` | `value: str` | `str` | convert the plane references to a string  Args:     value: new value  Returns:     plane references as string |
| `get_value` | `value_str: str` | `AllplanArch.PlaneReferences | list[AllplanArch.PlaneReferences]` | get the plane references from a string  Args:     value_str: value string  Returns:     value from string |
| `get_value_for_internal_update` | `value_str: str, document: AllplanEleAdapter.DocumentAdapter, pythonpart_element: AllplanEleAdapter.BaseElementAdapter` | `AllplanArch.PlaneReferences | list[AllplanArch.PlaneReferences]` | get the plane references from a string,     called from Allplan after an update of planes  Args:     value_str: value string     document: document      pythonpart_element: pythonpart element  Returns:     value from string |
| `__string_to_plane_references` | `value_str: str, document: AllplanEleAdapter.DocumentAdapter, pythonpart_element: AllplanEleAdapter.BaseElementAdapter` | `AllplanArch.PlaneReferences` | get the plane references from a string  Args:     value_str: value string     document: document     pythonpart_element: pythonpart element  Returns:     value from string |
| `add_to_palette` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the plane controls to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__add_to_palette_planes` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the plane controls to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__add_to_palette_bottom_plane` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the bottom plane controls to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `__add_to_palette_top_plane` | `wpf_palette: WpfPaletteBuilder, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | Add the top plane controls to the palette  Args:     wpf_palette:           WPf palette     prop:                  parameter property     ctrl_props:            control properties     prop_pal_ctrl_service: property palette control service |
| `get_resource_id` | `plane_dependency: AllplanArch.PlaneReferences.PlaneReferenceDependency, at_bottom: bool` | `int` | get the resource ID for the plane dependency  Args:     plane_dependency: plane dependency     at_bottom:        dependency at bottom state  Returns:     resource ID |
| `update_by_constraint` | `build_ele: BuildingElement, prop: ParameterProperty, ctrl_props: ControlProperties, name: str` | `None` | update by a constraint  Args:     build_ele:  building element with the parameter properties     prop:       parameter property to update     ctrl_props: control properties     name:       name of the modified value |
| `enum_to_int_str` | `value: AllplanArch.PlaneReferences.PlaneReferenceDependency` | `str` | convert the plane reference dependency enum to string  Args:     value: plane reference dependency  Returns:     string |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PlaneReferences value type
"""

from __future__ import annotations

import re

from typing import Any, TYPE_CHECKING, cast

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_ArchElements as AllplanArch
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from DocumentManager import DocumentManager
from StringEvaluate import StringEvaluate

from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

from ..ValueTypeUtils.BaseStringToValueConverter import BaseStringToValueConverter
from ..ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ..ParameterPropertyValueType import ParameterPropertyValueType
from ..ValueTypeUtils.StringToValueUtil import StringToValueUtil
from ..ValueTypeUtils.ValueToStringUtil import ValueToStringUtil

if TYPE_CHECKING:
    from BuildingElement import BuildingElement
    from ControlProperties import ControlProperties
    from ParameterProperty import ParameterProperty
    from ..ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

class PlaneReferencesImpl(ParameterPropertyValueType):
    """ implementation of the PlaneReferences value type
    """

    HEIGHT_KEY                  = ".Height"
    ABS_BOTTOM_ELEVATION_KEY    = ".AbsBottomElevation"
    BOTTOM_ELEVATION_KEY        = ".BottomElevation"
    ABS_TOP_ELEVATION_KEY       = ".AbsTopElevation"
    TOP_ELEVATION_KEY           = ".TopElevation"
    BOTTOM_PLANE_DEPENDENCY_KEY = ".BottomPlaneDependency"
    TOP_PLANE_DEPENDENCY_KEY    = ".TopPlaneDependency"

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

        if isinstance(value, str):
            value = PlaneReferencesImpl.get_value(value)

        if name.endswith(PlaneReferencesImpl.HEIGHT_KEY):
            plane_ref = cast(AllplanArch.PlaneReferences, ParameterPropertyListUtil.get_item_value(prop, name))

            plane_ref.Height = value

            return False

        if name.endswith(PlaneReferencesImpl.ABS_BOTTOM_ELEVATION_KEY):
            plane_ref = cast(AllplanArch.PlaneReferences, ParameterPropertyListUtil.get_item_value(prop, name))

            plane_ref.AbsBottomElevation  = value

            return False

        if name.endswith(PlaneReferencesImpl.ABS_TOP_ELEVATION_KEY):
            plane_ref = cast(AllplanArch.PlaneReferences, ParameterPropertyListUtil.get_item_value(prop, name))

            plane_ref.AbsTopElevation = value

            return False

        if name.endswith(PlaneReferencesImpl.BOTTOM_PLANE_DEPENDENCY_KEY):
            plane_ref = cast(AllplanArch.PlaneReferences, ParameterPropertyListUtil.get_item_value(prop, name))

            plane_ref.BottomPlaneDependency = AllplanArch.PlaneReferences.PlaneReferenceDependency.values[value]

            return False

        if name.endswith(PlaneReferencesImpl.TOP_PLANE_DEPENDENCY_KEY):
            plane_ref = cast(AllplanArch.PlaneReferences, ParameterPropertyListUtil.get_item_value(prop, name))

            plane_ref.TopPlaneDependency = AllplanArch.PlaneReferences.PlaneReferenceDependency.values[value]

            return False

        ParameterPropertyListUtil.set_item_value(prop, name, value)

        return True


    @staticmethod
    def to_string(value: str) -> str:
        """ convert the plane references to a string

        Args:
            value: new value

        Returns:
            plane references as string
        """

        return ValueToStringUtil.to_string_strip(value)


    @staticmethod
    def get_value(value_str: str) -> (AllplanArch.PlaneReferences | list[AllplanArch.PlaneReferences]):
        """ get the plane references from a string

        Args:
            value_str: value string

        Returns:
            value from string
        """

        #----------------- default value

        if value_str == "":
            return AllplanArch.PlaneReferences(DocumentManager.get_instance().document,
                                               DocumentManager.get_instance().pythonpart_element)

        return BaseStringToValueConverter.to_value_by_type_converter(
            lambda value_str: PlaneReferencesImpl.__string_to_plane_references(
                value_str,
                DocumentManager.get_instance().document,
                DocumentManager.get_instance().pythonpart_element
            ),
            value_str
        )

    @staticmethod
    def get_value_for_internal_update(value_str: str,
                                      document: AllplanEleAdapter.DocumentAdapter,
                                      pythonpart_element: AllplanEleAdapter.BaseElementAdapter
        ) -> (AllplanArch.PlaneReferences | list[AllplanArch.PlaneReferences]):
        """ get the plane references from a string,
            called from Allplan after an update of planes

        Args:
            value_str: value string
            document: document 
            pythonpart_element: pythonpart element

        Returns:
            value from string
        """

        #----------------- default value

        if value_str == "":
            return AllplanArch.PlaneReferences(document, pythonpart_element)

        return BaseStringToValueConverter.to_value_by_type_converter(
            lambda value_str: PlaneReferencesImpl.__string_to_plane_references(value_str, document, pythonpart_element),
        value_str)


    @staticmethod
    def __string_to_plane_references(value_str: str,
                                     document: AllplanEleAdapter.DocumentAdapter,
                                     pythonpart_element: AllplanEleAdapter.BaseElementAdapter) -> AllplanArch.PlaneReferences:
        """ get the plane references from a string

        Args:
            value_str: value string
            document: document
            pythonpart_element: pythonpart element

        Returns:
            value from string
        """

        value_str_lower = value_str.lower()

        plane_ref = AllplanArch.PlaneReferences(document, pythonpart_element)

        upper_plane = StringToValueUtil.get_property_string(value_str_lower, "upperreferenceplaneid", "")
        lower_plane = StringToValueUtil.get_property_string(value_str_lower, "lowerreferenceplaneid", "")

        plane_ref.TopReferencePlane = AllplanArch.ReferencePlaneID(StringToValueUtil.get_property_guid(upper_plane, "modelguid",
                                                                                        "00000000-0000-0000-0000-000000000000"),
                                                            StringToValueUtil.get_property_int(upper_plane, "planeid", -1))
        plane_ref.BottomReferencePlane = AllplanArch.ReferencePlaneID(StringToValueUtil.get_property_guid(lower_plane, "modelguid",
                                                                                           "00000000-0000-0000-0000-000000000000"),
                                                            StringToValueUtil.get_property_int(lower_plane, "planeid", -1))

        plane_ref_dep = AllplanArch.PlaneReferences.PlaneReferenceDependency

        plane_ref_deps = plane_ref_dep.values.values() # type: ignore

        if (dependency := StringToValueUtil[plane_ref_dep]. \
            get_property_enum(value_str_lower, "bottomdependency", PlaneReferencesImpl.enum_to_int_str(plane_ref_dep.eBottomPlane),
                              plane_ref_deps)) is not None:
            plane_ref.BottomPlaneDependency = dependency

        if (dependency := StringToValueUtil[plane_ref_dep]. \
            get_property_enum(value_str_lower, "topdependency", PlaneReferencesImpl.enum_to_int_str(plane_ref_dep.eTopPlane),
                              plane_ref_deps)) is not None:
            plane_ref.TopPlaneDependency = dependency

        if (dependency := StringToValueUtil[plane_ref_dep]. \
            get_property_enum(value_str, "BottomPlaneDependency", PlaneReferencesImpl.enum_to_int_str((plane_ref.BottomPlaneDependency)),
                              plane_ref_deps)) is not None:
            plane_ref.BottomPlaneDependency = dependency

        if (dependency := StringToValueUtil[plane_ref_dep]. \
            get_property_enum(value_str, "TopPlaneDependency", PlaneReferencesImpl.enum_to_int_str(plane_ref.TopPlaneDependency),
                              plane_ref_deps)) is not None:
            plane_ref.TopPlaneDependency = dependency

        plane_ref.BottomOffset = StringToValueUtil.get_property_float(value_str_lower, "bottomelevation", "0")
        plane_ref.TopOffset    = StringToValueUtil.get_property_float(value_str_lower, "topelevation", "0")

        plane_ref.MaximumHeight = StringToValueUtil.get_property_float(value_str_lower, "maxheight", "0")

        if (height := StringToValueUtil.get_property_float(value_str_lower, "height", "0")):
            plane_ref.Height = height

        return plane_ref


    @staticmethod
    def add_to_palette(wpf_palette          : WpfPaletteBuilder,
                       prop                 : ParameterProperty,
                       ctrl_props           : ControlProperties,
                       prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the plane controls to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        match ctrl_props.value_dialog:
            case "planereferences":
                PlaneReferencesImpl.__add_to_palette_planes(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)

            case "bottomplanereferences":
                PlaneReferencesImpl.__add_to_palette_bottom_plane(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)

            case "topplanereferences":
                PlaneReferencesImpl.__add_to_palette_top_plane(wpf_palette, prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def __add_to_palette_planes(wpf_palette          : WpfPaletteBuilder,
                                prop                 : ParameterProperty,
                                ctrl_props           : ControlProperties,
                                prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the plane controls to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        plane_ref = cast(AllplanArch.PlaneReferences, prop.value)

        row_name = ctrl_props.row_name or ctrl_props.text


        #----------------- create the height control

        if ParameterPropertyValueType.is_visible(prop.name + PlaneReferencesImpl.HEIGHT_KEY, prop_visible_dict):
            height = AllplanArch.BottomTopPlaneService.GetAbsoluteTopElevation(DocumentManager.get_instance().pythonpart_element,
                                                                               DocumentManager.get_instance().document,
                                                                               prop.value) - \
                    AllplanArch.BottomTopPlaneService.GetAbsoluteBottomElevation(DocumentManager.get_instance().pythonpart_element,
                                                                                 DocumentManager.get_instance().document,
                                                                                 prop.value)

            background_color = StringEvaluate.eval_color(ctrl_props.background_color, {})

            wpf_palette.AddLengthValue(ctrl_props.text, prop.name + PlaneReferencesImpl.HEIGHT_KEY, height,
                                       prop_pal_ctrl_service.page_index,
                                       ctrl_props.expander_name, row_name,
                                       prop_pal_ctrl_service.is_sub_control_enabled(ctrl_props, PlaneReferencesImpl.HEIGHT_KEY[1:]),
                                       ctrl_props.min_value, ctrl_props.max_value, 0, False,
                                       ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code,
                                       background_color)


        #----------------- show tbe dependencies

        wpf_palette.AddResourcePicture(ctrl_props.text, prop.name,
                                       PlaneReferencesImpl.get_resource_id(plane_ref.BottomPlaneDependency, True),
                                       prop_pal_ctrl_service.page_index, ctrl_props.expander_name + ctrl_props.expander_state_key,
                                       row_name + ctrl_props.row_state_key,
                                       ctrl_props.height, 20)

        wpf_palette.AddResourcePicture(ctrl_props.text, prop.name,
                                       PlaneReferencesImpl.get_resource_id(plane_ref.TopPlaneDependency, False),
                                       prop_pal_ctrl_service.page_index, ctrl_props.expander_name + ctrl_props.expander_state_key,
                                       row_name + ctrl_props.row_state_key,
                                       ctrl_props.height, 20)


        #----------------- create the dialog button

        wpf_palette.AddButton("...", prop.name + GeneralConstants.DIALOG_BUTTON_KEY,
                              0, prop_pal_ctrl_service.page_index,
                              ctrl_props.expander_name, row_name,
                              prop_pal_ctrl_service.is_sub_control_enabled(ctrl_props, ""),
                              ctrl_props.height, 20,
                              ctrl_props.font_style, ctrl_props.font_face_code)


    @staticmethod
    def __add_to_palette_bottom_plane(wpf_palette          : WpfPaletteBuilder,
                                      prop                 : ParameterProperty,
                                      ctrl_props           : ControlProperties,
                                      prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the bottom plane controls to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        plane_ref = cast(AllplanArch.PlaneReferences, prop.value)

        row_name = ctrl_props.row_name or ctrl_props.text


        #----------------- create the height control

        if ParameterPropertyValueType.is_visible(prop.name + PlaneReferencesImpl.ABS_BOTTOM_ELEVATION_KEY, prop_visible_dict):
            bottom = AllplanArch.BottomTopPlaneService.GetAbsoluteBottomElevation(DocumentManager.get_instance().pythonpart_element,
                                                                                  DocumentManager.get_instance().document,
                                                                                  prop.value)

            background_color = StringEvaluate.eval_color(ctrl_props.background_color, {})

            wpf_palette.AddLengthValue(ctrl_props.text, prop.name + PlaneReferencesImpl.ABS_BOTTOM_ELEVATION_KEY, bottom,
                                       prop_pal_ctrl_service.page_index,
                                       ctrl_props.expander_name, row_name,
                                       prop_pal_ctrl_service.is_sub_control_enabled(ctrl_props,
                                                                                    PlaneReferencesImpl.ABS_BOTTOM_ELEVATION_KEY[1:]),
                                       ctrl_props.min_value, ctrl_props.max_value, 0, False,
                                       ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code,
                                       background_color)


        #----------------- show tbe dependencies

        wpf_palette.AddResourcePicture(ctrl_props.text, prop.name,
                                       PlaneReferencesImpl.get_resource_id(plane_ref.BottomPlaneDependency, True),
                                       prop_pal_ctrl_service.page_index, ctrl_props.expander_name + ctrl_props.expander_state_key,
                                       row_name + ctrl_props.row_state_key,
                                       ctrl_props.height, 20)


        #----------------- create the dialog button

        wpf_palette.AddButton("...", prop.name + GeneralConstants.DIALOG_BUTTON_KEY,
                              0, prop_pal_ctrl_service.page_index,
                              ctrl_props.expander_name, row_name,
                              prop_pal_ctrl_service.is_sub_control_enabled(ctrl_props, ""),
                              ctrl_props.height, 20,
                              ctrl_props.font_style, ctrl_props.font_face_code)




    @staticmethod
    def __add_to_palette_top_plane(wpf_palette          : WpfPaletteBuilder,
                                   prop                 : ParameterProperty,
                                   ctrl_props           : ControlProperties,
                                   prop_pal_ctrl_service: PropertyPaletteControlService):
        """ Add the top plane controls to the palette

        Args:
            wpf_palette:           WPf palette
            prop:                  parameter property
            ctrl_props:            control properties
            prop_pal_ctrl_service: property palette control service
        """

        prop_visible_dict = ConditionUtil.get_condition_dict(ctrl_props.visible_condition, prop.name, prop_pal_ctrl_service.param_dict)

        plane_ref = cast(AllplanArch.PlaneReferences, prop.value)

        row_name = ctrl_props.row_name or ctrl_props.text


        #----------------- create the height control

        if ParameterPropertyValueType.is_visible(prop.name + PlaneReferencesImpl.ABS_TOP_ELEVATION_KEY, prop_visible_dict):
            top = AllplanArch.BottomTopPlaneService.GetAbsoluteTopElevation(DocumentManager.get_instance().pythonpart_element,
                                                                            DocumentManager.get_instance().document,
                                                                            prop.value)

            background_color = StringEvaluate.eval_color(ctrl_props.background_color, {})

            wpf_palette.AddLengthValue(ctrl_props.text, prop.name + PlaneReferencesImpl.ABS_TOP_ELEVATION_KEY, top,
                                       prop_pal_ctrl_service.page_index,
                                       ctrl_props.expander_name, row_name,
                                       prop_pal_ctrl_service.is_sub_control_enabled(ctrl_props,
                                                                                    PlaneReferencesImpl.ABS_TOP_ELEVATION_KEY[1:]),
                                       ctrl_props.min_value, ctrl_props.max_value, 0, False,
                                       ctrl_props.height, ctrl_props.width, ctrl_props.font_face_code,
                                       background_color)


        #----------------- show tbe dependencies

        wpf_palette.AddResourcePicture(ctrl_props.text, prop.name,
                                       PlaneReferencesImpl.get_resource_id(plane_ref.TopPlaneDependency, False),
                                       prop_pal_ctrl_service.page_index, ctrl_props.expander_name + ctrl_props.expander_state_key,
                                       row_name + ctrl_props.row_state_key,
                                       ctrl_props.height, 20)


        #----------------- create the dialog button

        wpf_palette.AddButton("...", prop.name + GeneralConstants.DIALOG_BUTTON_KEY,
                              0, prop_pal_ctrl_service.page_index,
                              ctrl_props.expander_name, row_name,
                              prop_pal_ctrl_service.is_sub_control_enabled(ctrl_props, ""),
                              ctrl_props.height, 20,
                              ctrl_props.font_style, ctrl_props.font_face_code)


    @staticmethod
    def get_resource_id(plane_dependency: AllplanArch.PlaneReferences.PlaneReferenceDependency,
                        at_bottom       : bool) -> int:
        """ get the resource ID for the plane dependency

        Args:
            plane_dependency: plane dependency
            at_bottom:        dependency at bottom state

        Returns:
            resource ID
        """

        match plane_dependency:
            case AllplanArch.PlaneReferences.PlaneReferenceDependency.eBottomPlane:
                return int(AllplanSettings.PictResPlaneReferences.eBottomPlane if at_bottom else \
                           AllplanSettings.PictResPlaneReferences.eBottomPlaneFromTop) # type: ignore

            case AllplanArch.PlaneReferences.PlaneReferenceDependency.eTopPlane:
                return int(AllplanSettings.PictResPlaneReferences.eTopPlaneFromBottom if at_bottom else \
                           AllplanSettings.PictResPlaneReferences.eTopPlane) # type: ignore

            case AllplanArch.PlaneReferences.PlaneReferenceDependency.eAbsElevation:
                return int(AllplanSettings.PictResPlaneReferences.eAbsElevationBottom if at_bottom else \
                           AllplanSettings.PictResPlaneReferences.eAbsElevationTop) # type: ignore

            case  AllplanArch.PlaneReferences.PlaneReferenceDependency.eComponentsTopPlane | \
                  AllplanArch.PlaneReferences.PlaneReferenceDependency.eComponentsBottomPlane:
                return int(AllplanSettings.PictResPlaneReferences.eComponentsBottomPlane if at_bottom else \
                           AllplanSettings.PictResPlaneReferences.eComponentsTopPlane) # type: ignore

            case _:
                return int(AllplanSettings.PictResPlaneReferences.eBottomFixed if at_bottom else \
                           AllplanSettings.PictResPlaneReferences.eTopFixed) # type: ignore


    @staticmethod
    def update_by_constraint(build_ele : BuildingElement,
                             prop      : ParameterProperty,
                             ctrl_props: ControlProperties,
                             name      : str):
        """ update by a constraint

        Args:
            build_ele:  building element with the parameter properties
            prop:       parameter property to update
            ctrl_props: control properties
            name:       name of the modified value
        """

        for constraint in ctrl_props.constraint:
            if not constraint:
                continue

            key, _, from_value = constraint.partition("=")

            if not from_value:
                if not re.search(fr"\b{name}\b",  key):
                    continue

                StringEvaluate.exec_function_string(f"{prop.name}{PlaneReferencesImpl.HEIGHT_KEY} = {constraint}",
                                                    StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0]))

            else:
                if not re.search(fr"\b{name}\b",  from_value):
                    continue

                StringEvaluate.exec_function_string(f"{prop.name}.{constraint}",
                                                    StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0]))

    @staticmethod
    def enum_to_int_str(value: AllplanArch.PlaneReferences.PlaneReferenceDependency) -> str:
        """ convert the plane reference dependency enum to string

        Args:
            value: plane reference dependency

        Returns:
            string
        """

        return str(int(AllplanArch.PlaneReferences.PlaneReferenceDependency.values[value])) # type: ignore

```

</details>