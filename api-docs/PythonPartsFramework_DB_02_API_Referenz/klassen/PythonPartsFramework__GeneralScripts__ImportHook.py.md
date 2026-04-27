---
title: "ImportHook"
source: "PythonPartsFramework\GeneralScripts\ImportHook.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# ImportHook

> **Pfad:** `PythonPartsFramework\GeneralScripts\ImportHook.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

import hook for file decryption

## Abhängigkeiten

- `FileNameService`
- `NemAll_Python_Utility`
- `PathConstants`
- `importlib`
- `importlib.abc`
- `importlib.machinery`
- `os`
- `sys`
- `types`
- `typing`

## Klassen

### `ImportHookLoader`

import loader for encrypted files
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, enc_file_name: str` | `None` | initialize  Args:     enc_file_name: name of the encrypted file |
| `set_import_file_name` | `self, import_file_name: str` | `None` | set the import file name  Args:     import_file_name: import file name |
| `exec_module` | `self, module_spec: ModuleSpec` | `Optional[ModuleType]` | execute the module  Args:     module_spec: module spec  Returns:     loaded module |
| `reload_module` | `self, module_spec: ModuleSpec` | `Optional[ModuleType]` | reload the module  Args:     module_spec: module spec  Returns:     loaded module |
| `create_module` | `self, _module_spec` | `None` | - |
| `module_repr` | `self, module: ModuleType` | `str` | Return a module's repr  Args:     module: module string  Returns:     module string |

### `ImportHookFinder`

import load for encrypted files
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `find_spec` | `fullname: str, path: Optional[Sequence[str]], _target=None` | `Optional[ModuleSpec]` | find the spec  Args:     fullname: full file name     path:     path     _target:  target  Returns:     module spec |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" import hook for file decryption
"""

# pylint: disable=exec-used


import os
import sys

from typing import Sequence, Optional

from importlib.machinery import ModuleSpec
from importlib.abc import Loader, MetaPathFinder
from importlib import util
from types import ModuleType

import NemAll_Python_Utility as AllplanUtil

from FileNameService import FileNameService
from PathConstants import PathConstants

class ImportHookLoader(Loader):
    """  import loader for encrypted files
    """

    def __init__(self,
                 enc_file_name: str):
        """ initialize

        Args:
            enc_file_name: name of the encrypted file
        """

        super().__init__()

        self.enc_file_name    = enc_file_name
        self.import_file_name = ""


    def set_import_file_name(self,
                             import_file_name: str):
        """ set the import file name

        Args:
            import_file_name: import file name
        """

        self.import_file_name = import_file_name


    def exec_module(self,
                    module_spec: ModuleSpec) -> Optional[ModuleType]:
        """ execute the module

        Args:
            module_spec: module spec

        Returns:
            loaded module
        """

        if module_spec is None:
            return None

        if (module_spec_load := util.spec_from_loader(self.import_file_name, loader = None)) is None:
            return None

        module = util.module_from_spec(module_spec_load)

        module.__file__   = ""
        module.__reload__ = self.reload_module    # type:ignore

        sys.modules[self.import_file_name] = module

        with open(self.enc_file_name, "r", encoding="utf_8_sig") as file:
            code = file.read()

        AllplanUtil.ImportScript(code, module.__dict__, self.import_file_name.rsplit(".", 1)[-1])

        return module


    def reload_module(self,
                      module_spec: ModuleSpec) -> Optional[ModuleType]:
        """ reload the module

        Args:
            module_spec: module spec

        Returns:
            loaded module
        """

        return self.exec_module(module_spec)


    def create_module(self, _module_spec):
        return None


    def module_repr(self,
                    module: ModuleType) -> str:
        """ Return a module's repr

        Args:
            module: module string

        Returns:
            module string
        """

        return str(module)


class ImportHookFinder(MetaPathFinder):
    """  import load for encrypted files
    """

    @staticmethod
    def find_spec(fullname: str,
                  path    : Optional[Sequence[str]],
                  _target = None) -> Optional[ModuleSpec]:
        """ find the spec

        Args:
            fullname: full file name
            path:     path
            _target:  target

        Returns:
            module spec
        """

        if path is None or not path or \
           path[0].lower().find("\\prg\\python\\lib\\") != -1 or \
           path[0].lower().find("\\lib\\site-packages\\") != -1:
            return None

        import_file_name = fullname.split(".")

        enc_file_name_list = [path[0] + "\\" + import_file_name[-1] + ".pye"]

        for folder in PathConstants.PATH_KEYS_SEARCH_ORDER:
            enc_file_name_list.append(FileNameService.get_global_standard_path(folder + "\\PythonPartsScripts\\" + \
                                      "\\".join(import_file_name) + ".pye"))

        for enc_file_name in enc_file_name_list:
            if os.path.exists(enc_file_name):
                hook_loader = ImportHookLoader(enc_file_name)

                hook_loader.set_import_file_name(fullname)

                return util.spec_from_loader(fullname, loader = hook_loader)

        return None

```

</details>