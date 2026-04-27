---
title: "BuildingElementCompositeCreator"
source: "PythonPartsFramework\GeneralScripts\BuildingElementCompositeCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementCompositeCreator

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementCompositeCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the build element composite creator

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementCompositeData`
- `BuildingElementCompositeReader`
- `BuildingElementControlProperties`
- `BuildingElementConverterUtil`
- `BuildingElementListUtil`
- `BuildingElementMaterialStringTable`
- `BuildingElementParameterPropertyUtil`
- `BuildingElementStringTable`
- `BuildingElementSubElementUtil`
- `BuildingElementTupleUtil`
- `BuildingElementUtil`
- `BuildingElementXML`
- `BuildingElementXMLInclude`
- `ControlProperties`
- `FileNameService`
- `NemAll_Python_Geometry`
- `NemAll_Python_Reinforcement`
- `ParameterProperty`
- `StringTableService`
- `StringToValueConverter`
- `ValueTypeUtil`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.ValueTypeUtils.ValueListValidator`
- `XMLReader.XmlElementTreeUtil`
- `collections`
- `os`
- `traceback`

## Klassen

### `BuildingElementCompositeCreator`

Implementation of class BuildingElementCompositeCreator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `read_data_from_pyp` | `composite_data: BuildingElementCompositeData, pyp_filename: str, build_ele_str_table: BuildingElementStringTable, is_node_script: bool, version: float` | `None` | Read the data from the pyp file  Args:     composite_data:      composite data     pyp_filename:        Name of the pyp file     build_ele_str_table: string table of the building element     is_node_script:      is node script state     version:             version |
| `create_building_element_list` | `composite_data: BuildingElementCompositeData, build_ele_list: list[BuildingElement], build_ele_ctrl_props_list: list[BuildingElementControlProperties], pyp_file_name: str, str_table: BuildingElementStringTable, material_str_table: BuildingElementMaterialStringTable, check_migration: bool` | `bool` | create the list of the building elements from the sub element list  Args:     composite_data:            composite data     build_ele_list:            list with the building elements     build_ele_ctrl_props_list: list with the building element control properties     pyp_file_name:             Full name of the pyp file     str_table:                 String table     material_str_table:        Material string table     check_migration:           check migration state  Returns:     create list state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the build element composite creator
"""

# pylint: disable=bare-except

import os
import traceback

from collections import Counter

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

import BuildingElementParameterPropertyUtil as PropertyUtil

from BuildingElementCompositeData import BuildingElementCompositeData
from BuildingElement import BuildingElement
from BuildingElementCompositeReader import BuildingElementCompositeReader
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementConverterUtil import BuildingElementConverterUtil
from BuildingElementListUtil import BuildingElementListUtil
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementSubElementUtil import BuildingElementSubElementUtil
from BuildingElementTupleUtil import BuildingElementTupleUtil
from BuildingElementStringTable import BuildingElementStringTable
from BuildingElementUtil import BuildingElementUtil
from BuildingElementXML import BuildingElementXML
from BuildingElementXMLInclude import BuildingElementXMLInclude
from ControlProperties import ControlProperties
from FileNameService import FileNameService
from ParameterProperty import ParameterProperty
from StringTableService import StringTableService
from StringToValueConverter import StringToValueConverter
from ValueTypeUtil import ValueTypeUtil

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl
from ValueTypes.ValueTypeUtils.ValueListValidator import ValueListValidator

from XMLReader.XmlElementTreeUtil import XmlElementTreeUtil

class BuildingElementCompositeCreator:
    """ Implementation of class BuildingElementCompositeCreator
    """

    @staticmethod
    def read_data_from_pyp(composite_data     : BuildingElementCompositeData,
                           pyp_filename       : str,
                           build_ele_str_table: BuildingElementStringTable,
                           is_node_script     : bool,
                           version            : float):
        """ Read the data from the pyp file

        Args:
            composite_data:      composite data
            pyp_filename:        Name of the pyp file
            build_ele_str_table: string table of the building element
            is_node_script:      is node script state
            version:             version
        """

        new_pyp_filename = pyp_filename if is_node_script else BuildingElementXMLInclude.get_final_pyp_file(pyp_filename)

        doc_ele = XmlElementTreeUtil.parse(new_pyp_filename)

        BuildingElementCompositeReader.read_property_palette_layout(doc_ele, build_ele_str_table,
                                                                    composite_data.sub_ele_palette_data)

        BuildingElementCompositeReader.read_data_from_pyp(doc_ele, is_node_script, version,
                                                          composite_data)


    @staticmethod
    def create_building_element_list(composite_data           : BuildingElementCompositeData,
                                     build_ele_list           : list[BuildingElement],
                                     build_ele_ctrl_props_list: list[BuildingElementControlProperties],
                                     pyp_file_name            : str,
                                     str_table                : BuildingElementStringTable,
                                     material_str_table       : BuildingElementMaterialStringTable,
                                     check_migration          : bool) -> bool:
        """ create the list of the building elements from the sub element list

        Args:
            composite_data:            composite data
            build_ele_list:            list with the building elements
            build_ele_ctrl_props_list: list with the building element control properties
            pyp_file_name:             Full name of the pyp file
            str_table:                 String table
            material_str_table:        Material string table
            check_migration:           check migration state

        Returns:
            create list state
        """

        build_ele_str_table = build_ele_list[0].get_string_tables()[0]


        #----------------- read the building elements and set the data

        param_dict = {"build_ele_list" : build_ele_list, "AllplanGeo" : AllplanGeo}

        script_data_dict = {}
        name_counter     = Counter()

        for sub_ele_script_name in composite_data.sub_ele_script_name:
            name_counter.update((sub_ele_script_name,))

        for sub_ele_id, sub_ele_script_name, sub_ele_visible, sub_ele_defaults, \
            sub_ele_constraints, sub_ele_page_index, sub_ele_script_uuid in zip(composite_data.sub_ele_id,
                                                                                composite_data.sub_ele_script_name,
                                                                                composite_data.sub_ele_visible,
                                                                                composite_data.sub_ele_defaults,
                                                                                composite_data.sub_ele_constraints,
                                                                                composite_data.sub_ele_page_index,
                                                                                composite_data.sub_ele_script_uuid):
            xml_ele = BuildingElementXML()

            file_name = BuildingElementSubElementUtil.get_file_name(pyp_file_name, sub_ele_script_name, False)

            try:                                                    # pylint: disable=too-many-try-statements
                if file_name in script_data_dict:
                    script_data = script_data_dict[file_name]

                    if name_counter[sub_ele_script_name] > 1:
                        build_ele     = script_data[0].deep_copy()
                        control_props = [prop.deep_copy() for prop in script_data[1]]
                    else:
                        build_ele     = script_data[0]
                        control_props = script_data[1]

                else:
                    build_ele, control_props, _ = xml_ele.read_element_parameter(file_name, str_table, material_str_table)

                    try:                                            # pylint: disable=too-many-try-statements
                        if name_counter[sub_ele_script_name] > 1:
                            script_data_dict[file_name] = (build_ele.deep_copy(), [prop.deep_copy() for prop in control_props])

                    except:
                        traceback.print_exc()
                        return True

                name_counter.subtract((sub_ele_script_name, ))

            except:
                if not check_migration:
                    traceback.print_exc()

                return False

            if sub_ele_script_uuid != build_ele.script_uuid:
                return False

            build_ele.pyp_file_name = (FileNameService.get_lib_pyp_sricpt_path(file_name))
            build_ele.element_id    = sub_ele_id + "___"

            if not build_ele.script_name:
                build_ele.script_name = "[" + sub_ele_script_name + "]"


            #----------------- Set the default values

            control_prop_name_dict = {PropertyUtil.get_property_value_name(prop.value_name) : \
                                      prop for prop in control_props if prop.control_type == ControlProperties.ControlType.CONTROL}

            for sub_ele_default in sub_ele_defaults:
                value_name = PropertyUtil.get_property_value_name(sub_ele_default.name)

                if (prop := build_ele.get_property(value_name)) is None:
                    continue

                control_prop = control_prop_name_dict[value_name]


                #----------------- set the value

                if sub_ele_default.value:
                    if "."in sub_ele_default.name:
                        PropertyUtil.set_property_value(prop, sub_ele_default.name, float(sub_ele_default.value))

                    elif (conv := BuildingElementConverterUtil.get_string_to_value_converter(prop.value_type)):
                        prop.value = StringToValueConverter.to_value_by_type_converter(conv, sub_ele_default.value)

                    elif prop.value_type.is_tuple_type():
                        if "object" in prop.value_type:
                            prop.value = sub_ele_default.value
                        else:
                            prop.value = BuildingElementTupleUtil.get_tuple_element_list(sub_ele_default.value, prop.value_type,
                                                                                         prop.named_tuple_def)

                    elif prop.value_type in (ParameterPropertyValueTypes.ANY_VALUE_BY_TYPE,
                                             ParameterPropertyValueTypes.FIXTURE,
                                             ParameterPropertyValueTypes.REINFORCEMENT_SHAPE_BAR_PROPERTIES,
                                             ParameterPropertyValueTypes.REINFORCEMENT_SHAPE_MESH_PROPERTIES):
                        prop.value = prop.value_type.get_value(sub_ele_default.value)

                    else:
                        value_type = prop.value_type

                        if ValueTypeUtil.is_combobox_with_string_input(value_type):
                            if sub_ele_default.value.startswith("["):
                                new_value = sub_ele_default.value[1:-1].split(";")
                            else:
                                text_id = sub_ele_default.value
                                no_localization_value = ValueListValidator.get_value_by_text_id(control_prop, text_id)
                                new_value = StringTableService.get_string_table_entry(build_ele.get_string_tables()[0], text_id,
                                                                                      no_localization_value if no_localization_value is not None else sub_ele_default.value)

                        elif value_type == ParameterPropertyValueTypes.DISPLAY_TEXT:
                            new_value = StringTableService.get_string_table_entry(build_ele_str_table, "", sub_ele_default.value)

                        elif ValueTypeUtil.is_string_input(value_type):
                            if sub_ele_default.value.startswith("["):
                                new_value = BuildingElementListUtil.get_list_element(
                                                sub_ele_default.value,
                                                ParameterPropertyValueTypesImpl.get_value_type_impl("string"), None)
                            else:
                                new_value = sub_ele_default.value

                        elif value_type == "picture":
                            new_value = os.path.dirname(pyp_file_name) + "\\" + sub_ele_default.value


                        #------------------ set the value by the formula, simple value or geometry object

                        else:
                            if (formula := BuildingElementCompositeReader.create_constraint_formula(composite_data.sub_ele_id,
                                                                                                    sub_ele_default.value)) != sub_ele_default.value:
                                if formula.startswith("["):
                                    formula = formula.replace(";", ",")

                                new_value = eval(formula, param_dict)

                            else:
                                new_value = prop.value_type.get_value(sub_ele_default.value)

                        if prop.value_type == "reinfbardiameter":
                            new_value = AllplanReinf.ReinforcementSettings.CheckBarDiameter(new_value)

                        prop.value = new_value


                        #----------------- set the persistent state

                    if prop.persistent != ParameterProperty.Persistent.NO and \
                       (sub_ele_default.visible == "False" or sub_ele_visible == "False"):
                        prop.persistent = ParameterProperty.Persistent.MODEL


                #----------------- set the list states

                if sub_ele_default.list_state is not None:
                    prop.list_state = sub_ele_default.list_state

                if sub_ele_default.list_reverse is not None:
                    prop.list_reverse = sub_ele_default.list_reverse

                if sub_ele_default.list_squeeze is not None:
                    prop.list_squeeze = sub_ele_default.list_squeeze


                #----------------- set the data of the controls

                if sub_ele_default.visible:
                    control_prop.set_visible_condition(sub_ele_default.name, sub_ele_default.visible)

                if sub_ele_default.text:
                    if prop.value_type == ParameterPropertyValueTypes.RADIO_BUTTON_GROUP:
                        control_prop.group_text = StringTableService.get_string_table_entry(build_ele_str_table, "",
                                                                                            sub_ele_default.text.replace("\"", ""))

                    elif prop.value_type == ParameterPropertyValueTypes.DISPLAY_TEXT:
                        prop.value = StringTableService.get_string_table_entry(build_ele_str_table, "",
                                                                               sub_ele_default.text.replace("\"", ""))

                    else:
                        if prop.value_type == "radiobutton" and sub_ele_default.text.startswith("_ {"):
                            control_prop.set_visible_condition(sub_ele_default.name, "False")

                        default_name = sub_ele_default.name
                        default_text = StringTableService.get_string_table_entry(build_ele_str_table, "",
                                                                                 sub_ele_default.text.replace("\"", ""))

                        if default_name.find(".") != -1:
                            control_prop.set_member_text(default_name, default_text)
                        else:
                            control_prop.text = default_text


            #----------------- Set the states by the constraints

            for constraint in sub_ele_constraints:

                #----------------- set the visible and enable condition

                if (value_name := PropertyUtil.get_property_value_name(constraint.name))in control_prop_name_dict:
                    control_prop = control_prop_name_dict[value_name]

                    if constraint.visible:
                        control_prop.set_visible_condition(constraint.name, constraint.visible)

                    if constraint.condition == "True"  and  constraint.visible != "False":
                        control_prop.enable_condition = "False"


                #----------------- set the list states

                prop = build_ele.get_existing_property(value_name)

                if constraint.list_state is not None:
                    prop.list_state = constraint.list_state

                if constraint.list_reverse is not None:
                    prop.list_reverse = constraint.list_reverse


                #----------------- set the value type when $dynamic

                if prop and prop.value_type == "$dynamic":
                    value_types = eval(constraint.value_type)

                    if isinstance(value_types, list):
                        prop.value_type = value_types[0]
                    else:
                        prop.value_type = value_types

                else:
                    constraint.value_type = ""


            #----------------- set the general data

            page_index = sub_ele_page_index - 1

            page_data = build_ele.get_pages()

            def is_visible_page(page_name: str) -> bool:
                """ get the visible page state

                Args:
                    page_name: page name

                Returns:
                    visible page state
                """
                return not page_name in ("__IN_MANDATORY__", "__IN__", "__OUT__", "__IN_OUT__", "__IN_OPTIONAL__")

            page_control_props = BuildingElementControlProperties([control_prop for control_prop in control_props \
                                                                  if is_visible_page(page_data[control_prop.page].name) and \
                                                                     page_index in [-1, control_prop.page]])

            build_ele_list.append(build_ele)
            build_ele_ctrl_props_list.append(page_control_props)

            script = BuildingElementUtil.import_building_element_script(build_ele, True)

            composite_data.sub_ele_script.append(script)

        return True

```

</details>