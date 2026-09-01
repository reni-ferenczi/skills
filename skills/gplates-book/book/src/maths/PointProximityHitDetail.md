# PointProximityHitDetail

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 904 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PointProximityHitDetail.h` | C++ | 98 |

## Overview

Encapsulates proximity-hit information for interactions with single-point geometries (`PointOnSphere`). When a proximity query hits a point, this class stores a copy of the point and the distance (closeness value). Like other `ProximityHitDetail` subclasses, it is always heap-allocated and uses intrusive pointers for lifetime management.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PointProximityHitDetail`](#gplatesmathspointproximityhitdetail) | class | [`ProximityHitDetail`](ProximityHitDetail.md) | — | 0 | This contains information about a proximity hit which hit a point. |

## Members

### `GPlatesMaths::PointProximityHitDetail`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const PointOnSphere &point_, const double &closeness_, const boost::optional<unsigned int> &index_ = boost::none)` | method | `ProximityHitDetail::non_null_ptr_type` | public | — |
| `~PointProximityHitDetail()` | destructor | `None` | public | — |
| `accept_visitor( ProximityHitDetailVisitor &visitor)` | method | `void` | public | — |
| `d_point` | field | `PointOnSphere` | private | — |
| `PointProximityHitDetail( const PointOnSphere &point_, const double &closeness_, const boost::optional<unsigned int> &index_ = boost::none)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `PointProximityHitDetail( const PointProximityHitDetail &)` | constructor | `None` | private | This constructor should never be defined, because we don't want/need to allow copy-construction. |
| `operator=` | field | `PointProximityHitDetail` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: There shouldn't be any copying; and all "assignment" should really only be assignment of one intrusive\_ptr to another. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_POINTPROXIMITYHITDETAIL_H` | macro | `None` | — |

## Notes

Always heap-allocated via the static `create()` method; copy construction and assignment are explicitly deleted. Uses intrusive reference counting for shared ownership across the rendering and interaction systems.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PointOnSphere](PointOnSphere.md) | maths | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PointProximityHitDetail.h
python scripts/gpq.py def GPlatesMaths::PointProximityHitDetail --body
python scripts/gpq.py uses PointProximityHitDetail --kind class
python scripts/gpq.py hier PointProximityHitDetail
```
