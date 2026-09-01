# DataSelector

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 579 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/DataSelector.h` | C++ | 192 |
| `src/data-mining/DataSelector.cc` | C++ | 538 |

## Overview

[[[PROSE overview unit=data-mining/DataSelector tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/DataSelector tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
