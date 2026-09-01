# DataOperatorFactory

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/DataOperatorFactory.h` | C++ | 55 |
| `src/data-mining/deprecated/DataOperatorFactory.cc` | C++ | 69 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/DataOperatorFactory tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::DataOperatorFactory`](#gplatesdataminingdataoperatorfactory) | class | — | — | 0 | TODO |

## Members

### `GPlatesDataMining::DataOperatorFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( DataOperatorType type, DataOperatorParameters cfg)` | method | `DataOperator` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_DATAASSOCIATIONFACTORY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/DataOperatorFactory tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/DistanceDataOperator](DistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/LookupDataOperator](LookupDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/MaxDistanceDataOperator](MaxDistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/MeanDistanceDataOperator](MeanDistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/MedianDistanceDataOperator](MedianDistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/MinDataOperator](MinDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/MinDistanceDataOperator](MinDistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/NumInROIDataOperator](NumInROIDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/PresenceDataOperator](PresenceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/SubDataSelector](SubDataSelector.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/DataOperatorFactory.h
python scripts/gpq.py def GPlatesDataMining::DataOperatorFactory --body
python scripts/gpq.py uses DataOperatorFactory --kind class
python scripts/gpq.py hier DataOperatorFactory
```
