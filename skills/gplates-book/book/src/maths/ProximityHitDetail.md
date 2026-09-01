# ProximityHitDetail

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 772 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ProximityHitDetail.h` | C++ | 141 |
| `src/maths/ProximityHitDetail.cc` | C++ | 32 |

## Overview

This is the answer type for "did the user hit this geometry, and how squarely". Every
`GeometryOnSphere` subclass implements `test_proximity` and `test_vertex_proximity` against a
`ProximityCriteria` (a test point plus an `AngularExtent` threshold) and returns a
`maybe_null_ptr_type`: null for a miss, or a heap-allocated hit detail for a hit. The base class
carries only the two things every hit has — a closeness value and an optional vertex index — while
each concrete subclass (`PointProximityHitDetail`, `MultiPointProximityHitDetail`,
`PolylineProximityHitDetail`, `PolygonProximityHitDetail`, `SmallCircleProximityHitDetail`) adds a
counted pointer back to the geometry that was hit and dispatches through
`ProximityHitDetailVisitor`. So the caller gets a self-describing hit it can rank without knowing
the geometry type, and can recover the type later by visiting.

The design is why picking on the globe works the way it does: `RenderedGeometryProximity` in
`view-operations` collects hit details from every rendered geometry under the mouse and sorts them
by `closeness()` alone, then the canvas tools visit the winner to find out what they actually hit.
Nothing in this unit computes proximity — the geometry classes and `GreatCircleArc::is_close_to` do
that; this is purely the shared result vocabulary.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ProximityHitDetail`](#gplatesmathsproximityhitdetail) | class | [`GPlatesUtils::ReferenceCount<ProximityHitDetail>`](../utils/ReferenceCount.md) | — | 5 | Derivations of this abstract base class will contain extra information about a proximity hit -- for example, the specific vertex (point) or segment (GCA) of a polyline which was hit. |

## Members

### `GPlatesMaths::ProximityHitDetail`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ProximityHitDetail>` | public | A convenience typedef for boost::intrusive\_ptr\<ProximityHitDetail\>. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ProximityHitDetail, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ProximityHitDetail, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `null` | field | `maybe_null_ptr_type` | public | This is used when there was no proximity hit, and thus no detail. |
| `ProximityHitDetail( const double &closeness_, const boost::optional<unsigned int> &index_)` | constructor | `None` | public | Construct a ProximityHitDetail instance. |
| `~ProximityHitDetail()` | destructor | `None` | public | — |
| `accept_visitor( ProximityHitDetailVisitor &)` | method | `void` | public | — |
| `d_closeness` | field | `double` | private | The "closeness" of the hit. |
| `d_index` | field | `boost::optional<unsigned int>` | private | The index of the vertex hit, (for vertex tests) |
| `ProximityHitDetail( const ProximityHitDetail &)` | constructor | `None` | private | This constructor should never be defined, because we don't want/need to allow copy-construction. |
| `operator=` | field | `ProximityHitDetail` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: There shouldn't be any copying; and all "assignment" should really only be assignment of one intrusive\_ptr to another. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `null` | variable | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | — |
| `GPLATES_MATHS_PROXIMITYHITDETAIL_H` | macro | `None` | — |
| `make_maybe_null_ptr( const ProximityHitDetail::non_null_ptr_type &non_null_ptr)` | function | `ProximityHitDetail::maybe_null_ptr_type` | — |

## Notes

**Closeness is a cosine, not a distance.** It is the dot product of the test point with the closest
point on the geometry, so *larger* means *closer*, and `ProximityCriteria::closeness_inclusion_threshold`
is likewise the cosine of the threshold angle. `RenderedGeometryProximity` sorts hits with `>`.
Never compare it as if it were an angle or an arc length.

**`index()` is usually `boost::none`.** The subclass `create` functions default it to none, and only
the `test_vertex_proximity` paths supply one. What it indexes is decided by the geometry that filled
it in — `PolygonOnSphere::test_vertex_proximity`, for example, only scans the exterior ring, so its
index is an exterior-ring vertex index and never reaches an interior ring.

**Two pointer types, on purpose.** `non_null_ptr_type` uses
`GPlatesUtils::NullIntrusivePointerHandler` and is what the subclass `create` functions return;
`maybe_null_ptr_type` is a plain `boost::intrusive_ptr` and is what the `test_proximity` interface
returns, because it has to be able to express "no hit". `make_maybe_null_ptr` is the conversion, and
`ProximityHitDetail::null` is the shared miss value — note it is a namespace-scope object defined in
the `.cc`, so it is not safe to depend on during another translation unit's static initialisation.

**Instances are heap-only and non-copyable.** The copy constructor and assignment operator are
declared private and never defined (the pre-C++11 idiom), and the subclass constructors are private
behind static `create`. Ownership is by intrusive reference count, so hold one through a smart
pointer and never delete it yourself; the virtual destructor makes destruction through the base
pointer correct.

**`accept_visitor` is non-const**, unlike the geometry-side `ConstGeometryOnSphereVisitor`. A hit
detail you only hold as `const` cannot be visited, and the visit methods receive a non-const
reference to the detail.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PointOnSphere](PointOnSphere.md) | maths | 18 |
| [maths/MultiPointOnSphere](MultiPointOnSphere.md) | maths | 16 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 16 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 16 |
| [view-operations/RenderedGeometry](../view-operations/RenderedGeometry.md) | view-operations | 13 |
| [view-operations/RenderedColouredTriangleSurfaceMesh](../view-operations/RenderedColouredTriangleSurfaceMesh.md) | view-operations | 9 |
| [maths/PointProximityHitDetail](PointProximityHitDetail.md) | maths | 8 |
| [maths/SmallCircleProximityHitDetail](SmallCircleProximityHitDetail.md) | maths | 8 |
| [view-operations/RenderedColouredEdgeSurfaceMesh](../view-operations/RenderedColouredEdgeSurfaceMesh.md) | view-operations | 8 |
| [view-operations/RenderedGeometryProximity](../view-operations/RenderedGeometryProximity.md) | view-operations | 8 |
| [property-values/GpmlIrregularSampling](../property-values/GpmlIrregularSampling.md) | property-values | 7 |
| [view-operations/RenderedGeometryImpl](../view-operations/RenderedGeometryImpl.md) | view-operations | 7 |
| [maths/MultiPointProximityHitDetail](MultiPointProximityHitDetail.md) | maths | 6 |
| [maths/PolygonProximityHitDetail](PolygonProximityHitDetail.md) | maths | 6 |
| [maths/PolylineProximityHitDetail](PolylineProximityHitDetail.md) | maths | 6 |
| [view-operations/RenderedMultiReconstructionGeometry](../view-operations/RenderedMultiReconstructionGeometry.md) | view-operations | 6 |
| [view-operations/RenderedPolygonOnSphere](../view-operations/RenderedPolygonOnSphere.md) | view-operations | 6 |
| [view-operations/RenderedPolylineOnSphere](../view-operations/RenderedPolylineOnSphere.md) | view-operations | 6 |
| [view-operations/RenderedReconstructionGeometry](../view-operations/RenderedReconstructionGeometry.md) | view-operations | 6 |
| [maths/GeometryOnSphere](GeometryOnSphere.md) | maths | 5 |

*... and 25 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ProximityHitDetail.h
python scripts/gpq.py def GPlatesMaths::ProximityHitDetail --body
python scripts/gpq.py uses ProximityHitDetail --kind class
python scripts/gpq.py hier ProximityHitDetail
```
