# Types

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 232 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/Types.h` | C++ | 199 |

## Overview

[[[PROSE overview unit=data-mining/Types tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/Types tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
