# PolylineProximityHitDetail

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1328 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolylineProximityHitDetail.h` | C++ | 101 |

## Overview

A concrete `ProximityHitDetail` subclass that records a proximity hit on a `PolylineOnSphere`. It holds the polyline that was hit and inherits the closeness value (distance metric) and an optional vertex index from its base class. The class uses intrusive pointer semantics for memory management and cannot be copied or stack-allocated; instances must be created via the static `create` factory method.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolylineProximityHitDetail`](#gplatesmathspolylineproximityhitdetail) | class | [`ProximityHitDetail`](ProximityHitDetail.md) | — | 0 | This contains information about a proximity hit which hit a polyline. |

## Members

### `GPlatesMaths::PolylineProximityHitDetail`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( PolylineOnSphere::non_null_ptr_to_const_type polyline_, const double &closeness_, const boost::optional<unsigned int> &index_ = boost::none)` | method | `ProximityHitDetail::non_null_ptr_type` | public | — |
| `~PolylineProximityHitDetail()` | destructor | `None` | public | — |
| `accept_visitor( ProximityHitDetailVisitor &visitor)` | method | `void` | public | — |
| `d_polyline` | field | `PolylineOnSphere::non_null_ptr_to_const_type` | private | — |
| `PolylineProximityHitDetail( PolylineOnSphere::non_null_ptr_to_const_type polyline_, const double &closeness_, const boost::optional<unsigned int> &index_)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `PolylineProximityHitDetail( const PolylineProximityHitDetail &)` | constructor | `None` | private | This constructor should never be defined, because we don't want/need to allow copy-construction. |
| `operator=` | field | `PolylineProximityHitDetail` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: There shouldn't be any copying; and all "assignment" should really only be assignment of one intrusive\_ptr to another. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_POLYLINEPROXIMITYHITDETAIL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 3 |
| [view-operations/RenderedPolylineOnSphere](../view-operations/RenderedPolylineOnSphere.md) | view-operations | 2 |
| [view-operations/RenderedColouredPolylineOnSphere](../view-operations/RenderedColouredPolylineOnSphere.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolylineProximityHitDetail.h
python scripts/gpq.py def GPlatesMaths::PolylineProximityHitDetail --body
python scripts/gpq.py uses PolylineProximityHitDetail --kind class
python scripts/gpq.py hier PolylineProximityHitDetail
```
