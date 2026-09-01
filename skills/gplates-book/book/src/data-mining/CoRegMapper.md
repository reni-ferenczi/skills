# CoRegMapper

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1574 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegMapper.h` | C++ | 95 |

## Overview

[[[PROSE overview unit=data-mining/CoRegMapper tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::CoRegMapper`](#gplatesdataminingcoregmapper) | class | — | — | 3 | — |
| [`GPlatesDataMining::DummyMapper`](#gplatesdataminingdummymapper) | class | [`CoRegMapper`](CoRegMapper.md) | — | 0 | — |

## Members

### `GPlatesDataMining::CoRegMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `reconstructed_feature_vector_type` | typedef | `std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature>` | public | — |
| `MapperInDataset` | typedef | `reconstructed_feature_vector_type` | public | — |
| `MapperOutDataset` | typedef | `std::vector< boost::tuple< OpaqueData, GPlatesAppLogic::ReconstructContext::ReconstructedFeature> >` | public | — |
| `process( MapperInDataset::const_iterator first, MapperInDataset::const_iterator last, MapperOutDataset& output )` | method | `void` | public | — |
| `~CoRegMapper()` | destructor | `None` | public | — |

### `GPlatesDataMining::DummyMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `process( CoRegMapper::MapperInDataset::const_iterator first, CoRegMapper::MapperInDataset::const_iterator last, CoRegMapper::MapperOutDataset& output)` | method | `void` | public | — |
| `~DummyMapper()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_COREGMAPPER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/CoRegMapper tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/RFGToRelationalPropertyMapper](RFGToRelationalPropertyMapper.md) | data-mining | 12 |
| [data-mining/RFGToPropertyValueMapper](RFGToPropertyValueMapper.md) | data-mining | 8 |
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 2 |
| [data-mining/DataSelector](DataSelector.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/CoRegMapper.h
python scripts/gpq.py def GPlatesDataMining::CoRegMapper --body
python scripts/gpq.py uses CoRegMapper --kind class
python scripts/gpq.py hier CoRegMapper
```
