# SmallCircleBounds

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 27 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SmallCircleBounds.h` | C++ | 1572 |
| `src/maths/SmallCircleBounds.cc` | C++ | 1041 |

## Overview

[[[PROSE overview unit=maths/SmallCircleBounds tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/SmallCircleBounds tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
