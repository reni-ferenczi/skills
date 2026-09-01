# MinDistanceDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/MinDistanceDataOperator.h` | C++ | 70 |
| `src/data-mining/deprecated/MinDistanceDataOperator.cc` | C++ | 26 |

## Overview

A `DistanceDataOperator` subclass that computes the minimum distance from a collection of distance values. The `calculate()` method delegates to `DataMiningUtils::minimum()` to find and return the smallest distance in the input vector.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MinDistanceDataOperator`](#gplatesdataminingmindistancedataoperator) | class | [`DistanceDataOperator`](DistanceDataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::MinDistanceDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `calculate( const std::vector< double >& input)` | method | `boost::optional< double >` | protected | — |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `MinDistanceDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `MinDistanceDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_MINDISTANCEDATAOPERATOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/DataOperatorFactory](DataOperatorFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/MinDistanceDataOperator.h
python scripts/gpq.py def GPlatesDataMining::MinDistanceDataOperator --body
python scripts/gpq.py uses MinDistanceDataOperator --kind class
python scripts/gpq.py hier MinDistanceDataOperator
```
