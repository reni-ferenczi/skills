# ShapefileXmlReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1375 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ShapefileXmlReader.h` | C++ | 81 |
| `src/file-io/ShapefileXmlReader.cc` | C++ | 100 |

## Overview

Parses GPlatesShapefileMap XML files that define property mappings for shapefile imports. The reader extends Qt's `QXmlStreamReader` and extracts key-value pairs from the root `<GPlatesShapefileMap version="1">` element, populating a `QMap<QString, QString>` provided by the caller. The map entries describe which shapefile attributes map to which GPlates feature properties, allowing `OgrReader` to correctly import shapefile feature collections without hardcoding attribute names.

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

Copy construction and assignment are private, preventing implicit copies. The caller owns the `QMap` pointer; the reader does not allocate or delete it. The XML version must be exactly "1" or a parse error is raised. Each XML element at the document root becomes a map entry with the element name as key and its text content as value; complex structures or nested elements are not supported.

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
