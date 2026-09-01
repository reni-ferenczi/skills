# CreateTopologyWidget

[Book TOC](../../../TOC.md) · [qt-widgets](../../../components/qt-widgets.md) · cluster Community 201 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/deprecated/CreateTopologyWidget.h` | C++ | 258 |
| `src/qt-widgets/deprecated/CreateTopologyWidget.cc` | C++ | 367 |
| `src/qt-widgets/deprecated/CreateTopologyWidgetUi.ui` | Qt form | 193 |

## Overview

[[[PROSE overview unit=qt-widgets/deprecated/CreateTopologyWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateTopologyWidget`](#gplatesqtwidgetscreatetopologywidget) | class | `QWidget`<br>`Ui_CreateTopologyWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateTopologyWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `geometry_collection_type` | typedef | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | — |
| `CreateTopologyWidget( GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, ViewportWindow &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `start_new_drag( const GPlatesMaths::PointOnSphere &current_oriented_position)` | method | `void` | public | — |
| `update_drag_position( const GPlatesMaths::PointOnSphere &current_oriented_position)` | method | `void` | public | — |
| `start_new_rotation_drag( const GPlatesMaths::PointOnSphere &current_oriented_position, const GPlatesMaths::PointOnSphere &oriented_center_of_viewport)` | method | `void` | public | — |
| `update_rotation_drag_position( const GPlatesMaths::PointOnSphere &current_oriented_position, const GPlatesMaths::PointOnSphere &oriented_center_of_viewport)` | method | `void` | public | — |
| `end_drag()` | method | `void` | public | — |
| `apply()` | method | `void` | public | — |
| `reset()` | method | `void` | public | — |
| `reset_adjustment()` | method | `void` | public | — |
| `set_focus( GPlatesModel::FeatureHandle::weak_ref feature_ref, GPlatesModel::ReconstructedFeatureGeometry::maybe_null_ptr_type focused_geometry)` | method | `void` | public | — |
| `handle_reconstruction_time_change( double new_time)` | method | `void` | public | — |
| `activate()` | method | `void` | public | — |
| `deactivate()` | method | `void` | public | — |
| `populate_initial_geometries()` | method | `void` | protected | Find the geometries whose RFG has a plate ID which is equal to the plate ID of the currently-focused RFG (if there is one). |
| `draw_initial_geometries()` | method | `void` | protected | Draw the initial geometries, before they've been dragged. |
| `draw_dragged_geometries()` | method | `void` | protected | Draw the initial geometries in "dragged" positions, as a result of the accumulated orientation. |
| `update_adjustment_fields()` | method | `void` | protected | Update the "Adjustment" fields in the TaskPanel pane. |
| `draw_initial_geometries_at_activation()` | method | `void` | protected | Draw the initial geometries when the canvas tool is first activated. |
| `clear_and_reset_after_reconstruction()` | method | `void` | protected | Clear geometries and reset the adjustment after a reconstruction. |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to draw rendered geometries. |
| `d_initial_geom_layer_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer to render initial geometries. |
| `d_dragged_geom_layer_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer to render dragged geometries. |
| `d_view_state_ptr` | field | `ViewportWindow` | private | — |
| `d_dialog_ptr` | field | `ApplyReconstructionPoleAdjustmentDialog` | private | The dialog presented to the user, to enable him to complete the modification of reconstruction poles. |
| `d_applicator_ptr` | field | `AdjustmentApplicator` | private | This is technically a memory leak, but since the CreateTopologyWidget will never be deleted... |
| `d_is_active` | field | `bool` | private | Whether or not this dialog is currently active. |
| `d_accum_orientation` | field | `boost::scoped_ptr<GPlatesGui::SimpleGlobeOrientation>` | private | This accumulates the rotation for us. |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The reconstruction plate ID from the reconstructed feature geometry (RFG). |
| `d_initial_geometries` | field | `geometry_collection_type` | private | The (initial) geometry of each of the RFGs whose plate IDs equal the plate ID of the currently-focused RFG (if there is one). |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `create_child_rendered_layers()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CREATETOPOLOGYWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/deprecated/CreateTopologyWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateTopologyWidget` | `QWidget` | Form | 21 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_apply` | `clicked()` | `this` | `apply()` |
| `button_reset_adjustment` | `clicked()` | `this` | `reset()` |
| `d_dialog_ptr` | `pole_sequence_choice_changed(int)` | `d_applicator_ptr` | `handle_pole_sequence_choice_changed(int)` |
| `d_dialog_ptr` | `pole_sequence_choice_cleared()` | `d_applicator_ptr` | `handle_pole_sequence_choice_cleared()` |
| `d_dialog_ptr` | `accepted()` | `d_applicator_ptr` | `apply_adjustment()` |
| `d_applicator_ptr` | `have_reconstructed()` | `this` | `clear_and_reset_after_reconstruction()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/deprecated/CreateTopologyWidget.h
python scripts/gpq.py def GPlatesQtWidgets::CreateTopologyWidget --body
python scripts/gpq.py uses CreateTopologyWidget --kind class
python scripts/gpq.py hier CreateTopologyWidget
```
