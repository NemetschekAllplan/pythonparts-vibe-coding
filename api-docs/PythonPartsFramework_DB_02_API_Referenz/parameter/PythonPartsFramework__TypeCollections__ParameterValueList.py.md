---
title: "ParameterValueList"
source: "PythonPartsFramework\TypeCollections\ParameterValueList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ParameterValueList

> **Pfad:** `PythonPartsFramework\TypeCollections\ParameterValueList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `werte`

## Übersicht

implementation of the parameter value list

## Abhängigkeiten

- `NemAll_Python_Palette`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ValueTypeUtils.ValueType`
- `dataclasses`
- `typing`

## Klassen

### `ParameterValueData`

implementation of the parameter value data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `ParameterValueList`

implementation of the parameter value list
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self` | `None` | initialize          |
| `set_attribute_id` | `self, attribute_id: int` | `None` | set the attribute ID  Args:     attribute_id: attribute ID |
| `AddAreaValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add an area value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddAngleValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add an angle value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddDoubleValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add a double value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddIntValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add an integer value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddLengthValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add a length value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddStringValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add a string value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddVolumeValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add a volume value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddWeightValue` | `self, text: str, name: str, value: Any, _page_index: int, _expander_name: str, row_name: str, *_args` | `None` | add a weight value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page_index:    page index     _expander_name: expander name     row_name:       row name     *_args:         additional arguments |
| `AddComboBoxValue` | `self, text: str, name: str, value: Any, _value_list: str, palette_value_type: AllplanPalette.PaletteValueType, *_args` | `None` | add a combobox  value  Args:     text:               text of the value     name:               name of the modified property     value:              value     _value_list:        value list                 palette_value_type: palette value type     *_args:             arguments |
| `AddCheckboxValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add checkbox value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddLayer` | `self, text: str, name: str, value: Any, _page: int, _expander_name: type, row_name: str, *_args` | `None` | add layer value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPenValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add pen value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddStroke` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add stroke value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddColorValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add color value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddFaceStyleValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add face style value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddHatchValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add hatch value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPatternValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add pattern value  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddMaterialButton` | `self, text: str, name: str, value: Any, _selected_value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add material value  Args:     text:            text of the value     name:            name of the modified property     value:           value     _selected_value: description     _page:           page index of the modified property     _expander_name:  expander name     row_name:        row name     *_args:          arguments |
| `AddPicture` | `self, *_args` | `None` | add a picture  Args:     *_args: arguments |
| `AddResourcePicture` | `self, *_args` | `None` | add a resource picture  Args:     *_args: arguments |
| `AddSeparator` | `self, *_args` | `None` | add a separator  Args:     *_args: arguments |
| `AddText` | `self, *_args` | `None` | add a text  Args:     *_args: arguments |
| `AddRadioButton` | `self, _group_text: str, group_name: str, text: str, _value: Any, selected_value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add an radio button value  Args:     _group_text:    description     group_name:     description     text:           text of the value     _value:         value     selected_value: description     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddButton` | `self, *_args` | `None` | add a button  Args:     *_args: arguments |
| `AddRefPointButton` | `self, text: str, name: str, _event_id: int, ref_pnt_type: int, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add a reference point button  Args:     text:           text of the value     name:           name of the modified property     _event_id:      event id of the clicked button control     ref_pnt_type:   description     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPictureButtonList` | `self, text: str, name: str, value: Any, _picture_path: type, _picture_list: type, _value_list: str, _text_list: type, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add a picture resource button list  Args:     text:           text of the value     name:           name of the modified property     value:          value     _picture_path:  description     _picture_list:  description     _value_list:    value list     _text_list:     description     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPictureResourceToggleButton` | `self, text: str, name: str, value: Any, _picture_list: type, _value_list: str, _text_list: type, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add a picture resource button list  Args:     text:           text of the value     name:           name of the modified property     value:          value     _picture_list:  description     _value_list:    value list     _text_list:     description     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPictureResourceButtonList` | `self, text: str, name: str, value: Any, _picture_list: type, _value_list: str, _text_list: type, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add a picture resource button list  Args:     text:           text of the value     name:           name of the modified property     value:          value     _picture_list:  description     _value_list:    value list     _text_list:     description     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPictureComboBox` | `self, text: str, name: str, value: Any, _picture_path: type, _picture_list: type, _value_list: str, _text_list: type, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add a picture resource button list  Args:     text:           text of the value     name:           name of the modified property     value:          value     _picture_path:  description     _picture_list:  description     _value_list:    value list     _text_list:     description     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPictureResourceComboBox` | `self, text: str, name: str, value: Any, _picture_list: type, _value_list: str, _text_list: type, _page: int, _expander_name: str, row_name: str, *_args` | `None` | add a picture resource button list  Args:     text:           text of the value     name:           name of the modified property     value:          value     _picture_list:  description     _value_list:    value list     _text_list:     description     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddPictureResourceButton` | `self, *_args` | `None` | add a picture resource button list  Args:     *_args: arguments |
| `AddPictureButton` | `self, *_args` | `None` | add a picture resource button list  Args:     *_args: arguments |
| `AddBarDiameter` | `self, text: str, name: str, value: float, _page: int, _expander_name: str, row_name: str, *_args` | `None` | function description  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddMeshType` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | function description  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddMeshGroup` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | function description  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddConcreteCoverValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | function description  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddBendingRollerValue` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | function description  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddSteelGrade` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | function description  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |
| `AddConcreteGrade` | `self, text: str, name: str, value: Any, _page: int, _expander_name: str, row_name: str, *_args` | `None` | function description  Args:     text:           text of the value     name:           name of the modified property     value:          value     _page:          page index of the modified property     _expander_name: expander name     row_name:       row name     *_args:         arguments |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the parameter value list
"""

# pylint: disable=invalid-name
# pylint: disable=too-many-public-methods

from typing import Any

from dataclasses import dataclass

import NemAll_Python_Palette as AllplanPalette

from ValueTypes.ValueTypeUtils.ValueType import ValueType
from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes

@dataclass
class ParameterValueData():
    """ implementation of the parameter value data
    """

    text        : str
    name        : str
    value       : Any
    value_type  : ValueType
    attribute_id: int


class ParameterValueList(list[ParameterValueData]):
    """ implementation of the parameter value list
    """

    def __init__(self):
        """ initialize
        """

        self.__attribute_id = 0


    def set_attribute_id(self,
                         attribute_id: int):
        """ set the attribute ID

        Args:
            attribute_id: attribute ID
        """

        self.__attribute_id = attribute_id

    def AddAreaValue(self,
                     text          : str,
                     name          : str,
                     value         : Any,
                     _page_index   : int,
                     _expander_name: str,
                     row_name      : str,
                     *_args        : Any):
        """ add an area value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.AREA, self.__attribute_id))

    def AddAngleValue(self,
                      text          : str,
                      name          : str,
                      value         : Any,
                      _page_index   : int,
                      _expander_name: str,
                      row_name      : str,
                      *_args        : Any):
        """ add an angle value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.ANGLE, self.__attribute_id))

    def AddDoubleValue(self,
                       text          : str,
                       name          : str,
                       value         : Any,
                       _page_index   : int,
                       _expander_name: str,
                       row_name      : str,
                       *_args        : Any):
        """ add a double value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.DOUBLE, self.__attribute_id))

    def AddIntValue(self,
                    text          : str,
                    name          : str,
                    value         : Any,
                    _page_index   : int,
                    _expander_name: str,
                    row_name      : str,
                    *_args        : Any):
        """ add an integer value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        if name.endswith(".DrawOrder"):
            return

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.INTEGER, self.__attribute_id))

    def AddLengthValue(self,
                       text          : str,
                       name          : str,
                       value         : Any,
                       _page_index   : int,
                       _expander_name: str,
                       row_name      : str,
                       *_args        : Any):
        """ add a length value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        if row_name:
            if (sub_part := name.rsplit(".", 1)[-1]) in {"X", "Y", "Z"}:
                text = f"{row_name} {sub_part}"
            else:
                text = row_name

        self.append(ParameterValueData(text, name, value,
                                       ParameterPropertyValueTypes.LENGTH, self.__attribute_id))

    def AddStringValue(self,
                       text          : str,
                       name          : str,
                       value         : Any,
                       _page_index   : int,
                       _expander_name: str,
                       row_name      : str,
                       *_args        : Any):
        """ add a string value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        self.append(ParameterValueData(row_name or text or name, name, value,
                                       ParameterPropertyValueTypes.STRING, self.__attribute_id))

    def AddVolumeValue(self,
                       text          : str,
                       name          : str,
                       value         : Any,
                       _page_index   : int,
                       _expander_name: str,
                       row_name      : str,
                       *_args        : Any):
        """ add a volume value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.VOLUME, self.__attribute_id))

    def AddWeightValue(self,
                       text          : str,
                       name          : str,
                       value         : Any,
                       _page_index   : int,
                       _expander_name: str,
                       row_name      : str,
                       *_args        : Any):
        """ add a weight value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page_index:    page index
            _expander_name: expander name
            row_name:       row name
            *_args:         additional arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.WEIGHT, self.__attribute_id))

    def AddComboBoxValue(self,
                         text              : str,
                         name              : str,
                         value             : Any,
                         _value_list       : str,                         
                         palette_value_type: AllplanPalette.PaletteValueType,
                         *_args            : Any):
        """ add a combobox  value

        Args:
            text:               text of the value
            name:               name of the modified property
            value:              value
            _value_list:        value list            
            palette_value_type: palette value type
            *_args:             arguments
        """

        if palette_value_type == AllplanPalette.PaletteValueType.ANGLE:
            self.append(ParameterValueData(text, name, float(value), ParameterPropertyValueTypes.ANGLE, self.__attribute_id))

        elif palette_value_type == AllplanPalette.PaletteValueType.DOUBLE:
            self.append(ParameterValueData(text, name, float(value), ParameterPropertyValueTypes.DOUBLE, self.__attribute_id))

        elif palette_value_type == AllplanPalette.PaletteValueType.INTEGER:
            self.append(ParameterValueData(text, name, int(value), ParameterPropertyValueTypes.INTEGER, self.__attribute_id))

        elif palette_value_type == AllplanPalette.PaletteValueType.LENGTH:
            self.append(ParameterValueData(text, name, float(value), ParameterPropertyValueTypes.LENGTH, self.__attribute_id))

        elif palette_value_type == AllplanPalette.PaletteValueType.STRING:
            self.append(ParameterValueData(text, name, value, ParameterPropertyValueTypes.STRING, self.__attribute_id))

    def AddCheckboxValue(self,
                         text          : str,
                         name          : str,
                         value         : Any,
                         _page         : int,
                         _expander_name: str,
                         row_name      : str,
                         *_args        : Any):
        """ add checkbox value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.CHECK_BOX, self.__attribute_id))

    def AddLayer(self,
                 text          : str,
                 name          : str,
                 value         : Any,
                 _page         : int,
                 _expander_name: type,
                 row_name      : str,
                 *_args        : Any):
        """ add layer value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.LAYER, self.__attribute_id))

    def AddPenValue(self,
                    text          : str,
                    name          : str,
                    value         : Any,
                    _page         : int,
                    _expander_name: str,
                    row_name      : str,
                    *_args        : Any):
        """ add pen value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.PEN, self.__attribute_id))



    def AddStroke(self,
                  text          : str,
                  name          : str,
                  value         : Any,
                  _page         : int,
                  _expander_name: str,
                  row_name      : str,
                  *_args        : Any):
        """ add stroke value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.STROKE, self.__attribute_id))



    def AddColorValue(self,
                      text          : str,
                      name          : str,
                      value         : Any,
                      _page         : int,
                      _expander_name: str,
                      row_name      : str,
                      *_args        : Any):
        """ add color value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.COLOR, self.__attribute_id))

    def AddFaceStyleValue(self,
                          text          : str,
                          name          : str,
                          value         : Any,
                          _page         : int,
                          _expander_name: str,
                          row_name      : str,
                          *_args        : Any):
        """ add face style value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.FACESTYLE, self.__attribute_id))

    def AddHatchValue(self,
                      text          : str,
                      name          : str,
                      value         : Any,
                      _page         : int,
                      _expander_name: str,
                      row_name      : str,
                      *_args        : Any):
        """ add hatch value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.HATCH, self.__attribute_id))

    def AddPatternValue(self,
                        text          : str,
                        name          : str,
                        value         : Any,
                        _page         : int,
                        _expander_name: str,
                        row_name      : str,
                        *_args        : Any):
        """ add pattern value

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.PATTERN, self.__attribute_id))

    def AddMaterialButton(self,
                          text           : str,
                          name           : str,
                          value          : Any,
                          _selected_value: Any,
                          _page          : int,
                          _expander_name : str,
                          row_name       : str,
                          *_args         : Any):
        """ add material value

        Args:
            text:            text of the value
            name:            name of the modified property
            value:           value
            _selected_value: description
            _page:           page index of the modified property
            _expander_name:  expander name
            row_name:        row name
            *_args:          arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.MATERIAL_BUTTON, self.__attribute_id))

    def AddPicture(self,
                   *_args: Any):
        """ add a picture

        Args:
            *_args: arguments
        """

    def AddResourcePicture(self,
                           *_args: Any):
        """ add a resource picture

        Args:
            *_args: arguments
        """

    def AddSeparator(self,
                     *_args: Any):
        """ add a separator

        Args:
            *_args: arguments
        """

    def AddText(self,
                *_args: Any):
        """ add a text

        Args:
            *_args: arguments
        """

    def AddRadioButton(self,
                       _group_text   : str,
                       group_name    : str,
                       text          : str,
                       _value        : Any,
                       selected_value: Any,
                       _page         : int,
                       _expander_name: str,
                       row_name      : str,
                       *_args        : Any):
        """ add an radio button value

        Args:
            _group_text:    description
            group_name:     description
            text:           text of the value
            _value:         value
            selected_value: description
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, group_name, selected_value,
                                       ParameterPropertyValueTypes.RADIO_BUTTON, self.__attribute_id))

    def AddButton(self,
                  *_args: Any):
        """ add a button

        Args:
            *_args: arguments
        """

    def AddRefPointButton(self,
                          text          : str,
                          name          : str,
                          _event_id     : int,
                          ref_pnt_type  : int,
                          _page         : int,
                          _expander_name: str,
                          row_name      : str,
                          *_args        : Any):
        """ add a reference point button

        Args:
            text:           text of the value
            name:           name of the modified property
            _event_id:      event id of the clicked button control
            ref_pnt_type:   description
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, ref_pnt_type,
                                       ParameterPropertyValueTypes.RADIO_BUTTON, self.__attribute_id))

    def AddPictureButtonList(self,
                             text          : str,
                             name          : str,
                             value         : Any,
                             _picture_path : type,
                             _picture_list : type,
                             _value_list   : str,
                             _text_list    : type,
                             _page         : int,
                             _expander_name: str,
                             row_name      : str,
                             *_args        : Any):
        """ add a picture resource button list

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _picture_path:  description
            _picture_list:  description
            _value_list:    value list
            _text_list:     description
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.RADIO_BUTTON, self.__attribute_id))


    def AddPictureResourceToggleButton(self,
                                       text          : str,
                                       name          : str,
                                       value         : Any,
                                       _picture_list : type,
                                       _value_list   : str,
                                       _text_list    : type,
                                       _page         : int,
                                       _expander_name: str,
                                       row_name      : str,
                                       *_args        : Any):
        """ add a picture resource button list

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _picture_list:  description
            _value_list:    value list
            _text_list:     description
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.RADIO_BUTTON, self.__attribute_id))

    def AddPictureResourceButtonList(self,
                                     text          : str,
                                     name          : str,
                                     value         : Any,
                                     _picture_list : type,
                                     _value_list   : str,
                                     _text_list    : type,
                                     _page         : int,
                                     _expander_name: str,
                                     row_name      : str,
                                     *_args        : Any):
        """ add a picture resource button list

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _picture_list:  description
            _value_list:    value list
            _text_list:     description
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.RADIO_BUTTON, self.__attribute_id))

    def AddPictureComboBox(self,
                           text          : str,
                           name          : str,
                           value         : Any,
                           _picture_path : type,
                           _picture_list : type,
                           _value_list   : str,
                           _text_list    : type,
                           _page         : int,
                           _expander_name: str,
                           row_name      : str,
                           *_args        : Any):
        """ add a picture resource button list

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _picture_path:  description
            _picture_list:  description
            _value_list:    value list
            _text_list:     description
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.RADIO_BUTTON, self.__attribute_id))


    def AddPictureResourceComboBox(self,
                                   text          : str,
                                   name          : str,
                                   value         : Any,
                                   _picture_list : type,
                                   _value_list   : str,
                                   _text_list    : type,
                                   _page         : int,
                                   _expander_name: str,
                                   row_name      : str,
                                   *_args        : Any):
        """ add a picture resource button list

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _picture_list:  description
            _value_list:    value list
            _text_list:     description
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.RADIO_BUTTON, self.__attribute_id))


    def AddPictureResourceButton(self,
                                 *_args: Any):
        """ add a picture resource button list

        Args:
            *_args: arguments
        """


    def AddPictureButton(self,
                         *_args: Any):
        """ add a picture resource button list

        Args:
            *_args: arguments
        """

    def AddBarDiameter(self,
                       text          : str,
                       name          : str,
                       value         : float,
                       _page         : int,
                       _expander_name: str,
                       row_name      : str,
                       *_args        : Any):
        """ function description

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.REINF_BAR_DIAMETER, self.__attribute_id))



    def AddMeshType(self,
                    text          : str,
                    name          : str,
                    value         : Any,
                    _page         : int,
                    _expander_name: str,
                    row_name      : str,
                    *_args        : Any):
        """ function description

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.REINF_MESH_TYPE, self.__attribute_id))

    def AddMeshGroup(self,
                     text          : str,
                     name          : str,
                     value         : Any,
                     _page         : int,
                     _expander_name: str,
                     row_name      : str,
                     *_args        : Any):
        """ function description

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.REINF_MESH_TYPE, self.__attribute_id))

    def AddConcreteCoverValue(self,
                              text          : str,
                              name          : str,
                              value         : Any,
                              _page         : int,
                              _expander_name: str,
                              row_name      : str,
                              *_args        : Any):
        """ function description

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """

        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.REINF_MESH_TYPE, self.__attribute_id))

    def AddBendingRollerValue(self,
                              text          : str,
                              name          : str,
                              value         : Any,
                              _page         : int,
                              _expander_name: str,
                              row_name      : str,
                              *_args        : Any):
        """ function description

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """
        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.REINF_MESH_TYPE, self.__attribute_id))

    def AddSteelGrade(self,
                      text          : str,
                      name          : str,
                      value         : Any,
                      _page         : int,
                      _expander_name: str,
                      row_name      : str,
                      *_args        : Any):
        """ function description

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """
        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.REINF_MESH_TYPE, self.__attribute_id))

    def AddConcreteGrade(self,
                         text          : str,
                         name          : str,
                         value         : Any,
                         _page         : int,
                         _expander_name: str,
                         row_name      : str,
                         *_args        : Any):
        """ function description

        Args:
            text:           text of the value
            name:           name of the modified property
            value:          value
            _page:          page index of the modified property
            _expander_name: expander name
            row_name:       row name
            *_args:         arguments
        """
        self.append(ParameterValueData(row_name if row_name else text, name, value,
                                       ParameterPropertyValueTypes.REINF_MESH_TYPE, self.__attribute_id))


    # def AddFixtureValues(self, path, _file, _entry, name, value,
    #                      _page, _expander_name, row_name, _is_control_enabled,
    #                      _height, _width, _font_face_code):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, path.split(" ")[0] , name, str(value))

    # def AddPointFixtureCatalogRef(self, text, name, value,
    #                               _page, _expander_name, row_name, _is_control_enabled,
    #                               _height, _width, _font_face_code):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddFactoryCatalogRef(self, text, name, value,
    #                               _page, _expander_name, row_name, _is_control_enabled):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddPrecastElementTypeCatalogRef(self, text, name, value,
    #                               _page, _expander_name, row_name, _is_control_enabled):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddConcreteGradeCatalogRef(self, text, name, value,
    #                               _page, _expander_name, row_name, _is_control_enabled):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddInsulationCatalogRef(self, text, name, value,
    #                             _page, _expander_name, row_name, _is_control_enabled):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddBrickTileCatalogRef(self, text, name, value,
	# 						   _page, _expander_name, row_name, _is_control_enabled):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddNormCatalogRef(self, text, name, value,
    #                               _page, _expander_name, row_name, _is_control_enabled):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddSurfaceCatalogRef(self, text, name, value,
    #                               _page, _expander_name, row_name, _is_control_enabled):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))

    # def AddPlaneReferencesButton(self, text, name, value,
    #                              _page, _expander_name, row_name, _is_control_enabled,
    #                              _height, _width, _font_face_code):
    #     self.add_expander(expander_name)
    #     self.add_control(row_name, text, name, str(value))


    # def IsConcreteCoverPaletteUpdate(self, _cover) -> bool:
    #     return True

```

</details>