# GeometryInterpolation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 261 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryInterpolation.h` | C++ | 132 |
| `src/maths/GeometryInterpolation.cc` | C++ | 1598 |

## Overview

[[[PROSE overview unit=maths/GeometryInterpolation tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::RotationInterpolateImpl::LatitudeGreaterCompare`](#gplatesmathsrotationinterpolateimpllatitudegreatercompare) | struct | — | — | 0 | Compares latitude of two points (distances relative to a North pole) using greater than. |
| [`GPlatesMaths::RotationInterpolateImpl::interpolate_param_type`](#gplatesmathsrotationinterpolateimplinterpolate_param_type) | typedef | — | — | 0 | Typedef for: 1) an interpolation distance interval (in radians), or 2) a sequence of interpolation factors (each in the range \[0,1\]). |
| [`GPlatesMaths::FlattenLongitudeOverlaps::Value`](#gplatesmathsflattenlongitudeoverlapsvalue) | enum | — | — | 0 | — |

## Members

### `GPlatesMaths::RotationInterpolateImpl::LatitudeGreaterCompare`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LatitudeGreaterCompare( const UnitVector3D &north_pole)` | constructor | `None` | public | — |
| `operator()( const PointOnSphere &p1, const PointOnSphere &p2)` | operator | `bool` | public | — |
| `d_north_pole` | field | `UnitVector3D` | private | — |

### `GPlatesMaths::RotationInterpolateImpl::interpolate_param_type`

*None.*

### `GPlatesMaths::FlattenLongitudeOverlaps::Value`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NO` | enumerator | `None` | — | — |
| `USE_FROM` | enumerator | `None` | — | — |
| `USE_TO` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INTERTEC_MONOTONICALLY_DECREASING_LATITUDE_BEHAVIOUR` | macro | `None` | Define this to make our monotonically decreasing latitudes behave like the original Intertec program. |
| `overlap( const PolylineOnSphere::non_null_ptr_to_const_type &from_polyline, const PolylineOnSphere::non_null_ptr_to_const_type &to_polyline, const UnitVector3D &rotation_axis, const double &minimum_latitude_overlap_radians)` | function | `bool` | Ensure the latitude (distance from rotation axis) overlap of the polylines exceeds the minimum requested amount. |
| `ensure_points_are_monotonically_decreasing_in_latitude( std::list<PointOnSphere> &polyline_points, const UnitVector3D &rotation_axis)` | function | `void` | Ensure polyline has points that are monotonically decreasing in latitude (distance from rotation axis). |
| `intersect_small_circle_with_great_circle_arc( const PointOnSphere &point1, const PointOnSphere &point2, const double &small_circle_axis_dot_product, const UnitVector3D &small_circle_axis)` | function | `PointOnSphere` | Interpolate between the point1 and point2 (along their connecting great circle arc) such that the resultant point has a dot product with small\_circle\_axis of small\_circle\_axis\_dot\_product. |
| `limit_latitude_range( std::list<PointOnSphere> &from_polyline_points, std::list<PointOnSphere> &to_polyline_points, const UnitVector3D &rotation_axis, std::vector<GreatCircleArc> &north_non_overlapping_latitude_arcs, std::vector<GreatCircleArc> &south_non_overlapping_latitude_arcs, boost::optional<double> max_latitude_ ...` | function | `bool` | Clip away any latitude ranges of either polyline that is not common to both polylines. |
| `ensure_aligned_latitudes( std::list<PointOnSphere> &points, const std::vector<PointOnSphere> &all_points, const UnitVector3D &rotation_axis)` | function | `void` | Ensure that points has a point at each latitude in all\_points. |
| `point1_is_left_of_point2( const UnitVector3D &point1, const UnitVector3D &point2, const UnitVector3D &rotation_axis)` | function | `bool` | Returns true if point1 is mostly to the left of point2 in the reference frame where rotation\_axis is the North pole. |
| `flatten_overlaps_in_longitude( std::list<PointOnSphere> &from_polyline_points, std::list<PointOnSphere> &to_polyline_points, const UnitVector3D &rotation_axis, FlattenLongitudeOverlaps::Value flatten_longitude_overlaps)` | function | `void` | Ensures longitudes of points of the left-most polyline (in North pole reference frame) don't overlap right-most polyline. |
| `are_polylines_within_maximum_distance_threshold( const std::list<PointOnSphere> &from_polyline_points, const std::list<PointOnSphere> &to_polyline_points, boost::optional<AngularDistance> max_angular_distance_threshold)` | function | `bool` | Returns true if the distance (between corresponding latitude points of the polylines) does not exceed max\_angular\_distance\_threshold (if specified). |
| `calculate_interpolate_ratios( std::vector<double> &interpolate_ratios, const std::list<PointOnSphere> &from_polyline_points, const std::list<PointOnSphere> &to_polyline_points, const UnitVector3D &rotation_axis, const double &interpolate_resolution_radians, boost::optional<AngularDistance> max_angular_distance_threshol ...` | function | `bool` | Calculate the evenly-spaced interpolate ratios for all interpolated polylines including the 'from' and 'to' polylines (ratios 0 and 1). |
| `calculate_interpolate_point_rotations( std::vector<Rotation> &interpolate_point_rotations, const std::vector<double> &interpolate_ratios, const std::list<PointOnSphere> &from_latitude_overlapping_points, const std::list<PointOnSphere> &to_latitude_overlapping_points, const UnitVector3D &rotation_axis, const std::vector ...` | function | `void` | Create a rotation for each 'from' / 'to' point pair that rotates from 'from' to 'to'. |
| `interpolate_polylines( std::vector<PolylineOnSphere::non_null_ptr_to_const_type> &interpolated_polylines, const std::list<PointOnSphere> &from_polyline_points, const std::vector<Rotation> &interpolate_point_rotations, const std::vector<double> &interpolate_ratios)` | function | `void` | Generate interpolated polylines and append to interpolated\_polylines. |
| `interpolate( std::vector<PolylineOnSphere::non_null_ptr_to_const_type> &interpolated_polylines, const PolylineOnSphere::non_null_ptr_to_const_type &from_polyline, const PolylineOnSphere::non_null_ptr_to_const_type &to_polyline, const UnitVector3D &rotation_axis, interpolate_param_type interpolate_param, const double &m ...` | function | `bool` | The main implementation function for rotation interpolation. |
| `GPLATES_MATHS_GEOMETRYINTERPOLATION_H` | macro | `None` | — |
| `interpolate( std::vector<PolylineOnSphere::non_null_ptr_to_const_type> &interpolated_polylines, const PolylineOnSphere::non_null_ptr_to_const_type &from_polyline, const PolylineOnSphere::non_null_ptr_to_const_type &to_polyline, const UnitVector3D &rotation_axis, const double &interpolate_resolution_radians, const doubl ...` | function | `bool` | The maximum distance between adjacent interpolated polylines is interpolate\_resolution\_radians. |
| `interpolate( std::vector<PolylineOnSphere::non_null_ptr_to_const_type> &interpolated_polylines, const PolylineOnSphere::non_null_ptr_to_const_type &from_polyline, const PolylineOnSphere::non_null_ptr_to_const_type &to_polyline, const UnitVector3D &rotation_axis, const std::vector<double> &interpolate_ratios, const doub ...` | function | `bool` | Interpolates between two polylines along small circle arcs emanating from rotation\_axis. |

## Notes

[[[PROSE notes unit=maths/GeometryInterpolation tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryInterpolation.h
python scripts/gpq.py def GPlatesMaths::RotationInterpolateImpl::LatitudeGreaterCompare --body
python scripts/gpq.py uses LatitudeGreaterCompare --kind struct
python scripts/gpq.py hier LatitudeGreaterCompare
```
