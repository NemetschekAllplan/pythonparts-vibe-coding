# Pattern: Standard PythonPart with Structured Parameters

Source: `input/Hochregallager.py` + `input/Hochregallager.pyp`

## Why it matters
- Demonstrates robust `build_ele` parameter reading with defaults.
- Uses one central class to collect parameters and create geometry.
- Applies guarded creation with fallback `CreateElementResult()`.

## Reusable pattern
1. Read all palette params once in `__init__`.
2. Normalize optional list/string parameters immediately.
3. Keep geometry append helper small and side-effect free.
4. Wrap `create_element` in top-level try/except with traceback output.

## Risk note
- Keep API calls verified; avoid introducing non-documented helper methods.
