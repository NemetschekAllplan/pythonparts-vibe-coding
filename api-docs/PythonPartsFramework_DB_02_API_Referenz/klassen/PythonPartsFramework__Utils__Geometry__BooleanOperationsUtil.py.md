---
title: "BooleanOperationsUtil"
source: "PythonPartsFramework\Utils\Geometry\BooleanOperationsUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - geometrie
  - utility
related:
  -
last_updated: "2026-02-20"
---


# BooleanOperationsUtil

> **Pfad:** `PythonPartsFramework\Utils\Geometry\BooleanOperationsUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `geometrie`, `utility`

## Übersicht

implementation of the boolean operations utility

- create a group for geometry elements
- add geometry elements to the group
- create union or diff of two groups

## Abhängigkeiten

- `NemAll_Python_Geometry`
- `TypeCollections.ModelEleList`
- `Utils.Geometry.TransformationStack`

## Klassen

### `BooleanOperationsUtil`

implementation of the boolean operations utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, trans_stack: TransformationStack` | `None` | initialize  Args:     trans_stack: transformation stack |
| `add_group` | `self, name: str` | `None` | add a foil  Args:     name: name of the group |
| `close_group` | `self` | `None` | close the current group          |
| `add_geometry` | `self, geo_ele: GEO_TYPES` | `None` | add a 3D geometry element  Args:     geo_ele: geometry element |
| `union` | `self, group1: str | list[GEO_TYPES] | GEO_TYPES, group2: str | list[GEO_TYPES] | GEO_TYPES` | `GEO_TYPES` | create a union from two groups  Args:     group1: first group of elements     group2: second group of elements  Returns:     the union of the two groups or None if the union is not possible |
| `diff` | `self, group1: str | list[GEO_TYPES] | GEO_TYPES, group2: str | list[GEO_TYPES] | GEO_TYPES` | `GEO_TYPES` | create a diff from two groups  Args:     group1: first group of elements     group2: second group of elements  Returns:     the difference of the two groups or None if the difference is not possible |
| `get_group_elements` | `self, name: str` | `ListModelEle3D` | get the group elements  Args:     name: name of the group  Returns:     the group elements |
| `__convert_to_brep` | `geo_ele1: GEO_TYPES, geo_ele2: GEO_TYPES` | `tuple[GEO_TYPES, GEO_TYPES]` | convert the geometry elements to BRep3D if necessary  Args:     geo_ele1: first geometry element     geo_ele2: second geometry element  Returns:     tuple of converted geometry elements |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the boolean operations utility

    - create a group for geometry elements
    - add geometry elements to the group
    - create union or diff of two groups
"""

import NemAll_Python_Geometry as AllplanGeo

from TypeCollections.ModelEleList import ListModelEle3D

from Utils.Geometry.TransformationStack import TransformationStack

GEO_TYPES = AllplanGeo.BRep3D | AllplanGeo.Polyhedron3D | None

class BooleanOperationsUtil():
    """ implementation of the boolean operations utility
    """

    def __init__(self,
                 trans_stack: TransformationStack):
        """ initialize

        Args:
            trans_stack: transformation stack
        """

        self.trans_stack    = trans_stack
        self.group_ele_list = {}
        self.geo_ele_list   = []


    def add_group(self,
                  name: str):
        """ add a foil

        Args:
            name: name of the group
        """

        self.group_ele_list[name] = []
        self.geo_ele_list       = self.group_ele_list[name]

        self.trans_stack.save_stack()


    def close_group(self):
        """ close the current group
        """

        self.trans_stack.restore_stack()


    def add_geometry(self,
                     geo_ele: GEO_TYPES):
        """ add a 3D geometry element

        Args:
            geo_ele: geometry element
        """

        if geo_ele is not None:
            self.geo_ele_list.append(AllplanGeo.Transform(geo_ele, self.trans_stack.trans_matrix))


    def union(self,
              group1: (str | list[GEO_TYPES] | GEO_TYPES),
              group2: (str | list[GEO_TYPES] | GEO_TYPES)) -> GEO_TYPES:
        """ create a union from two groups

        Args:
            group1: first group of elements
            group2: second group of elements

        Returns:
            the union of the two groups or None if the union is not possible
        """

        #----------------- get the elements of the first group

        if isinstance(group1, str):
            group = self.group_ele_list[group1]

        elif not isinstance(group1, list):
            group = [group1]

        else:
            group = group1


        #----------------- add the elements of the second group

        if isinstance(group2, str):
            if group2:
                group += self.group_ele_list[group2]

        elif isinstance(group2, list):      # pylint: disable=confusing-consecutive-elif
            group += group2

        else:
            group.append(group2)


        #----------------- create the union

        union = group[0]

        for _geo_ele in group[1:]:
            if _geo_ele is None:
                continue

            union, geo_ele = self.__convert_to_brep(union, _geo_ele)

            if union is None or geo_ele is None:
                print("Union is not possible")
                break

            err, union = AllplanGeo.MakeUnion(union, geo_ele)       # type: ignore

            if err:
                print("Union is not possible")
                break

        return union


    def diff(self,
             group1: (str | list[GEO_TYPES] | GEO_TYPES),
             group2: (str | list[GEO_TYPES] | GEO_TYPES)) -> GEO_TYPES:
        """ create a diff from two groups

        Args:
            group1: first group of elements
            group2: second group of elements

        Returns:
            the difference of the two groups or None if the difference is not possible
        """

        if (diff := self.union(group1, "")) is None:
            return None

        if isinstance(group2, str):
            group2 = self.group_ele_list[group2]

        elif not isinstance(group2, list):
            group2 = [group2]                   # pylint: disable=use-tuple-over-list

        if group2 is None:
            return None

        for _geo_ele in group2:             # type: ignore
            if _geo_ele is None:
                continue

            diff, geo_ele = self.__convert_to_brep(diff, _geo_ele)

            if diff is None or geo_ele is None:
                print("Diff is not possible")
                break

            err, diff = AllplanGeo.MakeSubtraction(diff, geo_ele)    # type: ignore

            if err:
                print("Diff is not possible")
                break

        return diff


    def get_group_elements(self,
                           name: str) -> ListModelEle3D:
        """ get the group elements

        Args:
            name: name of the group

        Returns:
            the group elements
        """

        return self.group_ele_list[name]


    @staticmethod
    def __convert_to_brep(geo_ele1: GEO_TYPES,
                          geo_ele2: GEO_TYPES) -> tuple[GEO_TYPES, GEO_TYPES]:
        """ convert the geometry elements to BRep3D if necessary

        Args:
            geo_ele1: first geometry element
            geo_ele2: second geometry element

        Returns:
            tuple of converted geometry elements
        """

        if isinstance(geo_ele1, AllplanGeo.BRep3D) and isinstance(geo_ele2, AllplanGeo.Polyhedron3D):
            err, geo_ele2 = AllplanGeo.CreateBRep3D(geo_ele2)

            if err != AllplanGeo.eGeometryErrorCode.eOK:
                print("BooleanOperationUtil: BRep3D creation failed")
                return None, None

            return geo_ele1, geo_ele2


        if isinstance(geo_ele1, AllplanGeo.Polyhedron3D) and isinstance(geo_ele2, AllplanGeo.BRep3D):
            err, geo_ele1 = AllplanGeo.CreateBRep3D(geo_ele1)

            if err != AllplanGeo.eGeometryErrorCode.eOK:
                print("BooleanOperationUtil: BRep3D creation failed")
                return None, None

        return geo_ele1, geo_ele2

```

</details>