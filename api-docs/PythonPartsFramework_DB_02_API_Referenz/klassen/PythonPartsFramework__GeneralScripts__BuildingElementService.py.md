---
title: "BuildingElementService"
source: "PythonPartsFramework\GeneralScripts\BuildingElementService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementService

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the build element service

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementComposite`
- `BuildingElementCompositeCreator`
- `BuildingElementControlProperties`
- `BuildingElementListService`
- `BuildingElementMaterialStringTable`
- `BuildingElementStringTable`
- `BuildingElementSubElementUtil`
- `BuildingElementUtil`
- `BuildingElementValueConstraint`
- `BuildingElementXML`
- `FileNameService`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Utility`
- `TraceService`
- `ntpath`
- `os`
- `os.path`
- `types`
- `typing`

## Klassen

### `BuildingElementService`

Definition of class BuildingElementService
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `read_data_from_pyp` | `file_name: str, str_table: BuildingElementStringTable, is_library_preview: bool, material_str_table: BuildingElementMaterialStringTable, sub_file_name: str='', init_with_last_input: bool=True, add_sub_file_name: str=''` | `Tuple[Optional[bool], Optional[ModuleType], List[BuildingElement], List[BuildingElementControlProperties], BuildingElementComposite, str, str]` | Read the data from the pyp file and check the version  Args:     file_name:              Name of the pyp file     str_table:              String table     is_library_preview:     Called for library preview     material_str_table:     Material string table     sub_file_name:          File with the sub elements     init_with_last_input:   Initialize with the data from the last input (only if ReadLastInput is set in the script)     add_sub_file_name:      additional sub file  Returns:     True, if import was successful, False otherwise     Python module representing the PythonPart script (.py file)     List with BuildingElement objects containing parameter values     List with Control properties     Building element composite object     Base name the .pyp file (without the directory path and the '.pyp' extension)     Absolute path of the .pyp file |
| `read_build_ele_from_pyp` | `file_name: str` | `tuple[bool, ModuleType | None, BuildingElement | None]` | Create BuildingElement and python module based on .pyp file  This method gets only the BuildingElement and the python module of the script, the .pyp file refers to. The resulting BuildingElement contains parameters with their default values.  Use this method in the script of a main element (e.g. PythonPartGroup) to get the BuildingElement of the subordinate elements (e.g. PythonParts in the group).  Args:     file_name: full path to the .pyp file  Returns:     True, if import was successful, False otherwise     Python module representing the PythonPart script (.py file)     The BuildingElement with parameters and their default values |
| `write_data_to_default_favorite_file` | `build_ele_list: List[BuildingElement]` | `None` | Write the data to the default favorite file  Args:     build_ele_list:  Building element list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the build element service
"""

import ntpath
import os
import os.path
from types import ModuleType
from typing import Any, List, Optional, Tuple

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Utility as AllplanUtil
from BuildingElement import BuildingElement
from BuildingElementComposite import BuildingElementComposite
from BuildingElementCompositeCreator import BuildingElementCompositeCreator
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementListService import BuildingElementListService
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementStringTable import BuildingElementStringTable
from BuildingElementSubElementUtil import BuildingElementSubElementUtil
from BuildingElementUtil import BuildingElementUtil
from BuildingElementValueConstraint import BuildingElementValueConstraint
from BuildingElementXML import BuildingElementXML
from FileNameService import FileNameService
from TraceService import TraceService


class BuildingElementService:
    """ Definition of class BuildingElementService
    """

    @staticmethod
    def read_data_from_pyp(file_name           : str,
                           str_table           : BuildingElementStringTable,
                           is_library_preview  : bool,
                           material_str_table  : BuildingElementMaterialStringTable,
                           sub_file_name       : str = "",
                           init_with_last_input: bool = True,
                           add_sub_file_name   : str = "") \
                           -> Tuple[Optional[bool], Optional[ModuleType], List[BuildingElement],
                                    List[BuildingElementControlProperties], BuildingElementComposite,
                                    str, str]:
        """ Read the data from the pyp file and check the version

        Args:
            file_name:              Name of the pyp file
            str_table:              String table
            is_library_preview:     Called for library preview
            material_str_table:     Material string table
            sub_file_name:          File with the sub elements
            init_with_last_input:   Initialize with the data from the last input (only if ReadLastInput is set in the script)
            add_sub_file_name:      additional sub file

        Returns:
            True, if import was successful, False otherwise
            Python module representing the PythonPart script (.py file)
            List with BuildingElement objects containing parameter values
            List with Control properties
            Building element composite object
            Base name the .pyp file (without the directory path and the '.pyp' extension)
            Absolute path of the .pyp file
        """

        build_ele_composite = BuildingElementComposite()


        #----------------- check the file

        if not os.path.isfile(file_name):
            file_name_org = file_name

            bfound, file_name = FileNameService.get_pyp_path_from_lib_struct(file_name)

            if not bfound:
                if (index := file_name_org.lower().find("\\library\\")) != -1:
                    bfound, file_name = FileNameService.get_pyp_path_from_lib_struct(file_name_org[index + 1:])

            if not bfound:
                bfound, file_name = FileNameService.search_pyp_file(file_name_org)

            if not bfound:
                TraceService.trace_1('******************************')
                TraceService.trace_1('Script ' + file_name_org + ' could not be found in lib structure')
                TraceService.trace_1('******************************')

                AllplanUtil.ShowMessageBox("Script: " + file_name_org + " could not be found in lib structure",
                                           AllplanUtil.MB_OK)

                return False, None, [], [], build_ele_composite, "", ""


        #----------------- read the data from the xml file

        xml_ele = BuildingElementXML()

        if str_table is None:
            str_table = BuildingElementStringTable("", False, "")

        if material_str_table is None:
            material_str_table = BuildingElementMaterialStringTable("", False, "")

        build_ele, build_ele_ctrl_props, sub_elements_file = xml_ele.read_element_parameter(file_name, str_table, material_str_table)

        if is_library_preview  and  build_ele.script_name.find("NodeScripts\\NodeScript.py") != -1:
            return False, None, [], [], build_ele_composite, "", ""


        #----------------- execute the node script migration if necessary

        is_node_script = "nodescript.py" in build_ele.script_name.lower()

        if is_node_script and build_ele.get_float_version() < 1.09:
            nodescript_migration = __import__("NodeScriptMigration")

            ns_migration = nodescript_migration.NodeScriptMigration()

            ns_migration.migrate_1_1(file_name, build_ele.get_string_tables()[0].get_path())

            build_ele, build_ele_ctrl_props, sub_elements_file = xml_ele.read_element_parameter(file_name, str_table, material_str_table)


        #----------------- read the composite data

        if not sub_file_name:
            if is_node_script:
                sub_file_name = file_name
            else:
                sub_file_name = BuildingElementSubElementUtil.get_file_name(file_name, sub_elements_file,
                                                                            is_library_preview)

        if not sub_file_name:
            return False, None, [], [], build_ele_composite, "", ""

        if not os.path.isfile(sub_file_name):
            TraceService.trace_1('******************************')
            TraceService.trace_1('File ' + sub_file_name + ' could not be found')
            TraceService.trace_1('******************************')

            AllplanUtil.ShowMessageBox("File: " + sub_file_name + " could not be found",
                                       AllplanUtil.MB_OK)

            return False, None, [], [], build_ele_composite, "", ""

        if (prop := build_ele.get_property("SubElementsName")):
            prop.value = sub_file_name

        BuildingElementCompositeCreator.read_data_from_pyp(build_ele_composite,
                                                           sub_file_name, build_ele.get_string_tables()[0],
                                                           is_node_script, build_ele.get_float_version())


        #------------------ Import the script

        build_ele_script = BuildingElementUtil.import_building_element_script(build_ele, False)

        if build_ele_script is None and file_name.lower().endswith(".pyp"):
            return False, None, [], [], build_ele_composite, "", ""

        pyp_name = ntpath.basename(file_name).split(".")[0]


        #------------------ Check the supported Allplan version

        current_version = AllplanSettings.AllplanVersion.Version()

        if build_ele_script:
            if getattr(build_ele_script, "check_allplan_version", None) is None:
                AllplanUtil.ShowMessageBox("Function 'check_allplan_version' must be implemented in script " + build_ele.script_name,
                                           AllplanUtil.MB_OK)

                return False, None, [], [], build_ele_composite, "", ""

            if not build_ele_script.check_allplan_version(build_ele, current_version):
                AllplanUtil.ShowMessageBox("Your Allplan version is not supported by this PythonPart",
                                           AllplanUtil.MB_OK)

                return False, None, [], [], build_ele_composite, "", ""


        #----------------- check for composite elements

        del xml_ele

        build_ele_list            = [build_ele]
        build_ele_ctrl_props_list = [build_ele_ctrl_props]

        for iteration in range(2):
            if BuildingElementCompositeCreator.create_building_element_list(build_ele_composite,
                                                                            build_ele_list, build_ele_ctrl_props_list,
                                                                            sub_file_name, str_table, material_str_table, iteration == 0):
                break


            #------------- not possible to create the list

            if iteration == 1 or not is_node_script:
                return False, None, [], [], build_ele_composite, "", ""


            #------------- execute the migration and read the data

            build_ele_list            = [build_ele]
            build_ele_ctrl_props_list = [build_ele_ctrl_props]

            nodescript_migration = __import__("NodeScriptMigration")

            ns_migration = nodescript_migration.NodeScriptMigration()

            ns_migration.migrate_path_99_99_0(file_name, build_ele.get_string_tables()[0].get_path())

            build_ele_composite = BuildingElementComposite()

            BuildingElementCompositeCreator.read_data_from_pyp(build_ele_composite,
                                                               sub_file_name, build_ele.get_string_tables()[0],
                                                               build_ele.script_name.lower() == "nodescript.py",
                                                               build_ele.get_float_version())

        #------------------ add a pypsub file

        if add_sub_file_name:
            xml_ele = BuildingElementXML()

            build_ele, build_ele_ctrl_props, _ = xml_ele.read_element_parameter(add_sub_file_name, str_table, material_str_table)

            build_ele_list.append(build_ele)
            build_ele_ctrl_props_list.append(build_ele_ctrl_props)


        #----------------- set the pyp data

        build_ele_list[0].pyp_file_name = (FileNameService.get_lib_pyp_sricpt_path(file_name))

        path, _ = os.path.split(file_name)

        for build_ele in build_ele_list:
            build_ele.pyp_file_path = path


        #----------------- read the favorite if needed

        if not is_library_preview  and  init_with_last_input and build_ele_list[0].read_last_input:
            BuildingElementListService.read_from_default_favorite_file(build_ele_list)

            for build_ele, ctrl_prop_list in zip(build_ele_list, build_ele_ctrl_props_list):
                BuildingElementValueConstraint.update_enable_by_constraint(build_ele, ctrl_prop_list)
                BuildingElementValueConstraint.check_property_constraint_init(build_ele, ctrl_prop_list)

        BuildingElementUtil.hide_element_index(build_ele_list, build_ele_ctrl_props_list)

        return True, build_ele_script, build_ele_list, build_ele_ctrl_props_list, build_ele_composite, pyp_name, file_name

    @staticmethod
    def read_build_ele_from_pyp(file_name: str) -> tuple[bool, ModuleType | None, BuildingElement | None]:
        """Create BuildingElement and python module based on .pyp file

        This method gets only the BuildingElement and the python module of the script, the .pyp
        file refers to. The resulting BuildingElement contains parameters with their default values.

        Use this method in the script of a main element (e.g. PythonPartGroup) to get the BuildingElement
        of the subordinate elements (e.g. PythonParts in the group).

        Args:
            file_name: full path to the .pyp file

        Returns:
            True, if import was successful, False otherwise
            Python module representing the PythonPart script (.py file)
            The BuildingElement with parameters and their default values
        """
        result, script, build_ele_list, _, _, _, _ = BuildingElementService.read_data_from_pyp(
            file_name, None, False, None,
            init_with_last_input = False)

        if not result or result is None:
            return False, None, None
        return result, script, build_ele_list[0]

    @staticmethod
    def write_data_to_default_favorite_file(build_ele_list: List[BuildingElement]):
        """ Write the data to the default favorite file

        Args:
            build_ele_list:  Building element list
        """

        BuildingElementListService.write_to_default_favorite_file(build_ele_list)

```

</details>