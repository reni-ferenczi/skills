# DistanceDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/DistanceDataOperator.h` | C++ | 70 |
| `src/data-mining/deprecated/DistanceDataOperator.cc` | C++ | 72 |

## Overview

An abstract base class for extracting and reducing distance values from feature associations in data-mining workflows. The `get_data()` method collects minimum distances from each associated feature and appends the result of the `calculate()` method to a `DataRow`. Subclasses override `calculate()` to implement different reduction strategies on the distance vector. This class is part of a deprecated data-mining architecture.

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

The constructors are protected; instances are created only by the `DataOperatorFactory` friend class. The `calculate()` method is pure virtual and must be overridden by subclasses. If no valid distances are found, `get_data()` appends `EmptyData`.

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
