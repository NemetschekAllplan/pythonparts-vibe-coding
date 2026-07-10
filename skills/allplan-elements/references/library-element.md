---
name: allplan-elements-library-elements
description: Use this skill when you want to create a library element as a result of your script, and need to understand how to implement it correctly with the ALLPLAN API.
---


# Library Elements

`LibraryElement` represents elements stored in the ALLPLAN library: symbols (`.sym`), smart symbols / macros (`.nmk`), and fixtures (`.pfx` / `.lfx`). Unlike other basis elements it does **not** use a `GeometryObject` — it is fully described by a `LibraryElementProperties` object.

## Symbols and Smart Symbols

Provide the absolute path to the file and the element type:

```python
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Geometry as AllplanGeo

library_props = AllplanBasisElements.LibraryElementProperties(
    fullPathName    = r"C:\Data\Allplan\2025\std\Library\2D Objects\Cat.sym",
    elementType     = AllplanBasisElements.LibraryElementType.eSymbol,   # or eSmartSymbol for .nmk
    placementMatrix = AllplanGeo.Matrix3D())

library_element = AllplanBasisElements.LibraryElement(library_props)
```

To place the same symbol at multiple locations efficiently, pass a `Matrix3DList` instead of a single `Matrix3D`.

> **Tip:** Use `FileNameService.get_global_standard_path()` to resolve relative paths starting with keywords like `STD\Library\...` into absolute paths.

## Fixtures

### From the library (`.pfx` / `.lfx`)

Leave the first three constructor arguments empty and pass the path as the fourth:

```python
library_props = AllplanBasisElements.LibraryElementProperties(
    "", "", "", fixture_path,
    AllplanBasisElements.LibraryElementType.eFixtureSingleFile,
    AllplanGeo.Matrix3D())
```

### From the legacy catalog

Use the `path`, `group`, and `element` fields from a `FixtureProperties` object (obtained from a palette parameter):

```python
fixture = build_ele.Fixture.value  # FixtureProperties

library_props = AllplanBasisElements.LibraryElementProperties(
    path            = fixture.Path,
    group           = fixture.Group,
    element         = fixture.Element,
    elementType     = AllplanBasisElements.LibraryElementType.eFixture,
    placementMatrix = AllplanGeo.Matrix3D())
```

### Line and plane fixtures

After constructing the properties, specify the placement polyline before creating the element:

```python
polyline = AllplanGeo.Polyline3D()
polyline += AllplanGeo.Point3D(0, 0, 0)
polyline += AllplanGeo.Point3D(1500, 0, 0)
library_props.SetPolyline(polyline)

library_element = AllplanBasisElements.LibraryElement(library_props)
```

## As Part of a PythonPart

When a library element must be an integral part of a PythonPart (move together, modify together), do **not** put it directly into a PythonPart view. Instead, link it as a child via `PythonPartUtil`:

```python
pyp_util.add_library_elements(library_element)
```

If the PythonPart consists solely of a library element, add at least an invisible bounding box to the view so the user can still double-click to reactivate the PythonPart.
