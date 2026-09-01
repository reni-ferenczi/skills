# ProximityHitDetailVisitor

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 5 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ProximityHitDetailVisitor.h` | C++ | 114 |
| `src/maths/ProximityHitDetailVisitor.cc` | C++ | 32 |

## Overview

[[[PROSE overview unit=maths/ProximityHitDetailVisitor tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/ProximityHitDetailVisitor tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
