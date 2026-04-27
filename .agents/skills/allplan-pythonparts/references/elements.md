# Elements and Properties

## Canonical imports
```python
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
from CreateElementResult import CreateElementResult
from TypeCollections.ModelEleList import ModelEleList
```

## CommonProperties pattern
```python
com_prop = AllplanBaseEle.CommonProperties()
com_prop.GetGlobalProperties()
com_prop.Color = 6
com_prop.Pen = 1
```

## ModelEleList pattern
```python
model_list = ModelEleList()
model_list.append_geometry_3d(geometry_3d)
model_list.append_geometry_2d(geometry_2d)
# append(element) is valid for element objects (for example TextElement)
```

## Result return
```python
return CreateElementResult(model_list)
```

## Handles
- Use `HandleProperties` with explicit parameter mapping.
- Keep `move_handle` side-effect free except parameter update + rebuild.

## Attributes
- Prefer robust reads with fallbacks.
- For mixed adapters, use guarded access paths and explicit logging.
