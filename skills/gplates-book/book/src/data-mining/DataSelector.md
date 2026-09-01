# DataSelector

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 579 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/DataSelector.h` | C++ | 192 |
| `src/data-mining/DataSelector.cc` | C++ | 538 |

## Overview

`DataSelector` is the entry point that drives a whole co-registration run: given the reconstructed seed features, the target `LayerProxy`s and a reconstruction time, `select()` produces a `DataTable` with one row per seed and one column per row of the `CoRegConfigurationTable` it was built from. Callers get an instance only through the static `create()` factory, which returns a `boost::shared_ptr` — the constructor itself is protected and also `optimize()`s the configuration table on first use.

`select()` splits target layers into two paths. Raster targets are handled by `co_register_target_reconstructed_rasters()`, which groups configuration rows by `(layer, band name)` so multiple attributes of the same raster are co-registered together via `GPlatesOpenGL::GLRasterCoRegistration` — this path only runs when a `RasterCoRegistration` (an OpenGL renderer plus co-registration context) is supplied; without it, raster columns are simply skipped. Reconstructed-geometry targets go through `co_register_target_reconstructed_geometries()`, which, for each seed and each configuration row, builds the row's `CoRegFilter`/`CoRegMapper`/`CoRegReducer` triple with `create_filter_map_reduce()`, runs filter then map then reduce, and writes the single resulting `OpaqueData` into the corresponding cell — using a `CoRegFilterCache` so identical filter configurations are not recomputed for every row.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::DataSelector`](#gplatesdataminingdataselector) | class | — | — | 0 | — |

## Members

### `GPlatesDataMining::DataSelector`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterCoRegistration` | struct | `None` | public | Used for co-registering target rasters. |
| `create( const CoRegConfigurationTable& table)` | method | `boost::shared_ptr<DataSelector>` | public | — |
| `select( const std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature> &reconstructed_seed_features, const std::vector<GPlatesAppLogic::LayerProxy::non_null_ptr_type> &target_layer_proxies, const double &reconstruction_time, DataTable &result_data_table, boost::optional<RasterCoRegistration> co_register_r ...` | method | `void` | public | Given the seed and target, select() will return the associated data in DataTable. |
| `set_data_table( const DataTable& table)` | method | `void` | public | — |
| `populate_table_header()` | method | `void` | public | — |
| `~DataSelector()` | destructor | `None` | public | — |
| `is_config_table_valid( const std::vector<GPlatesAppLogic::LayerProxy::non_null_ptr_type> &target_layer_proxies)` | method | `bool` | protected | It's possible that some config rows might reference non-existent, or inactive, target layers in which case this method returns false. |
| `fill_seed_info( const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature, DataRowSharedPtr)` | method | `void` | protected | — |
| `co_register_target_reconstructed_rasters( GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLRasterCoRegistration &raster_co_registration, const std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature> &reconstructed_seed_features, const double &reconstruction_time, GPlatesDataMining::DataTable &result ...` | method | `void` | protected | — |
| `co_register_target_reconstructed_geometries( const std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature> &reconstructed_seed_features, const double &reconstruction_time, GPlatesDataMining::DataTable &result_data_table)` | method | `void` | protected | — |
| `DataSelector()` | constructor | `None` | protected | default constructor |
| `DataSelector(const DataSelector&)` | constructor | `None` | protected | copy constructor |
| `operator=` | field | `DataSelector` | protected | assignment |
| `DataSelector(const CoRegConfigurationTable &table)` | constructor | `None` | protected | — |
| `d_cfg_table` | field | `CoRegConfigurationTable` | protected | — |
| `d_table_header` | field | `TableHeader` | protected | — |
| `d_data_index` | field | `unsigned` | protected | — |
| `d_data_table` | field | `DataTable` | protected | TODO: Need to remove the "static" in the future. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `d_data_table` | variable | `GPlatesDataMining::DataTable` | — |
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | The BOOST\_FOREACH macro in versions of boost before 1.37 uses the same local variable name in each instantiation. |
| `GPLATESDATAMINING_DATASELECTOR_H` | macro | `None` | — |

## Notes

`d_data_table` is `static`, a state the header itself flags as a `TODO` to remove — it is a shared, process-wide result buffer rather than per-instance state, so concurrent or nested `DataSelector` usage would clobber it. `select()` first calls `is_config_table_valid()` and, if any configuration row references a target layer that is disabled or no longer connected, logs a warning and skips co-registration entirely rather than producing a partial table; the header notes this situation can arise because Qt's slot delivery order does not guarantee the configuration dialog removes stale rows before a reconstruction-wide co-registration runs. A seed feature with no reconstructions at the given time (inactive at that time) is left with `EmptyData` in every column rather than being dropped from the table.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 11 |
| [api/CoReg](../api/CoReg.md) | api | 6 |
| [data-mining/deprecated/SubDataSelector](deprecated/SubDataSelector.md) | data-mining | 3 |
| [opengl/GLContext](../opengl/GLContext.md) | opengl | 2 |
| [opengl/GLRenderTargetImpl](../opengl/GLRenderTargetImpl.md) | opengl | 2 |
| [opengl/GLVertexArrayObject](../opengl/GLVertexArrayObject.md) | opengl | 2 |
| [app-logic/CoRegistrationLayerTask](../app-logic/CoRegistrationLayerTask.md) | app-logic | 1 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 1 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/DataSelector.h
python scripts/gpq.py def GPlatesDataMining::DataSelector --body
python scripts/gpq.py uses DataSelector --kind class
python scripts/gpq.py hier DataSelector
```
