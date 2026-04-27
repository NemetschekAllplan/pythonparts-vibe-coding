---
title: "ShapeGeometryPropertiesParameterUtil"
source: "PythonPartsFramework\ParameterUtils\Architecture\ShapeGeometryPropertiesParameterUtil.py"
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

> **Pfad:** `PythonPartsFramework\ParameterUtils\Architecture\ShapeGeometryPropertiesParameterUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `parameter`, `utility`

## Übersicht

implementation of the shape geometry parameter utilities

## Abhängigkeiten

- `BasePropertiesParameterUtil`
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
| `create_shape_geo_properties` | `self, shape_geo_props: AllplanArchEle.VerticalElementProperties, shape_polygon: AllplanGeo.Polygon2D` | `None` | create the shape geometry properties from the parameter values  Args:     shape_geo_props: shape geometry properties     shape_polygon:   shape polygon for the polygonal shape |
| `modify_shape_geo_properties` | `self, shape_geo_props: AllplanArchEle.VerticalElementProperties, shape_polygon: AllplanGeo.Polygon2D` | `None` | modify the shape geometry properties by the modified parameter values  Args:     shape_geo_props: shape geometry properties     shape_polygon:   shape polygon for the polygonal shape |
| `set_parameter_values` | `self, shape_geo_props: AllplanArchEle.VerticalElementProperties, name_postfix: str, shape_polygon: AllplanGeo.Polygon2D` | `None` | get the parameter values from the text properties  Args:     shape_geo_props: shape geometry properties     name_postfix:    post fix of the parameter names     shape_polygon:   shape polygon for the polygonal shape |
| `get_reference_point` | `self` | `AllplanGeo.Point2D` | get the reference point  Returns:     reference point+ |

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

from ..ProfileParameterUtil import ProfileParameterUtil
from ..BasePropertiesParameterUtil import BasePropertiesParameterUtil

class ShapeGeometryPropertiesParameterUtil(BasePropertiesParameterUtil):
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

        super().__init__(build_ele, name_postfix)

        profile_prop = build_ele.get_property(f"Profile{self.name_postfix}")

        self.profile_param_util = ProfileParameterUtil("" if profile_prop is None else profile_prop.value)


    def create_shape_geo_properties(self,
                                    shape_geo_props: AllplanArchEle.VerticalElementProperties,
                                    shape_polygon  : AllplanGeo.Polygon2D):
        """ create the shape geometry properties from the parameter values

        Args:
            shape_geo_props: shape geometry properties
            shape_polygon:   shape polygon for the polygonal shape
        """

        shape_geo_props.ShapeType = self.get_parameter_value("Shape")

        placing_angle = AllplanGeo.Angle.FromDeg(self.get_parameter_value("PlacingAngle"))

        shape_geo_props.Width           = 0
        shape_geo_props.Depth           = 0
        shape_geo_props.Radius          = 0
        shape_geo_props.CircleDivision  = 0
        shape_geo_props.ProfileFullName = ""
        shape_geo_props.ShapePolygon    = AllplanGeo.Polygon2D()

        match shape_geo_props.ShapeType:
            case AllplanArchEle.ShapeType.eRectangular:
                shape_geo_props.Width = self.get_parameter_value("Width")
                shape_geo_props.Depth = self.get_parameter_value("Depth")
                shape_geo_props.Angle = placing_angle

            case AllplanArchEle.ShapeType.eCircular:
                shape_geo_props.Radius         = self.get_parameter_value("Radius")
                shape_geo_props.CircleDivision = self.get_parameter_value("CircleDivision")
                shape_geo_props.Angle          = placing_angle

            case (AllplanArchEle.ShapeType.eRegularPolygonCircumscribed | AllplanArchEle.ShapeType.eRegularPolygonInscribed):
                shape_geo_props.Radius         = self.get_parameter_value("Radius")
                shape_geo_props.CircleDivision = self.get_parameter_value("NumberOfCorners")
                shape_geo_props.Angle          = placing_angle

            case AllplanArchEle.ShapeType.ePolygonal:
                shape_geo_props.ShapePolygon = shape_polygon

            case AllplanArchEle.ShapeType.eArbitrary:
                shape_geo_props.ProfileFullName = self.get_parameter_value("Profile")

                if shape_geo_props.ProfileFullName:
                    shape_geo_props.ShapePolygon = self.profile_param_util.get_polygon(shape_geo_props.ProfileFullName)
                else:
                    shape_geo_props.ShapePolygon = shape_polygon


    def modify_shape_geo_properties(self,
                                    shape_geo_props: AllplanArchEle.VerticalElementProperties,
                                    shape_polygon  : AllplanGeo.Polygon2D):
        """ modify the shape geometry properties by the modified parameter values

        Args:
            shape_geo_props: shape geometry properties
            shape_polygon:   shape polygon for the polygonal shape
        """

        shape_geo_props.ShapeType = self.get_modified_parameter_value("Shape", shape_geo_props.ShapeType)

        placing_angle = AllplanGeo.Angle.FromDeg(self.get_modified_parameter_value("PlacingAngle", shape_geo_props.Angle.Deg))

        match shape_geo_props.ShapeType:
            case AllplanArchEle.ShapeType.eRectangular:
                shape_geo_props.Width = self.get_modified_parameter_value("Width", shape_geo_props.Width)
                shape_geo_props.Depth = self.get_modified_parameter_value("Depth", shape_geo_props.Depth)
                shape_geo_props.Angle = placing_angle

            case AllplanArchEle.ShapeType.eCircular:
                shape_geo_props.Radius         = self.get_modified_parameter_value("Radius", shape_geo_props.Radius)
                shape_geo_props.CircleDivision = self.get_modified_parameter_value("CircleDivision", shape_geo_props.CircleDivision)
                shape_geo_props.Angle          = placing_angle

            case (AllplanArchEle.ShapeType.eRegularPolygonCircumscribed | AllplanArchEle.ShapeType.eRegularPolygonInscribed):
                shape_geo_props.Radius         = self.get_modified_parameter_value("Radius", shape_geo_props.Radius)
                shape_geo_props.CircleDivision = self.get_modified_parameter_value("NumberOfCorners", shape_geo_props.CircleDivision)
                shape_geo_props.Angle          = placing_angle

            case AllplanArchEle.ShapeType.ePolygonal:
                shape_geo_props.ShapePolygon = shape_polygon

            case AllplanArchEle.ShapeType.eArbitrary:
                shape_geo_props.ProfileFullName = self.get_modified_parameter_value("Profile", shape_geo_props.ProfileFullName)

                if shape_geo_props.ProfileFullName:
                    shape_geo_props.ShapePolygon = self.profile_param_util.get_polygon(shape_geo_props.ProfileFullName)
                else:
                    shape_geo_props.ShapePolygon = shape_polygon


    def set_parameter_values(self,
                             shape_geo_props: AllplanArchEle.VerticalElementProperties,
                             name_postfix   : str,
                             shape_polygon  : AllplanGeo.Polygon2D):
        """ get the parameter values from the text properties

        Args:
            shape_geo_props: shape geometry properties
            name_postfix:    post fix of the parameter names
            shape_polygon:   shape polygon for the polygonal shape
        """

        build_ele = self.build_ele

        build_ele.get_existing_property(f"Shape{name_postfix}").varied_value       = shape_geo_props.ShapeType
        build_ele.get_existing_property(f"RefPntIndex{name_postfix}").varied_value = AllplanPalette.RefPointPosition.eCenterCenter

        match shape_geo_props.ShapeType:
            case AllplanArchEle.ShapeType.eRectangular:
                build_ele.get_existing_property(f"Width{name_postfix}").varied_value        = shape_geo_props.Width
                build_ele.get_existing_property(f"Depth{name_postfix}").varied_value        = shape_geo_props.Depth
                build_ele.get_existing_property(f"PlacingAngle{name_postfix}").varied_value = shape_geo_props.Angle.Deg

            case AllplanArchEle.ShapeType.eCircular:
                build_ele.get_existing_property(f"Radius{name_postfix}").varied_value         = shape_geo_props.Radius
                build_ele.get_existing_property(f"CircleDivision{name_postfix}").varied_value = shape_geo_props.CircleDivision
                build_ele.get_existing_property(f"PlacingAngle{name_postfix}").varied_value   = shape_geo_props.Angle.Deg

            case (AllplanArchEle.ShapeType.eRegularPolygonCircumscribed | AllplanArchEle.ShapeType.eRegularPolygonInscribed):
                build_ele.get_existing_property(f"Radius{name_postfix}").varied_value          = shape_geo_props.Radius
                build_ele.get_existing_property(f"NumberOfCorners{name_postfix}").varied_value = shape_geo_props.CircleDivision
                build_ele.get_existing_property(f"PlacingAngle{name_postfix}").varied_value    = shape_geo_props.Angle.Deg

            case AllplanArchEle.ShapeType.ePolygonal:
                shape_polygon.Points = shape_geo_props.ShapePolygon.Points

            case AllplanArchEle.ShapeType.eArbitrary:
                build_ele.get_existing_property(f"Profile{name_postfix}").varied_value = shape_geo_props.ProfileFullName

                shape_polygon.Points = shape_geo_props.ShapePolygon.Points


    def get_reference_point(self) -> AllplanGeo.Point2D:
        """ get the reference point

        Returns:
            reference point+
        """

        placing_angle = AllplanGeo.Angle.FromDeg(self.get_parameter_value("PlacingAngle"))

        match self.get_parameter_value("Shape"):
            case AllplanArchEle.ShapeType.eRectangular:
                ref_dx = self.get_parameter_value("Width") / 2
                ref_dy = self.get_parameter_value("Depth") / 2


            case AllplanArchEle.ShapeType.eProfile:
                minmax, _ = AllplanGeo.CalcMinMax(self.profile_param_util.get_polygon(self.get_parameter_value("Profile")))

                ref_dx = minmax.GetSizeX() / 2
                ref_dy = minmax.GetSizeY() / 2

                placing_angle = AllplanGeo.Angle()

            case _:
                ref_dx = ref_dy = self.get_parameter_value("Radius")

        ref_pnt_index = self.get_parameter_value("RefPntIndex")

        ref_pnt = AllplanGeo.Point2D([-ref_dx, 0, ref_dx, -ref_dx, 0, ref_dx, -ref_dx, 0, ref_dx][ref_pnt_index - 1],
                                     [ref_dy, ref_dy, ref_dy, 0, 0, 0, -ref_dy, -ref_dy, -ref_dy][ref_pnt_index - 1])

        return AllplanGeo.Rotate(ref_pnt, placing_angle)

```

</details>