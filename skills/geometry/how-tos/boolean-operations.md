---
name: geometry-boolean-operations
description: How to perform boolean operations (union, subtraction, intersection) on solids.
---

## General Rules

- Cannot mix `Polyhedron3D` and `BRep3D` in one operation. Either:
  - Tessellate all BReps → polyhedrons (lossy), or
  - Convert all polyhedrons → BReps with `AllplanGeo.CreateBRep3D()` (lossless).
- Functions return `(error_code, result)` — always check the error.

## Intersection (Intersect)

Computes the overlapping volume of two solids.

```python
intersecting, result = AllplanGeo.Intersect(first_polyhedron, second_polyhedron)
```

- `intersecting`: `bool` — `True` if solids overlap (useful for collision detection without needing the result geometry).
- Works with: two polyhedrons, two BReps, or one BRep + one polyhedron.

**With typed lists** — treat each list as a single united body:

```python
from TypeCollections.PolyhedronTypesList import PolyhedronTypesList

list_a = PolyhedronTypesList()
list_a += [poly1, poly2]

list_b = PolyhedronTypesList()
list_b += [poly3]

intersecting, result = AllplanGeo.Intersect(list_a, list_b)
```

## Union (MakeUnion)

Joins multiple solids into one.

```python
polyhedrons = AllplanGeo.Polyhedron3DList()
polyhedrons += [first, second, third]

result, united = AllplanGeo.MakeUnion(polyhedrons)
```

**Union with voids** — join positives, then subtract negatives in one step:

```python
result, united = AllplanGeo.MakeUnion(positive_list, negative_list)
```

For BReps, use `AllplanGeo.BRep3DList()` instead.

## Subtraction (MakeSubtraction)

Subtracts one or more solids from a base solid.

```python
err, result = AllplanGeo.MakeSubtraction(minuend, subtrahend)
```

Subtract multiple at once:

```python
from TypeCollections.PolyhedronTypesList import PolyhedronTypesList

subtrahends = PolyhedronTypesList()
subtrahends += [hole1, hole2]

err, result = AllplanGeo.MakeSubtraction(base_polyhedron, subtrahends)
```

## All-in-One (MakeBoolean)

Computes all four boolean operations between two polyhedrons in a single call:

```python
err, intersection, union, sub_a_minus_b, sub_b_minus_a = \
    AllplanGeo.MakeBoolean(polyhedron_a, polyhedron_b)
```

Use when you need multiple results from the same pair — avoids redundant computation.
