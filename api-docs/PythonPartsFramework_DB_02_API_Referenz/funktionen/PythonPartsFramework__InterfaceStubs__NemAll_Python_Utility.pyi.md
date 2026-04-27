---
title: "NemAll_Python_Utility"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_Utility.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_Utility

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_Utility.pyi`  
> **Typ:** `stub`  
> **Tags:** `utility`

## Inhalt

```text
# pylint: disable=invalid-name
# pylint: disable=used-before-assignment
# pylint: disable=too-many-public-methods
# pylint: disable=c-extension-no-member
# pylint: disable=import-self
# pylint: disable=empty-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=line-too-long
# pylint: disable=unused-argument
# pylint: disable=redefined-builtin
# pylint: disable=anomalous-backslash-in-string
# pylint: disable=too-few-public-methods
# pylint: disable=function-redefined
# pylint: disable=eq-without-hash
# pylint: disable=too-many-lines
# pylint: disable=too-many-arguments

"""Exposed utility classes and functions"""

from __future__ import annotations

import typing

import collections.abc

import NemAll_Python_IFW_ElementAdapter


__all__ = [
    "CheckModuleLicence",
    "ClearUnitTestDocument",
    "DateDialog",
    "DefaultDirectories",
    "EncryptString",
    "FileDialog",
    "GUID",
    "GetPluginNameHash",
    "IDCANCEL",
    "IDNO",
    "IDOK",
    "IDYES",
    "ImportScript",
    "InitReinfNormInterpreter",
    "InitTkinter",
    "InitUnitTest",
    "IsExecutedByUnitTest",
    "KeyboardState",
    "LoadSymbolForUnitTest",
    "MB_DONOTASKAGAIN",
    "MB_OK",
    "MB_OKCANCEL",
    "MB_YESNO",
    "MB_YESNOCANCEL",
    "ProgressBar",
    "ShowMessageBox",
    "SizeTList",
    "SuppressLangDllErrorMessages",
    "Timer",
    "TraceDataBase",
    "UninitUnitTest",
    "VecByteList",
    "VecDoubleList",
    "VecGUIDList",
    "VecIntList",
    "VecSizeTList",
    "VecStringList",
    "VecUIntList",
    "VecULongList",
    "VecUShortList",
    "wstring"
]


class DateDialog():

    @staticmethod
    def GetDate(dateText: str, headerText: str) -> str:
        """Implementation of the file dialog expose

        Args:
            dateText:   default date
            headerText: header text
        """

class DefaultDirectories():
    """Default directories
    """
    def AddDirectory(self, path: str) -> bool:
        """Add a directory

        Args:
            path:    path of the directory

        Returns:
            directory added: true/false
        """
    def __init__(self):
        """Initialize
        """

class FileDialog():
    """File dialog
    """
    @staticmethod
    def AskOpenFavoriteFile(defaultPath: str, title: str, filters: str, extension: str) -> str:
        """Ask for a favorite file to open

        Args:
            defaultPath:    Initial default path
            title:          Title of the dialog. If the title is empty an internal string will be used
            filters:        Filters of the files
            extension:      Extension of the file

        Returns:
            selected file
        """
    @staticmethod
    def AskOpenFile(defaultPath: str, title: str, filters: str, extension: str, defaultDir: DefaultDirectories) -> str:
        """Ask for a file to open

        Args:
            defaultPath:    Initial default path
            title:          Title of the dialog. If the title is empty an internal string will be used
            filters:        Filters of the files
            extension:      Extension of the file
            defaultDir:     Default directories

        Returns:
            selected file
        """
    @staticmethod
    def AskSaveFavoriteFile(defaultPath: str, title: str, filters: str, extension: str) -> str:
        """Ask for a favorite file to save

        Args:
            defaultPath:    Initial default path
            title:          Title of the dialog. If the title is empty an internal string will be used
            filters:        Filters of the files
            extension:      Extension of the file

        Returns:
            selected file
        """
    @staticmethod
    def AskSaveFile(defaultPath: str, title: str, filters: str, extension: str, defaultDir: DefaultDirectories) -> str:
        """Ask for a file to save

        Args:
            defaultPath:    Initial default path
            title:          Title of the dialog. If the title is empty an internal string will be used
            filters:        Filters of the files
            extension:      Extension of the file
            defaultDir:     Default directories

        Returns:
            selected file
        """
    def __init__(self):
        """Initialize
        """

class GUID():

    @staticmethod
    def FromString(strGuid: str) -> GUID:
        """Create a GUID from a string

        Args:
            strGuid:GUID as string

        Returns:
            GUID from the string
        """
    def __eq__(self, compGuid: GUID) -> bool:
        """Compare a GUID

        Args:
            compGuid:GUID to compare

        Returns:
            GUIDs are equal: True/False
        """
    def __hash__(self) -> int:
        """Create a hash from the GUID

        Returns:
            hash from the GUID
        """
    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Create a string from the GUID

        Returns:
            string from the GUID
        """

class InitTkinter():

    def __init__(self):
        """Initialize the use of tkinter in Allplan
        """

class KeyboardState():
    """Get the keyboard state
    """
    @staticmethod
    def IsAltKeyPressed() -> bool:
        """Check for a pressed alt key

        Returns:
            alt key is pressed: True/False
        """
    @staticmethod
    def IsCtrlKeyPressed() -> bool:
        """Check for a pressed ctrl key

        Returns:
            ctrl key is pressed: True/False
        """
    @staticmethod
    def IsShiftKeyPressed() -> bool:
        """Check for a pressed shift key

        Returns:
            shift key is pressed: True/False
        """
    def __init__(self):
        """Initialize
        """

class ProgressBar():
    """Representation of the progress bar

    Examples:
        To show a progress bar, initialize it
        >>> progress_bar = ProgressBar(10,0,False)

        To increase the progress bar, call `Step()` method.

        **IMPORTANT**: The `Step()` must be called exactly as many times, as defined
        in the constructor!

    """
    def CloseProgressbar(self) -> bool:
        """Closed progressbar dialog

        Returns:
            true if progressbar closed correctly
        """
    @typing.overload
    def MakeStep(self, step: int) -> bool:
        """Make a step

        Args:
            step: step count

        Returns:
            true step is correctly executed
        """
    @typing.overload
    def MakeStep(self, step: int, additionalInfoStrID: int) -> bool:
        """Make a step

        Args:
            step:                step count
            additionalInfoStrID: additional info ID

        Returns:
            true step is correctly executed
        """
    @typing.overload
    def MakeStep(self, step: int, additionalInfo: str) -> bool:
        """Make a step

        Args:
            step:           step count
            additionalInfo: additional info

        Returns:
            true step is correctly executed
        """
    def MakeStep(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def ResetProgressBar(self, numberOfSteps: int, progressBarTitle: str, additionalInfo: str, closable: bool) -> bool:
        """Reset progressbar dialog

        Args:
            numberOfSteps:    number of steps/elements
            progressBarTitle: title of progressbar
            additionalInfo:   additional info
            closable:         progressbar can be canceled

        Returns:
            true if progressbar started correctly
        """
    @typing.overload
    def ResetProgressBar(self, numberOfSteps: int, progressBarTitleStrID: int, additionalInfoStrID: int, closable: bool) -> bool:
        """Reset progressbar dialog

        Args:
            numberOfSteps:         number of steps/elements
            progressBarTitleStrID: title of progressbar ID
            additionalInfoStrID:   additional info ID
            closable:              progressbar can be canceled

        Returns:
            true if progressbar started correctly
        """
    def ResetProgressBar(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def SetAditionalInfo(self, textId: int) -> bool:
        """Set the additional info

        Args:
            textId: additional info text ID

        Returns:
            true if set correctly
        """
    @typing.overload
    def SetAditionalInfo(self, text: str) -> bool:
        """Set the additional info

        Args:
            text: additional info text

        Returns:
            true if set correctly
        """
    def SetAditionalInfo(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    def SetInfinitProgressbar(self, isInfinit: bool) -> bool:
        """Set infinite progressbar dialog

        Args:
            isInfinit: infinite state

        Returns:
            true if set correctly
        """
    def SetIsClosable(self, isClosable: bool) -> bool:
        """Set the closeable state

        Args:
            isClosable: closable state

        Returns:
            true if set correctly
        """
    def SetNumberOfSteps(self, numberOfSteps: int) -> bool:
        """Set number of steps

        Args:
            numberOfSteps: number of steps/elements

        Returns:
            true if set correctly
        """
    @typing.overload
    def SetTitle(self, textId: int) -> bool:
        """Set the title

        Args:
            textId: title text ID

        Returns:
            true if set correctly
        """
    @typing.overload
    def SetTitle(self, text: str) -> bool:
        """Set the title

        Args:
            text: title text

        Returns:
            true if set correctly
        """
    def SetTitle(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def StartInfiniteProgressbar(self, progressBarTitle: str, additionalInfo: str, closable: bool, startImmediately: bool = False) -> bool:
        """Starts infinite progressbar dialog

        Args:
            progressBarTitle: title of progressbar
            additionalInfo:   additional info
            closable:         progressbar can be canceled
            startImmediately: start immediately

        Returns:
            true if progressbar started correctly
        """
    @typing.overload
    def StartInfiniteProgressbar(self, progressBarTitleID: int, additionalInfoStrID: int, closable: bool,
                                 startImmediately: bool = False) -> bool:
        """Starts infinite progressbar dialog

        Args:
            progressBarTitleID:  title of progressbar ID
            additionalInfoStrID: additional info ID
            closable:            progressbar can be canceled
            startImmediately:    start immediately

        Returns:
            true if progressbar started correctly
        """
    @typing.overload
    def StartInfiniteProgressbar(self, progressBarTitle: str, closable: bool, startImmediately: bool = False) -> bool:
        """Starts progressbar dialog

        Args:
            progressBarTitle: title of progressbar
            closable:         progressbar can be canceled
            startImmediately: start immediately

        Returns:
            true if progressbar started correctly
        """
    @typing.overload
    def StartInfiniteProgressbar(self, progressBarTitleID: int, closable: bool, startImmediately: bool = False) -> bool:
        """Starts progressbar dialog

        Args:
            progressBarTitleID: title of progressbar ID
            closable:           progressbar can be canceled
            startImmediately:   start immediately

        Returns:
            true if progressbar started correctly
        """
    def StartInfiniteProgressbar(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def StartProgressbar(self, numberOfSteps: int, progressBarTitle: str, additionalInfo: str, closable: bool,
                         startImmediately: bool = False) -> bool:
        """Starts progressbar dialog

        Args:
            numberOfSteps:    number of steps/elements
            progressBarTitle: title of progressbar
            additionalInfo:   additional info
            closable:         progressbar can be canceled
            startImmediately: start immediately

        Returns:
            true if progressbar started correctly
        """
    @typing.overload
    def StartProgressbar(self, numberOfSteps: int, progressBarTitleID: int, additionalInfoStrID: int, closable: bool,
                         startImmediately: bool = False) -> bool:
        """Starts progressbar dialog

        Args:
            numberOfSteps:       number of steps/elements
            progressBarTitleID:  title of progressbar ID
            additionalInfoStrID: additional info ID
            closable:            progressbar can be canceled
            startImmediately:    start immediately

        Returns:
            true if progressbar started correctly
        """
    @typing.overload
    def StartProgressbar(self, numberOfSteps: int, progressBarTitle: str, closable: bool, startImmediately: bool = False) -> bool:
        """Starts progressbar dialog

        Args:
            numberOfSteps:    number of steps/elements
            progressBarTitle: title of progressbar
            closable:         progressbar can be canceled
            startImmediately: start immediately

        Returns:
            true if progressbar started correctly
        """
    @typing.overload
    def StartProgressbar(self, numberOfSteps: int, progressBarTitleID: int, closable: bool, startImmediately: bool = False) -> bool:
        """Starts progressbar dialog

        Args:
            numberOfSteps:      number of steps/elements
            progressBarTitleID: title of progressbar ID
            closable:           progressbar can be canceled
            startImmediately:   start immediately

        Returns:
            true if progressbar started correctly
        """
    def StartProgressbar(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    @PythonPartPylintDecorator.deprecated(replace = " use MakeStep(...)")
    def Step(self) -> bool:
        """Increase the progress bar by one step

        Returns:
            _True_ when cancel button was clicked, _False_ otherwise
        """
    @typing.overload
    def __init__(self):
        """Shows the progress bar

        Args:
            countOfSteps:        Number of expected steps
            headerTextNumber:    Header text, 0 = standard
            bWithCancel:         _True_ if the cancel button should appear on the bar, _False_ otherwise
        """
    @typing.overload
    def __init__(self, countOfSteps: int, headerTextNumber: int, bWithCancel: bool):
        """Shows the progress bar

        Args:
            countOfSteps:        Number of expected steps
            headerTextNumber:    Header text, 0 = standard
            bWithCancel:         _True_ if the cancel button should appear on the bar, _False_ otherwise
        """
    @typing.overload
    def __init__(self, element: ProgressBar):
        """Shows the progress bar

        Args:
            countOfSteps:        Number of expected steps
            headerTextNumber:    Header text, 0 = standard
            bWithCancel:         _True_ if the cancel button should appear on the bar, _False_ otherwise
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class SizeTList():

    def __contains__(self, value: int) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: int):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: SizeTList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> int:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __init__(self):
        """Initialize
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """
    def __setitem__(self, index: int | slice, value: int):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: int):
        """Append a list item

        Args:
            value: Value to append
        """
    def count(self, value: int) -> int:
        """Get the values in the list

        Args:
            value: Value to count
        Returns:
            Value count
        """
    def extend(self, iterable: SizeTList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """
    def index(self, value: int) -> int:
        """Get the index for the value

        Args:
            value: Value to find

        Returns:
            Index for the value
        """
    def insert(self, index: int, item: int):
        """Insert an item in the list

        Args:
            index: Index of the item
            item:  Value to insert
        """
    @typing.overload
    def pop(self) -> int:
        """Pop the last value from the list

        Returns:
            Last value from the list
        """
    @typing.overload
    def pop(self, index: int) -> int:
        """Pop an item from the list

        Args:
            index: Index of the item

        Returns:
            Value of the item
        """
    def pop(self) -> int:
        """ Overloaded function. See individual overloads.
        """
    def remove(self, value: int):
        """Remove a value from the list

        Args:
            value: Value to remove
        """
    def reverse(self):
        """Reverse the list
        """
    @typing.overload
    def sort(self):
        """Sort the list
        """
    @typing.overload
    def sort(self, cmp: object):
        """EXPERIMENTAL!
        """
    def sort(self):
        """ Overloaded function. See individual overloads.
        """

class SuppressLangDllErrorMessages():

    def __init__(self):
        """Initialize
        """

class Timer():
    """Timer
    """
    def PrintTime(self, bReset: bool):
        """Print the time

        Args:
            bReset: Reset the timer
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, timer: Timer):
        """Copy constructor

        Args:
            timer: Timer to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class VecByteList():

    def __contains__(self, value: int) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: int):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: VecByteList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> int:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: int):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: int):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: VecByteList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecDoubleList():

    def __contains__(self, value: float) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: float):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: VecDoubleList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> float:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: float):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: float):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: VecDoubleList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecGUIDList():

    def __contains__(self, value: GUID) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: GUID):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: VecGUIDList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> GUID:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: GUID):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: GUID):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: VecGUIDList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecIntList():

    def __contains__(self, value: int) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: int):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: (list[int] |  VecIntList)) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> int:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: int):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: int):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: (list[int] |  VecIntList)):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecSizeTList():

    def __contains__(self, value: int) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: int):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: VecSizeTList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> int:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: int):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: int):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: VecSizeTList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecStringList():

    def __contains__(self, value: str) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: str):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: VecStringList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> str:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: str):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: str):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: VecStringList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecUIntList():

    def __contains__(self, value: int) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: int):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: (list[int] |  VecUIntList)) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> int:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: int):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: int):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: (list[int] |  VecUIntList)):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecULongList():

    def __contains__(self, value: int) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: int):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: VecULongList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> int:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: int):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: int):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: VecULongList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class VecUShortList():

    def __contains__(self, value: int) -> bool:
        """Check for a value in the list

        Args:
            value: Value to check

        Returns:
            State for value is in the list
        """
    def __delitem__(self, value: int):
        """Delete a list item

        Args:
            value: Value to delete
        """
    def __eq__(self, compare_list: VecUShortList) -> bool:
        """Compare two list

        Args:
            compare_list: List to compare

        Returns:
            Lists are equal state
        """
    def __getitem__(self, index: int) -> int:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, valueList: list):
        """Constructor with an initializer list

        Args:
            valueList: Value list
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Create a string from the values

        Returns:
            String
        """
    def __setitem__(self, index: int | slice, value: int):
        """Set a list item

        Args:
            index: Index of the item
            value: Value to item
        """
    def append(self, value: int):
        """Append a list item

        Args:
            value: Value to append
        """
    def extend(self, iterable: VecUShortList):
        """Add the items from an iterable to the end of the list

        Args:
            iterable: Iterable to add
        """

class wstring():

    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """

def CheckModuleLicence(moduleNumber: int) -> bool:
    """Check for a module licence

    Args:
        moduleNumber:Number of the module

    Returns:
        Licence for the module available: True/False
    """
def ClearUnitTestDocument():
    """Clear the document
    """
def EncryptString(stringtoEncrypt: str, pypName: str) -> str:
    """ImportScript an encrypted PythonPart script

    Args:
        stringtoEncrypt:    Path of the file
        pypName:            Name of the PythonPart
    """
def GetPluginNameHash() -> int:
    """
    """
def ImportScript(script: str, global_dict: object, pypName: str):
    """ImportScript an encrypted PythonPart script

    Args:
        script:      Path of the file
        global_dict: File name
        pypName:     Name of the PythonPart
    """
def InitReinfNormInterpreter():
    """
    """
def InitUnitTest(loadResources: bool) -> NemAll_Python_IFW_ElementAdapter.DocumentAdapter:
    """Initialize the unit test

    Args:
        loadResources: Load the resources
    """
def IsExecutedByUnitTest() -> bool:
    """Check, whether the script is executed by a unit test

    Returns:
        Script is executed by a unit test: True/False
    """
def LoadSymbolForUnitTest(file: str, clearDocument: bool,
                          updateArchEleGeometry: bool = False) -> NemAll_Python_IFW_ElementAdapter.BaseElementAdapterList:
    """Load a symbol to the Array

    Args:
        file:                 File name
        clearDocument:        Clear the document before symbol loading
        updateArchEleGeometry:Update the geometry elements after load (e.g. adapts slabs to the planes

    Returns:
        Created elements
    """
def ShowMessageBox(text: str, flags: int, dontAsk: int = 0) -> int:
    """Displays Message Box

    Args:
        text:   Message box text
        flags:  Button flags           dontAsk text number for the text that will be displayed when MB_DONOTASKAGAIN is used
    """
def TraceDataBase(arg2: int):
    """
    """
def UninitUnitTest():
    """Uninitialize the unit test
    """
IDCANCEL = 2
IDNO = 7
IDOK = 1
IDYES = 6
MB_DONOTASKAGAIN = 16777216
MB_OK = 0
MB_OKCANCEL = 1
MB_YESNO = 4
MB_YESNOCANCEL = 3

```