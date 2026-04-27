---
title: "TransformationStack"
source: "PythonPartsFramework\Utils\Geometry\TransformationStack.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TransformationStack

> **Pfad:** `PythonPartsFramework\Utils\Geometry\TransformationStack.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the transformation stack

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `enum`
- `typing`

## Klassen

### `LengthUnit`

length unit enum
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `AngleUnit`

angle unit enum
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `TransformationStack`

implementation of the transformation stack
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, length_unit: LengthUnit=LengthUnit.MM, angle_unit: AngleUnit=AngleUnit.DEGREE` | `None` | initialize  Args:     length_unit: length unit     angle_unit:  angle unit |
| `length_fac` | `self` | `float` | get the length factor  Returns:     length factor |
| `translate_xyz` | `self, vec_x: float, vec_y: float, vec_z: float` | `None` | add a x/y/z translation to the stack  Args:     vec_x: x translation     vec_y: y translation     vec_z: z translation |
| `translate` | `self, vec: AllplanGeo.Vector3D` | `None` | add a vector translation to the stack  Args:     vec:  translation vector |
| `translate_xy` | `self, vec_x: float, vec_y: float` | `None` | add a x/y translation to the stack  Args:     vec_x: x translation     vec_y: y translation |
| `translate_x` | `self, vec_x: float` | `None` | add a x translation to the stack  Args:     vec_x: x translation |
| `translate_y` | `self, vec_y: float` | `None` | add a y translation to the stack  Args:     vec_y: y translation |
| `translate_z` | `self, vec_z: float` | `None` | add a z translation to the stack  Args:     vec_z: z translation |
| `rotate_x` | `self, angle: float | AllplanGeo.Angle, axis_point: AllplanGeo.Point2D | AllplanGeo.Point3D=AllplanGeo.Point3D()` | `None` | add a rotation around the x axis to the stack  Args:     angle:      rotation angle in the defined angle unit     axis_point: axis point (optional, default is the origin) |
| `rotate_y` | `self, angle: float | AllplanGeo.Angle, axis_point: AllplanGeo.Point2D | AllplanGeo.Point3D=AllplanGeo.Point3D()` | `None` | add a rotation around the y axis to the stack  Args:     angle:      rotation angle in the defined angle unit     axis_point: axis point |
| `rotate_z` | `self, angle: float | AllplanGeo.Angle, axis_point: AllplanGeo.Point2D | AllplanGeo.Point3D=AllplanGeo.Point3D()` | `None` | add a rotation around the z axis to the stack  Args:     angle:      rotation angle in the defined angle unit     axis_point: axis point |
| `scale` | `self, x_fac: float, y_fac: float, z_fac: float` | `None` | add a scaling to the stack  Args:     x_fac: scale factor in x direction     y_fac: scale factor in y direction     z_fac: scale factor in z direction |
| `scale_xy` | `self, x_fac: float, y_fac: float` | `None` | add a x/y scaling to the stack  Args:     x_fac: scale factor in x direction     y_fac: scale factor in y direction |
| `scale_x` | `self, x_fac: float` | `None` | add a x scaling to the stack  Args:     x_fac: scale factor in x direction |
| `scale_y` | `self, y_fac: float` | `None` | add a y scaling to the stack  Args:     y_fac: scale factor in y direction |
| `scale_z` | `self, z_fac: float` | `None` | add a z scaling to the stack  Args:     z_fac: scale factor in z direction |
| `trans_matrix` | `self` | `AllplanGeo.Matrix3D` | get the current transformation matrix  Returns:     current transformation matrix |
| `restore` | `self, count: int` | `None` | restore a transformation  Args:     count: description |
| `restore_all` | `self` | `None` | restore all transformations          |
| `append` | `self, matrix: AllplanGeo.Matrix3D` | `None` | append a transformation matrix to the stack  Args:     matrix: matrix to append |
| `pop` | `self, pos: int=-1` | `AllplanGeo.Matrix3D` | pop the last transformation matrix from the stack  Args:     pos:  index of the transformation matrix to pop, -1 for the last one  Returns:     returns |
| `__getitem__` | `self, pos: int` | `AllplanGeo.Matrix3D` | get a transformation matrix from the stack  Args:     pos:  index of the transformation matrix  Returns:     transformation matrix at the given index |
| `transform` | `self, geo_ele: Any` | `Any` | transform a geometry element with the current transformation matrix  Args:     geo_ele: geometry element to transform  Returns:     transformed geometry element |
| `save_stack` | `self` | `None` | save and clear the stack          |
| `restore_stack` | `self` | `None` | restore the stack          |
| `__rotate` | `self, angle: float | int | AllplanGeo.Angle, axis_point: AllplanGeo.Point2D | AllplanGeo.Point3D, axis_vec: AllplanGeo.Vector3D` | `None` | add a rotation around the x axis to the stack  Args:     angle:      rotation angle in the defined angle unit     axis_point: axis point     axis_vec:   axis vector |
| `__create_matrix` | `self` | `None` | create the current transformation matrix from the stack          |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the transformation stack
"""

# pylint: disable=consider-ternary-expression

import enum

from typing import Any

import NemAll_Python_Geometry as AllplanGeo


class LengthUnit(enum.IntEnum):
    """ length unit enum
    """

    MM = 0
    CM = 1
    DM = 2
    M  = 3


class AngleUnit(enum.IntEnum):
    """ angle unit enum
    """

    RADIAN = 0
    DEGREE = 1


class TransformationStack():
    """ implementation of the transformation stack
    """

    def __init__(self,
                 length_unit: LengthUnit = LengthUnit.MM,
                 angle_unit : AngleUnit  = AngleUnit.DEGREE):
        """ initialize

        Args:
            length_unit: length unit
            angle_unit:  angle unit
        """

        self.__angle_is_rad = angle_unit == AngleUnit.RADIAN

        self.__trans_stack : list[tuple[AllplanGeo.Matrix3D, bool]] = []

        self.__saved_trans_stack = []

        self.__trans_matrix   = AllplanGeo.Matrix3D()
        self.__repair_polyhed = False

        self.__length_fac = [1., 10., 100., 1000.][length_unit]


    @property
    def length_fac(self) -> float:
        """ get the length factor

        Returns:
            length factor
        """

        return self.__length_fac


    def translate_xyz(self,
                      vec_x: float,
                      vec_y: float,
                      vec_z: float):
        """ add a x/y/z translation to the stack

        Args:
            vec_x: x translation
            vec_y: y translation
            vec_z: z translation
        """

        trans_mat = AllplanGeo.Matrix3D()
        trans_mat.SetTranslation(AllplanGeo.Vector3D(vec_x, vec_y, vec_z) * self.__length_fac)

        self.__trans_stack.append((trans_mat, False))

        self.__create_matrix()


    def translate(self,
                  vec : AllplanGeo.Vector3D):
        """ add a vector translation to the stack

        Args:
            vec:  translation vector
        """

        trans_mat = AllplanGeo.Matrix3D()
        trans_mat.SetTranslation(vec * self.__length_fac)

        self.__trans_stack.append((trans_mat, False))

        self.__create_matrix()


    def translate_xy(self,
                     vec_x: float,
                     vec_y: float):
        """ add a x/y translation to the stack

        Args:
            vec_x: x translation
            vec_y: y translation
        """

        trans_mat = AllplanGeo.Matrix3D()
        trans_mat.SetTranslation(AllplanGeo.Vector3D(vec_x, vec_y, 0) * self.__length_fac)

        self.__trans_stack.append((trans_mat, False))

        self.__create_matrix()


    def translate_x(self,
                    vec_x: float):
        """ add a x translation to the stack

        Args:
            vec_x: x translation
        """

        trans_mat = AllplanGeo.Matrix3D()
        trans_mat.SetTranslation(AllplanGeo.Vector3D(vec_x, 0, 0) * self.__length_fac)

        self.__trans_stack.append((trans_mat, False))

        self.__create_matrix()


    def translate_y(self,
                    vec_y: float):
        """ add a y translation to the stack

        Args:
            vec_y: y translation
        """

        trans_mat = AllplanGeo.Matrix3D()
        trans_mat.SetTranslation(AllplanGeo.Vector3D(0, vec_y, 0) * self.__length_fac)

        self.__trans_stack.append((trans_mat, False))

        self.__create_matrix()


    def translate_z(self,
                    vec_z: float):
        """ add a z translation to the stack

        Args:
            vec_z: z translation
        """

        trans_mat = AllplanGeo.Matrix3D()
        trans_mat.SetTranslation(AllplanGeo.Vector3D(0, 0, vec_z) * self.__length_fac)

        self.__trans_stack.append((trans_mat, False))

        self.__create_matrix()


    def rotate_x(self,
                 angle     : (float | AllplanGeo.Angle),
                 axis_point: (AllplanGeo.Point2D | AllplanGeo.Point3D) = AllplanGeo.Point3D()):
        """ add a rotation around the x axis to the stack

        Args:
            angle:      rotation angle in the defined angle unit
            axis_point: axis point (optional, default is the origin)
        """

        self.__rotate(angle, axis_point, AllplanGeo.Vector3D(1000, 0, 0))


    def rotate_y(self,
                 angle     : (float | AllplanGeo.Angle),
                 axis_point: (AllplanGeo.Point2D | AllplanGeo.Point3D) = AllplanGeo.Point3D()):
        """ add a rotation around the y axis to the stack

        Args:
            angle:      rotation angle in the defined angle unit
            axis_point: axis point
        """

        self.__rotate(angle, axis_point, AllplanGeo.Vector3D(0, 1000, 0))


    def rotate_z(self,
                 angle     : (float | AllplanGeo.Angle),
                 axis_point: (AllplanGeo.Point2D | AllplanGeo.Point3D) = AllplanGeo.Point3D()):
        """ add a rotation around the z axis to the stack

        Args:
            angle:      rotation angle in the defined angle unit
            axis_point: axis point
        """

        self.__rotate(angle, axis_point, AllplanGeo.Vector3D(0, 0, 1000))


    def scale(self,
              x_fac: float,
              y_fac: float,
              z_fac: float):
        """ add a scaling to the stack

        Args:
            x_fac: scale factor in x direction
            y_fac: scale factor in y direction
            z_fac: scale factor in z direction
        """

        scale_mat = AllplanGeo.Matrix3D()

        scale_mat.SetScaling(x_fac, y_fac, z_fac)

        self.__trans_stack.append((scale_mat, x_fac < 0 or y_fac < 0 or z_fac < 0))

        self.__create_matrix()


    def scale_xy(self,
                 x_fac: float,
                 y_fac: float):
        """ add a x/y scaling to the stack

        Args:
            x_fac: scale factor in x direction
            y_fac: scale factor in y direction
        """

        scale_mat = AllplanGeo.Matrix3D()

        scale_mat.SetScaling(x_fac, y_fac, 1)

        self.__trans_stack.append((scale_mat, x_fac < 0 or y_fac < 0))

        self.__create_matrix()


    def scale_x(self,
                x_fac: float):
        """ add a x scaling to the stack

        Args:
            x_fac: scale factor in x direction
        """

        scale_mat = AllplanGeo.Matrix3D()

        scale_mat.SetScaling(x_fac, 1, 1)

        self.__trans_stack.append((scale_mat, x_fac < 0))

        self.__create_matrix()


    def scale_y(self,
                y_fac: float):
        """ add a y scaling to the stack

        Args:
            y_fac: scale factor in y direction
        """

        scale_mat = AllplanGeo.Matrix3D()

        scale_mat.SetScaling(1, y_fac, 1)

        self.__trans_stack.append((scale_mat, y_fac < 0))

        self.__create_matrix()


    def scale_z(self,
                z_fac: float):
        """ add a z scaling to the stack

        Args:
            z_fac: scale factor in z direction
        """

        scale_mat = AllplanGeo.Matrix3D()

        scale_mat.SetScaling(1, 1, z_fac)

        self.__trans_stack.append((scale_mat, z_fac < 0))

        self.__create_matrix()


    @property
    def trans_matrix(self) -> AllplanGeo.Matrix3D:
        """ get the current transformation matrix

        Returns:
            current transformation matrix
        """

        return self.__trans_matrix


    def restore(self,
                count: int):
        """ restore a transformation

        Args:
            count: description
        """

        self.__trans_stack  = self.__trans_stack[:-count]
        self.__create_matrix()


    def restore_all(self):
        """ restore all transformations
        """

        self.__trans_stack.clear()

        self.__trans_matrix   = AllplanGeo.Matrix3D()
        self.__repair_polyhed = False

        self.__trans_matrix = AllplanGeo.Matrix3D()


    def append(self,
               matrix: AllplanGeo.Matrix3D):
        """ append a transformation matrix to the stack

        Args:
            matrix: matrix to append
        """

        self.__trans_stack.append((matrix, False))


    def pop(self,
            pos : int = -1) -> AllplanGeo.Matrix3D:
        """ pop the last transformation matrix from the stack

        Args:
            pos:  index of the transformation matrix to pop, -1 for the last one

        Returns:
            returns
        """

        matrix, _ = self.__trans_stack.pop(pos)

        self.__create_matrix()

        return matrix


    def __getitem__(self,
                    pos : int) -> AllplanGeo.Matrix3D:
        """ get a transformation matrix from the stack

        Args:
            pos:  index of the transformation matrix

        Returns:
            transformation matrix at the given index
        """

        return self.__trans_stack[pos][0]


    def transform(self,
                  geo_ele: Any) -> Any:
        """ transform a geometry element with the current transformation matrix

        Args:
            geo_ele: geometry element to transform

        Returns:
            transformed geometry element
        """

        trans_geo_ele = AllplanGeo.Transform(geo_ele, self.__trans_matrix)

        if not self.__repair_polyhed or not isinstance(trans_geo_ele, AllplanGeo.Polyhedron3D):
            return trans_geo_ele


        #----------------- invert the extruded element if needed (need to create a positive volume)

        volume = AllplanGeo.CalcMass(trans_geo_ele)[1]

        if volume > 0 and not trans_geo_ele.IsNegative():
            return trans_geo_ele

        if volume < 0 and trans_geo_ele.IsNegative():
            trans_geo_ele.Invert()

            return trans_geo_ele

        if volume < 0 and not trans_geo_ele.IsNegative():
            trans_geo_ele.InvertWithFlagUnchanged()

            return trans_geo_ele

        return trans_geo_ele


    def save_stack(self):
        """ save and clear the stack
        """

        self.__saved_trans_stack = list(self.__trans_stack)

        self.__trans_stack.clear()

        self.__trans_matrix = AllplanGeo.Matrix3D()


    def restore_stack(self):
        """ restore the stack
        """

        self.__trans_stack  = list(self.__saved_trans_stack)
        self.__create_matrix()


    def __rotate(self,
                 angle     : (float | int | AllplanGeo.Angle),
                 axis_point: (AllplanGeo.Point2D | AllplanGeo.Point3D),
                 axis_vec  : AllplanGeo.Vector3D):
        """ add a rotation around the x axis to the stack

        Args:
            angle:      rotation angle in the defined angle unit
            axis_point: axis point
            axis_vec:   axis vector
        """

        if isinstance(angle, (float, int)):
            rot_angle = AllplanGeo.Angle(angle) if self.__angle_is_rad else AllplanGeo.Angle.FromDeg(angle)
        else:
            rot_angle = AllplanGeo.Angle(angle)

        if isinstance(axis_point, AllplanGeo.Point2D):
            axis_point = axis_point.To3D

        axis = AllplanGeo.Line3D(axis_point, axis_point + axis_vec)

        rot_mat = AllplanGeo.Matrix3D()

        rot_mat.SetRotation(axis, rot_angle)

        self.__trans_stack.append((rot_mat, False))

        self.__create_matrix()


    def __create_matrix(self):
        """ create the current transformation matrix from the stack
        """

        mat = AllplanGeo.Matrix3D()

        self.__repair_polyhed = False

        for trans_mat, repair in self.__trans_stack:
            mat = trans_mat * mat

            self.__repair_polyhed = self.__repair_polyhed or repair

        self.__trans_matrix = mat

```

</details>