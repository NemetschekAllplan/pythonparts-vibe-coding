---
title: "TabularDataUtil"
source: "PythonPartsFramework\Utils\TabularDataUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TabularDataUtil

> **Pfad:** `PythonPartsFramework\Utils\TabularDataUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

Script for reading and accessing tabular data

## Abhängigkeiten

- `__future__`
- `collections`
- `csv`
- `itertools`
- `openpyxl`
- `openpyxl.worksheet.worksheet`
- `operator`
- `typing`
- `xml.etree.ElementTree`

## Klassen

### `DataFrame`

Two-dimensional tabular data structure with labeled axes (rows and columns)
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, data: Optional[Dict[Union[int, str], List[str]]]=None, columns: Optional[Union[List[int], List[str]]]=None, index: Optional[List[int]]=None` | `None` | Initialization of class DataFrame  Args:     data:    tabular data which is a dictionary of lists     columns: column labels     index:   row index |
| `__getitem__` | `self, key: Union[int, str, slice, Series]` | `Union[DataFrame, Series]` | Get items  Args:     key: it can be  Returns:     item for the index |
| `loc` | `self, location: int` | `Series` | Get a row from data frame  Args:     location: int value of row index, natural row index  Returns:     Series |
| `get_row` | `self, key: str, value: str` | `Optional[Series]` | Get a row from data frame by a condition: column_label == value  Args:     key:   column label     value: new value  Returns:     row value |
| `short_repr` | `self` | `str` | Represent the DataFrame by its row size x column size  Returns:     short data string frame |
| `__repr__` | `self` | `str` | create a string from the data frame  Returns:     data frame string |
| `__len__` | `self` | `int` | get the length of the data frame  Returns:     length of the data frame |
| `__iter__` | `self` | `Iterator` | get the data frame iterator  Yields:     data frame iterator |

### `Series`

One-dimensional array with axis labels
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, data: Optional[Union[List[int], List[str]]]=None, axis: Optional[Union[List[int], List[str]]]=None, name: Union[int, str]=0` | `None` | Initialization of class Series  Args:     data: a list of row or column data     axis: data labels, can be a list of int or str     name: name of the modified property |
| `__getitem__` | `self, key: Union[int, str, slice]` | `Optional[Union[int, str, Series]]` | Get items  Args:     key: it can be a column name or a range of row index  Returns:     item for the index |
| `__eq__` | `self, other: Any` | `Series` | comparison of the series values with an other value  Args:     other: value to compare  Returns:     series with the comparison state |
| `__ne__` | `self, other: Any` | `Series` | unequal comparison of the series values with an other value  Args:     other: value to compare  Returns:     series with the comparison state |
| `__ge__` | `self, other: Any` | `Series` | greater equal comparison of the series values with an other value  Args:     other: value to compare  Returns:     series with the comparison state |
| `__gt__` | `self, other: Any` | `Series` | greater comparison of the series values with an other value  Args:     other: value to compare  Returns:     series with the comparison state |
| `__le__` | `self, other: Any` | `Series` | less equal comparison of the series values with an other value  Args:     other: value to compare  Returns:     series with the comparison state |
| `__lt__` | `self, other: Any` | `Series` | less comparison of the series values with an other value  Args:     other: value to compare  Returns:     series with the comparison state |
| `__operation` | `self, operator_fct: Callable, other: Series` | `Series` | execute a comparison operation of the series values with an other value  Args:     operator_fct: operator function     other:        value to compare  Returns:     series |
| `__repr__` | `self` | `str` | create a string from a series  Returns:     series data a string |

## Funktionen

### `read_csv(csv_path: str)`

read the data from the csv file

Args:
    csv_path: path of the csv file

Returns:
    data frame

**Parameter:**
- `csv_path: str`

**Rückgabe:** `DataFrame`

**Beispiel:**
```python
result = read_csv(...)
```

### `read_xml(xml_path: str, *args)`

Read partial data from xml file and return a DataFrame. Xml file should be those which can be converted into tabular data.

Args:
    xml_path: xml file path
    *args:    string, the ElementTree tags, which serve later as column labels of data frame

Returns:
    data frame

**Parameter:**
- `xml_path: str`
- `*args`

**Rückgabe:** `Optional[DataFrame]`

**Beispiel:**
```python
result = read_xml(..., ...)
```

### `read_xlsx(xlsx_path: str, sheet: Union[int, str]=0)`

read an Excel file

Args:
    xlsx_path: excel path
    sheet:     sheet index

Returns:
    data frame

**Parameter:**
- `xlsx_path: str`
- `sheet: Union[int`
- `str]=0`

**Rückgabe:** `DataFrame`

**Beispiel:**
```python
result = read_xlsx(..., ..., ...)
```

### `read_matrix(lists: List[List[Any]])`

read a matrix

Args:
    lists: lists

Returns:
    matrix

**Parameter:**
- `lists: List[List[Any]]`

**Rückgabe:** `DataFrame`

**Beispiel:**
```python
result = read_matrix(...)
```

### `has_duplicates(data_frame: DataFrame, duplicates: List[Union[int, str]])`

check if data frame has duplicated column headers and return them if it has

Args:
    data_frame:  data frame
    duplicates: duplicates

Returns:
    duplicated state

**Parameter:**
- `data_frame: DataFrame`
- `duplicates: List[Union[int`
- `str]]`

**Rückgabe:** `bool`

**Beispiel:**
```python
result = has_duplicates(..., ..., ...)
```

### `concat(data_frames: List[DataFrame], _ignore_index: bool=False, _keys: Any=None)`

concatenate

Args:
    data_frames:   data frames
    _ignore_index: ignored index state
    _keys:         keys

Returns:
    concatenated data frame

**Parameter:**
- `data_frames: List[DataFrame]`
- `_ignore_index: bool=False`
- `_keys: Any=None`

**Rückgabe:** `Optional[DataFrame]`

**Beispiel:**
```python
result = concat(..., ..., ...)
```

### `eval_noex(value: Any, default: Any=None, value_type: Any=None)`

Evaluate value from Table without throwing exceptions, only used to evaluate value that is string or None

Args:
    value:      new value
    default:    has a higher priority than value_type, when both default and value_type are given
    value_type: string that indicates the value type

Returns:
    eval result

**Parameter:**
- `value: Any`
- `default: Any=None`
- `value_type: Any=None`

**Rückgabe:** `Any`

**Beispiel:**
```python
result = eval_noex(..., ..., ...)
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Script for reading and accessing tabular data
"""

# pylint: disable=bare-except

from __future__ import annotations

from typing import List, Any, Set, Optional, Union, Dict, Iterator, Callable

from itertools import compress

import csv
import xml.etree.ElementTree as ET
import operator
import collections
import openpyxl
import openpyxl.worksheet.worksheet

def read_csv(csv_path: str) -> DataFrame:
    """ read the data from the csv file

    Args:
        csv_path: path of the csv file

    Returns:
        data frame
    """

    def read_dataframe(csv_path: str,
                       encode : str) -> DataFrame:
        """ read the data frame

        Args:
            csv_path: path of the csv file
            encode:  encoding

        Returns:
            data frame
        """

        with open(csv_path, 'r', encoding = encode) as csvfile:
            data  = ""
            index = 0

            for line in csvfile.readlines():    # include a data line if possible: double quote, ...
                data += line
                index += 1

                if index == 2:
                    break

            dialect = csv.Sniffer().sniff(data)

            csvfile.seek(0)

            reader   = list(csv.reader(csvfile, dialect))
            columns  = reader[0]
            index    = list(range(len(reader)-1))
            col_dict = {}

            for j, key in enumerate(columns):
                col_dict[key] = [i[j] for i in reader[1:]]

            return DataFrame(data = col_dict, columns = columns, index = index)

    try:
        return read_dataframe(csv_path, "utf-8-sig")

    except:
        return read_dataframe(csv_path, "ansi")


def read_xml(xml_path: str,
             *args: list[Any]) -> Optional[DataFrame]:
    """ Read partial data from xml file and return a DataFrame. Xml file should be those which can be converted into tabular data.

    Args:
        xml_path: xml file path
        *args:    string, the ElementTree tags, which serve later as column labels of data frame

    Returns:
        data frame
    """

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

    except:
        print("cannot find " + xml_path)
        return None

    col_dict = {}

    args = [str(arg) for arg in args]

    for key in args:
        col_dict[key] = []

    for ele in root.findall(".//" + args[0] + "/.."):
        for key in args:
            if (val := ele.find(key)) is not None:
                col_dict[key].append(val.text)
            else:
                col_dict[key].append(None)

    return DataFrame(data = col_dict, columns = args, index = list(range(len(col_dict[args[0]]))))


def read_xlsx(xlsx_path: str,
              sheet    : Union[int, str] = 0) -> DataFrame:
    """ read an Excel file

    Args:
        xlsx_path: excel path
        sheet:     sheet index

    Returns:
        data frame
    """

    workbook = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True, keep_links=False)

    if isinstance(sheet, int):
        workbook_sheet = workbook.get_sheet_by_name(workbook.sheetnames[sheet])

    elif isinstance(sheet, str) and sheet in workbook.sheetnames:
        workbook_sheet = workbook.get_sheet_by_name(sheet)

    else:
        workbook_sheet = workbook.get_sheet_by_name(workbook.sheetnames[0])


    #--------------------- get the cell values

    data       : List[List[Any]] = []
    empty_rows : Set[int]        = set()

    for index, row in enumerate(workbook_sheet.rows):        # type: ignore
        if not next((cell.value is not None for cell in row), False):
            empty_rows.add(index)

        data.append([str(cell.value) if cell.value is not None else "" for cell in row])

    index = len(data) - 1

    while index >= 0:
        if not index in empty_rows:
            break

        data.pop()

        index -= 1


    #--------------------- remove empty rows at the end

    workbook.close()

    if not data:
        return DataFrame()

    columns  = data[0]
    index    = list(range(len(data) - 1))
    col_dict = {}

    for j, key in enumerate(columns):
        col_dict[key] = [i[j] for i in data[1:]]

    return DataFrame(data = col_dict, columns = columns, index = index)


def read_matrix(lists: List[List[Any]]) -> DataFrame:
    """ read a matrix

    Args:
        lists: lists

    Returns:
        matrix
    """

    if not isinstance(lists, list):
        return DataFrame()

    if not isinstance(lists[0], list):
        return DataFrame()

    list_len = len(lists[0])

    for list_ in lists:
        if not isinstance(list_, list):
            return DataFrame()

        if len(list_) != list_len:
            return DataFrame()

    index   = list(range(len(lists)))
    columns = list(range(len(lists[0])))

    col_dict = {}

    for j, _ in enumerate(lists[0]):
        col_dict[j] = [i[j] for i in lists]

    return DataFrame(data = col_dict, columns = columns, index = index)


def has_duplicates(data_frame : DataFrame,
                   duplicates: List[Union[int,str]]) -> bool:
    """ check if data frame has duplicated column headers and return them if it has

    Args:
        data_frame:  data frame
        duplicates: duplicates

    Returns:
        duplicated state
    """

    columns = data_frame.columns

    if len(set(columns)) == len(columns):
        return False

    duplicates.extend([item for item, count in collections.Counter(columns).items() if count > 1])

    return True


class DataFrame(dict):
    """ Two-dimensional tabular data structure with labeled axes (rows and columns)
    """

    def __init__(self,
                 data   : Optional[Dict[Union[int, str], List[str]]]  = None,
                 columns: Optional[Union[List[int], List[str]]]       = None,
                 index  : Optional[List[int]]                         = None):
        """ Initialization of class DataFrame

        Args:
            data:    tabular data which is a dictionary of lists
            columns: column labels
            index:   row index
        """

        self.data    = data    if data    is not None else {}
        self.columns = columns if columns is not None else []
        self.index   = index   if index   is not None else []

        super().__init__(self.data)


    def __getitem__(self,
                    key: Union[int, str, slice, Series]) -> Union[DataFrame, Series]:
        """ Get items

        Args:
            key: it can be

        Returns:
            item for the index
        """

        #----------------- get the item by a slice key

        if isinstance(key, slice):
            selected_df = {}

            for col_key in self.columns:
                selected_df[col_key] = self.data[col_key].__getitem__(key)

            return DataFrame(data = selected_df, columns = self.columns, index = list(range(len(selected_df[self.columns[0]]))))


        #----------------- get the item by a Series key

        if isinstance(key, Series):
            if self.index == key.axis:
                selected_df = {}

                for col_key in self.columns:
                    selected_df[col_key] = list(compress(self.data[col_key], key.data))

                return DataFrame(data = selected_df, columns = self.columns, index = list(range(len(selected_df[self.columns[0]]))))

            return DataFrame()


        #----------------- get the item by a string or int

        column = self.data[key]

        return Series(data = column, axis = self.index, name = key)


    def loc(self,
            location: int) -> Series:
        """ Get a row from data frame

        Args:
            location: int value of row index, natural row index

        Returns:
            Series
        """

        series_data = [self.data[col_key][location] for col_key in self.columns]

        return Series(data = series_data, axis = self.columns, name = location)


    def get_row(self,
                key  : str,
                value: str) -> Optional[Series]:
        """ Get a row from data frame by a condition: column_label == value

        Args:
            key:   column label
            value: new value

        Returns:
            row value
        """

        row_num = 0

        try:
            row_num = self.data[key].index(value)

        except:
            return None

        return self.loc(row_num)


    def short_repr(self) -> str:
        """ Represent the DataFrame by its row size x column size

        Returns:
            short data string frame
        """
        return f"DataFrame({len(self.index)}x{len(self.columns)})"


    def __repr__(self) -> str:
        """ create a string from the data frame

        Returns:
            data frame string
        """

        text = " " * 10

        max_widths = []


        #----------------- header string

        for col in self.columns:
            max_col_width = max(max(len(str(self.data[col][i])) for i in self.index), len(str(col)))

            max_widths.append(max_col_width)

            text += str(col) + " " * (max_col_width - len(str(col)) + 3)

        text += "\n"


        #----------------- add the row strings

        for i, row in enumerate(self.index):
            row_text = " "* (7 - len(str(row))) + str(row) + " " * 3

            for j, col in enumerate(self.columns):
                row_text += str(self.data[col][i]) + " " * (max_widths[j] + - len(str(self.data[col][i])) + 3)

            row_text += "\n"
            text     += row_text

        return text


    def __len__(self) -> int:
        """ get the length of the data frame

        Returns:
            length of the data frame
        """
        return len(self.index)


    def __iter__(self) -> Iterator:
        """ get the data frame iterator

        Yields:
            data frame iterator
        """

        for i in range(len(self.index)):
            yield self.loc(i)


class Series(list):
    """ One-dimensional array with axis labels
    """

    def __init__(self,
                 data: Optional[Union[List[int], List[str]]] = None,
                 axis: Optional[Union[List[int], List[str]]] = None,
                 name: Union[int, str]                       = 0):
        """ Initialization of class Series

        Args:
            data: a list of row or column data
            axis: data labels, can be a list of int or str
            name: name of the modified property
        """

        self.data = data if data is not None else []
        self.axis = axis if axis is not None else []
        self.name = name

        super().__init__(self.data)


    def __getitem__(self,
                    key: Union[int, str, slice]) -> Optional[Union[int, str, Series]]:
        """ Get items

        Args:
            key: it can be a column name or a range of row index

        Returns:
            item for the index
        """

        #----------------- create a new Series from a slice key

        if isinstance(key, slice) and isinstance(self.axis[0], int):
            return Series(data = self.data.__getitem__(key),
                          axis = self.axis.__getitem__(key),
                          name = self.name)


        #----------------- return a value by a string key

        if isinstance(key, str) and isinstance(self.axis[0], str):
            if key in self.axis:
                return self.data[self.axis.index(key)] # type: ignore

            print("Wrong key!")

            return None


        #----------------- return a value by an integer key

        if isinstance(key, int):
            return self.data[key]

        print("Wrong key!")

        return None


    def __eq__(self,
               other: Any) -> Series:
        """ comparison of the series values with an other value

        Args:
            other: value to compare

        Returns:
            series with the comparison state
        """
        return self.__operation(operator.eq, other)

    def __ne__(self,
               other: Any) -> Series:
        """ unequal comparison of the series values with an other value

        Args:
            other: value to compare

        Returns:
            series with the comparison state
        """
        return self.__operation(operator.ne, other)

    def __ge__(self,
               other: Any) -> Series:
        """ greater equal comparison of the series values with an other value

        Args:
            other: value to compare

        Returns:
            series with the comparison state
        """
        return self.__operation(operator.ge, other)

    def __gt__(self,
               other: Any) -> Series:
        """ greater comparison of the series values with an other value

        Args:
            other: value to compare

        Returns:
            series with the comparison state
        """
        return self.__operation(operator.gt, other)

    def __le__(self,
               other: Any) -> Series:
        """ less equal comparison of the series values with an other value

        Args:
            other: value to compare

        Returns:
            series with the comparison state
        """
        return self.__operation(operator.le, other)

    def __lt__(self,
               other: Any) -> Series:
        """ less comparison of the series values with an other value

        Args:
            other: value to compare

        Returns:
            series with the comparison state
        """
        return self.__operation(operator.lt, other)

    def __operation(self,
                    operator_fct: Callable,
                    other       : Series) -> Series:
        """ execute a comparison operation of the series values with an other value

        Args:
            operator_fct: operator function
            other:        value to compare

        Returns:
            series
        """

        result = []

        for val in self.data:
            if operator_fct(val, other):
                result.append(True)
            else:
                result.append(False)

        return Series(data = result, axis = self.axis, name = "bool:" + str(self.name))


    def __repr__(self) -> str:
        """ create a string from a series

        Returns:
            series data a string
        """

        max_width = max(len(str(x)) for x in self.axis) + max(len(str(x)) for x in self.data) + 3

        label_text =""

        for i, label in enumerate(self.axis):
            label_text += str(label) + " " * (max_width - len(str(label)) - len(str(self.data[i]))) + str(self.data[i]) + "\n"

        label_text += "Name: " + str(self.name)

        return label_text


def concat(data_frames  : List[DataFrame],
           _ignore_index: bool = False,
           _keys        : Any  = None) -> Optional[DataFrame]:
    """ concatenate

    Args:
        data_frames:   data frames
        _ignore_index: ignored index state
        _keys:         keys

    Returns:
        concatenated data frame
    """

    columns      = []
    total_length = 0

    for data_frame in data_frames:
        if not data_frame:
            data_frames.remove(data_frame)
            continue

        columns      += data_frame.columns
        total_length += len(data_frame)

    columns = list(set(columns))

    if total_length == 0:
        return None

    data = {}

    for col in columns:
        data[col] = []

    for data_frame in data_frames:
        for col in columns:
            if col in data_frame.data:
                data[col].extend(data_frame.data[col])
            else:
                data[col].extend([None for i in range(len(data_frame.index))])

    data_frame = DataFrame(data = data, columns = columns, index = list(range(total_length)))

    return data_frame


def eval_noex(value     : Any,
              default   : Any = None,
              value_type: Any = None) -> Any:
    """ Evaluate value from Table without throwing exceptions, only used to evaluate value that is string or None

    Args:
        value:      new value
        default:    has a higher priority than value_type, when both default and value_type are given
        value_type: string that indicates the value type

    Returns:
        eval result
    """

    if value is None or value == "":
        print("Not a valid value!")

        if not value_type and default is None:
            return ""

        if default is not None:
            return default

        return eval(value_type + "()")

    return eval(value)

```

</details>