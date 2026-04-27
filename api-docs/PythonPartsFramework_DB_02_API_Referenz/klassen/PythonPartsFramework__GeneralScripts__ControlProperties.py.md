---
title: "ControlProperties"
source: "PythonPartsFramework\GeneralScripts\ControlProperties.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# ControlProperties

> **Pfad:** `PythonPartsFramework\GeneralScripts\ControlProperties.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the control properties class

## Abhängigkeiten

- `DialogTypes.ValueDialogType`
- `Utilities.ConditionUtil`
- `Utilities.GeneralConstants`
- `__future__`
- `collections.abc`
- `enum`
- `typing`

## Klassen

### `ControlProperties`

Implementation of the control properties class

    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, text: str, value_name: str, enable_condition: str, visible_condition: str, page: int, expander_name: str, row_name: str, value_str: str, value_list: str, value_list_2: str, event_id: str, control_type: ControlType=ControlType.CONTROL, value_index_name: str='', value_list_start_row: int=0, value_dialog: ValueDialogType | None=None, value_list_textids: str='', as_slider: bool=False, height: str='22', width: str=DEFAULT_WIDTH, font_style: int=2, font_face_code: int=0, background_color: str='', row_state_key: str='', expander_state_key: str=''` | `None` | Set the properties of the control  Args:     text:                 Text of the control     value_name:           Name of the assigned value from the building element     enable_condition:     Condition for enabled state of the control     visible_condition:    Condition for visible state of the control     page:                 page index of the modified property     expander_name:        Expander name     row_name:             row_name     value_str:            Control value as string     value_list:           Text with the values for the combo box list like  1|2|5|7 or     value_list_2:         Second string list separated by | example 1|2|5|7 or     event_id:             event id of the clicked button control     control_type:         Type of the control     value_index_name:     Index name of the value (in case of list with single value by value index)     value_list_start_row: Start row of the value list row numbering inside the palette     value_dialog:         Dialog type for the value input     value_list_textids:   text ID's of the value list     as_slider:            Show the control as slider     height:               Control height in pixel, only used in a row     width:                Control width in pixel, only used in a row     font_style:           font style     font_face_code:       font face code     background_color:     Background color in the format "(red, green, blue)" with "(-1, -1, -1)" or "" as default     row_state_key:        row state key     expander_state_key:   expander state key |
| `__repr__` | `self` | `str` | create the string from the values  Returns:     string from the values |
| `text` | `self` | `str` | Get the control text  Returns:     control text |
| `text` | `self, text: str` | `None` | Set the control text  Args:     text: control text |
| `group_text` | `self` | `str` | Get the group text of the property  Returns:     text of the property. |
| `group_text` | `self, group_text: str` | `None` | Set the group text of the property  Args:     group_text: new text. |
| `member_text` | `self` | `dict[str, str]` | Get the member text of the property members  Returns:     text of the property members |
| `member_text` | `self, member_text: dict[str, str]` | `None` | Set the member text of the property members  Args:     member_text: of the property members |
| `set_member_text` | `self, member_name: str, member_text: str` | `None` | Set the member text of the property member  Args:     member_name: member name     member_text: member text |
| `enable_condition` | `self` | `str` | Get the enable condition of the control  Returns:     enable condition |
| `enable_condition` | `self, condition: str` | `None` | Set enable condition of the control  Args:     condition: enable condition |
| `visible_condition` | `self` | `str` | Get the visible condition of the control  Returns:     visible condition |
| `visible_condition` | `self, condition: str` | `None` | Set visible condition of the control  Args:     condition: visible condition |
| `enable_function` | `self` | `Callable[..., bool] | None` | Get the enable function of the control  Returns:     enable function |
| `enable_function` | `self, function: Callable[..., bool] | None` | `None` | Set enable function of the control  Args:     function: enable function |
| `visible_function` | `self` | `Callable[..., bool] | None` | Get the visible function of the control  Returns:     visible function |
| `visible_function` | `self, function: Callable[..., bool] | None` | `None` | Set visible function of the control  Args:     function: visible function |
| `value_name` | `self` | `str` | Get the name of the assigned value from the building element  Returns:     value name |
| `value_name` | `self, value_name: str` | `None` | Set the name of the assigned value from the building element  Args:     value_name: value name |
| `value_str` | `self` | `str` | Get the control value string  Returns:     value string |
| `value_list` | `self` | `str` | Get the values for the value list list like  1|2|...|...  Returns:     value list |
| `value_list` | `self, value_list: str` | `None` | Set the value list  Args:     value_list: value list |
| `value_text_list` | `self` | `str` | Get the text corresponding to the value list like  Rectangle|Circle|...|...  Returns:     value list |
| `value_text_list` | `self, value_text_list: str` | `None` | Set the value list  Args:     value_text_list: value list |
| `value_list_2` | `self` | `str` | Get the second value list  Returns:     second value list |
| `value_list_2` | `self, value_list_2: str` | `None` | Set the value list  Args:     value_list_2: second value list |
| `value_list_textids` | `self` | `str` | Get the second value list  Returns:     value list text IDs |
| `visible` | `self` | `bool | list[bool]` | Get the visible state of the control  Returns:     visible state |
| `visible` | `self, visible: bool | list[bool]` | `None` | Set the visible state of the control  Args:     visible: visible state |
| `enable` | `self` | `bool` | Get the enable state of the control  Returns:     enable state |
| `enable` | `self, enable: bool` | `None` | Set the enable state of the control  Args:     enable: enable state |
| `event_id` | `self` | `str` | Get the event id of the control  Returns:     event ID |
| `event_id` | `self, event_id: str` | `None` | Set the event id of the control  Args:     event_id: event id of the clicked button control |
| `row_name` | `self` | `str` | Get the row name of the control  Returns:     row name. |
| `row_name` | `self, row_name: str` | `None` | Set the row name of the control  Args:     row_name: row name |
| `row_state_key` | `self` | `str` | Get the row state key of the control  Returns:     row state key. |
| `row_state_key` | `self, row_state_key: str` | `None` | Set the row state key of the control  Args:     row_state_key: row state key |
| `expander_state_key` | `self` | `str` | Get the expander state key of the control  Returns:     expander state key. |
| `expander_state_key` | `self, expander_state_key: str` | `None` | Set the expander state key of the control  Args:     expander_state_key: expander state key |
| `page` | `self` | `int` | Get the page of the control  Returns:     page number. |
| `page` | `self, page: int` | `None` | Set the page of the control  Args:     page: page index of the modified property |
| `expander_name` | `self` | `str` | Get the name of the current expander control  Returns:     expander name of the control. |
| `expander_name` | `self, expander_name: str` | `None` | Set the name of the current expander control  Args:     expander_name: expander name |
| `min_value_condition` | `self` | `str` | Get the min value condition of the control  Returns:     minimal value condition |
| `min_value_condition` | `self, condition: str` | `None` | Set min value condition of the control  Args:     condition: min value condition |
| `max_value_condition` | `self` | `str` | Get the max value condition of the control  Returns:     maximal value condition |
| `max_value_condition` | `self, condition: str` | `None` | Set max value condition of the control  Args:     condition: max value condition |
| `min_value` | `self` | `int | float` | Get the min value of the control  Returns:     minimal value |
| `min_value` | `self, value: int | float` | `None` | Set min value of the control  Args:     value: minimal value |
| `max_value` | `self` | `int | float` | Get the max value of the control  Returns:     maximal value |
| `max_value` | `self, value: int | float` | `None` | Set max value of the control  Args:     value: maximal value |
| `interval_value` | `self` | `str` | Get the interval value of the control  Returns:     interval value |
| `interval_value` | `self, value: str` | `None` | Set interval value of the control  Args:     value: interval value |
| `constraint` | `self` | `list[str]` | Get the constraint name of the control  Returns:     constraint |
| `constraint` | `self, value: list[str]` | `None` | Set the constraint name of the control  Args:     value: constraint value |
| `control_type` | `self` | `ControlType` | Get the control type of the control  Returns:     control type |
| `control_type` | `self, value: ControlType` | `None` | Set the control type of the control  Args:     value: control type |
| `as_slider` | `self` | `bool` | Get the control as slider state  Returns:     control as slider state |
| `as_slider` | `self, value: bool` | `None` | Set the slider state of the control  Args:     value: control as slider state |
| `value_index_name` | `self` | `str` | Get the value index name of the control  Returns:     value index name |
| `value_index_name` | `self, value: str` | `None` | Set the value index name of the control  Args:     value: value index name |
| `value_index_name_base` | `self` | `int` | Get the value index name base of the control  Returns:     value index name base |
| `value_index_name_base` | `self, value: int` | `None` | Set the value index name base of the control  Args:     value: value index name base |
| `value_list_start_row` | `self` | `int` | Get the start row of the value list row numbering inside the palette  Returns:     value list start row |
| `value_list_start_row` | `self, value: int` | `None` | Set the start row of the value list row numbering inside the palette  Args:     value: value list start row |
| `list_group_name` | `self` | `str` | Get the name of the list group  Returns:     name of the list group |
| `list_group_name` | `self, list_group_name: str` | `None` | Set the name of the list group  Args:     list_group_name: name of the list group |
| `value_dialog` | `self` | `ValueDialogType | None` | Get the dialog name for the value input dialog  Returns:     dialog name for the value input dialog |
| `value_dialog` | `self, value: ValueDialogType | None` | `None` | Set the dialog name for the value input dialog  Args:     value: dialog name for the value input dialog |
| `height` | `self` | `int` | Get the height of the control  Returns:     height of the control |
| `height` | `self, height: str` | `None` | Set the height of the control  Args:     height: height of the control |
| `width` | `self` | `int` | Get the width of the control  Returns:     width of the control |
| `width` | `self, width: str | int` | `None` | Set the width of the control  Args:     width: width of the control |
| `font_style` | `self` | `int` | Get the font style of the control  Returns:     font style of the control |
| `font_style` | `self, font_style: int` | `None` | Set the font style of the control  Args:     font_style: font style of the control |
| `font_face_code` | `self` | `int` | Get the font face code of the control  Returns:     font face code of the control |
| `font_face_code` | `self, font_face_code: int` | `None` | Set the font face code of the control  Args:     font_face_code: font face code of the control |
| `background_color` | `self` | `str` | Get the background color of the control  Returns:     background color of the control |
| `background_color` | `self, background_color: str` | `None` | Set the background color of the control  Args:     background_color: background color of the control |
| `refresh_control` | `self` | `bool` | Get the refresh control state  Returns:     refresh control state |
| `reset_refresh_control` | `self` | `None` | reset the refresh state of the control  |
| `modify_visible_condition` | `self, value_name: str, value: str` | `None` | Modify the visible condition  Args:     value_name: Name of the value     value:      condition value |
| `set_visible_condition` | `self, value_name: str, condition: str` | `None` | Set the visible condition of the property  Args:     value_name: Name of the value     condition:  Visible condition |
| `palette_layout_dict` | `self` | `dict[str, Any]` | get the palette layout dictionary  Returns:     palette layout dictionary |
| `palette_layout_dict` | `self, palette_layout_dict: dict[str, Any]` | `None` | set the palette layout dictionary  Args:     palette_layout_dict: palette layout dictionary |
| `list_index_offset` | `self` | `int` | Get the list index offset  Returns:     list index offset |
| `list_index_offset` | `self, list_index_offset: int` | `None` | Set the list index offset  Args:     list_index_offset: list index offset |
| `deep_copy` | `self` | `ControlProperties` | deep copy of the data  Returns:     copied control properties |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the control properties class
"""

# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=too-many-public-methods

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import enum

from collections.abc import Callable

from Utilities.ConditionUtil import ConditionUtil
from Utilities.GeneralConstants import GeneralConstants

if TYPE_CHECKING:
    from DialogTypes.ValueDialogType import ValueDialogType

class ControlProperties():
    """ Implementation of the control properties class

    """

    DEFAULT_WIDTH = "30"
    FALSE_STR     = "False"

    class ControlType(enum.IntEnum):
        """ Definition of class ControlType
        """

        CONTROL      = 1
        EXPANDER     = 2
        ROW          = 3


    def __init__(self,
                 text                 : str,
                 value_name           : str,
                 enable_condition     : str,
                 visible_condition    : str,
                 page                 : int,
                 expander_name        : str,
                 row_name             : str,
                 value_str            : str,
                 value_list           : str,
                 value_list_2         : str,
                 event_id             : str,
                 control_type         : ControlType              = ControlType.CONTROL,
                 value_index_name     : str                      = "",
                 value_list_start_row: int                       = 0,
                 value_dialog         : (ValueDialogType | None) = None,
                 value_list_textids   : str                      = "",
                 as_slider            : bool                     = False,
                 height               : str                      = "22",
                 width                : str                      = DEFAULT_WIDTH,
                 font_style           : int                      = 2,
                 font_face_code       : int                      = 0,
                 background_color     : str                      = "",
                 row_state_key        : str                      = "",
                 expander_state_key   : str                      = "")                :
        """ Set the properties of the control

        Args:
            text:                 Text of the control
            value_name:           Name of the assigned value from the building element
            enable_condition:     Condition for enabled state of the control
            visible_condition:    Condition for visible state of the control
            page:                 page index of the modified property
            expander_name:        Expander name
            row_name:             row_name
            value_str:            Control value as string
            value_list:           Text with the values for the combo box list like  1|2|5|7 or
            value_list_2:         Second string list separated by | example 1|2|5|7 or
            event_id:             event id of the clicked button control
            control_type:         Type of the control
            value_index_name:     Index name of the value (in case of list with single value by value index)
            value_list_start_row: Start row of the value list row numbering inside the palette
            value_dialog:         Dialog type for the value input
            value_list_textids:   text ID's of the value list
            as_slider:            Show the control as slider
            height:               Control height in pixel, only used in a row
            width:                Control width in pixel, only used in a row
            font_style:           font style
            font_face_code:       font face code
            background_color:     Background color in the format "(red, green, blue)" with "(-1, -1, -1)" or "" as default
            row_state_key:        row state key
            expander_state_key:   expander state key
        """

        self.__text                 = text
        self.__group_text           = ""
        self.__enable_condition     = enable_condition
        self.__visible_condition    = visible_condition
        self.__value_name           = value_name
        self.__value_str            = value_str
        self.__value_list           = value_list
        self.__value_list_2         = value_list_2
        self.__value_list_textids   = value_list_textids
        self.__value_index_name     = value_index_name
        self.__value_list_start_row = value_list_start_row
        self.__event_id             = event_id
        self.__page                 = page
        self.__expander_name        = expander_name
        self.__row_name             = row_name
        self.__row_state_key        = row_state_key
        self.__expander_state_key   = expander_state_key
        self.__control_type         = control_type
        self.__as_slider            = as_slider
        self.__value_dialog         = value_dialog
        self.__height               = height
        self.__width                = width
        self.__font_style           = font_style
        self.__font_face_code       = font_face_code
        self.__background_color     = background_color

        self.__visible               : (bool | list[bool])          = True
        self.__enable                : bool                         = True
        self.__min_value_condition   : str                          = ""
        self.__max_value_condition   : str                          = ""
        self.__interval_value        : str                          = ""
        self.__constraint            : list[str]                    = []
        self.__list_group_name       : str                          = ""
        self.__value_text_list       : str                          = ""
        self.__refresh_control       : bool                         = False
        self.__min_value             : (int | float)                = 0
        self.__max_value             : (int | float)                = 0
        self.__member_text           : dict[str, str]               = {}
        self.__visible_function      : (Callable[..., bool] | None) = None
        self.__enable_function       : (Callable[..., bool] | None) = None
        self.__palette_layout_dict   : dict[str, Any]               = {}
        self.__list_index_offset     : int                          = 0
        self.__value_index_name_base : int                          = 1

    def __repr__(self) -> str:
        """ create the string from the values

        Returns:
            string from the values
        """

        return f"{self.__class__.__name__}(\n" \
               f"   text:                 {self.__text}\n" \
               f"   group_text:           {self.__group_text}\n" \
               f"   member_text:          {self.__member_text}\n" \
               f"   enable_condition:     {self.__enable_condition}\n" \
               f"   visible_condition:    {self.__visible_condition}\n" \
               f"   value_name:           {self.__value_name}\n" \
               f"   value_str:            {self.__value_str}\n" \
               f"   value_list:           {self.__value_list}\n" \
               f"   value_text_list:      {self.__value_text_list}\n" \
               f"   value_list_2:         {self.__value_list_2}\n" \
               f"   value_index_name:     {self.__value_index_name}\n" \
               f"   value_list_start_row: {self.__value_list_start_row}\n" \
               f"   enable:               {self.__enable}\n" \
               f"   visible:              {self.__visible}\n" \
               f"   event_id:             {self.__event_id}\n" \
               f"   page:                 {self.__page}\n" \
               f"   expander_name:        {self.__expander_name}\n" \
               f"   row_name:             {self.__row_name}\n" \
               f"   row_state_key:        {self.__row_state_key}\n" \
               f"   expander_state_key:   {self.__expander_state_key}\n" \
               f"   min_value_condition:  {self.__min_value_condition}\n" \
               f"   max_value_condition:  {self.__max_value_condition}\n" \
               f"   min_value:            {self.__min_value}\n" \
               f"   max_value:            {self.__max_value}\n" \
               f"   interval_value:       {self.__interval_value}\n" \
               f"   constraint:           {self.__constraint}\n" \
               f"   control_type:         ControlType.{self.__control_type.name}\n" \
               f"   as_slider:            {self.__as_slider}\n" \
               f"   value_dialog:         {str(self.__value_dialog)}\n" \
               f"   visible_function:     {self.__visible_function}\n" \
               f"   enable_function:      {self.__enable_function}\n" \
               f"   list_group_name:      {self.__list_group_name}\n" \
               f"   height:               {self.__height}\n" \
               f"   width:                {self.__width}\n" \
               f"   font_style:           {self.__font_style}\n" \
               f"   font_face_code:       {self.__font_face_code}\n" \
               f"   background_color:     {self.__background_color}\n" \
               f")\n"


    @property
    def text(self) -> str:
        """ Get the control text

        Returns:
            control text
        """
        return self.__text

    @text.setter
    def text(self,
             text: str):
        """ Set the control text

        Args:
            text: control text
        """
        self.__text = text

    @property
    def group_text(self) -> str:
        """ Get the group text of the property

        Returns:
            text of the property.
        """
        return self.__group_text

    @group_text.setter
    def group_text(self,
                   group_text: str):
        """ Set the group text of the property

        Args:
            group_text: new text.
        """
        self.__group_text = group_text

    @property
    def member_text(self) -> dict[str, str]:
        """ Get the member text of the property members

        Returns:
            text of the property members
        """
        return self.__member_text

    @member_text.setter
    def member_text(self,
                    member_text: dict[str, str]):
        """ Set the member text of the property members

        Args:
            member_text: of the property members
        """
        self.__member_text = member_text

    def set_member_text(self,
                        member_name: str,
                        member_text: str):
        """ Set the member text of the property member

        Args:
            member_name: member name
            member_text: member text
        """
        self.__member_text[member_name] = member_text

    @property
    def enable_condition(self) -> str:
        """ Get the enable condition of the control

        Returns:
            enable condition
        """
        return self.__enable_condition

    @enable_condition.setter
    def enable_condition(self,
                         condition: str):
        """ Set enable condition of the control

        Args:
            condition: enable condition
        """

        self.__enable_condition = condition

    @property
    def visible_condition(self) -> str:
        """ Get the visible condition of the control

        Returns:
            visible condition
        """
        return self.__visible_condition

    @visible_condition.setter
    def visible_condition(self,
                          condition: str):
        """ Set visible condition of the control

        Args:
            condition: visible condition
        """

        self.__visible_condition = condition

    @property
    def enable_function(self) -> (Callable[..., bool] | None):
        """ Get the enable function of the control

        Returns:
            enable function
        """
        return self.__enable_function

    @enable_function.setter
    def enable_function(self,
                        function: (Callable[..., bool] | None)):
        """ Set enable function of the control

        Args:
            function: enable function
        """

        self.__enable_function = function

    @property
    def visible_function(self) -> (Callable[..., bool] | None):
        """ Get the visible function of the control

        Returns:
            visible function
        """
        return self.__visible_function

    @visible_function.setter
    def visible_function(self,
                         function: (Callable[..., bool] | None)):
        """ Set visible function of the control

        Args:
            function: visible function
        """

        self.__visible_function = function

    @property
    def value_name(self) -> str:
        """ Get the name of the assigned value from the building element

        Returns:
            value name
        """
        return self.__value_name

    @value_name.setter
    def value_name(self,
                   value_name: str):
        """ Set the name of the assigned value from the building element

        Args:
            value_name: value name
        """
        self.__value_name = value_name

    @property
    def value_str(self) -> str:
        """ Get the control value string

        Returns:
            value string
        """
        return self.__value_str

    @property
    def value_list(self) -> str:
        """ Get the values for the value list list like  1|2|...|...

        Returns:
            value list
        """
        return self.__value_list

    @value_list.setter
    def value_list(self,
                   value_list: str):
        """ Set the value list

        Args:
            value_list: value list
        """

        if self.__value_list != value_list:
            self.__value_list      = value_list
            self.__refresh_control = True

    @property
    def value_text_list(self) -> str:
        """ Get the text corresponding to the value list like  Rectangle|Circle|...|...

        Returns:
            value list
        """
        return self.__value_text_list

    @value_text_list.setter
    def value_text_list(self,
                   value_text_list: str):
        """ Set the value list

        Args:
            value_text_list: value list
        """

        self.__value_text_list = value_text_list

    @property
    def value_list_2(self) -> str:
        """ Get the second value list

        Returns:
            second value list
        """
        return self.__value_list_2

    @value_list_2.setter
    def value_list_2(self,
                     value_list_2: str):
        """ Set the value list

        Args:
            value_list_2: second value list
        """

        if self.__value_list != value_list_2:
            self.__value_list_2    = value_list_2
            self.__refresh_control = True

    @property
    def value_list_textids(self) -> str:
        """ Get the second value list

        Returns:
            value list text IDs
        """
        return self.__value_list_textids

    @property
    def visible(self) -> (bool | list[bool]):
        """ Get the visible state of the control

        Returns:
            visible state
        """
        return self.__visible


    @visible.setter
    def visible(self,
                visible: (bool | list[bool])):
        """ Set the visible state of the control

        Args:
            visible: visible state
        """
        self.__visible = visible

    @property
    def enable(self) -> bool:
        """ Get the enable state of the control

        Returns:
            enable state
        """
        return self.__enable


    @enable.setter
    def enable(self,
               enable: bool):
        """ Set the enable state of the control

        Args:
            enable: enable state
        """
        self.__enable = enable

    @property
    def event_id(self) -> str:
        """ Get the event id of the control

        Returns:
            event ID
        """
        return self.__event_id

    @event_id.setter
    def event_id(self,
                 event_id: str):
        """ Set the event id of the control

        Args:
            event_id: event id of the clicked button control
        """
        self.__event_id = event_id

    @property
    def row_name(self) -> str:
        """ Get the row name of the control

        Returns:
            row name.
        """
        return self.__row_name

    @row_name.setter
    def row_name(self,
                 row_name: str):
        """ Set the row name of the control

        Args:
            row_name: row name
        """

        self.__row_name = row_name

    @property
    def row_state_key(self) -> str:
        """ Get the row state key of the control

        Returns:
            row state key.
        """
        return self.__row_state_key

    @row_state_key.setter
    def row_state_key(self,
                      row_state_key: str):
        """ Set the row state key of the control

        Args:
            row_state_key: row state key
        """

        self.__row_state_key = row_state_key

    @property
    def expander_state_key(self) -> str:
        """ Get the expander state key of the control

        Returns:
            expander state key.
        """
        return self.__expander_state_key

    @expander_state_key.setter
    def expander_state_key(self,
                           expander_state_key: str):
        """ Set the expander state key of the control

        Args:
            expander_state_key: expander state key
        """

        self.__expander_state_key = expander_state_key

    @property
    def page(self) -> int:
        """ Get the page of the control

        Returns:
            page number.
        """
        return self.__page

    @page.setter
    def page(self,
             page: int):
        """ Set the page of the control

        Args:
            page: page index of the modified property
        """
        self.__page = page

    @property
    def expander_name(self) -> str:
        """ Get the name of the current expander control

        Returns:
            expander name of the control.
        """
        return self.__expander_name

    @expander_name.setter
    def expander_name(self,
                      expander_name: str):
        """ Set the name of the current expander control

        Args:
            expander_name: expander name
        """
        self.__expander_name = expander_name

    @property
    def min_value_condition(self) -> str:
        """ Get the min value condition of the control

        Returns:
            minimal value condition
        """
        return self.__min_value_condition

    @min_value_condition.setter
    def min_value_condition(self,
                            condition: str):
        """ Set min value condition of the control

        Args:
            condition: min value condition
        """

        self.__min_value_condition = condition

    @property
    def max_value_condition(self) -> str:
        """ Get the max value condition of the control

        Returns:
            maximal value condition
        """
        return self.__max_value_condition

    @max_value_condition.setter
    def max_value_condition(self,
                            condition: str):
        """ Set max value condition of the control

        Args:
            condition: max value condition
        """

        self.__max_value_condition = condition

    @property
    def min_value(self) -> (int | float):
        """ Get the min value of the control

        Returns:
            minimal value
        """
        return self.__min_value

    @min_value.setter
    def min_value(self,
                  value: (int | float)):
        """ Set min value of the control

        Args:
            value: minimal value
        """

        self.__min_value = value

    @property
    def max_value(self) -> (int | float):
        """ Get the max value of the control

        Returns:
            maximal value
        """
        return self.__max_value

    @max_value.setter
    def max_value(self,
                  value: (int | float)):
        """ Set max value of the control

        Args:
            value: maximal value
        """

        self.__max_value = value

    @property
    def interval_value(self) -> str:
        """ Get the interval value of the control

        Returns:
            interval value
        """
        return self.__interval_value

    @interval_value.setter
    def interval_value(self,
                       value: str):
        """ Set interval value of the control

        Args:
            value: interval value
        """

        self.__interval_value = value

    @property
    def constraint(self) -> list[str]:
        """ Get the constraint name of the control

        Returns:
            constraint
        """
        return self.__constraint

    @constraint.setter
    def constraint(self,
                   value: list[str]):
        """ Set the constraint name of the control

        Args:
            value: constraint value
        """

        self.__constraint = value

    @property
    def control_type(self) -> ControlType:
        """ Get the control type of the control

        Returns:
            control type
        """
        return self.__control_type

    @control_type.setter
    def control_type(self,
                     value: ControlType):
        """ Set the control type of the control

        Args:
            value: control type
        """

        self.__control_type = value

    @property
    def as_slider(self) -> bool:
        """ Get the control as slider state

        Returns:
            control as slider state
        """
        return self.__as_slider

    @as_slider.setter
    def as_slider(self,
                  value: bool):
        """ Set the slider state of the control

        Args:
            value: control as slider state
        """

        self.__as_slider = value

    @property
    def value_index_name(self) -> str:
        """ Get the value index name of the control

        Returns:
            value index name
        """
        return self.__value_index_name

    @value_index_name.setter
    def value_index_name(self,
                         value: str):
        """ Set the value index name of the control

        Args:
            value: value index name
        """
        self.__value_index_name = value

    @property
    def value_index_name_base(self) -> int:
        """ Get the value index name base of the control

        Returns:
            value index name base
        """
        return self.__value_index_name_base

    @value_index_name_base.setter
    def value_index_name_base(self,
                              value: int):
        """ Set the value index name base of the control

        Args:
            value: value index name base
        """
        self.__value_index_name_base = value

    @property
    def value_list_start_row(self) -> int:
        """ Get the start row of the value list row numbering inside the palette

        Returns:
            value list start row
        """
        return self.__value_list_start_row

    @value_list_start_row.setter
    def value_list_start_row(self,
                             value: int):
        """ Set the start row of the value list row numbering inside the palette

        Args:
            value: value list start row
        """
        self.__value_list_start_row = value

    @property
    def list_group_name(self) -> str:
        """ Get the name of the list group

        Returns:
            name of the list group
        """
        return self.__list_group_name

    @list_group_name.setter
    def list_group_name(self,
                        list_group_name: str):
        """ Set the name of the list group

        Args:
            list_group_name: name of the list group
        """
        self.__list_group_name = list_group_name

    @property
    def value_dialog(self) -> (ValueDialogType | None):
        """ Get the dialog name for the value input dialog

        Returns:
            dialog name for the value input dialog
        """
        return self.__value_dialog

    @value_dialog.setter
    def value_dialog(self,
                     value: (ValueDialogType | None)):
        """ Set the dialog name for the value input dialog

        Args:
            value: dialog name for the value input dialog
        """

        self.__value_dialog = value

    @property
    def height(self) -> int:
        """ Get the height of the control

        Returns:
            height of the control
        """

        if self.__height.isnumeric():
            return int(self.__height)

        return int(eval(self.__height, self.__palette_layout_dict))     # pylint: disable=eval-used

    @height.setter
    def height(self,
               height: str):
        """ Set the height of the control

        Args:
            height: height of the control
        """
        self.__height = height

    @property
    def width(self) -> int:
        """ Get the width of the control

        Returns:
            width of the control
        """

        if self.__width.isnumeric():
            return int(self.__width)

        return int(eval(self.__width, self.__palette_layout_dict))   # pylint: disable=eval-used

    @width.setter
    def width(self,
              width: (str | int)):
        """ Set the width of the control

        Args:
            width: width of the control
        """

        self.__width = str(width)

    @property
    def font_style(self) -> int:
        """ Get the font style of the control

        Returns:
            font style of the control
        """
        return self.__font_style

    @font_style.setter
    def font_style(self,
                   font_style: int):
        """ Set the font style of the control

        Args:
            font_style: font style of the control
        """
        self.__font_style = font_style

    @property
    def font_face_code(self) -> int:
        """ Get the font face code of the control

        Returns:
            font face code of the control
        """
        return self.__font_face_code

    @font_face_code.setter
    def font_face_code(self,
                       font_face_code: int):
        """ Set the font face code of the control

        Args:
            font_face_code: font face code of the control
        """
        self.__font_face_code = font_face_code

    @property
    def background_color(self) -> str:
        """ Get the background color of the control

        Returns:
            background color of the control
        """
        return self.__background_color

    @background_color.setter
    def background_color(self,
                         background_color: str):
        """ Set the background color of the control

        Args:
            background_color: background color of the control
        """
        self.__background_color = background_color

    @property
    def refresh_control(self) -> bool:
        """ Get the refresh control state

        Returns:
            refresh control state
        """
        return self.__refresh_control

    def reset_refresh_control(self):
        """ reset the refresh state of the control """

        self.__refresh_control = False

    def modify_visible_condition(self,
                                 value_name: str,
                                 value     : str):
        """ Modify the visible condition

        Args:
            value_name: Name of the value
            value:      condition value
        """

        self.__visible_condition = ConditionUtil.modify_condition(value_name, self.__visible_condition, value)

        if GeneralConstants.SUB_NAME_SEPARATOR not in value_name:
            self.visible = value != self.FALSE_STR


    def set_visible_condition(self,
                              value_name: str,
                              condition : str):
        """ Set the visible condition of the property

        Args:
            value_name: Name of the value
            condition:  Visible condition
        """

        if self.__visible_condition == self.FALSE_STR:
            return

        vis_condition = condition

        if GeneralConstants.SUB_NAME_SEPARATOR not in value_name:
            self.__visible_condition = ""


        #---------------- add a property condition for geometry elements

        else:
            vis_condition = f"|{value_name}:{condition}"

        self.__visible_condition += vis_condition

        self.__visible = self.__visible_condition != self.FALSE_STR

    @property
    def palette_layout_dict(self) -> dict[str, Any]:
        """ get the palette layout dictionary

        Returns:
            palette layout dictionary
        """

        return self.__palette_layout_dict


    @palette_layout_dict.setter
    def palette_layout_dict(self,
                            palette_layout_dict: dict[str, Any]):
        """ set the palette layout dictionary

        Args:
            palette_layout_dict: palette layout dictionary
        """

        self.__palette_layout_dict = palette_layout_dict


    @property
    def list_index_offset(self) -> int:
        """ Get the list index offset

        Returns:
            list index offset
        """

        return self.__list_index_offset

    @list_index_offset.setter
    def list_index_offset(self,
                          list_index_offset: int):
        """ Set the list index offset

        Args:
            list_index_offset: list index offset
        """

        self.__list_index_offset = list_index_offset


    def deep_copy(self) -> ControlProperties:
        """ deep copy of the data

        Returns:
            copied control properties
        """

        prop = ControlProperties(self.text, self.value_name, self.enable_condition, self.visible_condition,
                                 self.page, self.expander_name, self.row_name,
                                 self.value_str, self.value_list, self.value_list_2,
                                 self.event_id, self.control_type,
                                 self.value_index_name, self.value_list_start_row, self.value_dialog, self.value_list_textids,
                                 self.as_slider, self.__height, self.__width, self.font_style, self.font_face_code,
                                 self.background_color, self.row_state_key, self.expander_state_key)

        prop.group_text            = self.group_text
        prop.visible               = self.visible
        prop.min_value_condition   = self.min_value_condition
        prop.max_value_condition   = self.max_value_condition
        prop.min_value             = self.min_value
        prop.max_value             = self.max_value
        prop.interval_value        = self.interval_value
        prop.constraint            = self.constraint
        prop.visible_function      = self.visible_function
        prop.enable_function       = self.enable_function
        prop.value_text_list       = self.value_text_list
        prop.palette_layout_dict   = self.palette_layout_dict
        prop.list_index_offset     = self.list_index_offset
        prop.value_index_name_base = self.value_index_name_base

        return prop

```

</details>