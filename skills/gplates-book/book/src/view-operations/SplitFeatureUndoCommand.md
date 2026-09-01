# SplitFeatureUndoCommand

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 922 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/SplitFeatureUndoCommand.h` | C++ | 103 |
| `src/view-operations/SplitFeatureUndoCommand.cc` | C++ | 345 |

## Overview

A `QUndoCommand` that implements splitting a polyline feature into two separate features at a specified point. When redo is called, it clones the original feature and divides its geometry at the given point index, creating a new feature that holds the second half of the line while the original feature retains the first half. Optionally inserts a new point at the split location, with support for reverse-reconstructing it back to present day if needed. The command wraps geometry creation and model notifications to ensure a clean undo/redo cycle. On undo, it restores the original geometry to the old feature and removes the newly created feature from the collection.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::SplitFeatureUndoCommand`](#gplatesviewoperationssplitfeatureundocommand) | class | `QUndoCommand` | — | 0 | Command to split a feature. |

## Members

### `GPlatesViewOperations::SplitFeatureUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SplitFeatureUndoCommand( GPlatesGui::FeatureFocus &feature_focus, GPlatesModel::ModelInterface model_interface, GeometryBuilder::PointIndex point_index_to_insert_at, boost::optional<const GPlatesMaths::PointOnSphere> &oriented_pos_on_globe, QUndoCommand *parent = 0)` | constructor | `None` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_model_interface` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_point_index_to_insert_at` | field | `GeometryBuilder::PointIndex` | private | — |
| `d_oriented_pos_on_globe` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_old_geometry_property` | field | `boost::optional<GPlatesModel::TopLevelProperty::non_null_ptr_type>` | private | — |
| `d_feature_collection_ref` | field | `GPlatesModel::FeatureCollectionHandle::weak_ref` | private | — |
| `d_new_feature` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | — |
| `d_old_feature` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | — |
| `d_nothing_has_been_done` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_SPLITFEATUREUNDOCOMMAND_H` | macro | `None` | — |

## Notes

Currently hard-coded to split polyline geometries only; other geometry types are not yet supported. The implementation assumes the focused feature has exactly one geometry property. The `d_nothing_has_been_done` flag tracks whether a split actually occurred (e.g., avoiding splits at start/end points). After the model notification guard is released during undo, reconstruction happens synchronously and data members should not be accessed.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/SplitFeatureUndoCommand.h
python scripts/gpq.py def GPlatesViewOperations::SplitFeatureUndoCommand --body
python scripts/gpq.py uses SplitFeatureUndoCommand --kind class
python scripts/gpq.py hier SplitFeatureUndoCommand
```
