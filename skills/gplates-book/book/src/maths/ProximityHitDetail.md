# ProximityHitDetail

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 772 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ProximityHitDetail.h` | C++ | 141 |
| `src/maths/ProximityHitDetail.cc` | C++ | 32 |

## Overview

[[[PROSE overview unit=maths/ProximityHitDetail tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/ProximityHitDetail tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
