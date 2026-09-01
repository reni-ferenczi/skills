# ShapefileXmlReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1375 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ShapefileXmlReader.h` | C++ | 81 |
| `src/file-io/ShapefileXmlReader.cc` | C++ | 100 |

## Overview

[[[PROSE overview unit=file-io/ShapefileXmlReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ShapefileXmlReader`](#gplatesfileioshapefilexmlreader) | class | `QXmlStreamReader` | — | 0 | — |

## Members

### `GPlatesFileIO::ShapefileXmlReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShapefileXmlReader()` | constructor | `None` | public | — |
| `read_file( QString &filename, QMap<QString,QString> *map)` | method | `bool` | public | Fills the map with data extracted from the xml file. |
| `ShapefileXmlReader( const ShapefileXmlReader &other)` | constructor | `None` | private | Copy-constructor is private. |
| `operator=` | field | `ShapefileXmlReader` | private | Assignment operator is private. |
| `read_xml()` | method | `void` | private | Read the xml data. |
| `read_map_item()` | method | `void` | private | Read an individual \<QString,QString\> pair and add it to d\_map. |
| `d_map` | field | `QMap<QString,QString>` | private | A pointer to the map to be filled. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_SHAPEFILEXMLREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ShapefileXmlReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrReader](OgrReader.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ShapefileXmlReader.h
python scripts/gpq.py def GPlatesFileIO::ShapefileXmlReader --body
python scripts/gpq.py uses ShapefileXmlReader --kind class
python scripts/gpq.py hier ShapefileXmlReader
```
