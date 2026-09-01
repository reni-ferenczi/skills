# ResolvedTopologicalSubSegmentImpl

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 286 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalSubSegmentImpl.h` | C++ | 87 |
| `src/app-logic/ResolvedTopologicalSubSegmentImpl.cc` | C++ | 1060 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedTopologicalSubSegmentImpl tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_rubber_band_vertex_source_info_at_section_end_point( const ReconstructionGeometry::non_null_ptr_to_const_type &section_reconstruction_geometry, const GPlatesMaths::PointOnSphere &section_end_point, bool is_at_start_vertex)` | function | `ResolvedVertexSourceInfo::non_null_ptr_to_const_type` | Returns the vertex source info at either the start (if is\_at\_start\_vertex is true) or end of the section. |
| `get_rubber_band_vertex_source_info( const ResolvedSubSegmentRangeInSection::RubberBand &rubber_band)` | function | `ResolvedVertexSourceInfo::non_null_ptr_to_const_type` | Get the vertex source info corresponding to the specified rubber band between section and adjacent section. |
| `get_resolved_topological_line_intersection_vertex_source_info( const ResolvedSubSegmentRangeInSection::Intersection &intersection, GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type section_geometry, ResolvedTopologicalLine::non_null_ptr_to_const_type section_resolved_topological_line)` | function | `ResolvedVertexSourceInfo::non_null_ptr_to_const_type` | Finds the vertex source info corresponding to the specified intersection along the section polyline of a resolved topological line. |
| `get_resolved_topological_line_sub_segment_vertex_source_infos( resolved_vertex_source_info_seq_type &vertex_source_infos, const ResolvedSubSegmentRangeInSection &sub_segment_range, ResolvedTopologicalLine::non_null_ptr_to_const_type section_resolved_topological_line, bool include_rubber_band_points)` | function | `void` | Get vertex source infos for a \*ResolvedTopologicalLine\* sub-segment. |
| `get_reconstructed_feature_geometry_sub_segment_vertex_source_infos( resolved_vertex_source_info_seq_type &vertex_source_infos, const ResolvedSubSegmentRangeInSection &sub_segment_range, ReconstructedFeatureGeometry::non_null_ptr_to_const_type section_reconstructed_feature_geometry, bool include_rubber_band_points)` | function | `void` | Get vertex source infos for a \*ReconstructedFeatureGeometry\* sub-segment. |
| `create_sub_sub_segment_with_new_range( const ResolvedTopologicalGeometrySubSegment &sub_sub_segment, boost::optional<ResolvedSubSegmentRangeInSection::IntersectionOrRubberBand> start_of_sub_sub_segment, boost::optional<ResolvedSubSegmentRangeInSection::IntersectionOrRubberBand> end_of_sub_sub_segment)` | function | `ResolvedTopologicalGeometrySubSegment::non_null_ptr_type` | Returns a new sub-sub-segment matching sub\_sub\_segment except for differing range (of section). |
| `replace_intersected_sub_sub_segment( const sub_segment_seq_type &unclipped_sub_sub_segments, sub_segment_seq_type &clipped_sub_sub_segments, // Same size as 'unclipped_sub_sub_segments' const ResolvedSubSegmentRangeInSection &sub_segment_range, const ResolvedSubSegmentRangeInSection::Intersection &intersection, bool in ...` | function | `sub_segment_seq_type::size_type` | Find the first/last unclipped sub-sub-segment containing the specified intersection and replace it with a clipped version of that sub-sub-segment that contributes to the sub-segment (ie, clipped resolved line). |
| `replace_rubber_banded_sub_sub_segment( sub_segment_seq_type &sub_sub_segments, const ResolvedSubSegmentRangeInSection::RubberBand &sub_segment_rubber_band, bool rubber_band_is_at_start_of_sub_segment)` | function | `void` | The first (or last) sub-sub-segment essentially gets replaced by a rubber-band version of that sub-sub-segment. |
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALSUBSEGMENTIMPL_H` | macro | `None` | — |
| `get_sub_segment_vertex_source_infos( resolved_vertex_source_info_seq_type &vertex_source_infos, const ResolvedSubSegmentRangeInSection &sub_segment, ReconstructionGeometry::non_null_ptr_to_const_type section_reconstruction_geometry, bool include_rubber_band_points = true)` | function | `void` | Find the vertex source infos in the specified sub-segment range of the specified resolved topological section geometry. |
| `get_sub_sub_segments( boost::optional<sub_segment_seq_type> &sub_sub_segments, const ResolvedSubSegmentRangeInSection &sub_segment, ReconstructionGeometry::non_null_ptr_to_const_type section_reconstruction_geometry)` | function | `void` | Returns the sub-sub-segments that contribute to the specified sub\_segment of the specified reconstruction geometry. |

## Notes

[[[PROSE notes unit=app-logic/ResolvedTopologicalSubSegmentImpl tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTopologicalGeometrySubSegment](ResolvedTopologicalGeometrySubSegment.md) | app-logic | 6 |
| [app-logic/ResolvedTopologicalSharedSubSegment](ResolvedTopologicalSharedSubSegment.md) | app-logic | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalSubSegmentImpl.h
```
