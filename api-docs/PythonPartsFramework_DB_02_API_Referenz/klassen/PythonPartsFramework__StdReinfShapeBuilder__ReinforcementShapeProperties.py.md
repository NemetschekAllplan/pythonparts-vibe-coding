---
title: "ReinforcementShapeProperties"
source: "PythonPartsFramework\StdReinfShapeBuilder\ReinforcementShapeProperties.py"
type: "class"
category: "02_API_Referenz"
tags:
  - bewehrung
related:
  -
last_updated: "2026-02-20"
---


# ReinforcementShapeProperties

> **Pfad:** `PythonPartsFramework\StdReinfShapeBuilder\ReinforcementShapeProperties.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `bewehrung`

## Übersicht

Implementation of the reinforcement shape properties class

## Abhängigkeiten

- `NemAll_Python_Reinforcement`
- `__future__`

## Klassen

### `ReinforcementShapeProperties`

Reinforcement shape properties class representing the properties relevant
for a reinforcement shape, such as bar diameter, steel grade or diameter of the
bending roller.

This class is a container for properties relevant for rebars as well as meshes.
Use the dedicated constructor methods (rebar() or mesh()), to define properties
for a rebar or for a mesh respectively.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, diameter: float, bending_roller: float, steel_grade: int, concrete_grade: int, bending_shape_type: AllplanReinf.BendingShapeType, mesh_type: str, mesh_bending_direction: AllplanReinf.MeshBendingDirection` | `None` | Default constructor  Args:     diameter:               Bar diameter     bending_roller:         Default bending roller (-1 = default for diameter)     steel_grade:            Steel grade     concrete_grade:         Concrete grade as index of the global list starting from 0.                             Set to -1 to use global value from the settings.     bending_shape_type:     Bending shape type     mesh_type:              Mesh type     mesh_bending_direction: Mesh bending direction |
| `__repr__` | `self` | `None` | - |
| `__eq__` | `self, other` | `None` | comparison operator  |
| `rebar` | `cls, diameter: float, bending_roller: float, steel_grade: int, concrete_grade: int, bending_shape_type: AllplanReinf.BendingShapeType` | `ReinforcementShapeProperties` | Constructs reinforcement shape properties with data relevant for a rebar  Args:     diameter:           Bar diameter     bending_roller:     Default bending roller as a multiple of bar diameter     steel_grade:        Steel grade as index of the global list     concrete_grade:     Concrete grade as index of the global list starting from 0.                         Set to -1 to use global value from the settings.     bending_shape_type: Bending shape type  Returns:     Reinforcement shape properties for a mesh |
| `mesh` | `cls, mesh_type: str, mesh_bending_direction: AllplanReinf.MeshBendingDirection, bending_roller: float, concrete_grade: int, bending_shape_type: AllplanReinf.BendingShapeType` | `ReinforcementShapeProperties` | Constructs reinforcement shape properties with data relevant for a mesh  Args:     mesh_type:              Mesh type     mesh_bending_direction: Mesh bending direction     concrete_grade:         Concrete grade as index of the global list starting from 0.                             Set to -1 to use global value from the settings.     bending_roller:         Default bending roller as a multiple of bar diameter     bending_shape_type:     Bending shape type  Returns:     Reinforcement shape properties for a mesh |
| `diameter` | `self` | `float` | Bar diameter          |
| `diameter` | `self, diameter: float` | `None` | - |
| `bending_roller` | `self` | `float` | Bending roller diameter as a multiple of bar diameter          |
| `bending_roller` | `self, bending_roller: float` | `None` | - |
| `steel_grade` | `self` | `int` | Steel grade as index of the global table          |
| `steel_grade` | `self, steel_grade: int` | `None` | - |
| `concrete_grade` | `self` | `int` | Concrete grade as index of the global list starting from 0          |
| `concrete_grade` | `self, concrete_grade: int` | `None` | - |
| `bending_shape_type` | `self` | `AllplanReinf.BendingShapeType` | Bending shape type          |
| `bending_shape_type` | `self, bending_shape_type: AllplanReinf.BendingShapeType` | `None` | - |
| `mesh_type` | `self` | `str` | Mesh type          |
| `mesh_type` | `self, mesh_type: str` | `None` | - |
| `mesh_bending_direction` | `self` | `AllplanReinf.MeshBendingDirection` | Mesh bending direction          |
| `mesh_bending_direction` | `self, mesh_bending_direction: AllplanReinf.MeshBendingDirection` | `None` | - |
| `deep_copy` | `self` | `'ReinforcementShapeProperties'` | Execute a deep copy of the data  Returns:     copy of the object |
| `to_reinforcementshapebarproperties_string` | `self` | `str` | Convert to a string.  Returns:     String for the reinforcementshapebarproperties value type |
| `to_reinforcementshapemeshproperties_string` | `self` | `str` | Convert to a string.  Returns:     String for the reinforcementshapebarproperties value type |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
"""Implementation of the reinforcement shape properties class
"""
from __future__ import annotations

import NemAll_Python_Reinforcement as AllplanReinf


class ReinforcementShapeProperties():
    """Reinforcement shape properties class representing the properties relevant
    for a reinforcement shape, such as bar diameter, steel grade or diameter of the
    bending roller.

    This class is a container for properties relevant for rebars as well as meshes.
    Use the dedicated constructor methods (rebar() or mesh()), to define properties
    for a rebar or for a mesh respectively.
    """

    def __init__(self,
                 diameter              : float,
                 bending_roller        : float,
                 steel_grade           : int,
                 concrete_grade        : int,
                 bending_shape_type    : AllplanReinf.BendingShapeType,
                 mesh_type             : str,
                 mesh_bending_direction: AllplanReinf.MeshBendingDirection ):
        """Default constructor

        Args:
            diameter:               Bar diameter
            bending_roller:         Default bending roller (-1 = default for diameter)
            steel_grade:            Steel grade
            concrete_grade:         Concrete grade as index of the global list starting from 0.
                                    Set to -1 to use global value from the settings.
            bending_shape_type:     Bending shape type
            mesh_type:              Mesh type
            mesh_bending_direction: Mesh bending direction
        """

        if mesh_type != "":
            mesh_data = AllplanReinf.ReinforcementShapeBuilder.GetMeshData(mesh_type)

            diameter = mesh_data.DiameterLongitudinal \
                      if mesh_bending_direction == AllplanReinf.MeshBendingDirection.LongitudinalBars \
                      else mesh_data.DiameterCross

        if steel_grade == -1:
            steel_grade = AllplanReinf.ReinforcementSettings.GetSteelGrade()

        if bending_roller == -1:
            bending_roller = AllplanReinf.BendingRollerService.GetBendingRollerFactor(diameter, steel_grade,
                                                                                      concrete_grade, False)

        if mesh_type == "-1":
            mesh_type = AllplanReinf.ReinforcementSettings.GetMeshType()

        self.prop_diameter               = diameter
        self.prop_bending_roller         = bending_roller
        self.prop_steel_grade            = steel_grade
        self.prop_concrete_grade         = concrete_grade
        self.prop_bending_shape_type     = bending_shape_type
        self.prop_mesh_type              = mesh_type
        self.prop_mesh_bending_direction = mesh_bending_direction

    def __repr__(self):
        description =  '%s(\n'\
            '   Diameter            (%s)\n'\
            '   BendingRoller       (%s)\n'\
            '   SteelGrade          (%s)\n'\
            '   ConcreteGrade       (%s)\n'\
            '   BendingShapeType    (%s)\n'\
            '   MeshType            (%s)\n'\
            '   MeshBendingDirection(%s)\n'\
            ')\n'   \
            % (self.__class__.__name__,
               self.prop_diameter,
               self.prop_bending_roller,
               self.prop_steel_grade,
               self.prop_concrete_grade,
               self.prop_bending_shape_type,
               self.prop_mesh_type,
               self.prop_mesh_bending_direction)
        return description


    def __eq__(self, other):
        """ comparison operator """

        if isinstance(other, ReinforcementShapeProperties):
            if self.prop_diameter != other.prop_diameter:
                return False
            if self.prop_bending_roller != other.prop_bending_roller:
                return False
            if self.prop_steel_grade != other.prop_steel_grade:
                return False
            if self.prop_concrete_grade != other.prop_concrete_grade:
                return False
            if self.prop_bending_shape_type != other.prop_bending_shape_type:
                return False
            if self.prop_mesh_type != other.prop_mesh_type:
                return False
            if self.prop_mesh_bending_direction != other.prop_mesh_bending_direction:
                return False

            return True

        return False


    @classmethod
    def rebar(cls,
              diameter          : float,
              bending_roller    : float,
              steel_grade       : int,
              concrete_grade    : int,
              bending_shape_type: AllplanReinf.BendingShapeType)  -> ReinforcementShapeProperties:
        """Constructs reinforcement shape properties with data relevant for a rebar

        Args:
            diameter:           Bar diameter
            bending_roller:     Default bending roller as a multiple of bar diameter
            steel_grade:        Steel grade as index of the global list
            concrete_grade:     Concrete grade as index of the global list starting from 0.
                                Set to -1 to use global value from the settings.
            bending_shape_type: Bending shape type

        Returns:
            Reinforcement shape properties for a mesh
        """

        return cls(diameter, bending_roller, steel_grade, concrete_grade,
                   bending_shape_type, "",
                   AllplanReinf.MeshBendingDirection.LongitudinalBars)


    @classmethod
    def mesh(cls,
             mesh_type             : str,
             mesh_bending_direction: AllplanReinf.MeshBendingDirection,
             bending_roller        : float,
             concrete_grade        : int,
             bending_shape_type    : AllplanReinf.BendingShapeType) -> ReinforcementShapeProperties:
        """Constructs reinforcement shape properties with data relevant for a mesh

        Args:
            mesh_type:              Mesh type
            mesh_bending_direction: Mesh bending direction
            concrete_grade:         Concrete grade as index of the global list starting from 0.
                                    Set to -1 to use global value from the settings.
            bending_roller:         Default bending roller as a multiple of bar diameter
            bending_shape_type:     Bending shape type

        Returns:
            Reinforcement shape properties for a mesh
        """

        return cls(0, bending_roller, 4, concrete_grade,
                   bending_shape_type, mesh_type, mesh_bending_direction)


    @property
    def diameter(self) -> float:
        """Bar diameter
        """
        return self.prop_diameter

    @diameter.setter
    def diameter(self, diameter: float):
        self.prop_diameter = diameter

    @property
    def bending_roller(self) -> float:
        """Bending roller diameter as a multiple of bar diameter
        """
        return self.prop_bending_roller

    @bending_roller.setter
    def bending_roller(self, bending_roller: float):
        self.prop_bending_roller = bending_roller

    @property
    def steel_grade(self) -> int:
        """Steel grade as index of the global table
        """
        return self.prop_steel_grade

    @steel_grade.setter
    def steel_grade(self, steel_grade: int):
        self.prop_steel_grade = steel_grade

    @property
    def concrete_grade(self) -> int:
        """Concrete grade as index of the global list starting from 0
        """
        return self.prop_concrete_grade

    @concrete_grade.setter
    def concrete_grade(self, concrete_grade: int):
        self.prop_concrete_grade = concrete_grade

    @property
    def bending_shape_type(self) -> AllplanReinf.BendingShapeType:
        """Bending shape type
        """
        return self.prop_bending_shape_type

    @bending_shape_type.setter
    def bending_shape_type(self, bending_shape_type: AllplanReinf.BendingShapeType):
        self.prop_bending_shape_type = bending_shape_type

    @property
    def mesh_type(self) -> str:
        """Mesh type
        """
        return self.prop_mesh_type

    @mesh_type.setter
    def mesh_type(self, mesh_type: str):
        self.prop_mesh_type = mesh_type

    @property
    def mesh_bending_direction(self) -> AllplanReinf.MeshBendingDirection:
        """Mesh bending direction
        """
        return self.prop_mesh_bending_direction

    @mesh_bending_direction.setter
    def mesh_bending_direction(self, mesh_bending_direction: AllplanReinf.MeshBendingDirection):
        self.prop_mesh_bending_direction = mesh_bending_direction


    def deep_copy(self) -> 'ReinforcementShapeProperties':
        """Execute a deep copy of the data

        Returns:
            copy of the object
        """

        return ReinforcementShapeProperties(self.diameter, self.bending_roller, self.steel_grade, self.concrete_grade,
                                            self.bending_shape_type, self.mesh_type, self.mesh_bending_direction)


    def to_reinforcementshapebarproperties_string(self) -> str:
        """Convert to a string.

        Returns:
            String for the reinforcementshapebarproperties value type
        """

        description =  '%s(\n'\
            '   ConcreteGrade       (%s),\n'\
            '   SteelGrade          (%s),\n'\
            '   Diameter            (%s),\n'\
            '   BendingRoller       (%s)\n'\
            ')\n'   \
            % (self.__class__.__name__,
               self.prop_concrete_grade,
               self.prop_steel_grade,
               self.prop_diameter,
               self.prop_bending_roller)
        return description


    def to_reinforcementshapemeshproperties_string(self) -> str:
        """Convert to a string.

        Returns:
            String for the reinforcementshapebarproperties value type
        """

        description =  '%s(\n'\
            '   ConcreteGrade       (%s),\n'\
            '   MeshType            (%s),\n'\
            '   MeshBendingDirection(%s),\n'\
            '   BendingRoller       (%s)\n'\
            ')\n'   \
            % (self.__class__.__name__,
               self.prop_concrete_grade,
               self.prop_mesh_type,
               self.prop_mesh_bending_direction,
               self.prop_bending_roller)
        return description

```

</details>