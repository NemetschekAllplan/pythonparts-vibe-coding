---
name: allplan-elements
description: This skill provides the foundational knowledge and high-level principles for defining native ALLPLAN elements (such as walls, lines, solids) within the ALLPLAN PythonParts framework.
---

## High-Level Principles

### 1. `AllplanElement` Base Class

In order to create anything within the PythonParts framework, the to-be-created-element must be an `AllplanElement` (or a class inheriting from it). Whether you are creating a multi-layer architectural wall, a simple 2D line, or a generic 3D solid, all classes representing these model components stem from the abstract `AllplanElement` base class. 

The API specializes `AllplanElement` into distinct branches:
- **Basis elements (`BasisElement`)**: Generic elements like lines, 3D-objects, hatchings, text, and library symbols.
- **Architecture (`ArchElement`)**: Native architectural elements like walls, slabs, beams, columns, and negative elements like window/door openings.
- **Precast (`PrecastElement`)**: Elements from the precast module (fixtures, assembly groups).
- **Reinforcement (`ReinfElement`)**: Components like rebars, meshes, and couplers.

### 2. Composition Over Inheritance (Geometry vs. Element)

A critical insight into the ALLPLAN API is that ALLPLAN entities **compose** geometry. They are not purely geometrical entities themselves.

It is not enough to define pure geometry (such as `Point3D`, `Line2D`, `Polyhedron3D`, or `BRep3D`). An element represents how that geometry should be processed and rendered in ALLPLAN.
For example:
- A wall (`WallElement`) **has** a geometry acting as its axis (usually a `Line2D` or `Arc2D`).
- A generic 3D solid (`ModelElement3D`) **has** a geometry defined as a `Polyhedron3D` or `BRep3D`.
- A simple 2D line (`ModelElement2D`) **has** a geometry object defined as just a `Line2D`.

Where geometry only handles spatial coordinates, the encapsulating **AllplanElement** defines specific components:
- **`CommonProperties`**: Defines the visual format representation (pen, stroke, color, layer).
- **Dedicated Property Classes**: An element typically pairs with property objects specific to its function (e.g., an `ArchElement` like `WallElement` uses `WallProperties` and `WallTierProperties` to handle thickness, tiers, and planes).

**Example: Creating a simple cuboid**

Pure geometry alone is not enough — it must be wrapped in an `AllplanElement`:

```python
import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Geometry as AllplanGeo

# 1. Define the pure geometry
cuboid_geometry = AllplanGeo.Polyhedron3D.CreateCuboid(1000, 500, 300)

# 2. Wrap it in an AllplanElement and assign CommonProperties
model_element = AllplanBasisElements.ModelElement3D()
model_element.GeometryObject   = cuboid_geometry
model_element.CommonProperties = AllplanSettings.AllplanGlobalSettings.GetCurrentCommonProperties()
```

`cuboid_geometry` is just a shape in space — no color, no pen, no layer. Only after it is assigned to `ModelElement3D` does it become a proper ALLPLAN element that can be placed in the drawing file.


## Defining Specific Objects

Due to this framework architecture, defining objects always separates the logic of generating pure geometry from wrapping it into native ALLPLAN entities.

Detailed instructions for each element category are in the following articles:

- **[Basis Elements](how-tos/basis-element.md)** — Generic drafting and modelling elements: 2D/3D lines, solids, text, hatchings, dimension lines. Covers which API class and geometry type to use for each ALLPLAN element.
- **[Library Elements](how-tos/library-element.md)** — Symbols, smart symbols, and fixtures from the ALLPLAN library. Covers path-based construction and how to attach them to a PythonPart.
- **[PythonPart Element](how-tos/pythonpart.md)** — Parametric containers built with `PythonPartUtil`. Covers views, placement matrix, attributes, hierarchy (structured PythonParts, child elements, groups), and key gotchas.
