# RegionOfInterestFilter

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1366 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/RegionOfInterestFilter.h` | C++ | 245 |
| `src/data-mining/RegionOfInterestFilter.cc` | C++ | 76 |

## Overview

[[[PROSE overview unit=data-mining/RegionOfInterestFilter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::RegionOfInterestFilter`](#gplatesdataminingregionofinterestfilter) | class | [`CoRegFilter`](CoRegFilter.md) | — | 0 | — |

## Members

### `GPlatesDataMining::RegionOfInterestFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RegionOfInterestFilter( const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature, const double range)` | constructor | `None` | public | — |
| `Config` | class | `None` | public | — |
| `process( CoRegFilter::reconstructed_feature_vector_type::const_iterator input_begin, CoRegFilter::reconstructed_feature_vector_type::const_iterator input_end, CoRegFilter::reconstructed_feature_vector_type& output)` | method | `void` | public | — |
| `~RegionOfInterestFilter()` | destructor | `None` | public | — |
| `region_of_interest_filter( GPlatesAppLogic::ReconstructContext::ReconstructedFeature::reconstruction_seq_type &filtered_reconstructed_target_geometries, const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_target_feature)` | method | `void` | protected | — |
| `d_reconstructed_seed_feature` | field | `GPlatesAppLogic::ReconstructContext::ReconstructedFeature` | protected | — |
| `d_range` | field | `double` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_REGIONOFINTERESTFILTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/RegionOfInterestFilter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 4 |
| [api/CoReg](../api/CoReg.md) | api | 3 |
| [data-mining/DataSelector](DataSelector.md) | data-mining | 2 |
| [data-mining/CoRegConfigurationTable](CoRegConfigurationTable.md) | data-mining | 1 |
| [data-mining/CoRegFilterCache](CoRegFilterCache.md) | data-mining | 1 |
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 1 |
| [data-mining/ScribeExportDataMining](ScribeExportDataMining.md) | data-mining | 1 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/RegionOfInterestFilter.h
python scripts/gpq.py def GPlatesDataMining::RegionOfInterestFilter --body
python scripts/gpq.py uses RegionOfInterestFilter --kind class
python scripts/gpq.py hier RegionOfInterestFilter
```
