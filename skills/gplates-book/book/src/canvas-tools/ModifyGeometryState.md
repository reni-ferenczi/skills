# ModifyGeometryState

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 1684 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ModifyGeometryState.h` | C++ | 77 |

## Overview

[[[PROSE overview unit=canvas-tools/ModifyGeometryState tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ModifyGeometryState`](#gplatescanvastoolsmodifygeometrystate) | class | `QObject` | — | 0 | This is used to communicate between ModifyGeometryWidget (and associated sub-widgets) and canvas tools that can modify either digitised or focused feature geometry. |

## Members

### `GPlatesCanvasTools::ModifyGeometryState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `set_snap_vertices_setup( bool should_check_nearby_vertices, double threshold, bool should_use_plate_id, GPlatesModel::integer_plate_id_type plate_id)` | method | `void` | public | Sets user-provided move-nearby-vertex information (from the task panel tab). |
| `snap_vertices_setup_changed( bool should_check_nearby_vertices, double threshold, bool should_use_plate_id, GPlatesModel::integer_plate_id_type plate_id)` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_MODIFYGEOMETRYSTATE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/ModifyGeometryState tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SnapNearbyVerticesWidget](../qt-widgets/SnapNearbyVerticesWidget.md) | qt-widgets | 4 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 2 |
| [view-operations/MoveVertexGeometryOperation](../view-operations/MoveVertexGeometryOperation.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/ModifyGeometryState.h
python scripts/gpq.py def GPlatesCanvasTools::ModifyGeometryState --body
python scripts/gpq.py uses ModifyGeometryState --kind class
python scripts/gpq.py hier ModifyGeometryState
```
