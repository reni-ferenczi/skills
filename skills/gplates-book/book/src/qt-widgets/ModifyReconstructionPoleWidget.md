# ModifyReconstructionPoleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 117 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ModifyReconstructionPoleWidget.h` | C++ | 359 |
| `src/qt-widgets/ModifyReconstructionPoleWidget.cc` | C++ | 1179 |
| `src/qt-widgets/ModifyReconstructionPoleWidgetUi.ui` | Qt form | 250 |

## Overview

[[[PROSE overview unit=qt-widgets/ModifyReconstructionPoleWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ModifyReconstructionPoleWidget`](#gplatesqtwidgetsmodifyreconstructionpolewidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_ModifyReconstructionPoleWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ModifyReconstructionPoleWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `reconstructed_feature_geometry_collection_type` | typedef | `std::vector<GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_to_const_type>` | public | Typedef for a sequence of ReconstructedFeatureGeometry objects. |
| `ModifyReconstructionPoleWidget( MovePoleWidget &move_pole_widget, GPlatesPresentation::ViewState &view_state, ViewportWindow &viewport_window, QAction *clear_action, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ModifyReconstructionPoleWidget()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `get_clear_action_text()` | method | `QString` | public | — |
| `clear_action_enabled()` | method | `bool` | public | — |
| `handle_clear_action_triggered()` | method | `void` | public | — |
| `start_new_drag( const GPlatesMaths::PointOnSphere &current_oriented_position)` | method | `void` | public | — |
| `update_drag_position( const GPlatesMaths::PointOnSphere &current_oriented_position)` | method | `void` | public | — |
| `start_new_rotation_drag( const GPlatesMaths::PointOnSphere &current_oriented_position, const GPlatesMaths::PointOnSphere &oriented_center_of_viewport)` | method | `void` | public | — |
| `update_rotation_drag_position( const GPlatesMaths::PointOnSphere &current_oriented_position, const GPlatesMaths::PointOnSphere &oriented_center_of_viewport)` | method | `void` | public | — |
| `end_drag()` | method | `void` | public | — |
| `apply()` | method | `void` | public | — |
| `reset()` | method | `void` | public | — |
| `reset_adjustment()` | method | `void` | public | — |
| `change_highlight_children_checkbox_state( int new_checkbox_state)` | method | `void` | public | — |
| `set_focus( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | — |
| `handle_reconstruction()` | method | `void` | public | — |
| `activate()` | method | `void` | public | — |
| `deactivate()` | method | `void` | public | — |
| `get_focused_feature_geometry()` | method | `boost::optional<GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_to_const_type>` | protected | Returns focused feature RFG (if there is one). |
| `populate_initial_geometries()` | method | `void` | protected | Find the geometries whose RFG has a plate ID which is equal to the plate ID of the currently-focused RFG (if there is one). |
| `draw_initial_geometries()` | method | `void` | protected | Draw the initial geometries, before they've been dragged. |
| `draw_dragged_geometries()` | method | `void` | protected | Draw the initial geometries in "dragged" positions, as a result of the accumulated orientation. |
| `draw_adjustment_pole()` | method | `void` | protected | Draw the adjustment pole location (from Move Pole canvas tool) if enabled. |
| `update_adjustment_fields()` | method | `void` | protected | Update the "Adjustment" fields in the TaskPanel pane. |
| `draw_initial_geometries_at_activation()` | method | `void` | protected | Draw the initial geometries when the canvas tool is first activated. |
| `clear_and_reset_after_reconstruction()` | method | `void` | protected | Clear geometries and reset the adjustment after a reconstruction. |
| `react_adjustment_pole_changed()` | method | `void` | protected | Re-draw the adjustment pole when it changes location. |
| `handle_layer_modified()` | method | `void` | protected | Re-populate the visible RFGs when a layer is made visible/invisible. |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | Manages reconstructions. |
| `d_move_pole_widget` | field | `MovePoleWidget` | private | Used to get the adjustment pole location. |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to draw rendered geometries. |
| `d_initial_geom_layer_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer to render initial geometries. |
| `d_dragged_geom_layer_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer to render dragged geometries. |
| `d_adjustment_pole_layer_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer to render the optional adjustment pole location. |
| `d_dialog_ptr` | field | `ApplyReconstructionPoleAdjustmentDialog` | private | The dialog presented to the user, to enable him to complete the modification of reconstruction poles. |
| `d_applicator_ptr` | field | `boost::scoped_ptr<AdjustmentApplicator>` | private | — |
| `d_should_display_children` | field | `bool` | private | Whether or not the children of the selected plate id should be displayed during a drag |
| `d_drag_start` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | The start-point of a latitude-constraining drag. |
| `d_is_active` | field | `bool` | private | Whether or not this dialog is currently active. |
| `d_accum_orientation` | field | `boost::scoped_ptr<GPlatesGui::SimpleGlobeOrientation>` | private | This accumulates the rotation for us. |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The reconstruction plate ID from the reconstructed feature geometry (RFG). |
| `d_reconstruction_tree` | field | `boost::optional<GPlatesAppLogic::ReconstructionTree::non_null_ptr_to_const_type>` | private | The reconstruction tree used to reconstruct the focused feature geometry. |
| `d_reconstructed_feature_geometries` | field | `reconstructed_feature_geometry_collection_type` | private | The RFGs whose plate IDs equal the plate ID of the currently-focused RFG (if there is one). |
| `d_view_state_ptr` | field | `GPlatesPresentation::ViewState` | private | View state for extracting VGP visibility settings. |
| `make_signal_slot_connections( GPlatesPresentation::ViewState &view_state)` | method | `void` | private | — |
| `create_child_rendered_layers()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_closest_point_on_horizon( const GPlatesMaths::PointOnSphere &oriented_point_within_horizon, const GPlatesMaths::PointOnSphere &oriented_center_of_viewport)` | function | `boost::optional<GPlatesMaths::PointOnSphere>` | Return the closest point on the horizon to oriented\_point\_within\_horizon. |
| `get_closest_point_on_equator_of_pole( const GPlatesMaths::PointOnSphere &point, const GPlatesMaths::PointOnSphere &pole)` | function | `boost::optional<GPlatesMaths::PointOnSphere>` | Return the closest point on the equator (of pole pole) to point. |
| `add_child_edges_to_collection( const GPlatesAppLogic::ReconstructionTree::Edge &edge, std::vector<GPlatesModel::integer_plate_id_type> &child_plate_id_collection)` | function | `void` | — |
| `add_children_to_geometry_collection( std::vector<GPlatesModel::integer_plate_id_type> &child_plate_id_collection, const GPlatesModel::integer_plate_id_type plate_id, const GPlatesAppLogic::ReconstructionTree &tree)` | function | `void` | — |
| `display_collection( const std::vector<GPlatesModel::integer_plate_id_type> &collection)` | function | `void` | — |
| `examine_trs( std::vector<GPlatesQtWidgets::ApplyReconstructionPoleAdjustmentDialog::PoleSequenceInfo> & sequence_choices, GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder &trs_plate_id_finder, GPlatesFeatureVisitors::TotalReconstructionSequenceTimePeriodFinder &trs_time_period_finder, GPlatesModel::inte ...` | function | `void` | — |
| `find_trses( std::vector<GPlatesQtWidgets::ApplyReconstructionPoleAdjustmentDialog::PoleSequenceInfo> &sequence_choices, GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder &trs_plate_id_finder, GPlatesFeatureVisitors::TotalReconstructionSequenceTimePeriodFinder &trs_time_period_finder, GPlatesModel::intege ...` | function | `void` | This finds all the TRSes (total reconstruction sequences) in the supplied reconstruction whose fixed or moving ref-frame plate ID matches our plate ID of interest. |
| `GPLATES_QTWIDGETS_MODIFYRECONSTRUCTIONPOLEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ModifyReconstructionPoleWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/ManipulatePole](../canvas-tools/ManipulatePole.md) | canvas-tools | 16 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 6 |
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ModifyReconstructionPoleWidget` | `QWidget` | Form | 16 |

**Qt signal/slot connections** (10 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_apply` | `clicked()` | `this` | `apply()` |
| `d_dialog_ptr` | `pole_sequence_choice_changed(int)` | `d_applicator_ptr.get()` | `handle_pole_sequence_choice_changed(int)` |
| `d_dialog_ptr` | `pole_sequence_choice_cleared()` | `d_applicator_ptr.get()` | `handle_pole_sequence_choice_cleared()` |
| `d_dialog_ptr` | `accepted()` | `d_applicator_ptr.get()` | `apply_adjustment()` |
| `d_applicator_ptr.get()` | `have_reconstructed()` | `this` | `clear_and_reset_after_reconstruction()` |
| `&view_state.get_feature_focus()` | `focus_changed( GPlatesGui::FeatureFocus &)` | `this` | `set_focus( GPlatesGui::FeatureFocus &)` |
| `d_application_state_ptr` | `reconstructed(GPlatesAppLogic::ApplicationState &)` | `this` | `handle_reconstruction()` |
| `checkbox_highlight_children` | `stateChanged(int)` | `this` | `change_highlight_children_checkbox_state(int)` |
| `&d_move_pole_widget` | `pole_changed(boost::optional<GPlatesMaths::PointOnSphere>)` | `this` | `react_adjustment_pole_changed()` |
| `&view_state.get_visual_layers()` | `layer_modified(size_t)` | `this` | `handle_layer_modified()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ModifyReconstructionPoleWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ModifyReconstructionPoleWidget --body
python scripts/gpq.py uses ModifyReconstructionPoleWidget --kind class
python scripts/gpq.py hier ModifyReconstructionPoleWidget
```
