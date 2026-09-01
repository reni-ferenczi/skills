# ResolvedSubSegmentRangeInSection

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 160 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedSubSegmentRangeInSection.h` | C++ | 642 |
| `src/app-logic/ResolvedSubSegmentRangeInSection.cc` | C++ | 853 |

## Overview

When a topological boundary or line is resolved, each of its sections is clipped against its two neighbours, and only the surviving middle piece contributes to the resolved geometry. This class *is* that piece — but it deliberately records it as a **range of vertex indices into the original section geometry**, plus at most one boundary condition at each end, rather than as a bare polyline. The reason is stated in the class comment and is the whole point of the design: quantities attached to section vertices — per-vertex plate IDs, velocities, scalar coverage values — must be carried through to the resolved topology, and that is only possible if you still know which of the section's vertices you kept. `ResolvedTopologicalGeometrySubSegment` and `ResolvedTopologicalSharedSubSegment` each hold one by value; `ResolvedTopologicalSubSegmentImpl` and `TopologyIntersections` are the code that builds them.

Each end of the range is either an `Intersection`, a `RubberBand`, or nothing (meaning the sub-segment runs to that end of the section). `Intersection` is a position expressed relative to the section's own great-circle-arc segments — a `segment_index`, an `on_segment_start` flag and an `AngularDistance` along the segment — which is what lets `get_interpolate_ratio_in_segment()` later blend per-vertex quantities across the segment that was cut. It is created either from a `GPlatesMaths::GeometryIntersect::Intersection` (picking geometry 1 or 2 according to which one was the section) or synthetically at a section endpoint. `RubberBand` is the *absence* of an intersection: when two adjacent sections do not meet, the resolved geometry is bridged by a point normally halfway between them, and the `RubberBand` keeps both contributing positions, an interpolate ratio, and both `ReconstructionGeometry` objects, so quantities can be blended across the gap in the same way. `IntersectionOrRubberBand` is a `boost::variant` enforcing that a given end is one or the other, never both.

The constructor is where the real work happens: it turns the two optional end conditions into `[d_start_section_vertex_index, d_end_section_vertex_index)`, a half-open range used exactly like begin/end iterators. Point/multi-point sections are supported as well as polylines (a multi-point is treated as if its points were joined by arcs, which matters when a resolved *line* section is later split into sub-sub-segments), and a polygon section is rejected — callers pass the exterior ring as a polyline instead. The class also carries a set of degenerate-case repairs so that `get_geometry()` can always produce a valid `PolylineOnSphere`: a T-junction intersection sitting exactly on the first or last section vertex, and a single-point section with no neighbours yet (the topology build tool's first click), both get a synthetic second `Intersection` manufactured at the section endpoint.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedSubSegmentRangeInSection`](#gplatesapplogicresolvedsubsegmentrangeinsection) | class | — | — | 0 | The sub-segment range of an entire topological section geometry that contributes to a resolved topological geometry. |

## Members

### `GPlatesAppLogic::ResolvedSubSegmentRangeInSection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Intersection` | class | `None` | public | Location of intersection within a specific section (eg, current or previous sections). |
| `RubberBand` | class | `None` | public | Location and information of rubber banding with an adjacent section. |
| `IntersectionOrRubberBand` | class | `None` | public | Can have an Intersection or a RubberBand (but not both) at start or end of a section. |
| `ResolvedSubSegmentRangeInSection( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type section_geometry, boost::optional<IntersectionOrRubberBand> start_intersection_or_rubber_band = boost::none, boost::optional<IntersectionOrRubberBand> end_intersection_or_rubber_band = boost::none)` | constructor | `None` | public | If no start intersection or rubber band then sub-segment starts at beginning of section. |
| `get_section_geometry()` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Returns the section geometry. |
| `get_num_points_in_section_geometry()` | method | `unsigned int` | public | Returns the number of points in get\_section\_geoemtry. |
| `get_geometry()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | Return the (unreversed) sub-segment geometry. |
| `get_geometry_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool include_rubber_band_points = true)` | method | `void` | public | Returns the (unreversed) geometry points. |
| `get_reversed_geometry_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool use_reverse, bool include_rubber_band_points = true)` | method | `void` | public | Returns the geometry points as they contribute to the resolved topology. |
| `get_end_points( bool include_rubber_band_points = true)` | method | `std::pair<GPlatesMaths::PointOnSphere/*start point*/, GPlatesMaths::PointOnSphere/*end point*/>` | public | Return the start and end points of the sub-segment range in the section. |
| `get_reversed_end_points( bool use_reverse, bool include_rubber_band_points = true)` | method | `std::pair<GPlatesMaths::PointOnSphere/*start point*/, GPlatesMaths::PointOnSphere/*end point*/>` | public | Return the start and end points of sub-segment range in section as contributed to resolved topology. |
| `get_num_points( bool include_rubber_band_points = true)` | method | `unsigned int` | public | Return the number of points in the sub-segment (including optional intersection or rubber band points). |
| `get_start_section_vertex_index()` | method | `unsigned int` | public | Index of first vertex of section geometry that contributes to sub-segment. |
| `get_end_section_vertex_index()` | method | `unsigned int` | public | Index of \*one-past-the-last\* vertex of section geometry that contributes to sub-segment. |
| `get_start_intersection_or_rubber_band()` | method | `boost::optional<IntersectionOrRubberBand>` | public | Optional intersection or rubber band signifying start of sub-segment. |
| `get_end_intersection_or_rubber_band()` | method | `boost::optional<IntersectionOrRubberBand>` | public | Optional intersection or rubber band signifying end of sub-segment. |
| `d_section_geometry` | field | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_num_points_in_section_geometry` | field | `unsigned int` | private | — |
| `d_start_section_vertex_index` | field | `unsigned int` | private | — |
| `d_end_section_vertex_index` | field | `unsigned int` | private | — |
| `d_start_intersection` | field | `boost::optional<Intersection>` | private | — |
| `d_end_intersection` | field | `boost::optional<Intersection>` | private | — |
| `d_start_rubber_band` | field | `boost::optional<RubberBand>` | private | — |
| `d_end_rubber_band` | field | `boost::optional<RubberBand>` | private | — |
| `d_sub_segment_geometry` | field | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | private | Cache our calculation of the sub-segment geometry (when it's requested). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDSUBSEGMENTRANGEINSECTION_H` | macro | `None` | — |

## Notes

**Invariant the whole class rests on: with rubber band points included there are always at least two points.** `get_geometry()` asserts it. Every odd branch in the constructor exists to preserve it, so if you add a construction path, check it against that assertion.

**The `segment_index` may be one past the last real segment.** This is the documented representation of "intersection at the final vertex", and `Intersection::get_segment()` returns `boost::none` for it. Never index the section geometry with a `segment_index` without handling that case, and do not "fix" it by decrementing — `get_interpolate_ratio_in_segment()` explicitly declines to do so because the index is also what drives the vertex-range arithmetic.

**Asymmetry between the start and end intersection.** `GeometryIntersect` never records an intersection on a segment's *end* point (it records it as the *start* of the next segment). So a start intersection can never displace a section vertex, but an end intersection with `on_segment_start` set does — hence the extra `--d_end_section_vertex_index` in the constructor, guarded so the range cannot go inverted when both intersections land on the same segment start.

**Both rubber bands can be on the same side.** Normally the start rubber band is at the start and the end one at the end, and the whole section is included. But when a resolved-line sub-segment is split into sub-sub-segments, both can end up at the same end, in which case *no* section vertices contribute (`d_start_section_vertex_index == d_end_section_vertex_index == d_num_points_in_section_geometry`). This is the one case where `get_geometry_points(..., include_rubber_band_points=false)` returns nothing at all and `get_num_points(false)` returns zero, and where `get_end_points(false)` quietly falls back to the section's own end points rather than the sub-segment's.

**Preconditions throw, they do not return an error.** A polygon `section_geometry`, or a start intersection ordered after the end intersection, raises `GPlatesGlobal::PreconditionViolationError`. The ordering check uses an epsilon comparison of `angle_in_segment` and is therefore slightly more permissive than `Intersection::operator<`, which does not.

**Two lazy caches, both `mutable`, neither synchronised**: the sub-segment `PolylineOnSphere` on the range object and the interpolate ratio on each `Intersection`. The latter is deferred because it costs two `acos()` calls and a division. Treat instances as single-threaded even through a `const` reference. Note that `Intersection` is copied by value into and out of the range, so a cached ratio computed on one copy does not benefit the others.

**`RubberBand` keeps counted references to two `ReconstructionGeometry` objects**, so a sub-segment range keeps the reconstruction geometries of its neighbouring sections alive for as long as it lives. `RubberBand::create()` also has an antipodal fallback: if the two section positions are exactly opposite, the midpoint is degenerate and an arbitrary perpendicular point is used instead.

**`get_geometry_points()` and `get_reversed_geometry_points()` append; they do not clear** the vector they are given.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTopologicalSubSegmentImpl](ResolvedTopologicalSubSegmentImpl.md) | app-logic | 175 |
| [app-logic/TopologyIntersections](TopologyIntersections.md) | app-logic | 153 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 149 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 18 |
| [app-logic/ResolvedTopologicalGeometrySubSegment](ResolvedTopologicalGeometrySubSegment.md) | app-logic | 9 |
| [app-logic/ResolvedTopologicalSharedSubSegment](ResolvedTopologicalSharedSubSegment.md) | app-logic | 8 |
| [maths/PolygonOnSphere](../maths/PolygonOnSphere.md) | maths | 4 |
| [app-logic/ScalarCoverageTimeSpan](ScalarCoverageTimeSpan.md) | app-logic | 2 |
| [maths/PolylineOnSphere](../maths/PolylineOnSphere.md) | maths | 2 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 1 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 1 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedSubSegmentRangeInSection.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedSubSegmentRangeInSection --body
python scripts/gpq.py uses ResolvedSubSegmentRangeInSection --kind class
python scripts/gpq.py hier ResolvedSubSegmentRangeInSection
```
