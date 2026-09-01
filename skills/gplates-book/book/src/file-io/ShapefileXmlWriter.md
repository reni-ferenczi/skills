# ShapefileXmlWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 381 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ShapefileXmlWriter.h` | C++ | 73 |
| `src/file-io/ShapefileXmlWriter.cc` | C++ | 127 |

## Overview

Serializes a `QMap<QString, QString>` property mapping to a GPlatesShapefileMap XML file. The writer extends Qt's `QXmlStreamWriter` and emits the map as a root `<GPlatesShapefileMap version="1">` element with one child element per key-value pair. The output includes a detailed comment header documenting supported tags—such as `ReconstructionPlateId`, `FeatureType`, `Begin`, `End`—and their meanings, making the file human-readable and self-documenting for shapefile-import configurations.

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

Copy construction and assignment are private. Auto-formatting is enabled on construction, making the output indented and human-readable. The comment header includes the GPlates version string from the build time, a documented list of supported property tags, and usage instructions. The XML version is hardcoded to "1" and the file is opened with `Text` mode for cross-platform line-ending handling.

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
