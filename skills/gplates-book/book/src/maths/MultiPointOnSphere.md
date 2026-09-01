# MultiPointOnSphere

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 362 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/MultiPointOnSphere.h` | C++ | 487 |
| `src/maths/MultiPointOnSphere.cc` | C++ | 252 |

## Overview

[[[PROSE overview unit=maths/MultiPointOnSphere tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::MultiPointOnSphereImpl::CachedCalculations`](#gplatesmathsmultipointonsphereimplcachedcalculations) | struct | [`GPlatesUtils::ReferenceCount<CachedCalculations>`](../utils/ReferenceCount.md) | — | 0 | Cached results of calculations performed on the multipoint geometry. |
| [`GPlatesMaths::MultiPointOnSphere`](#gplatesmathsmultipointonsphere) | class | [`GeometryOnSphere`](GeometryOnSphere.md) | — | 0 | Represents a multi-point on the surface of a sphere. |
| [`GPlatesMaths::InsufficientPointsForMultiPointConstructionError`](#gplatesmathsinsufficientpointsformultipointconstructionerror) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | The exception thrown when an attempt is made to create a multi-point using insufficient points. |

## Members

### `GPlatesMaths::MultiPointOnSphereImpl::CachedCalculations`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `centroid` | field | `boost::optional<UnitVector3D>` | public | — |
| `bounding_small_circle` | field | `boost::optional<BoundingSmallCircle>` | public | — |

### `GPlatesMaths::MultiPointOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<MultiPointOnSphere>` | private | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<MultiPointOnSphere\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const MultiPointOnSphere>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const MultiPointOnSphere\>. |
| `point_container_type` | typedef | `std::vector<PointOnSphere>` | public | The type of the container of points. |
| `const_iterator` | typedef | `point_container_type::const_iterator` | public | The type used to const\_iterate over the container of points. |
| `ConstructionParameterValidity` | enum | `None` | public | The possible return values from the construction-parameter validation function evaluate\_construction\_parameter\_validity. |
| `evaluate_construction_parameter_validity( ForwardIterPointOnSphere begin, ForwardIterPointOnSphere end)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. |
| `evaluate_construction_parameter_validity( const C &coll)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. coll should be a sequential STL container (list, vector, ...) of PointOnSphere. |
| `create( ForwardIterPointOnSphere begin, ForwardIterPointOnSphere end)` | method | `non_null_ptr_to_const_type` | public | Create a new MultiPointOnSphere instance on the heap from the sequence of points in the range begin / end, and return an intrusive\_ptr which points to the newly-created instance. |
| `create( const C &coll)` | method | `non_null_ptr_to_const_type` | public | Create a new MultiPointOnSphere instance on the heap from the sequence of points coll, and return an intrusive\_ptr which points to the newly-created instance. coll should be an STL container (list, vector, ...) of PointOnSphere. |
| `~MultiPointOnSphere()` | destructor | `None` | public | — |
| `get_non_null_pointer()` | method | `non_null_ptr_to_const_type` | public | Return this instance as a non-null pointer. |
| `collection()` | method | `point_container_type` | public | Get the collection as a vector |
| `test_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `accept_visitor( ConstGeometryOnSphereVisitor &visitor)` | method | `void` | public | Accept a ConstGeometryOnSphereVisitor instance. |
| `begin()` | method | `const_iterator` | public | Return the "begin" const\_iterator to iterate over the container of points which defines this multi-point. |
| `end()` | method | `const_iterator` | public | Return the "end" const\_iterator to iterate over the container of points which defines this multi-point. |
| `number_of_points()` | method | `unsigned int` | public | Return the number of points in this multi-point. |
| `is_close_to( const PointOnSphere &test_point, const real_t &closeness_inclusion_threshold, real_t &closeness)` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | public | Evaluate whether test\_point is "close" to this multi-point. |
| `operator==( const MultiPointOnSphere &other)` | operator | `bool` | public | Equality operator compares points in order. |
| `operator!=( const MultiPointOnSphere &other)` | operator | `bool` | public | Inequality operator. |
| `get_centroid` | field | `UnitVector3D` | public | Returns the sum of the points in this multipoint (normalised). |
| `get_bounding_small_circle` | field | `BoundingSmallCircle` | public | Returns the small circle that bounds this multipoint - the small circle centre is the same as calculated by get\_centroid. |
| `MultiPointOnSphere()` | constructor | `None` | private | Create an empty MultiPointOnSphere instance. |
| `s_min_num_collection_points` | field | `unsigned` | private | This is the minimum number of collection points to be passed into the 'create' function to enable creation of a multi-point. |
| `d_points` | field | `point_container_type` | private | This is the collection of points. |
| `d_cached_calculations` | field | `boost::intrusive_ptr<MultiPointOnSphereImpl::CachedCalculations>` | private | Useful calculations on the multipoint data. |

### `GPlatesMaths::InsufficientPointsForMultiPointConstructionError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InsufficientPointsForMultiPointConstructionError( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | Instantiate the exception. |
| `~InsufficientPointsForMultiPointConstructionError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `d_filename` | field | `char` | private | — |
| `d_line_num` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_min_num_collection_points` | variable | `unsigned` | — |
| `GPLATES_MATHS_MULTIPOINTONSPHERE_H` | macro | `None` | — |
| `multi_points_are_ordered_equivalent( const MultiPointOnSphere &mp1, const MultiPointOnSphere &mp2)` | function | `bool` | Determine whether the two multi-points mp1 and mp2 are equivalent when the ordering of the points is taken into account. |

## Notes

[[[PROSE notes unit=maths/MultiPointOnSphere tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 105 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 93 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 78 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 77 |
| [app-logic/GenerateVelocityDomainCitcoms](../app-logic/GenerateVelocityDomainCitcoms.md) | app-logic | 70 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 57 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 54 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 52 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 48 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 45 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 45 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 45 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 42 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 41 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 41 |
| [maths/GeneratePoints](GeneratePoints.md) | maths | 39 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 37 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](../file-io/OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 32 |
| [file-io/ReconstructionGeometryExportImpl](../file-io/ReconstructionGeometryExportImpl.md) | file-io | 30 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 29 |

*... and 123 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/MultiPointOnSphere.h
python scripts/gpq.py def GPlatesMaths::MultiPointOnSphere --body
python scripts/gpq.py uses MultiPointOnSphere --kind class
python scripts/gpq.py hier MultiPointOnSphere
```
