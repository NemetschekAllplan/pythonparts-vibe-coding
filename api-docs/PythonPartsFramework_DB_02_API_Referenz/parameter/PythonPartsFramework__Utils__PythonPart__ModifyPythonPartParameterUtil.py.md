---
title: "ModifyPythonPartParameterUtil"
source: "PythonPartsFramework\Utils\PythonPart\ModifyPythonPartParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ModifyPythonPartParameterUtil

> **Pfad:** `PythonPartsFramework\Utils\PythonPart\ModifyPythonPartParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the utility class for the PythonPart parameter modification

## Abhängigkeiten

- `BuildingElementInput`
- `BuildingElementMaterialStringTable`
- `BuildingElementStringTable`
- `ControlProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `Palette.PaletteData`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `StringToValueConverter`
- `TypeCollections.ModificationElementList`
- `TypeCollections.ParameterValueList`
- `Utilities.GeneralConstants`
- `Utils.PythonPart.PythonPartParameterDataUtil`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ValueTypeUtils.ParameterPropertyListUtil`
- `ValueTypes.ValueTypeUtils.PropertyPaletteControlService`
- `dataclasses`
- `typing`

## Klassen

### `ModifiedParameterData`

data for a modified parameter
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ModifyPythonPartParameterUtil`

implementation of the utility class for the PythonPart parameter modification
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `execute` | `python_part: AllplanEleAdapter.BaseElementAdapter, coord_input: AllplanIFWInput.CoordinateInput, mod_param_data: list[ModifiedParameterData]` | `None` | execute the parameter modification  Args:     python_part:    PythonPart to modify     coord_input:    API object for the coordinate input, element selection, ... in the Allplan view     mod_param_data: data of the modified parameter |
| `get_overtake_parameters` | `python_part_ele: AllplanEleAdapter.BaseElementAdapter, str_table: BuildingElementStringTable, material_str_table: BuildingElementMaterialStringTable` | `list[ModifiedParameterData]` | get the overtake parameters  Args:     python_part_ele:    PythonPart element     str_table:          global string table     material_str_table: global material string table  Returns:     overtake parameter |
| `get_modified_parameters` | `old_parameter: list[str], python_part_ele: AllplanEleAdapter.BaseElementAdapter, str_table: BuildingElementStringTable, material_str_table: BuildingElementMaterialStringTable` | `list[ModifiedParameterData]` | get the modified parameters  Args:     old_parameter:      old parameter     python_part_ele:    PythonPart element     str_table:          global string table     material_str_table: global material string table  Returns:     returns |
| `__get_modified_parameter` | `old_value: str, new_value: str, prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService, build_ele_str_table: BuildingElementStringTable` | `list[ModifiedParameterData]` | get the modified parameter  Args:     old_value:             old value string     new_value:             new value string     prop:                  parameter property     ctrl_props:            controls properties     prop_pal_ctrl_service: property palette control service     build_ele_str_table:   building element string table  Returns:     modified parameter data |
| `__add_parameter` | `new_parameter: ParameterValueData, prop: ParameterProperty, mod_param_data: list[ModifiedParameterData]` | `None` | add the parameter  Args:     new_parameter:  new parameter     prop:           parameter property     mod_param_data: data of the modified parameter |
| `__add_to_palette` | `prop: ParameterProperty, ctrl_props: ControlProperties, prop_pal_ctrl_service: PropertyPaletteControlService, parameter_data: ParameterValueList` | `None` | function description  Args:     prop:                  parameter property     ctrl_props:            controls properties     prop_pal_ctrl_service: property palette control service     parameter_data:        parameter data |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the utility class for the PythonPart parameter modification
"""

from typing import cast, Any

from dataclasses import dataclass

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFWInput

from BuildingElementInput import BuildingElementInput
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate
from StringToValueConverter import StringToValueConverter

from Palette.PaletteData import PaletteData
from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from Utilities.GeneralConstants import GeneralConstants

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

from ValueTypes.ValueTypeUtils.ParameterPropertyListUtil import ParameterPropertyListUtil
from ValueTypes.ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

from TypeCollections.ModificationElementList import ModificationElementList
from TypeCollections.ParameterValueList import ParameterValueList, ParameterValueData

from Utils.PythonPart.PythonPartParameterDataUtil import PythonPartParameterDataUtil

@dataclass
class ModifiedParameterData:
    """ data for a modified parameter
    """

    name : str = ""
    value: Any = None


class ModifyPythonPartParameterUtil():
    """ implementation of the utility class for the PythonPart parameter modification
    """

    @staticmethod
    def execute(python_part   : AllplanEleAdapter.BaseElementAdapter,
                coord_input   : AllplanIFWInput.CoordinateInput,
                mod_param_data: list[ModifiedParameterData]):
        """ execute the parameter modification

        Args:
            python_part:    PythonPart to modify
            coord_input:    API object for the coordinate input, element selection, ... in the Allplan view
            mod_param_data: data of the modified parameter
        """

        py_path = fr"{AllplanSettings.AllplanPaths.GetPythonPartsEtcPath()}PythonPartsFramework\GeneralScripts"

        build_ele_input = BuildingElementInput(coord_input, py_path)


        #----------------- execute the modification

        _, pyp_path, parameter = AllplanBaseEle.PythonPartService.GetParameter(python_part)

        _, placement_matrix = AllplanBaseEle.PythonPartService.GetPlacementMatrix(python_part)

        build_ele_input.start_input(pyp_path, parameter, None, ModificationElementList([python_part]),
                                    placement_matrix, AllplanGeo.Matrix3D(), AllplanEleAdapter.BaseElementAdapter(),
                                    AllplanSettings.ExecutionEvent.eConnection)

        for param in mod_param_data:
            build_ele_input.modify_element_property(0, param.name, param.value)

        build_ele_input.on_cancel_function()


    @staticmethod
    def get_overtake_parameters(python_part_ele   : AllplanEleAdapter.BaseElementAdapter,
                                str_table         : BuildingElementStringTable,
                                material_str_table: BuildingElementMaterialStringTable) -> list[ModifiedParameterData]:
        """ get the overtake parameters

        Args:
            python_part_ele:    PythonPart element
            str_table:          global string table
            material_str_table: global material string table

        Returns:
            overtake parameter
        """

        build_ele_list, build_ele_ctrl_props_list = PythonPartParameterDataUtil.get_data(python_part_ele,
                                                                                         str_table, material_str_table)

        _, _, new_parameter = AllplanBaseEle.PythonPartService.GetParameter(python_part_ele)

        overtake_param_data = []

        for param in new_parameter:
            name, _, value = param.partition("=")

            if (build_ele_index := next((index for index, item in enumerate(build_ele_list) \
                                         if item.get_property(name) is not None), None)) is None:
                continue

            if (ctrl_props := build_ele_ctrl_props_list[build_ele_index].get_property(name)) is None:
                continue

            build_ele = build_ele_list[build_ele_index]

            if build_ele.get_pages()[ctrl_props.page].name != GeneralConstants.HIDDEN_PAGE_KEY:
                prop = build_ele.get_existing_property(name)

                if prop.value_type != ParameterPropertyValueTypes.RADIO_BUTTON:
                    overtake_param_data.append(ModifiedParameterData(name,
                                                                     prop.value_type.get_value_extend(value.strip(),
                                                                                                      prop.attribute_id,
                                                                                                      build_ele.get_string_tables()[0])))

        return overtake_param_data


    @staticmethod
    def get_modified_parameters(old_parameter     : list[str],
                                python_part_ele   : AllplanEleAdapter.BaseElementAdapter,
                                str_table         : BuildingElementStringTable,
                                material_str_table: BuildingElementMaterialStringTable) -> list[ModifiedParameterData]:
        """ get the modified parameters

        Args:
            old_parameter:      old parameter
            python_part_ele:    PythonPart element
            str_table:          global string table
            material_str_table: global material string table

        Returns:
            returns
        """

        build_ele_list, build_ele_ctrl_props_list = PythonPartParameterDataUtil.get_data(python_part_ele,
                                                                                         str_table, material_str_table)

        _, _, new_parameter = AllplanBaseEle.PythonPartService.GetParameter(python_part_ele)

        mod_param_data = []


        #----------------- get the modified parameter

        for old_param, new_param in zip(old_parameter, new_parameter):
            if old_param != new_param:
                name, _, old_value = old_param.partition("=")

                name = name.lstrip("<").rstrip(">")

                build_ele  = next((item for item in build_ele_list if item.get_property(name) is not None), None)
                ctrl_props = next((item.get_property(name) for item in build_ele_ctrl_props_list
                                                           if item.get_property(name) is not None), None)

                if build_ele is None or ctrl_props is None:
                    continue

                param_dict = StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0])

                prop_pal_ctrl_service = PropertyPaletteControlService(PaletteData("", param_dict, 1, "", build_ele.get_string_tables()[1],
                                                                                  build_ele, -1, False))

                mod_param_data += ModifyPythonPartParameterUtil.__get_modified_parameter(old_value.rstrip(),
                                                                                         new_param.split("=", 1)[-1].rstrip(),
                                                                                         build_ele.get_existing_property(name), ctrl_props,
                                                                                         prop_pal_ctrl_service,
                                                                                         build_ele_list[0].get_string_tables()[0])

        return mod_param_data


    @staticmethod
    def __get_modified_parameter(old_value            : str,
                                 new_value            : str,
                                 prop                 : ParameterProperty,
                                 ctrl_props           : ControlProperties,
                                 prop_pal_ctrl_service: PropertyPaletteControlService,
                                 build_ele_str_table  : BuildingElementStringTable) -> list[ModifiedParameterData]:
        """ get the modified parameter

        Args:
            old_value:             old value string
            new_value:             new value string
            prop:                  parameter property
            ctrl_props:            controls properties
            prop_pal_ctrl_service: property palette control service
            build_ele_str_table:   building element string table

        Returns:
            modified parameter data
        """

        #----------------- get the old parameter data

        old_parameter_data = ParameterValueList()

        old_value = StringToValueConverter.get_value(prop.value_type, old_value, build_ele_str_table, prop.attribute_id)

        prop.value = old_value

        ModifyPythonPartParameterUtil.__add_to_palette(prop, ctrl_props, prop_pal_ctrl_service, old_parameter_data)


        #----------------- get the new parameter data

        new_parameter_data = ParameterValueList()

        prop.value = StringToValueConverter.get_value(prop.value_type, new_value, build_ele_str_table, prop.attribute_id)

        ModifyPythonPartParameterUtil.__add_to_palette(prop, ctrl_props, prop_pal_ctrl_service, new_parameter_data)


        #----------------- get the modified parameter data

        mod_param_data : list[ModifiedParameterData] = []

        for new_parameter in new_parameter_data:

            #------------- append a new parameter

            if (old_parameter := next((item for item in old_parameter_data if item.name == new_parameter.name), None)) is None:
                ModifyPythonPartParameterUtil.__add_parameter(new_parameter, prop, mod_param_data)
                continue


            #------------- modify the old parameter

            if new_parameter.value != old_parameter.value:
                if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE:
                    ModifyPythonPartParameterUtil.__add_parameter(new_parameter, prop, mod_param_data)
                else:
                    mod_param_data.append(ModifiedParameterData(new_parameter.name, new_parameter.value))

        return mod_param_data


    @staticmethod
    def __add_parameter(new_parameter : ParameterValueData,
                        prop          : ParameterProperty,
                        mod_param_data: list[ModifiedParameterData]):
        """ add the parameter

        Args:
            new_parameter:  new parameter
            prop:           parameter property
            mod_param_data: data of the modified parameter
        """

        if (list_index := ParameterPropertyListUtil.get_list_index(new_parameter.name)) is not None:
            mod_param_data.append(ModifiedParameterData(new_parameter.name, prop.value[list_index]))
        else:
            mod_param_data.append(ModifiedParameterData(new_parameter.name, new_parameter.value))


    @staticmethod
    def __add_to_palette(prop                 : ParameterProperty,
                         ctrl_props           : ControlProperties,
                         prop_pal_ctrl_service: PropertyPaletteControlService,
                         parameter_data       : ParameterValueList):
        """ function description

        Args:
            prop:                  parameter property
            ctrl_props:            controls properties
            prop_pal_ctrl_service: property palette control service
            parameter_data:        parameter data
        """

        if isinstance(prop.value, list):
            for index, value in enumerate(prop.value):
                list_prop = prop.deep_copy()

                list_prop.value = value
                list_prop.name  = f"{prop.name}[{index}]"

                prop.value_type.add_to_palette(cast(WpfPaletteBuilder, parameter_data),
                                               list_prop, ctrl_props, prop_pal_ctrl_service)
        else:
            prop.value_type.add_to_palette(cast(WpfPaletteBuilder, parameter_data),
                                        prop, ctrl_props, prop_pal_ctrl_service)

```

</details>