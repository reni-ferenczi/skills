# ResolvedSubSegmentRangeInSection

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 160 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedSubSegmentRangeInSection.h` | C++ | 642 |
| `src/app-logic/ResolvedSubSegmentRangeInSection.cc` | C++ | 853 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedSubSegmentRangeInSection tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/ResolvedSubSegmentRangeInSection tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
