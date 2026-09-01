# PropertyMapper

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1034 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PropertyMapper.h` | C++ | 125 |

## Overview

`PropertyMapper` is the abstract interface `OgrReader` calls when a shapefile
needs its attribute fields matched to GPlates model properties and no saved
mapping (the `.gplates.xml` sidecar) is available; the one non-abstract
implementation, `qt-widgets/ShapefilePropertyMapper`, does this by popping up a
dialog and letting the user choose. Keeping the interface in `file-io` and the Qt
implementation in `qt-widgets` lets `OgrReader`/`OgrUtils` call `map_properties`
without depending on the GUI.

`ShapefileAttributes::ModelProperties` and its two parallel string tables
(`model_properties`, `default_attribute_field_names`) enumerate the fixed set of
standard feature properties (plate ID, feature type, begin/end time, name,
description, feature ID, conjugate/left/right plate, reconstruction method,
spreading asymmetry, geometry import time) that shapefile attribute fields can be
mapped onto, together with the conventional attribute field name GPlates expects
for each one by default (e.g. `PLATEID1` for `ReconstructionPlateId`).

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

- `model_properties` and `default_attribute_field_names` are positional arrays
  indexed by `ShapefileAttributes::ModelProperties`; adding, removing or
  reordering an enumerator without updating both arrays in lockstep desynchronizes
  the mapping.
- `map_properties` returns `false` to signal that mapping was cancelled (e.g. the
  user dismissed the dialog); callers such as `OgrReader::read_file` treat that as
  aborting the whole file load.

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
