# Input and Selection

## Canonical imports
```python
import NemAll_Python_IFW_Input as AllplanIFW
import NemAll_Python_IFW_ElementAdapter as AllplanElementAdapter
```

## Coordinate input rule
- Use framework-compatible prompt wrappers where required (`InputStringConvert`).
- Normalize input objects defensively before using `X/Y/Z` values.

## Selection rule
- Selection order is not guaranteed.
- Normalize selected elements to consistent root adapters before write-back operations.
- Avoid broad child-delete behavior in architecture-heavy contexts unless verified.

## Script Object interaction
- Use `SingleElementSelectInteractor` / other interactor helpers for step-wise flow.
- If no interactive placement is desired, write directly to document and return empty `CreateElementResult()`.
