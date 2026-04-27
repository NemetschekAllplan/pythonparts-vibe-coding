---
title: "PythonPartAttributeTakeoverService"
source: "PythonPartsFramework\GeneralScripts\PythonPart\PythonPartAttributeTakeoverService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# PythonPartAttributeTakeoverService

> **Pfad:** `PythonPartsFramework\GeneralScripts\PythonPart\PythonPartAttributeTakeoverService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the attribute takeover service for the PythonPart

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementAttributeList`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_Utility`
- `ParameterProperty`
- `Utilities.AttributeIdEnums`
- `ValueTypes.DateImpl`
- `ValueTypes.ParameterPropertyValueTypes`
- `datetime`
- `typing`

## Klassen

### `PythonPartAttributeTakeoverService`

Implementation of the attribute takeover service for the PythonPart
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `check_external_attribute_modification` | `build_ele_list: list[BuildingElement]` | `None` | check for an external attribute modification and adapt the values inside the building elements  Args:     build_ele_list: building element list |
| `check_external_sub_pyp_attribute_modification` | `build_ele_list: list[BuildingElement], sub_pythonpart_key: str` | `None` | check for an external attribute modification and adapt the values for a sub PythonPart of a PythonPartGroup  Args:     build_ele_list:     list with the building elements     sub_pythonpart_key: key of the sub PythonPart |
| `add_external_attributes` | `attributes: list[AllplanBaseEle.Attribute], sub_pythonpart_key: str=''` | `None` | add the missing external attributes to the attribute list  Args:     attributes:         attributes     sub_pythonpart_key: key of the sub PythonPart |
| `__get_attributes_from_sub_elements` | `pyp_ele: AllplanEleAdapter.BaseElementAdapter` | `None` | get the attributes from the sub PythonParts of the group  Args:     pyp_ele: group element |
| `__get_param_values_from_attributes` | `build_ele_list: list[BuildingElement], attr_dict: dict[int, Any]` | `None` | get the parameter values from the attributes  Args:     build_ele_list: list with the building elements     attr_dict:      attribute dict |
| `__check_attribute_list` | `prop: ParameterProperty, attr_dict: dict[int, Any]` | `None` | check for attribute list  Args:     prop:      property     attr_dict: attribute dict |
| `__check_attribute_id_value` | `prop: ParameterProperty, attr_dict: dict[int, Any]` | `None` | check for attribute id and value  Args:     prop:      property     attr_dict: attribute dict |
| `__convert_attribute_value` | `value: Any, new_value: Any, attribute_id: int` | `Any` | convert the new attribute value  Args:     value:        value     new_value:    new value     attribute_id: attribute ID  Returns:     new parameter value |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the attribute takeover service for the PythonPart
"""

from typing import Any, cast

from datetime import date

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Utility as AllplanUtil

from BuildingElement import BuildingElement
from BuildingElementAttributeList import BuildingElementAttributeList
from DocumentManager import DocumentManager
from ParameterProperty import ParameterProperty

from Utilities.AttributeIdEnums import AttributeIdEnums

from ValueTypes.DateImpl import BaseStringToValueConverter
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

EXTERNAL_ATTRIBUTES     : dict[str, dict[int, Any]] = {}
SUB_ATTRIBUTES          : dict[str, dict[int, Any]] = {}
SUB_EXTERNAL_ATTRIBUTES : dict[str, dict[int, Any]] = {}


class PythonPartAttributeTakeoverService():
    """ Implementation of the attribute takeover service for the PythonPart
    """

    @staticmethod
    def check_external_attribute_modification(build_ele_list: list[BuildingElement]):
        """ check for an external attribute modification and adapt the values inside the building elements

        Args:
            build_ele_list: building element list
        """

        pyp_ele = DocumentManager.get_instance().pythonpart_element


        #----------------- get the attributes from the sub PythonParts

        if AllplanBaseEle.PythonPartService.IsPythonPartGroupElement(pyp_ele):
            PythonPartAttributeTakeoverService.__get_attributes_from_sub_elements(pyp_ele)

            return


        #----------------- get the PyP attribute parameter values from the element attributes

        attr_dict = dict(iter(AllplanBaseEle.ElementsAttributeService.GetAttributes(pyp_ele)))

        PythonPartAttributeTakeoverService.__get_param_values_from_attributes(build_ele_list, attr_dict)

        EXTERNAL_ATTRIBUTES[str(pyp_ele.GetModelElementUUID())] = attr_dict


    @staticmethod
    def check_external_sub_pyp_attribute_modification(build_ele_list    : list[BuildingElement],
                                                      sub_pythonpart_key: str):
        """ check for an external attribute modification and adapt the values for a sub PythonPart of a PythonPartGroup

        Args:
            build_ele_list:     list with the building elements
            sub_pythonpart_key: key of the sub PythonPart
        """

        if (sub_attr := SUB_ATTRIBUTES.get(sub_pythonpart_key)) is None:
            return

        sub_attr = sub_attr.copy()

        SUB_EXTERNAL_ATTRIBUTES[sub_pythonpart_key] = sub_attr

        PythonPartAttributeTakeoverService.__get_param_values_from_attributes(build_ele_list, sub_attr)


    @staticmethod
    def add_external_attributes(attributes        : list[AllplanBaseEle.Attribute],
                                sub_pythonpart_key: str = ""):
        """ add the missing external attributes to the attribute list

        Args:
            attributes:         attributes
            sub_pythonpart_key: key of the sub PythonPart
        """

        pyp_ele = DocumentManager.get_instance().pythonpart_element

        if (external_attr_dict := SUB_EXTERNAL_ATTRIBUTES.get(sub_pythonpart_key) if sub_pythonpart_key else \
                                  EXTERNAL_ATTRIBUTES.get(str(pyp_ele.GetModelElementUUID()))) is None:
            return


        #----------------- add the missing external attributes

        build_ele_attr = BuildingElementAttributeList()

        exclude_geo = {AttributeIdEnums.RADIUS, AttributeIdEnums.X_COORDINATE, AttributeIdEnums.Y_COORDINATE,
                       AttributeIdEnums.LENGTH, AttributeIdEnums.THICKNESS, AttributeIdEnums.HEIGHT, AttributeIdEnums.VOLUME,
                       AttributeIdEnums.BASE_AREA, AttributeIdEnums.WIDTH}

        for key, value in external_attr_dict.items():
            if key not in exclude_geo and next((True for attribute in attributes if key == attribute.Id), False) is False:
                build_ele_attr.add_attribute(key, value)

        attributes += build_ele_attr.get_attribute_list()


    @staticmethod
    def __get_attributes_from_sub_elements(pyp_ele: AllplanEleAdapter.BaseElementAdapter):
        """ get the attributes from the sub PythonParts of the group

        Args:
            pyp_ele: group element
        """

        SUB_ATTRIBUTES.clear()

        for child_ele in AllplanEleAdapter.BaseElementAdapterChildElementsService.GetChildElements(pyp_ele, True):
            if not AllplanBaseEle.PythonPartService.IsPythonPartElement(child_ele):
                continue

            attr_dict = dict(iter(AllplanBaseEle.ElementsAttributeService.GetAttributes(child_ele)))

            if (sub_key := attr_dict.get(AllplanBaseEle.ATTRNR_SUB_PYTHONPART_KEY)) is not None:
                SUB_ATTRIBUTES[sub_key] = attr_dict


    @staticmethod
    def __get_param_values_from_attributes(build_ele_list: list[BuildingElement],
                                           attr_dict     : dict[int, Any]):
        """ get the parameter values from the attributes

        Args:
            build_ele_list: list with the building elements
            attr_dict:      attribute dict
        """

        for build_ele in build_ele_list:
            for prop in build_ele.get_properties():
                if prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE:
                    PythonPartAttributeTakeoverService.__check_attribute_id_value(prop, attr_dict)

                elif isinstance(prop.attribute_id, list):
                    PythonPartAttributeTakeoverService.__check_attribute_list(prop, attr_dict)

                elif prop.attribute_id:
                    if (value := attr_dict.get(prop.attribute_id)):
                        prop.value = PythonPartAttributeTakeoverService.__convert_attribute_value(prop.value, value, prop.attribute_id)

                        del attr_dict[prop.attribute_id]


    @staticmethod
    def __check_attribute_list(prop     : ParameterProperty,
                               attr_dict: dict[int, Any]):
        """ check for attribute list

        Args:
            prop:      property
            attr_dict: attribute dict
        """

        for index, attribute_id in enumerate(cast(list, prop.attribute_id)):
            if (value := attr_dict.get(attribute_id)):
                prop.value[index] = PythonPartAttributeTakeoverService.__convert_attribute_value(prop.value[index], value, attribute_id)

                del attr_dict[attribute_id]


    @staticmethod
    def __check_attribute_id_value(prop     : ParameterProperty,
                                   attr_dict: dict[int, Any]):
        """ check for attribute id and value

        Args:
            prop:      property
            attr_dict: attribute dict
        """

        if isinstance(prop.value, list):
            for value in prop.value:
                if (attr_value := attr_dict.get(value.attribute_id, None)) is not None:
                    value.value = PythonPartAttributeTakeoverService.__convert_attribute_value(value.value, attr_value, value.attribute_id)

                    del attr_dict[value.attribute_id]

                elif value.attribute_id:
                    name = AllplanBaseEle.AttributeService.GetAttributeName(DocumentManager.get_instance().document,
                                                                            value.attribute_id)

                    AllplanUtil.ShowMessageBox(f"Not possible to update value for Attribute {name}",  AllplanUtil.MB_OK)

        elif prop.value.attribute_id:
            prop.value.value = PythonPartAttributeTakeoverService.__convert_attribute_value(prop.value.value,
                                                                                    attr_dict.get(prop.value.attribute_id),
                                                                                    prop.value.attribute_id)

            del attr_dict[prop.value.attribute_id]


    @staticmethod
    def __convert_attribute_value(value       : Any,
                                  new_value   : Any,
                                  attribute_id: int) -> Any:
        """ convert the new attribute value

        Args:
            value:        value
            new_value:    new value
            attribute_id: attribute ID

        Returns:
            new parameter value
        """

        if isinstance(value, date):
            if (date_value := BaseStringToValueConverter.string_to_date(new_value, True)) is None:
                return value

            return date_value


        #----------------- convert to mm

        match AllplanBaseEle.AttributeService.GetAttributeUnit(DocumentManager.get_instance().document, attribute_id):
            case "m":
                return new_value * 1000

            case "m²":
                return new_value * 1000000

            case "m³":
                return new_value * 1000000000

            case "cm":
                return new_value * 10

            case "cm²":
                return new_value * 100

            case "cm³":
                return new_value * 1000

        return new_value

```

</details>