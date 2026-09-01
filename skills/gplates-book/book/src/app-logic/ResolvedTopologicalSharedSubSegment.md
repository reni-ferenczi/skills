# ResolvedTopologicalSharedSubSegment

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 634 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalSharedSubSegment.h` | C++ | 341 |
| `src/app-logic/ResolvedTopologicalSharedSubSegment.cc` | C++ | 141 |

## Overview

`ResolvedTopologicalSharedSubSegment` is the inverse view of
`ResolvedTopologicalGeometrySubSegment`: instead of belonging to one resolved
topology, it belongs to a topological section and records every resolved
topology (`ResolvedTopologicalBoundary` or `ResolvedTopologicalNetwork`) that
reuses that section's sub-segment as part of its boundary. This matters
because adjacent plate boundaries and deforming network edges are typically
described by the same topological section feature, shared and possibly
reversed by each side; the nested `ResolvedTopologyInfo` struct pairs each
sharing topology with the reversal flag that applies to it specifically —
typically two entries, one if a boundary has no neighbour, and more than two
signalling overlapping topologies.

Per the header comment, it is kept as a separate class from
`ResolvedTopologicalGeometrySubSegment` rather than merged into it "partly in
order to avoid memory islands (cyclic references of shared pointers)": a
resolved topology owns its `ResolvedTopologicalGeometrySubSegment`s, but a
`ResolvedTopologicalSharedSubSegment` is not owned by the topologies it
references, so storing back-references to them here would create a reference
cycle if the class were the same one the topology owns. Otherwise it
duplicates the un-clipped/clipped geometry accessors, per-point source-info
caching, and recursive sub-sub-segment lookup of its sibling class.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTopologicalSharedSubSegment`](#gplatesapplogicresolvedtopologicalsharedsubsegment) | class | [`GPlatesUtils::ReferenceCount<ResolvedTopologicalSharedSubSegment>`](../utils/ReferenceCount.md) | — | 0 | Associates a sub-segment (of a resolved topological section) with those resolved topologies (ResolvedTopologicalBoundary and ResolvedTopologicalNetwork) that share it as part of their boundary. |
| [`GPlatesAppLogic::shared_sub_segment_seq_type`](#gplatesapplogicshared_sub_segment_seq_type) | typedef | — | — | 0 | Typedef for a sequence of ResolvedTopologicalSharedSubSegment objects. |

## Members

### `GPlatesAppLogic::ResolvedTopologicalSharedSubSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedTopologicalSharedSubSegment>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedTopologicalSharedSubSegment>` | public | — |
| `ResolvedTopologyInfo` | struct | `None` | public | A resolved topology's relationship to the shared sub-segment. |
| `create( const ResolvedSubSegmentRangeInSection &shared_sub_segment, const std::vector<ResolvedTopologyInfo> &sharing_resolved_topologies, const GPlatesModel::FeatureHandle::const_weak_ref &shared_segment_feature_ref, const ReconstructionGeometry::non_null_ptr_to_const_type &shared_segment_reconstruction_geometry)` | method | `non_null_ptr_type` | public | — |
| `get_section_geometry()` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Returns the full (un-clipped) section geometry. |
| `get_shared_sub_segment_geometry()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | The subset of vertices of topological section used in the sharing resolved topologies. |
| `get_shared_sub_segment_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool include_rubber_band_points = true)` | method | `void` | public | Returns the (unreversed) shared sub-segment points. |
| `get_reversed_shared_sub_segment_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool use_reverse, bool include_rubber_band_points = true)` | method | `void` | public | Returns the shared sub-segment points as they contribute to a specific sharing resolved topology. |
| `get_shared_sub_segment_point_source_infos( resolved_vertex_source_info_seq_type &point_source_infos, bool include_rubber_band_points = true)` | method | `void` | public | Returns the (unreversed) shared per-point source reconstructed feature geometries. |
| `get_reversed_shared_sub_segment_point_source_infos( resolved_vertex_source_info_seq_type &point_source_infos, bool use_reverse, bool include_rubber_band_points = true)` | method | `void` | public | Same as get\_shared\_sub\_segment\_point\_source\_infos but reverses them if necessary such that they are in the same order as get\_reversed\_shared\_sub\_segment\_points. |
| `get_sub_sub_segments` | field | `boost::optional<sub_segment_seq_type>` | public | Return any sub-segments of the resolved topological section that this sub-segment came from. |
| `d_shared_sub_segment` | field | `ResolvedSubSegmentRangeInSection` | private | The shared sub-segment. |
| `d_sharing_resolved_topologies` | field | `std::vector<ResolvedTopologyInfo>` | private | The resolved topologies that share this sub-segment. |
| `d_shared_segment_feature_ref` | field | `GPlatesModel::FeatureHandle::const_weak_ref` | private | Reference to the source feature handle of the topological section. |
| `d_shared_segment_reconstruction_geometry` | field | `ReconstructionGeometry::non_null_ptr_to_const_type` | private | The shared segment reconstruction geometry. |
| `d_point_source_infos` | field | `boost::optional<resolved_vertex_source_info_seq_type>` | private | Each point in the shared subsegment geometry can potentially reference a different source reconstructed feature geometry. |
| `d_sub_sub_segments` | field | `boost::optional< std::vector<ResolvedTopologicalGeometrySubSegment::non_null_ptr_type> >` | private | Sub-segments of our ResolvedTopologicalLine topological section (if one) than contribute to this shared sub-segment. |
| `d_calculated_sub_sub_segments` | field | `bool` | private | — |
| `ResolvedTopologicalSharedSubSegment( const ResolvedSubSegmentRangeInSection &shared_sub_segment, const std::vector<ResolvedTopologyInfo> &sharing_resolved_topologies, const GPlatesModel::FeatureHandle::const_weak_ref &shared_segment_feature_ref, const ReconstructionGeometry::non_null_ptr_to_const_type &shared_segment_r ...` | constructor | `None` | private | — |

### `GPlatesAppLogic::shared_sub_segment_seq_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALSHAREDSUBSEGMENT_H` | macro | `None` | — |

## Notes

Unlike `ResolvedTopologicalGeometrySubSegment`, there is no single "use
reverse" flag on the object itself: reversal is per sharing topology, so
callers must pass the `use_reverse` from the relevant `ResolvedTopologyInfo`
into `get_reversed_shared_sub_segment_points()` /
`get_reversed_shared_sub_segment_point_source_infos()` rather than relying on
a fixed direction. `get_shared_sub_segment_point_source_infos()` throws
`PreconditionViolationError` if the reconstruction geometry passed to
`create()` is neither a `ReconstructedFeatureGeometry` nor a
`ResolvedTopologicalLine`. `d_point_source_infos` and `d_sub_sub_segments`
are `mutable` and computed lazily on first access.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 34 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 7 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 4 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 4 |
| [app-logic/ResolvedTopologicalSection](ResolvedTopologicalSection.md) | app-logic | 3 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalSharedSubSegment.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTopologicalSharedSubSegment --body
python scripts/gpq.py uses ResolvedTopologicalSharedSubSegment --kind class
python scripts/gpq.py hier ResolvedTopologicalSharedSubSegment
```
