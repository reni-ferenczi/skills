# GsmlFeaturesDef

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1413 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlFeaturesDef.h` | C++ | 133 |

## Overview

[[[PROSE overview unit=file-io/GsmlFeaturesDef tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/GsmlFeaturesDef tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
