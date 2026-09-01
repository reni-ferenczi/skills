# CoRegistrationLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 419 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/CoRegistrationLayerProxy.h` | C++ | 337 |
| `src/app-logic/CoRegistrationLayerProxy.cc` | C++ | 501 |

## Overview

[[[PROSE overview unit=app-logic/CoRegistrationLayerProxy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::CoRegistrationLayerProxy`](#gplatesapplogiccoregistrationlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy that co-registers reconstructed seed geometries with reconstructed target features. |

## Members

### `GPlatesAppLogic::CoRegistrationLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CoRegistrationLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const CoRegistrationLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const CoRegistrationLayerProxy>` | public | A convenience typedef for a shared pointer to a const CoRegistrationLayerProxy. |
| `create()` | method | `non_null_ptr_type` | public | Creates a CoRegistrationLayerProxy object. |
| `~CoRegistrationLayerProxy()` | destructor | `None` | public | — |
| `get_coregistration_data( GPlatesOpenGL::GLRenderer &renderer)` | method | `boost::optional<CoRegistrationData::non_null_ptr_type>` | public | Returns the co-registration data for the current reconstruction time. renderer is required since \*raster\* co-registration is accelerated using OpenGL. |
| `get_coregistration_data( GPlatesOpenGL::GLRenderer &renderer, const double &reconstruction_time)` | method | `boost::optional<CoRegistrationData::non_null_ptr_type>` | public | Returns the co-registration data for the specified reconstruction time. |
| `get_birth_attribute_data( GPlatesOpenGL::GLRenderer &renderer, const GPlatesModel::FeatureId &feature_id)` | method | `boost::optional<CoRegistrationData::non_null_ptr_type>` | public | Returns all the attribute data at the birth time of the seed feature. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the co-registration data has changed since it was last retrieved. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `add_coregistration_seed_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &coregistration_seed_layer_proxy)` | method | `void` | public | Adds a co-registration seed layer proxy. |
| `get_seed_features()` | method | `std::vector<GPlatesModel::FeatureHandle::weak_ref>` | public | Returns all the seed features for this co-registration layer. |
| `remove_coregistration_seed_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &coregistration_seed_layer_proxy)` | method | `void` | public | Removes a co-registration seed layer proxy. |
| `add_coregistration_target_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &coregistration_target_layer_proxy)` | method | `void` | public | Adds a co-registration target (reconstructed geometries) layer proxy. |
| `remove_coregistration_target_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &coregistration_target_layer_proxy)` | method | `void` | public | Removes a co-registration target (reconstructed geometries) layer proxy. |
| `add_coregistration_target_layer_proxy( const RasterLayerProxy::non_null_ptr_type &coregistration_target_layer_proxy)` | method | `void` | public | Adds a co-registration target (raster) layer proxy. |
| `remove_coregistration_target_layer_proxy( const RasterLayerProxy::non_null_ptr_type &coregistration_target_layer_proxy)` | method | `void` | public | Removes a co-registration target (raster) layer proxy. |
| `set_current_coregistration_configuration_table( const GPlatesDataMining::CoRegConfigurationTable &coregistration_configuration_table)` | method | `void` | public | Sets the configuration table to use for co-registration. |
| `d_current_seed_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get the co-registration reconstructed seed geometries. |
| `d_current_target_reconstruct_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get the co-registration target (reconstructed geometries) layer proxies. |
| `d_current_target_raster_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<RasterLayerProxy>` | private | Used to get the co-registration target (raster) layer proxies. |
| `d_current_coregistration_configuration_table` | field | `GPlatesDataMining::CoRegConfigurationTable` | private | The current co-registration configuration. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_raster_co_registration` | field | `boost::optional<GPlatesGlobal::PointerTraits<GPlatesOpenGL::GLRasterCoRegistration>::non_null_ptr_type>` | private | Used to co-register rasters. |
| `d_cached_coregistration_data` | field | `boost::optional<CoRegistrationData::non_null_ptr_type>` | private | The cached co-registration data - the output of co-registration. |
| `d_cached_reconstruction_time` | field | `boost::optional<GPlatesMaths::real_t>` | private | Cached reconstruction time. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `CoRegistrationLayerProxy()` | constructor | `None` | private | Default constructor. |
| `reset_cache()` | method | `void` | private | Resets any cached variables forcing them to be recalculated next time they're accessed. |
| `check_input_layer_proxy( InputLayerProxyWrapperType &input_layer_proxy_wrapper)` | method | `void` | private | Checks if the specified input layer proxy has changed. |
| `check_input_layer_proxies()` | method | `void` | private | Checks if any input layer proxies have changed. |
| `get_raster_co_registration( GPlatesOpenGL::GLRenderer &renderer)` | method | `boost::optional<GPlatesOpenGL::GLRasterCoRegistration &>` | private | Returns the raster co-registration and creates one the first time this method is called. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_COREGISTRATIONLAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/CoRegistrationLayerProxy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CommandServer](../gui/CommandServer.md) | gui | 22 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 21 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 13 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 11 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 11 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 11 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 10 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 9 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/CoRegistrationLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::CoRegistrationLayerProxy --body
python scripts/gpq.py uses CoRegistrationLayerProxy --kind class
python scripts/gpq.py hier CoRegistrationLayerProxy
```
