# CloneOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1606 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/CloneOperation.h` | C++ | 92 |
| `src/view-operations/CloneOperation.cc` | C++ | 152 |

## Overview

A utility for duplicating the focused feature or just its geometry. `clone_focused_geometry()` copies the geometry from a focused feature into the digitise `GeometryBuilder` and switches to the appropriate digitise tool so the user can edit the copy. `clone_focused_feature()` makes a full clone of the feature with all its properties and adds it to a feature collection (defaulting to the feature's own collection), then focuses the new feature.

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

*None.*

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
