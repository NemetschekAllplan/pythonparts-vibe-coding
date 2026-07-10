---
name: allplan-elements-basis-elements
description: Use this skill when you want to create a basis element as a result of your script, and need to understand how to implement it correctly with the ALLPLAN API.
---

`BasisElement` is the abstract base for all generic ALLPLAN drafting and modelling elements — lines, 3D objects, text, hatchings, dimension lines, and more. Every concrete basis element class inherits from it and, through it, from `AllplanElement`.

## Choosing the Right Class and Geometry

The table below maps common ALLPLAN elements to their Python API class and the required geometry type. **The geometry type is not optional** — assigning the wrong geometry to an element class will either fail silently or produce unexpected results.

| ALLPLAN element          | API class                  | Required geometry                          |
|--------------------------|----------------------------|--------------------------------------------|
| 3D object (solid)        | `ModelElement3D`           | `Polyhedron3D`                             |
| General 3D object (BRep) | `ModelElement3D`           | `BRep3D`                                   |
| 3D line                  | `ModelElement3D`           | `Line3D`                                   |
| 2D line                  | `ModelElement2D`           | `Line2D`                                   |
| Circle / arc             | `ModelElement2D`           | `Arc2D`                                    |
| Text                     | `TextElement`              | position point (set via `TextProperties`)  |
| Filling                  | `FillingElement`           | closed 2D curve                            |
| Hatching                 | `HatchingElement`          | closed 2D curve                            |
| Dimension line           | `DimensionLineElement`     | dimension points + direction               |
| Elevation point          | `ElevationElement`         | inherits from `DimensionLineElement`       |
| Library symbol / macro   | `LibraryElement`           | see [library-element.md](library-element.md) |
| Point symbol             | `Symbol2DElement`          | —                                          |
| Terrain point            | `Symbol3DElement`          | —                                          |
| Pattern                  | `PatternElement`           | —                                          |

## What to Keep in Mind

### Every element needs `CommonProperties`
`CommonProperties` controls the visual appearance of the element in the viewport: pen weight, stroke style, color, and layer. Always assign it explicitly. The safest approach is to take the user's currently active settings:

```python
import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Geometry as AllplanGeo

element = AllplanBasisElements.ModelElement3D()
element.GeometryObject   = AllplanGeo.Polyhedron3D.CreateCuboid(1000, 500, 300)
element.CommonProperties = AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties()
```

### `ModelElement3D` vs `ModelElement2D` — determined by geometry, not intent
The same class (`ModelElement3D`) represents both a 3D solid and a 3D line. What makes the difference is the geometry you assign:
- `Polyhedron3D` or `BRep3D` → ALLPLAN treats it as a 3D object.
- `Line3D` → ALLPLAN treats it as a 3D line.

Likewise, `ModelElement2D` is used for 2D lines (`Line2D`) and circles/arcs (`Arc2D`).

### Element-specific properties
Some elements carry a dedicated properties object beyond `CommonProperties`:

- `TextElement` → has `TextProperties` (font, alignment, width, height, ...).
- `FillingElement` → has `FillingProperties` (fill colors, pattern, ...).
- `DimensionLineElement` → has `DimensionProperties` (point symbol, text location, text offset, ...).
- `LibraryElement` → constructed entirely through `LibraryElementProperties` — see [library-element.md](library-element.md).

These properties are aggregated by the element (not owned — you can share the same properties object across multiple elements).

### Returning elements
A completed basis element can be placed in the drawing file in two ways:

1. **Via `CreateElementResult`** (script object / standard PythonPart):
   ```python
   return CreateElementResult(elements=[element])
   ```
2. **Via `PythonPartTransaction.execute()`** (interactor):
   ```python
   transaction.execute(model_ele_list=[element], ...)
   ```
