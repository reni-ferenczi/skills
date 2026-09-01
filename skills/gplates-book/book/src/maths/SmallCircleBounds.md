# SmallCircleBounds

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 27 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SmallCircleBounds.h` | C++ | 1572 |
| `src/maths/SmallCircleBounds.cc` | C++ | 1041 |

## Overview

The spherical equivalent of a bounding sphere, and the first line of rejection
for nearly every geometric query in GPlates. A `BoundingSmallCircle` is a centre
`UnitVector3D` plus a radius held as an `AngularExtent`; a geometry is bounded by
it when every part of the geometry lies within that angle of the centre.
`InnerOuterBoundingSmallCircle` adds a second, concentric inner radius, which
buys a strictly stronger statement: not only is the geometry inside the outer
circle, it is entirely *outside* the inner one. That extra fact is what makes
"could this geometry possibly touch that polygon's outline?" answerable without
touching a single arc — the case the header calls out for polygon clipping and
point-in-polygon work.

The design decision that pervades the file is that no angles are ever computed.
`AngularExtent` stores cosine and sine, sums and differences of extents go
through trigonometric angle-sum identities, and the cosine of the angle between
two centres is just their dot product — so a bounds test is a handful of
multiplies and no `acos`. The one function that breaks this is
`create_optimal_bounding_small_circle`, which needs real angles for its half-angle
construction and says so; its comment also explains why not caching those `acos`
results is acceptable (it is only called while building a bounding tree
bottom-up, once per node). The two builder classes are the intended construction
path: they take a fixed centre, accumulate the running minimum and maximum
`AngularDistance` as primitives are added, and bake the result out on demand.

`PolygonOnSphere`, `PolylineOnSphere` and `MultiPointOnSphere` each cache one of
these on first request, centred on their boundary centroid;
`PolyGreatCircleArcBoundingTree` builds a hierarchy of them over a geometry's
arcs. From there the consumers are `PointInPolygon`, `DateLineWrapper`,
`GeneratePoints`, `CubeQuadTreePartition` and the OpenGL raster and mesh
classes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::BoundingSmallCircle`](#gplatesmathsboundingsmallcircle) | class | — | — | 0 | A small circle that encloses a region. |
| [`GPlatesMaths::BoundingSmallCircleBuilder`](#gplatesmathsboundingsmallcirclebuilder) | class | — | — | 0 | Used to incrementally build an BoundingSmallCircle. |
| [`GPlatesMaths::InnerOuterBoundingSmallCircle`](#gplatesmathsinnerouterboundingsmallcircle) | class | — | — | 0 | Two concentric small circles that enclose an annular region. |
| [`GPlatesMaths::InnerOuterBoundingSmallCircleBuilder`](#gplatesmathsinnerouterboundingsmallcirclebuilder) | class | — | — | 0 | Used to incrementally build an InnerOuterBoundingSmallCircle. |

## Members

### `GPlatesMaths::BoundingSmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BoundingSmallCircle( const UnitVector3D &small_circle_centre, const AngularExtent &angular_extent_radius)` | constructor | `None` | public | Ideally use BoundingSmallCircleBuilder to construct this. angular\_extent\_radius is the angular extent (radius) of the small circle boundary with the small circle centre. |
| `Result` | enum | `None` | public | The result of testing a primitive against the bounding region can return fully outside, fully inside or intersecting. |
| `test( const UnitVector3D &point)` | method | `Result` | public | Test a point against the bounding region. |
| `test( const GreatCircleArc &gca)` | method | `Result` | public | Test a great circle arc against the bounding region. |
| `test( GreatCircleArcForwardIter great_circle_arc_begin, GreatCircleArcForwardIter great_circle_arc_end)` | method | `Result` | public | Test a sequence of great circle arcs against the bounding region. |
| `test( const PointOnSphere &point)` | method | `Result` | public | Test a point against the bounding region. |
| `test( const MultiPointOnSphere &multi_point)` | method | `Result` | public | Test a multi-point against the bounding region. |
| `test( const PolylineOnSphere &polyline)` | method | `Result` | public | Test a polyline against the bounding region. |
| `test( const PolygonOnSphere &polygon)` | method | `Result` | public | Test a polygon against the bounding region. |
| `test_filled_polygon( const PolygonOnSphere &polygon)` | method | `Result` | public | Test a filled polygon against the bounding region. |
| `set_centre( const UnitVector3D &centre)` | method | `void` | public | Sets the small circle centre. |
| `expand( const AngularExtent &angular_expansion)` | method | `BoundingSmallCircle` | public | Creates a bounding small circle extended by the specified angle. |
| `contract( const AngularExtent &angular_contraction)` | method | `BoundingSmallCircle` | public | Creates a bounding small circle contracted by the specified angle. |
| `d_small_circle_centre` | field | `UnitVector3D` | private | — |
| `d_angular_extent` | field | `AngularExtent` | private | — |

### `GPlatesMaths::BoundingSmallCircleBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BoundingSmallCircleBuilder( const UnitVector3D &small_circle_centre)` | constructor | `None` | public | — |
| `add( const UnitVector3D &point)` | method | `void` | public | Adds a point on the sphere - the bound is expanded if necessary to bound the point. |
| `add( const GreatCircleArc &gca)` | method | `void` | public | Adds a great circle arc - the bound is expanded if necessary to bound the great circle arc. |
| `add( GreatCircleArcForwardIter great_circle_arc_begin, GreatCircleArcForwardIter great_circle_arc_end)` | method | `void` | public | Adds a sequence of great circle arcs and calls add on each great circle arc. |
| `add( const PointOnSphere &point)` | method | `void` | public | Adds a point on the sphere - the bound is expanded if necessary to bound the point. |
| `add( const MultiPointOnSphere &multi_point)` | method | `void` | public | Adds a multi-point on the sphere - the bound is expanded if necessary to bound the points. |
| `add( const PolygonOnSphere &polygon)` | method | `void` | public | Adds the great circle arcs in a polygon - the bound is expanded if necessary to bound them. |
| `add( const PolylineOnSphere &polyline)` | method | `void` | public | Adds the great circle arcs in a polyline - the bound is expanded if necessary to bound them. |
| `add( const BoundingSmallCircle &bounding_small_circle)` | method | `void` | public | Expands the bound to include the small circle of bounding\_small\_circle. |
| `get_bounding_small_circle( const AngularExtent &angular_expansion = get_default_angular_expansion())` | method | `BoundingSmallCircle` | public | Returns the bounding small circle of all primitives added so far. angular\_expansion is used to expand the bound to account for numerical precision. |
| `d_small_circle_centre` | field | `UnitVector3D` | private | — |
| `d_maximum_distance` | field | `AngularDistance` | private | — |
| `get_default_angular_expansion` | field | `AngularExtent` | public | Default angular expansion used to expand returned bounding small circles. |

### `GPlatesMaths::InnerOuterBoundingSmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InnerOuterBoundingSmallCircle( const UnitVector3D &small_circle_centre, const AngularExtent &outer_angular_extent_radius, const AngularExtent &inner_angular_extent_radius)` | constructor | `None` | public | These are also the minimum and maximum dot products of any geometry, bounded by these small circles, with the small circle(s) common centre. |
| `Result` | enum | `None` | public | The result of testing a primitive against the bounding region can return fully outside, fully inside or intersecting the region between the inner and outer bounds. |
| `test( const UnitVector3D &point)` | method | `Result` | public | Test a point against the bounding region. |
| `test( const GreatCircleArc &gca)` | method | `Result` | public | Test a great circle arc against the bounding region. |
| `test( GreatCircleArcForwardIter great_circle_arc_begin, GreatCircleArcForwardIter great_circle_arc_end)` | method | `Result` | public | Test a sequence of great circle arcs against the bounding region. |
| `test( const PointOnSphere &point)` | method | `Result` | public | Test a point against the bounding region. |
| `test( const MultiPointOnSphere &multi_point)` | method | `Result` | public | Test a multi-point against the bounding region. |
| `test( const PolylineOnSphere &polyline)` | method | `Result` | public | Test a polyline against the bounding region. |
| `test( const PolygonOnSphere &polygon)` | method | `Result` | public | Test a polygon against the bounding region. |
| `test_filled_polygon( const PolygonOnSphere &polygon)` | method | `Result` | public | Test a filled polygon against the bounding region. |
| `set_centre( const UnitVector3D &centre)` | method | `void` | public | Sets the centre of both small circles. |
| `get_inner_bounding_small_circle()` | method | `BoundingSmallCircle` | public | Returns the inner small circle boundary - a simplification that ignores the outer bounds. |
| `d_outer_small_circle` | field | `BoundingSmallCircle` | private | — |
| `d_inner_angular_extent` | field | `AngularExtent` | private | — |

### `GPlatesMaths::InnerOuterBoundingSmallCircleBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InnerOuterBoundingSmallCircleBuilder( const UnitVector3D &small_circle_centre)` | constructor | `None` | public | — |
| `add( const UnitVector3D &point)` | method | `void` | public | Adds a point on the sphere - the inner/outer bounds are contracted/expanded if necessary to bound the point. |
| `add( const GreatCircleArc &gca)` | method | `void` | public | Adds a great circle arc - the inner/outer bounds are contracted/expanded if necessary to bound the great circle arc. |
| `add( GreatCircleArcForwardIter great_circle_arc_begin, GreatCircleArcForwardIter great_circle_arc_end)` | method | `void` | public | Adds a sequence of great circle arcs and calls add on each great circle arc. |
| `add( const PointOnSphere &point)` | method | `void` | public | Adds a point on the sphere - the inner/outer bounds are contracted/expanded if necessary to bound the point. |
| `add( const MultiPointOnSphere &multi_point)` | method | `void` | public | Adds a multi-point on the sphere - the inner/outer bounds are contracted/expanded if necessary to bound the points. |
| `add( const PolygonOnSphere &polygon)` | method | `void` | public | Adds the great circle arcs in a polygon - the inner/outer bounds are contracted/expanded if necessary to bound the polygon. |
| `add( const PolylineOnSphere &polyline)` | method | `void` | public | Adds the great circle arcs in a polyline - the inner/outer bounds are contracted/expanded if necessary to bound the polyline. |
| `add( const BoundingSmallCircle &bounding_small_circle)` | method | `void` | public | Expands the bound to include the small circle of bounding\_small\_circle. |
| `add( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | method | `void` | public | Expands/contracts the outer/inner bounds to include the region bounded by inner\_outer\_bounding\_small\_circle. |
| `get_inner_outer_bounding_small_circle( const AngularExtent &inner_bound_angular_contraction = get_default_angular_expansion_contraction(), const AngularExtent &outer_bound_angular_expansion = get_default_angular_expansion_contraction())` | method | `InnerOuterBoundingSmallCircle` | public | Returns the inner outer bounding small circle of all primitives added so far. inner\_bound\_angular\_contraction is used to contract the \*inner\* bound to account for numerical precision. expand\_outer\_bound\_delta\_dot\_product is used to expand ... |
| `d_small_circle_centre` | field | `UnitVector3D` | private | — |
| `d_minimum_distance` | field | `AngularDistance` | private | — |
| `d_maximum_distance` | field | `AngularDistance` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator*( const FiniteRotation &rotation, const BoundingSmallCircle &bounding_small_circle)` | operator | `GPlatesMaths::BoundingSmallCircle` | — |
| `operator*( const Rotation &rotation, const BoundingSmallCircle &bounding_small_circle)` | operator | `GPlatesMaths::BoundingSmallCircle` | — |
| `operator*( const FiniteRotation &rotation, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | operator | `GPlatesMaths::InnerOuterBoundingSmallCircle` | — |
| `operator*( const Rotation &rotation, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | operator | `GPlatesMaths::InnerOuterBoundingSmallCircle` | — |
| `GPLATES_MATHS_SMALLCIRCLEBOUNDS_H` | macro | `None` | — |
| `create_optimal_bounding_small_circle( const BoundingSmallCircle &bounding_small_circle_1, const BoundingSmallCircle &bounding_small_circle_2)` | function | `BoundingSmallCircle` | Creates the optimal small circle that bounds the two specified bounding small circles. |
| `intersect( const BoundingSmallCircle &bounding_small_circle, const double &point_dot_circle_centre)` | function | `bool` | — |
| `intersect( const BoundingSmallCircle &bounding_small_circle_1, const BoundingSmallCircle &bounding_small_circle_2, const double &dot_product_circle_centres)` | function | `bool` | — |
| `minimum_distance( const BoundingSmallCircle &bounding_small_circle, const double &point_dot_circle_centre)` | function | `AngularDistance` | — |
| `minimum_distance( const BoundingSmallCircle &bounding_small_circle_1, const BoundingSmallCircle &bounding_small_circle_2, const double &dot_product_circle_centres)` | function | `AngularDistance` | — |
| `intersect( const PointOnSphere &point, const BoundingSmallCircle &bounding_small_circle)` | function | `bool` | Returns true if the point intersects (is inside) the bounding small circle. |
| `intersect( const BoundingSmallCircle &bounding_small_circle, const PointOnSphere &point)` | function | `bool` | Returns true if the point intersects (is inside) the bounding small circle. |
| `intersect( const UnitVector3D &position, const BoundingSmallCircle &bounding_small_circle)` | function | `bool` | Returns true if the position intersects (is inside) the bounding small circle. |
| `intersect( const BoundingSmallCircle &bounding_small_circle, const UnitVector3D &position)` | function | `bool` | Returns true if the position intersects (is inside) the bounding small circle. |
| `intersect( const BoundingSmallCircle &bounding_small_circle_1, const BoundingSmallCircle &bounding_small_circle_2)` | function | `bool` | Returns true if the two bounding small circles intersect each other. |
| `minimum_distance( const PointOnSphere &point, const BoundingSmallCircle &bounding_small_circle)` | function | `AngularDistance` | Returns the minimum angular distance between a point and a bounding small circle. |
| `minimum_distance( const BoundingSmallCircle &bounding_small_circle, const PointOnSphere &point)` | function | `AngularDistance` | Returns the minimum angular distance between a point and a bounding small circle. |
| `minimum_distance( const UnitVector3D &position, const BoundingSmallCircle &bounding_small_circle)` | function | `AngularDistance` | Returns the minimum angular distance between a position and a bounding small circle. |
| `minimum_distance( const BoundingSmallCircle &bounding_small_circle, const UnitVector3D &position)` | function | `AngularDistance` | Returns the minimum angular distance between a position and a bounding small circle. |
| `minimum_distance( const BoundingSmallCircle &bounding_small_circle_1, const BoundingSmallCircle &bounding_small_circle_2)` | function | `AngularDistance` | Returns the minimum angular distance between two bounding small circles. |
| `intersect( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const double &point_dot_circle_centre)` | function | `bool` | — |
| `intersect( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const BoundingSmallCircle &bounding_small_circle, const double &dot_product_circle_centres)` | function | `bool` | — |
| `intersect( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_1, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_2, const double &dot_product_circle_centres)` | function | `bool` | — |
| `minimum_distance( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const double &point_dot_circle_centre)` | function | `AngularDistance` | — |
| `minimum_distance( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const BoundingSmallCircle &bounding_small_circle, const double &dot_product_circle_centres)` | function | `AngularDistance` | — |
| `minimum_distance( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_1, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_2, const double &dot_product_circle_centres)` | function | `AngularDistance` | — |
| `is_inside_inner_bounding_small_circle( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const BoundingSmallCircle &bounding_small_circle, const double &dot_product_circle_centres)` | function | `bool` | — |
| `is_inside_inner_bounding_small_circle( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_1, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_2, const double &dot_product_circle_centres)` | function | `bool` | — |
| `intersect( const PointOnSphere &point, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | function | `bool` | Returns true if the point intersects the inner-outer bounding small circle. |
| `intersect( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const PointOnSphere &point)` | function | `bool` | Returns true if the point intersects the inner-outer bounding small circle. |
| `intersect( const UnitVector3D &position, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | function | `bool` | Returns true if the position intersects the inner-outer bounding small circle. |
| `intersect( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const UnitVector3D &position)` | function | `bool` | Returns true if the position intersects the inner-outer bounding small circle. |
| `intersect( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const BoundingSmallCircle &bounding_small_circle)` | function | `bool` | Returns true if a bounding small circle intersects an inner-outer bounding small circle. |
| `intersect( const BoundingSmallCircle &bounding_small_circle, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | function | `bool` | Returns true if a bounding small circle intersects an inner-outer bounding small circle. |
| `intersect( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_1, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_2)` | function | `bool` | Returns true if the two inner-outer bounding small circles intersect each other. |
| `minimum_distance( const PointOnSphere &point, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | function | `AngularDistance` | Returns the minimum angular distance between a point and an inner-outer bounding small circle. |
| `minimum_distance( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const PointOnSphere &point)` | function | `AngularDistance` | Returns the minimum angular distance between a point and an inner-outer bounding small circle. |
| `minimum_distance( const UnitVector3D &position, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | function | `AngularDistance` | Returns the minimum angular distance between a position and an inner-outer bounding small circle. |
| `minimum_distance( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const UnitVector3D &position)` | function | `AngularDistance` | Returns the minimum angular distance between a position and an inner-outer bounding small circle. |
| `minimum_distance( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const BoundingSmallCircle &bounding_small_circle)` | function | `AngularDistance` | Returns the minimum angular distance of a bounding small circle to an inner-outer bounding small circle. |
| `minimum_distance( const BoundingSmallCircle &bounding_small_circle, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | function | `AngularDistance` | Returns the minimum angular distance of a bounding small circle to an inner-outer bounding small circle. |
| `minimum_distance( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_1, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_2)` | function | `AngularDistance` | Returns the minimum angular distance between two inner-outer bounding small circles. |
| `is_inside_inner_bounding_small_circle( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle, const BoundingSmallCircle &bounding_small_circle)` | function | `bool` | Returns true if bounding\_small\_circle is completely inside the inner bounding small circle of inner\_outer\_bounding\_small\_circle. |
| `is_inside_inner_bounding_small_circle( const BoundingSmallCircle &bounding_small_circle, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle)` | function | `bool` | Returns true if bounding\_small\_circle is completely inside the inner bounding small circle of inner\_outer\_bounding\_small\_circle. |
| `is_inside_inner_bounding_small_circle( const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_1, const InnerOuterBoundingSmallCircle &inner_outer_bounding_small_circle_2)` | function | `bool` | Returns true if inner\_outer\_bounding\_small\_circle\_2 is completely inside the inner bounding small circle of inner\_outer\_bounding\_small\_circle\_1. |

## Notes

**The iterator `test()` overloads require a *connected* arc sequence.** This is
the sharpest trap in the file. Both templates classify the first arc, and if it
is wholly outside (or wholly inside) they scan the remainder only for a state
change, returning `INTERSECTING_BOUNDS` at the first one. That shortcut is valid
only because each arc begins where the last ended, as in a polyline or one
polygon ring. Hand these a disconnected set of arcs and they return a confident
wrong answer with no diagnostic. The polygon overloads honour this by testing the
exterior ring and each interior ring as separate sequences.

**Bounds are deliberately loose, in one direction.** Both builders apply a
default expansion (and, for the inner bound, contraction) equal to
`GeometryIntersect::Intersection::get_on_segment_start_threshold_cosine()`, so a
bound covers the "touching" region around its geometry. The header states the
intent: false positives are acceptable because a later exact test will reject
them, whereas a false negative discards a real intersection irrecoverably. Do
not pass `AngularExtent::ZERO` to tighten a bound unless you are certain no
downstream code depends on that margin.

**Centres are chosen by the caller, not the builder.** Both builders fix the
centre at construction and never move it. A poorly chosen centre yields a bound
that is correct but useless — the geometry classes pass their boundary centroid.
Relatedly, `InnerOuterBoundingSmallCircle`'s inner circle is *not* the polygon
interior: the centroid may fall outside the polygon entirely, and
`PolygonOnSphere`'s own documentation says so explicitly.

**`AngularExtent` caches lazily through `mutable` members.** Its sine and angle
are `mutable boost::optional<real_t>`, filled in on first request. So a `const`
call on a shared `BoundingSmallCircle` can write to it, and these objects are not
safe to use concurrently from multiple threads without external synchronisation —
including the instances cached inside `PolygonOnSphere` and friends. This is also
why `operator*(FiniteRotation, ...)` copies the bound and mutates the centre
through `set_centre` instead of building a fresh one: it preserves whatever the
original had already computed. Rotating only the centre is exact, since a rigid
rotation leaves the radius unchanged.

**Degenerate and edge cases.**

- `test()` on a point (or `PointOnSphere`) never returns `INTERSECTING_BOUNDS` —
  a point is inside or outside, nothing else.
- An empty arc range returns `OUTSIDE_BOUNDS` / `OUTSIDE_OUTER_BOUNDS`.
- The `MultiPointOnSphere` overloads dereference `begin()` without an emptiness
  check; this is safe only because `MultiPointOnSphere` guarantees at least one
  point.
- `InnerOuterBoundingSmallCircleBuilder::get_inner_outer_bounding_small_circle()`
  detects that nothing was ever added by comparing the untouched sentinel
  cosines, then emits a `qWarning` and returns zero-radius bounds rather than
  throwing. Easy to miss in a log.
- `create_optimal_bounding_small_circle` special-cases coincident and antipodal
  centres before it can divide by a zero-length cross product, falling back to
  `generate_perpendicular` in the antipodal case; it also clamps the resulting
  radius at PI, since `(A + R1 + R2)/2` can reach 1.5·PI.
- `test_filled_polygon` differs from `test(polygon)` only for the surrounding
  case, and pays for it with a real `is_point_in_polygon` call — use the plain
  overload when outline intersection is all you need.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GeneratePoints](GeneratePoints.md) | maths | 45 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 17 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 14 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 8 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 6 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 5 |
| [maths/SmallCircleCoverageMesh](SmallCircleCoverageMesh.md) | maths | 5 |
| [maths/PolyGreatCircleArcBoundingTree](PolyGreatCircleArcBoundingTree.md) | maths | 4 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 3 |
| [maths/MultiPointOnSphere](MultiPointOnSphere.md) | maths | 3 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 3 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 1 |
| [maths/CubeQuadTreePartition](CubeQuadTreePartition.md) | maths | 1 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/SmallCircleBounds.h
python scripts/gpq.py def GPlatesMaths::InnerOuterBoundingSmallCircle --body
python scripts/gpq.py uses InnerOuterBoundingSmallCircle --kind class
python scripts/gpq.py hier InnerOuterBoundingSmallCircle
```
