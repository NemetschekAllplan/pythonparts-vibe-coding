---
title: "CurveHandlesCreator"
source: "PythonPartsFramework\Utils\HandleCreator\CurveHandlesCreator.py"
type: "class"
category: "02_API_Referenz"
tags:
  - handle
  - utility
related:
  -
last_updated: "2026-02-20"
---


# CurveHandlesCreator

> **Pfad:** `PythonPartsFramework\Utils\HandleCreator\CurveHandlesCreator.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `handle`, `utility`

## Übersicht

implementation of the curve handles creator

## Abhängigkeiten

- `HandleCreator`
- `HandleDirection`
- `HandleParameterData`
- `HandleParameterType`
- `HandleProperties`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `PolyPointsDistanceType`
- `TypeCollections.GeometryTyping`
- `TypeCollections.HandleList`
- `math`
- `string`

## Klassen

### `CurveHandlesCreator`

implementation of the curve handles creator
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `poly_curve` | `handle_list: HandleList, name: str, poly_curve: POLY_CURVES, add_split_points: bool, info_text: str='', info_text_template: Template=Template(''), index_offset: int=0, delete_point: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter(), has_input_field: bool=True, show_input_field_always: bool=False, input_field_above: bool=True, poly_point_distance_fields: PolyPointsDistanceType=PolyPointsDistanceType.NONE` | `None` | create point move handles for a poly points curve  Args:     handle_list:                handle list     name:                       handle parameter name     poly_curve:                 poly points curve     add_split_points:           add split points     info_text:                  info text     info_text_template:         info text template     index_offset:               index offset for the info text     delete_point:               enable delete point state     owner_element:              owner element of the handle (in element modification mode)     has_input_field:            has input field state     show_input_field_always:    show the input field always state     input_field_above:          input field above the dimension line state     poly_point_distance_fields: distance fields for the poly points |
| `__add_poly_point_distances` | `handle_list: HandleList, name: str, poly_curve: POLY_CURVES, info_text: str, owner_element: AllplanEleAdapter.BaseElementAdapter, show_input_field_always: bool, input_field_above: bool, poly_point_distance_fields: PolyPointsDistanceType, index: int, start_pnt: AllplanGeo.Point3D, end_pnt: AllplanGeo.Point3D` | `None` | function description  Args:     handle_list:                handle list     name:                       handle parameter name     poly_curve:                 poly points curve     info_text:                  info text     owner_element:              owner element of the handle (in element modification mode)     show_input_field_always:    show the input field always state     input_field_above:          input field above the dimension line state     poly_point_distance_fields: distance fields for the poly points     index:                      index of the point in the curve     start_pnt:                  description     end_pnt:                    description |
| `vector` | `handle_list: HandleList, start_point: AllplanGeo.Point2D | AllplanGeo.Point3D, vector: AllplanGeo.Vector2D | AllplanGeo.Vector3D, name: str, info_text: str='', owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter()` | `None` | create point move handles for a vector  Args:     handle_list:   handle list     start_point:   start point     vector:        vector     name:          handle parameter name     info_text:     info text     owner_element: owner element of the handle (in element modification mode) |
| `line` | `handle_list: HandleList, name: str, line: AllplanGeo.Line3D | AllplanGeo.Line2D, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter()` | `None` | create x/y/z point distance handles for a line defined by two points  Args:     handle_list:             handle list     name:                    handle parameter name     line:                    line     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode) |
| `__add_curve_point` | `handle_list: HandleList, curve_point: POINTS, geo_element: CURVES, info_text: str, index: int, delete_point: bool, owner_element: AllplanEleAdapter.BaseElementAdapter, handle_dir: HandleDirection, handle_plane: AllplanGeo.Plane3D | None` | `None` | add a point move handle for a curve point  Args:     handle_list:   handle list     curve_point:   curve point     geo_element:   geometry element     info_text:     info text     index:         index of the point in the curve     delete_point:  enable delete point state     owner_element: owner element of the handle (in element modification mode)     handle_dir:    handle direction     handle_plane:  handle direction |
| `arc_2d` | `handle_list: HandleList, name: str, arc: AllplanGeo.Arc2D, info_text: str='', show_input_field_always: bool=False, owner_element: AllplanEleAdapter.BaseElementAdapter=AllplanEleAdapter.BaseElementAdapter()` | `None` | create arc handles  Args:     handle_list:             handle list     name:                    handle parameter name     arc:                     arc 2D     info_text:               info text     show_input_field_always: show the input field always state     owner_element:           owner element of the handle (in element modification mode) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the curve handles creator
"""

# pylint: disable=too-many-arguments

from string import Template

import math

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_IFW_Input as AllplanIFW

from HandleDirection import HandleDirection
from HandleParameterData import HandleParameterData
from HandleParameterType import HandleParameterType
from HandleProperties import HandleProperties

from TypeCollections.GeometryTyping import POLY_CURVES, POLY_CURVES_3D, CURVES, POINTS
from TypeCollections.HandleList import HandleList

from .HandleCreator import HandleCreator
from .PolyPointsDistanceType import PolyPointsDistanceType


class CurveHandlesCreator():
    """ implementation of the curve handles creator
    """

    @staticmethod
    def poly_curve(handle_list               : HandleList,
                   name                      : str,
                   poly_curve                : POLY_CURVES,
                   add_split_points          : bool,
                   info_text                 : str                                  = "",
                   info_text_template        : Template                             = Template(""),
                   index_offset              : int                                  = 0,
                   delete_point              : bool                                 = False,
                   owner_element             : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter(),
                   has_input_field           : bool                                 = True,
                   show_input_field_always   : bool                                 = False,
                   input_field_above         : bool                                 = True,
                   poly_point_distance_fields: PolyPointsDistanceType               = PolyPointsDistanceType.NONE):
        """ create point move handles for a poly points curve

        Args:
            handle_list:                handle list
            name:                       handle parameter name
            poly_curve:                 poly points curve
            add_split_points:           add split points
            info_text:                  info text
            info_text_template:         info text template
            index_offset:               index offset for the info text
            delete_point:               enable delete point state
            owner_element:              owner element of the handle (in element modification mode)
            has_input_field:            has input field state
            show_input_field_always:    show the input field always state
            input_field_above:          input field above the dimension line state
            poly_point_distance_fields: distance fields for the poly points
        """

        if poly_curve is None:
            return

        curve_points = poly_curve.Points

        if not (points := poly_curve.Points):
            return

        if points[0] == points[-1]:     # type: ignore
            points = points[:-1]


        #----------------- exclude the "connection" segments for the holes

        ret_segments = set[int]()

        for index in range(4, len(curve_points) - 2):
            start_pnt = curve_points[index]
            end_pnt   = curve_points[index + 1]

            for loop_index in range(index + 1, len(curve_points) - 1):
                loop_start_pnt = curve_points[loop_index + 1]
                loop_end_pnt   = curve_points[loop_index]

                if start_pnt == loop_start_pnt and end_pnt == loop_end_pnt:     # type: ignore
                    ret_segments.add(index)
                    ret_segments.add(loop_index)
                    break


        #----------------- special data for 3D polygon

        handle_dir   = HandleDirection.PLANE_DIR if isinstance(poly_curve, AllplanGeo.Polygon3D) else HandleDirection.XY_DIR
        handle_plane = poly_curve.GetPlane()[1]  if isinstance(poly_curve, AllplanGeo.Polygon3D) else None


        #----------------- create the handles

        for index, point in enumerate(points):
            if index == len(curve_points) - 1:
                continue

            if info_text_template:
                info_text = info_text_template.substitute(index = index + index_offset)

            CurveHandlesCreator.__add_curve_point(handle_list, point, poly_curve, info_text, index, delete_point,
                                                  owner_element, handle_dir, handle_plane)

            start_pnt = AllplanGeo.Point3D(curve_points[index])
            end_pnt   = AllplanGeo.Point3D(curve_points[index + 1])

            if add_split_points and index < len(curve_points) - 1 and index not in ret_segments:
                split_pnt = (start_pnt + end_pnt) / 2

                handle_list.append(HandleProperties("", split_pnt, split_pnt,
                                                    [HandleParameterData("", HandleParameterType.CURVE_SPLIT_POINT, False,
                                                                         list_index  = index + 1,
                                                                         geo_element = poly_curve)],
                                                    handle_dir,
                                                    plane         = handle_plane,
                                                    info_text     = info_text,
                                                    owner_element = owner_element))

                handle_list[-1].handle_type  = AllplanIFW.ElementHandleType.HANDLE_SQUARE_BLUE
                handle_list[-1].handle_angle = AllplanGeo.Vector2D(start_pnt.To2D, end_pnt.To2D).GetAngle() + AllplanGeo.Angle(math.pi / 4)


            #----------------- create the distance input controls

            if has_input_field and index < len(points) - 1:
                CurveHandlesCreator.__add_poly_point_distances(handle_list, name, poly_curve, info_text, owner_element,
                                                               show_input_field_always, input_field_above, poly_point_distance_fields,
                                                               index, start_pnt, end_pnt)


    @staticmethod
    def __add_poly_point_distances(handle_list               : HandleList,
                                   name                      : str,
                                   poly_curve                : POLY_CURVES,
                                   info_text                 : str,
                                   owner_element             : AllplanEleAdapter.BaseElementAdapter,
                                   show_input_field_always   : bool,
                                   input_field_above         : bool,
                                   poly_point_distance_fields: PolyPointsDistanceType,
                                   index                     : int,
                                   start_pnt                 : AllplanGeo.Point3D,
                                   end_pnt                   : AllplanGeo.Point3D):
        """ function description

        Args:
            handle_list:                handle list
            name:                       handle parameter name
            poly_curve:                 poly points curve
            info_text:                  info text
            owner_element:              owner element of the handle (in element modification mode)
            show_input_field_always:    show the input field always state
            input_field_above:          input field above the dimension line state
            poly_point_distance_fields: distance fields for the poly points
            index:                      index of the point in the curve
            start_pnt:                  description
            end_pnt:                    description
        """

        handle_param = list[HandleParameterData]()

        if poly_point_distance_fields & PolyPointsDistanceType.DELTA_X:
            handle_param.append(HandleParameterData(f"{name}._SegmentDeltaX[{index}]", HandleParameterType.X_POINT_DISTANCE,
                                                        show_input_field_always = show_input_field_always,
                                                        input_field_above       = input_field_above,
                                                        geo_element             = poly_curve))

        if poly_point_distance_fields & PolyPointsDistanceType.DELTA_Y:
            handle_param.append(HandleParameterData(f"{name}._SegmentDeltaY[{index}]", HandleParameterType.Y_POINT_DISTANCE,
                                                        show_input_field_always = show_input_field_always,
                                                        input_field_above       = input_field_above,
                                                        geo_element             = poly_curve))

        if poly_point_distance_fields & PolyPointsDistanceType.DELTA_Z and isinstance(poly_curve, POLY_CURVES_3D):
            handle_param.append(HandleParameterData(f"{name}._SegmentDeltaZ[{index}]", HandleParameterType.Z_POINT_DISTANCE,
                                                        show_input_field_always = show_input_field_always,
                                                        input_field_above       = input_field_above,
                                                        geo_element             = poly_curve))

        if poly_point_distance_fields & PolyPointsDistanceType.LENGTH:
            handle_param.append(HandleParameterData(f"{name}._SegmentLength[{index}]",
                                                        HandleParameterType.LENGTH_POINT_DISTANCE,
                                                        show_input_field_always = show_input_field_always,
                                                        input_field_above       = input_field_above,
                                                        geo_element             = poly_curve))

        handle_list.append(HandleProperties(f"{name}.Length[{index}]",  end_pnt,  start_pnt, handle_param,
                                                HandleDirection.XYZ_DIR,
                                                abs_value     = False,
                                                show_handles  = False,
                                                info_text     = info_text,
                                                owner_element = owner_element))



    @staticmethod
    def vector(handle_list  : HandleList,
               start_point  : (AllplanGeo.Point2D | AllplanGeo.Point3D),
               vector       : (AllplanGeo.Vector2D | AllplanGeo.Vector3D),
               name         : str,
               info_text    : str                                  = "",
               owner_element: AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()):
        """ create point move handles for a vector

        Args:
            handle_list:   handle list
            start_point:   start point
            vector:        vector
            name:          handle parameter name
            info_text:     info text
            owner_element: owner element of the handle (in element modification mode)
        """

        if isinstance(vector, AllplanGeo.Vector2D):
            handle_list.append(HandleProperties(name, AllplanGeo.Point3D(start_point) + vector.To3D, AllplanGeo.Point3D(start_point),
                                                [HandleParameterData(f"{name}.X",  HandleParameterType.X_DISTANCE,  True),
                                                 HandleParameterData(f"{name}.Y",  HandleParameterType.Y_DISTANCE,  True)],
                                                HandleDirection.XY_DIR, False,
                                                info_text     = info_text,
                                                owner_element = owner_element))
        else:
            handle_list.append(HandleProperties(name, AllplanGeo.Point3D(start_point) + vector, AllplanGeo.Point3D(start_point),
                                                [HandleParameterData(f"{name}.X",  HandleParameterType.X_DISTANCE,  True),
                                                 HandleParameterData(f"{name}.Y",  HandleParameterType.Y_DISTANCE,  True),
                                                 HandleParameterData(f"{name}.Z",  HandleParameterType.Z_DISTANCE,  True)],
                                                HandleDirection.XYZ_DIR, False,
                                                info_text     = info_text,
                                                owner_element = owner_element))


    @staticmethod
    def line(handle_list            : HandleList,
             name                   : str,
             line                   : (AllplanGeo.Line3D | AllplanGeo.Line2D),
             info_text              : str                                  = "",
             show_input_field_always: bool                                 = False,
             owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()):
        """ create x/y/z point distance handles for a line defined by two points

        Args:
            handle_list:             handle list
            name:                    handle parameter name
            line:                    line
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
        """

        start_point_3d = AllplanGeo.Point3D(line.StartPoint)
        end_point_3d   = AllplanGeo.Point3D(line.EndPoint)


        #----------------- create the point move handles

        CurveHandlesCreator.__add_curve_point(handle_list, start_point_3d, line, info_text, 0, False, owner_element,
                                              HandleDirection.XYZ_DIR, None)
        CurveHandlesCreator.__add_curve_point(handle_list, end_point_3d, line, info_text, 1, False, owner_element,
                                              HandleDirection.XYZ_DIR, None)


        #----------------- create the distance input controls

        dist_vec = AllplanGeo.Vector3D(start_point_3d, end_point_3d)

        x_distance_factor = 1 if dist_vec.X == 0 else math.copysign(1, dist_vec.X)
        y_distance_factor = 1 if dist_vec.Y == 0 else math.copysign(1, dist_vec.Y)
        z_distance_factor = 1 if dist_vec.Z == 0 else math.copysign(1, dist_vec.Z)

        x_above = start_point_3d.Y < end_point_3d.Y and start_point_3d.X < end_point_3d.X or \
                  start_point_3d.Y > end_point_3d.Y and start_point_3d.X > end_point_3d.X

        y_above = start_point_3d.X > end_point_3d.X and start_point_3d.Y < end_point_3d.Y or \
                  start_point_3d.X < end_point_3d.X and start_point_3d.Y > end_point_3d.Y

        handle_param = [HandleParameterData(f"{name}._Length",  HandleParameterType.LENGTH_POINT_DISTANCE,
                                            show_input_field_always = show_input_field_always,
                                            geo_element             = line),
                        HandleParameterData(f"{name}._X",  HandleParameterType.X_POINT_DISTANCE,
                                            distance_factor         = x_distance_factor,
                                            show_input_field_always = show_input_field_always,
                                            input_field_above       = x_above,
                                            geo_element             = line),
                        HandleParameterData(f"{name}._Y",  HandleParameterType.Y_POINT_DISTANCE,
                                            distance_factor         = y_distance_factor,
                                            show_input_field_always = show_input_field_always,
                                            input_field_above       = y_above,
                                            geo_element             = line)]

        if isinstance(start_point_3d, AllplanGeo.Point3D) and isinstance(end_point_3d, AllplanGeo.Point3D):
            handle_param.append(HandleParameterData(f"{name}.Z",  HandleParameterType.Z_POINT_DISTANCE,
                                                    distance_factor         = z_distance_factor,
                                                    show_input_field_always = show_input_field_always,
                                                    geo_element             = line))

        handle_list.append(HandleProperties(name, end_point_3d, start_point_3d, handle_param, HandleDirection.XYZ_DIR,
                                            abs_value     = False,
                                            show_handles  = False,
                                            info_text     = info_text,
                                            owner_element = owner_element))

    @staticmethod
    def __add_curve_point(handle_list  : HandleList,
                          curve_point  : POINTS,
                          geo_element  : CURVES,
                          info_text    : str,
                          index        : int,
                          delete_point : bool,
                          owner_element: AllplanEleAdapter.BaseElementAdapter,
                          handle_dir   : HandleDirection,
                          handle_plane : (AllplanGeo.Plane3D | None)):
        """ add a point move handle for a curve point

        Args:
            handle_list:   handle list
            curve_point:   curve point
            geo_element:   geometry element
            info_text:     info text
            index:         index of the point in the curve
            delete_point:  enable delete point state
            owner_element: owner element of the handle (in element modification mode)
            handle_dir:    handle direction
            handle_plane:  handle direction
        """

        handle_list.append(HandleProperties("", AllplanGeo.Point3D(curve_point), AllplanGeo.Point3D(curve_point),
                                            [HandleParameterData("", HandleParameterType.CURVE_POINT, False,
                                                                 list_index       = index,
                                                                 delete_list_item = delete_point,
                                                                 geo_element      = geo_element)],
                                            handle_dir,
                                            plane         = handle_plane,
                                            info_text     = info_text,
                                            owner_element = owner_element))


    @staticmethod
    def arc_2d(handle_list            : HandleList,
               name                   : str,
               arc                    : AllplanGeo.Arc2D,
               info_text              : str                                  = "",
               show_input_field_always: bool                                 = False,
               owner_element          : AllplanEleAdapter.BaseElementAdapter = AllplanEleAdapter.BaseElementAdapter()):
        """ create arc handles

        Args:
            handle_list:             handle list
            name:                    handle parameter name
            arc:                     arc 2D
            info_text:               info text
            show_input_field_always: show the input field always state
            owner_element:           owner element of the handle (in element modification mode)
        """

        radius     = arc.MinorRadius
        center_pnt = arc.Center.To3D

        angle_placement = AllplanGeo.AxisPlacement3D(center_pnt, AllplanGeo.Vector3D(1000, 0, 0),
                                                     AllplanGeo.Vector3D(0, 0, 1000))

        start_pnt = center_pnt + AllplanGeo.Point3D(radius * math.cos(arc.StartAngle), radius * math.sin(arc.StartAngle), 0)

        HandleCreator.angle(handle_list, f"{name}.StartAngle", start_pnt, center_pnt,
                            angle_placement, center_pnt, info_text ="Start angle")

        end_pnt = center_pnt + AllplanGeo.Point3D(radius * math.cos(arc.EndAngle), radius * math.sin(arc.EndAngle), 0)

        HandleCreator.angle(handle_list, f"{name}.EndAngle", end_pnt, center_pnt,
                            angle_placement, center_pnt, info_text = "End angle")

        handle_list.append(HandleProperties(name, start_pnt, end_pnt,
                                            [HandleParameterData(f"{name}.ArcLength", HandleParameterType.LENGTH_POINT_DISTANCE, True,
                                                                 input_field_above       = False,
                                                                 show_input_field_always = show_input_field_always,
                                                                 geo_element             = arc)],
                                            HandleDirection.XY_DIR,
                                            show_handles    = False,
                                            angle_placement = angle_placement,
                                            info_text       = info_text,
                                            center_point    = center_pnt,
                                            owner_element   = owner_element))

```

</details>