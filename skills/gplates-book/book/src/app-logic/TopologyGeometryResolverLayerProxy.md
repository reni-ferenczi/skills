# TopologyGeometryResolverLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 82 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyGeometryResolverLayerProxy.h` | C++ | 771 |
| `src/app-logic/TopologyGeometryResolverLayerProxy.cc` | C++ | 1486 |

## Overview

[[[PROSE overview unit=app-logic/TopologyGeometryResolverLayerProxy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyGeometryResolverLayerProxy`](#gplatesapplogictopologygeometryresolverlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy that resolves topological geometries (boundaries and lines) from feature collection(s) containing topological boundary and line features. |

## Members

### `GPlatesAppLogic::TopologyGeometryResolverLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologyGeometryResolverLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const TopologyGeometryResolverLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologyGeometryResolverLayerProxy>` | public | A convenience typedef for a shared pointer to a const TopologyGeometryResolverLayerProxy. |
| `create()` | method | `non_null_ptr_type` | public | Creates a TopologyGeometryResolverLayerProxy object. |
| `~TopologyGeometryResolverLayerProxy()` | destructor | `None` | public | — |
| `get_resolved_topological_geometries( std::vector<ResolvedTopologicalGeometry::non_null_ptr_type> &resolved_topological_geometries, boost::optional<std::vector<ReconstructHandle::type> &> reconstruct_handles = boost::none)` | method | `void` | public | Returns the resolved topological geometries (polygons and polylines), for the current reconstruction time, by appending them to them to resolved\_topological\_geometries. |
| `get_resolved_topological_geometries( std::vector<ResolvedTopologicalGeometry::non_null_ptr_type> &resolved_topological_geometries, const double &reconstruction_time, boost::optional<std::vector<ReconstructHandle::type> &> reconstruct_handles = boost::none)` | method | `void` | public | Returns the resolved topological geometries (polygons and polylines), at the specified time, by appending them to them to resolved\_topological\_geometries. |
| `get_resolved_topological_boundaries( std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries)` | method | `ReconstructHandle::type` | public | Returns the resolved topological boundaries (polygons), for the current reconstruction time, by appending them to them to resolved\_topological\_boundaries. |
| `get_resolved_topological_boundaries( std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the resolved topological boundaries (polygons), at the specified time, by appending them to them to resolved\_topological\_boundaries. |
| `get_resolved_topological_lines( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines)` | method | `ReconstructHandle::type` | public | Returns the resolved topological lines (polylines), for the current reconstruction time, by appending them to them to resolved\_topological\_lines. |
| `get_resolved_topological_lines( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the resolved topological lines (polylines), at the specified time, by appending them to them to resolved\_topological\_lines. |
| `get_resolved_topological_sections( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_sections, const std::set<GPlatesModel::FeatureId> &topological_sections_referenced)` | method | `ReconstructHandle::type` | public | Same as get\_resolved\_topological\_lines except limits the resolved topological lines to those matching the specified feature IDs. |
| `get_resolved_topological_sections( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_sections, const std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | — |
| `get_resolved_boundary_time_span( const TimeSpanUtils::TimeRange &time_range)` | method | `TopologyReconstruct::resolved_boundary_time_span_type::non_null_ptr_to_const_type` | public | Returns a time span of resolved topological boundaries. |
| `get_resolved_topological_geometry_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_velocities, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0, boost::optional<std::vector<ReconstructHandle::t ...` | method | `void` | public | Returns the velocities associated with the resolved topological geometries (polygons and polylines), for the current reconstruction time, by appending them to them to resolved\_topological\_velocities. |
| `get_resolved_topological_geometry_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_velocities, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0, boost::option ...` | method | `void` | public | Returns the velocities associated with the resolved topological geometries (polygons and polylines), for the specified reconstruction time, by appending them to resolved\_topological\_velocities. |
| `get_resolved_topological_line_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_line_velocities, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological lines (polylines), for the current reconstruction time, by appending them to them to resolved\_topological\_line\_velocities. |
| `get_resolved_topological_boundary_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_boundary_velocities, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological boundaries (polygons), for the specified reconstruction time, by appending them to resolved\_topological\_boundary\_velocities. |
| `get_resolved_topological_boundary_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_boundary_velocities, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological boundaries (polygons), for the current reconstruction time, by appending them to them to resolved\_topological\_boundary\_velocities. |
| `get_resolved_topological_line_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_line_velocities, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological lines (polylines), for the specified reconstruction time, by appending them to resolved\_topological\_line\_velocities. |
| `get_current_topological_geometry_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_geometry_features)` | method | `void` | public | Returns only the topological geometry subset (topological lines and boundaries) of features set by add\_topological\_geometry\_feature\_collection, etc. |
| `get_current_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &features)` | method | `void` | public | Returns all features set by add\_topological\_geometry\_feature\_collection, etc. |
| `get_current_reconstruction_layer_proxy()` | method | `ReconstructionLayerProxy::non_null_ptr_type` | public | Returns the current reconstruction layer proxy used for reconstructions. |
| `get_current_dependent_topological_sections( std::set<GPlatesModel::FeatureId> &resolved_boundary_dependent_topological_sections, std::set<GPlatesModel::FeatureId> &resolved_line_dependent_topological_sections)` | method | `void` | public | Inserts the feature IDs of topological sections referenced by the current topological features (resolved lines and boundaries) for \*all\* times (not just the current time). |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the resolved topological geometries (boundaries and lines) have changed since they were last retrieved. |
| `get_resolved_lines_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if \*just\* the resolved topological geometries \*lines\* have changed since they were last retrieved. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `set_current_reconstruction_layer_proxy( const ReconstructionLayerProxy::non_null_ptr_type &reconstruction_layer_proxy)` | method | `void` | public | Set the reconstruction layer proxy that defines velocities inside rigid topological boundaries. |
| `set_current_topological_sections_layer_proxies( const std::vector<ReconstructLayerProxy::non_null_ptr_type> & reconstructed_geometry_topological_sections_layer_proxies, const std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type> & resolved_line_topological_sections_layer_proxies)` | method | `void` | public | Sets the current layer proxies used to reconstruct/resolve the topological geometry sections. |
| `add_topological_geometry_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Add to the list of feature collections containing topological geometry features. |
| `remove_topological_geometry_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Remove from the list of feature collections containing topological geometry features. |
| `modified_topological_geometry_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | A topological geometry feature collection was modified. |
| `ResolvedBoundaries` | struct | `None` | private | Contains resolved topological boundary (polygon) geometries. |
| `ResolvedLines` | struct | `None` | private | Contains resolved topological line (polyline) geometries. |
| `ResolvedBoundaryTimeSpan` | struct | `None` | private | Contains resolved topological boundaries time span. |
| `d_current_topological_line_features` | field | `std::vector<GPlatesModel::FeatureHandle::weak_ref>` | private | The subset of features that are topological lines. |
| `d_current_topological_boundary_features` | field | `std::vector<GPlatesModel::FeatureHandle::weak_ref>` | private | The subset of features that are topological boundaries. |
| `d_current_feature_collections` | field | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | All input feature collections. |
| `d_current_reconstruction_layer_proxy` | field | `LayerProxyUtils::InputLayerProxy<ReconstructionLayerProxy>` | private | Used to get reconstruction trees at desired reconstruction times. |
| `d_current_reconstructed_geometry_topological_sections_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get reconstructed static features that form the topological sections for our topological geometries. |
| `d_current_resolved_line_topological_sections_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyGeometryResolverLayerProxy>` | private | Used to get resolved topological lines that form the topological sections for our topological geometries. |
| `d_cached_resolved_boundary_time_span` | field | `ResolvedBoundaryTimeSpan` | private | The cached resolved boundary topologies over a range of reconstruction times. |
| `d_cached_resolved_boundaries` | field | `ResolvedBoundaries` | private | The cached resolved topological boundaries (polygons). |
| `d_cached_resolved_lines` | field | `ResolvedLines` | private | The cached resolved topological lines (polylines). |
| `d_resolved_boundary_dependent_topological_sections` | field | `DependentTopologicalSectionLayers` | private | The cached resolved \*boundaries\* depend on these topological sections. |
| `d_resolved_line_dependent_topological_sections` | field | `DependentTopologicalSectionLayers` | private | The cached resolved \*lines\* depend on these topological sections. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated (either resolved lines or boundaries). |
| `d_resolved_lines_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that our resolved \*lines\* have been updated. |
| `d_inside_get_subject_token_method` | field | `bool` | private | Used to prevent |
| `TopologyGeometryResolverLayerProxy()` | constructor | `None` | private | Default constructor. |
| `reset_cache( bool invalidate_resolved_boundaries = true, bool invalidate_resolved_lines = true)` | method | `void` | private | Resets any cached variables forcing them to be recalculated next time they're accessed. |
| `check_input_layer_proxies( bool check_resolved_line_topological_sections = true)` | method | `void` | private | Checks if any input layer proxies have changed. |
| `cache_resolved_topological_boundaries` | field | `std::vector<ResolvedTopologicalBoundary::non_null_ptr_type>` | private | Generates resolved topological boundaries for the specified reconstruction time if they're not already cached. |
| `cache_resolved_boundary_time_span( const TimeSpanUtils::TimeRange &time_range)` | method | `TopologyReconstruct::resolved_boundary_time_span_type::non_null_ptr_to_const_type` | private | Generates a resolved boundary time span for the specified time range if one is not already cached. |
| `create_resolved_topological_boundaries( std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, const double &reconstruction_time)` | method | `ReconstructHandle::type` | private | Creates resolved topological boundaries for the specified reconstruction time. |
| `create_resolved_topological_lines( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, const std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_line_features, const double &reconstruction_time)` | method | `ReconstructHandle::type` | private | Creates resolved topological lines for the specified reconstruction time. |
| `create_resolved_topological_boundary_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_boundary_velocities, const std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_ ...` | method | `ReconstructHandle::type` | private | Creates resolved topological boundary velocities for the specified reconstruction time. |
| `create_resolved_topological_line_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_line_velocities, const std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type, const ...` | method | `ReconstructHandle::type` | private | Creates resolved topological line velocities for the specified reconstruction time. |
| `create_resolved_topological_sub_segment_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_sub_segment_velocities, const sub_segment_seq_type &sub_segments, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type, const double &velocity_delta_time, const ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `find_topological_geometry_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_line_features, std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_boundary_features, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &feature_collections)` | function | `void` | Filter out features that are topological geometries (lines and boundaries). |
| `GPLATES_APP_LOGIC_TOPOLOGYGEOMETRYRESOLVERLAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/TopologyGeometryResolverLayerProxy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 21 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 18 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 13 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 4 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 3 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 3 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 2 |
| [app-logic/DependentTopologicalSectionLayers](DependentTopologicalSectionLayers.md) | app-logic | 2 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 2 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 2 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyGeometryResolverLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::TopologyGeometryResolverLayerProxy --body
python scripts/gpq.py uses TopologyGeometryResolverLayerProxy --kind class
python scripts/gpq.py hier TopologyGeometryResolverLayerProxy
```
