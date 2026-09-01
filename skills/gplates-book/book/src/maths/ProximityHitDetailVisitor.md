# ProximityHitDetailVisitor

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 5 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ProximityHitDetailVisitor.h` | C++ | 114 |
| `src/maths/ProximityHitDetailVisitor.cc` | C++ | 32 |

## Overview

A textbook Gamma95 Visitor base for the `ProximityHitDetail` hierarchy: one `visit_*` overload per concrete hit-detail type (`MultiPointProximityHitDetail`, `PointProximityHitDetail`, `PolygonProximityHitDetail`, `PolylineProximityHitDetail`, `SmallCircleProximityHitDetail`), each with an empty default body so a concrete visitor only overrides the cases it cares about. Each `visit_*` function spells out its target type in its name rather than being overloaded on parameter type, specifically to dodge C++ name hiding: a derived class that declares any function called `visit` would otherwise hide every base overload of that name, forcing it to override all of them at once.

The destructor is declared pure virtual purely to force the class to be abstract; since every `visit_*` function already carries a body, that would otherwise be the only thing stopping direct instantiation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ProximityHitDetailVisitor`](#gplatesmathsproximityhitdetailvisitor) | class | — | — | 0 | This class defines an abstract interface for a Visitor to visit ProximityHitDetail instances. |

## Members

### `GPlatesMaths::ProximityHitDetailVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ProximityHitDetailVisitor()` | destructor | `None` | public | We'll make this function pure virtual so that the class is abstract. |
| `visit_multi_point_proximity_hit_detail( MultiPointProximityHitDetail &multi_point_detail)` | method | `void` | public | Please keep these proximity hit detail types ordered alphabetically. |
| `visit_point_proximity_hit_detail( PointProximityHitDetail &point_detail)` | method | `void` | public | — |
| `visit_polygon_proximity_hit_detail( PolygonProximityHitDetail &polygon_detail)` | method | `void` | public | — |
| `visit_polyline_proximity_hit_detail( PolylineProximityHitDetail &polyline_detail)` | method | `void` | public | — |
| `visit_small_circle_proximity_hit_detail( SmallCircleProximityHitDetail &small_circle_detail)` | method | `void` | public | — |
| `operator=` | field | `ProximityHitDetailVisitor` | public | This operator should never be defined, because we don't want/need to allow copy-assignment. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_PROXIMITYHITDETAILVISITOR_H` | macro | `None` | — |

## Notes

Copy-assignment is declared but intentionally left undefined, so any attempt to copy-assign a `ProximityHitDetailVisitor` fails to link.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/MultiPointProximityHitDetail](MultiPointProximityHitDetail.md) | maths | 2 |
| [maths/PointProximityHitDetail](PointProximityHitDetail.md) | maths | 2 |
| [maths/PolygonProximityHitDetail](PolygonProximityHitDetail.md) | maths | 2 |
| [maths/PolylineProximityHitDetail](PolylineProximityHitDetail.md) | maths | 2 |
| [maths/SmallCircleProximityHitDetail](SmallCircleProximityHitDetail.md) | maths | 2 |
| [view-operations/RenderedSmallCircle](../view-operations/RenderedSmallCircle.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ProximityHitDetailVisitor.h
python scripts/gpq.py def GPlatesMaths::ProximityHitDetailVisitor --body
python scripts/gpq.py uses ProximityHitDetailVisitor --kind class
python scripts/gpq.py hier ProximityHitDetailVisitor
```
