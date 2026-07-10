# Dialog Controls

These parameters render a button in the palette. Clicking it opens a secondary selection dialog. The `<ValueDialog>` tag specifies which dialog opens.

## Library / symbol picker

Lets the user select a symbol, smart symbol, or fixture from the ALLPLAN library. Result is a file path `str`.

```xml
<Parameter>
    <Name>SymbolPath</Name>
    <Text>Symbol</Text>
    <Value></Value>
    <ValueType>String</ValueType>
    <ValueDialog>SymbolDialog</ValueDialog>
</Parameter>
```

| `<ValueDialog>` value | Filters for |
|---|---|
| `SymbolDialog` | Symbols only |
| `FixtureDialog` | Fixtures (point, line, area) |
| `SmartSymbolDialog` | Smart symbols (macros) |
| `OpeningSymbolDialog` | Smart symbols and SmartParts |

> The result may be an absolute path or a relative path with a keyword (`etc`, `std`, `usr`, `prj`). To resolve a relative path to an absolute one, use `FileNameService.FileNameService.get_global_standard_path`.

```python
from FileNameService import FileNameService

abs_path = FileNameService.get_global_standard_path(self.build_ele.SymbolPath.value)
```

---

## Trade

Opens an ALLPLAN trade selection dialog. Result is an `int` (trade ID).

```xml
<Parameter>
    <Name>TradeID</Name>
    <Text>Trade</Text>
    <Value>0</Value>
    <ValueType>Integer</ValueType>
    <ValueDialog>Trade</ValueDialog>
</Parameter>
```

---

## RGB colour

Opens a colour picker dialog for an arbitrary RGB colour. Result is an `int` encoding `0xRRGGBB`.

```xml
<Parameter>
    <Name>LineColor</Name>
    <Text>Color</Text>
    <Value>255</Value>
    <ValueType>Integer</ValueType>
    <ValueDialog>RGBColorDialog</ValueDialog>
</Parameter>
```

To extract channels and construct an `ARGB` object:

```python
import NemAll_Python_BasisElements as AllplanBasisElements

rgb = self.build_ele.LineColor.value
color = AllplanBasisElements.ARGB(
    red   = (rgb >> 16) & 255,
    green = (rgb >> 8) & 255,
    blue  = rgb & 255,
    alpha = 0
)
```

---

## Attribute selection

Opens an attribute selection dialog. Result is an `int` (attribute ID).

```xml
<Parameter>
    <Name>AttrID</Name>
    <Text>Attribute</Text>
    <Value>0</Value>
    <ValueType>Integer</ValueType>
    <ValueDialog>AttributeSelection</ValueDialog>
</Parameter>
```

| `<ValueDialog>` value | Limitation |
|---|---|
| `AttributeSelection` | All attributes |
| `AttributeSelectionInsert` | Insert attributes (additional to default object attributes) |
| `AttributeSelectionProject` | Project attributes only |

---

## Bitmap picker

Opens a bitmap resource browser. Result is the **full file path** as a `str`.

```xml
<Parameter>
    <Name>BitmapPath</Name>
    <Text>Bitmap</Text>
    <Value></Value>
    <ValueType>String</ValueType>
    <ValueDialog>BitmapResourceDialog</ValueDialog>
</Parameter>
```

---

## Plane references

Opens a plane definition dialog. Result is a `PlaneReferences` object. Choose the dialog variant based on which reference planes the PythonPart needs:

```xml
<!-- Top plane only -->
<Parameter>
    <Name>TopPlane</Name>
    <Text>Top plane</Text>
    <Value></Value>
    <ValueType>PlaneReferences</ValueType>
    <ValueDialog>TopPlaneReferences</ValueDialog>
</Parameter>

<!-- Bottom plane only -->
<Parameter>
    <Name>BottomPlane</Name>
    <Text>Bottom plane</Text>
    <Value></Value>
    <ValueType>PlaneReferences</ValueType>
    <ValueDialog>BottomPlaneReferences</ValueDialog>
</Parameter>

<!-- Both planes -->
<Parameter>
    <Name>Planes</Name>
    <Text>Planes</Text>
    <Value></Value>
    <ValueType>PlaneReferences</ValueType>
    <ValueDialog>PlaneReferences</ValueDialog>
</Parameter>
```

> If your PythonPart creates a PythonPart element, plane references are saved in it and the element **will be updated** when a referenced plane changes. Ensure that re-activating the PythonPart and immediately pressing Escape results in a clean script termination to avoid ALLPLAN getting stuck.
