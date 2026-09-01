# LookupReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 387 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/LookupReducer.h` | C++ | 77 |
| `src/data-mining/LookupReducer.cc` | C++ | 172 |

## Overview

[[[PROSE overview unit=data-mining/LookupReducer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::LookupReducer`](#gplatesdatamininglookupreducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::LookupReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Config` | class | `None` | public | — |
| `LookupReducer( const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature)` | constructor | `None` | public | — |
| `~LookupReducer()` | destructor | `None` | public | — |
| `exec( ReducerInDataset::const_iterator input_begin, ReducerInDataset::const_iterator input_end)` | method | `OpaqueData` | protected | — |
| `d_reconstructed_seed_feature` | field | `GPlatesAppLogic::ReconstructContext::ReconstructedFeature` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `test_polygon_area( std::vector<const GPlatesAppLogic::ReconstructedFeatureGeometry*> seeds, std::vector<const GPlatesAppLogic::ReconstructedFeatureGeometry*> rfgs)` | function | `boost::optional<GPlatesMaths::real_t>` | If the seed geometries are inside polygons, return the area of smallest polygon in which seed locates. |
| `GPLATESDATAMINING_LOOKUPREDUCER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/LookupReducer tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/LookupReducer.h
python scripts/gpq.py def GPlatesDataMining::LookupReducer --body
python scripts/gpq.py uses LookupReducer --kind class
python scripts/gpq.py hier LookupReducer
```
