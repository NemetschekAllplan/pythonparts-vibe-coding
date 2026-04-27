---
title: "BuildingElementCompositeReader"
source: "PythonPartsFramework\GeneralScripts\BuildingElementCompositeReader.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementCompositeReader

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementCompositeReader.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the build element composite reader

## Abhängigkeiten

- `BuildingElementCompositeData`
- `BuildingElementStringTable`
- `StringTableService`
- `ValueTypes.ValueTypeUtils.StringToValueUtil`
- `XMLReader.XmlElementTreeUtil`
- `re`
- `xml.etree`

## Klassen

### `BuildingElementCompositeReader`

Implementation of class BuildingElementCompositeReader
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `read_property_palette_layout` | `doc_ele: ElementTree.ElementTree, build_ele_str_table: BuildingElementStringTable, sub_ele_palette_data: dict[str, PaletteData]` | `None` | read the data for the property palette layout  Args:     doc_ele:              xml document     build_ele_str_table:  building element string table     sub_ele_palette_data: sub element palette data |
| `read_data_from_pyp` | `doc_ele: ElementTree.ElementTree, is_node_script: bool, version: float, composite_data: BuildingElementCompositeData` | `None` | Read the data from the pyp file  Args:     doc_ele:        xml document     is_node_script: is node script state     version:        version     composite_data: composite data |
| `__read_default_values` | `node: ElementTree.Element, sub_ele_defaults: list[DefaultValues]` | `None` | read the default values  Args:     node:             node     sub_ele_defaults: default values of the sub element |
| `__read_default_values_14` | `node: ElementTree.Element, sub_ele_defaults: list[DefaultValues]` | `None` | read the default values  Args:     node:             node     sub_ele_defaults: default values of the sub element |
| `__read_constraints` | `node: ElementTree.Element, sub_ele_constraints: list[Constraint], sub_ele_id: list[str], is_node_script: bool` | `None` | read the constraints  Args:     node:                xml node     sub_ele_constraints: constraints of the sub element     sub_ele_id:          sub element IDs     is_node_script:      node script state |
| `__read_constraints_14` | `node: ElementTree.Element, sub_ele_constraints: list[Constraint], sub_ele_id: list[str], is_node_script: bool` | `None` | read the constraints  Args:     node:                xml node     sub_ele_constraints: constraints of the sub element     sub_ele_id:          sub element IDs     is_node_script:      node script state |
| `create_constraint_formula` | `sub_ele_id: list[str], formula_text: str, fetched_value: str='.value'` | `str` | create the constraint formula from the formula text (replace the xx: with the building element index)  Args:     sub_ele_id:    sub element IDs     formula_text:  formula text     fetched_value: fetched value  Returns:     constrained formula |
| `__get_build_ele_index` | `sub_ele_id: list[str], build_ele_id: str` | `int` | get the index of the building element by the ID  Args:     sub_ele_id:   sub element IDs     build_ele_id: id fo find  Returns:     index of the ID |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the build element composite reader
"""

from xml.etree import ElementTree

import re

from BuildingElementCompositeData import BuildingElementCompositeData, PaletteData, DefaultValues, Constraint
from BuildingElementStringTable import BuildingElementStringTable
from StringTableService import StringTableService

from XMLReader.XmlElementTreeUtil import XmlElementTreeUtil

from ValueTypes.ValueTypeUtils.StringToValueUtil import StringToValueUtil

class BuildingElementCompositeReader:
    """ Implementation of class BuildingElementCompositeReader
    """

    @staticmethod
    def read_property_palette_layout(doc_ele             : ElementTree.ElementTree,
                                     build_ele_str_table : BuildingElementStringTable,
                                     sub_ele_palette_data: dict[str,PaletteData]):
        """ read the data for the property palette layout

        Args:
            doc_ele:              xml document
            build_ele_str_table:  building element string table
            sub_ele_palette_data: sub element palette data
        """

        page_index    = -1
        control_index = 0

        for node in XmlElementTreeUtil.get_elements_by_tag_name(doc_ele, "PropertyPalette"):
            for page, _, _ in XmlElementTreeUtil.get_elements(node):
                page_textid_attr = XmlElementTreeUtil.get_attribute(page, "TextId")
                page_text_attr   = XmlElementTreeUtil.get_attribute(page, "Text")

                page_text = StringTableService.get_string_table_entry(build_ele_str_table,
                                                                      "" if page_textid_attr is None else page_textid_attr,
                                                                      "" if page_text_attr   is None else page_text_attr)

                expanders = XmlElementTreeUtil.get_elements(page)

                page_index_start = page_index

                for expander, _, _ in expanders:
                    expander_textid_attr = XmlElementTreeUtil.get_attribute(expander, "TextId")
                    expander_text_attr   = XmlElementTreeUtil.get_attribute(expander, "Text")

                    expander_text = StringTableService.get_string_table_entry(build_ele_str_table,
                                                                              "" if expander_textid_attr is None else expander_textid_attr,
                                                                              "" if expander_text_attr   is None else expander_text_attr)

                    for expander_node, _, _ in XmlElementTreeUtil.get_elements(expander):
                        if page_index_start == page_index:
                            page_index += 1

                        id_attr = XmlElementTreeUtil.get_attribute(expander_node, "ID")

                        sub_ele_palette_data[("" if id_attr is None else id_attr) + "___"] = \
                            PaletteData(page_index, control_index, page_text, page_textid_attr, expander_text, expander_textid_attr)

                        control_index += 1

    @staticmethod
    def read_data_from_pyp(doc_ele       : ElementTree.ElementTree,
                           is_node_script: bool,
                           version       : float,
                           composite_data: BuildingElementCompositeData):
        """ Read the data from the pyp file

        Args:
            doc_ele:        xml document
            is_node_script: is node script state
            version:        version
            composite_data: composite data
        """

        for ele in XmlElementTreeUtil.get_elements_by_tag_name(doc_ele, "SubElement"):
            ele_defaults    : list[DefaultValues] = []
            ele_constraints : list[Constraint]    = []
            ele_composite   : list[str]           = []
            ele_visible     : str                 = "True"
            ele_page_index  : int                 = 0
            ele_script_uuid : str                 = ""

            for node, name, value in XmlElementTreeUtil.get_elements(ele):
                if value is None:
                    continue

                if name == "PyP":
                    composite_data.sub_ele_script_name.append(value)

                elif name == "Uuid":
                    ele_script_uuid = value

                elif name == "PageIndex":
                    if value:
                        ele_page_index = int(value)

                elif name == "Name":
                    composite_data.sub_ele_name.append(value)

                elif name == "ID":
                    composite_data.sub_ele_id.append(value)

                elif name == "Visible":
                    ele_visible = BuildingElementCompositeReader.create_constraint_formula(composite_data.sub_ele_id, value)

                elif name == "Values":
                    ele_defaults = [DefaultValues(value_name, value_value, "True", "", None, None, None) \
                                                  for _, value_name, value_value in XmlElementTreeUtil.get_elements(node)]

                elif name == "Composite":
                    if value is not None:
                        ele_composite = value.split(",")

                elif name == "DefaultValues":
                    if is_node_script and version > 1.39:
                        BuildingElementCompositeReader.__read_default_values_14(node, ele_defaults)
                    else:
                        BuildingElementCompositeReader.__read_default_values(node, ele_defaults)

                elif name == "Constraints":
                    if is_node_script and version > 1.39:
                        BuildingElementCompositeReader.__read_constraints_14(node, ele_constraints, composite_data.sub_ele_id,
                                                                             is_node_script)
                    else:
                        BuildingElementCompositeReader.__read_constraints(node, ele_constraints, composite_data.sub_ele_id,
                                                                          is_node_script)

            composite_data.sub_ele_visible.append(ele_visible)
            composite_data.sub_ele_defaults.append(ele_defaults)
            composite_data.sub_ele_constraints.append(ele_constraints)
            composite_data.sub_ele_composite.append(ele_composite)
            composite_data.sub_ele_page_index.append(ele_page_index)
            composite_data.sub_ele_script_uuid.append(ele_script_uuid)


    @staticmethod
    def __read_default_values(node            : ElementTree.Element,
                              sub_ele_defaults: list[DefaultValues]):
        """ read the default values

        Args:
            node:             node
            sub_ele_defaults: default values of the sub element
        """

        for default_node, value_name, _ in XmlElementTreeUtil.get_elements(node):
            value_value         = ""
            value_visible       = ""
            value_text          = ""
            value_list_state    = None
            value_list_reverse  = None
            value_list_squeeze  = None

            def check_text_id(attrib: dict[str, str],
                              value : str) -> str:
                """ check text id

                Args:
                    attrib: attribute
                    value:  value

                Returns:
                    adapted value with text ID
                """

                if "TextId" in attrib:
                    return value + " {" + attrib["TextId"] + "}"

                return value


            #---------------- read the default values

            for _, name, value, attrib in XmlElementTreeUtil.get_elements_with_attrib(default_node):
                if name == "Value" and value is not None:
                    value_value = check_text_id(attrib, value)

                elif name == "Visible":
                    value_visible = value

                elif name == "Text" and value is not None:
                    value_text = check_text_id(attrib, value)

                elif name == "ListState":
                    if value:
                        value_list_state = int(value)

                elif name == "ListReverse" and value is not None:
                    value_list_reverse = StringToValueUtil.get_bool_value_from_str(value)

                elif name == "ListSqueeze" and value is not None:
                    value_list_squeeze = StringToValueUtil.get_bool_value_from_str(value)

            sub_ele_defaults.append(DefaultValues(value_name, value_value, value_visible, value_text,
                                                  value_list_state, value_list_reverse, value_list_squeeze))


    @staticmethod
    def __read_default_values_14(node            : ElementTree.Element,
                                 sub_ele_defaults: list[DefaultValues]):
        """ read the default values

        Args:
            node:             node
            sub_ele_defaults: default values of the sub element
        """

        for default_node, _, def_value in XmlElementTreeUtil.get_elements(node):
            def_name          = XmlElementTreeUtil.get_attribute(default_node, "Name")
            def_visible       = value if (value := XmlElementTreeUtil.get_attribute(default_node, "Visible")) is not None else ""
            def_text          = value if (value := XmlElementTreeUtil.get_attribute(default_node, "Text")) is not None else ""
            def_text_id       = value if (value := XmlElementTreeUtil.get_attribute(default_node, "TextId")) is not None else None
            def_list_state    = int(value) \
                                if (value := XmlElementTreeUtil.get_attribute(default_node, "ListState")) is not None else None
            def_list_reverse  = StringToValueUtil.get_bool_value_from_str(value) \
                                if (value := XmlElementTreeUtil.get_attribute(default_node, "ListReverse")) is not None else None
            def_list_squeeze  = StringToValueUtil.get_bool_value_from_str(value) \
                                if (value := XmlElementTreeUtil.get_attribute(default_node, "ListSqueeze")) is not None else None

            if def_visible == "false":
                def_visible = "False"

            if def_value is None:
                def_value = ""

            def check_text_id(value  : str,
                              text_id: (str | None)) -> str:
                """ check the text id

                Args:
                    value:   value
                    text_id: text id

                Returns:
                     adapted value with text ID
                """
                if text_id is not None:
                    return value + " {" + text_id + "}"

                return value

            if def_text:
                def_text = check_text_id(def_text, def_text_id)

            sub_ele_defaults.append(DefaultValues(def_name, def_value, def_visible, def_text,
                                                  def_list_state, def_list_reverse, def_list_squeeze))


    @staticmethod
    def __read_constraints(node               : ElementTree.Element,
                           sub_ele_constraints: list[Constraint],
                           sub_ele_id         : list[str],
                           is_node_script     : bool):
        """ read the constraints

        Args:
            node:                xml node
            sub_ele_constraints: constraints of the sub element
            sub_ele_id:          sub element IDs
            is_node_script:      node script state
        """

        for constraint_node, value_name, _ in XmlElementTreeUtil.get_elements(node):
            value_value         = ""
            value_type          = ""
            value_condition     = "True"
            value_visible       = "False" if is_node_script else ""
            value_list_state    = None
            value_list_reverse  = None

            for _, name, value in XmlElementTreeUtil.get_elements(constraint_node):
                if value is None:
                    continue

                if name == "Value":
                    value_value = BuildingElementCompositeReader.create_constraint_formula(sub_ele_id, value)
                    value_type = BuildingElementCompositeReader.create_constraint_formula(sub_ele_id, value,
                                                                                          fetched_value = ".value_type")

                elif name == "Condition":
                    value_condition = BuildingElementCompositeReader.create_constraint_formula(sub_ele_id, value)

                elif name == "Visible":
                    value_visible = BuildingElementCompositeReader.create_constraint_formula(sub_ele_id, value)

                elif name == "ListState":
                    if value:
                        value_list_state = int(value)

                elif name == "ListReverse":
                    value_list_reverse = StringToValueUtil.get_bool_value_from_str(value)

            sub_ele_constraints.append(Constraint(value_name, value_value, value_type, value_condition, value_visible,
                                                  value_list_state, value_list_reverse))


    @staticmethod
    def __read_constraints_14(node               : ElementTree.Element,
                              sub_ele_constraints: list[Constraint],
                              sub_ele_id         : list[str],
                              is_node_script     : bool):
        """ read the constraints

        Args:
            node:                xml node
            sub_ele_constraints: constraints of the sub element
            sub_ele_id:          sub element IDs
            is_node_script:      node script state
        """

        for constraint_node, _, _ in XmlElementTreeUtil.get_elements(node):
            if (const_name := XmlElementTreeUtil.get_attribute(constraint_node, "Name")) is None:
                continue

            const_list_state    = int(value) \
                                if (value := XmlElementTreeUtil.get_attribute(constraint_node, "ListState")) is not None else None
            const_list_reverse  = StringToValueUtil.get_bool_value_from_str(value) \
                                if (value := XmlElementTreeUtil.get_attribute(constraint_node, "ListReverse")) is not None else None

            const_links         = []
            const_type          = ""
            const_condition     = "True"
            const_visible       = "False" if is_node_script else ""

            for constraint, name, value in XmlElementTreeUtil.get_elements(constraint_node):
                if name == "Link":
                    node_id    = XmlElementTreeUtil.get_attribute(constraint, "NodeId")
                    node_name  = XmlElementTreeUtil.get_attribute(constraint, "Name")

                    if node_id is not None and node_name is not None:
                        const_links.append(node_id + ":" + node_name)

                elif name == "ListState":
                    if value:
                        const_list_state = int(value)

                elif name == "ListReverse" and value is not None:
                    const_list_reverse = StringToValueUtil.get_bool_value_from_str(value)

            if (const_value := ",".join(const_links)):
                const_type  = BuildingElementCompositeReader.create_constraint_formula(sub_ele_id, const_value,
                                                                                       fetched_value = ".value_type")
                const_value = BuildingElementCompositeReader.create_constraint_formula(sub_ele_id, const_value)

                if len(const_links) > 1:
                    const_value = "[" + const_value + "]"

            sub_ele_constraints.append(Constraint(const_name, const_value, const_type, const_condition, const_visible,
                                                  const_list_state, const_list_reverse))


    @staticmethod
    def create_constraint_formula(sub_ele_id   : list[str],
                                  formula_text : str,
                                  fetched_value: str = ".value") -> str:
        """ create the constraint formula from the formula text
        (replace the xx: with the building element index)

        Args:
            sub_ele_id:    sub element IDs
            formula_text:  formula text
            fetched_value: fetched value

        Returns:
            constrained formula
        """

        formula = formula_text

        while (ipos := formula.find(":")) != -1:
            left_str  = formula[:ipos]
            right_str = formula[ipos + 1:]


            #----------------- get the building element ID

            istart = -1

            for i in range(len(left_str) - 1, -1, -1):
                if (char := left_str[i]) in {" ", "-", ",", "(", "["}:
                    istart = i
                    break

            formula_left = "" if istart == -1 else left_str[:istart + 1]

            formula = "build_ele_list[" + str(BuildingElementCompositeReader.__get_build_ele_index(sub_ele_id, left_str[istart + 1:])) + "]"


            #----------------- get the value

            if not (match := re.compile(r"\ |\.|\,|\]|\[|\)").search(right_str)):
                formula = formula_left + formula

                if right_str:
                    formula += ".get_property(\"" + right_str + "\")" + fetched_value
            else:
                iend = match.start()

                if not right_str[iend].startswith("."):
                    formula = formula_left + formula + ".get_property(\"" + right_str[:iend] + "\")" + fetched_value + right_str[iend:]
                else:
                    formula += ".get_property(\"" + right_str[:iend] + "\")" + fetched_value

                    right_str = right_str[iend:]

                    iend = -1

                    for i, char in enumerate(right_str):
                        if char in [" ", ",", ")", "]"]:
                            iend = i
                            break

                    sub_value = right_str if iend == -1 else right_str[:iend]

                    if fetched_value == ".value_type":
                        sub_value = ""

                    formula = formula_left + "(" + formula + sub_value + " if not isinstance(" + formula + \
                              ",list) else get_values_from_list(" + formula + ", \"" + sub_value[1:] + "\"))"

                    if iend != -1:
                        formula += right_str[iend:]

        return formula


    @staticmethod
    def __get_build_ele_index(sub_ele_id  : list[str],
                              build_ele_id: str) -> int:
        """ get the index of the building element by the ID

        Args:
            sub_ele_id:   sub element IDs
            build_ele_id: id fo find

        Returns:
            index of the ID
        """

        return next((i + 1 for i, sub_ele_id in enumerate(sub_ele_id) if sub_ele_id == build_ele_id), -1)

```

</details>