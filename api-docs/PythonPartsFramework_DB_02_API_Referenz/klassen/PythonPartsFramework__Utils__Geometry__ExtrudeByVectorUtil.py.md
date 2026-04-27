---
title: "ExtrudeByVectorUtil"
source: "PythonPartsFramework\Utils\Geometry\ExtrudeByVectorUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# ExtrudeByVectorUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\ExtrudeByVectorUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the extrude by vector utility

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `TypeCollections.GeometryTyping`
- `typing`

## Klassen

### `ExtrudeByVectorUtil`

implementation of the extrude by vector utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `extrude` | `geo_elements: list[CURVES], extrusion_vec: AllplanGeo.Vector3D, from_center: bool, closed_volume: bool` | `AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None` | extrude the geometry elements by an extrusion vector  Args:     geo_elements:  geometry elements     extrusion_vec: extrusion vector     from_center:   extrude from center     closed_volume: closed volume state  Returns:     extrusion element |
| `__extrude_as_polyhedron_3d` | `closed_volume: bool, extrusion_vec: AllplanGeo.Vector3D, geo_element: LINEAR_CURVES_3D` | `AllplanGeo.Polyhedron3D | None` | extrude the geometry as polyhedron  Args:     closed_volume: closed volume state     extrusion_vec: extrusion vector     geo_element:   linear curve  Returns:     Polyhedron3D |
| `__extrude_as_brep_3d` | `closed_volume: bool, extrusion_vec: AllplanGeo.Vector3D, geo_elements_3d: list[CURVES_3D]` | `AllplanGeo.BRep3D | None` | extrude the geometry as polyhedron  Args:     closed_volume:   closed volume state     extrusion_vec:   extrusion vector     geo_elements_3d: geometry elements  Returns:     BRep3D |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the extrude by vector utility
"""

from typing import cast

import NemAll_Python_Geometry as AllplanGeo

from TypeCollections.GeometryTyping import CURVES, CURVES_2D, CURVES_3D, LINEAR_CURVES_3D, GeometryTyping

class ExtrudeByVectorUtil():
    """ implementation of the extrude by vector utility
    """

    @staticmethod
    def extrude(geo_elements : list[(CURVES)],
                extrusion_vec: AllplanGeo.Vector3D,
                from_center  : bool,
                closed_volume: bool) -> (AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None):
        """ extrude the geometry elements by an extrusion vector

        Args:
            geo_elements:  geometry elements
            extrusion_vec: extrusion vector
            from_center:   extrude from center
            closed_volume: closed volume state

        Returns:
            extrusion element
        """

        geo_elements_3d : list[CURVES_3D] = []

        if len(geo_elements) == 1 and isinstance(geo_elements[0], AllplanGeo.Path2D) and geo_elements[0].Count() == 1:
            geo_elements = [cast(CURVES_3D, geo_elements[0].GetElement(0))]     # pylint: disable=use-tuple-over-list


        #----------------- convert to 3D elements

        for geo_ele in geo_elements:
            if geo_ele is None:
                continue

            if GeometryTyping.is_curve_3d(geo_ele):
                geo_elements_3d.append(cast(CURVES_3D, geo_ele))
            else:
                geo_elements_3d.append(cast(CURVES_3D, AllplanGeo.ConvertTo3D(cast(CURVES_2D, geo_ele))[1]))

        if not geo_elements_3d:
            return None


        #----------------- move the geometry in case of extrude from center

        if from_center:
            move_vec = extrusion_vec / (-2)

            geo_elements_3d = [AllplanGeo.Move(geo_element, move_vec) for geo_element in geo_elements_3d]

        geo_element       = geo_elements_3d[0]
        geo_element_count = len(geo_elements_3d)


        #----------------- Polyhedron from line, polyline, polygon

        if geo_element_count == 1  and  isinstance(geo_element, LINEAR_CURVES_3D):
            return ExtrudeByVectorUtil.__extrude_as_polyhedron_3d(closed_volume, extrusion_vec, geo_element)

        return ExtrudeByVectorUtil.__extrude_as_brep_3d(closed_volume, extrusion_vec, geo_elements_3d)


    @staticmethod
    def __extrude_as_polyhedron_3d(closed_volume: bool,
                                   extrusion_vec: AllplanGeo.Vector3D,
                                   geo_element  : LINEAR_CURVES_3D) -> (AllplanGeo.Polyhedron3D | None):
        """ extrude the geometry as polyhedron

        Args:
            closed_volume: closed volume state
            extrusion_vec: extrusion vector
            geo_element:   linear curve

        Returns:
            Polyhedron3D
        """

        close_extrusion = closed_volume


        #----------------- create the needed Polyline3D for the extrusion as Polyhedron

        if isinstance(geo_element, AllplanGeo.Line3D):
            poly_line = AllplanGeo.Polyline3D()
            poly_line += geo_element

            close_extrusion = False

        elif isinstance(geo_element, AllplanGeo.Polyline3D):
            poly_line = geo_element
            close_extrusion = geo_element.StartPoint == geo_element.EndPoint

        elif isinstance(geo_element, AllplanGeo.Polygon3D):
            err, poly_line = AllplanGeo.CreatePolyline3D(geo_element)

            if err != AllplanGeo.eGeometryErrorCode.eOK:
                return None


        #----------------- create the polyline list

        poly_list = AllplanGeo.Polyline3DList()

        poly_list.append(poly_line)


        #----------------- create the extrusion path

        start_pnt = geo_element.StartPoint

        path = AllplanGeo.Polyline3D()

        path += start_pnt
        path += start_pnt + AllplanGeo.Point3D(extrusion_vec.X, extrusion_vec.Y, extrusion_vec.Z)


        #----------------- extrude the polyline

        err, extruded_ele = AllplanGeo.CreateSweptPolyhedron3D(poly_list, path, close_extrusion, True, AllplanGeo.Vector3D())

        if err != AllplanGeo.eGeometryErrorCode.eOK:
            print("ExtrudeByVectorUtil.__extrude_as_polyhedron_3d: CreateSweptPolyhedron3D failed:", err)

        return extruded_ele if err == AllplanGeo.eGeometryErrorCode.eOK else None


    @staticmethod
    def __extrude_as_brep_3d(closed_volume  : bool,
                             extrusion_vec  : AllplanGeo.Vector3D,
                             geo_elements_3d: list[CURVES_3D]) -> (AllplanGeo.BRep3D | None):
        """ extrude the geometry as polyhedron

        Args:
            closed_volume:   closed volume state
            extrusion_vec:   extrusion vector
            geo_elements_3d: geometry elements

        Returns:
            BRep3D
        """

        start_pnt = geo_elements_3d[0].StartPoint

        path = AllplanGeo.Polyline3D()

        path += start_pnt
        path += start_pnt + AllplanGeo.Point3D(extrusion_vec.X, extrusion_vec.Y, extrusion_vec.Z)

        err, extruded_ele = AllplanGeo.CreateSweptBRep3D(geo_elements_3d, path, closed_volume, False, None, 0)

        if err != AllplanGeo.eGeometryErrorCode.eOK:
            print("ExtrudeByVectorUtil.__extrude_as_brep_3d: CreateSweptBRep3D failed:", err)

        return extruded_ele if err == AllplanGeo.eGeometryErrorCode.eOK else None

```

</details>