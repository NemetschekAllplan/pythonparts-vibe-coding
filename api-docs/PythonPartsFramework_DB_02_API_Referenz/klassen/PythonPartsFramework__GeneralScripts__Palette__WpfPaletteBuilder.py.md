---
title: "WpfPaletteBuilder"
source: "PythonPartsFramework\GeneralScripts\Palette\WpfPaletteBuilder.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# WpfPaletteBuilder

> **Pfad:** `PythonPartsFramework\GeneralScripts\Palette\WpfPaletteBuilder.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

implementation of the wpf palette builder that is used to add controls to the palette

## Abhängigkeiten

- `NemAll.Python.Palette.WPF.ViewModel`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_ArchElements`
- `NemAll_Python_Geometry`
- `NemAll_Python_Palette`
- `NemAll_Python_Utility`
- `WpfPaletteBuilderUtils`
- `WpfPaletteChangeHandler`
- `__future__`
- `clr`
- `typing`

## Klassen

### `WpfPaletteBuilder`

implementation of the palette builder
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, cpp_palette_builder: AllplanPalette.PythonWpfPaletteBuilder` | `None` | initialize  Args:     cpp_palette_builder: cpp palette builder |
| `AddAngleValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add an angle value to the palette  Args:     description:     Description     name:            Value name     value:           Value     page:            Page index     expander_name:   Expander section name     row_name:        Name of the row     b_enabled:       Control is enabled: true/false     min_value:       Minimal value     max_value:       Maximal value     interval_value:  Interval value for the slider     as_slider:       Show as slider: true/false     height:          Control height, only used for a row     width:           Control width, only used for a row     font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `AddAreaFixtureCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add an area fixture precast catalog reference  Args:     description:     Description     name:            Value name     value:           Value string     page:            Page index     expander_name:   Expander section name     row_name:        Name of the row     b_enabled:       Control is enabled: true/false     height:          Control height, only used for a row     width:           Control width, only used for a row     font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddAreaValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add an area value to the palette  Args:     description:     Description     name:            Value name     value:           Value     page:            Page index     expander_name:   Expander section name     row_name:        Name of the row     b_enabled:       Control is enabled: true/false     min_value:       Minimal value     max_value:       Maximal value     interval_value:  Interval value for the slider     as_slider:       Show as slider: true/false     height:          Control height, only used for a row     width:           Control width, only used for a row     font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `AddBarDiameter` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a bar diameter value to the palette  Args:     description:     Description     name:            Value name     value:           Value     page:            Page index     expander_name:   Expander section name     row_name:        Name of the row     b_enabled:       Control is enabled: true/false     height:          Control height, only used for a row     width:           Control width, only used for a row     font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddBendingRollerValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a bending roller value to the palette  Args:     description:     Description     name:            Value name     value:           Value     page:            Page index     expander_name:   Expander section name     row_name:        Name of the row     b_enabled:       Control is enabled: true/false     height:          Control height, only used for a row     width:           Control width, only used for a row     font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddBrickTileCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a brick/tile reference  Args:     description:     Description     name:            Value name     value:           Value string     page:            Page index     expander_name:   Expander section name     row_name:        Name of the row     b_enabled:       Control is enabled: true/false     height:          Control height, only used for a row     width:           Control width, only used for a row     font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddButton` | `self, description: str, name: str, event_id: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_style: int, font_face_code: int` | `None` | Add a button to the palette  Args:     description:    Description     name:           Value name     event_id:       Value holds the event ID pressing the button     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_style:     Font size: 0=small, 1=extra small, 2=large     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddCheckboxValue` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a checkbox value to the palette  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddColorValue` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a color value to the palette  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddComboBoxValue` | `self, description: str, name: str, value: str, list_values: str, value_type: AllplanPalette.PaletteValueType, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList, is_editable: bool` | `None` | Add a combo box value to the palette  Args:     description:      Description     name:             Value name     value:            Value     list_values:      List values     value_type:       Value type     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color     is_editable:      Is editable state |
| `AddConcreteCoverValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a concrete cover value to the palette  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddConcreteGrade` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a concrete grade value to the palette  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddConcreteGradeCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a concrete grade reference  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddDoubleValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add a double value to the palette  Args:     description:      Description     name:             Value name     value:            Value     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     min_value:        Minimal value     max_value:        Maximal value     interval_value:   Interval value for the slider     as_slider:        Show as slider: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `AddFaceStyleValue` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a face style combobox to the palette  Args:     description:    Description     name:           ID name     value:          Selected value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddFactoryCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a factory precast catalog reference  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddFixtureCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a fixture precast catalog reference - all, only point, line or area  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddFixtureValues` | `self, description_path: str, description_group: str, description_element: str, name: str, fixture: AllplanPalette.FixtureProperties, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add the fixture values  Args:     description_path:    Description of the path value     description_group:   Description of the group value     description_element: Description of the element value     name:                Value name     fixture:             Properties of the fixture     page:                Page index     expander_name:       Expander section name     row_name:            Name of the row     b_enabled:           Control is enabled: true/false     height:              Control height, only used for a row     width:               Control width, only used for a row     font_face_code:      Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddHatchValue` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a hatch combobox to the palette  Args:     description:    Description     name:           ID name     value:          Selected value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddInsulationCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add an insulation reference  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddIntValue` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add an integer value to the palette  Args:     description:      Description     name:             Value name     value:            Value     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     min_value:        Minimal value     max_value:        Maximal value     interval_value:   Interval value for the slider     as_slider:        Show as slider: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `AddLayer` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a layer value to the palette  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddLengthValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add a length value to the palette  Args:     description:      Description     name:             Value name     value:            Value     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     min_value:        Minimal value     max_value:        Maximal value     interval_value:   Interval value for the slider     as_slider:        Show as slider: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `AddLineFixtureCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a line fixture precast catalog reference - all, only point, line or area  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddMaterialButton` | `self, description: str, name: str, value: str, button_type: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a material button to the palette  Args:     description:    Description     name:           Value name     value:          String of material     button_type:    Button type (0: simple material button, 1: mat button + switch off button)     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddMeshGroup` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a mesh group value to the palette  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddMeshType` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, mesh_group: int, height: int, width: int, font_face_code: int` | `None` | Add a mesh type value to the palette  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     mesh_group:     Mesh group     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddMultiMaterialLayoutCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `int` | Add a multi-material layout catalog reference  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline  Returns:     int: The result of adding the multi-material layout catalog reference |
| `AddNormCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a norm catalog reference  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPage` | `self, name: str, description: str` | `None` | Add a page to the palette  Args:     name:         ID name     description:  Description text (localized) |
| `AddPatternValue` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a pattern combobox to the palette  Args:     description:    Description     name:           ID name     value:          Selected value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPenValue` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a pen value to the palette  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPicture` | `self, description: str, name: str, picture_name: str, lib_path: str, orientation: AllplanPalette.Orientation, page: int, expander_name: str, row_name: str, height: int, width: int` | `None` | Add a picture to the palette  Args:     description:    Description used for the tooltip     name:           ID name     picture_name:   Name of the picture     lib_path:       Library path     orientation:    Orientation (0:LEFT, 1:MIDDLE, 2:RIGHT)     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     height:         Control height     width:          Weighted width of control if it is in the row, or width of the image if it is the only control in the row |
| `AddPictureButton` | `self, description: str, name: str, value: str, event_id: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a picture button to the palette  Args:     description:    Description     name:           Value name     value:          Value     event_id:       Value holds the event ID pressing the button     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPictureButtonList` | `self, description: str, name: str, value: int, picture_path: str, picture_list: str, value_list: str, text_list: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a picture button list to the palette  Args:     description:    Description     name:           Value name     value:          Value holds the selected picture button in buttons     picture_path:   Path of pictures     picture_list:   Picture list holds the images for the buttons - example: a.png|b.png|c.png     value_list:     Value list of possible values - example: 0|1|2     text_list:      Text list for the tooltips     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPictureComboBox` | `self, description: str, name: str, value: int, picture_path: str, picture_list: str, value_list: str, text_list: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a picture combobox to the palette  Args:     description:    Description     name:           Value name     value:          Value holds the selected picture button in buttons     picture_path:   Path of pictures     picture_list:   Picture list holds the images for the buttons - example: a.png|b.png|c.png     value_list:     Value list of possible values - example: 0|1|2     text_list:      Text list for the tooltips     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPictureResourceButton` | `self, description: str, name: str, value: int, event_id: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a picture button to the palette  Args:     description:    Description     name:           Value name     value:          Value holds the resource ID     event_id:       Value holds the event ID pressing the button     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPictureResourceButtonList` | `self, description: str, name: str, value: int, picture_list: str, value_list: str, text_list: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a picture resource button list to the palette  Args:     description:    Description     name:           Value name     value:          Value holds the selected picture button in buttons     picture_list:   Picture list holds the images for the buttons - example: 16433|16441|16449     value_list:     Value list of possible values - example: 0|1|2     text_list:      Text list for the tooltips     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPictureResourceComboBox` | `self, description: str, name: str, value: int, picture_list: str, value_list: str, text_list: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a picture resource combobox to the palette  Args:     description:    Description     name:           Value name     value:          Value holds the selected picture button in buttons     picture_list:   Picture list holds the images for the buttons - example: 16433|16441|16449     value_list:     Value list of possible values - example: 0|1|2     text_list:      Text list for the tooltips     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPictureResourceToggleButton` | `self, description: str, name: str, value: int, picture_list: str, value_list: str, text_list: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a picture toggle button to the palette  Args:     description:    Description     name:           Value name     value:          Value holds the selected picture button in buttons     picture_list:   Picture list holds the images for the buttons - example: a.png|b.png|c.png     value_list:     Value list of possible values - example: 0|1|2     text_list:      Text list for the tooltips     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPlaneReferencesButton` | `self, description: str, name: str, plane_refs: AllplanArchEle.BasePlaneReferences, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a plane references button to the palette  Args:     description:    Description     name:           Value name     plane_refs:     Plane references     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPointFixtureCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a point fixture precast catalog reference - all, only point, line or area  Args:     description:    Description     name:           Value name     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddConstructionPointSymbolValue` | `self, description: str, name: str, value: int, value_list: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a point symbol combobox to the palette  Args:     description:    Description     name:           ID name     value:          Selected value     value_list:     Pipe separated list of point symbol types     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddPrecastElementTypeCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `str` | Add a precast element type catalog reference  Args:     description:    Description     name:           Value name     value:          Value     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline  Returns:     str: The result of adding the precast element type catalog reference |
| `AddRadioButton` | `self, radio_button_group_description: str, radio_button_group_name: str, radio_button_description: str, value: object, selected_value_in_group: object, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a radio button to the palette  Args:     radio_button_group_description: Radio button group description     radio_button_group_name:        Radio button group ID name     radio_button_description:       Radio button description     value:                          Double value of this radio button     selected_value_in_group:        Selected value of radio button group     page:                           Page index     expander_name:                  Expander section name     row_name:                       Name of the row     b_enabled:                      Control is enabled: true/false     height:                         Control height, only used for a row     width:                          Control width, only used for a row     font_face_code:                 Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddRefPointButton` | `self, description: str, name: str, ref_point_position: AllplanPalette.RefPointPosition, ref_point_type: AllplanPalette.RefPointButtonType, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a reference point button to the palette  Args:     description:        Description     name:               Value name     ref_point_position: Reference point ID (1,...,9)     ref_point_type:     Reference point type     page:               Page index     expander_name:      Expander section name     row_name:           Name of the row     b_enabled:          Control is enabled: true/false     height:             Control height, only used for a row     width:              Control width, only used for a row     font_face_code:     Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddResourcePicture` | `self, description: str, name: str, picture_resource_id: int, page: int, expander_name: str, row_name: str, height: int, width: int` | `None` | Add a picture from a resource to the palette  Args:     description:        Description used for the tooltip     name:               ID name     picture_resource_id: Resource id of the picture     page:               Page index     expander_name:      Expander section name     row_name:           Name of the row     height:             Control height, only used for a row     width:              Control width, only used for a row |
| `AddSeparator` | `self, page: int, expander_name: str` | `None` | Add a separator to the palette  Args:     page:          Page index     expander_name: Expander section name |
| `AddSteelGrade` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a steel grade value to the palette  Args:     description:   Description     name:          Value name     value:         Value     page:          Page index     expander_name: Expander section name     row_name:      Name of the row     b_enabled:     Control is enabled: true/false     height:        Control height, only used for a row     width:         Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddStringValue` | `self, description: str, name: str, str_value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add a string value to the palette  Args:     description:      Description     name:             Value name     str_value:        String     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `AddStroke` | `self, description: str, name: str, value: int, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a stroke value to the palette  Args:     description:   Description     name:          Value name     value:         Value     page:          Page index     expander_name: Expander section name     row_name:      Name of the row     b_enabled:     Control is enabled: true/false     height:        Control height, only used for a row     width:         Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddSurfaceCatalogRef` | `self, description: str, name: str, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Add a surface catalog reference  Args:     description:   Description     name:          Value name     value:         Value string     page:          Page index     expander_name: Expander section name     row_name:      Name of the row     b_enabled:     Control is enabled: true/false     height:        Control height, only used for a row     width:         Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddText` | `self, description: str, value: str, orientation: AllplanPalette.Orientation, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_style: int, font_face_code: int` | `None` | Add a text  Args:     description:   Description     value:         Value     orientation:   Orientation     page:          Page index     expander_name: Expander section name     row_name:      Name of the row     b_enabled:     Control is enabled: true/false     height:        Control height, only used for a row     width:         Control width, only used for a row     font_style:    Font size: 0=small, 1=extra small, 2=large     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `AddVolumeValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add a volume value to the palette  Args:     description:      Description     name:             Value name     value:            Value     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     min_value:        Minimal value     max_value:        Maximal value     interval_value:   Interval value for the slider     as_slider:        Show as slider: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `AddWeightValue` | `self, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add a weight value to the palette  Args:     description:      Description     name:             Value name     value:            Value     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     min_value:        Minimal value     max_value:        Maximal value     interval_value:   Interval value for the slider     as_slider:        Show as slider: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `IsConcreteCoverPaletteUpdate` | `self, cover: float` | `bool` | Check for a palette update due to a new concrete cover  Args:     cover: Concrete cover  Returns:     Palette update: true/false |
| `Reset` | `self` | `None` | Reset the data          |
| `set_base_viewmodel_properties` | `parameter_viewmodel: SimpleParameterViewModel, description: str, name: str, b_enabled: bool, height: int, width: int, tooltip: str` | `None` | Sets the basic properties that are common for all parameter view models.  Args:     parameter_viewmodel: The parameter view model instance.     description:         The description of the parameter.     name:                The name of the parameter.     b_enabled:           Indicates whether the control is enabled.     height:              The height of the control.     width:               The width of the control.     tooltip:             The tooltip text for the control. |
| `_add_double_type_value` | `self, double_type: DoubleValueType, description: str, name: str, value: float, page: int, expander_name: str, row_name: str, b_enabled: bool, min_value: float, max_value: float, interval_value: float, as_slider: bool, height: int, width: int, font_face_code: int, background_color: list[int] | AllplanUtil.VecIntList` | `None` | Add a double type value to the palette  Args:     double_type:      Type of the double value (double, length...)     description:      Description     name:             Value name     value:            Value     page:             Page index     expander_name:    Expander section name     row_name:         Name of the row     b_enabled:        Control is enabled: true/false     min_value:        Minimal value     max_value:        Maximal value     interval_value:   Interval value for the slider     as_slider:        Show as slider: true/false     height:           Control height, only used for a row     width:            Control width, only used for a row     font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline     background_color: Background color of the control as red, green, blue |
| `_add_string_combobox` | `self, description: str, name: str, values_list: Any, value: str, page: int, expander_name: str, row_name: str, b_enabled: bool, height: int, width: int, font_face_code: int` | `None` | Helper method to add a string combobox to the palette.  Args:     description:    Description     name:           Value name     values_list:    List of values as a managed List     value:          Value string     page:           Page index     expander_name:  Expander section name     row_name:       Name of the row     b_enabled:      Control is enabled: true/false     height:         Control height, only used for a row     width:          Control width, only used for a row     font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline |
| `_register_update_callback` | `self, parameter_viewmodel: ValueParameterViewModel, page: int` | `None` | Registers the handler for value change events of the parameter view model.  Args:     parameter_viewmodel: The parameter view model instance.     page:                Page index where the parameter is located. |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the wpf palette builder that is used to add controls to the palette
"""

# pylint: disable=invalid-name
# pylint: disable=too-many-positional-arguments
# pylint: disable=too-many-public-methods

from __future__ import annotations

from typing import Any

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_ArchElements as AllplanArchEle
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Palette as AllplanPalette
import NemAll_Python_Utility as AllplanUtil

from .WpfPaletteBuilderUtils import WpfPaletteBuilderUtils
from .WpfPaletteChangeHandler import WpfPaletteChangeHandler

import clr # pylint: disable=wrong-import-order

python_palette_dll_path = f"{AllplanSettings.AllplanPaths.GetPathOfApplication()}\\NemAll_Python_Palette_WPF.dll"

clr.AddReference(python_palette_dll_path)  # pylint: disable=no-member  # type: ignore

from NemAll.Python.Palette.WPF.ViewModel import ( # pylint: disable=import-error, wrong-import-position, wrong-import-order  # type: ignore
    CheckboxParameterViewModel,
    ColorComboboxViewModel,
    ContructionPointSymbolViewModel,
    DoubleEditComboboxViewModel,
    DoubleEditParameterViewModel,
    DoubleSliderParameterViewModel,
    DoubleValueType,
    FaceStyleComboboxViewModel,
    HatchComboboxViewModel,
    IntegerComboboxViewModel,
    IntegerEditComboboxViewModel,
    IntegerEditParameterViewModel,
    IntegerSliderParameterViewModel,
    LayerComboboxViewModel,
    MaterialButtonParameterViewModel,
    PatternComboboxViewModel,
    PenComboboxViewModel,
    PictureButtonGroupParameterViewModel,
    PictureButtonParameterViewModel,
    PictureComboboxParameterViewModel,
    PictureParameterViewModel,
    PictureToggleButtonParameterViewModel,
    PythonPaletteResourceProvider,
    PythonPaletteViewModelBuilder,
    RadioButtonParameterViewModel,
    RefPointButtonParameterViewModel,
    ReinforcementResourceComboboxViewModel,
    SimpleParameterViewModel,
    StringComboboxViewModel,
    StringEditComboboxViewModel,
    StringEditParameterViewModel,
    StrokeComboboxViewModel,
    TextButtonParameterViewModel,
    TextParameterViewModel,
    ValueParameterViewModel
)

class WpfPaletteBuilder:
    """ implementation of the palette builder
    """

    def __init__(self,
                 cpp_palette_builder : AllplanPalette.PythonWpfPaletteBuilder):
        """ initialize

        Args:
            cpp_palette_builder: cpp palette builder
        """

        self.cpp_palette_builder = cpp_palette_builder
        self.view_model_builder = PythonPaletteViewModelBuilder.Instance
        self.change_handler = WpfPaletteChangeHandler()
        self._event_handlers = []

    def AddAngleValue(self,
                      description     : str,
                      name            : str,
                      value           : float,
                      page            : int,
                      expander_name   : str,
                      row_name        : str,
                      b_enabled       : bool,
                      min_value       : float,
                      max_value       : float,
                      interval_value  : float,
                      as_slider       : bool,
                      height          : int,
                      width           : int,
                      font_face_code  : int,
                      background_color: (list[int] | AllplanUtil.VecIntList)):
        """Add an angle value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expander_name:   Expander section name
            row_name:        Name of the row
            b_enabled:       Control is enabled: true/false
            min_value:       Minimal value
            max_value:       Maximal value
            interval_value:  Interval value for the slider
            as_slider:       Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        if isinstance(value, AllplanGeo.Angle):
            value = value.Deg

        self.cpp_palette_builder.AddAngleValue(description,
                                               name,
                                               value,
                                               page,
                                               expander_name,
                                               row_name,
                                               b_enabled,
                                               min_value,
                                               max_value,
                                               interval_value,
                                               as_slider,
                                               height,
                                               width,
                                               font_face_code,
                                               background_color)

        # values for view models need to be converted to rad
        # the exception are min and max values for editbox, they are expected in deg

        value_converted          = WpfPaletteBuilderUtils.convert_angle_to_palette_units(value)
        min_value_converted      = WpfPaletteBuilderUtils.convert_angle_to_palette_units(min_value) if as_slider else min_value
        max_value_converted      = WpfPaletteBuilderUtils.convert_angle_to_palette_units(max_value) if as_slider else max_value
        interval_value_converted = WpfPaletteBuilderUtils.convert_angle_to_palette_units(interval_value)

        self._add_double_type_value(DoubleValueType.Angle, description, name, value_converted, page, expander_name, row_name, b_enabled,
                                    min_value_converted, max_value_converted, interval_value_converted, as_slider,
                                    height, width, font_face_code, background_color)

    def AddAreaFixtureCatalogRef(self,
                                 description    : str,
                                 name           : str,
                                 value          : str,
                                 page           : int,
                                 expander_name  : str,
                                 row_name       : str,
                                 b_enabled      : bool,
                                 height         : int,
                                 width          : int,
                                 font_face_code : int):
        """Add an area fixture precast catalog reference

        Args:
            description:     Description
            name:            Value name
            value:           Value string
            page:            Page index
            expander_name:   Expander section name
            row_name:        Name of the row
            b_enabled:       Control is enabled: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddAreaFixtureCatalogRef(description,
                                                          name,
                                                          value,
                                                          page,
                                                          expander_name,
                                                          row_name,
                                                          b_enabled,
                                                          height,
                                                          width,
                                                          font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetAreaFixtureCatalogValues(),
                                  value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddAreaValue(self,
                     description      : str,
                     name             : str,
                     value            : float,
                     page             : int,
                     expander_name    : str,
                     row_name         : str,
                     b_enabled        : bool,
                     min_value        : float,
                     max_value        : float,
                     interval_value   : float,
                     as_slider        : bool,
                     height           : int,
                     width            : int,
                     font_face_code   : int,
                     background_color : (list[int] | AllplanUtil.VecIntList)):
        """Add an area value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expander_name:   Expander section name
            row_name:        Name of the row
            b_enabled:       Control is enabled: true/false
            min_value:       Minimal value
            max_value:       Maximal value
            interval_value:  Interval value for the slider
            as_slider:       Show as slider: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        self.cpp_palette_builder.AddAreaValue(description,
                                              name,
                                              value,
                                              page,
                                              expander_name,
                                              row_name,
                                              b_enabled,
                                              min_value,
                                              max_value,
                                              interval_value,
                                              as_slider,
                                              height,
                                              width,
                                              font_face_code,
                                              background_color)

        self._add_double_type_value(DoubleValueType.Area, description, name, value, page, expander_name, row_name, b_enabled,
                                   min_value, max_value, interval_value, as_slider, height, width, font_face_code, background_color)

    def AddBarDiameter(self,
                       description    : str,
                       name           : str,
                       value          : float,
                       page           : int,
                       expander_name  : str,
                       row_name       : str,
                       b_enabled      : bool,
                       height         : int,
                       width          : int,
                       font_face_code : int):
        """Add a bar diameter value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expander_name:   Expander section name
            row_name:        Name of the row
            b_enabled:       Control is enabled: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddBarDiameter(description,
                                                name,
                                                value,
                                                page,
                                                expander_name,
                                                row_name,
                                                b_enabled,
                                                height,
                                                width,
                                                font_face_code)

        combobox_view_model = ReinforcementResourceComboboxViewModel()

        PythonPaletteResourceProvider.InitializeBarDiameterCombobox(combobox_view_model, value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddBendingRollerValue(self,
                              description    : str,
                              name           : str,
                              value          : float,
                              page           : int,
                              expander_name  : str,
                              row_name       : str,
                              b_enabled      : bool,
                              height         : int,
                              width          : int,
                              font_face_code : int):
        """Add a bending roller value to the palette

        Args:
            description:     Description
            name:            Value name
            value:           Value
            page:            Page index
            expander_name:   Expander section name
            row_name:        Name of the row
            b_enabled:       Control is enabled: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddBendingRollerValue(description,
                                                       name,
                                                       value,
                                                       page,
                                                       expander_name,
                                                       row_name,
                                                       b_enabled,
                                                       height,
                                                       width,
                                                       font_face_code)

        combobox_view_model = DoubleEditComboboxViewModel(DoubleValueType.Double)

        combobox_view_model.IsEditable = False

        combobox_view_model.InitializeValues(PythonPaletteResourceProvider.GetBendingRollerValues(), value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddBrickTileCatalogRef(self,
                               description    : str,
                               name           : str,
                               value          : str,
                               page           : int,
                               expander_name  : str,
                               row_name       : str,
                               b_enabled      : bool,
                               height         : int,
                               width          : int,
                               font_face_code : int):
        """Add a brick/tile reference

        Args:
            description:     Description
            name:            Value name
            value:           Value string
            page:            Page index
            expander_name:   Expander section name
            row_name:        Name of the row
            b_enabled:       Control is enabled: true/false
            height:          Control height, only used for a row
            width:           Control width, only used for a row
            font_face_code:  Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddBrickTileCatalogRef(description,
                                                        name,
                                                        value,
                                                        page,
                                                        expander_name,
                                                        row_name,
                                                        b_enabled,
                                                        height,
                                                        width,
                                                        font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetBrickTileCatalogValues(),
                                  value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddButton(self,
                  description    : str,
                  name           : str,
                  event_id       : int,
                  page           : int,
                  expander_name  : str,
                  row_name       : str,
                  b_enabled      : bool,
                  height         : int,
                  width          : int,
                  font_style     : int,
                  font_face_code : int):
        """Add a button to the palette

        Args:
            description:    Description
            name:           Value name
            event_id:       Value holds the event ID pressing the button
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_style:     Font size: 0=small, 1=extra small, 2=large
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddButton(description,
                                           name,
                                           event_id,
                                           page,
                                           expander_name,
                                           row_name,
                                           b_enabled,
                                           height,
                                           width,
                                           font_style,
                                           font_face_code)

        button_view_model = TextButtonParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(button_view_model, description, name, b_enabled, height, width, "")

        button_view_model.SetSimplifiedButtonText(description)
        button_view_model.FontConfiguration.ConfigureFromFlags(font_face_code, font_style)

        self.view_model_builder.AddParameterToPalette(button_view_model, page, expander_name, row_name, font_face_code)

    def AddCheckboxValue(self,
                         description    : str,
                         name           : str,
                         value          : int,
                         page           : int,
                         expander_name  : str,
                         row_name       : str,
                         b_enabled      : bool,
                         height         : int,
                         width          : int,
                         font_face_code : int):
        """Add a checkbox value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddCheckboxValue(description,
                                                  name,
                                                  value,
                                                  page,
                                                  expander_name,
                                                  row_name,
                                                  b_enabled,
                                                  height,
                                                  width,
                                                  font_face_code)

        checkbox_view_model = CheckboxParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(checkbox_view_model, description, name, b_enabled, height, 0,
                                                        description if row_name else "")

        checkbox_view_model.InitializeIsChecked(value > 0)

        self.view_model_builder.AddParameterToPalette(checkbox_view_model, page, expander_name, row_name, font_face_code)

    def AddColorValue(self,
                      description    : str,
                      name           : str,
                      value          : int,
                      page           : int,
                      expander_name  : str,
                      row_name       : str,
                      b_enabled      : bool,
                      height         : int,
                      width          : int,
                      font_face_code : int):
        """Add a color value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddColorValue(description,
                                               name,
                                               value,
                                               page,
                                               expander_name,
                                               row_name,
                                               b_enabled,
                                               height,
                                               width,
                                               font_face_code)

        color_view_model = ColorComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(color_view_model, description, name, b_enabled, height, width, "")

        color_view_model.SelectedValue.Value = value

        self.view_model_builder.AddParameterToPalette(color_view_model, page, expander_name, row_name, font_face_code)

    def AddComboBoxValue(self,
                         description     : str,
                         name            : str,
                         value           : str,
                         list_values     : str,
                         value_type      : AllplanPalette.PaletteValueType,
                         page            : int,
                         expander_name   : str,
                         row_name        : str,
                         b_enabled       : bool,
                         height          : int,
                         width           : int,
                         font_face_code  : int,
                         background_color: (list[int] | AllplanUtil.VecIntList),
                         is_editable     : bool):
        """Add a combo box value to the palette

        Args:
            description:      Description
            name:             Value name
            value:            Value
            list_values:      List values
            value_type:       Value type
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color
            is_editable:      Is editable state
        """

        self.cpp_palette_builder.AddComboBoxValue(description,
                                                  name,
                                                  value,
                                                  list_values,
                                                  value_type,
                                                  page,
                                                  expander_name,
                                                  row_name,
                                                  b_enabled,
                                                  height,
                                                  width,
                                                  font_face_code,
                                                  background_color,
                                                  is_editable)

        combobox_view_model = None

        # We need to create different view models for different value types

        if value_type == AllplanPalette.PaletteValueType.INTEGER:
            if is_editable:
                combobox_view_model = IntegerEditComboboxViewModel()
            else:
                combobox_view_model = IntegerComboboxViewModel()

        elif value_type == AllplanPalette.PaletteValueType.STRING:
            if is_editable:
                combobox_view_model = StringEditComboboxViewModel()
            else:
                combobox_view_model = StringComboboxViewModel()

        elif (doubleValueType := WpfPaletteBuilderUtils.convert_to_DoubleValueType(value_type)) is not None:
            combobox_view_model            = DoubleEditComboboxViewModel(doubleValueType)
            combobox_view_model.IsEditable = is_editable

            # for length and angle values we need to convert the values to the palette units
            if value_type in (AllplanPalette.PaletteValueType.LENGTH, AllplanPalette.PaletteValueType.ANGLE):
                list_values = WpfPaletteBuilderUtils.convert_double_str_list_to_palette_units(list_values, value_type)
                value       = WpfPaletteBuilderUtils.convert_double_str_to_palette_units(value, value_type)

        if combobox_view_model is None:
            return

        combobox_view_model.InitializeItemsFromString(list_values)
        combobox_view_model.InitializeSelectedValueFromString(value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddConcreteCoverValue(self,
                              description   : str,
                              name          : str,
                              value         : float,
                              page          : int,
                              expander_name : str,
                              row_name      : str,
                              b_enabled     : bool,
                              height        : int,
                              width         : int,
                              font_face_code: int):
        """Add a concrete cover value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddConcreteCoverValue(description,
                                                       name,
                                                       value,
                                                       page,
                                                       expander_name,
                                                       row_name,
                                                       b_enabled,
                                                       height,
                                                       width,
                                                       font_face_code)

        combobox_view_model = DoubleEditComboboxViewModel(DoubleValueType.Length)

        combobox_view_model.IsEditable = True

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        PythonPaletteResourceProvider.InitializeConcreteCoverCombobox(combobox_view_model, value)

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddConcreteGrade(self,
                         description   : str,
                         name          : str,
                         value         : int,
                         page          : int,
                         expander_name : str,
                         row_name      : str,
                         b_enabled     : bool,
                         height        : int,
                         width         : int,
                         font_face_code: int):
        """Add a concrete grade value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddConcreteGrade(description,
                                                  name,
                                                  value,
                                                  page,
                                                  expander_name,
                                                  row_name,
                                                  b_enabled,
                                                  height,
                                                  width,
                                                  font_face_code)

        combobox_view_model = ReinforcementResourceComboboxViewModel()

        PythonPaletteResourceProvider.InitializeConcreteGradeCombobox(combobox_view_model, value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddConcreteGradeCatalogRef(self,
                                   description   : str,
                                   name          : str,
                                   value         : str,
                                   page          : int,
                                   expander_name : str,
                                   row_name      : str,
                                   b_enabled     : bool,
                                   height        : int,
                                   width         : int,
                                   font_face_code: int):
        """Add a concrete grade reference

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddConcreteGradeCatalogRef(description,
                                                            name,
                                                            value,
                                                            page,
                                                            expander_name,
                                                            row_name,
                                                            b_enabled,
                                                            height,
                                                            width,
                                                            font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetConcreteGradeCatalogValues(),
                                  value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddDoubleValue(self,
                       description     : str,
                       name            : str,
                       value           : float,
                       page            : int,
                       expander_name   : str,
                       row_name        : str,
                       b_enabled       : bool,
                       min_value       : float,
                       max_value       : float,
                       interval_value  : float,
                       as_slider       : bool,
                       height          : int,
                       width           : int,
                       font_face_code  : int,
                       background_color: (list[int] | AllplanUtil.VecIntList)):
        """Add a double value to the palette

        Args:
            description:      Description
            name:             Value name
            value:            Value
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            min_value:        Minimal value
            max_value:        Maximal value
            interval_value:   Interval value for the slider
            as_slider:        Show as slider: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        self.cpp_palette_builder.AddDoubleValue(description,
                                                name,
                                                value,
                                                page,
                                                expander_name,
                                                row_name,
                                                b_enabled,
                                                min_value,
                                                max_value,
                                                interval_value,
                                                as_slider,
                                                height,
                                                width,
                                                font_face_code,
                                                background_color)

        self._add_double_type_value(DoubleValueType.Double, description, name, value, page, expander_name, row_name, b_enabled,
                                   min_value, max_value, interval_value, as_slider, height, width, font_face_code, background_color)

    def AddFaceStyleValue(self,
                          description   : str,
                          name          : str,
                          value         : int,
                          page          : int,
                          expander_name : str,
                          row_name      : str,
                          b_enabled     : bool,
                          height        : int,
                          width         : int,
                          font_face_code: int):
        """Add a face style combobox to the palette

        Args:
            description:    Description
            name:           ID name
            value:          Selected value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddFaceStyleValue(description,
                                                   name,
                                                   value,
                                                   page,
                                                   expander_name,
                                                   row_name,
                                                   b_enabled,
                                                   height,
                                                   width,
                                                   font_face_code)

        face_style_view_model = FaceStyleComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(face_style_view_model, description, name, b_enabled, height, width, "")

        face_style_view_model.SelectedValue.Value = value

        self.view_model_builder.AddParameterToPalette(face_style_view_model, page, expander_name, row_name, font_face_code)

    def AddFactoryCatalogRef(self,
                             description   : str,
                             name          : str,
                             value         : str,
                             page          : int,
                             expander_name : str,
                             row_name      : str,
                             b_enabled     : bool,
                             height        : int,
                             width         : int,
                             font_face_code: int):
        """Add a factory precast catalog reference

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddFactoryCatalogRef(description,
                                                      name,
                                                      value,
                                                      page,
                                                      expander_name,
                                                      row_name,
                                                      b_enabled,
                                                      height,
                                                      width,
                                                      font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetFactoryCatalogValues(),
                                  value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddFixtureCatalogRef(self,
                             description   : str,
                             name          : str,
                             value         : str,
                             page          : int,
                             expander_name : str,
                             row_name      : str,
                             b_enabled     : bool,
                             height        : int,
                             width         : int,
                             font_face_code: int):
        """Add a fixture precast catalog reference - all, only point, line or area

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddFixtureCatalogRef(description,
                                                      name,
                                                      value,
                                                      page,
                                                      expander_name,
                                                      row_name,
                                                      b_enabled,
                                                      height,
                                                      width,
                                                      font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetAllFixtureCatalogValues(),
                                  value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddFixtureValues(self,
                         description_path    : str,
                         description_group   : str,
                         description_element : str,
                         name                : str,
                         fixture             : AllplanPalette.FixtureProperties,
                         page                : int,
                         expander_name       : str,
                         row_name            : str,
                         b_enabled           : bool,
                         height              : int,
                         width               : int,
                         font_face_code      : int):
        """Add the fixture values

        Args:
            description_path:    Description of the path value
            description_group:   Description of the group value
            description_element: Description of the element value
            name:                Value name
            fixture:             Properties of the fixture
            page:                Page index
            expander_name:       Expander section name
            row_name:            Name of the row
            b_enabled:           Control is enabled: true/false
            height:              Control height, only used for a row
            width:               Control width, only used for a row
            font_face_code:      Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddFixtureValues(description_path,
                                                  description_group,
                                                  description_element,
                                                  name,
                                                  fixture,
                                                  page,
                                                  expander_name,
                                                  row_name,
                                                  b_enabled,
                                                  height,
                                                  width,
                                                  font_face_code)

        short_names         = PythonPaletteResourceProvider.GetFixturePathShortNames()
        selected_short_name = PythonPaletteResourceProvider.GetFixturePathShortName(fixture.GetPath())
        short_name_index    = short_names.index(selected_short_name) if selected_short_name in short_names else 0

        self._add_string_combobox(description_path, f"{name}.PathShortcut", short_names, selected_short_name,
                                  page, expander_name, row_name, b_enabled, height, width, font_face_code)

        group_names = PythonPaletteResourceProvider.GetFixtureGroupNames(short_name_index)

        selected_group_index, selected_group = WpfPaletteBuilderUtils.get_string_index_in_fixture_list(group_names, fixture.GetGroup())

        self._add_string_combobox(description_group, f"{name}.Group", group_names, selected_group,
                                  page, expander_name, row_name, b_enabled, height, width, font_face_code)

        element_names = PythonPaletteResourceProvider.GetFixtureEntryNames(short_name_index, selected_group_index)

        _, selected_element = WpfPaletteBuilderUtils.get_string_index_in_fixture_list(element_names, fixture.GetElement())

        self._add_string_combobox(description_element, f"{name}.Element",element_names,selected_element,
                                  page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddHatchValue(self,
                      description    : str,
                      name           : str,
                      value          : int,
                      page           : int,
                      expander_name  : str,
                      row_name       : str,
                      b_enabled      : bool,
                      height         : int,
                      width          : int,
                      font_face_code : int):
        """Add a hatch combobox to the palette

        Args:
            description:    Description
            name:           ID name
            value:          Selected value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddHatchValue(description,
                                               name,
                                               value,
                                               page,
                                               expander_name,
                                               row_name,
                                               b_enabled,
                                               height,
                                               width,
                                               font_face_code)

        hatch_view_model = HatchComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(hatch_view_model, description, name, b_enabled, height, width, "")

        hatch_view_model.SelectedValue.Value = value

        self.view_model_builder.AddParameterToPalette(hatch_view_model, page, expander_name, row_name, font_face_code)

    def AddInsulationCatalogRef(self,
                                description    : str,
                                name           : str,
                                value          : str,
                                page           : int,
                                expander_name  : str,
                                row_name       : str,
                                b_enabled      : bool,
                                height         : int,
                                width          : int,
                                font_face_code : int):
        """Add an insulation reference

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddInsulationCatalogRef(description,
                                                         name,
                                                         value,
                                                         page,
                                                         expander_name,
                                                         row_name,
                                                         b_enabled,
                                                         height,
                                                         width,
                                                         font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetInsulationCatalogValues(),
                                 value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddIntValue(self,
                    description      : str,
                    name             : str,
                    value            : int,
                    page             : int,
                    expander_name    : str,
                    row_name         : str,
                    b_enabled        : bool,
                    min_value        : float,
                    max_value        : float,
                    interval_value   : float,
                    as_slider        : bool,
                    height           : int,
                    width            : int,
                    font_face_code   : int,
                    background_color : (list[int] | AllplanUtil.VecIntList)):
        """Add an integer value to the palette

        Args:
            description:      Description
            name:             Value name
            value:            Value
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            min_value:        Minimal value
            max_value:        Maximal value
            interval_value:   Interval value for the slider
            as_slider:        Show as slider: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        self.cpp_palette_builder.AddIntValue(description,
                                             name,
                                             value,
                                             page,
                                             expander_name,
                                             row_name,
                                             b_enabled,
                                             min_value,
                                             max_value,
                                             interval_value,
                                             as_slider,
                                             height,
                                             width,
                                             font_face_code,
                                             background_color)

        tooltip = description if row_name else ""

        if as_slider:
            int_view_model = IntegerSliderParameterViewModel()
            int_view_model.InitializeValues(value, min_value, max_value, interval_value)

        else:
            int_view_model = IntegerEditParameterViewModel()
            int_view_model.InitializeValues(value, min_value, max_value)
            int_view_model.SetBackgroundColor(background_color[0], background_color[1], background_color[2])

        WpfPaletteBuilder.set_base_viewmodel_properties(int_view_model, description, name, b_enabled, height, width, tooltip)

        self.view_model_builder.AddParameterToPalette(int_view_model, page, expander_name, row_name, font_face_code)

    def AddLayer(self,
                 description    : str,
                 name           : str,
                 value          : int,
                 page           : int,
                 expander_name  : str,
                 row_name       : str,
                 b_enabled      : bool,
                 height         : int,
                 width          : int,
                 font_face_code : int):
        """Add a layer value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddLayer(description,
                                          name,
                                          value,
                                          page,
                                          expander_name,
                                          row_name,
                                          b_enabled,
                                          height,
                                          width,
                                          font_face_code)

        layer_view_model = LayerComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(layer_view_model, description, name, b_enabled, height, width, "")

        layer_view_model.SelectedValue.Value = value

        self.view_model_builder.AddParameterToPalette(layer_view_model, page, expander_name, row_name, font_face_code)

    def AddLengthValue(self,
                       description      : str,
                       name             : str,
                       value            : float,
                       page             : int,
                       expander_name    : str,
                       row_name         : str,
                       b_enabled        : bool,
                       min_value        : float,
                       max_value        : float,
                       interval_value   : float,
                       as_slider        : bool,
                       height           : int,
                       width            : int,
                       font_face_code   : int,
                       background_color : (list[int] | AllplanUtil.VecIntList)):
        """Add a length value to the palette

        Args:
            description:      Description
            name:             Value name
            value:            Value
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            min_value:        Minimal value
            max_value:        Maximal value
            interval_value:   Interval value for the slider
            as_slider:        Show as slider: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        self.cpp_palette_builder.AddLengthValue(description,
                                                name,
                                                value,
                                                page,
                                                expander_name,
                                                row_name,
                                                b_enabled,
                                                min_value,
                                                max_value,
                                                interval_value,
                                                as_slider,
                                                height,
                                                width,
                                                font_face_code,
                                                background_color)

        # The values for view model are expected in mm so we need to convert them using the internal length factor

        value_converted          = WpfPaletteBuilderUtils.convert_length_to_palette_units(value)
        min_value_converted      = WpfPaletteBuilderUtils.convert_length_to_palette_units(min_value)
        max_value_converted      = WpfPaletteBuilderUtils.convert_length_to_palette_units(max_value)
        interval_value_converted = WpfPaletteBuilderUtils.convert_length_to_palette_units(interval_value)

        self._add_double_type_value(DoubleValueType.Length, description, name, value_converted, page, expander_name, row_name,
                                    b_enabled, min_value_converted, max_value_converted, interval_value_converted,
                                    as_slider, height, width, font_face_code, background_color)

    def AddLineFixtureCatalogRef(self,
                                 description   : str,
                                 name          : str,
                                 value         : str,
                                 page          : int,
                                 expander_name : str,
                                 row_name      : str,
                                 b_enabled     : bool,
                                 height        : int,
                                 width         : int,
                                 font_face_code: int):
        """Add a line fixture precast catalog reference - all, only point, line or area

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddLineFixtureCatalogRef(description,
                                                          name,
                                                          value,
                                                          page,
                                                          expander_name,
                                                          row_name,
                                                          b_enabled,
                                                          height,
                                                          width,
                                                          font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetLineFixtureCatalogValues(),
                                  value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddMaterialButton(self,
                          description   : str,
                          name          : str,
                          value         : str,
                          button_type   : int,
                          page          : int,
                          expander_name : str,
                          row_name      : str,
                          b_enabled     : bool,
                          height        : int,
                          width         : int,
                          font_face_code: int):
        """Add a material button to the palette

        Args:
            description:    Description
            name:           Value name
            value:          String of material
            button_type:    Button type (0: simple material button, 1: mat button + switch off button)
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddMaterialButton(description,
                                                   name,
                                                   value,
                                                   button_type,
                                                   page,
                                                   expander_name,
                                                   row_name,
                                                   b_enabled,
                                                   height,
                                                   width,
                                                   font_face_code)

        material_button_view_model = MaterialButtonParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(material_button_view_model, description, name, b_enabled, height, width, "")

        material_button_view_model.HasClearButton = button_type == 1

        material_button_view_model.SetMaterialButtonText(value)

        self.view_model_builder.AddParameterToPalette(material_button_view_model, page, expander_name, row_name, font_face_code)

    def AddMeshGroup(self,
                     description   : str,
                     name          : str,
                     value         : int,
                     page          : int,
                     expander_name : str,
                     row_name      : str,
                     b_enabled     : bool,
                     height        : int,
                     width         : int,
                     font_face_code: int):
        """Add a mesh group value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddMeshGroup(description,
                                              name,
                                              value,
                                              page,
                                              expander_name,
                                              row_name,
                                              b_enabled,
                                              height,
                                              width,
                                              font_face_code)

        combobox_view_model = ReinforcementResourceComboboxViewModel()

        PythonPaletteResourceProvider.InitializeMeshGroupCombobox(combobox_view_model, value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddMeshType(self,
                    description   : str,
                    name          : str,
                    value         : str,
                    page          : int,
                    expander_name : str,
                    row_name      : str,
                    b_enabled     : bool,
                    mesh_group    : int,
                    height        : int,
                    width         : int,
                    font_face_code: int):
        """Add a mesh type value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            mesh_group:     Mesh group
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddMeshType(description,
                                             name,
                                             value,
                                             page,
                                             expander_name,
                                             row_name,
                                             b_enabled,
                                             mesh_group,
                                             height,
                                             width,
                                             font_face_code)

        combobox_view_model = ReinforcementResourceComboboxViewModel()

        PythonPaletteResourceProvider.InitializeMeshTypeCombobox(combobox_view_model, mesh_group, value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddMultiMaterialLayoutCatalogRef(self,
                                         description   : str,
                                         name          : str,
                                         value         : str,
                                         page          : int,
                                         expander_name : str,
                                         row_name      : str,
                                         b_enabled     : bool,
                                         height        : int,
                                         width         : int,
                                         font_face_code: int) -> int:
        """Add a multi-material layout catalog reference

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline

        Returns:
            int: The result of adding the multi-material layout catalog reference
        """

        self.cpp_palette_builder.AddMultiMaterialLayoutCatalogRef(description,
                                                                         name,
                                                                         value,
                                                                         page,
                                                                         expander_name,
                                                                         row_name,
                                                                         b_enabled,
                                                                         height,
                                                                         width,
                                                                         font_face_code)

        combobox_view_model = StringComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        result = PythonPaletteResourceProvider.InitializeMultiMaterialLayoutCatalogCombobox(combobox_view_model, value)

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

        return result

    def AddNormCatalogRef(self,
                          description   : str,
                          name          : str,
                          value         : str,
                          page          : int,
                          expander_name : str,
                          row_name      : str,
                          b_enabled     : bool,
                          height        : int,
                          width         : int,
                          font_face_code: int):
        """Add a norm catalog reference

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddNormCatalogRef(description,
                                                   name,
                                                   value,
                                                   page,
                                                   expander_name,
                                                   row_name,
                                                   b_enabled,
                                                   height,
                                                   width,
                                                   font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetNormCatalogValues(value),
                                 value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddPage(self,
                name: str,
                description: str):
        """Add a page to the palette

        Args:
            name:         ID name
            description:  Description text (localized)
        """

        self.cpp_palette_builder.AddPage(name,
                                         description)

        self.view_model_builder.CreateAndAddPage(description)

    def AddPatternValue(self,
                        description   : str,
                        name          : str,
                        value         : int,
                        page          : int,
                        expander_name : str,
                        row_name      : str,
                        b_enabled     : bool,
                        height        : int,
                        width         : int,
                        font_face_code: int):
        """Add a pattern combobox to the palette

        Args:
            description:    Description
            name:           ID name
            value:          Selected value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPatternValue(description,
                                                 name,
                                                 value,
                                                 page,
                                                 expander_name,
                                                 row_name,
                                                 b_enabled,
                                                 height,
                                                 width,
                                                 font_face_code)

        pattern_view_model = PatternComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(pattern_view_model, description, name, b_enabled, height, width, "")

        pattern_view_model.SelectedValue.Value = value

        self.view_model_builder.AddParameterToPalette(pattern_view_model, page, expander_name, row_name, font_face_code)

    def AddPenValue(self,
                    description    : str,
                    name           : str,
                    value          : int,
                    page           : int,
                    expander_name  : str,
                    row_name       : str,
                    b_enabled      : bool,
                    height         : int,
                    width          : int,
                    font_face_code : int):
        """Add a pen value to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPenValue(description,
                                             name,
                                             value,
                                             page,
                                             expander_name,
                                             row_name,
                                             b_enabled,
                                             height,
                                             width,
                                             font_face_code)

        pen_view_model = PenComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(pen_view_model, description, name, b_enabled, height, width, "")

        pen_view_model.SelectedValue.Value = value

        self.view_model_builder.AddParameterToPalette(pen_view_model, page, expander_name, row_name, font_face_code)

    def AddPicture(self,
                   description    : str,
                   name           : str,
                   picture_name   : str,
                   lib_path       : str,
                   orientation    : AllplanPalette.Orientation,
                   page           : int,
                   expander_name  : str,
                   row_name       : str,
                   height         : int,
                   width          : int):
        """Add a picture to the palette

        Args:
            description:    Description used for the tooltip
            name:           ID name
            picture_name:   Name of the picture
            lib_path:       Library path
            orientation:    Orientation (0:LEFT, 1:MIDDLE, 2:RIGHT)
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            height:         Control height
            width:          Weighted width of control if it is in the row, or width of the image if it is the only control in the row
        """

        self.cpp_palette_builder.AddPicture(description,
                                            name,
                                            picture_name,
                                            lib_path,
                                            orientation,
                                            page,
                                            expander_name,
                                            row_name)

        # this is needed until proper palette builder mock is implemented
        if AllplanUtil.IsExecutedByUnitTest():
            return

        # if name is empty we set it to picture_name to have an identifier in the palette
        # and be backward compatible with the old palettes where the name can be missing in the pyp
        if name == "":
            name = picture_name

        picture_view_model = PictureParameterViewModel()

        #for "overall" picture we set weighted width to default value (as it is the only control in the row we can use any value > 0)
        #for picture in row we set the weighted width to a value set in pyp file, 0 means the actual fixed width of the image is used
        weighted_width = width if row_name != "" else 30

        WpfPaletteBuilder.set_base_viewmodel_properties(picture_view_model, description, name, True, 0, weighted_width, description)

        picture_view_model.CreateImageFromResourceIdOrPath(f"{lib_path}\\{picture_name}")

        # casting orientation to int is needed by the .net method
        # would be good to refactor it in the future to get rid of the c++ AllplanPalette.Orientation
        picture_view_model.SetHorizontalAlignmentFromFlag(int(orientation)) # type: ignore[arg-type]

        #for "overall" picture we set picture width to width
        #for picture in row we set the picture width to 0, which means the actual width of the image is used
        picture_width = width if row_name == "" else 0

        picture_view_model.ConfigureDefaultSize(picture_width, height)

        picture_view_model.SupportsOrientation = row_name == ""

        self.view_model_builder.AddParameterToPalette(picture_view_model, page, expander_name, row_name or f"{name}_OVERALL", 0)

    def AddPictureButton(self,
                         description    : str,
                         name           : str,
                         value          : str,
                         event_id       : int,
                         page           : int,
                         expander_name  : str,
                         row_name       : str,
                         b_enabled      : bool,
                         height         : int,
                         width          : int,
                         font_face_code : int):
        """Add a picture button to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value
            event_id:       Value holds the event ID pressing the button
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPictureButton(description,
                                                  name,
                                                  value,
                                                  event_id,
                                                  page,
                                                  expander_name,
                                                  row_name,
                                                  b_enabled,
                                                  height,
                                                  width,
                                                  font_face_code)

        picture_button_view_model = PictureButtonParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(picture_button_view_model, description, name, b_enabled, height, width, description)

        picture_button_view_model.CreateImageFromPath(value)

        self.view_model_builder.AddParameterToPalette(picture_button_view_model, page, expander_name, row_name, font_face_code)

    def AddPictureButtonList(self,
                             description    : str,
                             name           : str,
                             value          : int,
                             picture_path   : str,
                             picture_list   : str,
                             value_list     : str,
                             text_list      : str,
                             page           : int,
                             expander_name  : str,
                             row_name       : str,
                             b_enabled      : bool,
                             height         : int,
                             width          : int,
                             font_face_code : int):
        """Add a picture button list to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value holds the selected picture button in buttons
            picture_path:   Path of pictures
            picture_list:   Picture list holds the images for the buttons - example: a.png|b.png|c.png
            value_list:     Value list of possible values - example: 0|1|2
            text_list:      Text list for the tooltips
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPictureButtonList(description,
                                                      name,
                                                      value,
                                                      picture_path,
                                                      picture_list,
                                                      value_list,
                                                      text_list,
                                                      page,
                                                      expander_name,
                                                      row_name,
                                                      b_enabled,
                                                      height,
                                                      width,
                                                      font_face_code)

        button_list_view_model = PictureButtonGroupParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(button_list_view_model, description, name, b_enabled, height, width, "")

        button_list_view_model.AddItemsFromListStrings(f"{picture_path}\\", picture_list, value_list, text_list)
        button_list_view_model.SetSelectedItemWithValue(value)

        self.view_model_builder.AddParameterToPalette(button_list_view_model, page, expander_name, row_name, font_face_code)

    def AddPictureComboBox(self,
                           description    : str,
                           name           : str,
                           value          : int,
                           picture_path   : str,
                           picture_list   : str,
                           value_list     : str,
                           text_list      : str,
                           page           : int,
                           expander_name  : str,
                           row_name       : str,
                           b_enabled      : bool,
                           height         : int,
                           width          : int,
                           font_face_code : int):
        """Add a picture combobox to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value holds the selected picture button in buttons
            picture_path:   Path of pictures
            picture_list:   Picture list holds the images for the buttons - example: a.png|b.png|c.png
            value_list:     Value list of possible values - example: 0|1|2
            text_list:      Text list for the tooltips
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPictureComboBox(description,
                                                    name,
                                                    value,
                                                    picture_path,
                                                    picture_list,
                                                    value_list,
                                                    text_list,
                                                    page,
                                                    expander_name,
                                                    row_name,
                                                    b_enabled,
                                                    height,
                                                    width,
                                                    font_face_code)

        combobox_view_model = PictureComboboxParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        combobox_view_model.AddItemsFromListStrings(f"{picture_path}\\", picture_list, value_list, text_list)
        combobox_view_model.SetSelectedItemWithValue(value)

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddPictureResourceButton(self,
                                 description    : str,
                                 name           : str,
                                 value          : int,
                                 event_id       : int,
                                 page           : int,
                                 expander_name  : str,
                                 row_name       : str,
                                 b_enabled      : bool,
                                 height         : int,
                                 width          : int,
                                 font_face_code : int):
        """Add a picture button to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value holds the resource ID
            event_id:       Value holds the event ID pressing the button
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPictureResourceButton(description,
                                                          name,
                                                          value,
                                                          event_id,
                                                          page,
                                                          expander_name,
                                                          row_name,
                                                          b_enabled,
                                                          height,
                                                          width,
                                                          font_face_code)

        picture_button_view_model = PictureButtonParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(picture_button_view_model, description, name, b_enabled, height, width, description)

        picture_button_view_model.CreateImageFromResourceID(value)

        self.view_model_builder.AddParameterToPalette(picture_button_view_model, page, expander_name, row_name, font_face_code)

    def AddPictureResourceButtonList(self,
                                     description    : str,
                                     name           : str,
                                     value          : int,
                                     picture_list   : str,
                                     value_list     : str,
                                     text_list      : str,
                                     page           : int,
                                     expander_name  : str,
                                     row_name       : str,
                                     b_enabled      : bool,
                                     height         : int,
                                     width          : int,
                                     font_face_code : int):
        """Add a picture resource button list to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value holds the selected picture button in buttons
            picture_list:   Picture list holds the images for the buttons - example: 16433|16441|16449
            value_list:     Value list of possible values - example: 0|1|2
            text_list:      Text list for the tooltips
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPictureResourceButtonList(description,
                                                              name,
                                                              value,
                                                              picture_list,
                                                              value_list,
                                                              text_list,
                                                              page,
                                                              expander_name,
                                                              row_name,
                                                              b_enabled,
                                                              height,
                                                              width,
                                                              font_face_code)

        button_list_view_model = PictureButtonGroupParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(button_list_view_model, description, name, b_enabled, height, width, "")

        button_list_view_model.AddItemsFromListStrings("", picture_list, value_list, text_list)
        button_list_view_model.SetSelectedItemWithValue(value)

        self.view_model_builder.AddParameterToPalette(button_list_view_model, page, expander_name, row_name, font_face_code)

    def AddPictureResourceComboBox(self,
                                   description    : str,
                                   name           : str,
                                   value          : int,
                                   picture_list   : str,
                                   value_list     : str,
                                   text_list      : str,
                                   page           : int,
                                   expander_name  : str,
                                   row_name       : str,
                                   b_enabled      : bool,
                                   height         : int,
                                   width          : int,
                                   font_face_code : int):
        """Add a picture resource combobox to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value holds the selected picture button in buttons
            picture_list:   Picture list holds the images for the buttons - example: 16433|16441|16449
            value_list:     Value list of possible values - example: 0|1|2
            text_list:      Text list for the tooltips
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPictureResourceComboBox(description,
                                                            name,
                                                            value,
                                                            picture_list,
                                                            value_list,
                                                            text_list,
                                                            page,
                                                            expander_name,
                                                            row_name,
                                                            b_enabled,
                                                            height,
                                                            width,
                                                            font_face_code)


        combobox_view_model = PictureComboboxParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        combobox_view_model.AddItemsFromListStrings("", picture_list, value_list, text_list)
        combobox_view_model.SetSelectedItemWithValue(value)

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddPictureResourceToggleButton(self,
                                       description    : str,
                                       name           : str,
                                       value          : int,
                                       picture_list   : str,
                                       value_list     : str,
                                       text_list      : str,
                                       page           : int,
                                       expander_name  : str,
                                       row_name       : str,
                                       b_enabled      : bool,
                                       height         : int,
                                       width          : int,
                                       font_face_code : int):
        """Add a picture toggle button to the palette

        Args:
            description:    Description
            name:           Value name
            value:          Value holds the selected picture button in buttons
            picture_list:   Picture list holds the images for the buttons - example: a.png|b.png|c.png
            value_list:     Value list of possible values - example: 0|1|2
            text_list:      Text list for the tooltips
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPictureResourceToggleButton(description,
                                                                name,
                                                                value,
                                                                picture_list,
                                                                value_list,
                                                                text_list,
                                                                page,
                                                                expander_name,
                                                                row_name,
                                                                b_enabled,
                                                                height,
                                                                width,
                                                                font_face_code)

        toggle_button_view_model = PictureToggleButtonParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(toggle_button_view_model, description, name, b_enabled, height, width, "")

        toggle_button_view_model.IsChecked.Value = value > 0
        toggle_button_view_model.SetBitmapIDsFromListString(picture_list)

        self.view_model_builder.AddParameterToPalette(toggle_button_view_model, page, expander_name, row_name, font_face_code)

    def AddPlaneReferencesButton(self,
                                 description    : str,
                                 name           : str,
                                 plane_refs     : AllplanArchEle.BasePlaneReferences,
                                 page           : int,
                                 expander_name  : str,
                                 row_name       : str,
                                 b_enabled      : bool,
                                 height         : int,
                                 width          : int,
                                 font_face_code : int):
        """Add a plane references button to the palette

        Args:
            description:    Description
            name:           Value name
            plane_refs:     Plane references
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPlaneReferencesButton(description,
                                                          name,
                                                          plane_refs,
                                                          page,
                                                          expander_name,
                                                          row_name,
                                                          b_enabled,
                                                          height,
                                                          width,
                                                          font_face_code)

    def AddPointFixtureCatalogRef(self,
                                  description    : str,
                                  name           : str,
                                  value          : str,
                                  page           : int,
                                  expander_name  : str,
                                  row_name       : str,
                                  b_enabled      : bool,
                                  height         : int,
                                  width          : int,
                                  font_face_code : int):
        """Add a point fixture precast catalog reference - all, only point, line or area

        Args:
            description:    Description
            name:           Value name
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddPointFixtureCatalogRef(description,
                                                           name,
                                                           value,
                                                           page,
                                                           expander_name,
                                                           row_name,
                                                           b_enabled,
                                                           height,
                                                           width,
                                                           font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetPointFixtureCatalogValues(),
                                  value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddConstructionPointSymbolValue(self,
                                        description    : str,
                                        name           : str,
                                        value          : int,
                                        value_list     : str,
                                        page           : int,
                                        expander_name  : str,
                                        row_name       : str,
                                        b_enabled      : bool,
                                        height         : int,
                                        width          : int,
                                        font_face_code : int):
        """Add a point symbol combobox to the palette

        Args:
            description:    Description
            name:           ID name
            value:          Selected value
            value_list:     Pipe separated list of point symbol types
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        point_symbol_view_model = ContructionPointSymbolViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(point_symbol_view_model, description, name, b_enabled, height, width, "")

        point_symbol_view_model.SelectedValue.Value = value
        point_symbol_view_model.SymbolBehaviour = WpfPaletteBuilderUtils.get_construction_point_symbol_type_filter(value_list)

        SHOW_SYMBOL_OFF = "showsymboloff"
        SHOW_SYMBOL_ID = "showsymbolid"

        if SHOW_SYMBOL_OFF in value_list.lower():
            point_symbol_view_model.ShowSymbolOff = True

        if SHOW_SYMBOL_ID in value_list.lower():
            point_symbol_view_model.ShowSymbolID = True

        self.view_model_builder.AddParameterToPalette(point_symbol_view_model, page, expander_name, row_name, font_face_code)

        self._register_update_callback(point_symbol_view_model, page)

    def AddPrecastElementTypeCatalogRef(self,
                                        description    : str,
                                        name           : str,
                                        value          : str,
                                        page           : int,
                                        expander_name  : str,
                                        row_name       : str,
                                        b_enabled      : bool,
                                        height         : int,
                                        width          : int,
                                        font_face_code : int) -> str:
        """Add a precast element type catalog reference

        Args:
            description:    Description
            name:           Value name
            value:          Value
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline

        Returns:
            str: The result of adding the precast element type catalog reference
        """

        self.cpp_palette_builder.AddPrecastElementTypeCatalogRef(description,
                                                                        name,
                                                                        value,
                                                                        page,
                                                                        expander_name,
                                                                        row_name,
                                                                        b_enabled,
                                                                        height,
                                                                        width,
                                                                        font_face_code)

        combobox_view_model = StringComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        result = PythonPaletteResourceProvider.InitializePrecastElementTypeCombobox(combobox_view_model, value)

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

        return result

    def AddRadioButton(self,
                       radio_button_group_description : str,
                       radio_button_group_name        : str,
                       radio_button_description       : str,
                       value                          : object,
                       selected_value_in_group        : object,
                       page                           : int,
                       expander_name                  : str,
                       row_name                       : str,
                       b_enabled                      : bool,
                       height                         : int,
                       width                          : int,
                       font_face_code                 : int):
        """Add a radio button to the palette

        Args:
            radio_button_group_description: Radio button group description
            radio_button_group_name:        Radio button group ID name
            radio_button_description:       Radio button description
            value:                          Double value of this radio button
            selected_value_in_group:        Selected value of radio button group
            page:                           Page index
            expander_name:                  Expander section name
            row_name:                       Name of the row
            b_enabled:                      Control is enabled: true/false
            height:                         Control height, only used for a row
            width:                          Control width, only used for a row
            font_face_code:                 Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddRadioButton(radio_button_group_description,
                                                radio_button_group_name,
                                                radio_button_description,
                                                value,
                                                selected_value_in_group,
                                                page,
                                                expander_name,
                                                row_name,
                                                b_enabled,
                                                height,
                                                width,
                                                font_face_code)

        radio_button_view_model = RadioButtonParameterViewModel()

        # For compatibility with existing framework code, we need to compose the parameter name to ensure unique name
        # later the framework can be changed to pass the name from pyp file

        radio_button_name = f"{radio_button_group_name}_{str(value)}"

        WpfPaletteBuilder.set_base_viewmodel_properties(radio_button_view_model, radio_button_group_description, radio_button_name,
                                                        b_enabled, height, width, "")

        radio_button_view_model.RadioButtonGroupName   = radio_button_group_name
        radio_button_view_model.RadioButtonDescription = radio_button_description

        radio_button_view_model.IsChecked.InitializeValue(value == selected_value_in_group)

        self.view_model_builder.AddParameterToPalette(radio_button_view_model, page, expander_name, row_name, font_face_code)

    def AddRefPointButton(self,
                          description        : str,
                          name               : str,
                          ref_point_position : AllplanPalette.RefPointPosition,
                          ref_point_type     : AllplanPalette.RefPointButtonType,
                          page               : int,
                          expander_name      : str,
                          row_name           : str,
                          b_enabled          : bool,
                          height             : int,
                          width              : int,
                          font_face_code     : int):
        """Add a reference point button to the palette

        Args:
            description:        Description
            name:               Value name
            ref_point_position: Reference point ID (1,...,9)
            ref_point_type:     Reference point type
            page:               Page index
            expander_name:      Expander section name
            row_name:           Name of the row
            b_enabled:          Control is enabled: true/false
            height:             Control height, only used for a row
            width:              Control width, only used for a row
            font_face_code:     Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddRefPointButton(description,
                                                   name,
                                                   ref_point_position,
                                                   ref_point_type,
                                                   page,
                                                   expander_name,
                                                   row_name,
                                                   b_enabled,
                                                   height,
                                                   width,
                                                   font_face_code)

        refpoint_button_view_model = RefPointButtonParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(refpoint_button_view_model, description, name, b_enabled, height, width, "")

        refpoint_button_view_model.SetRefPointTypeAndPositionFromFlag(int(ref_point_type), int(ref_point_position)) # type: ignore[arg-type]

        self.view_model_builder.AddParameterToPalette(refpoint_button_view_model, page, expander_name, row_name, font_face_code)

    def AddResourcePicture(self,
                           description        : str,
                           name               : str,
                           picture_resource_id: int,
                           page               : int,
                           expander_name      : str,
                           row_name           : str,
                           height             : int,
                           width              : int):
        """Add a picture from a resource to the palette

        Args:
            description:        Description used for the tooltip
            name:               ID name
            picture_resource_id: Resource id of the picture
            page:               Page index
            expander_name:      Expander section name
            row_name:           Name of the row
            height:             Control height, only used for a row
            width:              Control width, only used for a row
        """

        self.cpp_palette_builder.AddResourcePicture(description,
                                                    name,
                                                    picture_resource_id,
                                                    page,
                                                    expander_name,
                                                    row_name,
                                                    height,
                                                    width)

        picture_view_model = PictureParameterViewModel()

        # compose the parameter name to ensure unique name
        # this can be removed later once the whole palette is build from python

        unique_name = f"{name}_{picture_resource_id}"

        WpfPaletteBuilder.set_base_viewmodel_properties(picture_view_model, description, unique_name, True, height, width, "")

        picture_view_model.CreateImageFromResourceID(picture_resource_id)

        picture_view_model.ConfigureAsResourceImage(height, width)

        self.view_model_builder.AddParameterToPalette(picture_view_model, page, expander_name, row_name, 0)

    def AddSeparator(self,
                     page          : int,
                     expander_name : str):
        """Add a separator to the palette

        Args:
            page:          Page index
            expander_name: Expander section name
        """

        self.cpp_palette_builder.AddSeparator(page,
                                              expander_name)

        self.view_model_builder.AddSeparatorToPalette(page, expander_name)

    def AddSteelGrade(self,
                      description    : str,
                      name           : str,
                      value          : int,
                      page           : int,
                      expander_name  : str,
                      row_name       : str,
                      b_enabled      : bool,
                      height         : int,
                      width          : int,
                      font_face_code : int):
        """Add a steel grade value to the palette

        Args:
            description:   Description
            name:          Value name
            value:         Value
            page:          Page index
            expander_name: Expander section name
            row_name:      Name of the row
            b_enabled:     Control is enabled: true/false
            height:        Control height, only used for a row
            width:         Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddSteelGrade(description,
                                               name,
                                               value,
                                               page,
                                               expander_name,
                                               row_name,
                                               b_enabled,
                                               height,
                                               width,
                                               font_face_code)

        combobox_view_model = ReinforcementResourceComboboxViewModel()

        PythonPaletteResourceProvider.InitializeSteelGradeCombobox(combobox_view_model, value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width,"")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def AddStringValue(self,
                       description      : str,
                       name             : str,
                       str_value        : str,
                       page             : int,
                       expander_name    : str,
                       row_name         : str,
                       b_enabled        : bool,
                       height           : int,
                       width            : int,
                       font_face_code   : int,
                       background_color : (list[int] | AllplanUtil.VecIntList)):
        """Add a string value to the palette

        Args:
            description:      Description
            name:             Value name
            str_value:        String
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        self.cpp_palette_builder.AddStringValue(description,
                                                name,
                                                str_value,
                                                page,
                                                expander_name,
                                                row_name,
                                                b_enabled,
                                                height,
                                                width,
                                                font_face_code,
                                                background_color)

        string_view_model = StringEditParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(string_view_model, description, name, b_enabled, height, width, "")

        string_view_model.InitializeValue(str_value)
        string_view_model.SetBackgroundColor(background_color[0], background_color[1], background_color[2])

        self.view_model_builder.AddParameterToPalette(string_view_model, page, expander_name, row_name, font_face_code)

    def AddStroke(self,
                  description    : str,
                  name           : str,
                  value          : int,
                  page           : int,
                  expander_name  : str,
                  row_name       : str,
                  b_enabled      : bool,
                  height         : int,
                  width          : int,
                  font_face_code : int):
        """Add a stroke value to the palette

        Args:
            description:   Description
            name:          Value name
            value:         Value
            page:          Page index
            expander_name: Expander section name
            row_name:      Name of the row
            b_enabled:     Control is enabled: true/false
            height:        Control height, only used for a row
            width:         Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddStroke(description,
                                           name,
                                           value,
                                           page,
                                           expander_name,
                                           row_name,
                                           b_enabled,
                                           height,
                                           width,
                                           font_face_code)

        stroke_view_model = StrokeComboboxViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(stroke_view_model, description, name, b_enabled, height, width, "")

        stroke_view_model.SelectedValue.Value = value

        self.view_model_builder.AddParameterToPalette(stroke_view_model, page, expander_name, row_name, font_face_code)

    def AddSurfaceCatalogRef(self,
                             description    : str,
                             name           : str,
                             value          : str,
                             page           : int,
                             expander_name  : str,
                             row_name       : str,
                             b_enabled      : bool,
                             height         : int,
                             width          : int,
                             font_face_code : int):
        """Add a surface catalog reference

        Args:
            description:   Description
            name:          Value name
            value:         Value string
            page:          Page index
            expander_name: Expander section name
            row_name:      Name of the row
            b_enabled:     Control is enabled: true/false
            height:        Control height, only used for a row
            width:         Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddSurfaceCatalogRef(description,
                                                      name,
                                                      value,
                                                      page,
                                                      expander_name,
                                                      row_name,
                                                      b_enabled,
                                                      height,
                                                      width,
                                                      font_face_code)

        self._add_string_combobox(description, name, PythonPaletteResourceProvider.GetSurfaceCatalogValues(),
                                          value, page, expander_name, row_name, b_enabled, height, width, font_face_code)

    def AddText(self,
                description    : str,
                value          : str,
                orientation    : AllplanPalette.Orientation,
                page           : int,
                expander_name  : str,
                row_name       : str,
                b_enabled      : bool,
                height         : int,
                width          : int,
                font_style     : int,
                font_face_code : int):
        """Add a text

        Args:
            description:   Description
            value:         Value
            orientation:   Orientation
            page:          Page index
            expander_name: Expander section name
            row_name:      Name of the row
            b_enabled:     Control is enabled: true/false
            height:        Control height, only used for a row
            width:         Control width, only used for a row
            font_style:    Font size: 0=small, 1=extra small, 2=large
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """

        self.cpp_palette_builder.AddText(description,
                                         value,
                                         orientation,
                                         page,
                                         expander_name,
                                         row_name,
                                         b_enabled,
                                         height,
                                         width,
                                         font_style,
                                         font_face_code)

        text_view_model = TextParameterViewModel()

        WpfPaletteBuilder.set_base_viewmodel_properties(text_view_model, "", value, b_enabled, height, width, "")

        text_view_model.Text = value

        text_view_model.FontConfiguration.ConfigureFromFlags(font_face_code, font_style)

        text_view_model.SetTextAlignmentFromFlag(int(orientation)) # type: ignore[arg-type]

        self.view_model_builder.AddParameterToPalette(text_view_model, page, expander_name, row_name or description, font_face_code)

    def AddVolumeValue(self,
                       description      : str,
                       name             : str,
                       value            : float,
                       page             : int,
                       expander_name    : str,
                       row_name         : str,
                       b_enabled        : bool,
                       min_value        : float,
                       max_value        : float,
                       interval_value   : float,
                       as_slider        : bool,
                       height           : int,
                       width            : int,
                       font_face_code   : int,
                       background_color : (list[int] | AllplanUtil.VecIntList)):
        """Add a volume value to the palette

        Args:
            description:      Description
            name:             Value name
            value:            Value
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            min_value:        Minimal value
            max_value:        Maximal value
            interval_value:   Interval value for the slider
            as_slider:        Show as slider: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        self.cpp_palette_builder.AddVolumeValue(description,
                                                name,
                                                value,
                                                page,
                                                expander_name,
                                                row_name,
                                                b_enabled,
                                                min_value,
                                                max_value,
                                                interval_value,
                                                as_slider,
                                                height,
                                                width,
                                                font_face_code,
                                                background_color)

        self._add_double_type_value(DoubleValueType.Volume, description, name, value, page, expander_name, row_name, b_enabled,
                                   min_value, max_value, interval_value, as_slider, height, width, font_face_code, background_color)

    def AddWeightValue(self,
                       description      : str,
                       name             : str,
                       value            : float,
                       page             : int,
                       expander_name    : str,
                       row_name         : str,
                       b_enabled        : bool,
                       min_value        : float,
                       max_value        : float,
                       interval_value   : float,
                       as_slider        : bool,
                       height           : int,
                       width            : int,
                       font_face_code   : int,
                       background_color : (list[int] | AllplanUtil.VecIntList)):
        """Add a weight value to the palette

        Args:
            description:      Description
            name:             Value name
            value:            Value
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            min_value:        Minimal value
            max_value:        Maximal value
            interval_value:   Interval value for the slider
            as_slider:        Show as slider: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        self.cpp_palette_builder.AddWeightValue(description,
                                                name,
                                                value,
                                                page,
                                                expander_name,
                                                row_name,
                                                b_enabled,
                                                min_value,
                                                max_value,
                                                interval_value,
                                                as_slider,
                                                height,
                                                width,
                                                font_face_code,
                                                background_color)

        self._add_double_type_value(DoubleValueType.Weight, description, name, value, page, expander_name, row_name, b_enabled,
                                   min_value, max_value, interval_value, as_slider, height, width, font_face_code, background_color)

    def IsConcreteCoverPaletteUpdate(self,
                                     cover : float) -> bool:
        """Check for a palette update due to a new concrete cover

        Args:
            cover: Concrete cover

        Returns:
            Palette update: true/false
        """

        return PythonPaletteResourceProvider.IsConcreteCoverPaletteUpdate(cover)

    def Reset(self):
        """Reset the data
        """

        # Unregister all event handlers

        for viewmodel, handler in self._event_handlers:
            viewmodel.ValueChanged -= handler

        self._event_handlers.clear()

        self.cpp_palette_builder.Reset()
        self.view_model_builder.Reset()

    @staticmethod
    def set_base_viewmodel_properties(parameter_viewmodel : SimpleParameterViewModel,
                                      description         : str,
                                      name                : str,
                                      b_enabled           : bool,
                                      height              : int,
                                      width               : int,
                                      tooltip             : str):
        """Sets the basic properties that are common for all parameter view models.

        Args:
            parameter_viewmodel: The parameter view model instance.
            description:         The description of the parameter.
            name:                The name of the parameter.
            b_enabled:           Indicates whether the control is enabled.
            height:              The height of the control.
            width:               The width of the control.
            tooltip:             The tooltip text for the control.
        """

        parameter_viewmodel.Description   = description
        parameter_viewmodel.ParameterName = name
        parameter_viewmodel.IsEnabled     = b_enabled
        parameter_viewmodel.Tooltip       = tooltip

        if height > 0:
            parameter_viewmodel.Height = height

        if width > 0:
            parameter_viewmodel.WeightedWidth = width

    def _add_double_type_value(self,
                              double_type      : DoubleValueType,
                              description      : str,
                              name             : str,
                              value            : float,
                              page             : int,
                              expander_name    : str,
                              row_name         : str,
                              b_enabled        : bool,
                              min_value        : float,
                              max_value        : float,
                              interval_value   : float,
                              as_slider        : bool,
                              height           : int,
                              width            : int,
                              font_face_code   : int,
                              background_color : (list[int] | AllplanUtil.VecIntList)):
        """Add a double type value to the palette

        Args:
            double_type:      Type of the double value (double, length...)
            description:      Description
            name:             Value name
            value:            Value
            page:             Page index
            expander_name:    Expander section name
            row_name:         Name of the row
            b_enabled:        Control is enabled: true/false
            min_value:        Minimal value
            max_value:        Maximal value
            interval_value:   Interval value for the slider
            as_slider:        Show as slider: true/false
            height:           Control height, only used for a row
            width:            Control width, only used for a row
            font_face_code:   Face code: 0=normal, 1=bold, 2=italic, 4=underline
            background_color: Background color of the control as red, green, blue
        """

        tooltip = description if row_name else ""

        if as_slider:
            double_view_model = DoubleSliderParameterViewModel(double_type)
            double_view_model.InitializeValues(value, min_value, max_value, interval_value)

        else:
            double_view_model = DoubleEditParameterViewModel(double_type)
            double_view_model.InitializeValues(value, min_value, max_value)
            double_view_model.SetBackgroundColor(background_color[0], background_color[1], background_color[2])

        WpfPaletteBuilder.set_base_viewmodel_properties(double_view_model, description, name, b_enabled, height, width, tooltip)

        self.view_model_builder.AddParameterToPalette(double_view_model, page, expander_name, row_name, font_face_code)

    def _add_string_combobox(self,
                             description    : str,
                             name           : str,
                             values_list    : Any,
                             value          : str,
                             page           : int,
                             expander_name  : str,
                             row_name       : str,
                             b_enabled      : bool,
                             height         : int,
                             width          : int,
                             font_face_code : int):
        """Helper method to add a string combobox to the palette.

        Args:
            description:    Description
            name:           Value name
            values_list:    List of values as a managed List
            value:          Value string
            page:           Page index
            expander_name:  Expander section name
            row_name:       Name of the row
            b_enabled:      Control is enabled: true/false
            height:         Control height, only used for a row
            width:          Control width, only used for a row
            font_face_code: Face code: 0=normal, 1=bold, 2=italic, 4=underline
        """
        combobox_view_model = StringComboboxViewModel()

        combobox_view_model.InitializeValues(values_list, value)

        WpfPaletteBuilder.set_base_viewmodel_properties(combobox_view_model, description, name, b_enabled, height, width, "")

        self.view_model_builder.AddParameterToPalette(combobox_view_model, page, expander_name, row_name, font_face_code)

    def _register_update_callback(self,
                                  parameter_viewmodel : ValueParameterViewModel,
                                  page                : int,):
        """Registers the handler for value change events of the parameter view model.

        Args:
            parameter_viewmodel: The parameter view model instance.
            page:                Page index where the parameter is located.
        """

        # Get the type of the parameter_viewmodel as a string

        parameter_type = type(parameter_viewmodel).__name__

        handler = self.change_handler.create_value_changed_handler(page, parameter_viewmodel.ParameterName, parameter_type)

        parameter_viewmodel.ValueChanged += handler

        self._event_handlers.append((parameter_viewmodel, handler))

```

</details>