# ClickGeometry

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 281 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ClickGeometry.h` | C++ | 220 |
| `src/canvas-tools/ClickGeometry.cc` | C++ | 129 |

## Overview

`ClickGeometry` is the default "pick a feature" canvas tool: clicking near a rendered geometry finds the reconstruction geometries under the cursor, populates the clicked-features table, and focuses one of them via `GPlatesGui::FeatureFocus`, letting the rest of the GUI (property inspector, highlighting) react to what the user selected. `handle_left_click()` does the finding and table population through `GPlatesGui::get_clicked_geometries()` and `add_clicked_geometries_to_feature_table()`, filtered by `d_filter_reconstruction_geometry_predicate` (defaulted to `default_filter_reconstruction_geometry_predicate`); `handle_shift_left_click()` layers one behaviour on top — after the same click handling, if a feature ends up focused it opens the `GPlatesQtWidgets::FeaturePropertiesDialog` via `choose_query_widget_and_open()`, so shift-click is "click and immediately inspect."

The tool's own rendered layer is shown only while it is active: `handle_activation()` calls `set_active()` and `handle_deactivation()` calls `set_active(false)` on the layer `RenderedGeometryCollection::get_main_rendered_layer(d_main_rendered_layer_type)` returns — its own layer only; the state of the other layers is left alone. The focused-feature highlight is only meaningful while this tool (or one built on it) is selected.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ClickGeometry`](#gplatescanvastoolsclickgeometry) | class | [`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to focus features by clicking on them. |

## Members

### `GPlatesCanvasTools::ClickGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &focused_feature_geometry_builder, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets: ...` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `ClickGeometry( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &focused_feature_geometry_builder, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtW ...` | constructor | `None` | private | Create a ClickGeometry instance. |
| `d_focused_feature_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | The focused feature geometry builder. |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | We need to change which canvas-tool layer is shown when this canvas-tool is activated. |
| `d_main_rendered_layer_type` | field | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_view_state_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the view state which is used to obtain the reconstruction root. |
| `d_clicked_table_model_ptr` | field | `GPlatesGui::FeatureTableModel` | private | This is the external table of hits which will be updated in the event that the test point hits one or more geometries. |
| `d_fp_dialog_ptr` | field | `GPlatesQtWidgets::FeaturePropertiesDialog` | private | This is the dialog box which we will be populating in response to a feature query. |
| `d_feature_focus_ptr` | field | `GPlatesGui::FeatureFocus` | private | This is our reference to the Feature Focus, which we use to let the rest of the application know what the user just clicked on. |
| `d_reconstruct_graph` | field | `GPlatesAppLogic::ReconstructGraph` | private | Used when adding reconstruction geometries to the clicked feature table. |
| `d_filter_reconstruction_geometry_predicate` | field | `GPlatesGui::filter_reconstruction_geometry_predicate_type` | private | Used to filter clicked geometries before adding to the feature table. |
| `d_clicked_geom_seq` | field | `std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type>` | private | The sequence of clicked geometries from the last user click. |
| `d_save_restore_focused_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The focused feature (if any) from the last user click. |
| `d_save_restore_focused_feature_geometry_property` | field | `GPlatesModel::FeatureHandle::iterator` | private | The focused feature geometry property (if any) to restore when this canvas tool workflow re-activates. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_CLICKGEOMETRY_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 17 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 13 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/ClickGeometry.h
python scripts/gpq.py def GPlatesCanvasTools::ClickGeometry --body
python scripts/gpq.py uses ClickGeometry --kind class
python scripts/gpq.py hier ClickGeometry
```
