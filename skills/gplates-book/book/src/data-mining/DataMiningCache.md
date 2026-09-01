# DataMiningCache

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 522 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/DataMiningCache.h` | C++ | 89 |

## Overview

[[[PROSE overview unit=data-mining/DataMiningCache tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::CacheHitTypes`](#gplatesdataminingcachehittypes) | enum | — | — | 0 | — |
| [`GPlatesDataMining::DataMiningCache`](#gplatesdataminingdataminingcache) | class | — | `< class Key, class Data>` | 0 | TODO: Comments.... |

## Members

### `GPlatesDataMining::CacheHitTypes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PERFECT_HIT` | enumerator | `None` | — | — |
| `NEED_FURTHER_PROCESS` | enumerator | `None` | — | — |
| `NO_HIT` | enumerator | `None` | — | — |

### `GPlatesDataMining::DataMiningCache`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `insert( Key key, Data data)` | method | `void` | public | TODO: comments.... |
| `query( Key key)` | method | `CacheHitTypes` | public | TODO: comments.... |
| `clear()` | method | `void` | public | Clear the cache. |
| `~DataMiningCache()` | destructor | `None` | public | — |
| `d_cache` | field | `std::map<Key, Data>` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_DATAMININGCACHE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/DataMiningCache tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/DataMiningCache.h
python scripts/gpq.py def GPlatesDataMining::DataMiningCache --body
python scripts/gpq.py uses DataMiningCache --kind class
python scripts/gpq.py hier DataMiningCache
```
