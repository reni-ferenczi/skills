# CoRegFilter

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 984 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegFilter.h` | C++ | 174 |
| `src/data-mining/CoRegFilter.cc` | C++ | 44 |

## Overview

[[[PROSE overview unit=data-mining/CoRegFilter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::CoRegFilter`](#gplatesdataminingcoregfilter) | class | — | — | 3 | — |
| [`GPlatesDataMining::DummyFilter`](#gplatesdataminingdummyfilter) | class | [`CoRegFilter`](CoRegFilter.md) | — | 0 | — |

## Members

### `GPlatesDataMining::CoRegFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `reconstructed_feature_vector_type` | typedef | `std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature>` | public | — |
| `Config` | class | `None` | public | — |
| `process( reconstructed_feature_vector_type::const_iterator first, reconstructed_feature_vector_type::const_iterator last, reconstructed_feature_vector_type& output )` | method | `void` | public | — |
| `~CoRegFilter()` | destructor | `None` | public | — |

### `GPlatesDataMining::DummyFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Config` | class | `None` | public | — |
| `process( CoRegFilter::reconstructed_feature_vector_type::const_iterator first, CoRegFilter::reconstructed_feature_vector_type::const_iterator last, CoRegFilter::reconstructed_feature_vector_type& output)` | method | `void` | public | — |
| `~DummyFilter()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_COREGFILTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/CoRegFilter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/RegionOfInterestFilter](RegionOfInterestFilter.md) | data-mining | 21 |
| [data-mining/SeedSelfFilter](SeedSelfFilter.md) | data-mining | 18 |
| [data-mining/DataSelector](DataSelector.md) | data-mining | 8 |
| [data-mining/CoRegConfigurationTable](CoRegConfigurationTable.md) | data-mining | 7 |
| [api/CoReg](../api/CoReg.md) | api | 5 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 4 |
| [data-mining/CoRegFilterCache](CoRegFilterCache.md) | data-mining | 3 |
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 3 |
| [data-mining/ScribeExportDataMining](ScribeExportDataMining.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/CoRegFilter.h
python scripts/gpq.py def GPlatesDataMining::DummyFilter --body
python scripts/gpq.py uses DummyFilter --kind class
python scripts/gpq.py hier DummyFilter
```
