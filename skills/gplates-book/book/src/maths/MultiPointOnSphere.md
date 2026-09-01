# MultiPointOnSphere

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 362 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/MultiPointOnSphere.h` | C++ | 487 |
| `src/maths/MultiPointOnSphere.cc` | C++ | 252 |

## Overview

`MultiPointOnSphere` is the simplest of the four `GeometryOnSphere` implementations: an
ordered, immutable bag of `PointOnSphere` with no connectivity implied between them. It
is what a `gml:MultiPoint` property becomes when read, what velocity-domain generators
such as `GenerateVelocityDomainCitcoms` produce, and the geometry type that survives a
reconstruction unchanged point by point. Unlike `PolylineOnSphere` and
`PolygonOnSphere`, it stores the points directly rather than deriving
`GreatCircleArc`s from them, so there is no minimum of two vertices — one point is
enough, and that is the only construction constraint.

The class follows the same shape as the other geometries in `maths`, and the shape is
worth recognising because it recurs: no public constructor, creation only through the
static `create` overloads which validate first and then hand back a
`non_null_ptr_to_const_type`; no mutators at all; lifetime managed by the atomic
reference count inherited from `GeometryOnSphere` via `GPlatesUtils::ReferenceCount`;
and polymorphic access through `accept_visitor`, which dispatches to
`ConstGeometryOnSphereVisitor::visit_multi_point_on_sphere`. Immutability is what makes
the caching design below legal — see the comment on `d_cached_calculations`, which
argues that derived quantities belong *with* the geometry rather than in a side table at
a higher level, precisely so that repeated queries of the same geometry from unrelated
parts of the code can share the work.

Those derived quantities are the centroid (via `Centroid::calculate_points_centroid`)
and the bounding small circle built around it (via `BoundingSmallCircleBuilder`). They
are the entry point for the spatial acceleration used throughout the codebase —
`GeometryDistance` and `SmallCircleBounds` reject far-apart geometries with a bounds test
before touching individual points. Both are held behind a single reference-counted
`CachedCalculations` block that is not allocated at all until the first query, so a
multi-point that is only ever read back costs nothing beyond its vector of points.

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

**Invariant: at least one point.** `start_point()` and `end_point()` call `front()` and
`back()` with no bounds check and say so in their comments; only `get_point` guards, via
`GPlatesGlobal::Assert<PreconditionViolationError>`. The invariant is established by
`create`, which rejects an empty range with
`InsufficientPointsForMultiPointConstructionError`. Note that
`s_min_num_collection_points` is defined but never read — the check is the literal
`begin == end` inside `evaluate_construction_parameter_validity`. (The corresponding
constant in `PolylineOnSphere` *is* used, which is presumably why this one survives.)

**`collection()` returns the point vector by value.** Every call copies the whole
multi-point. Iterate with `begin()`/`end()`, or index with `get_point`, unless you
genuinely want a detached copy.

**The cache is `mutable` and lazily built by `const` methods, with no locking.** The
first call to `get_centroid` or `get_bounding_small_circle` heap-allocates the
`CachedCalculations` block and fills it in. Two threads doing that concurrently on the
same geometry is a data race, even though the object is otherwise immutable and shared
freely through `non_null_ptr_to_const_type` — the reference count is atomic, but this is
not.

**The constructor and destructor are deliberately out-of-line in the `.cc`.** Both
comments explain why: `boost::intrusive_ptr`'s destructor needs the complete
`MultiPointOnSphereImpl::CachedCalculations` type, which is only defined in the `.cc`.
Moving either one into the header will not compile.

**Equality is order-sensitive and epsilon-based.** `operator==` compares the two
`std::vector<PointOnSphere>`s element-wise, which means `PointOnSphere::operator==` and
therefore a dot-product-with-epsilon test per point.
`multi_points_are_ordered_equivalent` is the same comparison written out, with an
explicit size check first. Neither treats two multi-points holding the same points in a
different order as equal.

`test_proximity` carries a standing FIXME: it delegates to `is_close_to` and so returns a
`MultiPointProximityHitDetail` without an index, unable to say *which* point was hit.
`test_vertex_proximity` does the per-point loop itself and does report the index of the
closest one. The non-const `non_null_ptr_type` is private, so nothing outside the class
can obtain a mutable handle.

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
