# QueryProximityThreshold

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 564 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/QueryProximityThreshold.h` | C++ | 64 |

## Overview

[[[PROSE overview unit=view-operations/QueryProximityThreshold tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::QueryProximityThreshold`](#gplatesviewoperationsqueryproximitythreshold) | class | — | — | 4 | Interface for querying the proximity threshold based on position on globe. |

## Members

### `GPlatesViewOperations::QueryProximityThreshold`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~QueryProximityThreshold()` | destructor | `None` | public | — |
| `current_proximity_inclusion_threshold( const GPlatesMaths::PointOnSphere &click_pos_on_globe)` | method | `double` | public | The proximity inclusion threshold is a measure of how close a geometry must be to a click-point be considered "hit" by the click. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_QUERYPROXIMITYTHRESHOLD_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/QueryProximityThreshold tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 3 |
| [qt-widgets/SceneView](../qt-widgets/SceneView.md) | qt-widgets | 3 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 2 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 1 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/QueryProximityThreshold.h
python scripts/gpq.py def GPlatesViewOperations::QueryProximityThreshold --body
python scripts/gpq.py uses QueryProximityThreshold --kind class
python scripts/gpq.py hier QueryProximityThreshold
```
