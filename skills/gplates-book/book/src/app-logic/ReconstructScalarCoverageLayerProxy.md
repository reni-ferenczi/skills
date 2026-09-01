# ReconstructScalarCoverageLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 608 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructScalarCoverageLayerProxy.h` | C++ | 711 |
| `src/app-logic/ReconstructScalarCoverageLayerProxy.cc` | C++ | 705 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructScalarCoverageLayerProxy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructScalarCoverageLayerProxy`](#gplatesapplogicreconstructscalarcoveragelayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy that can evolve specific types of scalar coverages over time (such as crustal thickness and topography). |

## Members

### `GPlatesAppLogic::ReconstructScalarCoverageLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructScalarCoverageLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const ReconstructScalarCoverageLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructScalarCoverageLayerProxy>` | public | A convenience typedef for a shared pointer to a const ReconstructScalarCoverageLayerProxy. |
| `MAX_NUM_RECONSTRUCTIONS_IN_CACHE` | field | `unsigned int` | public | The maximum number of reconstructions to cache for different reconstruction times - each combination represents one cached object. |
| `create( const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params = ReconstructScalarCoverageParams(), unsigned int max_num_reconstructions_in_cache = MAX_NUM_RECONSTRUCTIONS_IN_CACHE)` | method | `non_null_ptr_type` | public | Creates a ReconstructScalarCoverageLayerProxy object. |
| `~ReconstructScalarCoverageLayerProxy()` | destructor | `None` | public | — |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the current scalar type, coverage params and current reconstruction time, by appending them to them to reconstructed\_scalar\_coverages. |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages, const GPlatesPropertyValues::ValueObjectType &scalar_type)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the specified scalar type and the current coverage params and reconstruction time, by appending them to reconstructed\_scalar\_coverages. |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages, const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the specified scalar coverage params and current scalar type and reconstruction time, by appending them to reconstructed\_scalar\_coverages. |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the specified reconstruction time and current scalar type and coverage params, by appending them to reconstructed\_scalar\_coverages. |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages, const GPlatesPropertyValues::ValueObjectType &scalar_type, const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the specified scalar type and coverage params and current reconstruction time, by appending them to reconstructed\_scalar\_coverages. |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages, const GPlatesPropertyValues::ValueObjectType &scalar_type, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the specified scalar type and reconstruction time and current coverage params, by appending them to reconstructed\_scalar\_coverages. |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages, const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the specified coverage params and reconstruction time and current scalar type, by appending them to reconstructed\_scalar\_coverages. |
| `get_reconstructed_scalar_coverages( std::vector<ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages, const GPlatesPropertyValues::ValueObjectType &scalar_type, const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed scalar coverages, for the specified scalar type, coverage params and reconstruction time, by appending them to reconstructed\_scalar\_coverages. |
| `ReconstructedScalarCoverageTimeSpan` | class | `None` | public | A time span of scalar coverages associated with a feature and a specific scalar type. |
| `get_reconstructed_scalar_coverage_time_spans( std::vector<ReconstructedScalarCoverageTimeSpan> &reconstructed_scalar_coverage_time_spans)` | method | `void` | public | Returns the reconstructed scalar coverage time spans, for \*all\* scalar types and the current coverage params, by appending them to them to reconstructed\_scalar\_coverage\_time\_spans. |
| `get_reconstructed_scalar_coverage_time_spans( std::vector<ReconstructedScalarCoverageTimeSpan> &reconstructed_scalar_coverage_time_spans, const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params)` | method | `void` | public | Returns the reconstructed scalar coverage time spans, for \*all\* scalar types and the specified coverage params, by appending them to reconstructed\_scalar\_coverage\_time\_spans. |
| `get_scalar_coverages( std::vector<ScalarCoverageFeatureProperties::Coverage> &scalar_coverages)` | method | `void` | public | Gets all scalar coverages available across the scalar coverage features. |
| `get_scalar_types( std::vector<GPlatesPropertyValues::ValueObjectType> &scalar_types)` | method | `void` | public | Gets all scalar types available across the scalar coverage features. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the scalar coverages have changed since they were last retrieved. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `set_current_scalar_type( const GPlatesPropertyValues::ValueObjectType &scalar_type)` | method | `void` | public | Sets the current scalar type as set by the layer system. |
| `set_current_reconstruct_scalar_coverage_params( const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params)` | method | `void` | public | Sets the parameters used for scalar coverages. |
| `add_reconstructed_domain_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_domain_layer_proxy)` | method | `void` | public | Add a reconstructed domain layer proxy. |
| `remove_reconstructed_domain_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_domain_layer_proxy)` | method | `void` | public | Remove a reconstructed domain layer proxy. |
| `scalar_coverage_time_span_mapped_type` | typedef | `std::pair< GPlatesModel::FeatureHandle::iterator, /* range property iterator */ ScalarCoverageTimeSpan::non_null_ptr_type>` | private | The range property iterator and scalar coverage time span. |
| `scalar_coverage_time_span_map_type` | typedef | `std::map< GPlatesModel::FeatureHandle::const_iterator, scalar_coverage_time_span_mapped_type>` | private | Typedef for mapping geometry properties to their scalar coverage lookup tables. |
| `ScalarCoverageTimeSpanInfo` | struct | `None` | private | Contains optional cached scalar coverage time spans. |
| `ReconstructionInfo` | struct | `None` | private | Contains optional reconstructed scalar coverages. |
| `reconstruction_time_type` | typedef | `GPlatesMaths::real_t` | private | Typedef for reconstruction time. |
| `reconstruction_cache_key_type` | typedef | `std::pair<reconstruction_time_type, GPlatesPropertyValues::ValueObjectType>` | private | Typedef for the key type stored in the reconstruction cache. |
| `reconstruction_cache_value_type` | typedef | `ReconstructionInfo` | private | Typedef for the value type stored in the reconstruction cache. |
| `reconstruction_cache_type` | typedef | `GPlatesUtils::KeyValueCache< reconstruction_cache_key_type, reconstruction_cache_value_type>` | private | Typedef for a cache of reconstruction information keyed by reconstruction time and scalar type. |
| `d_current_reconstructed_domain_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get reconstructed domain geometries, and optionally strains to evolve coverages at. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_current_scalar_type` | field | `GPlatesPropertyValues::ValueObjectType` | private | The current scalar type (each GmlDataBlock can have multiple scalars). |
| `d_current_reconstruct_scalar_coverage_params` | field | `ReconstructScalarCoverageParams` | private | The current scalar coverages parameters as set by the layer system. |
| `d_cached_scalar_types` | field | `boost::optional< std::vector<GPlatesPropertyValues::ValueObjectType> >` | private | Cached scalar types associated with the reconstructed domain \*features\*. |
| `d_cached_scalar_coverages` | field | `boost::optional< std::vector<ScalarCoverageFeatureProperties::Coverage> >` | private | Cached scalar coverages associated with the reconstructed domain \*features\*. |
| `d_cached_reconstruct_scalar_coverage_params` | field | `boost::optional<ReconstructScalarCoverageParams>` | private | Cached scalar coverages parameters associated with d\_cached\_scalar\_coverage\_time\_span\_map. |
| `d_cached_scalar_coverage_time_span_info` | field | `boost::optional<ScalarCoverageTimeSpanInfo>` | private | The cached scalar value time spans. |
| `d_cached_reconstructions` | field | `reconstruction_cache_type` | private | The various reconstructions cached according to reconstruction time and scalar type. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `ReconstructScalarCoverageLayerProxy( const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params, unsigned int max_num_reconstructions_in_cache)` | constructor | `None` | private | — |
| `reset_cache()` | method | `void` | private | Resets all cached data forcing it to be recalculated next time it's accessed. |
| `check_input_layer_proxy( InputLayerProxyWrapperType &input_layer_proxy_wrapper)` | method | `void` | private | Checks if the specified input layer proxy has changed. |
| `check_input_layer_proxies()` | method | `void` | private | Checks if any input layer proxies have changed. |
| `cache_scalar_coverages()` | method | `void` | private | Cache all scalar coverages of all scalar coverage features. |
| `cache_scalar_types()` | method | `void` | private | Cache the unique set of scalar types of all scalar coverage features. |
| `cache_scalar_coverage_time_spans( const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params)` | method | `void` | private | Cache time spans for all scalar coverages (for all scalar types). |
| `cache_topology_reconstructed_scalar_coverage_time_spans( const std::vector<ReconstructContext::TopologyReconstructedFeatureTimeSpan> &topology_reconstructed_feature_time_spans)` | method | `void` | private | Cache time spans for topology-reconstructed scalar coverages. |
| `cache_non_topology_reconstructed_scalar_coverage_time_spans( const std::vector<GPlatesModel::FeatureHandle::weak_ref> &domain_features)` | method | `void` | private | Cache time spans for non-topology-reconstructed scalar coverages. |
| `cache_reconstructed_scalar_coverages` | field | `std::vector<ReconstructedScalarCoverage::non_null_ptr_type>` | private | Cache reconstructed scalar coverages for the specified reconstruction time. |
| `create_empty_reconstruction_info( const reconstruction_cache_key_type &reconstruction_cache_key)` | method | `ReconstructionInfo` | private | Create an empty ReconstructionInfo for the key/value cache. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGELAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructScalarCoverageLayerProxy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructScalarCoverageLayerParams](ReconstructScalarCoverageLayerParams.md) | app-logic | 19 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 5 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 2 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructScalarCoverageLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructScalarCoverageLayerProxy --body
python scripts/gpq.py uses ReconstructScalarCoverageLayerProxy --kind class
python scripts/gpq.py hier ReconstructScalarCoverageLayerProxy
```
