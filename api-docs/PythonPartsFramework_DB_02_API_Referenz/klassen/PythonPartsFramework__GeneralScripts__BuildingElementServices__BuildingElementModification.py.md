---
title: "BuildingElementModification"
source: "PythonPartsFramework\GeneralScripts\BuildingElementServices\BuildingElementModification.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementModification

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementServices\BuildingElementModification.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the building element modification

## Abhängigkeiten

- `BaseScriptObject`
- `BuildingElement`
- `BuildingElementComposite`
- `BuildingElementControlProperties`
- `BuildingElementControlService`
- `BuildingElementInputServices.ScriptService`
- `BuildingElementParameterPropertyUtil`
- `BuildingElementServices.BuildingElementIndexUtil`
- `BuildingElementValueUtil`
- `ControlPropertiesMinMaxUtil`
- `ControlPropertiesValueListUtil`
- `Palette.PaletteBuildingElementUtil`
- `Palette.WpfPaletteBuilder`
- `ScriptObjectInteractors.BaseScriptObjectInteractor`
- `StringEvaluate`
- `typing`

## Klassen

### `BuildingElementModification`

Definition of class BuildingElementModification
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele_list: list[BuildingElement], build_ele_composite: BuildingElementComposite, build_ele_script: Any, build_ele_ctrl_props_list: list[BuildingElementControlProperties]` | `None` | Initialize the data  Args:     build_ele_list:            list with the building elements     build_ele_composite:       building element composite with the building element constraints     build_ele_script:          Building element script     build_ele_ctrl_props_list: list with the building element control properties |
| `modify_element_property` | `self, page: int, name: str, value: Any, page_build_ele: list[list[int]], palette_builder: WpfPaletteBuilder | None, script_object: BaseScriptObject | BaseScriptObjectInteractor | None=None` | `bool` | Modify property of element  Args:     page:                     page index of the modified property     name:                     the name of the property.     value:                    new value for property.     page_build_ele:           page building element list     palette_builder:          property palette builder     script_object:            script object  Returns:     palette refresh state |
| `__execute_global_value_modification` | `self, name: str, value: Any` | `bool` | execute the global value modification  Args:     name:  the name of the property.     value: new value for property.  Returns:     returns |
| `__get_build_ele_visible_state` | `self` | `list[bool]` | get the visible state of the building elements  Returns:     visible state |
| `__is_visibility_change` | `self, name: str, build_ele_visible: list[bool], build_ele: BuildingElement, build_ele_ctrl_props: BuildingElementControlProperties, param_dict: dict[str, Any]` | `bool` | check for a visibility change  Args:     name:                 the name of the property.     build_ele_visible:    visible state of the building elements     build_ele:            building element with the parameter properties     build_ele_ctrl_props: building element control properties     param_dict:           parameter dictionary  Returns:     palette refresh state |
| `__check_multi_page_control` | `self, name: str` | `bool` | check for a multi page control  Args:     name: the name of the property.  Returns:     palette refresh state |
| `__modify_element_property` | `script_object: BaseScriptObject | BaseScriptObjectInteractor, name: str, value: Any` | `bool` | modify the element property  Args:     script_object: script object     name:          name     value:         value  Returns:     update palette state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the building element modification
"""

from typing import Any

from BaseScriptObject import BaseScriptObject
from BuildingElement import BuildingElement
from BuildingElementComposite import BuildingElementComposite
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementControlService import BuildingElementControlService
from ControlPropertiesMinMaxUtil import ControlPropertiesMinMaxUtil
from ControlPropertiesValueListUtil import ControlPropertiesValueListUtil
from StringEvaluate import StringEvaluate

import BuildingElementParameterPropertyUtil

import BuildingElementValueUtil

from BuildingElementInputServices.ScriptService import ScriptService
from BuildingElementServices.BuildingElementIndexUtil import BuildingElementIndexUtil

from Palette.PaletteBuildingElementUtil import PaletteBuildingElementUtil
from Palette.WpfPaletteBuilder import WpfPaletteBuilder

from ScriptObjectInteractors.BaseScriptObjectInteractor import BaseScriptObjectInteractor

class BuildingElementModification:
    """ Definition of class BuildingElementModification
    """

    def __init__(self,
                 build_ele_list           : list[BuildingElement],
                 build_ele_composite      : BuildingElementComposite,
                 build_ele_script         : Any,
                 build_ele_ctrl_props_list: list[BuildingElementControlProperties]):
        """ Initialize the data

        Args:
            build_ele_list:            list with the building elements
            build_ele_composite:       building element composite with the building element constraints
            build_ele_script:          Building element script
            build_ele_ctrl_props_list: list with the building element control properties
        """

        self.build_ele_list            = build_ele_list
        self.build_ele_composite       = build_ele_composite
        self.build_ele_script          = build_ele_script
        self.build_ele_ctrl_props_list = build_ele_ctrl_props_list


    def modify_element_property(self,
                                page                    : int,
                                name                    : str,
                                value                   : Any,
                                page_build_ele          : list[list[int]],
                                palette_builder         : (WpfPaletteBuilder | None),
                                script_object           : (BaseScriptObject | BaseScriptObjectInteractor | None) = None) -> bool:
        """ Modify property of element

        Args:
            page:                     page index of the modified property
            name:                     the name of the property.
            value:                    new value for property.
            page_build_ele:           page building element list
            palette_builder:          property palette builder
            script_object:            script object

        Returns:
            palette refresh state
        """

        if self.__execute_global_value_modification(name, value):
            return True


        #----------------- get the page number (input from a DOM control)

        name = name.replace("___DOM", "")

        if page >= 100:     # pylint: disable=magic-value-comparison
            page = PaletteBuildingElementUtil.get_page_from_building_element_index(page, page_build_ele,
                                                                                   self.build_ele_ctrl_props_list, name)


        #----------------- get the old visible state

        build_ele_visible = self.__get_build_ele_visible_state()


        #----------------- Get the building element for the name and page

        parent_name = BuildingElementParameterPropertyUtil.get_property_value_name(name)

        build_ele_index = PaletteBuildingElementUtil.get_build_ele_index(page_build_ele,
                                                                         self.build_ele_list,
                                                                         page, parent_name)

        build_ele            = self.build_ele_list[build_ele_index]
        build_ele_ctrl_props = self.build_ele_ctrl_props_list[build_ele_index]

        build_ele_ctrl_props.reset_refresh_control()


        #----------------- Check and set the new value

        refresh_palette, prop = BuildingElementValueUtil.update_value(name, value, build_ele, build_ele_ctrl_props)

        refresh_palette |= BuildingElementIndexUtil.modify_building_element_index(name, value, build_ele,
                                                                                  self.build_ele_list, self.build_ele_composite)

        if script_object is not None:
            refresh_palette |= self.__modify_element_property(script_object, name, value)

        elif self.build_ele_script:
            refresh_palette |= ScriptService.modify_element_property(name, value, prop, build_ele_index, self.build_ele_script,
                                                                     self.build_ele_list, self.build_ele_ctrl_props_list,
                                                                     self.build_ele_composite)

        if len(self.build_ele_list) > 1 and \
           self.build_ele_composite.connect_building_element_values(self.build_ele_list):
            refresh_palette = True


        #----------------- check the corresponding min and max values

        param_dict = StringEvaluate.get_string_eval_param_dict(build_ele, self.build_ele_list[0].get_string_tables()[0])

        refresh_palette |= ControlPropertiesMinMaxUtil.check_min_max_value(build_ele, build_ele_ctrl_props, param_dict,
                                                                           self.build_ele_list[0].get_string_tables()[1])

        refresh_palette |= ControlPropertiesValueListUtil.validate_values(build_ele, build_ele_ctrl_props, param_dict)

        if refresh_palette:
            return True


        #----------------- Check for palette update

        if self.__is_visibility_change(name, build_ele_visible, build_ele, build_ele_ctrl_props, param_dict):
            return True

        if prop and prop.value_type == "reinfconcretecover"  and palette_builder is not None and \
           palette_builder.IsConcreteCoverPaletteUpdate(value):           # pylint: disable=magic-value-comparison
            return True

        return self.__check_multi_page_control(name)


    def __execute_global_value_modification(self,
                                            name : str,
                                            value: Any) -> bool:
        """ execute the global value modification

        Args:
            name:  the name of the property.
            value: new value for property.

        Returns:
            returns
        """

        #----------------- set the global properties

        if name == "__GlobalConcreteCover__":                       # pylint: disable=magic-value-comparison
            for build_ele in self.build_ele_list:
                build_ele.modify_value_type("ReinfConcreteCover", value)

            return True

        if name == "__GlobalReinforcementDiameter__":               # pylint: disable=magic-value-comparison
            for build_ele in self.build_ele_list:
                build_ele.modify_value_type("ReinfBarDiameter", value)

            return True

        return False


    def __get_build_ele_visible_state(self) -> list[bool]:
        """ get the visible state of the building elements

        Returns:
            visible state
        """

        return [self.build_ele_composite.is_element_visible(i - 1, self.build_ele_list) for i in range(1, len(self.build_ele_list))]


    def __is_visibility_change(self,
                               name                : str,
                               build_ele_visible   : list[bool],
                               build_ele           : BuildingElement,
                               build_ele_ctrl_props: BuildingElementControlProperties,
                               param_dict          : dict[str, Any]) -> bool:
        """ check for a visibility change

        Args:
            name:                 the name of the property.
            build_ele_visible:    visible state of the building elements
            build_ele:            building element with the parameter properties
            build_ele_ctrl_props: building element control properties
            param_dict:           parameter dictionary

        Returns:
            palette refresh state
        """

        if BuildingElementControlService.check_visible_state(self.build_ele_list[0], build_ele_ctrl_props, param_dict, name, False):
            return True

        if BuildingElementControlService.check_enable_state(self.build_ele_list[0], build_ele_ctrl_props, param_dict, name, False):
            return True

        if any(name in page_data.visible_condition or name in page_data.enable_condition for page_data in build_ele.get_pages()):
            return True

        return any(build_ele_visible[i] != self.build_ele_composite.is_element_visible(i, self.build_ele_list) \
               for i in range(len(self.build_ele_list) - 1))


    def __check_multi_page_control(self,
                                   name: str) -> bool:
        """ check for a multi page control

        Args:
            name: the name of the property.

        Returns:
            palette refresh state
        """

        multi_page = False

        for build_ele_ctrl_props in self.build_ele_ctrl_props_list:
            if build_ele_ctrl_props.get_property(name) is not None:
                if multi_page:
                    return True

                multi_page = True

        return False


    @staticmethod
    def __modify_element_property(script_object: (BaseScriptObject | BaseScriptObjectInteractor),
                                  name         : str,
                                  value        : Any) -> bool:
        """ modify the element property

        Args:
            script_object: script object
            name:          name
            value:         value

        Returns:
            update palette state
        """

        if (modify_prop := getattr(script_object, "modify_element_property", None)) is None:
            return False

        return False if (result := modify_prop(name.split("___", 1)[0], value)) is None else result

```

</details>