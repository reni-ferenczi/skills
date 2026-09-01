# CloneOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1606 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/CloneOperation.h` | C++ | 92 |
| `src/view-operations/CloneOperation.cc` | C++ | 152 |

## Overview

[[[PROSE overview unit=view-operations/CloneOperation tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::CloneOperation`](#gplatesviewoperationscloneoperation) | class | `QObject` | — | 0 | — |

## Members

### `GPlatesViewOperations::CloneOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CloneOperation( GPlatesGui::CanvasToolWorkflows &canvas_tool_workflows, GPlatesViewOperations::GeometryBuilder &digitise_geometry_builder, GPlatesViewOperations::GeometryBuilder &focused_feature_geometry_builder, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | — |
| `~CloneOperation()` | destructor | `None` | public | — |
| `clone_focused_geometry()` | method | `void` | public | — |
| `clone_focused_feature( GPlatesModel::FeatureCollectionHandle::weak_ref target_feature_collection = GPlatesModel::FeatureCollectionHandle::weak_ref())` | method | `void` | public | — |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | — |
| `d_digitise_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | — |
| `d_focused_feature_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_CLONEOPERATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/CloneOperation tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/CloneOperation.h
python scripts/gpq.py def GPlatesViewOperations::CloneOperation --body
python scripts/gpq.py uses CloneOperation --kind class
python scripts/gpq.py hier CloneOperation
```
