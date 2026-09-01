# MaxDistanceDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/MaxDistanceDataOperator.h` | C++ | 70 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/MaxDistanceDataOperator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MaxDistanceDataOperator`](#gplatesdataminingmaxdistancedataoperator) | class | [`DistanceDataOperator`](DistanceDataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::MaxDistanceDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `calculate( const std::vector< double >& input)` | method | `boost::optional< double >` | protected | — |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `MaxDistanceDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `MaxDistanceDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_MAXDISTANCEDATAOPERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/MaxDistanceDataOperator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/MaxDistanceDataOperator.h
python scripts/gpq.py def GPlatesDataMining::MaxDistanceDataOperator --body
python scripts/gpq.py uses MaxDistanceDataOperator --kind class
python scripts/gpq.py hier MaxDistanceDataOperator
```
