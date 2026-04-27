---
title: "BuildingElementXMLInclude"
source: "PythonPartsFramework\GeneralScripts\BuildingElementXMLInclude.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - xml
related:
  -
last_updated: "2026-02-20"
---


# BuildingElementXMLInclude

> **Pfad:** `PythonPartsFramework\GeneralScripts\BuildingElementXMLInclude.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `xml`

## Übersicht

Definition of class BuildingElementXMLInclude

## Abhängigkeiten

- `BuildingElementStringTable`
- `FileNameService`
- `NemAll_Python_AllplanSettings`
- `NemAll_Python_Utility`
- `io`
- `os`
- `pathlib`

## Klassen

### `BuildingElementXMLInclude`

Definition of class BuildingElementXMLInclude
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__write_include_file` | `inc_file_name: str, str_table: BuildingElementStringTable | None, name_index_text: str, text_inc: str, is_index: bool, file_out: TextIOWrapper, encode: str` | `None` | Write the data from the include file  Args:     inc_file_name:   include file name     str_table:       string table     name_index_text: name index text     text_inc:        text include     is_index:        is index state     file_out:        out file     encode:          encoding |
| `__include_position` | `line: str` | `int` | Get the position of the include statement  Args:     line: line  Returns:     include position |
| `get_final_pyp_file` | `pyp_filename: str` | `str` | Get the final pyp file  Args:     pyp_filename: pyp file name  Returns:     name of the final pyp file |
| `__get_text_from_str_table` | `str_table: BuildingElementStringTable, text_id_tag: str, text_tag: str, iblank: int, text: str` | `str` | get the text from the string table  Args:     str_table:   string table     text_id_tag: text ID tag     text_tag:    text tag     iblank:      index of the blank char     text:        text  Returns:     text from the string table |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Definition of class BuildingElementXMLInclude
"""

from io import TextIOWrapper

import os
import pathlib

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_Utility as AllplanUtil

from FileNameService import FileNameService
from BuildingElementStringTable import BuildingElementStringTable

ORG_LIST_KEY  = "$list_"
TEMP_LIST_KEY = "@list_"

class BuildingElementXMLInclude():
    """ Definition of class BuildingElementXMLInclude
    """

    @staticmethod
    def __write_include_file(inc_file_name  : str,
                             str_table      : (BuildingElementStringTable | None),
                             name_index_text: str,
                             text_inc       : str,
                             is_index       : bool,
                             file_out       : TextIOWrapper,
                             encode         : str):
        """ Write the data from the include file

        Args:
            inc_file_name:   include file name
            str_table:       string table
            name_index_text: name index text
            text_inc:        text include
            is_index:        is index state
            file_out:        out file
            encode:          encoding
        """

        inc_file_name = inc_file_name.strip().replace("\n","")

        path = pathlib.Path(inc_file_name)

        if not path.exists():
            AllplanUtil.ShowMessageBox(f"Include file {inc_file_name} not found!!!", AllplanUtil.MB_OK)

            return


        #----------------- transform the file

        text_line       = ""
        value_line      = ""
        value_list_line = ""

        with open(inc_file_name, 'r', encoding = encode) as inc_file:
            for inc_line in inc_file:
                text = inc_line.replace("#", text_inc)

                if ORG_LIST_KEY in text:
                    text = text.replace(ORG_LIST_KEY, TEMP_LIST_KEY).replace("$", name_index_text).replace(TEMP_LIST_KEY, ORG_LIST_KEY)
                else:
                    text = text.replace("$", name_index_text)


                #----------------- manage the text

                if str_table:
                    if text.find("</Text>") != -1:
                        if not text_line:
                            text_line = text

                        continue

                    if text.find("</Value>") != -1:
                        if not value_line:
                            value_line = text

                        continue

                    if text.find("</ValueList>") != -1:
                        if not value_list_line:
                            value_list_line = text

                        continue

                if text.find("</Parameter>") != -1 or text.find("<Parameter>") != -1:
                    if text_line:
                        file_out.write(text_line)
                        file_out.write(text_line[:text_line.find("<")] + "<TextId>0</TextId>\n")

                    if value_line:
                        file_out.write(value_line)

                    if value_list_line:
                        file_out.write(value_list_line)

                    text_line       = ""
                    value_line      = ""
                    value_list_line = ""


                #----------------- append the name index, write the text include for inserting in the text from the TextId

                iblank = text.find("<")

                if (ipos := text.find("</Name>")) != -1:
                    text = text[:ipos] + name_index_text + text[ipos:]

                    if text_inc:
                        if is_index:
                            file_out.write(text[:iblank] + "<TextIndex>" + text_inc + "</TextIndex>\n")
                        else:
                            file_out.write(text[:iblank] + "<TextInc>" + text_inc + "</TextInc>\n")


                #----------------- new text for the include file string table

                if str_table and text.find("TextId") != -1:


                    if (res_text := BuildingElementXMLInclude.__get_text_from_str_table(str_table, "</TextId>", "Text",
                                                                                        iblank, text)):
                        text_line = res_text
                        continue

                    if (res_text := BuildingElementXMLInclude.__get_text_from_str_table(str_table, "</ValueTextId>", "Value",
                                                                                        iblank, text)):
                        value_line = res_text
                        continue

                    if (res_text := BuildingElementXMLInclude.__get_text_from_str_table(str_table, "</ValueList_TextIds>", "ValueList",
                                                                                        iblank, text)):
                        value_list_line = res_text
                        continue

                file_out.write(text)

        file_out.write("\n")

        inc_file.close()


    @staticmethod
    def __include_position(line: str) -> int:
        """ Get the position of the include statement

        Args:
            line: line

        Returns:
            include position
        """

        if line.find("<") != -1:
            return -1

        if (ipos := line.find("#include ")) == -1:
            return -1

        text = line.lstrip()

        if text.find("#include ") != 0:
            return -1

        if text.strip() == "#include":
            return -1

        return ipos


    @staticmethod
    def get_final_pyp_file(pyp_filename: str) -> str:
        """ Get the final pyp file

        Args:
            pyp_filename: pyp file name

        Returns:
            name of the final pyp file
        """

        pyp_path, _ = os.path.split(pyp_filename)

        new_pyp_filename = pyp_path + "\\___pyp__"


        #----------------- transfer the data

        def transfer_data(encode):
            with open(new_pyp_filename, 'w', encoding = encode) as file_out:
                with open(pyp_filename, 'r', encoding = encode) as file_in:
                    for line in file_in:
                        if (ipos := BuildingElementXMLInclude.__include_position(line)) == -1:
                            file_out.write(line)

                            continue


                        #----------------- get the language file

                        str_table = None

                        if (ip_lang := line.find("|LanguageFile=")) != -1:
                            language_file = line[ip_lang + 14:]

                            if not (global_lang_path := FileNameService.get_global_standard_path(language_file)):
                                global_lang_path = pyp_path + "\\" +language_file

                            str_table = BuildingElementStringTable(global_lang_path[:global_lang_path.rfind(".")] + ".pyp", True,
                                                                   AllplanSettings.AllplanLocalisationService.AllplanLanguage())

                            line = line[:ip_lang]


                        #----------------- get the include file

                        text_list = line[ipos + 9:].split(";")

                        if len(text_list) == 1:
                            text_list.append("")

                        if not (global_incl_path := FileNameService.get_global_standard_path(text_list[0])):
                            global_incl_path = pyp_path + "\\" + text_list[0]


                        #----------------- create new new parameter for the index and text

                        for itext in range(1, len(text_list)):
                            index_text = text_list[itext].strip().replace("\n","").split(",")

                            if len(index_text) == 1:
                                index_text.append("")

                            if (ipmin := index_text[0].find("-")) == -1:
                                BuildingElementXMLInclude.__write_include_file(global_incl_path, str_table,
                                                                               index_text[0], index_text[1], False, file_out, encode)
                            else:
                                for index in range(int(index_text[0][:ipmin]), int(index_text[0][ipmin + 1:]) + 1):
                                    BuildingElementXMLInclude.__write_include_file(global_incl_path, str_table,
                                                                                   str(index), str(index), True, file_out, encode)

                file_in.close()

            file_out.close()

        try:
            transfer_data("utf-8")

        except UnicodeDecodeError:
            transfer_data("utf-16")

        return new_pyp_filename


    @staticmethod
    def __get_text_from_str_table(str_table  : BuildingElementStringTable,
                                  text_id_tag: str,
                                  text_tag   : str,
                                  iblank     : int,
                                  text       : str) -> str:
        """ get the text from the string table

        Args:
            str_table:   string table
            text_id_tag: text ID tag
            text_tag:    text tag
            iblank:      index of the blank char
            text:        text

        Returns:
            text from the string table
        """

        if text.find(text_id_tag) == -1:
            return ""

        value_list_text_id = text.split(">")[1].split("<")[0].split("|")

        if not (res_text := [str_table.get_string(text_id, "") for text_id in value_list_text_id]):
            return ""

        if len(res_text) == 1:
            return text[:iblank] + "<" + text_tag + ">" + res_text[0] + "</" + text_tag + ">\n"

        return text[:iblank] + "<" + text_tag + ">" + "|".join(res_text) + "</" + text_tag + ">\n"

```

</details>