# Palette and PYP Reference

## Minimal PYP skeleton
```xml
<?xml version="1.0" encoding="utf-8"?>
<Element>
  <Script>
    <Name>MyPart.py</Name>
    <Title>My Part</Title>
    <Version>1.0</Version>
    <Interactor>False</Interactor>
    <ReadLastInput>True</ReadLastInput>
  </Script>
  <Page>
    <Name>Main</Name>
    <Text>Main</Text>
    <Parameters>
      <Parameter>
        <Name>Length</Name>
        <Text>Length</Text>
        <Value>1000</Value>
        <ValueType>Length</ValueType>
      </Parameter>
    </Parameters>
  </Page>
</Element>
```

## Required parameter fields
- `Name`
- `Value`
- `ValueType`

## Common optional fields
- `MinValue`, `MaxValue`
- `Visible`, `Enable`
- `ValueList`, `ValueTextList`
- `EventId`

## Dynamic layout blocks
- `Expander`
- `Row`
- `Separator`

## Binding rule
- PYP `<Name>X</Name>` must match Python access `build_ele.X.value` exactly.
- Case-sensitive, no fallback renaming.
