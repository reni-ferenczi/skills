# PropertyMapper

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1034 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PropertyMapper.h` | C++ | 125 |

## Overview

[[[PROSE overview unit=file-io/PropertyMapper tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`model_to_attribute_map_type`](#model_to_attribute_map_type) | typedef | — | — | 0 | — |
| [`ShapefileAttributes::ModelProperties`](#shapefileattributesmodelproperties) | enum | — | — | 0 | — |
| [`GPlatesFileIO::PropertyMapper`](#gplatesfileiopropertymapper) | class | — | — | 1 | An abstract base class for mapping file-io attributes to model properties. |

## Members

### `model_to_attribute_map_type`

*None.*

### `ShapefileAttributes::ModelProperties`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PLATEID` | enumerator | `None` | — | — |
| `FEATURE_TYPE` | enumerator | `None` | — | — |
| `BEGIN` | enumerator | `None` | — | — |
| `END` | enumerator | `None` | — | — |
| `NAME` | enumerator | `None` | — | — |
| `DESCRIPTION` | enumerator | `None` | — | — |
| `FEATURE_ID` | enumerator | `None` | — | — |
| `CONJUGATE_PLATE_ID` | enumerator | `None` | — | — |
| `RECONSTRUCTION_METHOD` | enumerator | `None` | — | — |
| `LEFT_PLATE` | enumerator | `None` | — | — |
| `RIGHT_PLATE` | enumerator | `None` | — | — |
| `SPREADING_ASYMMETRY` | enumerator | `None` | — | — |
| `GEOMETRY_IMPORT_TIME` | enumerator | `None` | — | — |
| `NUM_PROPERTIES` | enumerator | `None` | — | — |

### `GPlatesFileIO::PropertyMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PropertyMapper()` | constructor | `None` | public | — |
| `~PropertyMapper()` | destructor | `None` | public | — |
| `map_properties( QString &filename, QStringList &field_names, model_to_attribute_map_type &model_to_attribute_map, bool remapping )` | method | `bool` | public | — |
| `PropertyMapper( const PropertyMapper &other)` | constructor | `None` | private | Make copy and assignment private. |
| `operator=` | field | `PropertyMapper` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_PROPERTYMAPPER_H` | macro | `None` | — |
| `model_properties` | variable | `QString` | — |
| `default_attribute_field_names` | variable | `QString` | — |

## Notes

[[[PROSE notes unit=file-io/PropertyMapper tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 151 |
| [qt-widgets/ShapefileAttributeWidget](../qt-widgets/ShapefileAttributeWidget.md) | qt-widgets | 116 |
| [file-io/OgrReader](OgrReader.md) | file-io | 66 |
| [file-io/OgrUtils](OgrUtils.md) | file-io | 8 |
| [file-io/ShapefileXmlReader](ShapefileXmlReader.md) | file-io | 5 |
| [qt-widgets/ShapefilePropertyMapper](../qt-widgets/ShapefilePropertyMapper.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PropertyMapper.h
python scripts/gpq.py def GPlatesFileIO::PropertyMapper --body
python scripts/gpq.py uses PropertyMapper --kind class
python scripts/gpq.py hier PropertyMapper
```
