---
title: "ShapeGeometryPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\ShapeGeometryPropertiesParameterUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - parameter
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ShapeGeometryPropertiesParameterUtil

> **Pfad:** `PythonPartsFramework\ParameterUtils\ShapeGeometryPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `parameter`, `utility`

## Übersicht

implementation of the shape geometry parameter utilities

## Abhängigkeiten

- `BuildingElement`
- `NemAll_Python_ArchElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_Palette`
- `ProfileParameterUtil`

## Klassen

### `ShapeGeometryPropertiesParameterUtil`

implementation of the shape geometry parameter utilities
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, build_ele: BuildingElement, name_postfix: str` | `None` | initialize  Args:     build_ele:    building element with the parameter properties     name_postfix: postfix of the parameter names |
| `create_shape_geo_properties` | `self, build_ele: BuildingElement, shape_geo_props: AllplanArchEle.VerticalElementProperties, shape_polygon: AllplanGeo.Polygon2D` | `None` | create the shape geometry properties from the parameter values  Args:     build_ele:       building element with the parameter properties     shape_geo_props: shape geometry properties     shape_polygon:   shape polygon for the polygonal shape |
| `set_parameter_values` | `build_ele: BuildingElement, shape_geo_props: AllplanArchEle.VerticalElementProperties, name_postfix: str, shape_polygon: AllplanGeo.Polygon2D` | `None` | get the parameter values from the text properties  Args:     build_ele:       building element with the parameter properties     shape_geo_props: shape geometry properties     name_postfix:    post fix of the parameter names     shape_polygon:   shape polygon for the polygonal shape |
| `get_reference_point` | `self, build_ele: BuildingElement` | `AllplanGeo.Point2D` | get the reference point  Args:     build_ele: building element with the parameter properties  Returns:     reference point+ |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the shape geometry parameter utilities
"""

import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Palette as AllplanPalette

from BuildingElement import BuildingElement

from .ProfileParameterUtil import ProfileParameterUtil

class ShapeGeometryPropertiesParameterUtil():
    """ implementation of the shape geometry parameter utilities
    """

    def __init__(self,
                 build_ele   : BuildingElement,
                 name_postfix: str):
        """ initialize

        Args:
            build_ele:    building element with the parameter properties
            name_postfix: postfix of the parameter names
        """

        self.name_postfix = name_postfix

        profile_prop = build_ele.get_property(f"Profile{self.name_postfix}")

        self.profile_param_util = ProfileParameterUtil("" if profile_prop is None else profile_prop.value)


    def create_shape_geo_properties(self,
                                    build_ele      : BuildingElement,
                                    shape_geo_props: AllplanArchEle.VerticalElementProperties,
                                    shape_polygon  : AllplanGeo.Polygon2D):
        """ create the shape geometry properties from the parameter values

        Args:
            build_ele:       building element with the parameter properties
            shape_geo_props: shape geometry properties
            shape_polygon:   shape polygon for the polygonal shape
        """

        name_postfix = self.name_postfix

        shape_geo_props.ShapeType = build_ele.get_existing_property(f"Shape{name_postfix}").value

        placing_angle = AllplanGeo.Angle.FromDeg(build_ele.get_existing_property(f"PlacingAngle{name_postfix}").value)

        shape_geo_props.Width           = 0
        shape_geo_props.Depth           = 0
        shape_geo_props.Radius          = 0
        shape_geo_props.CircleDivision  = 0
        shape_geo_props.ProfileFullName = ""
        shape_geo_props.ShapePolygon    = AllplanGeo.Polygon2D()

        match shape_geo_props.ShapeType:
            case AllplanArchEle.ShapeType.eRectangular:
                shape_geo_props.Width = build_ele.get_existing_property(f"Width{name_postfix}").value
                shape_geo_props.Depth = build_ele.get_existing_property(f"Depth{name_postfix}").value
                shape_geo_props.Angle = placing_angle

            case AllplanArchEle.ShapeType.eCircular:
                shape_geo_props.Radius         = build_ele.get_existing_property(f"Radius{name_postfix}").value
                shape_geo_props.CircleDivision = build_ele.get_existing_property(f"CircleDivision{name_postfix}").value
                shape_geo_props.Angle          = placing_angle

            case (AllplanArchEle.ShapeType.eRegularPolygonCircumscribed | AllplanArchEle.ShapeType.eRegularPolygonInscribed):
                shape_geo_props.Radius         = build_ele.get_existing_property(f"Radius{name_postfix}").value
                shape_geo_props.CircleDivision = build_ele.get_existing_property(f"NumberOfCorners{name_postfix}").value
                shape_geo_props.Angle          = placing_angle

            case AllplanArchEle.ShapeType.ePolygonal:
                shape_geo_props.ShapePolygon = shape_polygon

            case AllplanArchEle.ShapeType.eArbitrary:
                shape_geo_props.ProfileFullName = build_ele.get_existing_property(f"Profile{name_postfix}").value

                if shape_geo_props.ProfileFullName:
                    shape_geo_props.ShapePolygon = self.profile_param_util.get_polygon(shape_geo_props.ProfileFullName)
                else:
                    shape_geo_props.ShapePolygon = shape_polygon


    @staticmethod
    def set_parameter_values(build_ele      : BuildingElement,
                             shape_geo_props: AllplanArchEle.VerticalElementProperties,
                             name_postfix   : str,
                             shape_polygon  : AllplanGeo.Polygon2D):
        """ get the parameter values from the text properties

        Args:
            build_ele:       building element with the parameter properties
            shape_geo_props: shape geometry properties
            name_postfix:    post fix of the parameter names
            shape_polygon:   shape polygon for the polygonal shape
        """

        build_ele.get_existing_property(f"Shape{name_postfix}").value       = shape_geo_props.ShapeType
        build_ele.get_existing_property(f"RefPntIndex{name_postfix}").value = AllplanPalette.RefPointPosition.eCenterCenter

        match shape_geo_props.ShapeType:
            case AllplanArchEle.ShapeType.eRectangular:
                build_ele.get_existing_property(f"Width{name_postfix}").value        = shape_geo_props.Width
                build_ele.get_existing_property(f"Depth{name_postfix}").value        = shape_geo_props.Depth
                build_ele.get_existing_property(f"PlacingAngle{name_postfix}").value = shape_geo_props.Angle.Deg

            case AllplanArchEle.ShapeType.eCircular:
                build_ele.get_existing_property(f"Radius{name_postfix}").value         = shape_geo_props.Radius
                build_ele.get_existing_property(f"CircleDivision{name_postfix}").value = shape_geo_props.CircleDivision
                build_ele.get_existing_property(f"PlacingAngle{name_postfix}").value   = shape_geo_props.Angle.Deg

            case (AllplanArchEle.ShapeType.eRegularPolygonCircumscribed | AllplanArchEle.ShapeType.eRegularPolygonInscribed):
                build_ele.get_existing_property(f"Radius{name_postfix}").value          = shape_geo_props.Radius
                build_ele.get_existing_property(f"NumberOfCorners{name_postfix}").value = shape_geo_props.CircleDivision
                build_ele.get_existing_property(f"PlacingAngle{name_postfix}").value    = shape_geo_props.Angle.Deg

            case AllplanArchEle.ShapeType.ePolygonal:
                shape_polygon.Points = shape_geo_props.ShapePolygon.Points

            case AllplanArchEle.ShapeType.eArbitrary:
                build_ele.get_existing_property(f"Profile{name_postfix}").value = shape_geo_props.ProfileFullName

                shape_polygon.Points = shape_geo_props.ShapePolygon.Points


    def get_reference_point(self,
                            build_ele: BuildingElement) -> AllplanGeo.Point2D:
        """ get the reference point

        Args:
            build_ele: building element with the parameter properties

        Returns:
            reference point+
        """

        name_postfix = self.name_postfix

        placing_angle = AllplanGeo.Angle.FromDeg(build_ele.get_existing_property(f"PlacingAngle{name_postfix}").value)

        match build_ele.get_existing_property(f"Shape{name_postfix}").value:
            case AllplanArchEle.ShapeType.eRectangular:
                ref_dx = build_ele.get_existing_property(f"Width{name_postfix}").value / 2
                ref_dy = build_ele.get_existing_property(f"Depth{name_postfix}").value / 2


            case AllplanArchEle.ShapeType.eProfile:
                minmax, _ = AllplanGeo.CalcMinMax(self.profile_param_util.get_polygon(
                                                            build_ele.get_existing_property(f"Profile{name_postfix}").value))

                ref_dx = minmax.GetSizeX() / 2
                ref_dy = minmax.GetSizeY() / 2

                placing_angle = AllplanGeo.Angle()

            case _:
                ref_dx = ref_dy = build_ele.get_existing_property(f"Radius{name_postfix}").value


        #----------------- get the reference point by the reference point index

        ref_pnt_index = build_ele.get_existing_property(f"RefPntIndex{name_postfix}").value

        ref_pnt = AllplanGeo.Point2D([-ref_dx, 0, ref_dx, -ref_dx, 0, ref_dx, -ref_dx, 0, ref_dx][ref_pnt_index - 1],
                                     [ref_dy, ref_dy, ref_dy, 0, 0, 0, -ref_dy, -ref_dy, -ref_dy][ref_pnt_index - 1])

        return AllplanGeo.Rotate(ref_pnt, placing_angle)

```

</details>