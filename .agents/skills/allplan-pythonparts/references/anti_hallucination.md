# Anti-Hallucination Rules

> **Read this BEFORE writing any Allplan PythonPart code.** Hallucinated API calls are the #1 failure mode.

## The Core Problem

The Allplan Python API (`NemAll_Python_*`) is proprietary. It is NOT part of standard Python or any open-source library. LLM training data contains almost no correct examples. This means:

- **Your Python knowledge does NOT transfer** to Allplan API method names
- **Guessing method names will fail** — Allplan uses unique naming conventions
- **A method that "sounds right" probably doesn't exist**

## Absolute Rules

### Rule 1: Only Use Verified API Calls

Every API call in generated code MUST come from one of these sources:
1. Templates and patterns in this skill
2. Project knowledge files (`01_OVERVIEW.md` through `10_UTILS_SETTINGS_MISC.md`)
3. Example `.py` files in project knowledge (`RoomArrange.py`, `BetonStuetze.py`, etc.)
4. The `PythonParts_API_Handbuch.md` handbook

If a method is not found in any of these sources, **do not use it**. Flag the gap to the user explicitly.

### Rule 2: Never Invent Convenience Methods

These are examples of methods that DO NOT EXIST but LLMs frequently hallucinate:

```python
# ❌ DOES NOT EXIST
AllplanGeo.Box3D(...)
AllplanGeo.Cylinder(...)
AllplanGeo.Sphere(...)
ModelEleList.add(...)
ModelEleList.append(...)          # It's append_geometry_3d() or append_geometry_2d()
Polyhedron3D.create_box(...)
Polyhedron3D.CreateBox(...)       # It's CreateCuboid()
AllplanGeo.CreateExtrusion(...)
AllplanBasisEle.TextElement(...)   # Constructor signatures differ
model_list.set_color(...)
model_list.set_pen(...)
build_ele.get_parameter(...)
```

### Rule 3: Never Guess Method Signatures

When you know a class exists but aren't sure about its methods:
1. Search project knowledge first
2. Check the example .py files for usage patterns
3. If still not found, tell the user: "I'm not certain this method exists — please verify against the API docs"

### Rule 4: Verify Parameter Names Match

The parameter name `<n>` in the PYP file MUST exactly match the Python access:

```xml
<!-- PYP -->
<Parameter>
    <n>Length</n>           <!-- This name... -->
    <Value>1000</Value>
    <ValueType>Length</ValueType>
</Parameter>
```

```python
# Python — must match exactly
length = build_ele.Length.value   # ✅ Correct
length = build_ele.length.value  # ❌ Case-sensitive!
length = build_ele.Laenge.value  # ❌ Wrong name!
```

### Rule 5: Units Are Always Millimeters

Allplan works internally in millimeters. All `Length` ValueType parameters are in mm.

```python
# ✅ Correct — 1 meter = 1000 mm
cube = AllplanGeo.Polyhedron3D.CreateCuboid(1000.0, 500.0, 3000.0)

# ❌ Wrong — this creates a 1mm cube
cube = AllplanGeo.Polyhedron3D.CreateCuboid(1.0, 0.5, 3.0)
```

### Rule 6: Import Aliases Are Fixed

Never use alternative aliases. These are the canonical ones:

| Module | Alias |
|--------|-------|
| `NemAll_Python_Geometry` | `AllplanGeo` |
| `NemAll_Python_BasisElements` | `AllplanBasisEle` |
| `NemAll_Python_BaseElements` | `AllplanBaseEle` |
| `NemAll_Python_ArchElements` | `AllplanArchEle` |
| `NemAll_Python_Reinforcement` | `AllplanReinf` |
| `NemAll_Python_IFW_Input` | `AllplanIFW` |
| `NemAll_Python_IFW_ElementAdapter` | `AllplanElementAdapter` |
| `NemAll_Python_AllplanSettings` | `AllplanSettings` |
| `NemAll_Python_Utility` | `AllplanUtil` |
| `NemAll_Python_Palette` | `AllplanPalette` |

Some examples also use longer aliases like `AllplanGeometry`, `AllplanBasisElements` — both are acceptable but the short forms above are preferred for consistency.

## Common Traps

### Trap: ModelEleList method names
```python
model_list = ModelEleList()
model_list.append_geometry_3d(polyhedron)   # ✅ For 3D geometry
model_list.append_geometry_2d(line2d)       # ✅ For 2D geometry
model_list.append(text_element)             # ✅ For elements (TextElement, etc.)
model_list.set_common_properties(com_prop)  # ✅ Sets properties for next elements
```

### Trap: Polyhedron3D.CreateCuboid signatures
```python
# ✅ Signature 1: dimensions from origin
AllplanGeo.Polyhedron3D.CreateCuboid(length, width, height)

# ✅ Signature 2: from two corner points
AllplanGeo.Polyhedron3D.CreateCuboid(
    AllplanGeo.Point3D(x1, y1, z1),
    AllplanGeo.Point3D(x2, y2, z2)
)
```

### Trap: Boolean operations return tuples
```python
# ✅ Always unpack the error code
err, result = AllplanGeo.MakeUnion(poly_a, poly_b)
err, result = AllplanGeo.MakeSubtraction(poly_a, poly_b)
err, result = AllplanGeo.MakeIntersection(poly_a, poly_b)

# ❌ Forgetting the error code
result = AllplanGeo.MakeUnion(poly_a, poly_b)  # Wrong!
```

### Trap: Transform is a free function
```python
# ✅ Correct — free function
transformed = AllplanGeo.Transform(geometry, matrix)

# ❌ Wrong — not a method on the geometry object
transformed = geometry.transform(matrix)
```

## When In Doubt

1. Search project knowledge files
2. Check example .py files for the exact usage pattern
3. Use the simplest verified alternative
4. Flag uncertainty explicitly to the user

**Never ship code with unverified API calls.** A compile error in Allplan means the entire PythonPart fails to load — there is no graceful fallback.