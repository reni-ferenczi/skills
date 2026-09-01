# PresenceDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/PresenceDataOperator.h` | C++ | 83 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/PresenceDataOperator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::PresenceDataOperator`](#gplatesdataminingpresencedataoperator) | class | [`DataOperator`](DataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::PresenceDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_data( const AssociationOperator::AssociatedCollection& input, /*In*/ const QString& attr_name, /*In*/ DataRow& data_row)` | method | `void` | public | Comments... |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `PresenceDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `PresenceDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_PRESENCEDATAOPERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/PresenceDataOperator tier=3]]]
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
python scripts/gpq.py file src/data-mining/deprecated/PresenceDataOperator.h
python scripts/gpq.py def GPlatesDataMining::PresenceDataOperator --body
python scripts/gpq.py uses PresenceDataOperator --kind class
python scripts/gpq.py hier PresenceDataOperator
```
