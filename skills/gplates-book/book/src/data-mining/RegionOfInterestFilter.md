# RegionOfInterestFilter

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1366 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/RegionOfInterestFilter.h` | C++ | 245 |
| `src/data-mining/RegionOfInterestFilter.cc` | C++ | 76 |

## Overview

`RegionOfInterestFilter` is a filter that selects reconstructed geometries within a specified distance of a seed feature, commonly used in co-registration data mining pipelines to focus on nearby features. It extends `CoRegFilter` and takes a reconstructed seed feature and a range in kilometers. The `process()` method filters input features, keeping only the geometries whose minimum distance to any seed geometry is below the range threshold (converted to radians). Overlapping polygon interiors count as zero distance, and the filter properly handles the Earth's curvature by using angular extent calculations.

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

The filter's `Config` inner class is serializable via the Scribe framework for persistence in GPlates projects and sessions.

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
