---
title: "ParameterPropertyValueTypes"
source: "PythonPartsFramework\GeneralScripts\ValueTypes\ParameterPropertyValueTypes.py"
type: "class"
category: "02_API_Referenz"
tags:
  - parameter
  - script
  - werte
related:
  -
last_updated: "2026-02-20"
---


# ParameterPropertyValueTypes

> **Pfad:** `PythonPartsFramework\GeneralScripts\ValueTypes\ParameterPropertyValueTypes.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `parameter`, `script`, `werte`

## Übersicht

definition of the parameter property value types

## Abhängigkeiten

- `ParameterPropertyValueType`
- `Utilities.GeneralConstants`
- `ValueTypeUtils.ValueType`

## Klassen

### `ParameterPropertyValueTypes`

definition of the parameter property value types
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `is_button_type` | `value_type: ParameterPropertyValueType` | `bool` | test for button value type  Args:     value_type: value type  Returns:     button type state |
| `is_resource_list_type` | `value_type: ParameterPropertyValueType` | `bool` | test for resource list value type  Args:     value_type: value type  Returns:     button list type state |
| `has_multiple_types` | `value_type: ParameterPropertyValueType` | `bool` | test for button value type  Args:     value_type: value type  Returns:     button   type state |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" definition of the parameter property value types
"""

from Utilities.GeneralConstants import GeneralConstants

from .ValueTypeUtils.ValueType import ValueType

from .ParameterPropertyValueType import ParameterPropertyValueType

class ParameterPropertyValueTypes():
    """ definition of the parameter property value types
    """

    #--------------------- standard value types

    CONDITION_GROUP = ValueType("ParameterPropertyValueType", "conditiongroup", False, True)
    INCLUDE         = ValueType("ParameterPropertyValueType", "include", False, True)
    LIST_GROUP      = ValueType("ParameterPropertyValueType", "listgroup", False, True)
    NAMED_TUPLE     = ValueType("ParameterPropertyValueType", "namedtuple", False, True)
    ROW             = ValueType("ParameterPropertyValueType", "row", False, True)
    TUPLE           = ValueType("ParameterPropertyValueType", "tuple", False, True)


    #--------------------- attribute value types

    ATTRIBUTE          = ValueType("Resources.AttributeImpl", "attribute", True, True)
    ATTRIBUTE_ID       = ValueType("Resources.AttributeIdImpl", "attributeid", True, True)
    ATTRIBUTE_ID_VALUE = ValueType("Resources.AttributeIdValueImpl", "attributeidvalue", True, True)


    #--------------------- general value types

    EXPANDER  = ValueType("ParameterPropertyValueType", "expander", False, True)
    LIST      = ValueType("ListImpl", "list", True, True)
    OBJECT    = ValueType("ObjectImpl", "object", True, True)
    PICTURE   = ValueType("PictureImpl", "picture", True, False)
    SEPARATOR = ValueType("SeparatorImpl", "separator", True, True)

    COMMON_PROPERTIES          = ValueType("Resources.CommonPropertiesImpl", "commonproperties", True, True)
    PLANE_REFERENCES           = ValueType("Resources.PlaneReferencesImpl", "planereferences", True, True)
    SURFACE_ELEMENT_PROPERTIES = ValueType("Resources.SurfaceElementPropertiesImpl", "surfaceelementproperties", True, True)


    #--------------------- edit value types

    ANY_VALUE_BY_TYPE = ValueType("AnyValueByTypeImpl", "anyvaluebytype", True, True)
    AREA              = ValueType("AreaImpl", "area", True, True)
    ANGLE             = ValueType("AngleImpl", "angle", True, True)
    CODESTRING        = ValueType("CodeStringImpl", "codestring", True, True)
    DATE              = ValueType("DateImpl", "date", True, True)
    DISPLAY_TEXT      = ValueType("DisplayTextImpl", "displaytext", True, False)
    DOUBLE            = ValueType("DoubleImpl", "double", True, True)
    INTEGER           = ValueType("IntegerImpl", "integer", True, True)
    LENGTH            = ValueType("LengthImpl", "length", True, True)
    MULTILINESTRING   = ValueType("MultiLineStringImpl", "multilinestring", True, True)
    MULTIINDEX        = ValueType("MultiIndexImpl", "multiindex", True, True)
    STRING            = ValueType("StringImpl", "string", True, True)
    TEXT              = ValueType("TextImpl", "text", True, False)
    VOLUME            = ValueType("VolumeImpl", "volume", True, True)
    WEIGHT            = ValueType("WeightImpl", "weight", True, True)


    #--------------------- combo box value types

    ANGLE_COMBO_BOX          = ValueType("AngleComboBoxImpl", "anglecombobox", True, True)
    DOUBLE_COMBO_BOX         = ValueType("DoubleComboBoxImpl", "doublecombobox", True, True)
    DYNAMIC_STRING_COMBO_BOX = ValueType("DynamicStringComboBoxImpl", "dynamicstringcombobox", True, True)
    INTEGER_COMBO_BOX        = ValueType("IntegerComboBoxImpl", "integercombobox", True, True)
    LENGTH_COMBO_BOX         = ValueType("LengthComboBoxImpl", "lengthcombobox", True, True)
    STRING_COMBO_BOX         = ValueType("StringComboBoxImpl", "stringcombobox", True, True)


    #--------------------- selection controls

    BUTTON                       = ValueType("ButtonImpl", "button", True, False)
    CHECK_BOX                    = ValueType("CheckBoxImpl", "checkbox", True, True)
    MATERIAL_BUTTON              = ValueType("Resources.MaterialButtonImpl", "materialbutton", True, True)
    RADIO_BUTTON                 = ValueType("RadioButtonImpl", "radiobutton", True, False)
    RADIO_BUTTON_GROUP           = ValueType("RadioButtonGroupImpl", "radiobuttongroup", True, True)
    PICTURE_BUTTON               = ValueType("PictureButtonImpl", "picturebutton", True, False)
    PICTURE_BUTTON_LIST          = ValueType("PictureButtonListImpl", "picturebuttonlist", True, True)
    PICTURE_COMBO_BOX            = ValueType("PictureComboBoxImpl", "picturecombobox", True, True)
    PICTURE_RESOURCE_BUTTON      = ValueType("PictureResourceButtonImpl", "pictureresourcebutton", True, False)
    PICTURE_RESOURCE_BUTTON_LIST = ValueType("PictureResourceButtonListImpl", "pictureresourcebuttonlist", True, True)
    PICTURE_RESOURCE_COMBO_BOX   = ValueType("PictureResourceComboBoxImpl", "pictureresourcecombobox", True, True)
    REF_POINT_BUTTON             = ValueType("Resources.RefPointButtonImpl", "refpointbutton", True, True)


    #--------------------- reinforcement value type

    REINF_BAR_DIAMETER       = ValueType("Reinforcement.ReinfBarDiameterImpl", "reinfbardiameter", True, True)
    REINF_BENDING_ROLLER     = ValueType("Reinforcement.ReinfBendingRollerImpl", "reinfbendingroller", True, True)
    REINF_CONCRETE_COVER     = ValueType("Reinforcement.ReinfConcreteCoverImpl", "reinfconcretecover", True, True)
    REINF_CONCRETE_GRADE     = ValueType("Reinforcement.ReinfConcreteGradeImpl", "reinfconcretegrade", True, True)
    REINF_HOOK_LENGTH        = ValueType("Reinforcement.ReinfHookLengthImpl", "reinfhooklength", True, True)
    REINF_MESH_GROUP         = ValueType("Reinforcement.ReinfMeshGroupImpl", "reinfmeshgroup", True, True)
    REINF_MESH_TYPE          = ValueType("Reinforcement.ReinfMeshTypeImpl", "reinfmeshtype", True, True)
    REINF_POSITION           = ValueType("Reinforcement.ParameterPropertyValueType", "reinfposition", False, True)
    REINF_STEEL_GRADE        = ValueType("Reinforcement.ReinfSteelGradeImpl", "reinfsteelgrade", True, True)
    REINF_BAR_LABEL_POINTER  = ValueType("Reinforcement.ReinfBarLabelPointerImpl", "reinfbarlabelpointer", True, True)
    REINF_MESH_LABEL_POINTER = ValueType("Reinforcement.ReinfMeshLabelPointerImpl", "reinfmeshlabelpointer", True, True)
    REINF_LABEL_TEXT         = ValueType("Reinforcement.ReinfLabelTextImpl", "reinflabeltext", True, True)

    REINFORCEMENT_SHAPE_PROPERTIES      = ValueType("Reinforcement.ReinforcementShapePropertiesImpl",
                                                    "reinforcementshapeproperties", True, True)
    REINFORCEMENT_SHAPE_BAR_PROPERTIES  = ValueType("Reinforcement.ReinforcementShapeBarPropertiesImpl",
                                                    "reinforcementshapebarproperties", True, True)
    REINFORCEMENT_SHAPE_MESH_PROPERTIES = ValueType("Reinforcement.ReinforcementShapeMeshPropertiesImpl",
                                                    "reinforcementshapemeshproperties", True, True)


    #--------------------- precast

    AREA_FIXTURE_CATALOG_REFERENCE          = ValueType("Precast.AreaFixtureCatalogReferenceImpl", "areafixturecatalogreference",
                                                        True, True)
    BRICK_TILE_CATALOG_REFERENCE            = ValueType("Precast.BrickTileCatalogReferenceImpl", "bricktilecatalogreference", True, True)
    CONCRETE_GRADE_CATALOGREFERENCE         = ValueType("Precast.ConcreteGradeCatalogReferenceImpl",
                                                        "concretegradecatalogreference", True, True)
    FACTORY_CATALOG_REFERENCE               = ValueType("Precast.FactoryCatalogReferenceImpl", "factorycatalogreference", True, True)
    FIXTURE                                 = ValueType("Precast.FixtureImpl", "fixture", True, True)
    FIXTURE_PROPERTIES                      = ValueType("Precast.FixtureImpl", "fixtureproperties", True, True)
    FIXTURE_CATALOG_REFERENCE               = ValueType("Precast.FixtureCatalogReferenceImpl", "fixturecatalogreference", True, True)
    INSULATION_CATALOG_REFERENCE            = ValueType("Precast.InsulationCatalogReferenceImpl", "insulationcatalogreference",
                                                        True, True)
    LINE_FIXTURE_CATALOG_REFERENCE          = ValueType("Precast.LineFixtureCatalogReferenceImpl", "linefixturecatalogreference",
                                                        True, True)
    MATERIAL_CATALOG_REFERENCE              = ValueType("Precast.MaterialCatalogReferenceImpl", "materialcatalogreference", True, True)
    MULTI_MATERIAL_LAYOUT_CATALOG_REFERENCE = ValueType("Precast.MultiMaterialLayoutCatalogReferenceImpl",
                                                        "multimateriallayoutcatalogreference", True, True)
    NORM_CATALOG_REFERENCE                  = ValueType("Precast.NormCatalogReferenceImpl", "normcatalogreference", True, True)
    POINT_FIXTURE_CATALOG_REFERENCE         = ValueType("Precast.PointFixtureCatalogReferenceImpl",
                                                        "pointfixturecatalogreference", True, True)
    PRECAST_ELEMENT_TYPE_CATALOG_REFERENCE  = ValueType("Precast.PrecastElementTypeCatalogReferenceImpl",
                                                        "precastelementtypecatalogreference", True, True)
    SURFACE_CATALOG_REFERENCE               = ValueType("Precast.SurfaceCatalogReferenceImpl", "surfacecatalogreference", True, True)

    PRECAST_LAYER_PROPERTIES = ValueType("Precast.PrecastLayerPropertiesImpl", "precastlayerproperties", True, True)

    #--------------------- resource combo box value types

    COLOR                   = ValueType("Resources.ColorImpl", "color", True, True)
    FACESTYLE               = ValueType("Resources.FaceStyleImpl", "facestyle", True, True)
    FONT                    = ValueType("Resources.FontImpl", "font", True, True)
    FONTEMPHASIS            = ValueType("Resources.FontEmphasisImpl", "fontemphasis", True, True)
    HATCH                   = ValueType("Resources.HatchImpl", "hatch", True, True)
    LAYER                   = ValueType("Resources.LayerImpl", "layer", True, True)
    PATTERN                 = ValueType("Resources.PatternImpl", "pattern", True, True)
    PEN                     = ValueType("Resources.PenImpl", "pen", True, True)
    CONSTRUCTIONPOINTSYMBOL = ValueType("Resources.ConstructionPointSymbolImpl", "constructionpointsymbol", True, True)
    STROKE                  = ValueType("Resources.StrokeImpl", "stroke", True, True)


    #--------------------- geometry value types

    ARC2D           = ValueType("GeometryElements.Arc2DImpl", "arc2d", True, True)
    ARC3D           = ValueType("GeometryElements.Arc3DImpl", "arc3d", True, True)
    AXISPLACEMENT3D = ValueType("GeometryElements.AxisPlacement3DImpl", "axisplacement3d", True, True)
    BREP3D          = ValueType("GeometryElements.BRep3DImpl", "brep3d", True, True)
    BSPLINE2D       = ValueType("GeometryElements.BSpline2DImpl", "bspline2d", True, True)
    BSPLINE3D       = ValueType("GeometryElements.BSpline3DImpl", "bspline3d", True, True)
    CIRCLE2D        = ValueType("GeometryElements.Circle2DImpl", "circle2d", True, True)
    CIRCLE3D        = ValueType("GeometryElements.Circle3DImpl", "circle3d", True, True)
    GEOMETRY_OBJECT = ValueType("GeometryElements.GeometryObjectImpl", "$geometryobject", True, True)
    LINE2D          = ValueType("GeometryElements.Line2DImpl", "line2d", True, True)
    LINE3D          = ValueType("GeometryElements.Line3DImpl", "line3d", True, True)
    MATRIX3D        = ValueType("GeometryElements.Matrix3DImpl", "matrix3d", True, True)
    PLANE3D         = ValueType("GeometryElements.Plane3DImpl", "plane3d", True, True)
    POINT2D         = ValueType("GeometryElements.Point2DImpl", "point2d", True, True)
    POINT3D         = ValueType("GeometryElements.Point3DImpl", "point3d", True, True)
    PATH2D          = ValueType("GeometryElements.Path2DImpl", "path2d", True, True)
    PATH3D          = ValueType("GeometryElements.Path3DImpl", "path3d", True, True)
    POLYGON2D       = ValueType("GeometryElements.Polygon2DImpl", "polygon2d", True, True)
    POLYGON3D       = ValueType("GeometryElements.Polygon3DImpl", "polygon3d", True, True)
    POLYHEDRON3D    = ValueType("GeometryElements.Polyhedron3DImpl", "polyhedron3d", True, True)
    POLYLINE2D      = ValueType("GeometryElements.Polyline2DImpl", "polyline2d", True, True)
    POLYLINE3D      = ValueType("GeometryElements.Polyline3DImpl", "polyline3d", True, True)
    SPLINE2D        = ValueType("GeometryElements.Spline2DImpl", "spline2d", True, True)
    SPLINE3D        = ValueType("GeometryElements.Spline3DImpl", "spline3d", True, True)
    VECTOR2D        = ValueType("GeometryElements.Vector2DImpl", "vector2d", True, True)
    VECTOR3D        = ValueType("GeometryElements.Vector3DImpl", "vector3d", True, True)


    #--------------------- connection value types

    TIMESTAMP_CONNECTION        = ValueType("Connections.TimeStampConnectionImpl", "timestampconnection", True, True)
    PARAMETER_CONNECTION        = ValueType("Connections.ParameterConnectionImpl", "parameterconnection", True, True)
    POINT_CONNECTION            = ValueType("Connections.PointConnectionImpl", "pointconnection", True, True)
    ELEMENT_GEOMETRY_CONNECTION = ValueType("Connections.ElementGeometryConnectionImpl", "elementgeometryconnection", True, True)
    ARCH_OPENING_CONNECTION     = ValueType("Connections.ArchOpeningConnectionImpl", "archopeningconnection", True, True)


    #--------------------- special value types

    DYNAMIC_LIST        = "dynamiclist"
    SINGLE_VALUE_SELECT = "singlevalueselection"
    DRAWING_FILE        = ValueType("DrawingFileImpl", "drawingfile", True, True)


    @staticmethod
    def is_button_type(value_type: ParameterPropertyValueType) -> bool:
        """ test for button value type

        Args:
            value_type: value type

        Returns:
            button type state
        """

        return value_type in {ParameterPropertyValueTypes.BUTTON,
                              ParameterPropertyValueTypes.PICTURE_BUTTON,
                              ParameterPropertyValueTypes.PICTURE_RESOURCE_BUTTON}

    @staticmethod
    def is_resource_list_type(value_type: ParameterPropertyValueType) -> bool:
        """ test for resource list value type

        Args:
            value_type: value type

        Returns:
            button list type state
        """

        return value_type in {ParameterPropertyValueTypes.PICTURE_BUTTON_LIST,
                              ParameterPropertyValueTypes.PICTURE_COMBO_BOX,
                              ParameterPropertyValueTypes.PICTURE_RESOURCE_BUTTON_LIST,
                              ParameterPropertyValueTypes.PICTURE_RESOURCE_COMBO_BOX}

    @staticmethod
    def has_multiple_types(value_type: ParameterPropertyValueType) -> bool:
        """ test for button value type

        Args:
            value_type: value type

        Returns:
            button   type state
        """

        return GeneralConstants.TUPLE_SEPARATOR_START in value_type

```

</details>