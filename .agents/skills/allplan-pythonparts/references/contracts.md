# Contract Types and Skeletons

Use this decision matrix first:

| Requirement | Contract | Required Entry Point | PYP `<Interactor>` |
|---|---|---|---|
| Parametric element from palette values | Standard PythonPart | `create_element` | `False` |
| Multi-step selection/workflow with framework support | Script Object | `create_script_object` + `BaseScriptObject.execute` | `False` |
| Real-time mouse-driven interaction and event loop | Interactor PythonPart | `create_interactor` + `BaseInteractor` | `True` |

## Standard PythonPart (minimum)
```python
from BuildingElement import BuildingElement
from CreateElementResult import CreateElementResult


def check_allplan_version(_build_ele: BuildingElement, version: float) -> bool:
    return float(version) >= 2026.0


def create_element(build_ele: BuildingElement, doc) -> CreateElementResult:
    del build_ele, doc
    return CreateElementResult()
```

## Script Object (minimum)
```python
from BaseScriptObject import BaseScriptObject, BaseScriptObjectData
from BuildingElement import BuildingElement
from CreateElementResult import CreateElementResult


def check_allplan_version(_build_ele: BuildingElement, version: float) -> bool:
    return float(version) >= 2026.0


def create_script_object(build_ele: BuildingElement, data: BaseScriptObjectData) -> BaseScriptObject:
    return MyScriptObject(build_ele, data)


class MyScriptObject(BaseScriptObject):
    def __init__(self, build_ele: BuildingElement, data: BaseScriptObjectData):
        super().__init__(build_ele, data)

    def execute(self) -> CreateElementResult:
        return CreateElementResult()
```

## Interactor (minimum)
```python
from BaseInteractor import BaseInteractor, BaseInteractorData


def check_allplan_version(_build_ele, version: float) -> bool:
    return float(version) >= 2026.0


def create_interactor(interactor_data: BaseInteractorData) -> "MyInteractor":
    return MyInteractor(interactor_data)


class MyInteractor(BaseInteractor):
    def __init__(self, interactor_data: BaseInteractorData):
        super().__init__(interactor_data)

    def process_mouse_msg(self, mouse_msg, pnt, msg_info):
        del mouse_msg, pnt, msg_info
        return True
```

## PYP rule
- Script Object: keep `<Interactor>False</Interactor>`.
- Interactor: use `<Interactor>True</Interactor>`.
- Standard: default to `<Interactor>False</Interactor>`.
