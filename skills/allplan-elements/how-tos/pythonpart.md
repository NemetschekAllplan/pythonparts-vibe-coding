---
name: allplan-elements-pythonparts
description: Use this skill when you want to create a parametric PythonPart element as a result of your script, and need to understand how to implement it correctly with the ALLPLAN API.
---

# PythonPart Element

A **PythonPart** as a model element is a parametric container that encapsulates `AllplanElements` (e.g. `ModelElement3D`, `ModelElement2D`). Its defining feature is that the user can double-click it to reactivate the script in modification mode — changing parameters and regenerating the geometry in-place.

## Internal Structure

Internally a PythonPart mirrors a smart object (macro) and is composed of three entities:

| Entity | API class | Responsibility |
|---|---|---|
| **Placement** | `MacroPlacementElement` | Positions the definition in global space via `Matrix3D`; carries `CommonProperties` and `Attributes` |
| **Definition** | `MacroElement` | Owns the views; identified by a unique hash computed from the parameter values |
| **View** | (managed by `PythonPartUtil`) | Holds the nested model elements; can be shown/hidden by scale or drawing type |

You never construct `MacroPlacementElement` or `MacroElement` directly. Use `PythonPartUtil` instead.

## Creating a PythonPart — Minimal Example

```python
from PythonPartUtil import PythonPartUtil

pyp_util = PythonPartUtil()                            # optional: pass CommonProperties to control placement appearance
pyp_util.add_pythonpart_view_2d3d(model_elements)      # add elements to a view visible in all contexts
python_part = pyp_util.create_pythonpart(build_ele)    # returns a list [MacroPlacementElement, MacroElement]

return CreateElementResult(elements=python_part)
```

`build_ele` is the `BuildingElement` carrying all parameter values. It is required so the framework can compute the hash and link palette attributes.

## Views

A PythonPart can have multiple views with different geometry. Views are added via three methods on `PythonPartUtil`:

| Method | Visible in |
|---|---|
| `add_pythonpart_view_2d3d(elements)` | Always (ground view and isometric) |
| `add_pythonpart_view_2d(elements)` | Ground view only |
| `add_pythonpart_view_3d(elements)` | Isometric view only |

### Scale-dependent visibility

Pass a `PythonPartViewData` object to control at which scale a view is shown:

```python
from PythonPartViewData import PythonPartViewData

detailed_view_data = PythonPartViewData()
detailed_view_data.start_scale = 1    # show from 1:1
detailed_view_data.end_scale   = 50   # … down to 1:50

simplified_view_data = PythonPartViewData()
simplified_view_data.start_scale = 51
simplified_view_data.end_scale   = 200

pyp_util.add_pythonpart_view_2d3d(detailed_elements,   view_data=detailed_view_data)
pyp_util.add_pythonpart_view_2d3d(simplified_elements, view_data=simplified_view_data)
```

### Drawing type-dependent visibility

```python
view_data = PythonPartViewData()
view_data.all_drawing_types = False
view_data.drawing_types = [AllplanBaseElements.DrawingTypeService.DefaultDrawingTypes.eDesignDrawing]

pyp_util.add_pythonpart_view_2d3d(elements, view_data=view_data)
```

## Placement Matrix

To place the PythonPart at a specific position or orientation, pass a `Matrix3D` to `create_pythonpart`:

```python
python_part = pyp_util.create_pythonpart(build_ele, placement_matrix=my_matrix)
```

Prefer controlling position here rather than transforming individual model elements inside the view.

## Attributes

To store computed values as ALLPLAN attributes on the PythonPart placement, use `BuildingElementAttributeList`:

```python
from BuildingElementAttributeList import BuildingElementAttributeList

attribute_list = BuildingElementAttributeList()
attribute_list.add_attribute(221, width)   # attribute @221@ = width
pyp_util.add_attribute_list(attribute_list)
```

Parameters defined in the PYP file with an attribute ID are linked automatically — no need to add them again manually.

## Hierarchy

When a PythonPart consists of sub-elements that need their own attributes (e.g. for quantity take-off), introduce a hierarchy.

### Structured PythonPart (element nodes)

Use `ElementNodeElement` to give each sub-element its own identity, attributes, and position in the hierarchy. Each node requires a deterministically generated UUID (use `uuid.uuid5` with `uuid.NAMESPACE_OID`):

```python
import uuid
import NemAll_Python_BasisElements as AllplanBasisElements

box_1_uuid = uuid.uuid5(uuid.NAMESPACE_OID, "Box_1")
box_2_uuid = uuid.uuid5(uuid.NAMESPACE_OID, "Box_2")

node_1 = AllplanBasisElements.ElementNodeElement(box_1_uuid, [box_1_model_element])
node_2 = AllplanBasisElements.ElementNodeElement(box_2_uuid, [box_2_model_element])

# For nested hierarchy: make node_2 a child of node_1
node_2.SetParentID(box_1_uuid)

pyp_util.add_pythonpart_view_2d3d([node_1, node_2])
```

### Child elements (linked, not encapsulated)

Architecture components, reinforcement, library elements, and fixtures must be **linked** to the PythonPart, not placed inside a view. Use the dedicated methods:

| Child element type | Method |
|---|---|
| Architecture element | `pyp_util.add_architecture_elements(elements)` |
| Reinforcement | `pyp_util.add_reinforcement_elements(elements)` |
| Library element | `pyp_util.add_library_elements(elements)` |
| Fixture | `pyp_util.add_fixture_elements(elements)` |

> **Important:** Never put reinforcement, architecture elements, or library elements directly into a view. They will appear correct on creation, but changes made with native ALLPLAN tools will be lost when the PythonPart is reactivated.

### PythonPart group

Multiple PythonParts can be grouped so the user interacts with them as one, while ALLPLAN treats them as separate elements (useful for invoicing individual parts of an assembly):

```python
from PythonPart.PythonPartGroup import PythonPartGroup

group = PythonPartGroup.from_build_ele(build_ele)
group.add(python_part_a)
group.add(python_part_b)
model_ele_list = group.create()
```

## Display Name

Assign a human-readable name so users can identify the PythonPart type in the viewport tooltip and object manager:

```python
python_part = pyp_util.create_pythonpart(build_ele, display_name="My Custom Beam")
```

## What to Keep in Mind

- **Always pass `build_ele`** to `create_pythonpart` — the hash and attribute links depend on it.
- **One `PythonPartUtil` per PythonPart** — do not reuse the same instance for multiple independent PythonParts.
- **Attributes live on the placement**, not on individual model elements inside views. Reports and legends only see placement attributes.
- **The hash determines identity** — PythonParts with the same hash are considered identical, and ALLPLAN will offer to update all of them when one is modified. Exclude irrelevant parameters (e.g. rotation) with `<ExcludeIdentical>True</ExcludeIdentical>` in the PYP file.
