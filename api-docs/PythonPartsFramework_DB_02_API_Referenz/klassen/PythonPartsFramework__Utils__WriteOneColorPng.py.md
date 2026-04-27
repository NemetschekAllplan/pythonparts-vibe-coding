---
title: "WriteOneColorPng"
source: "PythonPartsFramework\Utils\WriteOneColorPng.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# WriteOneColorPng

> **Pfad:** `PythonPartsFramework\Utils\WriteOneColorPng.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

Create a one color png and write it to a file 

## Abhängigkeiten

- `zlib`

## Klassen

### `WriteOneColorPngFile`

Create a one color png and write it to a file 

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, height, width, color` | `None` | initialize  |
| `write` | `self, file` | `None` | write to the file  |
| `resetcrc` | `self` | `None` | reset the crc  |
| `writelong` | `self, l_value` | `None` | write a long value  |
| `writelongcrc` | `self, l_value` | `None` | write a long crc value  |
| `writewordcrc` | `self, s_value, reverse` | `None` | write word crc value  |
| `write_byte_crc` | `self, c_value` | `None` | write a byte crc  |
| `beginchunk` | `self, name, length` | `None` | begin chunk  |
| `endchunk` | `self` | `None` | end chunk  |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" Create a one color png and write it to a file """

from zlib import adler32, crc32

class WriteOneColorPngFile():
    """ Create a one color png and write it to a file """

    def __init__(self, height, width, color):
        """ initialize """

        self.height      = height
        self.width       = width
        self.bits        = 8
        self.group_bytes = int(self.width / (8 / self.bits) + 1)
        self.colors      = 1 #(1 << self.bits)
        self.crc         = 0
        self.plt         = color
        self.png_magic   = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
        self.file        = None

    def write(self, file):
        """ write to the file """

        self.file = file

        self.resetcrc()

        self.file.write(self.png_magic)

        self.beginchunk(b"IHDR", 0x0d)
        self.writelongcrc(self.width)	    # width
        self.writelongcrc(self.height)      # height
        self.write_byte_crc(self.bits)	    # bit depth
        self.write_byte_crc(3)	            # color type
        self.write_byte_crc(0)	            # compression
        self.write_byte_crc(0) 	            # filter
        self.write_byte_crc(0)	            # interlace
        self.endchunk()

        self.beginchunk(b"PLTE", self.colors * 3)

        for j in range(3):
            self.write_byte_crc((self.plt >> ((2 - j) * 8)) & 0xFF)

        self.endchunk()

        self.beginchunk(b"IDAT", (self.height * (self.group_bytes + 4 + 1)) + 4 + 2)

        self.writewordcrc(((0x0800 + 30) // 31) * 31, False)	# compression method

        zcrc = 1

        for i in range(self.height):
            if i == (self.height - 1):
                self.write_byte_crc(0x01)
            else:
                self.write_byte_crc(0)

            self.writewordcrc(self.group_bytes, True)
            self.writewordcrc(~self.group_bytes, True)

            zcrc = adler32(bytes([0]),zcrc)

            self.write_byte_crc(0)

            for _ in range(self.width):
                zcrc = adler32(bytes([0]),zcrc)
                self.write_byte_crc(0)

        self.writelongcrc(zcrc)

        self.endchunk()

        self.beginchunk(b"IEND", 0)
        self.endchunk()


    def resetcrc(self):
        """ reset the crc """

        self.crc = 0


    def writelong(self, l_value):
        """ write a long value """

        self.file.write(bytes([(l_value >> 24)&0xFF,(l_value >> 16)&0xFF,(l_value >> 8) & 0xFF, l_value & 0xFF]))


    def writelongcrc(self, l_value):
        """ write a long crc value """

        byte3 = bytes([(l_value >> 24) & 0xFF])
        byte2 = bytes([(l_value >> 16) & 0xFF])
        byte1 = bytes([(l_value >> 8) & 0xFF])
        byte0 = bytes([l_value & 0xFF])

        self.crc = crc32(byte3, self.crc)
        self.file.write(byte3)
        self.crc = crc32(byte2, self.crc)
        self.file.write(byte2)
        self.crc = crc32(byte1, self.crc)
        self.file.write(byte1)
        self.crc = crc32(byte0, self.crc)
        self.file.write(byte0)


    def writewordcrc(self, s_value, reverse):
        """ write word crc value """

        byte1 = bytes([(s_value >> 8) & 0xFF])
        byte0 = bytes([s_value & 0xFF])

        if reverse:
            byte1, byte0 = byte0, byte1

        self.crc = crc32(byte1, self.crc)
        self.file.write(byte1)
        self.crc = crc32(byte0, self.crc)
        self.file.write(byte0)


    def write_byte_crc(self, c_value):
        """ write a byte crc """

        c_value = bytes([c_value])

        self.crc = crc32(c_value, self.crc)
        self.file.write(c_value)


    def beginchunk(self, name, length):
        """ begin chunk """

        self.writelong(length)
        self.resetcrc()

        self.crc = crc32(name, self.crc)

        self.file.write(name)


    def endchunk(self):
        """ end chunk """

        self.writelong(self.crc)

```

</details>