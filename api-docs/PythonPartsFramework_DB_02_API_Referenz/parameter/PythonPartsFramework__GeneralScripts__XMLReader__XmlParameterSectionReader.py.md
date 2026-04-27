---
title: "XmlParameterSectionReader"
source: "PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterSectionReader.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlParameterSectionReader

> **Pfad:** `PythonPartsFramework\GeneralScripts\XMLReader\XmlParameterSectionReader.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `xml`

## Übersicht

implementation of the parameter section reader

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `BuildingElementMaterialStringTable`
- `BuildingElementStringTable`
- `BuildingElementXMLReinfPos`
- `ControlProperties`
- `IncludeData`
- `ParameterProperty`
- `StringEvaluate`
- `Utilities.GeneralConstants`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `ValueTypes.ValueTypeUtils.ComboBoxValueListUtil`
- `XMLSelectionValueReader`
- `XmlElementTreeUtil`
- `XmlParameterInclude`
- `XmlParameterReader`
- `XmlParameterReaderUtil`
- `XmlParameterTextReader`
- `XmlParameterValueReader`
- `XmlParentParameterData`
- `_collections_abc`
- `xml.etree`

## Klassen

### `XmlParameterSectionReader`

Definition of class BuildingElementXML
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele: BuildingElement, build_ele_ctrl_props: BuildingElementControlProperties, local_str_table: BuildingElementStringTable, global_str_table: BuildingElementStringTable, persistent: ParameterProperty.Persistent, input_type: ParameterProperty.InputType, is_imperial_unit: bool, is_visual_script: bool` | `None` | Initialization  Args:     build_ele:            building element with the parameter properties     build_ele_ctrl_props: description     local_str_table:      local string table     global_str_table:     global string table     persistent:           persistent state     input_type:           input type     is_imperial_unit:     imperial unit state     is_visual_script:     visual script state |
| `execute` | `self, section: ElementTree.Element, page_index: int, global_material_str_table: BuildingElementMaterialStringTable` | `None` | Get the data from the pages  Args:     section:                   section     page_index:                page index     global_material_str_table: global material string table |
| `__get_parameter_data` | `self, page_index: int, param: ElementTree.Element, parent_param_data: XmlParentParameterData, material_str_table: BuildingElementMaterialStringTable, local_str_table: BuildingElementStringTable, include_data: IncludeData` | `None` | Get the data from one parameter  Args:     page_index:         page index / number     param:              this parameter node     parent_param_data:  data of the parent parameter     material_str_table: material string table     local_str_table:    local string table     include_data:       include data |
| `__get_expander_data` | `self, page_index: int, param: ElementTree.Element, parent_param_data: XmlParentParameterData, material_str_table: BuildingElementMaterialStringTable, local_str_table: BuildingElementStringTable, include_data: IncludeData` | `None` | Get the data from one expander parameter node  Args:     page_index:         page index / number     param:              this parameter node     parent_param_data:  data of the parent parameter     material_str_table: material string table     local_str_table:    local string table     include_data:       include data |
| `__get_row_data` | `self, page_index: int, param: ElementTree.Element, parent_param_data: XmlParentParameterData, material_str_table: BuildingElementMaterialStringTable, local_str_table: BuildingElementStringTable, include_data: IncludeData` | `None` | Get the data from one row parameter node  Args:     page_index:         page index / number     param:              this parameter node     parent_param_data:  data of the parent parameter     material_str_table: material string table     local_str_table:    local string table     include_data:       include data |
| `__get_listgroup_data` | `self, page_index: int, param: ElementTree.Element, parent_param_data: XmlParentParameterData, material_str_table: BuildingElementMaterialStringTable, local_str_table: BuildingElementStringTable, include_data: IncludeData` | `None` | Get the data from one row parameter node  Args:     page_index:         page index / number     param:              this parameter node     parent_param_data:  data of the parent parameter     material_str_table: material string table     local_str_table:    local string table     include_data:       include data |
| `__get_condition_group_data` | `self, page_index: int, param: ElementTree.Element, parent_param_data: XmlParentParameterData, material_str_table: BuildingElementMaterialStringTable, local_str_table: BuildingElementStringTable, include_data: IncludeData` | `None` | Get the data from a condition group  Args:     page_index:         page index / number     param:              this parameter node     parent_param_data:  data of the parent parameter     material_str_table: material string table     local_str_table:    local string table     include_data:       include data |
| `__get_radio_button_group_data` | `self, page_index: int, param: ElementTree.Element, parent_param_data: XmlParentParameterData, material_str_table: BuildingElementMaterialStringTable, local_str_table: BuildingElementStringTable, include_data: IncludeData` | `None` | Get the data from one radio button group parameter node  Args:     page_index:         page index / number     param:              this parameter node     parent_param_data:  data of the parent parameter     material_str_table: material string table     local_str_table:    local string table     include_data:       include data |
| `__yield_parameters` | `element: ElementTree.Element` | `Iterator[ElementTree.Element]` | Yield `Parameter` tree elements from the given XML tree element  Search for a `Parameters` element and yield the `Parameter` elements from it. For backward compatibility, if there is no `Parameters` element, yield the `Parameter` elements directly.  Args:     element: XML tree element  Yield:     `Parameter` tree elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the parameter section reader
"""

# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-return-statements
# pylint: disable=magic-value-comparison

from xml.etree import ElementTree

from _collections_abc import Iterator
from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementStringTable import BuildingElementStringTable
from BuildingElementXMLReinfPos import BuildingElementXMLReinfPos
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate
from Utilities.GeneralConstants import GeneralConstants
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl
from ValueTypes.ValueTypeUtils.ComboBoxValueListUtil import ComboBoxValueListUtil

from .IncludeData import IncludeData
from .XmlElementTreeUtil import XmlElementTreeUtil
from .XmlParameterInclude import XmlParameterInclude
from .XmlParameterReader import XmlParameterReader
from .XmlParameterReaderUtil import XmlParameterReaderUtil
from .XmlParameterTextReader import XmlParameterTextReader
from .XmlParameterValueReader import XmlParameterValueReader
from .XmlParentParameterData import XmlParentParameterData
from .XMLSelectionValueReader import XMLSelectionValueReader

DEPRECATED_ROW_STATE_KEY = "1"
EXPANDER_LEVEL_SEPARATOR = "|"

class XmlParameterSectionReader():
    """    Definition of class BuildingElementXML
    """

    def __init__(self,
                 build_ele           : BuildingElement,
                 build_ele_ctrl_props: BuildingElementControlProperties,
                 local_str_table     : BuildingElementStringTable,
                 global_str_table    : BuildingElementStringTable,
                 persistent          : ParameterProperty.Persistent,
                 input_type          : ParameterProperty.InputType,
                 is_imperial_unit    : bool,
                 is_visual_script    : bool):
        """ Initialization

        Args:
            build_ele:            building element with the parameter properties
            build_ele_ctrl_props: description
            local_str_table:      local string table
            global_str_table:     global string table
            persistent:           persistent state
            input_type:           input type
            is_imperial_unit:     imperial unit state
            is_visual_script:     visual script state
        """

        self.build_ele            = build_ele
        self.build_ele_ctrl_props = build_ele_ctrl_props
        self.local_str_table      = local_str_table
        self.global_str_table     = global_str_table
        self.persistent           = persistent
        self.input_type           = input_type
        self.is_imperial_unit     = is_imperial_unit
        self.is_visual_script     = is_visual_script

        self.cond_group_visible : list[str] = []
        self.cond_group_enable  : list[str] = []


    def execute(self,
                section                  : ElementTree.Element,
                page_index               : int,
                global_material_str_table: BuildingElementMaterialStringTable):
        """ Get the data from the pages

        Args:
            section:                   section
            page_index:                page index
            global_material_str_table: global material string table
        """

        for param in self.__yield_parameters(section):
            self.__get_parameter_data(page_index, param, XmlParentParameterData(), global_material_str_table,
                                      self.local_str_table, IncludeData())

    def __get_parameter_data(self,
                             page_index        : int,
                             param             : ElementTree.Element,
                             parent_param_data : XmlParentParameterData,
                             material_str_table: BuildingElementMaterialStringTable,
                             local_str_table   : BuildingElementStringTable,
                             include_data      : IncludeData):
        """ Get the data from one parameter

        Args:
            page_index:         page index / number
            param:              this parameter node
            parent_param_data:  data of the parent parameter
            material_str_table: material string table
            local_str_table:    local string table
            include_data:       include data
        """

        value_type = XmlElementTreeUtil.get_tag_data(param, 'ValueType').lower().replace("\n", "").replace(" ", "")

        match value_type:
            case ParameterPropertyValueTypes.INCLUDE:
                param_include = XmlParameterInclude(self.build_ele, self.local_str_table)

                param_include.execute(page_index, param, parent_param_data, material_str_table,
                                      self.__get_parameter_data)

                return

            case ParameterPropertyValueTypes.EXPANDER:
                self.__get_expander_data(page_index, param, parent_param_data, material_str_table,
                                         local_str_table, include_data)

                return

            case ParameterPropertyValueTypes.ROW:
                self.__get_row_data(page_index, param, parent_param_data, material_str_table,
                                    local_str_table, include_data)

                return

            case ParameterPropertyValueTypes.RADIO_BUTTON_GROUP:
                self.__get_radio_button_group_data(page_index, param, parent_param_data, material_str_table,
                                                   local_str_table, include_data)

                return

            case ParameterPropertyValueTypes.LIST_GROUP:
                self.__get_listgroup_data(page_index, param, parent_param_data, material_str_table,
                                          local_str_table, include_data)

                return

            case ParameterPropertyValueTypes.CONDITION_GROUP:
                self.__get_condition_group_data(page_index, param, parent_param_data, material_str_table,
                                                local_str_table, include_data)

                return

            case ParameterPropertyValueTypes.REINF_POSITION:
                build_ele_reinf_pos = BuildingElementXMLReinfPos(self.build_ele, self.build_ele_ctrl_props, self.persistent,
                                                                self.global_str_table)

                build_ele_reinf_pos.get_reinforcement_position_data(
                    page_index, param, parent_param_data.expander_name,
                    XmlParameterTextReader.get_prop_text(param, local_str_table,
                                                         self.global_str_table, self.is_visual_script).replace("#",
                                                                                                               include_data.text_postfix))

                return


        #----------------- read the parameter data

        param_prop = XmlParameterReader.get_parameter_property(param, value_type, self.persistent, self.input_type, self.is_visual_script,
                                                               self.build_ele, local_str_table, self.global_str_table,
                                                               material_str_table, self.is_imperial_unit, include_data.name_postfix,
                                                               self.build_ele_ctrl_props.palette_layout_dict)

        ctrl_prop = XmlParameterReader.get_control_properties(param, local_str_table, self.global_str_table, self.is_visual_script,
                                                              self.is_imperial_unit, self.build_ele, page_index,
                                                              parent_param_data, param_prop,
                                                              include_data,
                                                              self.build_ele_ctrl_props.palette_layout_dict)

        if (value_list_path := XmlElementTreeUtil.get_str_value(param, "ValueListFile", "")):
            param_prop.value_list_util = ComboBoxValueListUtil(value_list_path, ctrl_prop.value_list, param_prop.value_type)


        #----------------- set the selected value

        XMLSelectionValueReader.set_selected_value(param, param_prop)


        #----------------- special handling needed for radio buttons, selected value is stored in parent

        if str(ParameterPropertyValueTypes.RADIO_BUTTON) in param_prop.value_type:
            param_prop.selected_value = parent_param_data.radio_group_selection
            param_prop.group_name     = parent_param_data.radio_group_name
            ctrl_prop.group_text      = parent_param_data.radio_group_text


        #----------------- Add parameter to element

        if (prop := self.build_ele.get_property(param_prop.name)) is None:
            self.build_ele.add_property(param_prop.name, param_prop)
        else:
            prop.enum_dict = prop.enum_dict | param_prop.enum_dict

            if (item := self.build_ele_ctrl_props.get_property(param_prop.name)) is not None:
                ctrl_prop.value_list   = item.value_list
                ctrl_prop.value_list_2 = item.value_list_2


        #----------------- add the group condition

        group_visible = ") and (".join(self.cond_group_visible)
        group_enable  = ") and (".join(self.cond_group_enable)

        if group_visible:
            group_visible = f"({group_visible})"

            ctrl_prop.visible_condition = f"{group_visible} and ({ctrl_prop.visible_condition})" if ctrl_prop.visible_condition else \
                                          group_visible

        if group_enable:
            group_enable = f"({group_enable})"

            ctrl_prop.enable_condition = f"{group_enable} and ({ctrl_prop.enable_condition})" if ctrl_prop.enable_condition else \
                                         group_enable

        ctrl_prop.palette_layout_dict = self.build_ele_ctrl_props.palette_layout_dict

        self.build_ele_ctrl_props.append(ctrl_prop)


    def __get_expander_data(self,
                            page_index        : int,
                            param             : ElementTree.Element,
                            parent_param_data : XmlParentParameterData,
                            material_str_table: BuildingElementMaterialStringTable,
                            local_str_table   : BuildingElementStringTable,
                            include_data      : IncludeData):
        """ Get the data from one expander parameter node

        Args:
            page_index:         page index / number
            param:              this parameter node
            parent_param_data:  data of the parent parameter
            material_str_table: material string table
            local_str_table:    local string table
            include_data:       include data
        """

        expander_name = \
            XmlParameterTextReader.get_prop_text(param, local_str_table, self.global_str_table,
                                                 self.is_visual_script, "Expander").replace("#", include_data.text_postfix)

        expander_name = expander_name.replace(EXPANDER_LEVEL_SEPARATOR, "")

        expander_state_key = "COLLAPSED" if XmlElementTreeUtil.get_bool_value(param, 'Value', 'Expander') else ""

        # if a parent expander exists compose the expander name and state key by using the '|' character
        # the state key is prefixed by '_' character if it is not an empty string

        if parent_param_data.expander_name:
            parent_param_data.expander_name = f"{parent_param_data.expander_name}{EXPANDER_LEVEL_SEPARATOR}{expander_name}"

            if not parent_param_data.expander_state_key:
                parent_param_data.expander_state_key = "_"

            parent_param_data.expander_state_key = f"{parent_param_data.expander_state_key}{EXPANDER_LEVEL_SEPARATOR}{expander_state_key}"

        else:
            parent_param_data.expander_name      = expander_name
            parent_param_data.expander_state_key = f"_{expander_state_key}" if expander_state_key else ""

        name = XmlElementTreeUtil.get_tag_data(param, "Name") + include_data.name_postfix

        ctrl_prop = ControlProperties("", parent_param_data.expander_name, "",
                                      XmlParameterReaderUtil.get_visible(param, name, include_data, "Expander", ""),
                                      page_index, parent_param_data.expander_name, parent_param_data.row_name,
                                      "", "", "", "", ControlProperties.ControlType.EXPANDER)

        self.build_ele_ctrl_props.append(ctrl_prop)

        for subparam in self.__yield_parameters(param):
            self.__get_parameter_data(page_index, subparam, parent_param_data, material_str_table,
                                      local_str_table, include_data)

        parent_param_data.reset_expander()


    def __get_row_data(self,
                       page_index        : int,
                       param             : ElementTree.Element,
                       parent_param_data : XmlParentParameterData,
                       material_str_table: BuildingElementMaterialStringTable,
                       local_str_table   : BuildingElementStringTable,
                       include_data      : IncludeData):
        """ Get the data from one row parameter node

        Args:
            page_index:         page index / number
            param:              this parameter node
            parent_param_data:  data of the parent parameter
            material_str_table: material string table
            local_str_table:    local string table
            include_data:       include data
        """

        row_has_text = True

        if not (row_name := XmlParameterTextReader.get_prop_text(param, self.local_str_table, self.global_str_table,
                                                                 self.is_visual_script, "row", include_data.is_include)):
            row_has_text = False

            row_name = XmlParameterTextReader.get_prop_text(param, self.local_str_table, self.global_str_table,
                                                            self.is_visual_script)

        row_name = row_name.replace("#", include_data.text_postfix)

        if "__create_empty_row_text" in row_name:
            row_name = StringEvaluate.eval_text(row_name, {})


        #----------------- get and adapt the row state key

        if (row_state_key := XmlElementTreeUtil.get_tag_data(param, "Value", "row")) == DEPRECATED_ROW_STATE_KEY:
            row_state_key = "OVERALL"

        if row_state_key:
            row_state_key = f"_{row_state_key.upper()}"

            if GeneralConstants.ROW_STATE_KEY_SEPARATOR in row_state_key:
                diff = 1

                if row_has_text:
                    diff = 2

                row_state_key, _, right = row_state_key.partition(":")

                if (right := right.strip()):
                    row_state_key = f"_OVERALL:{int(right.strip()) + diff}"


        #----------------- create the properties

        name = XmlElementTreeUtil.get_tag_data(param, "Name") + include_data.name_postfix

        ctrl_prop = ControlProperties("", name, "",
                                      XmlParameterReaderUtil.get_visible(param, name, include_data, "Row", ""),
                                      page_index, parent_param_data.expander_name, row_name,
                                      "", "", "", "", ControlProperties.ControlType.ROW,
                                      row_state_key = row_state_key)

        self.build_ele_ctrl_props.append(ctrl_prop)

        parent_param_data.row_name      = row_name
        parent_param_data.row_state_key = row_state_key

        for subparam in self.__yield_parameters(param):
            self.__get_parameter_data(page_index, subparam, parent_param_data, material_str_table,
                                      local_str_table, include_data)

        parent_param_data.reset_row()


    def __get_listgroup_data(self,
                             page_index        : int,
                             param             : ElementTree.Element,
                             parent_param_data : XmlParentParameterData,
                             material_str_table: BuildingElementMaterialStringTable,
                             local_str_table   : BuildingElementStringTable,
                             include_data      : IncludeData):
        """ Get the data from one row parameter node

        Args:
            page_index:         page index / number
            param:              this parameter node
            parent_param_data:  data of the parent parameter
            material_str_table: material string table
            local_str_table:    local string table
            include_data:       include data
        """

        list_group_name = XmlElementTreeUtil.get_tag_data(param, "Name") + include_data.name_postfix

        start_index = len(self.build_ele_ctrl_props)

        for subparam in self.__yield_parameters(param):
            self.__get_parameter_data(page_index, subparam, parent_param_data, material_str_table,
                                      local_str_table, include_data)

        for index in range(start_index, len(self.build_ele_ctrl_props)):
            self.build_ele_ctrl_props[index].list_group_name = list_group_name


    def __get_condition_group_data(self,
                                   page_index        : int,
                                   param             : ElementTree.Element,
                                   parent_param_data : XmlParentParameterData,
                                   material_str_table: BuildingElementMaterialStringTable,
                                   local_str_table   : BuildingElementStringTable,
                                   include_data      : IncludeData):
        """ Get the data from a condition group

        Args:
            page_index:         page index / number
            param:              this parameter node
            parent_param_data:  data of the parent parameter
            material_str_table: material string table
            local_str_table:    local string table
            include_data:       include data
        """

        self.cond_group_visible.append(XmlElementTreeUtil.get_str_value(param, "Visible", "True", "conditiongroup"))
        self.cond_group_enable.append(XmlElementTreeUtil.get_str_value(param, "Enable", "True", "conditiongroup"))

        for subparam in self.__yield_parameters(param):
            self.__get_parameter_data(page_index, subparam, parent_param_data, material_str_table,
                                      local_str_table, include_data)

        self.cond_group_visible.pop()
        self.cond_group_enable.pop()


    def __get_radio_button_group_data(self,
                                      page_index        : int,
                                      param             : ElementTree.Element,
                                      parent_param_data : XmlParentParameterData,
                                      material_str_table: BuildingElementMaterialStringTable,
                                      local_str_table   : BuildingElementStringTable,
                                      include_data      : IncludeData):
        """ Get the data from one radio button group parameter node

        Args:
            page_index:         page index / number
            param:              this parameter node
            parent_param_data:  data of the parent parameter
            material_str_table: material string table
            local_str_table:    local string table
            include_data:       include data
        """

        value_str = XmlElementTreeUtil.get_tag_data(param, 'Value')

        parent_param_data.radio_group_text = \
            XmlParameterTextReader.get_prop_text(param, self.local_str_table, self.global_str_table,
                                                 self.is_visual_script, "RadioButtonGroup").replace("#", include_data.text_postfix)
        parent_param_data.radio_group_name = XmlElementTreeUtil.get_tag_data(param, 'Name') + include_data.name_postfix

        parent_param_data.radio_group_selection = XmlParameterReaderUtil.get_radio_button_group_selection(self.build_ele, value_str)

        exclude_identical = XmlElementTreeUtil.get_bool_value(param, "ExcludeIdentical", "RadioButtonGroup")

        enum_dict, _ = XmlParameterValueReader.get_enum_dict(param)

        # define a property for RadioButtonGroup

        if self.build_ele.get_property(parent_param_data.radio_group_name) is None:
            param_prop                   = ParameterProperty()
            param_prop.value_type        = "radiobuttongroup"
            param_prop.name              = parent_param_data.radio_group_name
            param_prop.value             = parent_param_data.radio_group_selection
            param_prop.persistent        = self.persistent
            param_prop.exclude_identical = exclude_identical
            param_prop.dimensions        = XmlElementTreeUtil.get_tag_data(param, "Dimensions")
            param_prop.enum_dict         = enum_dict

            self.build_ele.add_property(param_prop.name, param_prop)

        value_list = XmlParameterValueReader.get_value_list(param, ParameterPropertyValueTypesImpl.get_value_type_impl("radiobuttongroup"),
                                                            self.local_str_table, self.global_str_table)

        name = XmlElementTreeUtil.get_tag_data(param, "Name") + include_data.name_postfix

        ctrl_prop = ControlProperties("", parent_param_data.radio_group_name, "",
                                      XmlParameterReaderUtil.get_visible(param, name, include_data, "RadioButtonGroup", ""),
                                      page_index, parent_param_data.expander_name, parent_param_data.row_name,
                                      "", value_list, "", "",
                                      value_index_name = XmlElementTreeUtil.get_tag_data(param, 'ValueIndexName'))

        ctrl_prop.value_index_name_base = XmlElementTreeUtil.get_int_value(param, 'ValueIndexNameBase', 1)

        self.build_ele_ctrl_props.append(ctrl_prop)

        for subparam in self.__yield_parameters(param):
            self.__get_parameter_data(page_index, subparam, parent_param_data, material_str_table,
                                      local_str_table, include_data)

        parent_param_data.reset_radio_group()

    @staticmethod
    def __yield_parameters(element: ElementTree.Element) -> Iterator[ElementTree.Element]:
        """ Yield `Parameter` tree elements from the given XML tree element

        Search for a `Parameters` element and yield the `Parameter` elements from it.
        For backward compatibility, if there is no `Parameters` element, yield the `Parameter` elements directly.

        Args:
            element: XML tree element

        Yield:
            `Parameter` tree elements
        """

        if (parameters_element := XmlElementTreeUtil.get_element(element, 'Parameters')) is None:
            yield from XmlElementTreeUtil.get_children_by_title(element, 'Parameter')
        else:
            yield from XmlElementTreeUtil.get_children_by_title(parameters_element, 'Parameter')

```

</details>