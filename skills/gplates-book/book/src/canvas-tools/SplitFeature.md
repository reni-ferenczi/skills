# SplitFeature

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 364 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/SplitFeature.h` | C++ | 158 |
| `src/canvas-tools/SplitFeature.cc` | C++ | 116 |

## Overview

[[[PROSE overview unit=canvas-tools/SplitFeature tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::SplitFeature`](#gplatescanvastoolssplitfeature) | class | [`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to insert vertices into geometry. |

## Members

### `GPlatesCanvasTools::SplitFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesGui::FeatureFocus &feature_focus, GPlatesModel::ModelInterface model_interface, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryColle ...` | method | `non_null_ptr_type` | public | — |
| `~SplitFeature()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> &c ...` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `SplitFeature( const status_bar_callback_type &status_bar_callback, GPlatesGui::FeatureFocus &feature_focus, GPlatesModel::ModelInterface model_interface, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometr ...` | constructor | `None` | private | Create a InsertVertex instance. |
| `d_split_feature_geometry_operation` | field | `boost::scoped_ptr<GPlatesViewOperations::SplitFeatureGeometryOperation>` | private | Digitise operation for inserting a vertex into digitised or focused feature geometry. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_SPLITFEATURE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/SplitFeature tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/SplitFeature.h
python scripts/gpq.py def GPlatesCanvasTools::SplitFeature --body
python scripts/gpq.py uses SplitFeature --kind class
python scripts/gpq.py hier SplitFeature
```
