# CoRegFilter

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 984 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegFilter.h` | C++ | 174 |
| `src/data-mining/CoRegFilter.cc` | C++ | 44 |

## Overview

`CoRegFilter` is the abstract base of the co-registration filter/mapper hierarchy: `process()` takes a range of `GPlatesAppLogic::ReconstructContext::ReconstructedFeature` and appends the ones that pass into `output`, letting `RegionOfInterestFilter` and `SeedSelfFilter` narrow the candidate features attributed to a seed before a reducer runs. Each filter also carries a nested `Config` — a small abstract factory that knows how to `create_filter()` for a given seed feature, compare configs for equality and ordering (so identical filter setups can be cached), and describe itself (`filter_name()`, `to_string()`, `get_parameters_as_strings()`) for the co-registration UI and for `Scribe` serialisation of saved layer setups.

`DummyFilter` is the trivial concrete instance: its `process()` is a no-op, so it passes every candidate through unchanged. It exists as the default/no-filtering choice `CoRegConfigurationTable` and `DataSelector` fall back to when no real filter is configured, and as a template for how a `Config` subclass wires itself up — though its own `operator<` and `operator==` are unimplemented stubs that throw `GPlatesGlobal::LogException`.

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

`Config::create_filter()` returns a raw, heap-allocated `CoRegFilter*` — ownership passes to the caller. `DummyFilter::Config::operator<` and `operator==` throw `GPlatesGlobal::LogException` rather than implement a real comparison, so code that orders or deduplicates `Config` objects must not exercise those paths on a `DummyFilter`.

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
