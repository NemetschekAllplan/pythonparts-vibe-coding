---
title: "ModelEleList"
source: "PythonPartsFramework\TypeCollections\ModelEleList.py"
type: "class"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# ModelEleList

> **Pfad:** `PythonPartsFramework\TypeCollections\ModelEleList.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `dokumentation`

## Übersicht

implementation of the model element list

## Abhängigkeiten

- `Curve3DList`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_ArchElements`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `Utils.Geometry.TransformationStack`
- `__future__`
- `ntpath`
- `typing`

## Klassen

### `ModelEleList`

implementation of the model element list
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, com_prop: AllplanBaseEle.CommonProperties=AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties(), element: AllplanBasisEle.AllplanElement | None=None, trans_stack: TransformationStack=TransformationStack(LengthUnit.MM, AngleUnit.RADIAN)` | `None` | initialize  Args:     com_prop:    common properties for the elements     element:     element to add to the list     trans_stack: transformation stack |
| `trans_stack` | `self` | `TransformationStack` | get the transformation stack  Returns:     transformation stack |
| `append_geometry_2d` | `self, geo_ele: ListModelEle2D | ModelEle2D | ModelEle2DList | None, com_prop: AllplanBaseEle.CommonProperties | None=None` | `None` | append a 2D geometry element to the list  Args:     geo_ele:  2D geometry element     com_prop: common properties |
| `append_geometry_3d_with_texture` | `self, geo_ele: ListModelEle3D | ModelEle3D | ModelEle3DList | Curve3DList, texture_def: AllplanBasisEle.TextureDefinition, com_prop: AllplanBaseEle.CommonProperties | None=None, texture_mapping: AllplanBasisEle.TextureMapping | None=None, section_surface_ele_props: AllplanArchEle.SurfaceElementProperties | None=None, use_trans_matrix: bool=True` | `None` | append a 3D geometry element to the list  Args:     geo_ele:                   3D geometry element     texture_def:               texture definition     com_prop:                  common properties     texture_mapping:           texture mapping     section_surface_ele_props: surface element properties for the representation in the section     use_trans_matrix:          use the current transformation matrix state |
| `append_geometry_3d` | `self, geo_ele: ListModelEle3D | ModelEle3D | ModelEle3DList | Curve3DList | None, com_prop: AllplanBaseEle.CommonProperties | None=None, section_surface_ele_props: AllplanArchEle.SurfaceElementProperties | None=None, use_trans_matrix: bool=True` | `None` | append a 3D geometry element to the list  Args:     geo_ele:                   3D geometry element     com_prop:                  common properties     section_surface_ele_props: surface element properties for the representation in the section     use_trans_matrix:          use the current transformation matrix state |
| `append` | `self, allplan_ele: AllplanBasisEle.AllplanElement` | `None` | append an element to the list  Args:     allplan_ele: Allplan element |
| `__create_model_element_3d` | `self, geo_ele: ModelEle3D, use_trans_matrix: bool, com_prop: AllplanBaseEle.CommonProperties, texture_def: AllplanBasisEle.TextureDefinition | None, texture_mapping: AllplanBasisEle.TextureMapping | None, section_surface_ele_props: AllplanArchEle.SurfaceElementProperties | None` | `AllplanBasisEle.ModelElement3D` | create a model element 3D  Args:     geo_ele:                   3D geometry element     use_trans_matrix:          use the current transformation matrix state     com_prop:                  common properties     texture_def:               texture definition     texture_mapping:           texture mapping     section_surface_ele_props: surface element properties for the representation in the section  Returns:     ModelElement3D |
| `set_color` | `self, color: int` | `None` | set the color  Args:     color: color |
| `set_pen` | `self, pen: int` | `None` | set the pen  Args:     pen: pen |
| `set_stroke` | `self, stroke: int` | `None` | set the stroke  Args:     stroke: stroke |
| `set_color_by_layer` | `self, color_by_layer: bool` | `None` | set the color by layer  Args:     color_by_layer: color by layer |
| `set_pen_by_layer` | `self, pen_by_layer: bool` | `None` | set the pen by layer  Args:     pen_by_layer: pen by layer |
| `set_stroke_by_layer` | `self, stroke_by_layer: bool` | `None` | set the stroke by layer  Args:     stroke_by_layer: stroke by layer |
| `set_layer` | `self, layer: int | str, document: AllplanEleAdapter.DocumentAdapter` | `None` | set the layer  Args:     layer:    layer as integer or string     document: document adapter to get the layer ID by the short name |
| `set_help_construction` | `self, help_construction: bool` | `None` | set the help construction flag  Args:     help_construction: help construction flag |
| `set_common_properties` | `self, com_prop: AllplanBaseEle.CommonProperties` | `None` | set the common properties  Args:     com_prop: common properties |
| `get_common_properties` | `self` | `AllplanBaseEle.CommonProperties` | get the common properties  Returns:     common properties |
| `set_texture` | `self, texture_def: AllplanBasisEle.TextureDefinition | None` | `None` | set the texture definition  Args:     texture_def: texture definition |
| `get_texture` | `self` | `AllplanBasisEle.TextureDefinition | None` | get the texture definition  Returns:     texture definition |
| `set_texture_mapping` | `self, texture_mapping: AllplanBasisEle.TextureMapping | None` | `None` | set the texture mapping  Args:     texture_mapping: texture mapping |
| `get_texture_mapping` | `self` | `AllplanBasisEle.TextureMapping | None` | get the texture mapping  Returns:     texture mapping |
| `set_section_filling` | `self, filling_id: int` | `None` | set the section filling properties  Args:     filling_id: filling ID |
| `set_section_hatching` | `self, hatching_id: int` | `None` | set the section hatching properties  Args:     hatching_id: hatching ID |
| `set_section_pattern` | `self, pattern_id: int` | `None` | set the section pattern properties  Args:     pattern_id: pattern ID |
| `set_section_face_style` | `self, face_style_id: int` | `None` | set the section face style properties  Args:     face_style_id: face style ID |
| `set_section_bitmap` | `self, bitmap_id: str` | `None` | set the section bitmap properties  Args:     bitmap_id: bitmap ID |
| `set_section_surface_ele_props` | `self, section_surface_ele_props: AllplanArchEle.SurfaceElementProperties | None` | `None` | set the section surface element properties  Args:     section_surface_ele_props: section surface element properties |
| `set_element_attributes` | `self, index: int, attributes: list[AllplanBaseEle.Attribute]` | `None` | set the attributes to the element with the defined index  Args:     index:      index     attributes: attributes |
| `__getitem__` | `self, index: int` | `AllplanBasisEle.AllplanElement` | get the model element by an index  Args:     index: index  Returns:     model element as AllplanElement |
| `__iadd__` | `self, other: ModelEleList` | `ModelEleList` | add the elements of another list to the current list  Args:     other: other list  Returns:     current list |
| `__add__` | `self, other: ModelEleList` | `ModelEleList` | add the elements of the current and another list  Args:     other: other list  Returns:     new list |
| `__add_section_surface_element_properties` | `model_ele: AllplanBasisEle.ModelElement3D, section_surface_ele_props: AllplanArchEle.SurfaceElementProperties` | `None` | add the surface element properties for the representation in the section  Args:     model_ele:                 model element     section_surface_ele_props: surface element properties for the representation in the section |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the model element list
"""

from __future__ import annotations

from typing import get_args, cast

import ntpath

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter
import NemAll_Python_Geometry as AllplanGeo

from Utils.Geometry.TransformationStack import TransformationStack, LengthUnit, AngleUnit

from .Curve3DList import Curve3DList

ModelEle2D = (AllplanGeo.Line2D | AllplanGeo.Arc2D |
              AllplanGeo.Polyline2D | AllplanGeo.Polygon2D |
              AllplanGeo.Spline2D | AllplanGeo.BSpline2D |
              AllplanGeo.Path2D | AllplanGeo.Clothoid2D)

ModelEle3D = (AllplanGeo.Line3D | AllplanGeo.Arc3D |
              AllplanGeo.Polyline3D | AllplanGeo.Polygon3D |
              AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D |
              AllplanGeo.Spline3D | AllplanGeo.BSpline3D |
              AllplanGeo.Path3D | AllplanGeo.Cylinder3D |
              AllplanGeo.ClippedSweptSolid3D | AllplanGeo.Cuboid3D)

ListModelEle2D = (list[AllplanGeo.Line2D] | list[AllplanGeo.Arc2D] |
                  list[AllplanGeo.Polyline2D] | list[AllplanGeo.Polygon2D] |
                  list[AllplanGeo.Spline2D] | list[AllplanGeo.BSpline2D] |
                  list[AllplanGeo.Path2D] | list[AllplanGeo.Clothoid2D])

ListModelEle3D = (list[AllplanGeo.Line3D] | list[AllplanGeo.Arc3D] |
                  list[AllplanGeo.Polyline3D] | list[AllplanGeo.Polygon3D] |
                  list[AllplanGeo.Polyhedron3D] | list[AllplanGeo.BRep3D] |
                  list[AllplanGeo.Spline3D] | list[AllplanGeo.BSpline3D] |
                  list[AllplanGeo.Path3D] | list[AllplanGeo.Cylinder3D] |
                  list[AllplanGeo.ClippedSweptSolid3D] | list[AllplanGeo.Cuboid3D])

ModelEle2DList = (AllplanGeo.Line2DList | AllplanGeo.Arc2DList |
                  AllplanGeo.Polyline2DList | AllplanGeo.Polygon2DList |
                  AllplanGeo.Spline2DList | AllplanGeo.BSpline2DList |
                  AllplanGeo.Path2DList | AllplanGeo.Clothoid2D)

ModelEle3DList = (AllplanGeo.Line3DList | AllplanGeo.Arc3DList |
                  AllplanGeo.Polyline3DList | AllplanGeo.Polygon3DList |
                  AllplanGeo.Polyhedron3DList | AllplanGeo.BRep3DList |
                  AllplanGeo.Spline3DList | AllplanGeo.BSpline3DList |
                  AllplanGeo.Path3DList | AllplanGeo.Cylinder3DList |
                  AllplanGeo.ClippedSweptSolid3DList | AllplanGeo.Cuboid3DList)


class ModelEleList(list[AllplanBasisEle.AllplanElement]):
    """ implementation of the model element list
    """

    def __init__(self,
                 com_prop   : AllplanBaseEle.CommonProperties         = AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties(),
                 element    : (AllplanBasisEle.AllplanElement | None) = None,
                 trans_stack: TransformationStack                     = TransformationStack(LengthUnit.MM, AngleUnit.RADIAN)):
        """ initialize

        Args:
            com_prop:    common properties for the elements
            element:     element to add to the list
            trans_stack: transformation stack
        """

        self.__com_prop    = AllplanBaseEle.CommonProperties(com_prop)
        self.__trans_stack = trans_stack

        self.__texture_def               : (AllplanBasisEle.TextureDefinition | None)       = None
        self.__texture_mapping           : (AllplanBasisEle.TextureMapping | None)          = None
        self.__section_surface_ele_props : (AllplanArchEle.SurfaceElementProperties | None) = None

        if element is not None:
            self.append(element)


    @property
    def trans_stack(self) -> TransformationStack:
        """ get the transformation stack

        Returns:
            transformation stack
        """

        return self.__trans_stack


    def append_geometry_2d(self,
                           geo_ele : (ListModelEle2D | ModelEle2D | ModelEle2DList | None),
                           com_prop: (AllplanBaseEle.CommonProperties | None) = None):
        """ append a 2D geometry element to the list

        Args:
            geo_ele:  2D geometry element
            com_prop: common properties
        """

        if geo_ele is None:
            return

        trans_mat = self.__trans_stack.trans_matrix.ReduceZDimension()

        if com_prop is None:
            com_prop = self.__com_prop

        if isinstance(geo_ele, get_args(ModelEle2D)):
            super().append(AllplanBasisEle.ModelElement2D(com_prop,
                                                          AllplanGeo.Transform(geo_ele, trans_mat)))               # type: ignore
        else:
            self += [AllplanBasisEle.ModelElement2D(com_prop,
                                                    AllplanGeo.Transform(item, trans_mat)) \
                     for item in geo_ele] # type: ignore


    def append_geometry_3d_with_texture(self,
                                        geo_ele                  : (ListModelEle3D | ModelEle3D | ModelEle3DList | Curve3DList),
                                        texture_def              : AllplanBasisEle.TextureDefinition,
                                        com_prop                 : (AllplanBaseEle.CommonProperties | None)         = None,
                                        texture_mapping          : (AllplanBasisEle.TextureMapping | None)          = None,
                                        section_surface_ele_props: (AllplanArchEle.SurfaceElementProperties | None) = None,
                                        use_trans_matrix         : bool                                             = True):
        """ append a 3D geometry element to the list

        Args:
            geo_ele:                   3D geometry element
            texture_def:               texture definition
            com_prop:                  common properties
            texture_mapping:           texture mapping
            section_surface_ele_props: surface element properties for the representation in the section
            use_trans_matrix:          use the current transformation matrix state
        """

        if com_prop is None:
            com_prop = self.__com_prop

        if section_surface_ele_props is None:
            section_surface_ele_props = self.__section_surface_ele_props

        if isinstance(geo_ele, get_args(ModelEle3D)):
            super().append(self.__create_model_element_3d(cast(ModelEle3D, geo_ele), use_trans_matrix, com_prop, texture_def,
                                                          texture_mapping, section_surface_ele_props))

            return


        #----------------- geometry list

        self.extend([self.__create_model_element_3d(item, True, com_prop, texture_def, texture_mapping,
                                                    section_surface_ele_props) for item in cast(ListModelEle3D, geo_ele)])


    def append_geometry_3d(self,
                           geo_ele                  : (ListModelEle3D | ModelEle3D | ModelEle3DList | Curve3DList | None),
                           com_prop                 : (AllplanBaseEle.CommonProperties | None)         = None,
                           section_surface_ele_props: (AllplanArchEle.SurfaceElementProperties | None) = None,
                           use_trans_matrix         : bool                                             = True):
        """ append a 3D geometry element to the list

        Args:
            geo_ele:                   3D geometry element
            com_prop:                  common properties
            section_surface_ele_props: surface element properties for the representation in the section
            use_trans_matrix:          use the current transformation matrix state
        """

        if geo_ele is None:
            return

        if com_prop is None:
            com_prop = self.__com_prop

        texture_def     = self.__texture_def
        texture_mapping = self.__texture_mapping

        if isinstance(geo_ele, get_args(ModelEle3D)):
            super().append(self.__create_model_element_3d(cast(ModelEle3D, geo_ele), use_trans_matrix, com_prop, texture_def,
                                                          texture_mapping, section_surface_ele_props))

            return


        #----------------- geometry list

        self.extend([self.__create_model_element_3d(item, use_trans_matrix, com_prop, texture_def, texture_mapping,
                                                    section_surface_ele_props) for item in cast(ListModelEle3D, geo_ele)])


    def append(self,
               allplan_ele: AllplanBasisEle.AllplanElement):
        """ append an element to the list

        Args:
            allplan_ele: Allplan element
        """

        if (geo_ele := allplan_ele.GetGeometryObject()) is not None:
            geo_ele = type(geo_ele)(geo_ele)  # type: ignore

            if isinstance(geo_ele, get_args(ModelEle2D)):
                trans_mat = self.trans_stack.trans_matrix.ReduceZDimension()

                geo_ele = AllplanGeo.Transform(geo_ele, trans_mat)       # type: ignore

            elif isinstance(geo_ele, get_args(ModelEle3D)):
                geo_ele = AllplanGeo.Transform(geo_ele, self.trans_stack.trans_matrix)       # type: ignore

            allplan_ele.SetGeometryObject(geo_ele)

        super().append(allplan_ele)


    def __create_model_element_3d(self,
                                  geo_ele                  : ModelEle3D,
                                  use_trans_matrix         : bool,
                                  com_prop                 : AllplanBaseEle.CommonProperties,
                                  texture_def              : (AllplanBasisEle.TextureDefinition | None),
                                  texture_mapping          : (AllplanBasisEle.TextureMapping | None),
                                  section_surface_ele_props: (AllplanArchEle.SurfaceElementProperties | None)) \
                                                              -> AllplanBasisEle.ModelElement3D:
        """ create a model element 3D

        Args:
            geo_ele:                   3D geometry element
            use_trans_matrix:          use the current transformation matrix state
            com_prop:                  common properties
            texture_def:               texture definition
            texture_mapping:           texture mapping
            section_surface_ele_props: surface element properties for the representation in the section

        Returns:
            ModelElement3D
        """

        trans_matrix = self.__trans_stack.trans_matrix if use_trans_matrix else AllplanGeo.Matrix3D()

        if texture_mapping is not None and texture_def is not None:
            model_ele = AllplanBasisEle.ModelElement3D(com_prop, texture_def, texture_mapping,
                                                       AllplanGeo.Transform(geo_ele, trans_matrix))
        elif texture_def is not None:
            model_ele = AllplanBasisEle.ModelElement3D(com_prop, texture_def, AllplanGeo.Transform(geo_ele, trans_matrix))

        else:
            model_ele = AllplanBasisEle.ModelElement3D(com_prop, AllplanGeo.Transform(geo_ele, trans_matrix))

        if section_surface_ele_props is not None:
            self.__add_section_surface_element_properties(model_ele, section_surface_ele_props)

        return model_ele


    def set_color(self,
                  color: int):
        """ set the color

        Args:
            color: color
        """

        self.__com_prop.Color = color

    def set_pen(self,
                pen: int):
        """ set the pen

        Args:
            pen: pen
        """

        self.__com_prop.Pen = pen

    def set_stroke(self,
                   stroke: int):
        """ set the stroke

        Args:
            stroke: stroke
        """

        self.__com_prop.Stroke = stroke

    def set_color_by_layer(self,
                           color_by_layer: bool):
        """ set the color by layer

        Args:
            color_by_layer: color by layer
        """

        self.__com_prop.ColorByLayer = color_by_layer

    def set_pen_by_layer(self,
                         pen_by_layer: bool):
        """ set the pen by layer

        Args:
            pen_by_layer: pen by layer
        """

        self.__com_prop.PenByLayer = pen_by_layer


    def set_stroke_by_layer(self,
                            stroke_by_layer: bool):
        """ set the stroke by layer

        Args:
            stroke_by_layer: stroke by layer
        """

        self.__com_prop.StrokeByLayer = stroke_by_layer

    def set_layer(self,
                  layer   : (int | str),
                  document: AllplanEleAdapter.DocumentAdapter):
        """ set the layer

        Args:
            layer:    layer as integer or string
            document: document adapter to get the layer ID by the short name
        """

        self.__com_prop.Layer = AllplanBaseEle.LayerService.GetIDByShortName(layer, document) if isinstance(layer, str) else layer


    def set_help_construction(self,
                             help_construction: bool):
        """ set the help construction flag

        Args:
            help_construction: help construction flag
        """

        self.__com_prop.HelpConstruction = help_construction

    def set_common_properties(self,
                              com_prop: AllplanBaseEle.CommonProperties):
        """ set the common properties

        Args:
            com_prop: common properties
        """

        self.__com_prop = AllplanBaseEle.CommonProperties(com_prop)

    def get_common_properties(self) -> AllplanBaseEle.CommonProperties:
        """ get the common properties

        Returns:
            common properties
        """

        return self.__com_prop

    def set_texture(self,
                    texture_def: (AllplanBasisEle.TextureDefinition | None)):
        """ set the texture definition

        Args:
            texture_def: texture definition
        """

        self.__texture_def = texture_def

    def get_texture(self) -> (AllplanBasisEle.TextureDefinition | None):
        """ get the texture definition

        Returns:
            texture definition
        """

        return self.__texture_def

    def set_texture_mapping(self,
                            texture_mapping: (AllplanBasisEle.TextureMapping | None)):
        """ set the texture mapping

        Args:
            texture_mapping: texture mapping
        """

        self.__texture_mapping = texture_mapping

    def get_texture_mapping(self) -> (AllplanBasisEle.TextureMapping | None):
        """ get the texture mapping

        Returns:
            texture mapping
        """

        return self.__texture_mapping

    def set_section_filling(self,
                            filling_id: int):
        """ set the section filling properties

        Args:
            filling_id: filling ID
        """

        filling_prop = AllplanArchEle.SurfaceElementProperties()

        filling_prop.FillingSelected = True
        filling_prop.FillingID       = filling_id

        self.__section_surface_ele_props = filling_prop

    def set_section_hatching(self,
                             hatching_id: int):
        """ set the section hatching properties

        Args:
            hatching_id: hatching ID
        """

        hatching_prop = AllplanArchEle.SurfaceElementProperties()

        hatching_prop.HatchSelected = True
        hatching_prop.HatchID       = hatching_id

        self.__section_surface_ele_props = hatching_prop

    def set_section_pattern(self,
                            pattern_id: int):
        """ set the section pattern properties

        Args:
            pattern_id: pattern ID
        """

        pattern_prop = AllplanArchEle.SurfaceElementProperties()

        pattern_prop.PatternSelected = True
        pattern_prop.PatternID       = pattern_id

        self.__section_surface_ele_props = pattern_prop

    def set_section_face_style(self,
                               face_style_id: int):
        """ set the section face style properties

        Args:
            face_style_id: face style ID
        """

        face_style_prop = AllplanArchEle.SurfaceElementProperties()

        face_style_prop.FaceStyleSelected = True
        face_style_prop.FaceStyleID       = face_style_id

        self.__section_surface_ele_props = face_style_prop

    def set_section_bitmap(self,
                           bitmap_id: str):
        """ set the section bitmap properties

        Args:
            bitmap_id: bitmap ID
        """

        bitmap_prop = AllplanArchEle.SurfaceElementProperties()

        bitmap_prop.BitmapSelected = True
        bitmap_prop.BitmapID       = bitmap_id

        self.__section_surface_ele_props = bitmap_prop

    def set_section_surface_ele_props(self,
                                      section_surface_ele_props: (AllplanArchEle.SurfaceElementProperties) | None):
        """ set the section surface element properties

        Args:
            section_surface_ele_props: section surface element properties
        """

        self.__section_surface_ele_props = section_surface_ele_props

    def set_element_attributes(self,
                               index     : int,
                               attributes: list[AllplanBaseEle.Attribute]):
        """ set the attributes to the element with the defined index

        Args:
            index:      index
            attributes: attributes
        """

        self[index].Attributes = AllplanBaseEle.Attributes([AllplanBaseEle.AttributeSet(attributes)])

    def __getitem__(self,
                    index: int) -> AllplanBasisEle.AllplanElement:
        """ get the model element by an index

        Args:
            index: index

        Returns:
            model element as AllplanElement
        """

        return super().__getitem__(index)


    def __iadd__(self,
                 other: ModelEleList) -> ModelEleList:
        """ add the elements of another list to the current list

        Args:
            other: other list

        Returns:
            current list
        """

        super().__iadd__(other)

        return self


    def __add__(self,
                other: ModelEleList) -> ModelEleList:
        """ add the elements of the current and another list

        Args:
            other: other list

        Returns:
            new list
        """

        new_list = ModelEleList()

        new_list.__iadd__(self)
        new_list.__iadd__(other)

        return new_list


    @staticmethod
    def __add_section_surface_element_properties(model_ele                : AllplanBasisEle.ModelElement3D,
                                                 section_surface_ele_props: AllplanArchEle.SurfaceElementProperties):
        """ add the surface element properties for the representation in the section

        Args:
            model_ele:                 model element
            section_surface_ele_props: surface element properties for the representation in the section
        """

        attr_list = [] if model_ele.Attributes is None else model_ele.Attributes.AttributeSets[0].Attributes

        match True:
            case _ if section_surface_ele_props.FillingSelected:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 3))
                attr_list.append(AllplanBaseEle.AttributeInteger(252, section_surface_ele_props.FillingID))

            case _ if section_surface_ele_props.HatchSelected:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 2))
                attr_list.append(AllplanBaseEle.AttributeInteger(124, section_surface_ele_props.HatchID))

                if section_surface_ele_props.FillingSelected:
                    attr_list.append(AllplanBaseEle.AttributeInteger(252, section_surface_ele_props.FillingID))

            case _ if section_surface_ele_props.PatternSelected:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 1))
                attr_list.append(AllplanBaseEle.AttributeInteger(126, section_surface_ele_props.PatternID))

                if section_surface_ele_props.FillingSelected:
                    attr_list.append(AllplanBaseEle.AttributeInteger(252, section_surface_ele_props.FillingID))

            case _ if section_surface_ele_props.FaceStyleSelected:
                attr_list.append(AllplanBaseEle.AttributeInteger(125, section_surface_ele_props.FaceStyleID))
                attr_list.append(AllplanBaseEle.AttributeInteger(252, 0))

            case _ if section_surface_ele_props.BitmapSelected:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 4))
                path, file = ntpath.split(section_surface_ele_props.BitmapID)

                attr_list.append(AllplanBaseEle.AttributeString(333, path))
                attr_list.append(AllplanBaseEle.AttributeString(336, file))

            case _:
                attr_list.append(AllplanBaseEle.AttributeInteger(118, 0))

        model_ele.SetAttributes(AllplanBaseEle.Attributes([AllplanBaseEle.AttributeSet(attr_list)]))

```

</details>