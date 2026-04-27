---
title: "HandleProperties"
source: "PythonPartsFramework\GeneralScripts\HandleProperties.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandleProperties

> **Pfad:** `PythonPartsFramework\GeneralScripts\HandleProperties.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

Implementation of the handle properties class

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `ControlProperties`
- `HandleDirection`
- `HandleParameterData`
- `HandleParameterType`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `StringEvaluate`
- `ValueTypes.ValueTypeUtils.ControlMinMaxUtil`
- `__future__`
- `typing`

## Klassen

### `HandleProperties`

Implementation of the handle properties class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, handle_id: str | tuple[int, str], handle_point: AllplanGeo.Point3D, ref_point: AllplanGeo.Point3D, handle_param_data: list[HandleParameterData], handle_move_dir: HandleDirection, abs_value: bool=True, distance_factor: float=1.0, plane: AllplanGeo.Plane3D | None=None, dir_vector: AllplanGeo.Vector3D | None=None, info_text: str='', angle_placement: AllplanGeo.AxisPlacement3D | None=None, show_handles: bool=True, center_point: AllplanGeo.Point3D | None=None, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter()` | `None` | Set the properties of a handle  Args:     handle_id:         Unique handle ID, e.g. the name of the handle     handle_point:      Handle point which will be moved     ref_point:         Reference point for the distance calculation     handle_param_data: List with the parameter data. The parameter data are used for recalculation     handle_move_dir:   Allowed move direction for the handle     abs_value:         Use the absolute value from the calculation: True/False     distance_factor:   Factor for property calculation. -1=show negative value in the input control.     plane:             Input plane for the handle_point movement     dir_vector:        Direction vector for the handle point movement     info_text:         Information text of the tooltip     angle_placement:   Placement for the 3D angle input     show_handles:      Show handles state. This offers the possibility to use only the input by the edit fields     center_point:      Center point for arc handles     owner_element:     owner element of the handle (in element modification mode) |
| `__repr__` | `self` | `str` | Create class information as string  Returns:     created data string |
| `handle_id` | `self` | `str | tuple[int, str]` | Get the handle id  Returns:     handle id |
| `handle_point` | `self` | `AllplanGeo.Point3D` | Get the handle point  Returns:     handle point |
| `handle_point` | `self, handle_point: AllplanGeo.Point3D` | `None` | Set the handle point  Args:     handle_point: handle point |
| `ref_point` | `self` | `AllplanGeo.Point3D` | Get the reference point  Returns:     reference point |
| `ref_point` | `self, ref_point: AllplanGeo.Point3D` | `None` | set the reference point  Args:     ref_point: reference point |
| `center_point` | `self` | `AllplanGeo.Point3D | None` | Get the center point  Returns:     center point |
| `center_point` | `self, center_point: AllplanGeo.Point3D` | `None` | Set the center point  Args:     center_point: center point |
| `parameter_data` | `self` | `list[HandleParameterData]` | Get tbe list with the parameter data of the handle  Returns:     parameter data |
| `ele_prop_list` | `self` | `list[tuple[str, HandleParameterType, bool, bool, bool, Any, int | list[int] | None, bool, bool, AllplanGeo.Vector3D | None]]` | Get the parameter data as list of tuples (called from C++)  Returns:     parameter data as list of tuples |
| `handle_move_dir` | `self` | `HandleDirection` | Get the allowed move direction for the handle  Returns:     allowed move direction |
| `abs_value` | `self` | `bool` | Get the absolute value state of the properties  Returns:     absolute value |
| `distance_factor` | `self` | `float` | Get the factor for property calculation:  -1=show negative value in the input control. Multiply the distance between reference and handle point with the factor to get the property value, e.g. 2.0 if the ref_point is a center point.  Returns:     distance factor |
| `distance_factor` | `self, factor: float` | `None` | Set the distance factor for calculation  Args:     factor: distance factor |
| `plane` | `self` | `AllplanGeo.Plane3D | None` | Get the input plane for the handle_point movement  Returns:     inout plane |
| `dir_vector` | `self` | `AllplanGeo.Vector3D | None` | Get the direction vector of the handle point movement  Returns:     direction vector |
| `dir_vector` | `self, dir_vector: AllplanGeo.Vector3D | None` | `None` | Set the direction vector of the handle point movement  Args:     dir_vector: direction vector |
| `angle_placement` | `self` | `AllplanGeo.AxisPlacement3D | None` | Get the placement for the 3D angle input  Returns:     placement for the 3D angle input |
| `angle_placement` | `self, angle_placement: AllplanGeo.AxisPlacement3D` | `None` | Set the placement for the 3D angle input  Args:     angle_placement: placement for the 3D angle input |
| `show_handles` | `self` | `bool` | Get the show handles state  Returns:     show handles state |
| `show_handles` | `self, show_handles: bool` | `None` | Set the show handles state  Args:     show_handles: show handles state |
| `build_ele_index_list` | `self` | `list[int]` | Get the index list of the building elements  Returns:     index list |
| `build_ele_index_list` | `self, index_list: list[int]` | `None` | Set the index list of the building element  Args:     index_list: index list |
| `click_state` | `self` | `bool` | Get the click state:      - False: Handle can be moved     - True:  Handle can be clicked, used like a button  Returns:     click state |
| `handle_type` | `self` | `AllplanIFW.ElementHandleType` | Handle type  Returns:     handle type |
| `handle_type` | `self, handle_type: AllplanIFW.ElementHandleType` | `None` | Set the handle type  Args:     handle_type: handle type |
| `handle_angle` | `self` | `AllplanGeo.Angle` | Handle angle  Returns:     handle angle |
| `handle_angle` | `self, angle: AllplanGeo.Angle` | `None` | Set the handle angle  Args:     angle: handle angle |
| `info_text` | `self` | `str` | Info text of the tooltip  Returns:     into text |
| `info_text` | `self, text: str` | `None` | Set the info text for the tooltip  Args:     text: info text |
| `in_modification` | `self` | `bool` | Get the modification state  Returns:     modification state |
| `in_modification` | `self, in_modification: bool` | `None` | Set the modification state  Args:     in_modification: modification state |
| `owner_element` | `self` | `AllplanEleAdapter.BaseElementAdapter` | Get the owner element  Returns:     owner element |
| `owner_element` | `self, owner_element: AllplanEleAdapter.BaseElementAdapter` | `None` | Set the owner element  Args:     owner_element: owner element |
| `trans_matrix` | `self` | `AllplanGeo.Matrix3D` | Get the transformation matrix  Returns:     transformation matrix |
| `trans_matrix` | `self, trans_matrix: AllplanGeo.Matrix3D` | `None` | Set the transformation matrix  Args:     trans_matrix: transformation matrix |
| `set_min_max_values` | `self, control_props: list[BuildingElementControlProperties], build_ele_list: list[BuildingElement]` | `None` | Set the min/max values of the handle property  Args:     control_props:  control properties     build_ele_list: list with the building elements |
| `__set_min_value_values_for_list_item` | `self, ctrl_prop: ControlProperties, build_ele: BuildingElement, name: str, param_dict: dict[str, Any]` | `None` | set the min/max values for a list item  Args:     ctrl_prop:  control property     build_ele:  building element with the parameter properties     name:       name of the property     param_dict: parameter dictionary |
| `get_min_max_values` | `self, name: str` | `tuple[int | float, int | float, str, str]` | Get the min/max values of the handle property  Args:     name: name of the property  Returns:     tuple(min value, max value, value list, interval value) |
| `transform` | `self, transformation_matrix: AllplanGeo.Matrix3D` | `None` | Transform the handle  Args:     transformation_matrix: transformation matrix |
| `get_parameter_names` | `self` | `list[str]` | get the names of the parameters  Returns:     names of the parameters |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the handle properties class
"""

from __future__ import annotations

from typing import cast, Any, TYPE_CHECKING

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from BuildingElementControlProperties import BuildingElementControlProperties
from ControlProperties import ControlProperties
from HandleDirection import HandleDirection
from HandleParameterData import HandleParameterData
from HandleParameterType import HandleParameterType
from StringEvaluate import StringEvaluate

from ValueTypes.ValueTypeUtils.ControlMinMaxUtil import ControlMinMaxUtil

if TYPE_CHECKING:
    from BuildingElement import BuildingElement

class HandleProperties():
    """ Implementation of the handle properties class
    """

    def __init__(self,                                                                      # pylint: disable=too-many-arguments
                 handle_id        : (str | tuple[int, str]),
                 handle_point     : AllplanGeo.Point3D,
                 ref_point        : AllplanGeo.Point3D,
                 handle_param_data: list[HandleParameterData],
                 handle_move_dir  : HandleDirection,
                 abs_value        : bool                                 = True,
                 distance_factor  : float                                = 1.0,
                 plane            : (AllplanGeo.Plane3D | None)          = None,
                 dir_vector       : (AllplanGeo.Vector3D | None)         = None,
                 info_text        : str                                  = "",
                 angle_placement  : (AllplanGeo.AxisPlacement3D | None)  = None,
                 show_handles     : bool                                 = True,
                 center_point     : (AllplanGeo.Point3D | None)          = None,
                 owner_element    : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()):
        """ Set the properties of a handle

        Args:
            handle_id:         Unique handle ID, e.g. the name of the handle
            handle_point:      Handle point which will be moved
            ref_point:         Reference point for the distance calculation
            handle_param_data: List with the parameter data. The parameter data are used for recalculation
            handle_move_dir:   Allowed move direction for the handle
            abs_value:         Use the absolute value from the calculation: True/False
            distance_factor:   Factor for property calculation. -1=show negative value in the input control.
            plane:             Input plane for the handle_point movement
            dir_vector:        Direction vector for the handle point movement
            info_text:         Information text of the tooltip
            angle_placement:   Placement for the 3D angle input
            show_handles:      Show handles state. This offers the possibility to use only the input by the edit fields
            center_point:      Center point for arc handles
            owner_element:     owner element of the handle (in element modification mode)
        """

        self.__handle_id       = handle_id
        self.__handle_point    = handle_point
        self.__ref_point       = ref_point
        self.__center_point    = center_point
        self.__handle_move_dir = handle_move_dir
        self.__abs_value       = abs_value
        self.__distance_factor = distance_factor
        self.__plane           = plane
        self.__dir_vector      = dir_vector
        self.__info_text       = info_text
        self.__angle_placement = angle_placement
        self.__show_handles    = show_handles
        self.__owner_element   = owner_element

        self.__handle_type     = AllplanIFW.ElementHandleType.HANDLE_CIRCLE
        self.__handle_angle    = AllplanGeo.Angle()
        self.__in_modification = False
        self.__trans_matrix    = AllplanGeo.Matrix3D()

        self.__build_ele_index_list = [0]     # index list with the connected building elements
                                              # (geometry, ...) of a sub element

        self.__min_max_value_list : list[tuple[(int | float), (int | float), str, str]] = []
        self.__handle_param_data  : list[HandleParameterData]                           = []

        if not handle_param_data:
            return


        #----------------- convert from tuple

        if isinstance(handle_param_data[0], tuple):
            self.__handle_param_data = [HandleParameterData(*cast(tuple, data)) for data in handle_param_data]
        else:
            self.__handle_param_data = handle_param_data


        #----------------- set the handle type for the check box handle

        if self.__handle_param_data[0].param_type == HandleParameterType.CHECK_BOX:
            self.handle_type = AllplanIFW.ElementHandleType.HANDLE_SQUARE_BLUE if self.__handle_param_data[0].check_box_state else \
                               AllplanIFW.ElementHandleType.HANDLE_SQUARE_EMPTY


        #----------------- set the handle type for the increment / decrement handle

        if self.__handle_param_data[0].param_type in [HandleParameterType.INCREMENT_BUTTON, HandleParameterType.DECREMENT_BUTTON]:
            self.handle_type = AllplanIFW.ElementHandleType.HANDLE_SQUARE_RIGHT


    def __repr__(self) -> str:
        """ Create class information as string

        Returns:
            created data string
        """

        return f"<{self.__class__.__name__}>\n" \
               f"   handle_id:             {self.__handle_id}\n" \
               f"   handle_point:          {self.__handle_point}\n" \
               f"   ref_point:             {self.__ref_point}\n" \
               f"   center_point:          {self.__center_point}\n" \
               f"   handle_param_data:     {self.__handle_param_data}\n" \
               f"   handle_move_dir:       HandleDirection.{self.__handle_move_dir.name}\n" \
               f"   abs_value:             {self.__abs_value}\n" \
               f"   distance_factor:       {self.__distance_factor}\n" \
               f"   build_ele_index_list:  {self.__build_ele_index_list}\n" \
               f"   click_state:           {self.click_state}\n" \
               f"   min_max_value_list:    {self.__min_max_value_list}\n" \
               f"   plane:                 {self.__plane}\n" \
               f"   handle_type:           {str(self.__handle_type).replace(chr(10), '')}\n" \
               f"   handle_angle:          {self.__handle_angle}\n" \
               f"   info_text:             {self.__info_text}\n" \
               f"   dir_vector:            {self.__dir_vector}\n" \
               f"   angle_placement:       {self.__angle_placement}\n" \
               f"   show_handles:          {self.__show_handles}\n" \
               f"   trans_matrix:          {self.__trans_matrix}\n"


    @property
    def handle_id(self) -> (str | tuple[int, str]):
        """ Get the handle id

        Returns:
            handle id
        """

        return self.__handle_id


    @property
    def handle_point(self) -> AllplanGeo.Point3D:
        """ Get the handle point

        Returns:
            handle point
        """

        return self.__handle_point


    @handle_point.setter
    def handle_point(self,
                     handle_point: AllplanGeo.Point3D):
        """ Set the handle point

        Args:
            handle_point: handle point
        """

        self.__handle_point = handle_point


    @property
    def ref_point(self) -> AllplanGeo.Point3D:
        """ Get the reference point

        Returns:
            reference point
        """

        return self.__ref_point


    @ref_point.setter
    def ref_point(self,
                  ref_point: AllplanGeo.Point3D):
        """ set the reference point

        Args:
            ref_point: reference point
        """

        self.__ref_point = ref_point


    @property
    def center_point(self) -> (AllplanGeo.Point3D | None):
        """ Get the center point

        Returns:
            center point
        """

        return self.__center_point


    @center_point.setter
    def center_point(self,
                     center_point: AllplanGeo.Point3D):
        """ Set the center point

        Args:
            center_point: center point
        """

        self.__center_point = center_point


    @property
    def parameter_data(self) -> list[HandleParameterData]:
        """ Get tbe list with the parameter data of the handle

        Returns:
            parameter data
        """

        return self.__handle_param_data


    @property
    def ele_prop_list(self) -> list[tuple[str, HandleParameterType, bool, bool, bool, Any, ((int | list[int]) | None), bool, bool, \
                                    (AllplanGeo.Vector3D | None)]]:
        """ Get the parameter data as list of tuples (called from C++)

        Returns:
            parameter data as list of tuples
        """

        return [(param_data.param_prop_name, param_data.param_type, param_data.has_input_field,
                 param_data.show_negative_value, param_data.check_box_state, param_data.in_decrement_value,
                 param_data.list_index, param_data.show_input_field_always,
                 param_data.input_field_above, param_data.dir_vector) for param_data in self.__handle_param_data]

    @property
    def handle_move_dir(self) -> HandleDirection:
        """ Get the allowed move direction for the handle

        Returns:
            allowed move direction
        """

        return self.__handle_move_dir


    @property
    def abs_value(self) -> bool:
        """ Get the absolute value state of the properties

        Returns:
            absolute value
        """

        return self.__abs_value


    @property
    def distance_factor(self) -> float:
        """ Get the factor for property calculation:

        -1=show negative value in the input control.
        Multiply the distance between reference and handle point with the factor to
        get the property value, e.g. 2.0 if the ref_point is a center point.

        Returns:
            distance factor
        """

        return self.__distance_factor

    @distance_factor.setter
    def distance_factor(self,
                        factor: float):
        """ Set the distance factor for calculation

        Args:
            factor: distance factor
        """

        self.__distance_factor = factor


    @property
    def plane(self) -> (AllplanGeo.Plane3D | None):
        """ Get the input plane for the handle_point movement

        Returns:
            inout plane
        """

        return self.__plane


    @property
    def dir_vector(self) -> (AllplanGeo.Vector3D | None):
        """ Get the direction vector of the handle point movement

        Returns:
            direction vector
        """

        return self.__dir_vector


    @dir_vector.setter
    def dir_vector(self,
                   dir_vector: (AllplanGeo.Vector3D | None)):
        """ Set the direction vector of the handle point movement

        Args:
            dir_vector: direction vector
        """

        self.__dir_vector = dir_vector


    @property
    def angle_placement(self) -> (AllplanGeo.AxisPlacement3D | None):
        """ Get the placement for the 3D angle input

        Returns:
            placement for the 3D angle input
        """

        return self.__angle_placement


    @angle_placement.setter
    def angle_placement(self,
                        angle_placement: AllplanGeo.AxisPlacement3D):
        """ Set the placement for the 3D angle input

        Args:
            angle_placement: placement for the 3D angle input
        """

        self.__angle_placement = angle_placement


    @property
    def show_handles(self) -> bool:
        """ Get the show handles state

        Returns:
            show handles state
        """

        return self.__show_handles


    @show_handles.setter
    def show_handles(self,
                     show_handles: bool):
        """ Set the show handles state

        Args:
            show_handles: show handles state
        """

        self.__show_handles = show_handles


    @property
    def build_ele_index_list(self) -> list[int]:
        """ Get the index list of the building elements

        Returns:
            index list
        """

        return self.__build_ele_index_list


    @build_ele_index_list.setter
    def build_ele_index_list(self,
                             index_list: list[int]):
        """ Set the index list of the building element

        Args:
            index_list: index list
        """
        self.__build_ele_index_list = index_list


    @property
    def click_state(self) -> bool:
        """ Get the click state:

            - False: Handle can be moved
            - True:  Handle can be clicked, used like a button

        Returns:
            click state
        """

        return self.handle_move_dir == HandleDirection.CLICK


    @property
    def handle_type(self) -> AllplanIFW.ElementHandleType:
        """ Handle type

        Returns:
            handle type
        """
        return self.__handle_type


    @handle_type.setter
    def handle_type(self,
                    handle_type: AllplanIFW.ElementHandleType):
        """ Set the handle type

        Args:
            handle_type: handle type
        """
        self.__handle_type = handle_type


    @property
    def handle_angle(self) -> AllplanGeo.Angle:
        """ Handle angle

        Returns:
            handle angle
        """
        return self.__handle_angle


    @handle_angle.setter
    def handle_angle(self,
                     angle: AllplanGeo.Angle):
        """ Set the handle angle

        Args:
            angle: handle angle
        """
        self.__handle_angle = angle


    @property
    def info_text(self) -> str:
        """ Info text of the tooltip

        Returns:
            into text
        """
        return self.__info_text


    @info_text.setter
    def info_text(self,
                  text: str):
        """ Set the info text for the tooltip

        Args:
            text: info text
        """
        self.__info_text = text

    @property
    def in_modification(self) -> bool:
        """ Get the modification state

        Returns:
            modification state
        """
        return self.__in_modification

    @in_modification.setter
    def in_modification(self,
                        in_modification: bool):
        """ Set the modification state

        Args:
            in_modification: modification state
        """
        self.__in_modification = in_modification

    @property
    def owner_element(self) -> AllplanEleAdapter.BaseElementAdapter:
        """ Get the owner element

        Returns:
            owner element
        """
        return self.__owner_element

    @owner_element.setter
    def owner_element(self,
                      owner_element: AllplanEleAdapter.BaseElementAdapter):
        """ Set the owner element

        Args:
            owner_element: owner element
        """
        self.__owner_element = owner_element

    @property
    def trans_matrix(self) -> AllplanGeo.Matrix3D:
        """ Get the transformation matrix

        Returns:
            transformation matrix
        """

        return self.__trans_matrix

    @trans_matrix.setter
    def trans_matrix(self,
                     trans_matrix: AllplanGeo.Matrix3D):
        """ Set the transformation matrix

        Args:
            trans_matrix: transformation matrix
        """

        self.__trans_matrix = trans_matrix

    def set_min_max_values(self,
                           control_props : list[BuildingElementControlProperties],
                           build_ele_list: list[BuildingElement]):
        """ Set the min/max values of the handle property

        Args:
            control_props:  control properties
            build_ele_list: list with the building elements
        """

        self.__min_max_value_list = []

        for build_ele_index in self.build_ele_index_list:
            build_ele = build_ele_list[build_ele_index]

            param_dict = StringEvaluate.get_string_eval_param_dict(build_ele, build_ele.get_string_tables()[0]) | \
                         StringEvaluate.get_allplan_geometry_dict()

            for param_data in self.__handle_param_data:
                name = param_data.param_prop_name

                if (ctrl_prop := next((item for item in control_props[build_ele_index] if item.value_name == name), None)) is None:
                    continue

                if param_data.list_index is None or build_ele_list is None:
                    if (prop := build_ele.get_property(name)) is None:
                        continue

                    ControlMinMaxUtil.set_min_max_values(ctrl_prop, prop.value_type, cast(int, prop.attribute_id), param_dict)

                    self.__min_max_value_list.append((ctrl_prop.min_value, ctrl_prop.max_value,
                                                      ctrl_prop.value_list, ctrl_prop.interval_value))
                else:
                    self.__set_min_value_values_for_list_item(ctrl_prop, build_ele, name, param_dict)


    def __set_min_value_values_for_list_item(self,
                                             ctrl_prop : ControlProperties,
                                             build_ele : BuildingElement,
                                             name      : str,
                                             param_dict: dict[str, Any]):
        """ set the min/max values for a list item

        Args:
            ctrl_prop:  control property
            build_ele:  building element with the parameter properties
            name:       name of the property
            param_dict: parameter dictionary
        """

        list_ctrl_props = ctrl_prop.deep_copy()

        if (item_prop := build_ele.get_property(name)) is None:
            return

        ControlMinMaxUtil.set_min_max_values(list_ctrl_props, item_prop.value_type, cast(int, item_prop.attribute_id), param_dict)

        self.__min_max_value_list.append((list_ctrl_props.min_value, list_ctrl_props.max_value,
                                          list_ctrl_props.value_list, list_ctrl_props.interval_value))


    def get_min_max_values(self,
                           name: str) -> tuple[(int | float), (int | float), str, str]:
        """ Get the min/max values of the handle property

        Args:
            name: name of the property

        Returns:
            tuple(min value, max value, value list, interval value)
        """

        index = 0

        for param_data in self.__handle_param_data:
            if name == param_data.param_prop_name  and  index < len(self.__min_max_value_list):
                return self.__min_max_value_list[index]

            index +=1

        return (-1.7976931348623157e+300, 1.7976931348623157e+300, "", "")


    def transform(self,
                  transformation_matrix: AllplanGeo.Matrix3D):
        """ Transform the handle

        Args:
            transformation_matrix: transformation matrix
        """

        self.__handle_point = AllplanGeo.Transform(self.__handle_point, transformation_matrix)
        self.__ref_point    = AllplanGeo.Transform(self.__ref_point, transformation_matrix)


    def get_parameter_names(self) -> list[str]:
        """ get the names of the parameters

        Returns:
            names of the parameters
        """

        return [param_data.param_prop_name for param_data in self.parameter_data]

```

</details>