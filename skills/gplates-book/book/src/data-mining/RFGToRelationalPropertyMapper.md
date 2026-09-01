# RFGToRelationalPropertyMapper

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 387 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/RFGToRelationalPropertyMapper.h` | C++ | 124 |

## Overview

[[[PROSE overview unit=data-mining/RFGToRelationalPropertyMapper tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/RFGToRelationalPropertyMapper tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
