# MinDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 959 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/MinDataOperator.h` | C++ | 109 |
| `src/data-mining/deprecated/MinDataOperator.cc` | C++ | 91 |

## Overview

A `DataOperator` that finds and records the minimum value from a feature property. The `get_data()` method calls `get_min_from_feature()` to extract and compute the minimum value across all associated features, then appends it to a data row. `get_min_from_feature()` iterates over associated features, retrieving a property by name from each, extracting numeric values via a visitor, and computing the minimum across all features. `get_min()` performs the actual minimum computation over a vector of doubles.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MinDataOperator`](#gplatesdataminingmindataoperator) | class | [`DataOperator`](DataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::MinDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_data( const AssociationOperator::AssociatedCollection& input, /*In*/ const QString& attr_name, /*In*/ DataRow& data_row)` | method | `void` | public | Comments... |
| `get_min( const std::vector< double >& input)` | method | `boost::optional< double >` | protected | Comments... |
| `get_min_from_feature( const AssociationOperator::AssociatedCollection& input, const QString& attr_name)` | method | `boost::optional< double >` | protected | Comments... |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `MinDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `MinDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_MINDATAOPERATOR_H` | macro | `None` | — |

## Notes

If a named property is not found on a feature, a warning is logged and that feature is skipped. If no features have the property or all have empty values, `EmptyData` is recorded. The minimum is computed across all values in all features with the property.

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/DataOperatorFactory](DataOperatorFactory.md) | data-mining | 3 |
| [data-mining/deprecated/MinDistanceDataOperator](MinDistanceDataOperator.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/MinDataOperator.h
python scripts/gpq.py def GPlatesDataMining::MinDataOperator --body
python scripts/gpq.py uses MinDataOperator --kind class
python scripts/gpq.py hier MinDataOperator
```
