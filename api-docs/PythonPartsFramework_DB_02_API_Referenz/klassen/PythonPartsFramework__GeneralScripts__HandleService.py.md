---
title: "HandleService"
source: "PythonPartsFramework\GeneralScripts\HandleService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - script
related:
  -
last_updated: "2026-02-20"
---


# HandleService

> **Pfad:** `PythonPartsFramework\GeneralScripts\HandleService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `script`

## Übersicht

Implementation of the handle service

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementParameterPropertyUtil`
- `HandleDirection`
- `HandleParameterData`
- `HandleParameterType`
- `HandleProperties`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `TypeCollections`
- `__future__`
- `math`
- `typing`

## Klassen

### `HandleService`

Definition of class HandleService
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_abscissa_line` | `trans_mat: AllplanGeo.Matrix3D, handle_to_asso_mat: AllplanGeo.Matrix3D, handle_prop: HandleProperties, coord_input: AllplanIFW.CoordinateInput` | `None` | Set the abscissa line from the handle direction  Args:     trans_mat:          Transformation matrix     handle_to_asso_mat: Transformation matrix from world handle to asso handle     handle_prop:        Handle property     coord_input:        API object for the coordinate input, element selection, ... in the Allplan view |
| `draw_direction_symbol` | `trans_mat: AllplanGeo.Matrix3D, handle_prop: HandleProperties, coord_input: AllplanIFW.CoordinateInput, asso_ref_ele: AllplanEleAdapter.BaseElementAdapter | None, use_system_angle: bool=True` | `None` | Draw the direction symbol for the handle  Args:     trans_mat:        Transformation matrix     handle_prop:      Handle property     coord_input:      API object for the coordinate input, element selection, ... in the Allplan view     asso_ref_ele:     Associative view reference element     use_system_angle: use system angle state |
| `add_arrow` | `dir_line: AllplanGeo.Line3D, dir_line_length: float, view_proj: AllplanIFW.ViewWorldProjection, prev_ele_list: ModelEleList` | `None` | add the arrow  Args:     dir_line:        direction line     dir_line_length: direction line length     view_proj:       view world projection     prev_ele_list:   preview element list |
| `is_coordinate_input_possible` | `handle_prop: HandleProperties, ref_pnt: AllplanGeo.Point3D, handle_pnt: AllplanGeo.Point3D` | `bool` | Check for an allowed coordinate input  Args:     handle_prop: Handle property     ref_pnt:     Reference point     handle_pnt:  Handle point  Returns:     coordinate input state |
| `create_orthogonal_handle` | `line2d: AllplanGeo.Line2D, x_local: float, y_local: float, from_start: bool, z_coord: float, name: str` | `HandleProperties` | Create an orthogonal handle on a 2D line  Args:     line2d:     2D-line     x_local:    local x coordinate     y_local:    local y coordinate     from_start: x_local from start: True/False     z_coord:    z coordinate of the handle point     name:       name of the modified property  Returns:     created handle |
| `transform_handles` | `handle_list: list[HandleProperties], trans_mat: AllplanGeo.Matrix3D` | `None` | Transform the handles  Args:     handle_list: handle list     trans_mat:   transformation matrix |
| `set_input_point_for_isometric_projection` | `input_pnt: AllplanGeo.Point3D, handle_point: AllplanGeo.Point3D, iso_projection: AllplanIFW.eProjectionType` | `None` | Set the handle input point for an isometric projection  Args:     input_pnt:      input point     handle_point:   handle point     iso_projection: isometric projection |
| `get_property_values` | `build_ele_list: list[BuildingElement], handle_prop: HandleProperties` | `list[tuple[int, str, Any]]` | Get the property values for properties of the handle  Args:     build_ele_list: list with the building elements     handle_prop:    handle property  Returns:     list with the handle property values |
| `get_curve_points` | `handle_prop: HandleProperties` | `list[tuple[GeometryTyping.POLY_CURVES, list[GeometryTyping.POINTS]]]` | Get the curve points  Args:     handle_prop: handle property  Returns:     list with the original curve and the curve points |
| `__draw_distance_symbol` | `handle_pnt: AllplanGeo.Point3D, dist_vec: AllplanGeo.Vector3D, view_proj: AllplanIFW.ViewWorldProjection, dir_line_length: float, prev_ele_list: ModelEleList, system_angle: float, handle_move_dir: HandleParameterType, handle_trans_matrix: AllplanGeo.Matrix3D` | `bool` | draw a distance symbol  Args:     handle_pnt:          Handle point     dist_vec:            distance vector     view_proj:           view world projection     dir_line_length:     direction line length     prev_ele_list:       preview element list     system_angle:        system angle     handle_move_dir:     handle move direction     handle_trans_matrix: handle transformation matrix  Returns:     True if the symbol was drawn |
| `__draw_angle_symbol` | `trans_mat: AllplanGeo.Matrix3D, handle_prop: HandleProperties, handle_pnt: AllplanGeo.Point3D, dir_line_length: float, prev_ele_list: ModelEleList` | `None` | draw the angle symbol  Args:     trans_mat:       transformation matrix     handle_prop:     handle property     handle_pnt:      Handle point     dir_line_length: direction line length     prev_ele_list:   preview element list |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the handle service
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import math

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from HandleProperties import HandleProperties
from HandleDirection import HandleDirection
from HandleParameterData import HandleParameterData
from HandleParameterType import HandleParameterType

import BuildingElementParameterPropertyUtil

from TypeCollections import ModelEleList
from TypeCollections import GeometryTyping

if TYPE_CHECKING:
    from BuildingElement import BuildingElement

class HandleService:
    """ Definition of class HandleService
    """

    @staticmethod
    def set_abscissa_line(trans_mat         : AllplanGeo.Matrix3D,
                          handle_to_asso_mat: AllplanGeo.Matrix3D,
                          handle_prop       : HandleProperties,
                          coord_input       : AllplanIFW.CoordinateInput):
        """ Set the abscissa line from the handle direction

        Args:
            trans_mat:          Transformation matrix
            handle_to_asso_mat: Transformation matrix from world handle to asso handle
            handle_prop:        Handle property
            coord_input:        API object for the coordinate input, element selection, ... in the Allplan view
        """

        handle_move_dir = handle_prop.handle_move_dir

        handle_trans_matrix = handle_prop.trans_matrix

        mat = handle_trans_matrix * trans_mat * handle_to_asso_mat

        ref_pnt    = handle_prop.ref_point    * mat
        handle_pnt = handle_prop.handle_point * mat

        match handle_move_dir:
            case HandleDirection.X_DIR:
                dir_pnt = (handle_prop.ref_point + AllplanGeo.Vector3D(1000, 0, 0)) * mat

                coord_input.SetAbscissaElement(AllplanGeo.Line3D(ref_pnt, dir_pnt), handle_to_asso_mat)

            case HandleDirection.Y_DIR:
                dir_pnt = (handle_prop.ref_point + AllplanGeo.Vector3D(0, 1000, 0)) * mat

                coord_input.SetAbscissaElement(AllplanGeo.Line3D(ref_pnt, dir_pnt), handle_to_asso_mat)

            case HandleDirection.Z_DIR:
                dir_pnt = (handle_prop.ref_point + AllplanGeo.Vector3D(0, 0, 1000)) * mat

                coord_input.SetAbscissaElement(AllplanGeo.Line3D(ref_pnt, dir_pnt), handle_to_asso_mat)

            case HandleDirection.POINT_DIR | HandleDirection.Z_COORD:
                if handle_prop.center_point:
                    center_pnt = handle_prop.center_point

                    ref_pnt_vec    = AllplanGeo.Vector3D(center_pnt, handle_prop.ref_point)
                    handle_pnt_vec = AllplanGeo.Vector3D(center_pnt, handle_prop.handle_point)

                    radius      = ref_pnt_vec.GetLength()
                    start_angle = AllplanGeo.Vector2D(handle_pnt_vec).GetAngle().Deg
                    end_angle   = AllplanGeo.Vector2D(ref_pnt_vec).GetAngle().Deg

                    if start_angle > end_angle:
                        start_angle -= math.pi * 2

                    coord_input.SetAbscissaElement(AllplanGeo.Arc3D(center_pnt, radius, radius, start_angle, end_angle - start_angle),
                                                   handle_to_asso_mat)
                else:
                    coord_input.SetAbscissaElement(AllplanGeo.Line3D(ref_pnt, handle_pnt), handle_to_asso_mat)

            case HandleDirection.XZ_DIR:
                coord_input.SetInputPlane(AllplanGeo.Plane3D(handle_pnt, AllplanGeo.Vector3D(0, 1000.0, 0)))

            case HandleDirection.YZ_DIR:
                coord_input.SetInputPlane(AllplanGeo.Plane3D(handle_pnt, AllplanGeo.Vector3D(1000.0, 0, 0)))

            case HandleDirection.XY_DIR:
                coord_input.SetInputPlane(AllplanGeo.Plane3D(handle_pnt, AllplanGeo.Vector3D(0, 0, 1000.0)))

            case HandleDirection.PLANE_DIR:
                if handle_prop.plane is not None:
                    coord_input.SetInputPlane(handle_prop.plane * mat)

            case HandleDirection.VECTOR_DIR:
                if handle_prop.dir_vector is not None:
                    coord_input.SetAbscissaElement(AllplanGeo.Line3D(handle_pnt + handle_prop.dir_vector * handle_trans_matrix, handle_pnt),
                                                   handle_to_asso_mat)

                elif len(handle_prop.parameter_data) == 1 and handle_prop.parameter_data[0].dir_vector is not None:
                    coord_input.SetAbscissaElement(AllplanGeo.Line3D(handle_pnt + handle_prop.parameter_data[0].dir_vector * \
                                                                     handle_trans_matrix, handle_pnt),
                                                   handle_to_asso_mat)


    @staticmethod
    def draw_direction_symbol(trans_mat       : AllplanGeo.Matrix3D,
                              handle_prop     : HandleProperties,
                              coord_input     : AllplanIFW.CoordinateInput,
                              asso_ref_ele    : (AllplanEleAdapter.BaseElementAdapter | None),
                              use_system_angle: bool = True):
        """ Draw the direction symbol for the handle

        Args:
            trans_mat:        Transformation matrix
            handle_prop:      Handle property
            coord_input:      API object for the coordinate input, element selection, ... in the Allplan view
            asso_ref_ele:     Associative view reference element
            use_system_angle: use system angle state
        """

        trans_mat = handle_prop.trans_matrix * trans_mat

        ref_pnt    = handle_prop.ref_point    * trans_mat
        handle_pnt = handle_prop.handle_point * trans_mat

        dist_vec = AllplanGeo.Vector3D(ref_pnt, handle_pnt)

        view_proj = coord_input.GetViewWorldProjection()

        pix_factor, _ = view_proj.GetPixelFactor()

        dir_line_length = 50 / pix_factor

        prev_ele_list = ModelEleList()

        system_angle = AllplanSettings.InputAngleSettings.GetSystemAngle() if use_system_angle else 0


        #----------------- create the direction line

        for parameter_data in handle_prop.parameter_data:
            handle_move_dir = parameter_data.param_type

            if HandleService.__draw_distance_symbol(handle_pnt, dist_vec, view_proj, dir_line_length,
                                                    prev_ele_list, system_angle, handle_move_dir, handle_prop.trans_matrix):
                continue

            match handle_move_dir:
                case HandleParameterType.VECTOR_DISTANCE:
                    if (dir_vec := parameter_data.dir_vector if parameter_data.dir_vector is not None else handle_prop.dir_vector) is None:
                        continue

                    system_angle_mat = AllplanGeo.Matrix3D()
                    system_angle_mat.SetRotation(AllplanGeo.Line3D(0, 0, 0, 0, 0, 1000),
                                                AllplanGeo.Angle(system_angle))

                    dir_vec = dir_vec * handle_prop.trans_matrix * system_angle_mat

                    dir_line = AllplanGeo.Line3D(handle_pnt, handle_pnt + dir_vec)

                    start_pnt = dir_line.StartPoint

                    dir_line.TrimStart(-dir_line_length)

                    dir_line = AllplanGeo.Line3D(start_pnt, dir_line.StartPoint)

                    HandleService.add_arrow(dir_line, dir_line_length, view_proj, prev_ele_list)

                case HandleParameterType.POINT_DISTANCE | HandleParameterType.Z_COORD:
                    dir_line = AllplanGeo.Line3D(handle_pnt, ref_pnt)

                    start_pnt = dir_line.StartPoint

                    dir_line.TrimStart(-dir_line_length)

                    dir_line = AllplanGeo.Line3D(start_pnt, dir_line.StartPoint)

                    HandleService.add_arrow(dir_line, dir_line_length, view_proj, prev_ele_list)

                case HandleParameterType.ANGLE:
                    HandleService.__draw_angle_symbol(trans_mat, handle_prop, handle_pnt, dir_line_length, prev_ele_list)

        AllplanBaseEle.DrawElementPreview(coord_input.GetInputViewDocument(), AllplanGeo.Matrix3D(),
                                          prev_ele_list, False, asso_ref_ele, False, False)


    @staticmethod
    def add_arrow(dir_line       : AllplanGeo.Line3D,
                  dir_line_length: float,
                  view_proj      : AllplanIFW.ViewWorldProjection,
                  prev_ele_list  : ModelEleList):
        """ add the arrow

        Args:
            dir_line:        direction line
            dir_line_length: direction line length
            view_proj:       view world projection
            prev_ele_list:   preview element list
        """

        prev_ele_list.append_geometry_3d(dir_line)

        view_line = view_proj.WorldToView(dir_line)

        arrow_length = abs(dir_line_length) / 3
        arrow_delta  = arrow_length / 2

        end_pnt = dir_line.EndPoint

        if AllplanGeo.CalcLength(view_line) > 1:
            view_line_length = AllplanGeo.CalcLength(view_line)

            loc_arrow_pnt1 = AllplanGeo.Point2D(view_line_length - arrow_length, arrow_delta)
            loc_arrow_pnt2 = AllplanGeo.Point2D(view_line_length - arrow_length, -arrow_delta)

            arrow_pnt1 = AllplanGeo.TransformCoord.PointGlobal(view_line, loc_arrow_pnt1)
            arrow_pnt2 = AllplanGeo.TransformCoord.PointGlobal(view_line, loc_arrow_pnt2)

            z_coord = end_pnt.Z

            world_arrow_pnt1 = view_proj.ViewToWorldBaseZ(AllplanGeo.Point2D(arrow_pnt1), z_coord)
            world_arrow_pnt2 = view_proj.ViewToWorldBaseZ(AllplanGeo.Point2D(arrow_pnt2), z_coord)

        elif end_pnt.Z > dir_line.StartPoint.Z:
            world_arrow_pnt1 = end_pnt - AllplanGeo.Point3D(arrow_delta, arrow_delta, arrow_length)
            world_arrow_pnt2 = end_pnt - AllplanGeo.Point3D(-arrow_delta, -arrow_delta, arrow_length)
        else:
            world_arrow_pnt1 = end_pnt + AllplanGeo.Point3D(arrow_delta, arrow_delta, arrow_length)
            world_arrow_pnt2 = end_pnt + AllplanGeo.Point3D(-arrow_delta, -arrow_delta, arrow_length)

        prev_ele_list.append_geometry_3d(AllplanGeo.Line3D(world_arrow_pnt1, end_pnt))

        prev_ele_list.append_geometry_3d(AllplanGeo.Line3D(world_arrow_pnt2, end_pnt))


    @staticmethod
    def is_coordinate_input_possible(handle_prop: HandleProperties,
                                     ref_pnt    : AllplanGeo.Point3D,
                                     handle_pnt : AllplanGeo.Point3D) -> bool:
        """ Check for an allowed coordinate input

        Args:
            handle_prop: Handle property
            ref_pnt:     Reference point
            handle_pnt:  Handle point

        Returns:
            coordinate input state
        """

        # pylint: disable=too-many-boolean-expressions

        handle_move_dir = handle_prop.handle_move_dir

        if handle_move_dir == HandleDirection.Z_DIR  and  abs(ref_pnt.Z - handle_pnt.Z) < 1. or  \
           handle_move_dir == HandleDirection.Y_DIR  and  abs(ref_pnt.Y - handle_pnt.Y) < 1. or  \
           handle_move_dir == HandleDirection.X_DIR  and  abs(ref_pnt.X - handle_pnt.X) < 1.:
            return False

        return True


    @staticmethod
    def create_orthogonal_handle(line2d    : AllplanGeo.Line2D,
                                 x_local   : float,
                                 y_local   : float,
                                 from_start: bool,
                                 z_coord   : float,
                                 name      : str) -> HandleProperties:
        """ Create an orthogonal handle on a 2D line

        Args:
            line2d:     2D-line
            x_local:    local x coordinate
            y_local:    local y coordinate
            from_start: x_local from start: True/False
            z_coord:    z coordinate of the handle point
            name:       name of the modified property

        Returns:
            created handle
        """

        x_coord = x_local

        if not from_start:
            x_coord = AllplanGeo.CalcLength(line2d) - x_local

        ref_pnt    = AllplanGeo.TransformCoord.PointGlobal(line2d,AllplanGeo.Point2D(x_coord, 0))
        handle_pnt = AllplanGeo.TransformCoord.PointGlobal(line2d,AllplanGeo.Point2D(x_coord, y_local))

        ref_pnt.Z    = z_coord
        handle_pnt.Z = z_coord

        return HandleProperties(name, handle_pnt, ref_pnt,
                                [HandleParameterData(name, HandleParameterType.POINT_DISTANCE)], HandleDirection.POINT_DIR)


    @staticmethod
    def transform_handles(handle_list: list[HandleProperties],
                          trans_mat  : AllplanGeo.Matrix3D):
        """ Transform the handles

        Args:
            handle_list: handle list
            trans_mat:   transformation matrix
        """

        for handle in handle_list:
            handle.transform(trans_mat)


    @staticmethod
    def set_input_point_for_isometric_projection(input_pnt     : AllplanGeo.Point3D,
                                                 handle_point  : AllplanGeo.Point3D,
                                                 iso_projection: AllplanIFW.eProjectionType):
        """ Set the handle input point for an isometric projection

        Args:
            input_pnt:      input point
            handle_point:   handle point
            iso_projection: isometric projection
        """

        match iso_projection:
            case AllplanIFW.eProjectionType.NORTH_VIEW | AllplanIFW.eProjectionType.SOUTH_VIEW:
                input_pnt.Y = handle_point.Y

            case AllplanIFW.eProjectionType.EAST_VIEW | AllplanIFW.eProjectionType.WEST_VIEW:
                input_pnt.X = handle_point.X

            case AllplanIFW.eProjectionType.GROUND_PLAN:
                input_pnt.Z = handle_point.Z

            case _:
                if input_pnt.Z == 0:
                    input_pnt.Z = handle_point.Z


    @staticmethod
    def get_property_values(build_ele_list: list[BuildingElement],
                            handle_prop   : HandleProperties) -> list[tuple[int, str, Any]]:
        """ Get the property values for properties of the handle

        Args:
            build_ele_list: list with the building elements
            handle_prop:    handle property

        Returns:
            list with the handle property values
        """

        handle_values = []

        index_list = handle_prop.build_ele_index_list

        for param_data in handle_prop.parameter_data:
            node_index = index_list[0] if index_list else 0

            build_ele = build_ele_list[node_index]

            name = BuildingElementParameterPropertyUtil.get_property_value_name(param_data.param_prop_name)

            if (prop := build_ele.get_property(name)) is None:
                continue

            value = prop.value

            handle_values.append((node_index, name, type(value)(value)))    # type: ignore

        return handle_values


    @staticmethod
    def get_curve_points(handle_prop: HandleProperties) -> list[tuple[GeometryTyping.POLY_CURVES, list[GeometryTyping.POINTS]]]:
        """ Get the curve points

        Args:
            handle_prop: handle property

        Returns:
            list with the original curve and the curve points
        """

        return [(geo_ele, [geo_ele.StartPoint, geo_ele.EndPoint] if isinstance(geo_ele, GeometryTyping.SINGLE_POINT_CURCES) else \
                           geo_ele.Points) \
                for param_data in handle_prop.parameter_data if (geo_ele := param_data.geo_element) is not None]  # type: ignore


    @staticmethod
    def __draw_distance_symbol(handle_pnt         : AllplanGeo.Point3D,
                               dist_vec           : AllplanGeo.Vector3D,
                               view_proj          : AllplanIFW.ViewWorldProjection,
                               dir_line_length    : float,
                               prev_ele_list      : ModelEleList,
                               system_angle       : float,
                               handle_move_dir    : HandleParameterType,
                               handle_trans_matrix: AllplanGeo.Matrix3D) -> bool:
        """ draw a distance symbol

        Args:
            handle_pnt:          Handle point
            dist_vec:            distance vector
            view_proj:           view world projection
            dir_line_length:     direction line length
            prev_ele_list:       preview element list
            system_angle:        system angle
            handle_move_dir:     handle move direction
            handle_trans_matrix: handle transformation matrix

        Returns:
            True if the symbol was drawn
        """

        if handle_move_dir == HandleParameterType.POINT:
            handle_trans_matrix = AllplanGeo.Matrix3D()

        has_symbol = False

        if handle_move_dir in (HandleParameterType.X_DISTANCE, HandleParameterType.POINT):
            if dist_vec.X < 0:
                dir_line_length *= -1

            cos_angle = math.cos(system_angle)
            sin_angle = math.sin(system_angle)

            dir_line = AllplanGeo.Line3D(handle_pnt, handle_pnt + AllplanGeo.Point3D(cos_angle * dir_line_length,
                                                                                     sin_angle * dir_line_length, 0) * handle_trans_matrix)

            HandleService.add_arrow(dir_line, dir_line_length, view_proj, prev_ele_list)

            has_symbol = True

        if handle_move_dir in (HandleParameterType.Y_DISTANCE, HandleParameterType.POINT):
            if dist_vec.Y < 0:
                dir_line_length *= -1

            cos_angle = math.cos(system_angle + math.pi / 2)
            sin_angle = math.sin(system_angle + math.pi / 2)

            dir_line = AllplanGeo.Line3D(handle_pnt, handle_pnt + AllplanGeo.Point3D(cos_angle * dir_line_length,
                                                                                     sin_angle * dir_line_length, 0) * handle_trans_matrix)

            HandleService.add_arrow(dir_line, dir_line_length, view_proj, prev_ele_list)

            has_symbol = True

        if handle_move_dir in (HandleParameterType.Z_DISTANCE, HandleParameterType.POINT):
            if dist_vec.Z < 0:
                dir_line_length *= -1

            dir_line = AllplanGeo.Line3D(handle_pnt, handle_pnt + AllplanGeo.Point3D(0, 0, dir_line_length) * handle_trans_matrix)

            HandleService.add_arrow(dir_line, dir_line_length, view_proj, prev_ele_list)

            has_symbol = True

        return has_symbol


    @staticmethod
    def __draw_angle_symbol(trans_mat      : AllplanGeo.Matrix3D,
                            handle_prop    : HandleProperties,
                            handle_pnt     : AllplanGeo.Point3D,
                            dir_line_length: float,
                            prev_ele_list  : ModelEleList):
        """ draw the angle symbol

        Args:
            trans_mat:       transformation matrix
            handle_prop:     handle property
            handle_pnt:      Handle point
            dir_line_length: direction line length
            prev_ele_list:   preview element list
        """

        rad = dir_line_length / 2

        x_arrow = rad / 2
        y_arrow = rad / 3

        arrow_pnt = AllplanGeo.Point3D(0, rad, 0)

        arrow_line1 = AllplanGeo.Line3D(arrow_pnt, arrow_pnt + AllplanGeo.Point3D(x_arrow, y_arrow * 0.6, 0))
        arrow_line2 = AllplanGeo.Line3D(arrow_pnt, arrow_pnt + AllplanGeo.Point3D(x_arrow, -y_arrow * 1.5, 0))

        if handle_prop.angle_placement:
            placement = AllplanGeo.AxisPlacement3D(handle_prop.angle_placement)
            placement.Origin = handle_prop.handle_point

            dir_arc = AllplanGeo.Arc3D(placement.GetOrigin() * trans_mat,
                                       placement.GetXDirection() * trans_mat,
                                       placement.GetZDirection() * trans_mat,
                                       rad, rad, -1.57, 3.14)

            arrow_line1 *= placement.GetTransformationMatrix()
            arrow_line2 *= placement.GetTransformationMatrix()
        else:
            dir_arc = AllplanGeo.Arc3D(handle_pnt, AllplanGeo.Vector3D(1000, 0, 0), AllplanGeo.Vector3D(0, 0, 1000),
                                            rad, rad, -1.57, 3.14,)

            arrow_line1 = AllplanGeo.Move(arrow_line1, AllplanGeo.Vector3D(handle_prop.handle_point))
            arrow_line2 = AllplanGeo.Move(arrow_line2, AllplanGeo.Vector3D(handle_prop.handle_point))

        arrow_line1 *= trans_mat
        arrow_line2 *= trans_mat

        prev_ele_list.append_geometry_3d(dir_arc)

        prev_ele_list.append_geometry_3d(arrow_line1)
        prev_ele_list.append_geometry_3d(arrow_line2)

```

</details>