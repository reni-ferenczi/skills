# OpaqueData

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1241 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/OpaqueData.h` | C++ | 102 |

## Overview

[[[PROSE overview unit=data-mining/OpaqueData tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::dummy`](#gplatesdataminingdummy) | struct | — | — | 0 | Use a pointer of dummy class data member to define empty\_data\_type, which will be used when there is no valid data in OpaqueData type |
| [`GPlatesDataMining::empty_data_type`](#gplatesdataminingempty_data_type) | typedef | — | — | 0 | — |
| [`GPlatesDataMining::OpaqueData`](#gplatesdataminingopaquedata) | typedef | — | — | 0 | The definition of opaque data type. |
| [`GPlatesDataMining::is_empty_visitor`](#gplatesdataminingis_empty_visitor) | class | `boost::static_visitor<bool>` | — | 0 | — |

## Members

### `GPlatesDataMining::dummy`

*None.*

### `GPlatesDataMining::empty_data_type`

*None.*

### `GPlatesDataMining::OpaqueData`

*None.*

### `GPlatesDataMining::is_empty_visitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const empty_data_type)` | operator | `bool` | public | — |
| `operator()(const type)` | operator | `bool` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_OPAQUEDATA_H` | macro | `None` | — |
| `EmptyData` | variable | `empty_data_type` | — |
| `is_empty_opaque(const OpaqueData& data)` | function | `bool` | — |

## Notes

[[[PROSE notes unit=data-mining/OpaqueData tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/DataMiningUtils](DataMiningUtils.md) | data-mining | 21 |
| [data-mining/CoRegReducer](CoRegReducer.md) | data-mining | 9 |
| [data-mining/DataTable](DataTable.md) | data-mining | 9 |
| [data-mining/LookupReducer](LookupReducer.md) | data-mining | 5 |
| [data-mining/MaxReducer](MaxReducer.md) | data-mining | 5 |
| [data-mining/MinReducer](MinReducer.md) | data-mining | 5 |
| [data-mining/VoteReducer](VoteReducer.md) | data-mining | 4 |
| [unit-test/DataAssociationDataTableTest](../unit-test/DataAssociationDataTableTest.md) | unit-test | 4 |
| [api/PyFeature](../api/PyFeature.md) | api | 3 |
| [data-mining/MeanReducer](MeanReducer.md) | data-mining | 3 |
| [data-mining/MedianReducer](MedianReducer.md) | data-mining | 3 |
| [data-mining/RFGToRelationalPropertyMapper](RFGToRelationalPropertyMapper.md) | data-mining | 3 |
| [data-mining/deprecated/DistanceDataOperator](deprecated/DistanceDataOperator.md) | data-mining | 3 |
| [data-mining/deprecated/LookupDataOperator](deprecated/LookupDataOperator.md) | data-mining | 3 |
| [data-mining/CoRegMapper](CoRegMapper.md) | data-mining | 2 |
| [data-mining/DataSelector](DataSelector.md) | data-mining | 2 |
| [data-mining/GetValueFromPropertyVisitor](GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [data-mining/PercentileReducer](PercentileReducer.md) | data-mining | 2 |
| [data-mining/WeightedMeanReducer](WeightedMeanReducer.md) | data-mining | 2 |
| [data-mining/deprecated/MinDataOperator](deprecated/MinDataOperator.md) | data-mining | 2 |

*... and 7 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/OpaqueData.h
python scripts/gpq.py def GPlatesDataMining::is_empty_visitor --body
python scripts/gpq.py uses is_empty_visitor --kind class
python scripts/gpq.py hier is_empty_visitor
```
