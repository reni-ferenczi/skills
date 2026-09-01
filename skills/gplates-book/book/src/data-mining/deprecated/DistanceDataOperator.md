# DistanceDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/DistanceDataOperator.h` | C++ | 70 |
| `src/data-mining/deprecated/DistanceDataOperator.cc` | C++ | 72 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/DistanceDataOperator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::DistanceDataOperator`](#gplatesdataminingdistancedataoperator) | class | [`DataOperator`](DataOperator.md) | — | 4 | Comments... |

## Members

### `GPlatesDataMining::DistanceDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_data( const AssociationOperator::AssociatedCollection& input, const QString& attr_name, DataRow& data_row)` | method | `void` | public | — |
| `calculate( const std::vector< double >&)` | method | `boost::optional< double >` | protected | — |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `DistanceDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `DistanceDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_DISTANCEDATAOPERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/DistanceDataOperator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/MaxDistanceDataOperator](MaxDistanceDataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/MeanDistanceDataOperator](MeanDistanceDataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/MedianDistanceDataOperator](MedianDistanceDataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/MinDistanceDataOperator](MinDistanceDataOperator.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/DistanceDataOperator.h
python scripts/gpq.py def GPlatesDataMining::DistanceDataOperator --body
python scripts/gpq.py uses DistanceDataOperator --kind class
python scripts/gpq.py hier DistanceDataOperator
```
