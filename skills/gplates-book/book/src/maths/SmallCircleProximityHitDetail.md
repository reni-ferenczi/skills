# SmallCircleProximityHitDetail

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1703 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SmallCircleProximityHitDetail.h` | C++ | 96 |

## Overview

A concrete `ProximityHitDetail` subclass that records a proximity hit on a small circle. Unlike other proximity hit detail subclasses, it does not store a reference to the small circle itself; it records only the closeness value. The class uses intrusive pointer semantics and follows the same pattern as other proximity hit detail types: no stack allocation, no copying, and creation through a static `create` factory method.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::SmallCircleProximityHitDetail`](#gplatesmathssmallcircleproximityhitdetail) | class | [`ProximityHitDetail`](ProximityHitDetail.md) | — | 0 | This contains information about a proximity hit which hit a point. |

## Members

### `GPlatesMaths::SmallCircleProximityHitDetail`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const double &closeness_)` | method | `ProximityHitDetail::non_null_ptr_type` | public | FIXME: we should probably add some sort of reference to the small circle in the constructor. |
| `~SmallCircleProximityHitDetail()` | destructor | `None` | public | — |
| `accept_visitor( ProximityHitDetailVisitor &visitor)` | method | `void` | public | FIXME: not sure if these visitors are required by any of the proximity-hit code at the moment. |
| `SmallCircleProximityHitDetail( const double &closeness_)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `SmallCircleProximityHitDetail( const SmallCircleProximityHitDetail &)` | constructor | `None` | private | This constructor should never be defined, because we don't want/need to allow copy-construction. |
| `operator=` | field | `SmallCircleProximityHitDetail` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: There shouldn't be any copying; and all "assignment" should really only be assignment of one intrusive\_ptr to another. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_SMALLCIRCLEPROXIMITYHITDETAIL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/RenderedSmallCircle](../view-operations/RenderedSmallCircle.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/SmallCircleProximityHitDetail.h
python scripts/gpq.py def GPlatesMaths::SmallCircleProximityHitDetail --body
python scripts/gpq.py uses SmallCircleProximityHitDetail --kind class
python scripts/gpq.py hier SmallCircleProximityHitDetail
```
