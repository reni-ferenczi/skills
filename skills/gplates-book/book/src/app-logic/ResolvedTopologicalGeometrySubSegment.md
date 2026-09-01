# ResolvedTopologicalGeometrySubSegment

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 479 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalGeometrySubSegment.h` | C++ | 316 |
| `src/app-logic/ResolvedTopologicalGeometrySubSegment.cc` | C++ | 140 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedTopologicalGeometrySubSegment tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTopologicalGeometrySubSegment`](#gplatesapplogicresolvedtopologicalgeometrysubsegment) | class | [`GPlatesUtils::ReferenceCount<ResolvedTopologicalGeometrySubSegment>`](../utils/ReferenceCount.md) | — | 0 | Records the reconstructed geometry, and any other relevant information, of a subsegment. |
| [`GPlatesAppLogic::sub_segment_seq_type`](#gplatesapplogicsub_segment_seq_type) | typedef | — | — | 0 | Typedef for a sequence of ResolvedTopologicalGeometrySubSegment objects. |

## Members

### `GPlatesAppLogic::ResolvedTopologicalGeometrySubSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedTopologicalGeometrySubSegment>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedTopologicalGeometrySubSegment>` | public | — |
| `create( const ResolvedSubSegmentRangeInSection &sub_segment, bool use_reverse, const GPlatesModel::FeatureHandle::weak_ref &segment_feature_ref, const ReconstructionGeometry::non_null_ptr_to_const_type &segment_reconstruction_geometry)` | method | `non_null_ptr_type` | public | Create a subsegment using specified subsegment range (in section) and reconstruction geometry that it came from. |
| `get_section_geometry()` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Returns the full (un-clipped) section geometry. |
| `get_num_points_in_section_geometry()` | method | `unsigned int` | public | Returns the number of points in get\_section\_geoemtry. |
| `get_use_reverse()` | method | `bool` | public | If true then the geometry returned by get\_sub\_segment\_geometry had its points reversed in order before contributing to the final resolved topological geometry. |
| `get_sub_segment_geometry()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | The subset of vertices of topological section used in resolved topology geometry. |
| `get_num_points_in_sub_segment( bool include_rubber_band_points = true)` | method | `unsigned int` | public | Return the number of points in the sub-segment geometry. |
| `get_sub_segment_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool include_rubber_band_points = true)` | method | `void` | public | Returns the (unreversed) sub-segment points. |
| `get_reversed_sub_segment_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool include_rubber_band_points = true)` | method | `void` | public | Returns the sub-segment points as they contribute to the resolved topology. |
| `get_sub_segment_point_source_infos( resolved_vertex_source_info_seq_type &point_source_infos, bool include_rubber_band_points = true)` | method | `void` | public | Returns the (unreversed) per-point source reconstructed feature geometries. |
| `get_reversed_sub_segment_point_source_infos( resolved_vertex_source_info_seq_type &point_source_infos, bool include_rubber_band_points = true)` | method | `void` | public | Same as get\_sub\_segment\_point\_source\_infos but reverses them if necessary such that they are in the same order as get\_reversed\_sub\_segment\_points. |
| `get_sub_sub_segments` | field | `boost::optional< std::vector<ResolvedTopologicalGeometrySubSegment::non_null_ptr_type> >` | public | Return any sub-segments of the resolved topological section that this sub-segment came from. |
| `d_sub_segment` | field | `ResolvedSubSegmentRangeInSection` | private | The sub-segment. |
| `d_use_reverse` | field | `bool` | private | Indicates if geometry (sub-segment) direction was reversed when assembling topology. |
| `d_segment_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | Reference to the source feature handle of the topological section. |
| `d_segment_reconstruction_geometry` | field | `ReconstructionGeometry::non_null_ptr_to_const_type` | private | The section reconstruction geometry. |
| `d_point_source_infos` | field | `boost::optional<resolved_vertex_source_info_seq_type>` | private | Each point in the subsegment geometry can potentially reference a different source reconstructed feature geometry. |
| `d_sub_sub_segments` | field | `boost::optional< std::vector<ResolvedTopologicalGeometrySubSegment::non_null_ptr_type> >` | private | Sub-segments of our ResolvedTopologicalLine topological section (if one) than contribute to this sub-segment. |
| `d_calculated_sub_sub_segments` | field | `bool` | private | — |
| `ResolvedTopologicalGeometrySubSegment( const ResolvedSubSegmentRangeInSection &sub_segment, bool use_reverse, const GPlatesModel::FeatureHandle::weak_ref &segment_feature_ref, const ReconstructionGeometry::non_null_ptr_to_const_type &segment_reconstruction_geometry)` | constructor | `None` | private | — |

### `GPlatesAppLogic::sub_segment_seq_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALGEOMETRYSUBSEGMENT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ResolvedTopologicalGeometrySubSegment tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTopologicalSubSegmentImpl](ResolvedTopologicalSubSegmentImpl.md) | app-logic | 30 |
| [app-logic/ResolvedTopologicalSharedSubSegment](ResolvedTopologicalSharedSubSegment.md) | app-logic | 20 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 9 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 9 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 9 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 8 |
| [app-logic/ResolvedTopologicalBoundary](ResolvedTopologicalBoundary.md) | app-logic | 7 |
| [app-logic/ResolvedTopologicalLine](ResolvedTopologicalLine.md) | app-logic | 7 |
| [app-logic/ResolvedTopologicalNetwork](ResolvedTopologicalNetwork.md) | app-logic | 6 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 6 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 5 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 5 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 5 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 4 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 4 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 3 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalGeometrySubSegment.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTopologicalGeometrySubSegment --body
python scripts/gpq.py uses ResolvedTopologicalGeometrySubSegment --kind class
python scripts/gpq.py hier ResolvedTopologicalGeometrySubSegment
```
