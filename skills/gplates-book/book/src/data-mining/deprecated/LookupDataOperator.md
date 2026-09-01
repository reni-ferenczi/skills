# LookupDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 937 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/LookupDataOperator.h` | C++ | 84 |
| `src/data-mining/deprecated/LookupDataOperator.cc` | C++ | 140 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/LookupDataOperator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::LookUpDataOperator`](#gplatesdatamininglookupdataoperator) | class | [`DataOperator`](DataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::LookUpDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~LookUpDataOperator()` | destructor | `None` | public | — |
| `get_data( const AssociationOperator::AssociatedCollection& input, const QString& attr_name, DataRow& data_row)` | method | `void` | public | — |
| `get_qstring_from_feature( const AssociationOperator::AssociatedCollection& input, const QString& attr_name)` | method | `boost::optional< QString >` | protected | — |
| `get_qstring_from_shape_attr( const AssociationOperator::AssociatedCollection& input, const QString& attr_name)` | method | `boost::optional< QString >` | protected | — |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `LookUpDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `LookUpDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_LOOKUPDATAOPERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/LookupDataOperator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/DataOperatorFactory](DataOperatorFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/LookupDataOperator.h
python scripts/gpq.py def GPlatesDataMining::LookUpDataOperator --body
python scripts/gpq.py uses LookUpDataOperator --kind class
python scripts/gpq.py hier LookUpDataOperator
```
