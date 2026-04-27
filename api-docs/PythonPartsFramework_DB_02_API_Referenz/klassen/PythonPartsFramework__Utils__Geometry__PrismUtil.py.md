---
title: "PrismUtil"
source: "PythonPartsFramework\Utils\Geometry\PrismUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# PrismUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\PrismUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of PrismUtil class

- create a prism from a 2D path or polygon and height

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Geometry`
- `Utils.Geometry.ExtrudeByVectorUtil`
- `math`
- `typing`

## Klassen

### `PrismUtil`

implementation of PrismUtil class
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `from_path_2d` | `path: AllplanGeo.Path2D, height: float` | `AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None` | create a prism from a 2D path and height  Args:     path:   path of the footprint     height: height of the prism  Returns:     created prism |
| `from_path_2d_with_chamfer` | `path: AllplanGeo.Path2D, height: float, chamfer_height: float, chamfer_angle: float` | `AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None` | create a prism from a 2D path and height with chamfer  Args:     path:           path of the footprint     height:         height of the prism     chamfer_height: height of the chamfer     chamfer_angle:  angle of the chamfer  Returns:     created prism |
| `from_polygon_2d` | `polygon: AllplanGeo.Polygon2D, height: float, scale_poly: bool=False` | `AllplanGeo.Polyhedron3D | None` | create a prism from a 2D polygon and height  Args:     polygon:    polygon of the footprint     height:     height of the prism     scale_poly: scale the polygon to the length factor  Returns:     created prism |
| `from_polygon_2d_with_holes` | `polygon: AllplanGeo.Polygon2D, holes: list[AllplanGeo.Polygon2D], height: float, scale_poly: bool=False` | `AllplanGeo.Polyhedron3D | None` | create a prism from a 2D polygon and height with holes  Args:     polygon:    polygon of the footprint     holes:      hole polygons (the polygons itself can have multiple parts)     height:     height of the prism     scale_poly: scale the polygon to the length factor  Returns:     created prism |
| `from_polygon_2d_with_chamfer` | `polygon: AllplanGeo.Polygon2D, height: float, chamfer_height: float, chamfer_angle: float, scale_poly: bool=False` | `AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None` | create a prism from a 2D polygon and height with chamfer  Args:     polygon:        polygon of the footprint     height:         height of the prism     chamfer_height: height of the chamfer     chamfer_angle:  angle of the chamfer     scale_poly:     scale the polygon to the length factor  Returns:     created prism |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of PrismUtil class

    - create a prism from a 2D path or polygon and height
"""

from typing import cast

import math

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Geometry as AllplanGeo

from Utils.Geometry.ExtrudeByVectorUtil import ExtrudeByVectorUtil

class PrismUtil():
    """ implementation of PrismUtil class
    """

    @staticmethod
    def from_path_2d(path  : AllplanGeo.Path2D,
                     height: float) -> (AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None):
        """ create a prism from a 2D path and height

        Args:
            path:   path of the footprint
            height: height of the prism

        Returns:
            created prism
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        return ExtrudeByVectorUtil.extrude([path], AllplanGeo.Vector3D(0, 0, height * length_fac), False, True)


    @staticmethod
    def from_path_2d_with_chamfer(path          : AllplanGeo.Path2D,
                                  height        : float,
                                  chamfer_height: float,
                                  chamfer_angle : float) -> (AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None):
        """ create a prism from a 2D path and height with chamfer

        Args:
            path:           path of the footprint
            height:         height of the prism
            chamfer_height: height of the chamfer
            chamfer_angle:  angle of the chamfer

        Returns:
            created prism
        """

        assert False, "Not implemented yet"

        prism = PrismUtil.from_path_2d(path, height)

        return prism


    @staticmethod
    def from_polygon_2d(polygon   : AllplanGeo.Polygon2D,
                        height    : float,
                        scale_poly: bool = False) -> AllplanGeo.Polyhedron3D | None:
        """ create a prism from a 2D polygon and height

        Args:
            polygon:    polygon of the footprint
            height:     height of the prism
            scale_poly: scale the polygon to the length factor

        Returns:
            created prism
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        if scale_poly:
            scale_mat = AllplanGeo.Matrix2D()
            scale_mat.SetScaling(length_fac, length_fac)

            polygon *= scale_mat

        polyhedron = ExtrudeByVectorUtil.extrude([polygon], AllplanGeo.Vector3D(0, 0, height * length_fac), False, True)

        return None if polyhedron is None else cast(AllplanGeo.Polyhedron3D, polyhedron)


    @staticmethod
    def from_polygon_2d_with_holes(polygon   : AllplanGeo.Polygon2D,
                                   holes     : list[AllplanGeo.Polygon2D],
                                   height    : float,
                                   scale_poly: bool = False) -> AllplanGeo.Polyhedron3D | None:
        """ create a prism from a 2D polygon and height with holes

        Args:
            polygon:    polygon of the footprint
            holes:      hole polygons (the polygons itself can have multiple parts)
            height:     height of the prism
            scale_poly: scale the polygon to the length factor

        Returns:
            created prism
        """

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        if scale_poly:
            scale_mat = AllplanGeo.Matrix2D()
            scale_mat.SetScaling(length_fac, length_fac)

            polygon *= scale_mat

        if (polyhedron := ExtrudeByVectorUtil.extrude([polygon], AllplanGeo.Vector3D(0, 0, height * length_fac), False, True)) is None:
            print("PrismUtil.from_polygon_2d_with_holes: Extrude failed for outer polygon")

            return None

        if not holes:
            return cast(AllplanGeo.Polyhedron3D, polyhedron)


        #--------------- extrude holes and subtract from prism

        for _hole in holes:
            hole = _hole * scale_mat if scale_poly else _hole

            for hole_polygon in AllplanGeo.Polygon2DBuilder.SplitToPolygonParts(hole):
                print(hole_polygon)

                if (hole_polyhedron := ExtrudeByVectorUtil.extrude([hole_polygon], AllplanGeo.Vector3D(0, 0, height * length_fac),
                                                                   False, True)) is None:
                    print("PrismUtil.from_polygon_2d_with_holes: Extrude failed for hole polygon")

                    return None

                err, polyhedron = AllplanGeo.MakeSubtraction(cast(AllplanGeo.Polyhedron3D, polyhedron),
                                                             cast(AllplanGeo.Polyhedron3D, hole_polyhedron))

                if err != AllplanGeo.eGeometryErrorCode.eOK:
                    print("PrismUtil.from_polygon_2d_with_holes: MakeSubtraction failed:", err)

        return None if polyhedron is None else cast(AllplanGeo.Polyhedron3D, polyhedron)


    @staticmethod
    def from_polygon_2d_with_chamfer(polygon       : AllplanGeo.Polygon2D,
                                     height        : float,
                                     chamfer_height: float,
                                     chamfer_angle : float,
                                     scale_poly    : bool = False) -> (AllplanGeo.Polyhedron3D | AllplanGeo.BRep3D | None):
        """ create a prism from a 2D polygon and height with chamfer

        Args:
            polygon:        polygon of the footprint
            height:         height of the prism
            chamfer_height: height of the chamfer
            chamfer_angle:  angle of the chamfer
            scale_poly:     scale the polygon to the length factor

        Returns:
            created prism
        """

        if (prism1 := PrismUtil.from_polygon_2d(polygon, height - chamfer_height, scale_poly)) is None:
            print("PrismUtil.from_polygon_2d_with_chamfer: creating main prism failed")

            return None


        #--------------- create the chamfer part

        length_fac = AllplanSettings.PythonPartsSettings.GetInstance().GetLengthFactor()

        if scale_poly:
            scale_mat = AllplanGeo.Matrix2D()
            scale_mat.SetScaling(length_fac, length_fac)

            polygon *= scale_mat

        _, top_poly = AllplanGeo.Offset(chamfer_height * length_fac / math.tan(math.radians(chamfer_angle)), polygon, True)

        _, bottom_poly = AllplanGeo.ConvertTo3D(polygon, (height - chamfer_height) * length_fac)
        _, top_poly    = AllplanGeo.ConvertTo3D(top_poly, height * length_fac)

        _, prism2 = AllplanGeo.CreatePolyhedron(bottom_poly, top_poly)

        err, prism = AllplanGeo.MakeUnion(prism1, prism2)

        return prism if err == AllplanGeo.eGeometryErrorCode.eOK else None

```

</details>