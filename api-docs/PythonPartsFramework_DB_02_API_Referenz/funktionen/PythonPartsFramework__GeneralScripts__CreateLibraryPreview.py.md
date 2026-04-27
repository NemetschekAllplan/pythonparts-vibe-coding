---
title: "CreateLibraryPreview"
source: "PythonPartsFramework\GeneralScripts\CreateLibraryPreview.py"
type: "module"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# CreateLibraryPreview

> **Pfad:** `PythonPartsFramework\GeneralScripts\CreateLibraryPreview.py`  
> **Typ:** Modul  
> **Tags:** `script`

## Übersicht

This script generates library preview for PythonPart

## Abhängigkeiten

- `BaseScriptObject`
- `BuildingElement`
- `BuildingElementComposite`
- `BuildingElementControlProperties`
- `BuildingElementMaterialStringTable`
- `BuildingElementService`
- `BuildingElementStringTable`
- `BuildingElementUtil`
- `ControlPropertiesUtil`
- `CreateElementResult`
- `DeleteObsoleteFiles`
- `DocumentManager`
- `ImportHook`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_IFW_ElementAdapter`
- `NemAll_Python_IFW_Input`
- `TestHelper.Mock.CoordinateInputMock`
- `TraceService`
- `TypeCollections.ModelEleList`
- `TypeCollections.ModificationElementList`
- `collections.abc`
- `dataclasses`
- `sys`
- `traceback`
- `typing`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `create_library_preview(file_name: str, document: AllplanEleAdapter.DocumentAdapter, used_for_import: bool)`

Create preview objects for PythonPart

Args:
    file_name:       the name of the XML file.
    document:        the document adapter.
    used_for_import: used for import state

Returns:
    created preview state, created script

**Parameter:**
- `file_name: str`
- `document: AllplanEleAdapter.DocumentAdapter`
- `used_for_import: bool`

**Rückgabe:** `tuple[bool, Any]`

**Beispiel:**
```python
result = create_library_preview(..., ..., ...)
```

### `__initialize_control_properties(build_ele_list: list[BuildingElement], build_ele_ctrl_props_list: list[BuildingElementControlProperties], build_ele_script: object, document: AllplanEleAdapter.DocumentAdapter)`

initialize the control properties

Args:
    build_ele_list:            list with the building elements
    build_ele_ctrl_props_list: list with the building element control properties
    build_ele_script:          building element script
    document:                  the document

Returns:
    success state

**Parameter:**
- `build_ele_list: list[BuildingElement]`
- `build_ele_ctrl_props_list: list[BuildingElementControlProperties]`
- `build_ele_script: object`
- `document: AllplanEleAdapter.DocumentAdapter`

**Rückgabe:** `bool`

**Beispiel:**
```python
result = __initialize_control_properties(..., ..., ..., ...)
```

### `__create_preview_elements(used_for_import: bool, build_ele_list: list[BuildingElement], build_ele_ctrl_props_list: list[BuildingElementControlProperties], build_ele_composite: BuildingElementComposite, build_ele_script: object, document: AllplanEleAdapter.DocumentAdapter)`

create the preview elements

Args:
    used_for_import:           used for import state
    build_ele_list:            list with the building elements
    build_ele_ctrl_props_list: list with the building element control properties
    build_ele_composite:       building element composite with the building element constraints
    build_ele_script:          building element script
    document:                  the document

Returns:
    the preview elements

**Parameter:**
- `used_for_import: bool`
- `build_ele_list: list[BuildingElement]`
- `build_ele_ctrl_props_list: list[BuildingElementControlProperties]`
- `build_ele_composite: BuildingElementComposite`
- `build_ele_script: object`
- `document: AllplanEleAdapter.DocumentAdapter`

**Rückgabe:** `list[Any] | CreateElementResult`

**Beispiel:**
```python
result = __create_preview_elements(..., ..., ..., ..., ..., ...)
```

### `__script_object_preview(build_ele_list: list[BuildingElement], build_ele_ctrl_props_list: list[BuildingElementControlProperties], build_ele_script: object, document: AllplanEleAdapter.DocumentAdapter)`

create the library preview from a script object

Args:
    build_ele_list:            list with the building elements
    build_ele_ctrl_props_list: list with the building element control properties
    build_ele_script:          building element script
    document:                  the document

Returns:
    created elements for the preview

**Parameter:**
- `build_ele_list: list[BuildingElement]`
- `build_ele_ctrl_props_list: list[BuildingElementControlProperties]`
- `build_ele_script: object`
- `document: AllplanEleAdapter.DocumentAdapter`

**Rückgabe:** `CreateElementResult`

**Beispiel:**
```python
result = __script_object_preview(..., ..., ..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" This script generates library preview for PythonPart
"""

# pylint: disable=bare-except
# pylint: disable=not-callable

from typing import Any, cast

import sys
import traceback

import dataclasses

from collections.abc import Callable

# pylint: disable=unused-import
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter              # needed for document (call from C++)
# pylint: enable=unused-import

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_Input as AllplanIFW

from BaseScriptObject import BaseScriptObject, BaseScriptObjectData
from BuildingElement import BuildingElement
from BuildingElementComposite import BuildingElementComposite
from BuildingElementControlProperties import BuildingElementControlProperties
from BuildingElementUtil import BuildingElementUtil
from BuildingElementService import BuildingElementService
from BuildingElementMaterialStringTable import BuildingElementMaterialStringTable
from BuildingElementStringTable import BuildingElementStringTable
from CreateElementResult import CreateElementResult
from ControlPropertiesUtil import ControlPropertiesUtil
from DocumentManager import DocumentManager
from TraceService import TraceService
from DeleteObsoleteFiles import delete_obsolete_files
from ImportHook import ImportHookFinder

from TypeCollections.ModelEleList import ModelEleList
from TypeCollections.ModificationElementList import ModificationElementList

from TestHelper.Mock.CoordinateInputMock import CoordinateInputMock

sys.meta_path.append(ImportHookFinder)

def create_library_preview(file_name      : str,
                           document       : AllplanEleAdapter.DocumentAdapter,
                           used_for_import: bool) -> tuple[bool, Any]:
    """ Create preview objects for PythonPart

    Args:
        file_name:       the name of the XML file.
        document:        the document adapter.
        used_for_import: used for import state

    Returns:
        created preview state, created script
    """

    TraceService(True)

    delete_obsolete_files()

    DocumentManager.get_instance().document = document
    DocumentManager.get_instance().clear_pythonpart_element()

    path                       = AllplanSettings.AllplanPaths.GetPythonPartsEtcPath()
    string_table_path          = path + '\\PythonPartsFramework\\GeneralScripts\\Stringtable\\BuildingElement.pyp'
    material_string_table_path = path + '\\PythonPartsFramework\\GeneralScripts\\Stringtable\\BuildingElementMaterial.pyp'

    language = AllplanSettings.AllplanLocalisationService.AllplanLanguage()

    str_table          = BuildingElementStringTable(string_table_path, False, language)
    material_str_table = BuildingElementMaterialStringTable(material_string_table_path, False, language)


    #------------------ Read the building element

    result, build_ele_script, build_ele_list, build_ele_ctrl_props_list, build_ele_composite, _, file_name = \
        BuildingElementService().read_data_from_pyp(file_name, str_table, True, material_str_table)

    if not result or not build_ele_script or not build_ele_list or not build_ele_ctrl_props_list:
        return False, build_ele_script


    #------------------ Import the script

    if (build_ele_script := BuildingElementUtil.import_building_element_script(build_ele_list[0], False)) is None:
        return False, build_ele_script

    if not __initialize_control_properties(build_ele_list, build_ele_ctrl_props_list, build_ele_script, document):
        return False, build_ele_script


    #------------------ Execute the element creation

    if not (preview_ele_list := __create_preview_elements(used_for_import, build_ele_list, build_ele_ctrl_props_list,
                                                          build_ele_composite, build_ele_script, document)):
        return False, build_ele_script


    #------------------ Create element in document

    if not preview_ele_list:
        return False, build_ele_script

    if dataclasses.is_dataclass(preview_ele_list):
        AllplanBaseEle.CreateElements(document, AllplanGeo.Matrix3D(), cast(CreateElementResult, preview_ele_list).elements,
                                      ModificationElementList(), None)

    elif isinstance(preview_ele_list[0], list):
        AllplanBaseEle.CreateElements(document, AllplanGeo.Matrix3D(), preview_ele_list[0],
                                      ModificationElementList(), None)

    else:
        return False, build_ele_script

    return True, build_ele_script


def __initialize_control_properties(build_ele_list           : list[BuildingElement],
                                    build_ele_ctrl_props_list: list[BuildingElementControlProperties],
                                    build_ele_script         : object,
                                    document                 : AllplanEleAdapter.DocumentAdapter) -> bool:
    """ initialize the control properties

    Args:
        build_ele_list:            list with the building elements
        build_ele_ctrl_props_list: list with the building element control properties
        build_ele_script:          building element script
        document:                  the document

    Returns:
        success state
    """

    if (init_ctrl__prop := getattr(build_ele_script, "initialize_control_properties", None)) is None:
        return True

    try:                        # pylint: disable=too-many-try-statements
        if build_ele_list and len(build_ele_list) == 1:
            init_ctrl__prop(build_ele_list[0],ControlPropertiesUtil(build_ele_ctrl_props_list, build_ele_list), document)
        else:
            init_ctrl__prop(build_ele_list, ControlPropertiesUtil(build_ele_ctrl_props_list, build_ele_list), document)

        return True

    except:
        traceback.print_exc()

        return False


def __create_preview_elements(used_for_import          : bool,
                              build_ele_list           : list[BuildingElement],
                              build_ele_ctrl_props_list: list[BuildingElementControlProperties],
                              build_ele_composite      : BuildingElementComposite,
                              build_ele_script         : object,
                              document                 : AllplanEleAdapter.DocumentAdapter) -> (list[Any] | CreateElementResult):
    """ create the preview elements

    Args:
        used_for_import:           used for import state
        build_ele_list:            list with the building elements
        build_ele_ctrl_props_list: list with the building element control properties
        build_ele_composite:       building element composite with the building element constraints
        build_ele_script:          building element script
        document:                  the document

    Returns:
        the preview elements
    """

    node_script_key = "nodescript.py"

    is_node_script = build_ele_list[0].script_name.lower() == node_script_key

    try:                                # pylint: disable=too-many-try-statements
        if used_for_import and is_node_script:
            node_script = build_ele_script.create_elements(None, build_ele_list,                                # type: ignore
                                                           build_ele_composite, build_ele_ctrl_props_list)

            return [node_script.create_elements()]


        #----------------- PythonPart with special preview

        if (preview_fct := getattr(build_ele_script, "create_preview", None)):
            if len(build_ele_list) > 1:
                if not is_node_script:
                    build_ele_composite.connect_building_element_values(build_ele_list)

                return preview_fct(build_ele_list, build_ele_composite, document)

            return preview_fct(build_ele_list[0], document)


        #----------------- standard PythonPart

        if (create_element := getattr(build_ele_script, "create_element", None)):
            if len(build_ele_list) == 1:
                return create_element(build_ele_list[0], document)

            build_ele_composite.connect_building_element_values(build_ele_list)

            return create_element(build_ele_list, build_ele_composite, document)


        #----------------- script object

        return __script_object_preview(build_ele_list, build_ele_ctrl_props_list, build_ele_script, document)

    except:
        traceback.print_exc()

    return []


def __script_object_preview(build_ele_list           : list[BuildingElement],
                            build_ele_ctrl_props_list: list[BuildingElementControlProperties],
                            build_ele_script         : object,
                            document                 : AllplanEleAdapter.DocumentAdapter) -> CreateElementResult:
    """ create the library preview from a script object

    Args:
        build_ele_list:            list with the building elements
        build_ele_ctrl_props_list: list with the building element control properties
        build_ele_script:          building element script
        document:                  the document

    Returns:
        created elements for the preview
    """

    if (create_script_object := getattr(build_ele_script, "create_script_object", None)) is None:
        return CreateElementResult()

    script_object_data = BaseScriptObjectData(cast(AllplanIFW.CoordinateInput, CoordinateInputMock(document)),
                                              ModificationElementList(),
                                              True, AllplanSettings.ExecutionEvent.eCreation,
                                              AllplanGeo.Matrix3D(),
                                              ControlPropertiesUtil(build_ele_ctrl_props_list,
                                                                    build_ele_list),
                                              cast(Callable, None),
                                              cast(Callable, None),
                                              {})

    script_object = cast(BaseScriptObject, create_script_object(build_ele_list[0], script_object_data))

    return script_object.create_library_preview()

```

</details>