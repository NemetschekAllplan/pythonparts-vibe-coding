---
title: "BuildingElementAttributeList"
source: "PythonPartsFramework\GeneralScripts\BuildingElementAttributeList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementAttributeList

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementAttributeList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the attribute list

## Abhängigkeiten

- `BuildingElement`
- `DocumentManager`
- `NemAll_Python_ArchElements`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Precast`
- `NemAll_Python_Reinforcement`
- `NemAll_Python_Utility`
- `ValueTypes.ParameterPropertyValueTypes`
- `__future__`
- `collections.abc`
- `datetime`
- `typing`

## Klassen

### `BuildingElementAttributeList`

Implementation of the attribute list
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize  |
| `add_attribute_list` | `self, attribute_list: list[AllplanBaseEle.Attribute]` | `None` | add an attribute list  Args:     attribute_list: attribute list |
| `get_attribute_list` | `self` | `list[AllplanBaseEle.Attribute]` | get the attribute list  Returns:     attribute list |
| `set_attributes_to_element` | `self, element: AllplanArchEle.AllplanElement | AllplanBasisEle.AllplanElement | AllplanPrecast.AllplanElement | AllplanReinf.AllplanElement` | `None` | set the attributes to the element  Args:     element: element |
| `add_attributes_from_parameters` | `self, build_ele: BuildingElement` | `None` | add the attributes from the parameter attributes  Args:     build_ele: building element with the parameter properties |
| `add_attribute` | `self, attribute_id: int, attribute_value: Any` | `None` | add an attribute to the list  Args:     attribute_id:    attribute ID     attribute_value: attribute value |
| `add_attribute_by_unit` | `self, attribute_id: int, attribute_value: Any` | `None` | add an attribute to the list, convert the value to the attribute unit  Args:     attribute_id:    attribute ID     attribute_value: attribute value |
| `add_attributes` | `self, attributes: list[tuple[int, Any]]` | `None` | add attributes to the list  Args:     attributes: attribute list |
| `add_attributes_by_unit` | `self, attributes: list[tuple[int, Any]]` | `None` | add attributes to the list, convert the value to the attribute unit  Args:     attributes: attribute list |
| `get_attributes_list_as_tuples` | `self` | `list[tuple[int, Any]]` | Returns a list of attribute ids and values grouped as a tuple.  Returns:     list[tuple[int, Any]]: list of attribute ids and values as a tuple. |
| `__add_attribute` | `self, attribute_id: int, attribute_value: Any, convert_to_unit: bool=False` | `None` | add an attribute to the list  Args:     attribute_id:    attribute ID     attribute_value: attribute value     convert_to_unit: state for convert the value to the attribute unit |
| `__visit_Integer` | `self, attribute_id: int, attribute_value: Any, convert_to_unit: bool` | `None` | add an integer attribute to the list  Args:     attribute_id:    attribute ID     attribute_value: attribute value     convert_to_unit: convert the value to the attribute unit state |
| `__visit_IntegerVec` | `self, attribute_id: int, attribute_value: Any, _convert_to_unit: bool` | `None` | add an integer vector attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_Double` | `self, attribute_id: int, attribute_value: Any, convert_to_unit: bool` | `None` | add a double attribute to the list  Args:     attribute_id:    attribute ID     attribute_value: attribute value     convert_to_unit: convert the value to the attribute unit state |
| `__visit_DoubleVec` | `self, attribute_id: int, attribute_value: Any, _convert_to_unit: bool` | `None` | add an double vector attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_String` | `self, attribute_id: int, attribute_value: Any, _convert_to_unit: bool` | `None` | add a string attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_WString` | `self, attribute_id: int, attribute_value: Any, _convert_to_unit: bool` | `None` | add a wide string attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_Date` | `self, attribute_id: int, attribute_value: date, _convert_to_unit: bool` | `None` | add a date attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_StringVec` | `self, attribute_id: int, attribute_value: Any, _convert_to_unit: bool` | `None` | add a string vector attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_ByteVec` | `self, attribute_id: int, attribute_value: Any, _convert_to_unit: bool` | `None` | add a byte vector attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_Enum` | `self, attribute_id: int, attribute_value: Any, _convert_to_unit: bool` | `None` | add an enum attribute to the list  Args:     attribute_id:     attribute ID     attribute_value:  attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__visit_Undef` | `self, attribute_id: int, _attribute_value: Any, _convert_to_unit: bool` | `None` | undefined attribute  Args:     attribute_id:     attribute ID     _attribute_value: attribute value     _convert_to_unit: convert the value to the attribute unit state |
| `__repr__` | `self` | `str` | create the data as string  Returns:     data string |
| `__iadd__` | `self, other: BuildingElementAttributeList` | `BuildingElementAttributeList` | implement the += operator  Args:     other: attribute list to add  Returns:     attribute list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the attribute list
"""

# pylint: disable=used-before-assignment
# pylint: disable=invalid-name
# pylint: disable=unused-private-member

from __future__ import annotations

from typing import Any, cast

from collections.abc import Callable
from datetime import date

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Utility as AllplanUtil
import NemAll_Python_Precast as AllplanPrecast
import NemAll_Python_Reinforcement as AllplanReinf

from BuildingElement import BuildingElement
from DocumentManager import DocumentManager

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

class BuildingElementAttributeList():
    """ Implementation of the attribute list
    """

    def __init__(self) -> None:
        """ initialize """

        self.__attribute_list: list[AllplanBaseEle.Attribute] = []


    def add_attribute_list(self, attribute_list: list[AllplanBaseEle.Attribute]):
        """ add an attribute list

        Args:
            attribute_list: attribute list
        """

        self.__attribute_list += attribute_list


    def get_attribute_list(self) -> list[AllplanBaseEle.Attribute]:
        """ get the attribute list

        Returns:
            attribute list
        """

        return self.__attribute_list


    def set_attributes_to_element(self,
                                  element: (AllplanArchEle.AllplanElement | AllplanBasisEle.AllplanElement | \
                                            AllplanPrecast.AllplanElement | AllplanReinf.AllplanElement)):
        """ set the attributes to the element

        Args:
            element: element
        """

        attr_set_list = [AllplanBaseEle.AttributeSet(self.__attribute_list)]

        attributes = AllplanBaseEle.Attributes(attr_set_list)

        element.Attributes = attributes


    def add_attributes_from_parameters(self,
                                       build_ele: BuildingElement):
        """ add the attributes from the parameter attributes

        Args:
            build_ele: building element with the parameter properties
        """

        for param_prop in build_ele.get_properties():
            if param_prop.value_type == ParameterPropertyValueTypes.ATTRIBUTE_ID_VALUE:
                if isinstance(param_prop.value, list):
                    _ = [self.__add_attribute(value.attribute_id, value.value, True) for value in param_prop.value]
                else:
                    self.__add_attribute(param_prop.value.attribute_id, param_prop.value.value, True)

            elif param_prop.attribute_id:
                if isinstance(param_prop.attribute_id, list):
                    _ = [self.__add_attribute(attribute_id, value, True) \
                         for attribute_id, value in zip(param_prop.attribute_id, param_prop.value)]
                else:
                    self.__add_attribute(int(param_prop.attribute_id), param_prop.value, True)


    def add_attribute(self,
                      attribute_id   : int,
                      attribute_value: Any):
        """ add an attribute to the list

        Args:
            attribute_id:    attribute ID
            attribute_value: attribute value
        """

        self.__add_attribute(attribute_id, attribute_value, False)


    def add_attribute_by_unit(self,
                              attribute_id   : int,
                              attribute_value: Any):
        """ add an attribute to the list, convert the value to the attribute unit

        Args:
            attribute_id:    attribute ID
            attribute_value: attribute value
        """

        self.__add_attribute(attribute_id, attribute_value, True)


    def add_attributes(self,
                       attributes: list[tuple[int, Any]]):
        """ add attributes to the list

        Args:
            attributes: attribute list
        """

        for attribute_id, attribute_value in attributes:
            self.add_attribute(attribute_id, attribute_value)


    def add_attributes_by_unit(self,
                               attributes: list[tuple[int, Any]]):
        """ add attributes to the list, convert the value to the attribute unit

        Args:
            attributes: attribute list
        """

        for attribute_id, attribute_value in attributes:
            self.add_attribute_by_unit(attribute_id, attribute_value)


    def get_attributes_list_as_tuples(self) -> list[tuple[int, Any]]:
        """ Returns a list of attribute ids and values grouped as a tuple.

        Returns:
            list[tuple[int, Any]]: list of attribute ids and values as a tuple.
        """

        return[(attr.Id, attr.Value) for attr in self.get_attribute_list()]


    def __add_attribute(self,
                        attribute_id   : int,
                        attribute_value: Any,
                        convert_to_unit: bool = False):
        """ add an attribute to the list

        Args:
            attribute_id:    attribute ID
            attribute_value: attribute value
            convert_to_unit: state for convert the value to the attribute unit
        """

        if not attribute_id:
            return

        doc = DocumentManager.get_instance().document

        attrib_type = AllplanBaseEle.AttributeService.GetAttributeType(doc, attribute_id)

        visitor_name = f"_BuildingElementAttributeList__visit_{attrib_type}"

        if (visitor := getattr(self, visitor_name, None)) is not None:
            cast(Callable[[int, Any, bool], None], visitor)(attribute_id, attribute_value, convert_to_unit)        #pylint: disable=not-callable
        else:
            print("not implemented", attrib_type)


    def __visit_Integer(self,
                        attribute_id   : int,
                        attribute_value: Any,
                        convert_to_unit: bool):
        """ add an integer attribute to the list

        Args:
            attribute_id:    attribute ID
            attribute_value: attribute value
            convert_to_unit: convert the value to the attribute unit state
        """

        if isinstance(attribute_value, str):
            self.__attribute_list.append(AllplanBaseEle.AttributeInteger(attribute_id, 0))
            self.__attribute_list[-1].Undefined = True
        else:
            self.__attribute_list.append(AllplanBaseEle.AttributeInteger(attribute_id, attribute_value))


    def __visit_IntegerVec(self,
                           attribute_id    : int,
                           attribute_value : Any,
                           _convert_to_unit: bool):
        """ add an integer vector attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        if not isinstance(attribute_value, AllplanUtil.VecIntList):
            int_value    = AllplanUtil.VecIntList()
            int_value[:] = attribute_value

            self.__attribute_list.append(AllplanBaseEle.AttributeIntegerVec(attribute_id, int_value))
        else:
            self.__attribute_list.append(AllplanBaseEle.AttributeIntegerVec(attribute_id, attribute_value))


    def __visit_Double(self,
                       attribute_id   : int,
                       attribute_value: Any,
                       convert_to_unit: bool):
        """ add a double attribute to the list

        Args:
            attribute_id:    attribute ID
            attribute_value: attribute value
            convert_to_unit: convert the value to the attribute unit state
        """

        if isinstance(attribute_value, str):
            self.__attribute_list.append(AllplanBaseEle.AttributeDouble(attribute_id, 0))
            self.__attribute_list[-1].Undefined = True

            return

        if convert_to_unit:
            match AllplanBaseEle.AttributeService.GetAttributeUnit(DocumentManager.get_instance().document, attribute_id):
                case "m":
                    attribute_value /= 1000

                case "m²":
                    attribute_value /= 1000000

                case "m³":
                    attribute_value /= 1000000000

                case "cm":
                    attribute_value /= 10

                case "cm²":
                    attribute_value /= 100

                case "cm³":
                    attribute_value /= 1000

        self.__attribute_list.append(AllplanBaseEle.AttributeDouble(attribute_id, attribute_value))


    def __visit_DoubleVec(self,
                          attribute_id    : int,
                          attribute_value : Any,
                          _convert_to_unit: bool):
        """ add an double vector attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        if not isinstance(attribute_value, AllplanUtil.VecDoubleList):
            double_value    = AllplanUtil.VecDoubleList()
            double_value[:] = attribute_value
            self.__attribute_list.append(AllplanBaseEle.AttributeDoubleVec(attribute_id, double_value))
        else:
            self.__attribute_list.append(AllplanBaseEle.AttributeDoubleVec(attribute_id, attribute_value))


    def __visit_String(self,
                       attribute_id    : int,
                       attribute_value : Any,
                       _convert_to_unit: bool):
        """ add a string attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        self.__attribute_list.append(AllplanBaseEle.AttributeString(attribute_id, attribute_value))


    def __visit_WString(self,
                        attribute_id    : int,
                        attribute_value : Any,
                        _convert_to_unit: bool):
        """ add a wide string attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        if attribute_id in {231, 232, 233, 235}:
            value_list = AllplanBaseEle.AttributeService.GetInputListValues(DocumentManager.get_instance().document,
                                                                            attribute_id)

            index = value_list.index(attribute_value) if attribute_value in value_list else 0

            self.__attribute_list.append(AllplanBaseEle.AttributeInteger(attribute_id, index))
        else:
            self.__attribute_list.append(AllplanBaseEle.AttributeString(attribute_id, attribute_value))


    def __visit_Date(self,
                     attribute_id    : int,
                     attribute_value : date,
                     _convert_to_unit: bool):
        """ add a date attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        if attribute_value is None:
            return

        if isinstance(attribute_value, str):
            self.__attribute_list.append(AllplanBaseEle.AttributeDate(attribute_id, 0, 0, 0))
            self.__attribute_list[-1].Undefined = True

            return

        self.__attribute_list.append(AllplanBaseEle.AttributeDate(attribute_id,
                                                                  attribute_value.day, attribute_value.month, attribute_value.year))


    def __visit_StringVec(self,
                          attribute_id    : int,
                          attribute_value : Any,
                          _convert_to_unit: bool):
        """ add a string vector attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        if not isinstance(attribute_value, AllplanUtil.VecStringList):
            string_value    = AllplanUtil.VecStringList()
            string_value[:] = attribute_value
            self.__attribute_list.append(AllplanBaseEle.AttributeStringVec(attribute_id, string_value))
        else:
            self.__attribute_list.append(AllplanBaseEle.AttributeStringVec(attribute_id, attribute_value))


    def __visit_ByteVec(self,
                        attribute_id    : int,
                        attribute_value : Any,
                        _convert_to_unit: bool):
        """ add a byte vector attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        if not isinstance(attribute_value, AllplanUtil.VecByteList):
            byte_value    = AllplanUtil.VecByteList()
            byte_value[:] = attribute_value
            self.__attribute_list.append(AllplanBaseEle.AttributeByteVec(attribute_id, byte_value))
        else:
            self.__attribute_list.append(AllplanBaseEle.AttributeByteVec(attribute_id, attribute_value))


    def __visit_Enum(self,
                     attribute_id    : int,
                     attribute_value : Any,
                     _convert_to_unit: bool):
        """ add an enum attribute to the list

        Args:
            attribute_id:     attribute ID
            attribute_value:  attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        attr_service = AllplanBaseEle.AttributeService

        if isinstance(attribute_value, int):
            self.__attribute_list.append(AllplanBaseEle.AttributeEnum(attribute_id, attribute_value))
        else:
            self.__attribute_list.append(AllplanBaseEle.AttributeEnum(attribute_id,
                                                                      attr_service.GetEnumIDFromValueString(attribute_id, attribute_value)))


    def __visit_Undef(self,                     # pylint: disable=no-self-use
                      attribute_id    : int,
                      _attribute_value: Any,
                      _convert_to_unit: bool):
        """ undefined attribute

        Args:
            attribute_id:     attribute ID
            _attribute_value: attribute value
            _convert_to_unit: convert the value to the attribute unit state
        """

        print()
        print("Attribute ", attribute_id, " is not defined in the project!!!")
        print()


    def __repr__(self) -> str:
        """ create the data as string

        Returns:
            data string
        """

        attr_str = ""

        for attr in self.__attribute_list:
            attr_str += str(attr)

        return attr_str


    def __iadd__(self,
                 other: BuildingElementAttributeList) -> BuildingElementAttributeList:
        """ implement the += operator

        Args:
            other: attribute list to add

        Returns:
            attribute list
        """

        self.__attribute_list += other.get_attribute_list()

        return self

```

</details>