# ResolvedTopologicalSubSegmentImpl

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 286 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalSubSegmentImpl.h` | C++ | 87 |
| `src/app-logic/ResolvedTopologicalSubSegmentImpl.cc` | C++ | 1060 |

## Overview

`ResolvedTopologicalSubSegmentImpl` is the implementation namespace behind
`ResolvedTopologicalGeometrySubSegment` and `ResolvedTopologicalSharedSubSegment`:
both classes forward their point-source-info and sub-sub-segment queries here
rather than implementing the logic themselves, because the logic is identical
whichever "owning" class asked for it and is intricate enough to deserve its
own file. The header declares only the two entry points,
`get_sub_segment_vertex_source_infos()` and `get_sub_sub_segments()`; almost
all of the 1060-line `.cc` is private helper functions in the same namespace.

`get_sub_segment_vertex_source_infos()` fills in, per vertex of a (possibly
rubber-banded) sub-segment, which source reconstructed feature geometry that
vertex's velocity should be computed from — a single shared source if the
topological section is a `ReconstructedFeatureGeometry`, or one source per
vertex inherited from the section's own sub-segments if it is a
`ResolvedTopologicalLine`. Rubber-band vertices (inserted where a section
doesn't quite meet its neighbour) get an interpolated source blended between
the two adjacent sections, fixed to be evaluated *at* the section endpoint so
that velocities interpolate correctly rather than being sampled at the
rubber-band midpoint. `get_sub_sub_segments()` handles the companion problem
for a section that is a `ResolvedTopologicalLine`: it maps the (possibly
clipped, by intersection or rubber-banding) range of the outer sub-segment
back onto the line's own unclipped sub-segments, splitting or replacing the
first/last one where the outer sub-segment's boundary falls in the middle of
one of them.

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

`get_sub_segment_vertex_source_infos()` asserts (via `PreconditionViolationError`)
that the section reconstruction geometry passed in is either a
`ReconstructedFeatureGeometry` or a `ResolvedTopologicalLine` — no other
`ReconstructionGeometry` kind is valid as a topological section. The
sub-sub-segment splitting logic in the `.cc` file has several subtle
special cases (documented inline) around intersections and rubber bands
landing exactly on the first or last vertex of a resolved line; the
author's own comment on `replace_intersected_sub_sub_segment` calls it
"probably the most subtle point of this function" — read that function's
comments closely before changing the clipping behaviour.

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
