# SubDataSelector

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 397 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/SubDataSelector.h` | C++ | 75 |
| `src/data-mining/deprecated/SubDataSelector.cc` | C++ | 86 |

## Overview

A deprecated prospector job that extracts data for a single seed feature according to a co-registration configuration. The `do_job()` method iterates through each row of a `CoRegConfigurationTable`, using association operators to find related features and data operators to extract attribute values, accumulating all results in a single data row.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::SubDataSelector`](#gplatesdataminingsubdataselector) | class | [`Prospector`](Prospector.md) | — | 0 | — |

## Members

### `GPlatesDataMining::SubDataSelector`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SubDataSelector( const CoRegConfigurationTable& matrix, GPlatesModel::FeatureHandle::const_weak_ref seed_feature, const FeatureGeometryMap& seed_geometry_map, const FeatureGeometryMap& target_geometry_map)` | constructor | `None` | public | — |
| `do_job()` | method | `void` | public | — |
| `~SubDataSelector()` | destructor | `None` | public | — |
| `d_data_row` | field | `DataRowSharedPtr` | protected | — |
| `d_matrix` | field | `CoRegConfigurationTable` | protected | — |
| `d_seed_feature` | field | `GPlatesModel::FeatureHandle::const_weak_ref` | protected | — |
| `d_seed_geometry_map` | field | `FeatureGeometryMap` | protected | — |
| `d_target_geometry_map` | field | `FeatureGeometryMap` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_SUBDATASELECTOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/SubDataSelector.h
python scripts/gpq.py def GPlatesDataMining::SubDataSelector --body
python scripts/gpq.py uses SubDataSelector --kind class
python scripts/gpq.py hier SubDataSelector
```
