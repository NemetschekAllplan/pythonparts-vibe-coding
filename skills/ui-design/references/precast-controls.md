# Precast Controls

## Catalog references

The `xxxCatalogReference` value types create combo boxes pre-populated with values from ALLPLAN Precast module catalogs. The framework reads catalog values automatically at palette creation time. The result type is `str` for all variants except `PrecastElementTypeCatalogReference`.

| `<ValueType>` | Precast catalog | Result type |
|---|---|---|
| `FactoryCatalogReference` | Factory Catalogs | `str` |
| `NormCatalogReference` | Standards Catalog | `str` |
| `ConcreteGradeCatalogReference` | Concrete Grade Catalog | `str` |
| `FixtureCatalogReference` | Fixture Catalog | `str` |
| `InsulationCatalogReference` | Insulation Material Catalog | `str` |
| `BrickTileCatalogReference` | Brick/Tile Catalog | `str` |
| `PrecastElementTypeCatalogReference` | Element type catalog | `int` |

```xml
<Parameter>
    <Name>ConcreteGrade</Name>
    <Text>Concrete grade</Text>
    <ValueType>ConcreteGradeCatalogReference</ValueType>
</Parameter>

<Parameter>
    <Name>Insulation</Name>
    <Text>Insulation</Text>
    <ValueType>InsulationCatalogReference</ValueType>
</Parameter>
```

---

## Fixture

Shows three linked combo boxes for selecting a fixture: path, file, and element. Returns a `NemAll_Python_Palette.FixtureProperties` object.

```xml
<Parameter>
    <Name>Fixture</Name>
    <Text>Fixture</Text>
    <Value>FixtureProperties(PathShortcut(Office)Group(Deckendosen)Element(E-Dose groß))</Value>
    <ValueType>Fixture</ValueType>
</Parameter>
```

The `PathShortcut` value controls the base directory:

| `PathShortcut` | Directory |
|---|---|
| `Office` | `std` (office standard) |
| `Project` | `prj` (current project) |
| `Private` | `usr` (user's private directory) |
