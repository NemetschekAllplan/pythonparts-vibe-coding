---
title: "FoilElementUtil"
source: "PythonPartsFramework\SmartPartUtils\FoilElementUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# FoilElementUtil

> **Pfad:** `PythonPartsFramework\SmartPartUtils\FoilElementUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the foil element utility 

## Abhängigkeiten

- `BuildingElement`
- `BuildingElementAttributeList`
- `DocumentManager`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `PythonPartUtil`
- `PythonPartViewData`
- `SmartPartUtils.TransformationStack2D`
- `SmartPartUtils.TransformationStack3D`
- `Utils.Text3DUtil`
- `Utils.TextReferencePointPosition`
- `typing`

## Klassen

### `FoilElementUtil`

implementation of the foil element utility 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, trans_stack_2d: TransformationStack2D, trans_stack_3d: TransformationStack3D, length_unit: int` | `None` | initialize  |
| `add_foil` | `self, name: str, visible_in_2d: bool=True, visible_in_3d: bool=True, start_scale: float=0, end_scale: float=9999, ref_pnt1_x: float=0, ref_pnt1_y: float=0, ref_pnt1_z: float=0, ref_pnt2_x: float=0, ref_pnt2_y: float=0, ref_pnt2_z: float=0, visibility_layer_a: bool=True, visibility_layer_b: bool=True, visibility_layer_c: bool=True, scale_x: int=1, scale_y: int=2, scale_z: int=3` | `None` | add a foil  |
| `set_use_default_3d_foil` | `self, state: bool` | `None` | set the 2D/3D mode for the default foil  |
| `set_foil` | `self, name: str` | `None` | set the foil for the next elements  |
| `set_material` | `self, material_name: str` | `None` | set the material surface  |
| `add_rectangle2d` | `self, com_prop: AllplanBaseEle.CommonProperties, x_left: float, y_bottom: float, x_right: float, y_top: float` | `None` | add a 2d rectangle  |
| `add_line2d` | `self, com_prop: AllplanBaseEle.CommonProperties, x_start: float, y_start: float, x_end: float, y_end: float` | `None` | add a 2d line  |
| `add_arc2d` | `self, com_prop: AllplanBaseEle.CommonProperties, x_center: float, y_center: float, radius: float, angle_start=0.0, angle_end=360.0` | `None` | add a 2d arc  |
| `add_arc3d` | `self, com_prop: AllplanBaseEle.CommonProperties, x_center: float, y_center: float, radius: float, angle_start=0.0, angle_end=360.0` | `None` | add a 3d arc  |
| `add_circle2d` | `self, com_prop: AllplanBaseEle.CommonProperties, x_center: float, y_center: float, radius: float` | `None` | add a 2d circle  |
| `add_circle3d` | `self, com_prop: AllplanBaseEle.CommonProperties, x_center: float, y_center: float, radius: float` | `None` | add a 3d circle  |
| `add_poly_point_element_2d` | `self, com_prop: AllplanBaseEle.CommonProperties, poly_point_element: Any` | `None` | add a 2D element with poly points  |
| `add_text2d` | `self, com_prop: AllplanBaseEle.CommonProperties, text_prop: AllplanBasisEle.TextProperties, x_ref_pnt: float, y_ref_pnt: float, text: str` | `None` | add a 2d text  |
| `add_text3d` | `self, com_prop: AllplanBaseEle.CommonProperties, text_prop: AllplanBasisEle.TextProperties, _text_thickness_z: float, _height_flag: int, text: str` | `None` | add a 3d text  |
| `add_line3d` | `self, com_prop: AllplanBaseEle.CommonProperties, x_start: float, y_start: float, z_start: float, x_end: float, y_end: float, z_end: float` | `None` | add a 2d line  |
| `add_box` | `self, com_prop: AllplanBaseEle.CommonProperties, length: float, width: float, height: float` | `None` | add a box  |
| `add_cylinder` | `self, com_prop: AllplanBaseEle.CommonProperties, height: float, radius: float` | `None` | add a cylinder  |
| `add_prism` | `self, com_prop: AllplanBaseEle.CommonProperties, height: float, polygon: AllplanGeo.Polygon2D` | `None` | add a prism  |
| `add_geometry` | `self, com_prop: AllplanBaseEle.CommonProperties, geo_object: Any` | `None` | add a geometry  |
| `__add_geometry_3d` | `self, com_prop: AllplanBaseEle.CommonProperties, geo_object: Any` | `None` | add a 3D geometry object  Args:     com_prop:   common properties     geo_object: geometry object |
| `create_pythonpart` | `self, build_ele: BuildingElement, build_ele_attr_list: BuildingElementAttributeList` | `List[Any]` | create the PythonPart  |
| `get_elements` | `self` | `List[Any]` | get the created element  Returns:     elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the foil element utility """

# pylint: disable=too-many-arguments

from typing import Dict, Tuple, List, Any

import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_Geometry as AllplanGeo

from BuildingElement import BuildingElement
from BuildingElementAttributeList import BuildingElementAttributeList
from DocumentManager import DocumentManager
from PythonPartUtil import PythonPartUtil
from PythonPartViewData import PythonPartViewData

from SmartPartUtils.TransformationStack2D import TransformationStack2D
from SmartPartUtils.TransformationStack3D import TransformationStack3D

from Utils.Text3DUtil import Text3DUtil
from Utils.TextReferencePointPosition import TextReferencePointPosition

class FoilElementUtil():
    """ implementation of the foil element utility """


    def __init__(self,
                 trans_stack_2d: TransformationStack2D,
                 trans_stack_3d: TransformationStack3D,
                 length_unit   : int):
        """ initialize """

        self.trans_stack_2d =  trans_stack_2d
        self.trans_stack_3d =  trans_stack_3d

        self.view_model_ele_list         :Dict[str, Tuple[PythonPartViewData, List]] = {}
        self.view_model_ele_list["0_2D"] = (PythonPartViewData(True, False), [])
        self.view_model_ele_list["0_3D"] = (PythonPartViewData(False, True), [])
        self.model_ele_list              = self.view_model_ele_list["0_2D"][1]
        self.length_fac                  = [1., 10., 100., 1000.][length_unit]
        self.use_default_3d_foil         = False
        self.material_name               = ""


    def add_foil(self,
                 name              : str,
                 visible_in_2d     : bool = True,
                 visible_in_3d     : bool = True,
                 start_scale       : float = 0,
                 end_scale         : float = 9999,
                 ref_pnt1_x        : float = 0,
                 ref_pnt1_y        : float = 0,
                 ref_pnt1_z        : float = 0,
                 ref_pnt2_x        : float = 0,
                 ref_pnt2_y        : float = 0,
                 ref_pnt2_z        : float = 0,
                 visibility_layer_a: bool = True,
                 visibility_layer_b: bool = True,
                 visibility_layer_c: bool = True,
                 scale_x           : int = 1,
                 scale_y           : int = 2,
                 scale_z           : int = 3):
        """ add a foil """

        self.view_model_ele_list[name] = (PythonPartViewData(visible_in_2d, visible_in_3d,
                                                             start_scale, end_scale,
                                                             ref_pnt1_x, ref_pnt1_y, ref_pnt1_z,
                                                             ref_pnt2_x, ref_pnt2_y, ref_pnt2_z,
                                                             visibility_layer_a, visibility_layer_b, visibility_layer_c,
                                                             scale_x, scale_y, scale_z), [])


    def set_use_default_3d_foil(self, state: bool):
        """ set the 2D/3D mode for the default foil """

        self.use_default_3d_foil = state

        self.set_foil("0")


    def set_foil(self, name: str):
        """ set the foil for the next elements """

        if name == "0":
            name += "_3D" if self.use_default_3d_foil else "_2D"

        self.model_ele_list = self.view_model_ele_list[name][1]


    def set_material(self, material_name: str):
        """ set the material surface """

        self.material_name = material_name


    def add_rectangle2d(self,
                        com_prop: AllplanBaseEle.CommonProperties,
                        x_left  : float,
                        y_bottom: float,
                        x_right : float,
                        y_top   : float):
        """ add a 2d rectangle """

        print(x_left, x_right, y_bottom, y_top)

        polygon = AllplanGeo.Polygon2D.CreateRectangle(AllplanGeo.Point2D(x_left * self.length_fac, y_bottom * self.length_fac),
                                                       AllplanGeo.Point2D(x_right * self.length_fac, y_top * self.length_fac))

        print(polygon)

        mat = self.trans_stack_2d.get_matrix()

        self.model_ele_list.append(AllplanBasisEle.ModelElement2D(com_prop, AllplanGeo.Transform(polygon, mat)))


    def add_line2d(self,
                   com_prop: AllplanBaseEle.CommonProperties,
                   x_start: float,
                   y_start: float,
                   x_end  : float,
                   y_end  : float):
        """ add a 2d line """

        line = AllplanGeo.Line2D(x_start * self.length_fac, y_start * self.length_fac,
                                 x_end * self.length_fac, y_end * self.length_fac)

        mat = self.trans_stack_2d.get_matrix()

        self.model_ele_list.append(AllplanBasisEle.ModelElement2D(com_prop, AllplanGeo.Transform(line, mat)))


    def add_arc2d(self,
                  com_prop   : AllplanBaseEle.CommonProperties,
                  x_center   : float,
                  y_center   : float,
                  radius     : float,
                  angle_start = 0.,
                  angle_end   = 360.):
        """ add a 2d arc """

        if angle_start == angle_end:
            return

        radius = radius * self.length_fac

        arc = AllplanGeo.Arc2D(AllplanGeo.Point2D(x_center * self.length_fac, y_center * self.length_fac),
                               radius, radius, 0.,
                               AllplanGeo.Angle.DegToRad(angle_start),
                               AllplanGeo.Angle.DegToRad(angle_end))

        mat = self.trans_stack_2d.get_matrix()

        self.model_ele_list.append(AllplanBasisEle.ModelElement2D(com_prop, AllplanGeo.Transform(arc, mat)))


    def add_arc3d(self,
                  com_prop   : AllplanBaseEle.CommonProperties,
                  x_center   : float,
                  y_center   : float,
                  radius     : float,
                  angle_start = 0.,
                  angle_end   = 360.):
        """ add a 3d arc """

        if angle_start == angle_end:
            return

        radius = radius * self.length_fac

        arc = AllplanGeo.Arc3D(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x_center * self.length_fac, y_center * self.length_fac, 0)),
                               radius, radius,
                               AllplanGeo.Angle.DegToRad(angle_start),
                               AllplanGeo.Angle.DegToRad(angle_end), True)


        mat = self.trans_stack_3d.get_matrix()

        self.model_ele_list.append(AllplanBasisEle.ModelElement3D(com_prop, AllplanGeo.Transform(arc, mat)))


    def add_circle2d(self,
                     com_prop   : AllplanBaseEle.CommonProperties,
                     x_center   : float,
                     y_center   : float,
                     radius     : float):
        """ add a 2d circle """

        radius = radius * self.length_fac

        arc = AllplanGeo.Arc2D(AllplanGeo.Point2D(x_center * self.length_fac, y_center * self.length_fac),
                               radius, radius, 0., 0,
                               AllplanGeo.Angle.DegToRad(360))

        mat = self.trans_stack_2d.get_matrix()

        self.model_ele_list.append(AllplanBasisEle.ModelElement2D(com_prop, AllplanGeo.Transform(arc, mat)))


    def add_circle3d(self,
                     com_prop   : AllplanBaseEle.CommonProperties,
                     x_center   : float,
                     y_center   : float,
                     radius     : float):
        """ add a 3d circle """

        radius = radius * self.length_fac

        arc = AllplanGeo.Arc3D(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x_center * self.length_fac, y_center * self.length_fac, 0)),
                               radius, radius, 0,
                               AllplanGeo.Angle.DegToRad(360), True)

        mat = self.trans_stack_3d.get_matrix()

        self.model_ele_list.append(AllplanBasisEle.ModelElement3D(com_prop, AllplanGeo.Transform(arc, mat)))


    def add_poly_point_element_2d(self,
                                  com_prop          : AllplanBaseEle.CommonProperties,
                                  poly_point_element: Any)                                :
        """ add a 2D element with poly points """

        scale_mat = AllplanGeo.Matrix2D()
        scale_mat.Scaling(self.length_fac, self.length_fac)

        mat = self.trans_stack_2d.get_matrix()

        self.model_ele_list.append(AllplanBasisEle.ModelElement2D(com_prop, AllplanGeo.Transform(poly_point_element,
                                                                                                      scale_mat * mat)))


    def add_text2d(self,
                   com_prop   : AllplanBaseEle.CommonProperties,
                   text_prop  : AllplanBasisEle.TextProperties,
                   x_ref_pnt  : float,
                   y_ref_pnt  : float,
                   text       : str):
        """ add a 2d text """

        mat = self.trans_stack_2d.get_matrix()

        ref_pnt = AllplanGeo.Transform(AllplanGeo.Point2D(x_ref_pnt * self.length_fac, y_ref_pnt * self.length_fac), mat)

        self.model_ele_list.append(AllplanBasisEle.TextElement(com_prop, text_prop, text, ref_pnt))


    def add_text3d(self,
                   com_prop        : AllplanBaseEle.CommonProperties,
                   text_prop       : AllplanBasisEle.TextProperties,
                   _text_thickness_z: float,
                   _height_flag     : int,
                   text            : str):
        """ add a 3d text """

        text_util = Text3DUtil()

        scaling_fac = DocumentManager.get_instance().document.GetScalingFactor()

        values = {AllplanBasisEle.TextAlignment.eLeftMiddle:    TextReferencePointPosition.CENTER_LEFT,
                  AllplanBasisEle.TextAlignment.eMiddleMiddle:  TextReferencePointPosition.CENTER_CENTER,
                  AllplanBasisEle.TextAlignment.eRightMiddle:   TextReferencePointPosition.CENTER_RIGHT,
                  AllplanBasisEle.TextAlignment.eLeftBottom:    TextReferencePointPosition.BOTTOM_LEFT,
                  AllplanBasisEle.TextAlignment.eMiddleBottom : TextReferencePointPosition.BOTTOM_CENTER,
                  AllplanBasisEle.TextAlignment.eRightBottom:   TextReferencePointPosition.BOTTOM_RIGHT,
                  AllplanBasisEle.TextAlignment.eLeftTop:       TextReferencePointPosition.TOP_LEFT,
                  AllplanBasisEle.TextAlignment.eMiddleTop:     TextReferencePointPosition.TOP_CENTER,
                  AllplanBasisEle.TextAlignment.eRightTop:      TextReferencePointPosition.TOP_RIGHT}

        bsplines = text_util.get_bsplines(AllplanGeo.Point3D(), text,
                                          values[text_prop.Alignment], text_prop.Height * scaling_fac, text_prop.TextAngle)

        for bspline in bsplines:
            self.add_geometry(com_prop, bspline)


    def add_line3d(self,
                   com_prop: AllplanBaseEle.CommonProperties,
                   x_start: float,
                   y_start: float,
                   z_start: float,
                   x_end  : float,
                   y_end  : float,
                   z_end  : float):
        """ add a 2d line """

        line = AllplanGeo.Line3D(x_start * self.length_fac, y_start * self.length_fac, z_start * self.length_fac,
                                 x_end * self.length_fac, y_end * self.length_fac, z_end * self.length_fac)

        self.__add_geometry_3d(com_prop, line)


    def add_box(self,
                com_prop: AllplanBaseEle.CommonProperties,
                length: float,
                width : float,
                height: float):
        """ add a box """

        box = AllplanGeo.Polyhedron3D.CreateCuboid(length * self.length_fac, width * self.length_fac, height * self.length_fac)

        self.__add_geometry_3d(com_prop, box)


    def add_cylinder(self,
                     com_prop: AllplanBaseEle.CommonProperties,
                     height: float,
                     radius: float):
        """ add a cylinder """

        if not height or not radius:
            return

        cylinder = AllplanGeo.BRep3D.CreateCylinder(AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(),
                                                                               AllplanGeo.Vector3D(radius * self.length_fac, 0, 0),
                                                                               AllplanGeo.Vector3D(0, 0, height * self.length_fac)),
                                                    radius * self.length_fac,
                                                    abs(height) * self.length_fac)

        self.__add_geometry_3d(com_prop, cylinder)


    def add_prism(self,
                  com_prop: AllplanBaseEle.CommonProperties,
                  height: float,
                  polygon: AllplanGeo.Polygon2D):
        """ add a prism """

        ref_pnt = polygon[0]

        path = AllplanGeo.Polyline3D()
        path += AllplanGeo.Point3D(ref_pnt)
        path += AllplanGeo.Point3D(ref_pnt.X, ref_pnt.Y, height * self.length_fac)

        scale_mat = AllplanGeo.Matrix2D()
        scale_mat.Scaling(self.length_fac, self.length_fac)

        polygon = AllplanGeo.Transform(polygon, scale_mat)

        _, polyhed = AllplanGeo.CreatePolyhedron(polygon, ref_pnt, path)

        self.__add_geometry_3d(com_prop, polyhed)


    def add_geometry(self,
                     com_prop: AllplanBaseEle.CommonProperties,
                     geo_object: Any):
        """ add a geometry """

        if str(type(geo_object)).find("2D") != -1:
            mat = self.trans_stack_2d.get_matrix()

            self.model_ele_list.append(AllplanBasisEle.ModelElement2D(com_prop, AllplanGeo.Transform(geo_object, mat)))

            return

        if not isinstance(geo_object, list):
            self.__add_geometry_3d(com_prop, geo_object)

            return

        for geo in geo_object:
            self.__add_geometry_3d(com_prop, geo)


    def __add_geometry_3d(self,
                          com_prop: AllplanBaseEle.CommonProperties,
                          geo_object: Any):
        """ add a 3D geometry object

        Args:
            com_prop:   common properties
            geo_object: geometry object
        """

        mat = self.trans_stack_3d.get_matrix()

        if self.material_name:
            self.model_ele_list.append(AllplanBasisEle.ModelElement3D(com_prop,
                                                                           AllplanBasisEle.TextureDefinition(self.material_name),
                                                                           AllplanGeo.Transform(geo_object, mat)))
        else:
            self.model_ele_list.append(AllplanBasisEle.ModelElement3D(com_prop, AllplanGeo.Transform(geo_object, mat)))


    def create_pythonpart(self,
                          build_ele          : BuildingElement,
                          build_ele_attr_list: BuildingElementAttributeList) -> List[Any]:
        """ create the PythonPart """

        pyp_util = PythonPartUtil()
        pyp_util.add_attribute_list(build_ele_attr_list)

        for _, (view_data, elements) in self.view_model_ele_list.items():
            if not elements:
                continue

            if view_data.visible_in_2d and view_data.visible_in_3d:
                pyp_util.add_pythonpart_view_2d3d(elements, view_data)

            elif view_data.visible_in_2d and not view_data.visible_in_3d:
                pyp_util.add_pythonpart_view_2d(elements, view_data)

            else:
                pyp_util.add_pythonpart_view_3d(elements, view_data)

        return pyp_util.create_pythonpart(build_ele)


    def get_elements(self) -> List[Any]:
        """ get the created element

        Returns:
            elements
        """

        return self.model_ele_list

```

</details>