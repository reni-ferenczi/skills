# BuildTopology

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 610 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/BuildTopology.h` | C++ | 187 |
| `src/canvas-tools/BuildTopology.cc` | C++ | 214 |

## Overview

`BuildTopology` is the canvas tool for the "build" phase of constructing a topological line, boundary or network: clicking a feature on the globe or map adds it to the clicked-features table so the user can pick it as a topological section in `GPlatesQtWidgets::TopologyToolsWidget`. Which `GPlatesAppLogic::TopologyGeometry::Type` it is building (`LINE`, `BOUNDARY` or `NETWORK`) is fixed at construction and drives `d_topology_sections_filter`, one of `GPlatesAppLogic::TopologyInternalUtils::can_use_as_resolved_line_topological_section` and its boundary/network counterparts, which `handle_left_click()` uses to restrict which reconstructed/resolved geometries under the cursor are eligible sections.

On activation the tool saves whatever feature is currently focused so it can restore it on deactivation, which lets the build tools work even while a feature is focused elsewhere in the GUI; on deactivation it restores that focus (falling back to the feature's first geometry if the saved geometry property is no longer valid) and repopulates the clicked-features table from the restored focus so the "Clicked" panel reflects it. `handle_left_control_click()` is currently just an alias for `handle_left_click()`, with a `TODO` noting the intent to also add the hit feature as a topological section directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::BuildTopology`](#gplatescanvastoolsbuildtopology) | class | `QObject`<br>[`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to define new geometry. |

## Members

### `GPlatesCanvasTools::BuildTopology`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::TopologyGeometry::Type build_topology_geometry_type, const status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window, GPlatesGui::FeatureTableModel &clicked_table_model, GPlatesQtWidgets::TopologyToolsWidget &top ...` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_control_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `BuildTopology( GPlatesAppLogic::TopologyGeometry::Type build_topology_geometry_type, const status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window, GPlatesGui::FeatureTableModel &clicked_table_model, GPlatesQtWidgets::TopologyToolsWidg ...` | constructor | `None` | private | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | We need to change which canvas-tool layer is shown when this canvas-tool is activated. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is currently used to pass messages to the status bar. |
| `d_clicked_table_model_ptr` | field | `GPlatesGui::FeatureTableModel` | private | This is the external table of hits which will be updated in the event that the test point hits one or more geometries. |
| `d_save_restore_focused_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The focused feature (if any) to restore upon deactivation. |
| `d_save_restore_focused_feature_geometry_property` | field | `GPlatesModel::FeatureHandle::iterator` | private | The focused feature geometry property (if any) to restore upon deactivation. |
| `d_topology_tools_widget_ptr` | field | `GPlatesQtWidgets::TopologyToolsWidget` | private | This is the TopologyToolsWidget in the Task Panel. |
| `d_feature_focus_ptr` | field | `GPlatesGui::FeatureFocus` | private | This is our reference to the Feature Focus, which we use to let the rest of the application know what the user just clicked on. |
| `d_reconstruct_graph` | field | `GPlatesAppLogic::ReconstructGraph` | private | Used when adding reconstruction geometries to the clicked feature table. |
| `d_build_topology_geometry_type` | field | `GPlatesAppLogic::TopologyGeometry::Type` | private | The topological geometry type this tool is building. |
| `d_topology_sections_filter` | field | `GPlatesGui::filter_reconstruction_geometry_predicate_type` | private | Determines which reconstructed/resolved feature geometries can be used as topological sections. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_BUILD_TOPOLOGY_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 39 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/BuildTopology.h
python scripts/gpq.py def GPlatesCanvasTools::BuildTopology --body
python scripts/gpq.py uses BuildTopology --kind class
python scripts/gpq.py hier BuildTopology
```
