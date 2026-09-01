# GreatCircleArc

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 526 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GreatCircleArc.h` | C++ | 724 |
| `src/maths/GreatCircleArc.cc` | C++ | 1302 |

## Overview

A `GreatCircleArc` is the edge primitive of GPlates geometry: the shortest path between
two `PointOnSphere`s, and the element type of the `std::vector<GreatCircleArc>` that
`PolylineOnSphere` and `PolygonOnSphere` store. That storage role dominates the class's
design. An arc keeps only its two endpoints and the pre-computed dot product of their
position vectors; everything else — arc length, whether the arc is degenerate, the
rotation axis — lives in the private `CachedOnDemand` block and is computed on first
request. The header spells out why that block is a hand-packed struct of two booleans
plus a `UnitVector3D` and a `real_t` rather than a set of `boost::optional` members:
each `optional` would cost an extra eight bytes after alignment, multiplied by every
edge of every reconstructed geometry. The same reasoning explains why animating a
reconstruction is cheap — displaying a polyline never asks for a rotation axis, so the
axis is never computed.

The domain has two edge cases that shape the whole interface. Antipodal endpoints do not
determine an arc, so `create` throws `IndeterminateResultException` for them (and
`evaluate_construction_parameter_validity` lets a caller check first and then pass
`check_validity = false` on the hot path). Coincident endpoints, by contrast, *are*
legal: they give a zero-length, point-like arc that has no determinate rotation axis, so
`rotation_axis()` throws `IndeterminateArcRotationAxisException`. Every algorithm in the
`.cc` therefore branches on `is_zero_length()` first and falls back to point-to-point
comparisons — `intersect`, `arcs_lie_on_same_great_circle` and `minimum_distance` all
open that way, and `ArcHasIndeterminateRotationAxis` exists so callers can filter such
arcs out of a sequence.

The free functions are the geometric kernel that `GeometryDistance`, `GeometryIntersect`,
`PolylineIntersections`, `SphericalArea` and the OpenGL raster code build on. Distances
are returned as `AngularDistance` and thresholds taken as `AngularExtent` — cosine/sine
pairs rather than angles, which keeps the common case to dot products and avoids `acos`.
The threshold arguments are not just filters but an optimisation and a correctness
device: when a threshold is exceeded the functions return `AngularDistance::PI` as a
sentinel and deliberately leave the caller's closest-point out-parameters untouched, and
the arc-to-arc `minimum_distance` tightens the threshold after each of its four
point-to-arc probes so a later, further probe cannot overwrite the closest point found
by an earlier one. `maximum_distance` is implemented as PI minus the minimum distance to
the antipodal arc (or antipodal point), citing the Minkowski-addition thesis the
lune-based point-to-arc test also comes from. `tessellate` is the subdivision routine the
renderers and exporters use; it re-appends the original end point rather than the last
rotated one, so accumulated rotation error never moves an arc's endpoint.

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

**Invariant.** The endpoints are never antipodal, so the spanned angle lies in [0, PI)
and the arc is unique. The test is `dot_p1_p2 <= -1.0` evaluated in `real_t`, hence
epsilon-tolerant like all `GPlatesMaths::Real` comparisons. Everything else about the
arc is derived from the two endpoints, which is why `operator==` compares only
`d_start_point` and `d_end_point` and ignores the cached fields.

**The cache is `mutable` and lazily filled by `const` member functions, with no
locking.** `is_zero_length()`, `rotation_axis()` and `arc_length()` all write into
`d_cached_on_demand` on first call, so sharing one arc — or one `PolylineOnSphere`,
whose arcs are owned by an immutable, reference-counted geometry — across threads and
querying it concurrently is a data race even though every call site looks read-only.

**Two different notions of "zero length" coexist.** `is_zero_length()` tests
`cross(start, end).magSqrd() <= 0` under `real_t`'s epsilon, while `arc_length()` is
`acos` of the endpoint dot product. The header states the consequence explicitly: an arc
can report zero length and still return a non-zero `arc_length()`.
`get_zero_length_threshold_cosine()` exists only to tell other classes the approximate
upper bound of a zero-length arc; it is not the predicate the class actually uses, and
the header warns against using it as one.

**`create_rotated_arc` and `create_antipodal_arc` copy the cache instead of
invalidating it**, on the reasoning that the endpoint dot product and the arc length
survive both transforms and the rotation axis only needs rotating (and is left alone
under the antipodal transform). If you add a cached quantity that is not invariant under
those operations, both functions must be updated or they will silently propagate a stale
value.

**Threshold semantics in the distance functions.** Exceeding a `minimum_distance`
threshold is signalled by returning `AngularDistance::PI`, not by a boolean or an
optional — and in that case the caller's closest-point references are left *unmodified*,
so an uninitialised out-parameter stays uninitialised. `maximum_distance` mirrors this
with `AngularDistance::ZERO`. The private helper
`minimum_distance_for_position_inside_arc_lune` additionally requires that the position
not equal the arc's plane normal; its caller guards that with epsilon-tested dot products
rather than an explicit check, so calling the helper directly is unsafe.

**Other sharp edges.** `direction_on_arc` throws `IndeterminateArcRotationAxisException`
on a zero-length arc even though `point_on_arc` handles that case silently.
`point_on_arc` returns the stored endpoints exactly at 0 and 1 rather than rotating, and
accepts values outside [0, 1] as extrapolation. When two arcs overlap along the same
great circle, `intersect` reports an arbitrary endpoint of one of them as *the*
intersection. `arcs_are_near_each_other` is a conservative pre-filter only — a false
result rules out intersection, a true result proves nothing.
`calculate_angle_between_adjacent_non_zero_length_arcs` trusts the caller on both of its
preconditions (neither arc zero-length, and the arcs genuinely adjacent in sequence
order) and returns an angle in [0, 2PI).

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
