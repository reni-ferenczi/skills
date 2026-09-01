# TopologyNetworkResolver

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 576 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyNetworkResolver.h` | C++ | 375 |
| `src/app-logic/TopologyNetworkResolver.cc` | C++ | 973 |

## Overview

Resolves topological network features at a specific reconstruction time by visiting feature properties and constructing `ResolvedTopologicalNetwork` objects. The resolver implements the visitor pattern over a feature model, extracting topological boundary sections and interior geometries from `GpmlTopologicalNetwork` property values and assembling them into resolved networks with processed intersections.

Each resolved network requires boundary sections; networks without them are discarded. The resolver handles both ordinary topological networks and rift-specific variants, which carry left and right plate IDs and additional strain rate parameters. The resolver respects feature existence at the reconstruction time, filtering out features that do not span the requested time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyNetworkResolver`](#gplatesapplogictopologynetworkresolver) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md)<br>`boost::noncopyable` | — | 0 | Finds all topological network features (in the features visited) that exist at a particular reconstruction time and creates ResolvedTopologicalNetwork objects for each one. |

## Members

### `GPlatesAppLogic::TopologyNetworkResolver`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopologyNetworkResolver( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const double &reconstruction_time, ReconstructHandle::type reconstruct_handle, boost::optional<const std::vector<ReconstructHandle::type> &> topological_geometry_reconstruct_handles, const TopologyNetwork ...` | constructor | `None` | public | The resolved networks are appended to resolved\_topological\_networks. identifies the subset, of all RFGs observing the topological boundary section and/or interior features, and all resolved topological lines (ResolvedTopologicalLine) ... |
| `~TopologyNetworkResolver()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `finalise_post_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_time_window( GPlatesPropertyValues::GpmlTimeWindow &gpml_time_window)` | method | `void` | public | — |
| `visit_gpml_topological_network( GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | public | — |
| `visit_gpml_topological_line_section( GPlatesPropertyValues::GpmlTopologicalLineSection &gpml_topological_line_section)` | method | `void` | public | — |
| `visit_gpml_topological_point( GPlatesPropertyValues::GpmlTopologicalPoint &gpml_topological_point)` | method | `void` | public | — |
| `visit_gpml_plate_id( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | public | — |
| `visit_xs_double( GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | public | — |
| `ResolvedNetwork` | class | `None` | private | Stores/builds information from iterating over GpmlTopologicalSection objects. |
| `RiftProperties` | struct | `None` | private | Feature properties if this network is a rift. |
| `d_resolved_topological_networks` | field | `std::vector<ResolvedTopologicalNetwork::non_null_ptr_type>` | private | The resolved topological networks we're generating. |
| `d_reconstruction_time` | field | `double` | private | The time at which topologies are being resolved. |
| `d_reconstruct_handle` | field | `ReconstructHandle::type` | private | The reconstruction identifier placed in all resolved topological networks. |
| `d_topological_geometry_reconstruct_handles` | field | `boost::optional<std::vector<ReconstructHandle::type> >` | private | The reconstructed topological boundary sections and/or interior geometries we're using to assemble our network. |
| `d_topology_network_params` | field | `TopologyNetworkParams` | private | Parameters, including whether to smooth the deformation strain rate calculation results across the triangulation. |
| `d_currently_visited_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The current feature being visited. |
| `d_current_reconstruction_params` | field | `ReconstructionFeatureProperties` | private | Gathers some useful reconstruction parameters. |
| `d_current_rift_params` | field | `RiftProperties` | private | Parameters if this network is a rift. |
| `d_current_resolved_network` | field | `ResolvedNetwork` | private | Used to help build the resolved network of the current topological polygon. |
| `find_topological_reconstruction_geometry( const GPlatesPropertyValues::GpmlPropertyDelegate &geometry_delegate)` | method | `boost::optional<ReconstructionGeometry::non_null_ptr_type>` | private | — |
| `is_deprecated_seed_geometry( const ReconstructionGeometry::non_null_ptr_type &reconstruction_geometry)` | method | `bool` | private | — |
| `record_topological_interior_geometries( GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | private | — |
| `record_topological_interior_geometry( const GPlatesPropertyValues::GpmlPropertyDelegate &gpml_topological_interior)` | method | `void` | private | — |
| `record_topological_interior_reconstructed_geometry( const GPlatesModel::FeatureId &interior_source_feature_id, const ReconstructionGeometry::non_null_ptr_type &interior_source_rg)` | method | `boost::optional<ResolvedNetwork::InteriorGeometry>` | private | — |
| `record_topological_boundary_sections( GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | private | — |
| `record_topological_boundary_section_reconstructed_geometry( const GPlatesModel::FeatureId &boundary_section_source_feature_id, const ReconstructionGeometry::non_null_ptr_type &boundary_section_source_rg, bool reverse_hint)` | method | `boost::optional<ResolvedNetwork::BoundarySection>` | private | — |
| `process_topological_boundary_section_intersections()` | method | `void` | private | — |
| `process_topological_section_intersection_boundary( const std::size_t current_section_index, const bool two_sections = false)` | method | `void` | private | — |
| `create_resolved_topology_network()` | method | `void` | private | Create a ResolvedTopologicalNetwork from information gathered from the most recently visited topological polygon (stored in d\_resolved\_network) and add it to the Reconstruction. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGY_NETWORK_RESOLVER_H` | macro | `None` | — |

## Notes

Features are only processed if they are defined at the reconstruction time; older or not-yet-born features are skipped. A valid resolved network requires at least one boundary section—interior geometries are optional—and networks without boundary sections are silently discarded.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyNetworkResolver.h
python scripts/gpq.py def GPlatesAppLogic::TopologyNetworkResolver --body
python scripts/gpq.py uses TopologyNetworkResolver --kind class
python scripts/gpq.py hier TopologyNetworkResolver
```
