# ResolvedTopologicalLine

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 547 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalLine.h` | C++ | 277 |
| `src/app-logic/ResolvedTopologicalLine.cc` | C++ | 59 |

## Overview

`ResolvedTopologicalLine` is the `ResolvedTopologicalGeometry` subclass for
topological features whose resolved shape is an open polyline rather than a
closed boundary — it implements `resolved_topology_geometry()` by returning
its `resolved_topology_line_ptr_type` (a `PolylineOnSphere`). Like
`ResolvedTopologicalBoundary`, it is assembled from a sequence of
`ResolvedTopologicalGeometrySubSegment` objects, one per contributing
topological section, stored in `d_sub_segment_seq` and exposed via
`get_sub_segment_sequence()`.

Because a resolved topological line can itself act as a topological section
for another topology (see `ResolvedTopologicalGeometrySubSegment`), it also
exposes per-vertex provenance through `get_vertex_source_infos()`. This is
computed lazily by `calc_vertex_source_infos()`, which walks the sub-segment
sequence and asks each one for its reversed point-source infos, and the
result is cached in `d_vertex_source_infos`. `INCLUDE_SUB_SEGMENT_RUBBER_BAND_POINTS_IN_RESOLVED_LINE`
is `false` because rubber-band points (inserted where sections don't meet
exactly) don't change the line's shape at the join, only the shape of the
individual sub-segments they delineate.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTopologicalLine`](#gplatesapplogicresolvedtopologicalline) | class | [`ResolvedTopologicalGeometry`](ResolvedTopologicalGeometry.md) | — | 0 | A resolved topological \*polyline\*. |

## Members

### `GPlatesAppLogic::ResolvedTopologicalLine`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedTopologicalLine>` | public | A convenience typedef for a shared pointer to a non-const ResolvedTopologicalLine. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedTopologicalLine>` | public | A convenience typedef for a shared pointer to a non-const ResolvedTopologicalLine. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ResolvedTopologicalLine>` | public | A convenience typedef for boost::intrusive\_ptr\<ResolvedTopologicalLine\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ResolvedTopologicalLine>` | public | A convenience typedef for boost::intrusive\_ptr\<const ResolvedTopologicalLine\>. |
| `resolved_topology_line_ptr_type` | typedef | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for a resolved topological polyline geometry. |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator, const resolved_topology_line_ptr_type &resolved_topology_line_ptr, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator_, SubSe ...` | method | `non_null_ptr_type` | public | Create a resolved topological \*line\* with an optional plate ID and an optional time of formation. |
| `~ResolvedTopologicalLine()` | destructor | `None` | public | — |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | Get a non-null pointer to a const ResolvedTopologicalLine which points to this instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | Get a non-null pointer to a ResolvedTopologicalLine which points to this instance. |
| `resolved_topology_geometry()` | method | `resolved_topology_geometry_ptr_type` | public | Access the resolved topology polyline as a GeometryOnSphere. |
| `resolved_topology_line()` | method | `resolved_topology_line_ptr_type` | public | Returns the resolved topology polyline as a PolylineOnSphere. |
| `get_vertex_source_infos` | field | `resolved_vertex_source_info_seq_type` | public | Returns the per-vertex source reconstructed feature geometries. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `INCLUDE_SUB_SEGMENT_RUBBER_BAND_POINTS_IN_RESOLVED_LINE` | field | `bool` | public | Whether rubber band points of this resolved topological line's sub-segments contributed to its line geometry. |
| `d_resolved_topology_line_ptr` | field | `resolved_topology_line_ptr_type` | private | The resolved topology polyline. |
| `d_sub_segment_seq` | field | `sub_segment_seq_type` | private | The sequence of SubSegment objects that form the resolved topology line. |
| `d_vertex_source_infos` | field | `boost::optional<resolved_vertex_source_info_seq_type>` | private | Each point in the resolved topological line can potentially reference a different source reconstructed feature geometry. |
| `ResolvedTopologicalLine( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, resolved_topology_line_ptr_type resolved_topology_line_ptr, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_itera ...` | constructor | `None` | private | Instantiate a resolved topological line with an optional reconstruction plate ID and an optional time of formation. |
| `calc_vertex_source_infos()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALLINE_H` | macro | `None` | — |

## Notes

The constructor is a private template (taking a forward-iterator range of
sub-segments) and `create()` is the only way to build an instance, so a
`ResolvedTopologicalLine` is never constructed on the stack. `d_vertex_source_infos`
is `mutable` and populated on first call to `get_vertex_source_infos()`, not
at construction time.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTopologicalSubSegmentImpl](ResolvedTopologicalSubSegmentImpl.md) | app-logic | 13 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 4 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 4 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 3 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 2 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 2 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 2 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 1 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 1 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalLine.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTopologicalLine --body
python scripts/gpq.py uses ResolvedTopologicalLine --kind class
python scripts/gpq.py hier ResolvedTopologicalLine
```
