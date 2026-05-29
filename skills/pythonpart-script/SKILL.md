---
name: pythonpart-script
description: >
  Use this skill when writing python code for a PythonPart. It covers the structure of the script,
  the Script Object contract, coding rules, and how to add input steps.
---

# Skill: PythonPart Script

## How the framework loads your script

The framework **never runs your script top-to-bottom**. It loads it as a Python module and then
calls specific functions or methods from it. This means:

- Do **not** put executable logic at module level — only imports, function definitions, and class definitions.
- The framework is the caller. Your job is to implement the functions/methods/classes it expects.

## Script Object contract

The **Script Object** is the default contract. It requires:

| What to implement | Type | Required |
|---|---|---|
| `check_allplan_version` | module-level function | yes |
| `create_script_object` | module-level function | yes |
| A class inheriting `BaseScriptObject` | class | yes |

### Minimal templates

See `templates/EntryPointFunctions.py` for a ready-to-copy file containing only the functions that the framework calls, and `templates/MyScriptObject.py` for a ready-to-copy script object class template. In a simple case, both can be implemented in the same file.

## Coding rules

- `check_allplan_version` and `create_script_object` are **module-level functions**, not methods.
- The script object class **must** inherit from `BaseScriptObject`.
- `execute()` is the **only mandatory method** to override. It must return `CreateElementResult`.
- Access parameter values via `self.build_ele.<ParameterName>.value`. The name must match the `<Name>` tag in the PYP file.
- Use `TYPE_CHECKING` guard for `BuildingElement` import — it is only needed for type hints, not at runtime.
- `AllplanGeometry` and `AllplanBasisElements` in the template are just examples. Remove them if not needed or add others as required - see 
- Never instantiate `DocumentAdapter` and `CoordinateInput` directly — use the ones provided by the framework via `self.document` and `self.coord_input`.

## Adding input steps

The Script Object contract allows adding interaction steps (point pick, element selection, etc.)
between the palette and element creation. Override `start_input()` to launch the first step and
`start_next_input()` for any subsequent ones.

### Point pick

```python
from ScriptObjectInteractors.PointInteractor import PointInteractor, PointInteractorResult

class MyPythonPart(BaseScriptObject):

    def start_input(self):
        self.point_result = PointInteractorResult()
        self.script_object_interactor = PointInteractor(self.point_result,
                                                        prompt_msg="Pick insertion point")

    def start_next_input(self):
        self.script_object_interactor = None   # no more steps after this

    def execute(self) -> CreateElementResult:
        insertion_point = self.point_result.point
        elements = ModelEleList()
        # ... use insertion_point ...
        return CreateElementResult(elements)
```

### Single element selection

```python
from ScriptObjectInteractors.SingleElementSelectInteractor import (
    SingleElementSelectInteractor, SingleElementSelectInteractorResult)

class MyPythonPart(BaseScriptObject):

    def start_input(self):
        self.sel_result = SingleElementSelectInteractorResult()
        self.script_object_interactor = SingleElementSelectInteractor(
            self.sel_result, prompt_msg="Select element")

    def start_next_input(self):
        self.script_object_interactor = None

    def execute(self) -> CreateElementResult:
        selected = self.sel_result.sel_element
        elements = ModelEleList()
        # ... process selected element ...
        return CreateElementResult(elements)
```

Set `self.script_object_interactor = None` in `start_next_input()` once there are no more steps.
The framework calls `execute()` only after all input steps are finished.

---

## Optional methods on BaseScriptObject

| Method | When called | Use it to |
|--------|------------|----------|
| `modify_element_property(page, name, value)` | user changes a palette value | react to palette changes, update other params |
| `on_control_event(build_ele, event_id)` | user presses a palette button | handle button actions |
| `on_cancel_function()` | user presses Escape | clean up, cancel the input |
| `start_input()` | after palette closes, before `execute()` | launch first interaction step |
| `start_next_input()` | after each interaction step completes | launch next step or set interactor to `None` |

