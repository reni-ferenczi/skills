# PointOnSphere

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 453 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PointOnSphere.h` | C++ | 615 |
| `src/maths/PointOnSphere.cc` | C++ | 200 |

## Overview

[[[PROSE overview unit=maths/PointOnSphere tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PointOnSphere`](#gplatesmathspointonsphere) | class | [`GPlatesUtils::QtStreamable<PointOnSphere>`](../utils/QtStreamable.md) | — | 0 | Represents a point on the surface of a sphere. |
| [`GPlatesMaths::PointGeometryOnSphere`](#gplatesmathspointgeometryonsphere) | class | [`GeometryOnSphere`](GeometryOnSphere.md)<br>[`GPlatesUtils::QtStreamable<PointGeometryOnSphere>`](../utils/QtStreamable.md) | — | 0 | A derivation of GeometryOnSphere that wraps a PointOnSphere. |
| [`GPlatesMaths::PointOnSphereMapPredicate`](#gplatesmathspointonspheremappredicate) | class | — | — | 0 | Enables PointOnSphere to be used as a key in a 'std::map'. |

## Members

### `GPlatesMaths::PointOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `north_pole` | field | `PointOnSphere` | public | This is the North Pole (latitude \\f$ 90^\\circ \\f$). |
| `south_pole` | field | `PointOnSphere` | public | This is the South Pole (latitude \\f$ -90^\\circ \\f$). |
| `PointOnSphere( const UnitVector3D &position_vector_)` | constructor | `None` | public | Create a new PointOnSphere instance from the unit vector position\_vector\_. |
| `is_close_to( const PointOnSphere &test_point, const real_t &closeness_inclusion_threshold, real_t &closeness)` | method | `bool` | public | Evaluate whether test\_point is "close" to this point. |
| `lies_on_gca( const GreatCircleArc &gca)` | method | `bool` | public | Evaluate whether this point lies on gca. |
| `test_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Test for a proximity hit. |
| `test_vertex_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Test for a proximity hit, but only on the vertices of the geometry. |
| `get_geometry_on_sphere()` | method | `GeometryOnSphere::non_null_ptr_to_const_type` | public | Copy this point into a PointGeometryOnSphere instance and return that as its base class GeometryOnSphere. |
| `get_point_geometry_on_sphere()` | method | `GPlatesUtils::non_null_intrusive_ptr<const PointGeometryOnSphere>` | public | Copy this point into a PointGeometryOnSphere instance. |
| `d_position_vector` | field | `UnitVector3D` | private | This is the 3-D unit-vector which defines the position of this point. |

### `GPlatesMaths::PointGeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PointGeometryOnSphere>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const PointGeometryOnSphere\>. |
| `create( const PointOnSphere &position_)` | method | `non_null_ptr_to_const_type` | public | Create a new PointGeometryOnSphere instance on the heap from the PointOnSphere position\_. |
| `test_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Inherited from GeometryOnSphere. |
| `test_vertex_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Inherited from GeometryOnSphere. |
| `accept_visitor( ConstGeometryOnSphereVisitor &visitor)` | method | `void` | public | Accept a ConstGeometryOnSphereVisitor instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_to_const_type` | public | Return this instance as a non-null pointer. |
| `PointGeometryOnSphere( const PointOnSphere &position_)` | constructor | `None` | private | Construct a PointGeometryOnSphere instance from a PointOnSphere. |
| `d_position` | field | `PointOnSphere` | private | The wrapped point-on-sphere position. |

### `GPlatesMaths::PointOnSphereMapPredicate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const PointOnSphere &lhs, const PointOnSphere &rhs)` | operator | `bool` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `north_pole` | variable | `GPlatesMaths::PointOnSphere` | — |
| `south_pole` | variable | `GPlatesMaths::PointOnSphere` | — |
| `operator()( const PointOnSphere &lhs, const PointOnSphere &rhs)` | operator | `bool` | — |
| `GPLATES_MATHS_POINTONSPHERE_H` | macro | `None` | — |
| `get_antipodal_point( const PointOnSphere &p)` | function | `PointOnSphere` | Return the point antipodal to p on the sphere. |
| `calculate_closeness( const PointOnSphere &p1, const PointOnSphere &p2)` | function | `real_t` | Calculate the "closeness" of the points p1 and p2 on the surface of the sphere. |
| `calculate_distance_on_surface_of_sphere( const PointOnSphere &p1, const PointOnSphere &p2, real_t radius_of_sphere)` | function | `real_t` | Calculate the distance between the points p1 and p2 on the surface of the sphere of radius radius\_of\_sphere. |
| `points_are_coincident( const PointOnSphere &p1, const PointOnSphere &p2)` | function | `bool` | Return whether the points p1 and p2 are coincident. |
| `count_distinct_adjacent_points( PointForwardIter point_seq_begin, PointForwardIter point_seq_end)` | function | `unsigned` | Count the number of distinct adjacent points in the sequence point\_seq in the range point\_seq\_begin / point\_seq\_end (which is assumed to be a sequence of PointOnSphere). |
| `count_distinct_adjacent_points( const S &point_seq)` | function | `unsigned` | Count the number of distinct adjacent points in the sequence point\_seq of type S (which is assumed to be a sequence of PointOnSphere). |
| `populate_point_on_sphere_sequence( D &dest_seq, PointForwardIter source_seq_begin, PointForwardIter source_seq_end)` | function | `void` | Populate the supplied (presumably empty) destination sequence dest\_seq of type D (which is assumed to be a sequence of type PointOnSphere) from the source sequence range source\_seq\_begin / source\_seq\_end (which is assumed to be a sequence ... |
| `populate_point_on_sphere_sequence( D &dest_seq, const S &source_seq)` | function | `void` | Populate the supplied (presumably empty) destination sequence dest\_seq of type D (which is assumed to be a sequence of type PointOnSphere) from the source sequence source\_seq of type S (which is assumed to be a sequence of double). |
| `operator<<` | variable | `std::ostream` | — |
| `operator==( const PointOnSphere &p1, const PointOnSphere &p2)` | operator | `bool` | — |
| `operator!=( const PointOnSphere &p1, const PointOnSphere &p2)` | operator | `bool` | — |
| `operator==( const PointGeometryOnSphere &p1, const PointGeometryOnSphere &p2)` | operator | `bool` | — |
| `operator!=( const PointGeometryOnSphere &p1, const PointGeometryOnSphere &p2)` | operator | `bool` | — |

## Notes

[[[PROSE notes unit=maths/PointOnSphere tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GenerateVelocityDomainCitcoms](../app-logic/GenerateVelocityDomainCitcoms.md) | app-logic | 28 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 22 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 15 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 14 |
| [gui/deprecated/GLCanvas](../gui/deprecated/GLCanvas.md) | gui | 14 |
| [maths/CalculateVelocity](CalculateVelocity.md) | maths | 14 |
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 13 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 12 |
| [opengl/GLCubeSubdivision](../opengl/GLCubeSubdivision.md) | opengl | 12 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 10 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 10 |
| [unit-test/FeatureHandleTest](../unit-test/FeatureHandleTest.md) | unit-test | 10 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 9 |
| [maths/EllipseGenerator](EllipseGenerator.md) | maths | 8 |
| [maths/GreatCircle](GreatCircle.md) | maths | 8 |
| [qt-widgets/FiniteRotationCalculatorDialog](../qt-widgets/FiniteRotationCalculatorDialog.md) | qt-widgets | 7 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 6 |
| [gui/TopologySectionsContainer](../gui/TopologySectionsContainer.md) | gui | 6 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 6 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 6 |

*... and 151 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PointOnSphere.h
python scripts/gpq.py def GPlatesMaths::PointOnSphere --body
python scripts/gpq.py uses PointOnSphere --kind class
python scripts/gpq.py hier PointOnSphere
```
