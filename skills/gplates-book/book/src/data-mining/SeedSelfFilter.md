# SeedSelfFilter

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1260 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/SeedSelfFilter.h` | C++ | 124 |
| `src/data-mining/SeedSelfFilter.cc` | C++ | 44 |

## Overview

[[[PROSE overview unit=data-mining/SeedSelfFilter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::SeedSelfFilter`](#gplatesdataminingseedselffilter) | class | [`CoRegFilter`](CoRegFilter.md) | — | 0 | — |

## Members

### `GPlatesDataMining::SeedSelfFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Config` | class | `None` | public | — |
| `SeedSelfFilter( const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature)` | constructor | `None` | public | — |
| `process( CoRegFilter::reconstructed_feature_vector_type::const_iterator input_begin, CoRegFilter::reconstructed_feature_vector_type::const_iterator input_end, CoRegFilter::reconstructed_feature_vector_type& output)` | method | `void` | public | — |
| `~SeedSelfFilter()` | destructor | `None` | public | — |
| `d_reconstructed_seed_feature` | field | `GPlatesAppLogic::ReconstructContext::ReconstructedFeature` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_SEEDSELFFILTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/SeedSelfFilter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 1 |
| [data-mining/ScribeExportDataMining](ScribeExportDataMining.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/SeedSelfFilter.h
python scripts/gpq.py def GPlatesDataMining::SeedSelfFilter --body
python scripts/gpq.py uses SeedSelfFilter --kind class
python scripts/gpq.py hier SeedSelfFilter
```
