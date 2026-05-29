"""This module contains the entry point functions that are called by the Allplan framework to interact with the Python part script object."""
from __future__ import annotations
from typing import TYPE_CHECKING

from BaseScriptObject import BaseScriptObject, BaseScriptObjectData

from BuildingElement import BuildingElement
from .MyScriptObject import MyPythonPart

def check_allplan_version(_build_ele: BuildingElement, version: float) -> bool:
    """Called by the framework to verify ALLPLAN version compatibility."""
    return float(version) >= 2025.0


def create_script_object(build_ele: BuildingElement,
                         script_object_data: BaseScriptObjectData) -> BaseScriptObject:
    """Called by the framework to instantiate the script object."""
    return MyPythonPart(build_ele, script_object_data)
