# MeanDistanceDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/MeanDistanceDataOperator.h` | C++ | 73 |

## Overview

A `DistanceDataOperator` subclass intended to compute the mean (average) distance from a collection of distance values. The `calculate()` method is declared virtual but not implemented—it currently contains only a TODO comment and returns `EmptyData` unconditionally.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MeanDistanceDataOperator`](#gplatesdataminingmeandistancedataoperator) | class | [`DistanceDataOperator`](DistanceDataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::MeanDistanceDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `calculate( const std::vector< double >& input)` | method | `boost::optional< double >` | protected | — |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `MeanDistanceDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `MeanDistanceDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_MEANDISTANCEDATAOPERATOR_H` | macro | `None` | — |

## Notes

The `calculate()` method is not implemented and always returns `EmptyData`.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/MeanDistanceDataOperator.h
python scripts/gpq.py def GPlatesDataMining::MeanDistanceDataOperator --body
python scripts/gpq.py uses MeanDistanceDataOperator --kind class
python scripts/gpq.py hier MeanDistanceDataOperator
```
