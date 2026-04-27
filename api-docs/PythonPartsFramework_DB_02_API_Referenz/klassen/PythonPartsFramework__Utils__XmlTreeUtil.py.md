---
title: "XmlTreeUtil"
source: "PythonPartsFramework\Utils\XmlTreeUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
  - xml
related:
  -
last_updated: "2026-02-20"
---


# XmlTreeUtil

> **Pfad:** `PythonPartsFramework\Utils\XmlTreeUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`, `xml`

## Übersicht

Keine Modul-Docstring vorhanden.

## Abhängigkeiten

- `copy`
- `fnmatch`
- `os`
- `re`
- `xml.etree.ElementTree`

## Klassen

### `CommentedTreeBuilder`

Keine Klassen-Docstring vorhanden.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, *args, **kwargs` | `None` | - |
| `comment` | `self, data` | `None` | - |

### `XmlTreeUtil`

Keine Klassen-Docstring vorhanden.

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `indent` | `elem, level=0` | `None` | - |
| `get_tree_root` | `path` | `None` | - |
| `write_tree` | `tree, root, path` | `None` | - |
| `locate` | `pattern, root=os.curdir` | `None` | Locate all files matching supplied filename pattern in and below supplied root directory. |
| `add_xml_file` | `name, path` | `None` | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
import os
import re
import xml.etree.ElementTree as ET
import fnmatch

from copy import copy

class CommentedTreeBuilder(ET.TreeBuilder):
    def __init__(self, *args, **kwargs):
        super(CommentedTreeBuilder, self).__init__(*args, **kwargs)

    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


class XmlTreeUtil():

    @staticmethod
    def indent(elem, level=0):
        i = "\n" + level*"    "
        if len(elem):
          if not elem.text or not elem.text.strip():
            elem.text = i + "    "
          if not elem.tail or not elem.tail.strip():
            elem.tail = i
          for elem in elem:
            XmlTreeUtil.indent(elem, level+1)
          if not elem.tail or not elem.tail.strip():
            elem.tail = i
        else:
          if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


    @staticmethod
    def get_tree_root(path):
        parser = ET.XMLParser(target=CommentedTreeBuilder())

        try:
            tree = ET.parse(path, parser = parser)
        except:
            print("Not possible for " + path)
            return None, None

        root = tree.getroot()
        return tree, root

    @staticmethod
    def write_tree(tree, root, path):
        XmlTreeUtil.indent(root)
        tree.write(path, encoding = "utf-8", xml_declaration = True, short_empty_elements = False)


    @staticmethod
    def locate(pattern, root=os.curdir):
        '''Locate all files matching supplied filename pattern in and below
        supplied root directory.'''
        for path, dirs, files in os.walk(os.path.abspath(root)):
            for filename in fnmatch.filter(files, pattern):
                yield os.path.join(path, filename)


    @staticmethod
    def add_xml_file(name, path):
        root = ET.Element("Element")
        string_table = ET.SubElement(root, "StringTable")
        string_table.text = name + " stringtable"
        XmlTreeUtil.indent(root)
        tree = ET.ElementTree(root)
        tree.write(path, encoding = "utf-8", xml_declaration = True, short_empty_elements = False)




```

</details>