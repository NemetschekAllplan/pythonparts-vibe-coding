# Geometry Controls

These value types create input controls for geometry objects. The framework automatically converts the string stored in `<Value>` into an actual geometry object from `NemAll_Python_Geometry`.

> **Default value format:** The `<Value>` must be a string representation of the geometry object (e.g. `Point3D(0,0,0)`). To generate this string from an existing object, use `Utils.GeometryStringValueConverter`.

## Reference table

| `<ValueType>` | Python type (`.value`) | Default value example |
|---|---|---|
| `Point2D` | `Point2D` | `Point2D(1000,500)` |
| `Point3D` | `Point3D` | `Point3D(0,0,0)` |
| `Vector2D` | `Vector2D` | `Vector2D(2000,200)` |
| `Vector3D` | `Vector3D` | `Vector3D(2000,200,1000)` |
| `AxisPlacement3D` | `AxisPlacement3D` | `AxisPlacement3D(Origin(0,0,0)XDirection(1,0,0)ZDirection(0,0,1))` |
| `Line2D` | `Line2D` | `Line2D(1000,1100,5000,1500)` |
| `Line3D` | `Line3D` | `Line3D(1000,6100,0,5000,6500,1000)` |
| `Arc2D` | `Arc2D` | see example below |
| `Arc3D` | `Arc3D` | see example below |
| `Circle2D` | `Arc2D` (full circle) | `Circle2D(CenterPoint(10000,0)MajorRadius(1000))` |
| `Circle3D` | `Arc3D` (full circle) | `Circle3D(CenterPoint(10000,5000,1000)ZAxis(0,0,1)MajorRadius(1000))` |

## Examples

### Point3D

```xml
<Parameter>
    <Name>InsertionPoint</Name>
    <Text>Insertion point</Text>
    <Value>Point3D(0,0,0)</Value>
    <ValueType>Point3D</ValueType>
</Parameter>
```

```python
import NemAll_Python_Geometry as AllplanGeo

point: AllplanGeo.Point3D = self.build_ele.InsertionPoint.value
```

### AxisPlacement3D

```xml
<Parameter>
    <Name>Placement</Name>
    <Text>Placement</Text>
    <Value>AxisPlacement3D(Origin(0,0,0)XDirection(1,0,0)ZDirection(0,0,1))</Value>
    <ValueType>AxisPlacement3D</ValueType>
</Parameter>
```

### Line2D

```xml
<Parameter>
    <Name>Axis</Name>
    <Text>Axis</Text>
    <Value>Line2D(0,0,5000,0)</Value>
    <ValueType>Line2D</ValueType>
</Parameter>
```

### Arc2D

```xml
<Parameter>
    <Name>Arc</Name>
    <Text>Arc</Text>
    <Value>Arc2D(CenterPoint(7000, 0) MinorRadius(1000) MajorRadius(2000) AxisAngle(0.785) StartAngle(0.785) EndAngle(4.712) IsCounterClockwise(1))</Value>
    <ValueType>Arc2D</ValueType>
</Parameter>
```

### Arc3D

```xml
<Parameter>
    <Name>Arc3D</Name>
    <Text>Arc</Text>
    <Value>Arc3D(CenterPoint(7000, 5000, 1000) XDirection(1, 0, 0) ZAxis(0, 0, 1) MinorRadius(1000) MajorRadius(2000) AxisAngle(0.785) StartAngle(0.785) EndAngle(4.712) IsCounterClockwise(1))</Value>
    <ValueType>Arc3D</ValueType>
</Parameter>
```
