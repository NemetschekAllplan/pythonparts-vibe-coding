# Reinforcement Patterns

## Canonical import
```python
import NemAll_Python_Reinforcement as AllplanReinf
```

## Preferred framework helpers
- `GeneralReinfShapeBuilder`
- `LinearBarPlacementBuilder`
- `RotationUtil`

## Stable strategy
1. Build validated shape first.
2. Apply concrete cover (x/y/z explicit).
3. Place bars with deterministic spacing/count rule.
4. Apply rotation only after shape is verified.

## Common pitfalls
- Mixing incompatible placement rules in one logical reinforcement set.
- Implicit orientation assumptions across mirrored sides.
- Missing cover normalization after transform.

## Rule of thumb
- Start with standard builder paths; add freeform only after base version is stable.
