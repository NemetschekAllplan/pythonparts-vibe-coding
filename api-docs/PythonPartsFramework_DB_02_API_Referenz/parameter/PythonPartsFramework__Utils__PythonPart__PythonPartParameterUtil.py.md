---
title: "PythonPartParameterUtil"
source: "PythonPartsFramework\Utils\PythonPart\PythonPartParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PythonPartParameterUtil

> **Pfad:** `PythonPartsFramework\Utils\PythonPart\PythonPartParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `utility`

## Übersicht

implementation of the PythonPart parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementMaterialStringTable`
- `BuildingElementStringTable`
- `ControlProperties`
- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Palette`
- `Palette.PaletteData`
- `Palette.WpfPaletteBuilder`
- `ParameterProperty`
- `StringEvaluate`
- `TypeCollections.ParameterValueList`
- `Utils.PythonPart.PythonPartParameterDataUtil`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ValueTypeUtils.PropertyPaletteControlService`
- `typing`

## Klassen

### `PythonPartParameterUtil`

implementation of the PythonPart parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, python_part_ele: AllplanEleAdapter.BaseElementAdapter, str_table: BuildingElementStringTable, material_str_table: BuildingElementMaterialStringTable` | `None` | initialize  Args:     python_part_ele:    PythonPart element     str_table:          string table     material_str_table: material string table |
| `get_label_data` | `self, doc: AllplanEleAdapter.DocumentAdapter` | `tuple[ParameterValueList, list[BuildingElement]]` | get the data for a label from the parameters  Args:     doc: document of the Allplan drawing files  Returns:     parameter value data, building element list |
| `__create_label_data` | `self, doc: AllplanEleAdapter.DocumentAdapter, prop: ParameterProperty, ctrl_props: ControlProperties, label_data: ParameterValueList, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | create the label data  Args:     doc:                   document of the Allplan drawing files     prop:                  parameter property     ctrl_props:            control properties     label_data:            label data     prop_pal_ctrl_service: property palette control service |
| `__create_attribute_id_label_data` | `doc: AllplanEleAdapter.DocumentAdapter, prop: ParameterProperty, ctrl_props: ControlProperties, label_data: ParameterValueList, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | create the label data for the value type AttributeID  Args:     doc:                   document of the Allplan drawing files     prop:                  parameter property     ctrl_props:            control properties     label_data:            label data     prop_pal_ctrl_service: property palette control service |
| `__create_attribute_label_data` | `doc: AllplanEleAdapter.DocumentAdapter, prop: ParameterProperty, ctrl_props: ControlProperties, label_data: ParameterValueList, prop_pal_ctrl_service: PropertyPaletteControlService` | `None` | create the label data for the value type Attribute  Args:     doc:                   document of the Allplan drawing files     prop:                  parameter property     ctrl_props:            control properties     label_data:            label data     prop_pal_ctrl_service: property palette control service |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the PythonPart parameter utilities
"""

from typing import cast

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Palette as AllplanPalette

from BuildingElement import BuildingElement
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementStringTable import BuildingElementStringTable
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty
from StringEvaluate import StringEvaluate

from Palette.PaletteData import PaletteData
from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ValueTypeUtils.PropertyPaletteControlService import PropertyPaletteControlService

from TypeCollections.ParameterValueList import ParameterValueList

from Utils.PythonPart.PythonPartParameterDataUtil import PythonPartParameterDataUtil

class PythonPartParameterUtil():
    """ implementation of the PythonPart parameter utilities
    """

    def __init__(self,
                 python_part_ele   : AllplanEleAdapter.BaseElementAdapter,
                 str_table         : BuildingElementStringTable,
                 material_str_table: BuildingElementMaterialStringTable):
        """ initialize

        Args:
            python_part_ele:    PythonPart element
            str_table:          string table
            material_str_table: material string table
        """

        self.python_part_ele    = python_part_ele
        self.str_table          = str_table
        self.material_str_table = material_str_table


    def get_label_data(self,
                       doc: AllplanEleAdapter.DocumentAdapter) -> tuple[ParameterValueList, list[BuildingElement]]:
        """ get the data for a label from the parameters

        Args:
            doc: document of the Allplan drawing files

        Returns:
            parameter value data, building element list
        """

        build_ele_list, build_ele_ctrl_props_list = PythonPartParameterDataUtil.get_data(self.python_part_ele,
                                                                                         self.str_table, self.material_str_table)

        if not build_ele_list:
            return ParameterValueList(), []


        #----------------- get the values from the parameter

        label_data = ParameterValueList()

        for build_ele, control_props in zip(build_ele_list, build_ele_ctrl_props_list):
            param_dict = StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0])

            prop_pal_ctrl_service = PropertyPaletteControlService(PaletteData("", param_dict, 1, "", self.str_table, build_ele, -1, False))

            for prop in build_ele.get_properties():
                if (ctrl_props := control_props.get_property(prop.name)) is not None:
                    self.__create_label_data(doc, prop, ctrl_props, label_data, prop_pal_ctrl_service)


        #----------------- exclude some value types

        label_data_excl = ParameterValueList()

        for data in label_data:
            if data.value_type not in [ParameterPropertyValueTypes.CHECK_BOX,
                                       ParameterPropertyValueTypes.RADIO_BUTTON]:
                label_data_excl.append(data)

        return label_data_excl, build_ele_list



    def __create_label_data(self,
                            doc                  : AllplanEleAdapter.DocumentAdapter,
                            prop                 : ParameterProperty,
                            ctrl_props           : ControlProperties,
                            label_data           : ParameterValueList,
                            prop_pal_ctrl_service: PropertyPaletteControlService):
        """ create the label data

        Args:
            doc:                   document of the Allplan drawing files
            prop:                  parameter property
            ctrl_props:            control properties
            label_data:            label data
            prop_pal_ctrl_service: property palette control service
        """

        #----------------- attribute parameter

        if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE:
            self.__create_attribute_id_label_data(doc, prop, ctrl_props, label_data, prop_pal_ctrl_service)

        elif prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE:
            self.__create_attribute_label_data(doc, prop, ctrl_props, label_data, prop_pal_ctrl_service)


        #----------------- add values

        elif prop.value_type.has_impl and not prop.value_type.is_tuple_type():
            if isinstance(prop.value, list):
                if prop.value:
                    prop.value = prop.value[0]
                else:
                    prop.value = prop.value_type.get_value("")

            label_data.set_attribute_id(cast(int, prop.attribute_id))

            ctrl_props.enable_condition = ctrl_props.enable_condition.replace("$list_row", "0")

            prop.value_type.add_to_palette(cast(WpfPaletteBuilder, label_data),
                                           prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def __create_attribute_id_label_data(doc                  : AllplanEleAdapter.DocumentAdapter,
                                         prop                 : ParameterProperty,
                                         ctrl_props           : ControlProperties,
                                         label_data           : ParameterValueList,
                                         prop_pal_ctrl_service: PropertyPaletteControlService):
        """ create the label data for the value type AttributeID

        Args:
            doc:                   document of the Allplan drawing files
            prop:                  parameter property
            ctrl_props:            control properties
            label_data:            label data
            prop_pal_ctrl_service: property palette control service
        """

        if isinstance(prop.value, list):
            for index, item in enumerate(prop.value):
                if not item.attribute_id:
                    continue

                label_data.set_attribute_id(item.attribute_id)

                list_prop       = prop.deep_copy()
                list_ctrl_props = ctrl_props.deep_copy()

                list_prop.value      = item
                list_prop.name       = f"{prop.name}[{index}]"
                list_ctrl_props.text = AllplanBaseEle.AttributeService.GetAttributeName(doc, item.attribute_id)

                prop.value_type.add_to_palette(cast(WpfPaletteBuilder, label_data),
                                                list_prop, list_ctrl_props, prop_pal_ctrl_service)

        else:
            label_data.set_attribute_id(prop.value.attribute_id)

            prop.value_type.add_to_palette(cast(WpfPaletteBuilder, label_data),
                                            prop, ctrl_props, prop_pal_ctrl_service)


    @staticmethod
    def __create_attribute_label_data(doc                  : AllplanEleAdapter.DocumentAdapter,
                                      prop                 : ParameterProperty,
                                      ctrl_props           : ControlProperties,
                                      label_data           : ParameterValueList,
                                      prop_pal_ctrl_service: PropertyPaletteControlService):
        """ create the label data for the value type Attribute

        Args:
            doc:                   document of the Allplan drawing files
            prop:                  parameter property
            ctrl_props:            control properties
            label_data:            label data
            prop_pal_ctrl_service: property palette control service
        """

        if isinstance(prop.value, list):
            for index, (attribute_value, attribute_id) in enumerate(zip(prop.value, cast(list, prop.attribute_id))):
                label_data.set_attribute_id(attribute_id)

                list_prop       = prop.deep_copy()
                list_ctrl_props = ctrl_props.deep_copy()

                list_prop.value            = attribute_value
                list_prop.attribute_id_str = str(attribute_id)
                list_prop.name             = f"{prop.name}[{index}]"
                list_ctrl_props.text       = AllplanBaseEle.AttributeService.GetAttributeName(doc, attribute_id)

                prop.value_type.add_to_palette(cast(WpfPaletteBuilder, label_data),
                                               list_prop, list_ctrl_props, prop_pal_ctrl_service)

        else:
            label_data.set_attribute_id(cast(int, prop.attribute_id))

            prop.value_type.add_to_palette(cast(WpfPaletteBuilder, label_data),
                                            prop, ctrl_props, prop_pal_ctrl_service)

```

</details>