from BaseScriptObject import BaseScriptObject, BaseScriptObjectData
from BuildingElement import BuildingElement
from CreateElementResult import CreateElementResult


def check_allplan_version(_build_ele: BuildingElement, version: float) -> bool:
    return float(version) >= 2026.0


def create_script_object(build_ele: BuildingElement, data: BaseScriptObjectData) -> BaseScriptObject:
    return ScriptObjectTemplate(build_ele, data)


class ScriptObjectTemplate(BaseScriptObject):
    def __init__(self, build_ele: BuildingElement, data: BaseScriptObjectData):
        super().__init__(build_ele, data)

    def execute(self) -> CreateElementResult:
        return CreateElementResult()
