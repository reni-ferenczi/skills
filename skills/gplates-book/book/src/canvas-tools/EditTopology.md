# EditTopology

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 611 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/EditTopology.h` | C++ | 176 |
| `src/canvas-tools/EditTopology.cc` | C++ | 204 |

## Overview

Canvas tool for interactively selecting features to build up topologies (closed boundaries, lines, and networks). Inherits from both `QObject` and `CanvasTool` to handle Qt signals and mouse events. On activation, it determines the topology type being edited and sets a filter to show only geometries valid as topological sections, then activates the `TopologyToolsWidget`. On left-click, it finds all clicked geometries near the cursor and populates the feature table with them. On deactivation, it restores the previously focused feature to leave the UI in a consistent state.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::EditTopology`](#gplatescanvastoolsedittopology) | class | `QObject`<br>[`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to define new geometry. |

## Members

### `GPlatesCanvasTools::EditTopology`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window, GPlatesGui::FeatureTableModel &clicked_table_model_, //GPlatesGui::TopologySectionsContainer &topology_sections_container, GPlatesQtWidgets::TopologyToolsWidget &to ...` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `EditTopology( const status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window, GPlatesGui::FeatureTableModel &clicked_table_model_, //GPlatesGui::TopologySectionsContainer &topology_sections_container, GPlatesQtWidgets::TopologyToolsWidg ...` | constructor | `None` | private | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | We need to change which canvas-tool layer is shown when this canvas-tool is activated. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is currently used to pass messages to the status bar. |
| `d_clicked_table_model_ptr` | field | `GPlatesGui::FeatureTableModel` | private | This is the external table of hits which will be updated in the event that the test point hits one or more geometries. |
| `d_save_restore_focused_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The focused feature (if any) to restore upon deactivation. |
| `d_save_restore_focused_feature_geometry_property` | field | `GPlatesModel::FeatureHandle::iterator` | private | The focused feature geometry property (if any) to restore upon deactivation. |
| `d_topology_tools_widget_ptr` | field | `GPlatesQtWidgets::TopologyToolsWidget` | private | This is the TopologyToolsWidget in the Task Panel. |
| `d_feature_focus_ptr` | field | `GPlatesGui::FeatureFocus` | private | This is our reference to the Feature Focus, which we use to let the rest of the application know what the user just clicked on. |
| `d_reconstruct_graph` | field | `GPlatesAppLogic::ReconstructGraph` | private | Used when adding reconstruction geometries to the clicked feature table. |
| `d_topology_sections_filter` | field | `GPlatesGui::filter_reconstruction_geometry_predicate_type` | private | Determines which reconstructed/resolved feature geometries can be used as topological sections. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_EDIT_TOPOLOGY_H` | macro | `None` | — |

## Notes

Focused feature state is preserved: on activation, the current focused feature and its geometry property are saved; on deactivation, they are restored. This allows the user to return to their previous selection after finishing topology editing. The `d_topology_sections_filter` is set during activation based on the topology geometry type (LINE, BOUNDARY, or NETWORK) and cleared on deactivation, ensuring only valid sections are clickable while the tool is active.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/EditTopology.h
python scripts/gpq.py def GPlatesCanvasTools::EditTopology --body
python scripts/gpq.py uses EditTopology --kind class
python scripts/gpq.py hier EditTopology
```
