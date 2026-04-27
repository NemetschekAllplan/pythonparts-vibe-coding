# Pattern: Dynamic Palette Controls

Source: `input/Hochregallager.pyp`

## Why it matters
- Shows practical `Visible` and `Enable` expressions.
- Uses grouped options via `Expander` blocks.

## Reusable pattern
- Use `CheckBox` parameter as controlling switch.
- Guard dependent values with both `Visible` and `Enable`.
- Keep min/max bounds explicit for numeric parameters.

## Validation note
- Every dependent parameter still requires a safe default in Python.
