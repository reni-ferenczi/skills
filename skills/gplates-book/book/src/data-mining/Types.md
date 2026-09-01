# Types

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 232 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/Types.h` | C++ | 199 |

## Overview

`Types.h` defines the two enumerations that describe a co-registration query in the data-mining layer. `AttributeType` selects where a per-feature attribute value comes from — a GPML property, a shapefile attribute, a raster sample, or one of the built-in distance/presence pseudo-attributes. `ReducerType` selects how the values sampled from features within a region of interest are collapsed into a single result — minimum, maximum, mean, median, percentile, a weighted mean, a nearest-distance or vote-style lookup, or a simple presence/count test.

Both enums are declared inline in the header along with a `to_string()` helper used for display and logging, and a `transcribe()` overload that lets `GPlatesScribe::Scribe` read and write the enum value in the session/project file format. These two types are the shared vocabulary that `DataSelector`, `CoRegFilterMapReduceFactory`, `CoRegConfigurationTable` and the `CoRegistrationLayerConfigurationDialog` UI pass around when building and running a co-registration filter/map/reduce pipeline.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::AttributeType`](#gplatesdataminingattributetype) | enum | — | — | 0 | — |
| [`GPlatesDataMining::ReducerType`](#gplatesdataminingreducertype) | enum | — | — | 0 | — |

## Members

### `GPlatesDataMining::AttributeType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CO_REGISTRATION_GPML_ATTRIBUTE` | enumerator | `None` | — | — |
| `CO_REGISTRATION_SHAPEFILE_ATTRIBUTE` | enumerator | `None` | — | — |
| `CO_REGISTRATION_RASTER_ATTRIBUTE` | enumerator | `None` | — | — |
| `DISTANCE_ATTRIBUTE` | enumerator | `None` | — | — |
| `PRESENCE_ATTRIBUTE` | enumerator | `None` | — | — |
| `NUMBER_OF_PRESENCE_ATTRIBUTE` | enumerator | `None` | — | — |
| `NUM_OF_Attribute_Type` | enumerator | `None` | — | NOTE: Any new values should also be added to transcribe. |

### `GPlatesDataMining::ReducerType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `REDUCER_MIN` | enumerator | `None` | — | — |
| `REDUCER_MAX` | enumerator | `None` | — | — |
| `REDUCER_MEAN` | enumerator | `None` | — | — |
| `REDUCER_STANDARD_DEVIATION` | enumerator | `None` | — | — |
| `REDUCER_MEDIAN` | enumerator | `None` | — | — |
| `REDUCER_LOOKUP` | enumerator | `None` | — | — |
| `REDUCER_VOTE` | enumerator | `None` | — | — |
| `REDUCER_WEIGHTED_MEAN` | enumerator | `None` | — | — |
| `REDUCER_PERCENTILE` | enumerator | `None` | — | — |
| `REDUCER_MIN_DISTANCE` | enumerator | `None` | — | — |
| `REDUCER_PRESENCE` | enumerator | `None` | — | — |
| `REDUCER_NUM_IN_ROI` | enumerator | `None` | — | — |
| `NUM_OF_Reducer_Type` | enumerator | `None` | — | NOTE: Any new values should also be added to transcribe. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_REDUCERTYPES_H` | macro | `None` | — |
| `to_string( AttributeType type)` | function | `QString` | — |
| `to_string( ReducerType type)` | function | `QString` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, AttributeType &attribute_type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `transcribe( GPlatesScribe::Scribe &scribe, ReducerType &reducer_type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

Each `transcribe()` overload encodes enumerators by an explicit string id rather than by ordinal, so reordering or renaming an enumerator does not break saved sessions/projects. Adding a new enumerator (before the `NUM_OF_Attribute_Type` / `NUM_OF_Reducer_Type` sentinel) must be mirrored by hand in the corresponding `transcribe()` table, as the header comments warn — the compiler will not catch a missed entry, and the new value silently fails to round-trip. `to_string()` returns an empty `QString` for any value at or past the `NUM_OF_*` sentinel rather than asserting.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 29 |
| [data-mining/DataSelector](DataSelector.md) | data-mining | 18 |
| [api/CoReg](../api/CoReg.md) | api | 16 |
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 14 |
| [data-mining/RFGToRelationalPropertyMapper](RFGToRelationalPropertyMapper.md) | data-mining | 8 |
| [data-mining/CoRegConfigurationTable](CoRegConfigurationTable.md) | data-mining | 5 |
| [utils/deprecated/FilterMapReduceWorkFlow](../utils/deprecated/FilterMapReduceWorkFlow.md) | utils | 4 |
| [data-mining/DataMiningUtils](DataMiningUtils.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/Types.h
python scripts/gpq.py def GPlatesDataMining::ReducerType --body
python scripts/gpq.py uses ReducerType --kind enum
```
