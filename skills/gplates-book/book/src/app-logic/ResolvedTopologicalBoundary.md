# ResolvedTopologicalBoundary

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 605 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalBoundary.h` | C++ | 279 |
| `src/app-logic/ResolvedTopologicalBoundary.cc` | C++ | 59 |

## Overview

`ResolvedTopologicalBoundary` is the `ResolvedTopologicalGeometry` specialisation for a resolved topological *polygon* — a plate or other closed region built by stitching together the reconstructed geometries of its boundary sections. Beyond the plate ID, time-of-formation and reconstruction-tree bookkeeping it inherits from `ResolvedTopologicalGeometry`, it adds the resolved `GPlatesMaths::PolygonOnSphere` itself (`resolved_topology_boundary_ptr_type`) and the ordered sequence of `ResolvedTopologicalGeometrySubSegment` objects — one per contributing boundary section, each already reversed if the section's geometry ran the wrong way round for this boundary — whose vertices, concatenated, form the polygon.

`get_vertex_source_infos()` answers, per vertex of the resolved boundary, which source reconstructed feature geometry contributed it; because building that per-vertex mapping means walking every sub-segment, it is computed once by `calc_vertex_source_infos()` and cached in `d_vertex_source_infos` on first request rather than up front. The static `INCLUDE_SUB_SEGMENT_RUBBER_BAND_POINTS_IN_RESOLVED_BOUNDARY` constant is `false` because rubber-band points sit exactly halfway between adjacent sub-segments and so never move the boundary's shape — they matter only when a sub-segment is examined in isolation, to mark where it starts and ends.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTopologicalBoundary`](#gplatesapplogicresolvedtopologicalboundary) | class | [`ResolvedTopologicalGeometry`](ResolvedTopologicalGeometry.md) | — | 0 | A resolved topological \*polygon\*. |

## Members

### `GPlatesAppLogic::ResolvedTopologicalBoundary`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedTopologicalBoundary>` | public | A convenience typedef for a shared pointer to a non-const ResolvedTopologicalBoundary. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedTopologicalBoundary>` | public | A convenience typedef for a shared pointer to a non-const ResolvedTopologicalBoundary. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ResolvedTopologicalBoundary>` | public | A convenience typedef for boost::intrusive\_ptr\<ResolvedTopologicalBoundary\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ResolvedTopologicalBoundary>` | public | A convenience typedef for boost::intrusive\_ptr\<const ResolvedTopologicalBoundary\>. |
| `resolved_topology_boundary_ptr_type` | typedef | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for a resolved topological polygon geometry. |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator, const resolved_topology_boundary_ptr_type &resolved_topology_boundary_ptr, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator ...` | method | `non_null_ptr_type` | public | Create a resolved topological \*boundary\* with an optional plate ID and an optional time of formation. |
| `~ResolvedTopologicalBoundary()` | destructor | `None` | public | — |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | Get a non-null pointer to a const ResolvedTopologicalBoundary which points to this instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | Get a non-null pointer to a ResolvedTopologicalBoundary which points to this instance. |
| `resolved_topology_geometry()` | method | `resolved_topology_geometry_ptr_type` | public | Access the resolved topology polygon as a GeometryOnSphere. |
| `resolved_topology_boundary()` | method | `resolved_topology_boundary_ptr_type` | public | Returns the resolved topology polygon as a PolygonOnSphere. |
| `get_vertex_source_infos` | field | `resolved_vertex_source_info_seq_type` | public | Returns the per-vertex source reconstructed feature geometries. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `INCLUDE_SUB_SEGMENT_RUBBER_BAND_POINTS_IN_RESOLVED_BOUNDARY` | field | `bool` | public | Whether rubber band points of this resolved topological boundary's sub-segments contributed to its boundary geometry. |
| `d_resolved_topology_boundary_ptr` | field | `resolved_topology_boundary_ptr_type` | private | The resolved topology polygon. |
| `d_sub_segment_seq` | field | `sub_segment_seq_type` | private | The sequence of SubSegment objects that form the resolved topology boundary. |
| `d_vertex_source_infos` | field | `boost::optional<resolved_vertex_source_info_seq_type>` | private | Each point in the resolved topological line can potentially reference a different source reconstructed feature geometry. |
| `ResolvedTopologicalBoundary( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, resolved_topology_boundary_ptr_type resolved_topology_boundary_ptr, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator pr ...` | constructor | `None` | private | Instantiate a resolved topological boundary with an optional reconstruction plate ID and an optional time of formation. |
| `calc_vertex_source_infos()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALBOUNDARY_H` | macro | `None` | — |

## Notes

- `get_vertex_source_infos()` lazily populates `d_vertex_source_infos` (marked `mutable`) on first call and reuses it thereafter; the cache is never invalidated because a `ResolvedTopologicalBoundary` instance's underlying geometry never changes after construction.
- A sub-segment can itself be a resolved topological *line* (not just a `ReconstructedFeatureGeometry`), which `get_vertex_source_infos` accounts for via each sub-segment's own `get_reversed_sub_segment_point_source_infos`.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 7 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 5 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 3 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 3 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 2 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 2 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 1 |
| [app-logic/TopologyPointLocation](TopologyPointLocation.md) | app-logic | 1 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 1 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 1 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalBoundary.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTopologicalBoundary --body
python scripts/gpq.py uses ResolvedTopologicalBoundary --kind class
python scripts/gpq.py hier ResolvedTopologicalBoundary
```
