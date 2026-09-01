# NumInROIDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/NumInROIDataOperator.h` | C++ | 77 |

## Overview

A `DataOperator` that counts and records the number of features associated with a region of interest. The `get_data()` method extracts the size of the associated-features collection and appends it as a data cell, ignoring the attribute name parameter.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::NumInROIDataOperator`](#gplatesdataminingnuminroidataoperator) | class | [`DataOperator`](DataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::NumInROIDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_data( const AssociationOperator::AssociatedCollection& input, /*In*/ const QString& attr_name, /*In*/ DataRow& data_row)` | method | `void` | public | Comments... |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `NumInROIDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `NumInROIDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_NUMINROIDATAOPERATOR_H` | macro | `None` | — |

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
python scripts/gpq.py file src/data-mining/deprecated/NumInROIDataOperator.h
python scripts/gpq.py def GPlatesDataMining::NumInROIDataOperator --body
python scripts/gpq.py uses NumInROIDataOperator --kind class
python scripts/gpq.py hier NumInROIDataOperator
```
