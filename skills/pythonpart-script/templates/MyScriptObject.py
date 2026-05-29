from BaseScriptObject import BaseScriptObject, BaseScriptObjectData
from CreateElementResult import CreateElementResult
from TypeCollections.ModelEleList import ModelEleList

import NemAll_Python_Geometry as AllplanGeometry
import NemAll_Python_BasisElements as AllplanBasisElements

class MyPythonPart(BaseScriptObject):
    """Script object implementation."""

    def __init__(self,
                 script_object_data: BaseScriptObjectData,
                 build_ele: BuildingElement):
        """Initialize

        Args:
            build_ele:  BuildingElement object containing parameter properties
        """
        super().__init__(script_object_data)
        self.build_ele = build_ele


    def execute(self) -> CreateElementResult:
        """Called by the framework to create the elements."""
        elements = ModelEleList()

        # --- build geometry here ---
        # Access parameters via self.build_ele, e.g.:
        #   width = self.build_ele.Width.value

        return CreateElementResult(elements)
