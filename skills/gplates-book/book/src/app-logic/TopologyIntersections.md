# TopologyIntersections

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 449 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyIntersections.h` | C++ | 386 |
| `src/app-logic/TopologyIntersections.cc` | C++ | 961 |

## Overview

[[[PROSE overview unit=app-logic/TopologyIntersections tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologicalIntersections`](#gplatesapplogictopologicalintersections) | class | `boost::enable_shared_from_this<TopologicalIntersections>` | — | 0 | Keeps track of a topological section's intersection results with its neighbouring sections to assist with determining the partitioned segment. |

## Members

### `GPlatesAppLogic::TopologicalIntersections`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<TopologicalIntersections>` | public | — |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const TopologicalIntersections>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<TopologicalIntersections>` | public | — |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const TopologicalIntersections>` | public | — |
| `create( const ReconstructionGeometry::non_null_ptr_to_const_type &section_reconstruction_geometry, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &section_geometry, bool reverse_hint)` | method | `shared_ptr_type` | public | We initialise with the full section geometry. |
| `set_reverse_hint( bool reverse_hint)` | method | `void` | public | Set the reverse hint (if it cannot be set in the constructor, or if it needs to be changed). |
| `get_section_reconstruction_geometry()` | method | `ReconstructionGeometry::non_null_ptr_to_const_type` | public | Returns the original reconstruction geometry that the section geometry came from. |
| `get_section_geometry()` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Returns the section geometry. |
| `intersect_with_previous_section( const shared_ptr_type &previous_section)` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | public | Intersects this section with the previous neighbouring topological section and returns intersection point if there was one. |
| `intersect_with_previous_section_allowing_two_intersections( const shared_ptr_type &previous_section)` | method | `boost::optional< boost::tuple< // First intersection GPlatesMaths::PointOnSphere, // Optional second intersection boost::optional<GPlatesMaths::PointOnSphere> > >` | public | Intersects this section with the previous neighbouring topological section and returns one or two intersection points if there were any. |
| `get_reverse_flag()` | method | `bool` | public | Returns the reverse flag for this section. |
| `get_sub_segment_range_in_section()` | method | `ResolvedSubSegmentRangeInSection` | public | Returns the sub-segment range (including optional start/end intersections) of the entire section geometry that will contribute to a resolved topological geometry. |
| `get_sub_segment_geometry()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | Delegate to equivalent method in ResolvedSubSegmentRangeInSection. |
| `get_sub_segment_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool include_rubber_band_points = true)` | method | `void` | public | Delegate to equivalent method in ResolvedSubSegmentRangeInSection. |
| `get_reversed_sub_segment_points( std::vector<GPlatesMaths::PointOnSphere> &geometry_points, bool include_rubber_band_points = true)` | method | `void` | public | Delegate to equivalent method in ResolvedSubSegmentRangeInSection. |
| `get_sub_segment_end_points( bool include_rubber_band_points = true)` | method | `std::pair<GPlatesMaths::PointOnSphere/*start point*/, GPlatesMaths::PointOnSphere/*end point*/>` | public | Delegate to equivalent method in ResolvedSubSegmentRangeInSection. |
| `get_reversed_sub_segment_end_points( bool include_rubber_band_points = true)` | method | `std::pair<GPlatesMaths::PointOnSphere/*start point*/, GPlatesMaths::PointOnSphere/*end point*/>` | public | Delegate to equivalent method in ResolvedSubSegmentRangeInSection. |
| `only_intersects_previous_section()` | method | `bool` | public | Returns true if this section only intersects the previous section. |
| `only_intersects_next_section()` | method | `bool` | public | Returns true if this section only intersects the next section. |
| `intersects_previous_and_next_sections()` | method | `bool` | public | Returns true if this section intersects both its adjacent sections. |
| `does_not_intersect_previous_or_next_section()` | method | `bool` | public | Returns true if this section does not intersect either of its adjacent sections. |
| `backward_compatible_segment_type` | typedef | `std::pair< boost::optional<ResolvedSubSegmentRangeInSection::Intersection>, boost::optional<ResolvedSubSegmentRangeInSection::Intersection> >` | private | Type to emulate \*segments\* used in prior implementations. |
| `d_section_reconstruction_geometry` | field | `ReconstructionGeometry::non_null_ptr_to_const_type` | private | The original reconstruction geometry that the section geometry came from. |
| `d_section_geometry` | field | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | private | The original section geometry before it was partitioned by intersections. |
| `d_reverse_hint` | field | `bool` | private | If this section intersects both its neighbouring sections then reverse\_hint will be ignored (and a reverse flag determined by intersection processing will be used). |
| `d_intersectable_section_polyline` | field | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | private | The section geometry as an intersectable polyline. |
| `d_prev_section` | field | `boost::optional<weak_ptr_type>` | private | The previous section that we were tested for intersection with. |
| `d_next_section` | field | `boost::optional<weak_ptr_type>` | private | The next section that we were tested for intersection with. |
| `d_prev_intersection` | field | `boost::optional<ResolvedSubSegmentRangeInSection::Intersection>` | private | Intersection with previous section, if any. |
| `d_next_intersection` | field | `boost::optional<ResolvedSubSegmentRangeInSection::Intersection>` | private | Intersection with next section, if any. |
| `TopologicalIntersections( const ReconstructionGeometry::non_null_ptr_to_const_type &section_reconstruction_geometry, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &section_geometry, bool reverse_hint)` | constructor | `None` | private | — |
| `backward_compatible_multiple_intersections_with_previous_section( const shared_ptr_type &previous_section, const GPlatesMaths::GeometryIntersect::Graph &intersection_graph)` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `backward_compatible_multiple_intersections_between_segments( const shared_ptr_type &previous_section, const GPlatesMaths::GeometryIntersect::Graph &intersection_graph, const backward_compatible_segment_type &previous_segment, const backward_compatible_segment_type &current_segment)` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `get_rubber_band( const boost::optional<weak_ptr_type> &adjacent_section, bool adjacent_is_previous_section)` | method | `boost::optional<ResolvedSubSegmentRangeInSection::RubberBand>` | private | — |
| `set_intersection_with_previous_section( const shared_ptr_type &previous_section, const GPlatesMaths::GeometryIntersect::Intersection &intersection, const ResolvedSubSegmentRangeInSection::Intersection &intersection_in_previous, const ResolvedSubSegmentRangeInSection::Intersection &intersection_in_current)` | method | `GPlatesMaths::PointOnSphere` | private | — |
| `set_intersection_with_previous_section( const shared_ptr_type &previous_section, const GPlatesMaths::GeometryIntersect::Intersection &intersection)` | method | `GPlatesMaths::PointOnSphere` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_intersectable_section_polyline( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &section_geometry)` | function | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | Returns the section geometry as an intersectable polyline. |
| `GPLATES_APP_LOGIC_TOPOLOGYINTERSECTIONS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/TopologyIntersections tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 21 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 11 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 8 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyIntersections.h
python scripts/gpq.py def GPlatesAppLogic::TopologicalIntersections --body
python scripts/gpq.py uses TopologicalIntersections --kind class
python scripts/gpq.py hier TopologicalIntersections
```
