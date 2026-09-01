# GreatCircleArc

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 526 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GreatCircleArc.h` | C++ | 724 |
| `src/maths/GreatCircleArc.cc` | C++ | 1302 |

## Overview

[[[PROSE overview unit=maths/GreatCircleArc tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::(anonymous)::GreatCircleArcFeature`](#gplatesmathsanonymousgreatcirclearcfeature) | enum | — | — | 0 | Feature type of GreatCircleArc. |
| [`GPlatesMaths::GreatCircleArc`](#gplatesmathsgreatcirclearc) | class | — | — | 0 | A great-circle arc on the surface of a sphere. |
| [`GPlatesMaths::ArcHasIndeterminateRotationAxis`](#gplatesmathsarchasindeterminaterotationaxis) | struct | — | — | 0 | This class instantiates to a function object which determines whether a GreatCircleArc has an indeterminate rotation axis. |

## Members

### `GPlatesMaths::(anonymous)::GreatCircleArcFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GCA_START_POINT` | enumerator | `None` | — | Feature type of GreatCircleArc. |
| `GCA_END_POINT` | enumerator | `None` | — | Feature type of GreatCircleArc. |
| `GCA_ARC` | enumerator | `None` | — | Feature type of GreatCircleArc. |

### `GPlatesMaths::GreatCircleArc`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConstructionParameterValidity` | enum | `None` | public | — |
| `evaluate_construction_parameter_validity( const PointOnSphere &p1, const PointOnSphere &p2)` | method | `ConstructionParameterValidity` | public | Test in advance whether the supplied great circle arc creation parameters would be valid or not. |
| `create( const PointOnSphere &p1, const PointOnSphere &p2, bool check_validity = true)` | method | `GreatCircleArc` | public | Make a great circle arc beginning at p1 and ending at p2. |
| `create_rotated_arc( const FiniteRotation &rot, const GreatCircleArc &arc)` | method | `GreatCircleArc` | public | Create a rotated version of arc. |
| `create_antipodal_arc( const GreatCircleArc &arc)` | method | `GreatCircleArc` | public | Create the antipodal great circle arc of arc. |
| `arc_length` | field | `real_t` | public | Returns the arc length (in radians). |
| `is_zero_length()` | method | `bool` | public | Return whether this great-circle arc is of zero length. |
| `rotation_axis` | field | `UnitVector3D` | public | Return the rotation axis of the arc. |
| `point_on_arc( const real_t &normalised_distance_from_start_point)` | method | `PointOnSphere` | public | Returns a point on this arc at a specified distance from the arc start point. and between zero and one are points along the arc. |
| `direction_on_arc( const real_t &normalised_distance_from_start_point)` | method | `Vector3D` | public | Returns the direction along this arc at a specified distance from the arc start point. and between zero and one are points along the arc. |
| `is_close_to( const PointOnSphere &test_point, const AngularExtent &closeness_angular_extent_threshold, real_t &closeness)` | method | `boost::optional<PointOnSphere>` | public | Evaluate whether test\_point is "close" to this arc. |
| `get_closest_point( const PointOnSphere &test_point)` | method | `PointOnSphere` | public | Finds the closest point on this arc to test\_point. |
| `operator==( const GreatCircleArc &other)` | operator | `bool` | public | — |
| `operator!=( const GreatCircleArc &other)` | operator | `bool` | public | — |
| `GreatCircleArc( const PointOnSphere &p1, const PointOnSphere &p2, const real_t &dot_p1_p2)` | constructor | `None` | protected | Construct a great-circle arc instance. |
| `CachedOnDemand` | class | `None` | private | Purpose of this structure is two-fold: 1) To delay calculating some quantities until they are requested. |
| `d_start_point` | field | `PointOnSphere` | private | — |
| `d_end_point` | field | `PointOnSphere` | private | — |
| `d_dot_of_endpoints` | field | `real_t` | private | — |
| `d_cached_on_demand` | field | `CachedOnDemand` | private | Information that is only calculated when needed. |
| `evaluate_construction_parameter_validity( const UnitVector3D &p1, const UnitVector3D &p2, const real_t &dot_p1_p2)` | method | `ConstructionParameterValidity` | private | — |
| `get_zero_length_threshold_cosine()` | method | `real_t` | public | This is an estimate of the threshold of the dot product of an arc's start and end points that distinguishes between non-zero length and zero length. |

### `GPlatesMaths::ArcHasIndeterminateRotationAxis`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ArcHasIndeterminateRotationAxis()` | constructor | `None` | public | — |
| `operator()( const GreatCircleArc &arc)` | operator | `bool` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `calculate_closest_position_on_great_circle( const UnitVector3D &test_point, const UnitVector3D &great_circle_rotation_axis, const real_t &test_point_dot_rotation_axis)` | function | `UnitVector3D` | — |
| `calculate_closest_position_on_great_circle( const UnitVector3D &test_point, const UnitVector3D &rotation_axis)` | function | `UnitVector3D` | — |
| `calculate_closest_feature( const GreatCircleArc &great_circle_arc, const PointOnSphere &test_point, boost::optional<PointOnSphere> &closest_point_on_great_circle_arc, real_t &closeness)` | function | `GreatCircleArcFeature` | Returns feature of great\_circle\_arc that is closest to test\_point. |
| `minimum_distance_for_position_inside_arc_lune( const UnitVector3D &position_vector, const UnitVector3D &arc_plane_normal, boost::optional<UnitVector3D &> closest_position_on_great_circle_arc, boost::optional<const AngularExtent &> minimum_distance_threshold)` | function | `AngularDistance` | Returns the minimum distance of a position to a great circle arc, where the position is inside the lune of the (non-zero length) great circle arc. |
| `minimum_distance_for_position_outside_arc_lune( const UnitVector3D &position_vector, const UnitVector3D &arc_start_position, const UnitVector3D &arc_end_position, boost::optional<UnitVector3D &> closest_position_on_great_circle_arc, boost::optional<const AngularExtent &> minimum_distance_threshold)` | function | `AngularDistance` | Returns the minimum distance of a position to a great circle arc, where the position is outside the lune of the (non-zero length) great circle arc. |
| `operator==( const GreatCircleArc &other)` | operator | `bool` | — |
| `GPLATES_MATHS_GREATCIRCLEARC_H` | macro | `None` | — |
| `tessellate( std::vector<PointOnSphere> &tessellation_points, const GreatCircleArc &great_circle_arc, const real_t &max_segment_angular_extent)` | function | `void` | Uniformly subdivides a great circle arc into smaller great circle arcs and appends the sequence of subdivided points to tessellation\_points. |
| `arcs_are_near_each_other( const GreatCircleArc &arc1, const GreatCircleArc &arc2)` | function | `bool` | Determine whether the two great-circle arcs arc1 and arc2 are "near" each other. |
| `intersect( const GreatCircleArc &arc1, const GreatCircleArc &arc2, boost::optional<UnitVector3D &> intersection = boost::none)` | function | `bool` | Determine whether the two great-circle arcs arc1 and arc2 intersect each other. |
| `minimum_distance( const GreatCircleArc &arc1, const GreatCircleArc &arc2, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*closest point on arc1*/, UnitVector3D &/*closest point on arc2*/> > closest_positions_on_arcs = boost::none)` | function | `AngularDistance` | Returns the minimum angular distance between two great circle arcs. |
| `minimum_distance( const UnitVector3D &position_vector, const GreatCircleArc &arc, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Returns the minimum angular distance between a unit vector and a great circle arc, and optionally the closest point on the arc - optionally within a minimum threshold distance. |
| `minimum_distance( const GreatCircleArc &arc, const UnitVector3D &position_vector, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Overload of minimum\_distance between a point and a great circle arc. |
| `minimum_distance( const PointOnSphere &point, const GreatCircleArc &arc, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Overload of minimum\_distance between a point and a great circle arc. |
| `minimum_distance( const GreatCircleArc &arc, const PointOnSphere &point, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Overload of minimum\_distance between a point and a great circle arc. |
| `maximum_distance( const GreatCircleArc &arc1, const GreatCircleArc &arc2, boost::optional<const AngularExtent &> maximum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*furthest point on arc1*/, UnitVector3D &/*furthest point on arc2*/> > furthest_positions_on_arcs = boost::none)` | function | `AngularDistance` | Returns the maximum angular distance between two great circle arcs. |
| `maximum_distance( const UnitVector3D &position_vector, const GreatCircleArc &arc, boost::optional<const AngularExtent &> maximum_distance_threshold = boost::none, boost::optional<UnitVector3D &> furthest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Returns the maximum angular distance between a unit vector and a great circle arc, and optionally the furthest point on the arc - optionally exceeding a maximum threshold distance. |
| `maximum_distance( const GreatCircleArc &arc, const UnitVector3D &position_vector, boost::optional<const AngularExtent &> maximum_distance_threshold = boost::none, boost::optional<UnitVector3D &> furthest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Overload of maximum\_distance between a point and a great circle arc. |
| `maximum_distance( const PointOnSphere &point, const GreatCircleArc &arc, boost::optional<const AngularExtent &> maximum_distance_threshold = boost::none, boost::optional<UnitVector3D &> furthest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Overload of maximum\_distance between a point and a great circle arc. |
| `maximum_distance( const GreatCircleArc &arc, const PointOnSphere &point, boost::optional<const AngularExtent &> maximum_distance_threshold = boost::none, boost::optional<UnitVector3D &> furthest_position_on_great_circle_arc = boost::none)` | function | `AngularDistance` | Overload of maximum\_distance between a point and a great circle arc. |
| `arcs_lie_on_same_great_circle( const GreatCircleArc &arc1, const GreatCircleArc &arc2)` | function | `bool` | Determine whether the two great-circle arcs arc1 and arc2 lie on the same great-circle. |
| `arcs_are_directed_equivalent( const GreatCircleArc &arc1, const GreatCircleArc &arc2)` | function | `bool` | Determine whether the two great-circle arcs @arc1 and arc2 are equivalent when the directedness of the arcs is taken into account. |
| `arcs_are_undirected_equivalent( const GreatCircleArc &arc1, const GreatCircleArc &arc2)` | function | `bool` | Determine whether the two great-circle arcs @arc1 and arc2 are equivalent when the directedness of the arcs is ignored. |
| `calculate_angle_between_adjacent_non_zero_length_arcs( const GreatCircleArc &first_gca, const GreatCircleArc &second_gca)` | function | `double` | Calculates the angle, in radians, between two adjacent great circle arcs. |

## Notes

[[[PROSE notes unit=maths/GreatCircleArc tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 80 |
| [maths/SphericalArea](SphericalArea.md) | maths | 67 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 64 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 50 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 38 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 35 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 34 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 34 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 27 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 26 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 24 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 23 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 23 |
| [maths/GeometryIntersect](GeometryIntersect.md) | maths | 19 |
| [utils/GeometryCreationUtils](../utils/GeometryCreationUtils.md) | utils | 19 |
| [maths/PolylineIntersections](PolylineIntersections.md) | maths | 18 |
| [maths/deprecated/PolylineIntersections_test](deprecated/PolylineIntersections_test.md) | maths | 18 |
| [opengl/GLIntersect](../opengl/GLIntersect.md) | opengl | 17 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 16 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 16 |

*... and 58 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GreatCircleArc.h
python scripts/gpq.py def GPlatesMaths::GreatCircleArc --body
python scripts/gpq.py uses GreatCircleArc --kind class
python scripts/gpq.py hier GreatCircleArc
```
