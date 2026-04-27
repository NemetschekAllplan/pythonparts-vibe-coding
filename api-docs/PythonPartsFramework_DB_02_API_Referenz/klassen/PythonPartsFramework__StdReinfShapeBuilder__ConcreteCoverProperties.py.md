---
title: "ConcreteCoverProperties"
source: "PythonPartsFramework\StdReinfShapeBuilder\ConcreteCoverProperties.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# ConcreteCoverProperties

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\ConcreteCoverProperties.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`

## Übersicht

Implementation of the concrete cover properties class

## Abhängigkeiten

- `ReinforcementDefinition`
- `__future__`

## Klassen

### `ConcreteCoverProperties`

Implementation of the concrete cover properties class

The class includes concrete cover properties for the
left, right, top and bottom border

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, left: float=0, right: float=0, top: float=0, bottom: float=0` | `None` | Set the properties of the concrete cover  Args:     left:   Concrete cover at the left border     right:  Concrete cover at the right border     top:    Concrete cover at the top border     bottom: Concrete cover at the bottom border |
| `__repr__` | `self` | `None` | convert to string          |
| `all` | `concrete_cover: float` | `ConcreteCoverProperties` | Set the properties of the concrete cover for all borders  Args:     concrete_cover: concrete cover for all sides  Returns:     concrete cover properties |
| `left_right_bottom` | `left: float, right: float, bottom: float` | `ConcreteCoverProperties` | Set the properties of the concrete cover  Args:     left:   description     right:  description     bottom: description  Returns:     concrete cover properties |
| `left_right` | `left: float, right: float` | `ConcreteCoverProperties` | Set the properties of the concrete cover  Args:     left:  description     right: description  Returns:     concrete cover properties |
| `top_bottom` | `top: float, bottom: float` | `ConcreteCoverProperties` | Set the properties of the concrete cover  Args:     top:    description     bottom: description  Returns:     concrete cover properties |
| `left` | `self` | `float` | Get the cover at the left border  Returns:     concrete cover at the left |
| `left` | `self, concrete_cover: float` | `None` | Set the cover at the left border  Args:     concrete_cover: description |
| `right` | `self` | `float` | Get the cover at the right border  Returns:     concrete cover at the right |
| `right` | `self, concrete_cover: float` | `None` | Set the cover at the right border  Args:     concrete_cover: description |
| `top` | `self` | `float` | Get the cover at the top border  Returns:     concrete cover at the top |
| `top` | `self, concrete_cover: float` | `None` | Set the cover at the top border  Args:     concrete_cover: description |
| `bottom` | `self` | `float` | Get the cover at the bottom border  Returns:     concrete cover at the bottom |
| `bottom` | `self, concrete_cover: float` | `None` | Set the cover at the bottom border  Args:     concrete_cover: description |
| `from_reinforcement_definition` | `self, reinf_def: ReinforcementDefinition` | `None` | Get the cover from the reinforcement definition  Args:     reinf_def: reinforcement definition |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the concrete cover properties class
"""

from __future__ import annotations

from ReinforcementDefinition import ReinforcementDefinition


class ConcreteCoverProperties():
    """ Implementation of the concrete cover properties class

    The class includes concrete cover properties for the
    left, right, top and bottom border
    """

    def __init__(self,
                 left  : float = 0,
                 right : float = 0,
                 top   : float = 0,
                 bottom: float = 0):
        """ Set the properties of the concrete cover

        Args:
            left:   Concrete cover at the left border
            right:  Concrete cover at the right border
            top:    Concrete cover at the top border
            bottom: Concrete cover at the bottom border
        """

        self.prop_left   = left
        self.prop_right  = right
        self.prop_top    = top
        self.prop_bottom = bottom

    def __repr__(self):
        """ convert to string
        """

        return f"<{self.__class__.__name__}>\n"     \
                "   left    = {self.prop_left}\n"   \
                "   right   = {self.prop_right}\n"  \
                "   top     = {self.prop_top}\n"    \
                "   bottom  = {self.prop_bottom}\n"

    @staticmethod
    def all(concrete_cover: float) -> ConcreteCoverProperties:
        """ Set the properties of the concrete cover for all borders

        Args:
            concrete_cover: concrete cover for all sides

        Returns:
            concrete cover properties
        """

        return ConcreteCoverProperties(concrete_cover, concrete_cover, concrete_cover, concrete_cover)


    @staticmethod
    def left_right_bottom(left  : float,
                          right : float,
                          bottom: float) -> ConcreteCoverProperties:
        """ Set the properties of the concrete cover

        Args:
            left:   description
            right:  description
            bottom: description

        Returns:
            concrete cover properties
        """

        return ConcreteCoverProperties(left, right, 0, bottom)


    @staticmethod
    def left_right(left : float,
                   right: float) -> ConcreteCoverProperties:
        """ Set the properties of the concrete cover

        Args:
            left:  description
            right: description

        Returns:
            concrete cover properties
        """

        return ConcreteCoverProperties(left, right, 0, 0)


    @staticmethod
    def top_bottom(top   : float,
                   bottom: float) -> ConcreteCoverProperties:
        """ Set the properties of the concrete cover

        Args:
            top:    description
            bottom: description

        Returns:
            concrete cover properties
        """

        return ConcreteCoverProperties(0, 0, top, bottom)


    @property
    def left(self) -> float:
        """ Get the cover at the left border

        Returns:
            concrete cover at the left
        """
        return self.prop_left


    @left.setter
    def left(self,
             concrete_cover: float):
        """ Set the cover at the left border

        Args:
            concrete_cover: description
        """
        self.prop_left = concrete_cover


    @property
    def right(self) -> float:
        """ Get the cover at the right border

        Returns:
            concrete cover at the right
        """
        return self.prop_right


    @right.setter
    def right(self,
              concrete_cover: float):
        """ Set the cover at the right border

        Args:
            concrete_cover: description
        """
        self.prop_right = concrete_cover


    @property
    def top(self) -> float:
        """ Get the cover at the top border

        Returns:
            concrete cover at the top
        """
        return self.prop_top


    @top.setter
    def top(self,
            concrete_cover: float):
        """ Set the cover at the top border

        Args:
            concrete_cover: description
        """
        self.prop_top = concrete_cover


    @property
    def bottom(self) -> float:
        """ Get the cover at the bottom border

        Returns:
            concrete cover at the bottom
        """
        return self.prop_bottom


    @bottom.setter
    def bottom(self,
               concrete_cover: float):
        """ Set the cover at the bottom border

        Args:
            concrete_cover: description
        """
        self.prop_bottom = concrete_cover


    def from_reinforcement_definition(self,
                                      reinf_def: ReinforcementDefinition):
        """ Get the cover from the reinforcement definition

        Args:
            reinf_def: reinforcement definition
        """

        self.prop_left   = reinf_def.get_value("ShapeCoverLeft", self.left)
        self.prop_right  = reinf_def.get_value("ShapeCoverRight", self.right)
        self.prop_bottom = reinf_def.get_value("ShapeCoverBottom", self.bottom)
        self.prop_top    = reinf_def.get_value("ShapeCoverTop", self.top)

```

</details>