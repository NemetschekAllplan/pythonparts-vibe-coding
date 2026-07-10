---
name: geometry-hidden-calculation
description: How to project 3D geometry into 2D visible/hidden lines using HiddenCalculus.
---

## Purpose

`HiddenCalculus` computes 2D line projections from 3D polyhedrons, separating visible edges from hidden (occluded) ones. Useful for generating 2D views/sections from 3D models.

## Requirements

- Input must be `Polyhedron3D`. Tessellate `BRep3D` first (see [tessellation.md](tessellation.md)).
- Output is `Line3D` (convert to `Line2D` manually).

## Setup

### 1. Configure Parameters

```python
params = AllplanGeo.HiddenCalculationParameters()
params.AdjacentEdgesMaxAngle = AllplanGeo.Angle.FromDeg(10)  # edges below this angle are hidden
params.SetObserverMatrix(
    eyePoint  = AllplanGeo.Point3D(0, 0, 0),
    viewPoint = AllplanGeo.Point3D(1, 1, -1))  # isometric from front-left
params.GetHiddenLines = True  # False = skip hidden lines (faster)
```

> Only isometric views are possible. No perspective projection.

### 2. Create Material (for tagging)

```python
material = AllplanGeo.HiddenMaterial()
```

Multiple materials can be created and assigned to different polyhedrons for later identification.

## Calculation

```python
calc = AllplanGeo.HiddenCalculus()
calc.Configure(params)

calc.AddElement(polyhedron_a, material, elementTag=0)
calc.AddElement(polyhedron_b, material, elementTag=1)

calc.Calculate()
```

## Retrieve Results

```python
for i in range(calc.GetLinesCount()):
    line_3d, visibility = calc.GetResultLine(i)   # Line3D + visible/hidden flag
    tag = calc.GetResultLineTag(i)                # integer tag from AddElement
    line_2d = AllplanGeo.Line2D(line_3d)          # convert to 2D
```

- `visibility`: indicates whether the line is visible or hidden behind another solid.
- `tag`: maps back to the source polyhedron (for assigning matching CommonProperties, etc.).

## Key Parameters

| Parameter | Effect |
|-----------|--------|
| `AdjacentEdgesMaxAngle` | Higher angle = fewer edges drawn. Edges between faces meeting below this angle are suppressed. |
| `GetHiddenLines` | Set `False` to skip hidden lines and reduce computation time. |
| Observer eye/view point | Defines the isometric viewing direction. |
