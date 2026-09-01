# ModifyGeometryState

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 1684 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ModifyGeometryState.h` | C++ | 77 |

## Overview

A simple Qt-signal relay that bridges the `ModifyGeometryWidget` UI in the task panel with canvas tools that edit geometry. It broadcasts snap-to-vertices configuration—whether nearby vertices should be snapped, the snapping distance threshold, and which plate to filter by—to all interested listeners. The sole method `set_snap_vertices_setup` emits the `snap_vertices_setup_changed` signal with the new settings, which canvas tools like `MoveVertexGeometryOperation` connect to in order to update their behaviour.

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

*None.*

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
