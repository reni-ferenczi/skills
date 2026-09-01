# ShapefileXmlWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 381 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ShapefileXmlWriter.h` | C++ | 73 |
| `src/file-io/ShapefileXmlWriter.cc` | C++ | 127 |

## Overview

[[[PROSE overview unit=file-io/ShapefileXmlWriter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ShapefileXmlWriter`](#gplatesfileioshapefilexmlwriter) | class | `QXmlStreamWriter` | — | 0 | — |

## Members

### `GPlatesFileIO::ShapefileXmlWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShapefileXmlWriter()` | constructor | `None` | public | — |
| `write_file( const QString &filename, const QMap<QString,QString> &map)` | method | `bool` | public | Writes the data contained in \<map\> as an xml file. |
| `ShapefileXmlWriter( const ShapefileXmlWriter &other)` | constructor | `None` | private | Copy-constructor is made private |
| `operator=` | field | `ShapefileXmlWriter` | private | Assignment is made private. |
| `write_map_item( QString key, QString value)` | method | `void` | private | Writes a map item to the xml file. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_SHAPEFILEXMLWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ShapefileXmlWriter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrUtils](OgrUtils.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ShapefileXmlWriter.h
python scripts/gpq.py def GPlatesFileIO::ShapefileXmlWriter --body
python scripts/gpq.py uses ShapefileXmlWriter --kind class
python scripts/gpq.py hier ShapefileXmlWriter
```
