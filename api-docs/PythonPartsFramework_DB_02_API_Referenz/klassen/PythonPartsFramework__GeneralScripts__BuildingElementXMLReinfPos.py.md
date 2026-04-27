---
title: "BuildingElementXMLReinfPos"
source: "PythonPartsFramework\GeneralScripts\BuildingElementXMLReinfPos.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementXMLReinfPos

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementXMLReinfPos.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`, `script`, `xml`

## Übersicht

Script for BuildingElementXMLReinfPos

## Abhängigkeiten

- `ControlProperties`
- `NemAll_Python_Palette`
- `ParameterProperty`
- `StringTableService`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `XMLReader.XmlElementTreeUtil`
- `XMLReader.XmlStringToValueConverter`

## Klassen

### `BuildingElementXMLReinfPos`

Definition of class BuildingElementXMLReinfPos

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele, control_data, persistent, global_str_table` | `None` | - |
| `__add_radiobutton` | `self, ctrl_id, page_index, group_name, expander_name, row_name, button_id, value, enable_cond, visible_cond` | `None` | Add a radio button control  Args:     ctrl_id:            id of the control     page_index:         page index / number     group_name:         radio button group name     param:              this parameter node     expander_name:      expander name     row_name:           row name     button_id           button id     value               control value     enable_cond         enable condition     visible_cond        visible condition |
| `__add_reinf_diameter` | `self, ctrl_id, page_index, expander_name, row_name, value_str, visible_cond, enable_cond=''` | `None` | Add a reinforcement diameter control  Args:     ctrl_id:            id of the control     page_index:         page index / number     group_name:         radio button group name     param:              this parameter node     expander_name:      expander name     row_name:           row name     button_id           button id     value               control value     visible_cond        visible condition     enable_cond         enable condition |
| `__add_reinf_mesh_type` | `self, ctrl_id, page_index, expander_name, row_name, value_str, visible_cond, enable_cond=''` | `None` | Add a reinforcement mesh type control  Args:     ctrl_id:            id of the control     page_index:         page index / number     group_name:         radio button group name     param:              this parameter node     expander_name:      expander name     row_name:           row name     button_id           button id     value               control value     visible_cond        visible condition     enable_cond         enable condition |
| `__add_reinf_side_length` | `self, ctrl_id, page_index, expander_name, prop_name, prop_text, value_str, enable_cond, visible_cond` | `None` | Add a reinforcement diameter control  Args:     ctrl_id:            id of the control     page_index:         page index / number     group_name:         radio button group name     param:              this parameter node     expander_name:      expander name     prop_name:          property name     button_id:          button id     value:              control value     enable_cond:        enable condition     visible_cond:       visible condition |
| `get_reinforcement_position_data` | `self, page_index, param, expander_name, text` | `None` | Get the data from one radio button group parameter node  Args:     page_index:         page index / number     param:              this parameter node     expander_name:      name of the expander |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""
Script for BuildingElementXMLReinfPos
"""

# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-return-statements

import NemAll_Python_Palette as AllplanPalette

from ParameterProperty import ParameterProperty
from ControlProperties import ControlProperties
from StringTableService import StringTableService

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

from XMLReader.XmlStringToValueConverter import XmlStringToValueConverter
from XMLReader.XmlElementTreeUtil import XmlElementTreeUtil

class BuildingElementXMLReinfPos():
    """
    Definition of class BuildingElementXMLReinfPos
    """

    def __init__(self, build_ele, control_data, persistent, global_str_table):
        self.build_ele        = build_ele
        self.control_data     = control_data
        self.persistent       = persistent
        self.global_str_table = global_str_table


    def __add_radiobutton(self, ctrl_id, page_index, group_name, expander_name, row_name, button_id, value,
                          enable_cond, visible_cond):
        """
        Add a radio button control

        Args:
            ctrl_id:            id of the control
            page_index:         page index / number
            group_name:         radio button group name
            param:              this parameter node
            expander_name:      expander name
            row_name:           row name
            button_id           button id
            value               control value
            enable_cond         enable condition
            visible_cond        visible condition
        """
        param_prop                = ParameterProperty()
        param_prop.value_type     = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.RADIO_BUTTON)
        param_prop.name           = "RadioButton" + ctrl_id + button_id
        param_prop.value          = value
        param_prop.selected_value = 1
        param_prop.group_name     = group_name
        param_prop.persistent     = self.persistent

        ctrl_prop = ControlProperties("", param_prop.name, enable_cond, visible_cond,
                                      page_index, expander_name, row_name,
                                      "", "", "", "0")

        self.build_ele.add_property(param_prop.name, param_prop)
        self.control_data.append(ctrl_prop)


    def __add_reinf_diameter(self, ctrl_id, page_index, expander_name, row_name, value_str,  \
                             visible_cond, enable_cond = ""):
        """
        Add a reinforcement diameter control

        Args:
            ctrl_id:            id of the control
            page_index:         page index / number
            group_name:         radio button group name
            param:              this parameter node
            expander_name:      expander name
            row_name:           row name
            button_id           button id
            value               control value
            visible_cond        visible condition
            enable_cond         enable condition
        """
        param_prop            = ParameterProperty()
        param_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.REINF_BAR_DIAMETER)
        param_prop.name       = "Diameter" + ctrl_id
        param_prop.value      = float(value_str)
        param_prop.persistent = self.persistent

        ctrl_prop = ControlProperties("", param_prop.name, enable_cond, visible_cond,
                                      page_index, expander_name, row_name,
                                      "", "", "", 0)

        self.build_ele.add_property(param_prop.name, param_prop)
        self.control_data.append(ctrl_prop)


    def __add_reinf_mesh_type(self, ctrl_id, page_index, expander_name, row_name, value_str,  \
                              visible_cond, enable_cond = ""):
        """
        Add a reinforcement mesh type control

        Args:
            ctrl_id:            id of the control
            page_index:         page index / number
            group_name:         radio button group name
            param:              this parameter node
            expander_name:      expander name
            row_name:           row name
            button_id           button id
            value               control value
            visible_cond        visible condition
            enable_cond         enable condition
        """
        param_prop            = ParameterProperty()
        param_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.REINF_MESH_TYPE)
        param_prop.name       = "MeshType" + ctrl_id
        param_prop.value      = XmlStringToValueConverter.get_value(self.build_ele, param_prop.value_type,
                                                                    value_str, None, 0, None, None)
        param_prop.persistent = self.persistent

        ctrl_prop = ControlProperties("", param_prop.name, enable_cond, visible_cond,
                                      page_index, expander_name, row_name,
                                      "", "", "", 0)

        self.build_ele.add_property(param_prop.name, param_prop)
        self.control_data.append(ctrl_prop)


    def __add_reinf_side_length(self, ctrl_id, page_index, expander_name, prop_name, prop_text, value_str,
                                enable_cond, visible_cond):
        """
        Add a reinforcement diameter control

        Args:
            ctrl_id:            id of the control
            page_index:         page index / number
            group_name:         radio button group name
            param:              this parameter node
            expander_name:      expander name
            prop_name:          property name
            button_id:          button id
            value:              control value
            enable_cond:        enable condition
            visible_cond:       visible condition
        """
        param_prop            = ParameterProperty()
        param_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.LENGTH)
        param_prop.name       = prop_name + ctrl_id
        param_prop.value      = float(value_str)
        param_prop.persistent = self.persistent

        ctrl_prop = ControlProperties(prop_text, param_prop.name, enable_cond, visible_cond,
                                      page_index, expander_name, "",
                                      "", "", "", 0)

        self.build_ele.add_property(param_prop.name, param_prop)
        self.control_data.append(ctrl_prop)


    def get_reinforcement_position_data(self,
                                        page_index,
                                        param,
                                        expander_name,
                                        text):
        """
        Get the data from one radio button group parameter node

        Args:
            page_index:         page index / number
            param:              this parameter node
            expander_name:      name of the expander
        """

        reinf_id          = XmlElementTreeUtil.get_tag_data(param, "ReinfID")
        picture           = XmlElementTreeUtil.get_tag_data(param, "Picture")
        diameter          = XmlElementTreeUtil.get_tag_data(param, "Diameter")
        mesh_type         = XmlElementTreeUtil.get_tag_data(param, "MeshType")
        side_length_start = XmlElementTreeUtil.get_tag_data(param, "SideLengthStart")
        side_length_end   = XmlElementTreeUtil.get_tag_data(param, "SideLengthEnd")
        distance          = XmlElementTreeUtil.get_tag_data(param, "Distance")
        visible_cond      = XmlElementTreeUtil.get_tag_data(param, "Visible")
        select            = XmlElementTreeUtil.get_tag_data(param, "Select")

        if picture:
            param_prop                = ParameterProperty()
            param_prop.value          = picture
            param_prop.value_type     = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.PICTURE)
            param_prop.name           = "Picture" + reinf_id
            param_prop.selected_value = AllplanPalette.Orientation.eLeft
            param_prop.persistent     = self.persistent

            ctrl_prop = ControlProperties(text, param_prop.name, "", visible_cond,
                                          page_index, expander_name, "",
                                          "", "", "", 0)

            self.build_ele.add_property(param_prop.name, param_prop)
            self.control_data.append(ctrl_prop)

        enable_cond = ""

        if select:
            param_prop            = ParameterProperty()
            param_prop.value      = int(select)
            param_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.CHECK_BOX)
            param_prop.name       = "Shape" + reinf_id
            enable_cond           = "Shape" + reinf_id
            param_prop.persistent = self.persistent

            ctrl_prop = ControlProperties(text, param_prop.name, "", visible_cond,
                                          page_index, expander_name, "",
                                          "", "", "", 0)

            self.build_ele.add_property(param_prop.name, param_prop)
            self.control_data.append(ctrl_prop)

        diameter_text = StringTableService.get_string_table_entry(self.global_str_table, 'e_BAR_DIAMETER', 'Bar diameter')
        mesh_text     = StringTableService.get_string_table_entry(self.global_str_table, 'e_MESH_TYPE', 'Mesh type')

        if diameter and mesh_type:
            reinf_type = "ReinfType" + reinf_id

            param_prop            = ParameterProperty()
            param_prop.name       = reinf_type
            param_prop.value      = 1
            param_prop.persistent = self.persistent
            param_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.INTEGER)

            enable = enable_cond

            if enable:
                enable += "  and  "

            self.build_ele.add_property(param_prop.name, param_prop)

            self.__add_radiobutton(reinf_id, page_index, reinf_type, expander_name, diameter_text, "a", 1,
                                   enable_cond, visible_cond)
            self.__add_reinf_diameter(reinf_id, page_index, expander_name,
                                      diameter_text, diameter,
                                      visible_cond, enable + reinf_type + " == 1")

            self.__add_radiobutton(reinf_id, page_index, reinf_type, expander_name, mesh_text, "b", 2,
                                   enable_cond, visible_cond)
            self.__add_reinf_mesh_type(reinf_id, page_index, expander_name, mesh_text, mesh_type,
                                       visible_cond, enable + reinf_type + " == 2")

        elif diameter:
            self.__add_reinf_diameter(reinf_id, page_index, expander_name,
                                      diameter_text, diameter, visible_cond, enable_cond)

        else:
            self.__add_reinf_mesh_type(reinf_id, page_index, expander_name,
                                       mesh_type, mesh_type, visible_cond, enable_cond)


        if side_length_start:
            text = StringTableService.get_string_table_entry(self.global_str_table, 'e_SEGMENT_LENGTH_START', 'Segment length start')

            self.__add_reinf_side_length(reinf_id, page_index, expander_name, "SideLengthStart", text,
                                         side_length_start, enable_cond, visible_cond)

        if side_length_end:
            text = StringTableService.get_string_table_entry(self.global_str_table, 'e_SEGMENT_LENGTH_END', 'Segment length end')

            self.__add_reinf_side_length(reinf_id, page_index, expander_name, "SideLengthEnd", text,
                                         side_length_end, enable_cond, visible_cond)


        if distance:
            distance_text         = StringTableService.get_string_table_entry(self.global_str_table, 'e_SPACING', 'Spacing')

            param_prop            = ParameterProperty()
            param_prop.value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.LENGTH)
            param_prop.name       = "Distance" + reinf_id
            param_prop.value      = float(distance)
            param_prop.persistent = self.persistent

            ctrl_prop = ControlProperties(distance_text, param_prop.name, enable_cond, visible_cond,
                                          page_index, expander_name, "",
                                          "", "", "", 0)

            self.build_ele.add_property(param_prop.name, param_prop)
            self.control_data.append(ctrl_prop)

```

</details>