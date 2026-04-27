import traceback

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanElementAdapter

from BuildingElement import BuildingElement
from CreateElementResult import CreateElementResult
from TypeCollections.ModelEleList import ModelEleList


def check_allplan_version(_build_ele: BuildingElement, version: float) -> bool:
    return float(version) >= 2026.0


def create_element(build_ele: BuildingElement, _doc: AllplanElementAdapter.DocumentAdapter) -> CreateElementResult:
    try:
        length = float(getattr(getattr(build_ele, "Length", None), "value", 1000.0))
        width = float(getattr(getattr(build_ele, "Width", None), "value", 500.0))
        height = float(getattr(getattr(build_ele, "Height", None), "value", 2500.0))

        length = max(10.0, length)
        width = max(10.0, width)
        height = max(10.0, height)

        body = AllplanGeo.Polyhedron3D.CreateCuboid(length, width, height)
        model_list = ModelEleList()
        model_list.append_geometry_3d(body)
        return CreateElementResult(model_list)
    except Exception:
        traceback.print_exc()
        return CreateElementResult()
