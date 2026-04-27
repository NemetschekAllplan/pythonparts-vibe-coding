---
title: "BuildingElementControlProperties"
source: "PythonPartsFramework\GeneralScripts\BuildingElementControlProperties.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementControlProperties

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementControlProperties.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the container for the controls properties of the building element

## Abhängigkeiten

- `BuildingElement`
- `ControlProperties`
- `StringEvaluate`
- `__future__`
- `collections.abc`
- `typing`

## Klassen

### `BuildingElementControlProperties`

implementation of the container for the controls properties of the building element
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, control_props: Iterable[ControlProperties]=iter([])` | `None` | initialize  Args:     control_props: controls properties |
| `get_property` | `self, name: str` | `ControlProperties | None` | get the control property for the name  Args:     name: name of the modified property  Returns:     control property |
| `reset_refresh_control` | `self` | `None` | set the refresh control state          |
| `is_refresh_control` | `self` | `bool` | get the refresh control state  Returns:     refresh of the controls state |
| `palette_layout_script` | `self` | `str` | get the palette layout script  Returns:     palette layout script |
| `palette_layout_script` | `self, palette_layout_script: str` | `None` | get the palette layout script  Args:     palette_layout_script: palette layout script |
| `palette_layout_dict` | `self` | `dict[str, Any]` | get the palette layout dictionary  Returns:     palette layout dictionary |
| `eval_palette_layout_script` | `self` | `None` | evaluate the palette layout script          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the container for the controls properties of the building element
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from collections.abc import Iterable

from ControlProperties import ControlProperties
from StringEvaluate import StringEvaluate

if TYPE_CHECKING:
    from BuildingElement import BuildingElement

class BuildingElementControlProperties(list[ControlProperties]):
    """ implementation of the container for the controls properties of the building element
    """

    def __init__(self,
                 control_props: Iterable[ControlProperties] = iter([])):
        """ initialize

        Args:
            control_props: controls properties
        """

        super().__init__(control_props)

        self.__palette_layout_script = ""
        self.__palette_layout_dict : dict[str, Any] = {}


    def get_property(self,
                     name: str) -> (ControlProperties | None):
        """ get the control property for the name

        Args:
            name: name of the modified property

        Returns:
            control property
        """

        return next((ctrl_prop for ctrl_prop in self if ctrl_prop.value_name == name and \
                     ctrl_prop.control_type not in (ControlProperties.ControlType.EXPANDER, ControlProperties.ControlType.ROW)), None)


    def reset_refresh_control(self):
        """ set the refresh control state
        """

        for ctrl_prop in self:
            ctrl_prop.reset_refresh_control()


    def is_refresh_control(self) -> bool:
        """ get the refresh control state

        Returns:
            refresh of the controls state
        """

        return next((True for ctrl_prop in self if ctrl_prop.refresh_control), False)


    @property
    def palette_layout_script(self) -> str:
        """ get the palette layout script

        Returns:
            palette layout script
        """

        return self.__palette_layout_script


    @palette_layout_script.setter
    def palette_layout_script(self,
                              palette_layout_script: str):
        """ get the palette layout script

        Args:
            palette_layout_script: palette layout script
        """

        self.__palette_layout_script = palette_layout_script


    @property
    def palette_layout_dict(self) -> dict[str, Any]:
        """ get the palette layout dictionary

        Returns:
            palette layout dictionary
        """

        return self.__palette_layout_dict


    def eval_palette_layout_script(self):
        """ evaluate the palette layout script
        """

        if not self.__palette_layout_script:
            return

        script_dict = {}

        local_var = StringEvaluate.get_allplan_api_param_dict()

        exec(self.__palette_layout_script, script_dict, local_var)     # pylint: disable=exec-used

        for key, value in local_var.items():
            if not key.startswith("Allplan"):
                self.__palette_layout_dict[key] = value

```

</details>