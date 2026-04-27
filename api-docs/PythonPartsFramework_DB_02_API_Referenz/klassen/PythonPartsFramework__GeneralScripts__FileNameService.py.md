---
title: "FileNameService"
source: "PythonPartsFramework\GeneralScripts\FileNameService.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
related:
  -
last_updated: "2026-02-20"
---


# FileNameService

> **Pfad:** `PythonPartsFramework\GeneralScripts\FileNameService.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`

## Übersicht

Implementation of the file name service

## Abhängigkeiten

- `PathConstants`
- `os`
- `pathlib`

## Klassen

### `FileNameService`

Definition of service class FileNameService
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `set_node_script_default_path` | `node_script_default_path: str` | `None` | Set the default path of the node scripts  Args:     node_script_default_path: description |
| `get_filename_without_root_path` | `str_file_name: str, str_path: str` | `str` | Cuts the root_path of the filename  Args:     str_file_name: Full file path     str_path:      Root directory path  Returns:     File path relative to the root directory  Examples:     >>> FileNameService.get_filename_without_root_path(     ...     "c:\programdata\Allplan\etc\library\python\macrocolumn.pyp",     ...     "c:\programdata\Allplan\etc\")     'library\python\macrocolumn.pyp' |
| `get_lib_pyp_sricpt_path` | `file_name: str` | `str` | Searches the file_name in the parts (Cur_proj, Std, Etc )of the library Cuts the library_path of the filename  Args:     file_name: name of file.  Returns:     str_file_name without lib_path  Examples:     >>> FileNameService.get_lib_pyp_sricpt_path("etc\library\python\macrocolumn.pyp")     'library\python\macrocolumn.pyp' |
| `get_pyp_path_from_lib_struct` | `file_name: str, extended_search: bool=False` | `tuple[bool, str]` | Searches the file_name in the parts (Cur_proj, Std, Etc ) of the library.  Args:     file_name:       name of file without lib_path     extended_search: search the filein all library folders if not found  Returns:     True when file exist state, False otherwise     str_file_name with lib_path      Examples:     >>> FileNameService.get_pyp_path_from_lib_struct("library\python\macrocolumn.pyp")      (True, 'c:\programdata\Allplan\etc\library\python\macrocolumn.pyp') |
| `search_pyp_file` | `file_name: str` | `tuple[bool, str]` | Searches the pyp file_name in all library folders in the parts (Cur_proj, Std, Etc )  Args:     file_name: name of file without lib_path  Returns:     True when file exist state, False otherwise     str_file_name with lib_path |
| `get_global_standard_path` | `local_path: str` | `str` | Get the absolute path from a path relative to etc/std/prj directory  Args:     local_path: local path  Returns:     global path (empty if not exist)  Examples:     >>> FileNameService.get_global_standard_path("etc\library\python\macrocolumn.pyp")     'C:\ProgramData\Allplan\Etc\library\python\macrocolumn.pyp' |
| `update_global_standard_path` | `global_path: str` | `str` | update the global standard path for a new location  Args:     global_path: global path  Returns:     updated global path (empty if not exists) |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Implementation of the file name service
"""

# pylint: disable=global-statement

import os
import pathlib

from PathConstants import PathConstants

STATIC_NODE_SCRIPT_DEFAULT_PATH = ""
DELIVERY_DATA_PATH              = r"\deliverydata"
LIBRARY_EXAMPLES_PATH           = "Library\\Examples\\"

class FileNameService():
    """ Definition of service class FileNameService
    """

    @staticmethod
    def set_node_script_default_path(node_script_default_path: str):
        """ Set the default path of the node scripts

        Args:
            node_script_default_path: description
        """

        global STATIC_NODE_SCRIPT_DEFAULT_PATH

        STATIC_NODE_SCRIPT_DEFAULT_PATH = node_script_default_path


    @staticmethod
    def get_filename_without_root_path(str_file_name: str,
                                       str_path     : str) -> str:
        """ Cuts the root_path of the filename

        Args:
            str_file_name: Full file path
            str_path:      Root directory path

        Returns:
            File path relative to the root directory

        Examples:
            >>> FileNameService.get_filename_without_root_path(
            ...     "c:\\programdata\\Allplan\\etc\\library\\python\\macrocolumn.pyp",
            ...     "c:\\programdata\\Allplan\\etc\\")
            'library\\python\\macrocolumn.pyp'

        """

        return str_file_name[len(str_path):]


    @staticmethod
    def get_lib_pyp_sricpt_path(file_name: str) -> str:
        """ Searches the file_name in the parts (Cur_proj, Std, Etc )of the library
        Cuts the library_path of the filename

        Args:
            file_name: name of file.

        Returns:
            str_file_name without lib_path

        Examples:
            >>> FileNameService.get_lib_pyp_sricpt_path("etc\\library\\python\\macrocolumn.pyp")
            'library\\python\\macrocolumn.pyp'
        """

        for path in PathConstants.PYP_SEARCH_PATHS:
            if file_name.startswith(path):
                str_res = FileNameService.get_filename_without_root_path(file_name, path)
                return str_res

        return file_name


    @staticmethod
    def get_pyp_path_from_lib_struct(file_name      : str,
                                     extended_search: bool = False) -> tuple[bool, str]:
        """ Searches the file_name in the parts (Cur_proj, Std, Etc ) of the library.

        Args:
            file_name:       name of file without lib_path
            extended_search: search the filein all library folders if not found

        Returns:
            True when file exist state, False otherwise
            str_file_name with lib_path

            Examples:
            >>> FileNameService.get_pyp_path_from_lib_struct("library\python\macrocolumn.pyp")

            (True, 'c:\programdata\Allplan\etc\library\python\macrocolumn.pyp')
        """

        if os.path.isfile(file_name):
            return True, file_name

        for path in PathConstants.PYP_SEARCH_PATHS:
            file = path + file_name.split("\\", 1)[-1] if DELIVERY_DATA_PATH in path.lower() and \
                                                          LIBRARY_EXAMPLES_PATH in file_name else path + file_name     # for development

            if os.path.isfile(file):
                return True, file

        return FileNameService.search_pyp_file(file_name) if extended_search else (False, "")


    @staticmethod
    def search_pyp_file(file_name: str) -> tuple[bool, str]:
        """ Searches the pyp file_name in all library folders in the parts (Cur_proj, Std, Etc )

        Args:
            file_name: name of file without lib_path

        Returns:
            True when file exist state, False otherwise
            str_file_name with lib_path
        """

        file_name = os.path.basename(file_name)

        for path in PathConstants.PYP_SEARCH_PATHS:
            library_path = pathlib.Path(path + ("" if DELIVERY_DATA_PATH in path.lower() else "Library"))

            for file in library_path.rglob(file_name):
                return True, str(file)

        return False, ""


    @staticmethod
    def get_global_standard_path(local_path: str) -> str:
        """ Get the absolute path from a path relative to etc/std/prj directory

        Args:
            local_path: local path

        Returns:
            global path (empty if not exist)

        Examples:
            >>> FileNameService.get_global_standard_path("etc\\library\\python\\macrocolumn.pyp")
            'C:\\ProgramData\\Allplan\\Etc\\library\\python\\macrocolumn.pyp'
        """

        lower_local_path = local_path.lower()

        for folder, path in PathConstants.KEY_PATH_TUPLES:
            if lower_local_path.startswith(folder + "\\") or \
               lower_local_path.startswith(folder + ".") and folder != PathConstants.PRJ_PATH:
                if (ip_vs := lower_local_path.find("\\visualscripts\\")) != -1:
                    return path + local_path[ip_vs + 1:]

                return path + local_path[local_path.find("\\") + 1:]

        return ""


    @staticmethod
    def update_global_standard_path(global_path: str) -> str:
        """ update the global standard path for a new location

        Args:
            global_path: global path

        Returns:
            updated global path (empty if not exists)
        """

        if os.path.exists(global_path):
            return global_path

        lower_global_path = global_path.lower()

        for folder, path in PathConstants.KEY_PATH_TUPLES:
            if (ip_folder := lower_global_path.find("\\" + folder + "\\")) != -1:
                global_path = path + global_path[ip_folder + 4:]

                if os.path.exists(global_path):
                    return global_path

                return ""

        return ""

```

</details>