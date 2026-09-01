# DataOperatorFactory

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/DataOperatorFactory.h` | C++ | 55 |
| `src/data-mining/deprecated/DataOperatorFactory.cc` | C++ | 69 |

## Overview

A factory for creating `DataOperator` instances based on type enum and parameters. The static `create()` method accepts a `DataOperatorType` and `DataOperatorParameters` and returns an appropriate operator instance. Supported types include Min, Lookup, Min Distance, Presence, and NumberInROI operators. This class is part of a deprecated data-mining workflow architecture.

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

The `create()` method returns a newly allocated `DataOperator` instance; callers are responsible for managing the returned pointer. The default case (unknown type) returns a `MinDataOperator` instance.

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
