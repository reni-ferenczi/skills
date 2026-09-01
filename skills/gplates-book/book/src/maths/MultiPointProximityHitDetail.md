# MultiPointProximityHitDetail

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1327 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/MultiPointProximityHitDetail.h` | C++ | 100 |

## Overview

Encapsulates proximity-hit information for interactions with `MultiPointOnSphere` geometries. When a proximity query (such as a mouse click on the globe) strikes a collection of points, this class stores the reference to the `MultiPointOnSphere` and the distance (closeness value). Like other `ProximityHitDetail` subclasses, it is always heap-allocated and uses intrusive pointers for lifetime management.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::MultiPointProximityHitDetail`](#gplatesmathsmultipointproximityhitdetail) | class | [`ProximityHitDetail`](ProximityHitDetail.md) | — | 0 | This contains information about a proximity hit which hit a multi-point. |

## Members

### `GPlatesMaths::MultiPointProximityHitDetail`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_, const double &closeness_, const boost::optional<unsigned int> &index_ = boost::none)` | method | `ProximityHitDetail::non_null_ptr_type` | public | — |
| `~MultiPointProximityHitDetail()` | destructor | `None` | public | — |
| `accept_visitor( ProximityHitDetailVisitor &visitor)` | method | `void` | public | — |
| `d_multi_point` | field | `MultiPointOnSphere::non_null_ptr_to_const_type` | private | — |
| `MultiPointProximityHitDetail( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_, const double &closeness_, const boost::optional<unsigned int> &index_)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `MultiPointProximityHitDetail( const MultiPointProximityHitDetail &)` | constructor | `None` | private | This constructor should never be defined, because we don't want/need to allow copy-construction. |
| `operator=` | field | `MultiPointProximityHitDetail` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: There shouldn't be any copying; and all "assignment" should really only be assignment of one intrusive\_ptr to another. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_MULTIPOINTPROXIMITYHITDETAIL_H` | macro | `None` | — |

## Notes

Always heap-allocated via the static `create()` method; copy construction and assignment are explicitly deleted. Uses intrusive reference counting for shared ownership across the rendering and interaction systems.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/MultiPointOnSphere](MultiPointOnSphere.md) | maths | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/MultiPointProximityHitDetail.h
python scripts/gpq.py def GPlatesMaths::MultiPointProximityHitDetail --body
python scripts/gpq.py uses MultiPointProximityHitDetail --kind class
python scripts/gpq.py hier MultiPointProximityHitDetail
```
