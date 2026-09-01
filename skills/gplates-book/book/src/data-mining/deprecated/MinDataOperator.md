# MinDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 959 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/MinDataOperator.h` | C++ | 109 |
| `src/data-mining/deprecated/MinDataOperator.cc` | C++ | 91 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/MinDataOperator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/deprecated/MinDataOperator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
