---
title: "BuildingElementValueConstraint"
source: "PythonPartsFramework\GeneralScripts\BuildingElementValueConstraint.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementValueConstraint

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementValueConstraint.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `werte`

## Übersicht

Implementation of the building element value constraint

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementControlProperties`
- `ControlProperties`
- `NemAll_Python_Reinforcement`
- `ParameterProperty`
- `ValueTypes.ParameterPropertyValueTypes`
- `ValueTypes.ParameterPropertyValueTypesImpl`
- `re`
- `typing`

## Klassen

### `BuildingElementValueConstraint`

Implementation of the functions for the building element value constraint
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `_update_data` | `data_dict: dict[str, Any], build_ele: BuildingElement, ctrl_props: ControlProperties` | `None` | Update the data  Args:     data_dict:  dict with the parameter data     build_ele:  building element with the parameter properties     ctrl_props: control properties |
| `_update_reinfbarhooklength` | `build_ele: BuildingElement, hook_length_prop: ParameterProperty, ctrl_props: ControlProperties` | `None` | Update the bar hook length  Args:     build_ele:        building element with the parameter properties     hook_length_prop: hook length property     ctrl_props:       control properties |
| `_update_reinfmeshhooklength` | `build_ele: BuildingElement, hook_length_prop: ParameterProperty, ctrl_props: ControlProperties` | `None` | Update the mesh hook length  Args:     build_ele:        building element with the parameter properties     hook_length_prop: hook length property     ctrl_props:       control properties |
| `_update_reinfhooklength` | `build_ele: BuildingElement, hook_length_prop: ParameterProperty, ctrl_props: ControlProperties` | `None` | Update the hook length  Args:     build_ele:        building element with the parameter properties     hook_length_prop: hook length property     ctrl_props:       control properties |
| `check_property_constraint` | `modified_name: str, build_ele: BuildingElement, ctrl_prop_list: BuildingElementControlProperties` | `bool` | Check for a property constraint  Args:     modified_name:  name of the modified property     build_ele:      building element with the parameter properties     ctrl_prop_list: control properties  Returns:     update state |
| `check_property_constraint_init` | `build_ele: BuildingElement, ctrl_prop_list: BuildingElementControlProperties` | `None` | Check for a property constraint initialization  Args:     build_ele:      building element with the parameter properties     ctrl_prop_list: control properties |
| `update_enable_by_constraint` | `build_ele: BuildingElement, ctrl_prop_list: BuildingElementControlProperties` | `None` | Check for a property constraint initialization  Args:     build_ele:      building element with the parameter properties     ctrl_prop_list: control properties |
| `__process_property_constraint_updates` | `modified_name: str, build_ele: BuildingElement, ctrl_prop_list: BuildingElementControlProperties, modified_names: list[str]` | `bool` | process the property update by constraint  Args:     modified_name:  name of the modified property     build_ele:      building element with the parameter properties     ctrl_prop_list: control properties     modified_names: modified names  Returns:     update state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the building element value constraint
"""

from typing import Any

import re

import NemAll_Python_Reinforcement as AllplanReinf

from BuildingElement import BuildingElement
from BuildingElementControlProperties import BuildingElementControlProperties
from ControlProperties import ControlProperties
from ParameterProperty import ParameterProperty

from ValueTypes.ParameterPropertyValueTypes import ParameterPropertyValueTypes
from ValueTypes.ParameterPropertyValueTypesImpl import ParameterPropertyValueTypesImpl

class BuildingElementValueConstraint():
    """ Implementation of the functions for the building element value constraint
    """

    name_mapping = "__"

    @staticmethod
    def _update_data(data_dict : dict[str, Any],
                     build_ele : BuildingElement,
                     ctrl_props: ControlProperties):
        """ Update the data

        Args:
            data_dict:  dict with the parameter data
            build_ele:  building element with the parameter properties
            ctrl_props: control properties
        """

        for constraint_name in ctrl_props.constraint:
            if BuildingElementValueConstraint.name_mapping not in constraint_name:
                if (prop := build_ele.get_property(constraint_name)):
                    if (value_type := prop.value_type) == ParameterPropertyValueTypes.ANGLE_COMBO_BOX:
                        value_type = ParameterPropertyValueTypesImpl.get_value_type_impl(ParameterPropertyValueTypes.ANGLE)

                    data_dict[value_type] = prop.value

            else:
                key_value = constraint_name.replace("_", "").replace(" ", "").split("=")

                prop = build_ele.get_property(key_value[1])

                data_dict[key_value[0].lower()] = prop.value if prop else eval(key_value[1])        # pylint: disable=eval-used


    @staticmethod
    def _update_reinfbarhooklength(build_ele       : BuildingElement,
                                   hook_length_prop: ParameterProperty,
                                   ctrl_props      : ControlProperties):
        """ Update the bar hook length

        Args:
            build_ele:        building element with the parameter properties
            hook_length_prop: hook length property
            ctrl_props:       control properties
        """

        data_dict = {"reinfbardiameter"   : 0,
                     "reinfsteelgrade"    : AllplanReinf.ReinforcementSettings.GetSteelGrade(),
                     "reinfconcretegrade" : AllplanReinf.ReinforcementSettings.GetConcreteGrade(),
                     "angle"              : 90,
                     "reinfhooktype"      : AllplanReinf.HookType.eAnchorage}

        BuildingElementValueConstraint._update_data(data_dict, build_ele, ctrl_props)

        length_service = AllplanReinf.HookLengthService(AllplanReinf.ReinforcementSettings.GetNorm(),
                                                        data_dict["reinfconcretegrade"], data_dict["reinfsteelgrade"], True)

        hook_length_prop.value = length_service.GetHookLength(data_dict["angle"],
                                                              AllplanReinf.HookType(data_dict["reinfhooktype"]),
                                                              data_dict["reinfbardiameter"])

    @staticmethod
    def _update_reinfmeshhooklength(build_ele       : BuildingElement,
                                    hook_length_prop: ParameterProperty,
                                    ctrl_props      : ControlProperties):
        """ Update the mesh hook length

        Args:
            build_ele:        building element with the parameter properties
            hook_length_prop: hook length property
            ctrl_props:       control properties
        """

        data_dict = {"reinfmeshtype"             : "",
                     "reinfsteelgrade"           : AllplanReinf.ReinforcementSettings.GetSteelGrade(),
                     "reinfconcretegrade"        : AllplanReinf.ReinforcementSettings.GetConcreteGrade(),
                     "angle"                     : 90,
                     "reinfhooktype"             : AllplanReinf.HookType.eAnchorage,
                     "reinfmeshbendingdirection" : AllplanReinf.MeshBendingDirection.LongitudinalBars}

        BuildingElementValueConstraint._update_data(data_dict, build_ele, ctrl_props)

        mesh_data = AllplanReinf.ReinforcementShapeBuilder.GetMeshData(data_dict["reinfmeshtype"])

        diameter = mesh_data.DiameterLongitudinal \
                   if data_dict["reinfmeshbendingdirection"] == AllplanReinf.MeshBendingDirection.LongitudinalBars else \
                   mesh_data.DiameterCross

        length_service = AllplanReinf.HookLengthService(AllplanReinf.ReinforcementSettings.GetNorm(),
                                                        data_dict["reinfconcretegrade"], data_dict["reinfsteelgrade"], True)

        hook_length_prop.value = length_service.GetHookLength(data_dict["angle"],
                                                              AllplanReinf.HookType(data_dict["reinfhooktype"]), diameter)


    @staticmethod
    def _update_reinfhooklength(build_ele       : BuildingElement,
                                hook_length_prop: ParameterProperty,
                                ctrl_props      : ControlProperties):
        """ Update the hook length

        Args:
            build_ele:        building element with the parameter properties
            hook_length_prop: hook length property
            ctrl_props:       control properties
        """

        for constraint_name in ctrl_props.constraint:
            if BuildingElementValueConstraint.name_mapping not in constraint_name:
                if (prop := build_ele.get_property(constraint_name)):
                    if prop.value_type == ParameterPropertyValueTypes.REINF_BAR_DIAMETER:
                        BuildingElementValueConstraint._update_reinfbarhooklength(build_ele, hook_length_prop, ctrl_props)

                    elif prop.value_type == ParameterPropertyValueTypes.REINF_MESH_TYPE:
                        BuildingElementValueConstraint._update_reinfmeshhooklength(build_ele, hook_length_prop, ctrl_props)

    @staticmethod
    def check_property_constraint(modified_name : str,
                                  build_ele     : BuildingElement,
                                  ctrl_prop_list: BuildingElementControlProperties) -> bool:
        """ Check for a property constraint

        Args:
            modified_name:  name of the modified property
            build_ele:      building element with the parameter properties
            ctrl_prop_list: control properties

        Returns:
            update state
        """

        is_update = False

        updated_names  = set[str]()
        modified_names = list[str]([modified_name.split("[", 1)[0].split(".", 1)[0]])


        #----------------- loop over the modified names

        while modified_names:
            if (modified_name := modified_names[0]) in updated_names:
                del modified_names[0]
                continue

            is_update |= BuildingElementValueConstraint.__process_property_constraint_updates(modified_name, build_ele,
                                                                                              ctrl_prop_list, modified_names)

            updated_names.add(modified_name)

            del modified_names[0]

        return is_update


    @staticmethod
    def check_property_constraint_init(build_ele     : BuildingElement,
                                       ctrl_prop_list: BuildingElementControlProperties):
        """ Check for a property constraint initialization

        Args:
            build_ele:      building element with the parameter properties
            ctrl_prop_list: control properties
        """

        for ctrl_prop in ctrl_prop_list:
            if not ctrl_prop.constraint:
                continue

            prop = build_ele.get_property(ctrl_prop.value_name)

            if prop and (prop.value == -1 or prop.value_type.is_default_init_by_constraint(build_ele, ctrl_prop)):
                if (update_fct := getattr(prop.value_type, "update_by_constraint", None)) is not None:
                    update_fct(build_ele, prop, ctrl_prop, "")
                else:
                    BuildingElementValueConstraint.check_property_constraint(ctrl_prop.constraint[0], build_ele, ctrl_prop_list)


    @staticmethod
    def update_enable_by_constraint(build_ele     : BuildingElement,
                                    ctrl_prop_list: BuildingElementControlProperties):
        """ Check for a property constraint initialization

        Args:
            build_ele:      building element with the parameter properties
            ctrl_prop_list: control properties
        """

        for ctrl_prop in ctrl_prop_list:
            if not ctrl_prop.constraint:
                continue

            if (prop := build_ele.get_property(ctrl_prop.value_name)) is not None:
                prop.value_type.update_enable_by_constraint(build_ele, prop, ctrl_prop)


    @staticmethod
    def __process_property_constraint_updates(modified_name : str,                              # NOSONAR
                                              build_ele     : BuildingElement,
                                              ctrl_prop_list: BuildingElementControlProperties,
                                              modified_names: list[str]) -> bool:
        """ process the property update by constraint

        Args:
            modified_name:  name of the modified property
            build_ele:      building element with the parameter properties
            ctrl_prop_list: control properties
            modified_names: modified names

        Returns:
            update state
        """

        is_update = False

        for ctrl_prop in ctrl_prop_list:
            if not ctrl_prop.constraint:
                continue

            if not (prop := build_ele.get_property(ctrl_prop.value_name)):
                continue


            #------------- search for the modified name in the constraint

            for constraint in [item for constaint_item in ctrl_prop.constraint for item in constaint_item.split("\n")]:
                constraint_value = re.split("(?<!=)==(?!=)", constraint)[-1].strip("_")     # internal names are start and end with "__"

                if not re.search(fr"\b{modified_name}\b",  constraint_value):
                    continue


                #--------- get the property for the constraint

                if (update_fct := getattr(prop.value_type, "update_by_constraint", None)) is not None:
                    update_fct(build_ele, prop, ctrl_prop, modified_name)

                    is_update = True

                    if ctrl_prop.value_name not in modified_names:
                        modified_names.append(ctrl_prop.value_name)

                    break

                if (update_fct := getattr(BuildingElementValueConstraint, f"_update_{prop.value_type}",  None)) is not None:
                    update_fct(build_ele, prop, ctrl_prop)  # pylint: disable=not-callable

                    is_update = True

                    if ctrl_prop.value_name not in modified_names:
                        modified_names.append(ctrl_prop.value_name)

                    break

        return is_update

```

</details>