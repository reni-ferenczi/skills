# GsmlFeaturesDef

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1413 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlFeaturesDef.h` | C++ | 133 |

## Overview

Metadata definition of supported GeoSciML feature types and their property schemas. The `FeatureInfo` struct pairs a feature type name with an array of `PropertyInfo` pointers describing which properties that type can contain. Five static arrays define property lists for `MappedFeature`, `GeologicUnit`, `UnclassifiedFeature`, `RockUnit*` (prefix-based), and `FossilCollection*` (prefix-based) types, collected in the `AllFeatureTypes` array.

During GSML feature extraction, `GsmlNodeProcessorFactory` consults `AllFeatureTypes` to determine which properties to extract and process for each feature type. The struct provides the extensibility hook: adding a new feature type requires defining its property array, adding an entry to `AllFeatureTypes`, and ensuring the property definitions exist in `GsmlPropertyDef.h`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FeatureInfo`](#gplatesfileiofeatureinfo) | struct | — | — | 0 | Add new feature type: 1. |

## Members

### `GPlatesFileIO::FeatureInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `name` | field | `char` | public | — |
| `properties` | field | `PropertyInfo` | public | — |
| `property_num` | field | `unsigned` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GSMLFEATURESDEF_H` | macro | `None` | — |
| `MappedFeatureProperties` | variable | `PropertyInfo` | define the properties that are contained in feature. |
| `GeologicUnitProperties` | variable | `PropertyInfo` | — |
| `UnclassifiedFeatureProperties` | variable | `PropertyInfo` | — |
| `RockUnitFeatureProperties` | variable | `PropertyInfo` | — |
| `FossilCollectionFeatureProperties` | variable | `PropertyInfo` | — |
| `AllFeatureTypes` | variable | `FeatureInfo` | define all features. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GsmlNodeProcessorFactory](GsmlNodeProcessorFactory.md) | file-io | 13 |
| [file-io/OgrReader](OgrReader.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GsmlFeaturesDef.h
python scripts/gpq.py def GPlatesFileIO::FeatureInfo --body
python scripts/gpq.py uses FeatureInfo --kind struct
python scripts/gpq.py hier FeatureInfo
```
