# RFGToRelationalPropertyMapper

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 387 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/RFGToRelationalPropertyMapper.h` | C++ | 124 |

## Overview

`RFGToRelationalPropertyMapper` is a mapper that computes relational properties between reconstructed features and a reference seed feature. It extends `CoRegMapper` and supports multiple attribute types: `DISTANCE_ATTRIBUTE` computes the shortest distance between seed and target geometries, `PRESENCE_ATTRIBUTE` checks if any input features exist, and `NUMBER_OF_PRESENCE_ATTRIBUTE` counts input features. The `process()` method iterates through target features and outputs tuples of computed values with their features.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::RFGToRelationalPropertyMapper`](#gplatesdataminingrfgtorelationalpropertymapper) | class | [`CoRegMapper`](CoRegMapper.md) | — | 0 | — |

## Members

### `GPlatesDataMining::RFGToRelationalPropertyMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RFGToRelationalPropertyMapper( const AttributeType attr_type, const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature)` | constructor | `None` | public | — |
| `process( CoRegMapper::MapperInDataset::const_iterator input_begin, CoRegMapper::MapperInDataset::const_iterator input_end, CoRegMapper::MapperOutDataset &output)` | method | `void` | public | — |
| `~RFGToRelationalPropertyMapper()` | destructor | `None` | public | — |
| `d_attr_type` | field | `AttributeType` | protected | — |
| `d_reconstructed_seed_feature` | field | `GPlatesAppLogic::ReconstructContext::ReconstructedFeature` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_RFGTORELATIONALPROPERTYMAPPER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/RFGToRelationalPropertyMapper.h
python scripts/gpq.py def GPlatesDataMining::RFGToRelationalPropertyMapper --body
python scripts/gpq.py uses RFGToRelationalPropertyMapper --kind class
python scripts/gpq.py hier RFGToRelationalPropertyMapper
```
