# CoRegFilterCache

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1423 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegFilterCache.h` | C++ | 108 |
| `src/data-mining/CoRegFilterCache.cc` | C++ | 62 |

## Overview

[[[PROSE overview unit=data-mining/CoRegFilterCache tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::CoRegFilterCache`](#gplatesdataminingcoregfiltercache) | class | — | — | 0 | — |

## Members

### `GPlatesDataMining::CoRegFilterCache`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `reconstructed_feature_vector_type` | typedef | `std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature>` | public | — |
| `insert( const ConfigurationTableRow& key, const reconstructed_feature_vector_type &value)` | method | `void` | public | — |
| `find( const ConfigurationTableRow& key, reconstructed_feature_vector_type &value)` | method | `bool` | public | — |
| `insert(const ConfigurationTableRow& key)` | method | `void` | public | — |
| `CacheItem` | class | `None` | private | — |
| `d_data` | field | `std::vector<CacheItem>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_COREGFILTERCACHE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/CoRegFilterCache tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/DataSelector](DataSelector.md) | data-mining | 6 |
| [api/CoReg](../api/CoReg.md) | api | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/CoRegFilterCache.h
python scripts/gpq.py def GPlatesDataMining::CoRegFilterCache --body
python scripts/gpq.py uses CoRegFilterCache --kind class
python scripts/gpq.py hier CoRegFilterCache
```
