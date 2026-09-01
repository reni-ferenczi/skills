# RFGToPropertyValueMapper

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1527 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/RFGToPropertyValueMapper.h` | C++ | 97 |

## Overview

[[[PROSE overview unit=data-mining/RFGToPropertyValueMapper tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::RFGToPropertyValueMapper`](#gplatesdataminingrfgtopropertyvaluemapper) | class | [`CoRegMapper`](CoRegMapper.md) | — | 0 | — |

## Members

### `GPlatesDataMining::RFGToPropertyValueMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RFGToPropertyValueMapper( const QString& attr_name, bool is_shapefile_attr = false)` | constructor | `None` | public | — |
| `process( CoRegMapper::MapperInDataset::const_iterator input_begin, CoRegMapper::MapperInDataset::const_iterator input_end, CoRegMapper::MapperOutDataset &output)` | method | `void` | public | — |
| `~RFGToPropertyValueMapper()` | destructor | `None` | public | — |
| `d_attr_name` | field | `QString` | protected | — |
| `d_is_shapefile_attr` | field | `bool` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_RFGTOPROPERTYVALUEMAPPER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/RFGToPropertyValueMapper tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/RFGToPropertyValueMapper.h
python scripts/gpq.py def GPlatesDataMining::RFGToPropertyValueMapper --body
python scripts/gpq.py uses RFGToPropertyValueMapper --kind class
python scripts/gpq.py hier RFGToPropertyValueMapper
```
