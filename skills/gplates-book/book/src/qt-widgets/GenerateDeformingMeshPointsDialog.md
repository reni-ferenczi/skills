# GenerateDeformingMeshPointsDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 423 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GenerateDeformingMeshPointsDialog.h` | C++ | 258 |
| `src/qt-widgets/GenerateDeformingMeshPointsDialog.cc` | C++ | 945 |
| `src/qt-widgets/GenerateDeformingMeshPointsDialogUi.ui` | Qt form | 664 |

## Overview

[[[PROSE overview unit=qt-widgets/GenerateDeformingMeshPointsDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GenerateDeformingMeshPointsDialog`](#gplatesqtwidgetsgeneratedeformingmeshpointsdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_GenerateDeformingMeshPointsDialog` | — | 0 | This dialog generates a distribution of points with initial crustal thicknesses at a past geological time. |

## Members

### `GPlatesQtWidgets::GenerateDeformingMeshPointsDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StackedWidgetPage` | enum | `None` | public | — |
| `GenerateDeformingMeshPointsDialog( GPlatesPresentation::ViewState &view_state, QWidget *parent = 0)` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | Reset the state of the dialog for a new creation process. |
| `feature_created( GPlatesModel::FeatureHandle::weak_ref feature)` | method | `void` | public | — |
| `handle_create()` | method | `void` | private | — |
| `handle_cancel()` | method | `void` | private | — |
| `handle_previous()` | method | `void` | private | — |
| `handle_next()` | method | `void` | private | — |
| `handle_points_region_mode_button( bool checked)` | method | `void` | private | — |
| `handle_left_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `handle_right_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `handle_use_global_extents_button_clicked()` | method | `void` | private | — |
| `handle_point_density_spin_box_value_changed( int value)` | method | `void` | private | — |
| `handle_visual_layer_added( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | method | `void` | private | — |
| `CurrentlyCreatingFeatureGuard` | class | `None` | private | RAII class keeps track of whether currently creating a feature or not. |
| `initialise_widgets()` | method | `void` | private | — |
| `setup_pages()` | method | `void` | private | — |
| `make_generate_points_page_current()` | method | `void` | private | — |
| `make_properties_page_current()` | method | `void` | private | — |
| `make_feature_collection_page_current()` | method | `void` | private | — |
| `display_point_density_spacing()` | method | `void` | private | — |
| `reverse_reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geom, const double &reconstruction_time, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | private | — |
| `open_topology_reconstruction_parameters_dialog( boost::weak_ptr<GPlatesPresentation::VisualLayer> reconstruct_visual_layer)` | method | `void` | private | — |
| `GPML_CRUSTAL_THICKNESS` | field | `GPlatesPropertyValues::ValueObjectType` | private | — |
| `GPML_CRUSTAL_STRETCHING_FACTOR` | field | `GPlatesPropertyValues::ValueObjectType` | private | — |
| `GPML_CRUSTAL_THINNING_FACTOR` | field | `GPlatesPropertyValues::ValueObjectType` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_plate_id_widget` | field | `EditPlateIdWidget` | private | The custom edit widget for reconstruction. |
| `d_time_period_widget` | field | `EditTimePeriodWidget` | private | The custom edit widget for GmlTimePeriod. |
| `d_name_widget` | field | `EditStringWidget` | private | The custom edit widget for XsString which we are using for the gml:name property. |
| `d_choose_feature_collection_widget` | field | `GPlatesQtWidgets::ChooseFeatureCollectionWidget` | private | The widget for choosing the feature collection. |
| `d_set_topology_reconstruction_parameters_dialog` | field | `SetTopologyReconstructionParametersDialog` | private | Used to initialise topological reconstruction for newly created reconstruct layers. |
| `d_focused_boundary_polygon` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | The polygon geometry of the focused feature (topological plate/network or static polygon). |
| `d_focused_boundary_polygon_with_rigid_block_holes` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | Same as d\_focused\_boundary\_polygon but including rigid block holes as interiors. |
| `d_currently_creating_feature` | field | `bool` | private | Is true when inside handle\_create, so we know when a new layer is created as a result of creating a new feature. |
| `d_help_scalar_type_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_point_region_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_point_distribution_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_SCALAR_TYPE_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_SCALAR_TYPE_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_POINT_REGION_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_POINT_REGION_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_POINT_DISTRIBUTION_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_POINT_DISTRIBUTION_DIALOG_TEXT` | variable | `QString` | — |
| `GPML_CRUSTAL_THICKNESS` | variable | `GPlatesPropertyValues::ValueObjectType` | — |
| `GPML_CRUSTAL_STRETCHING_FACTOR` | variable | `GPlatesPropertyValues::ValueObjectType` | — |
| `GPML_CRUSTAL_THINNING_FACTOR` | variable | `GPlatesPropertyValues::ValueObjectType` | — |
| `GPLATES_QTWIDGETS_GENERATEDEFORMINGMESHPOINTSDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/GenerateDeformingMeshPointsDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `GenerateDeformingMeshPointsDialog` | `QDialog` | Generate Deforming Mesh Points | 49 |

**Qt signal/slot connections** (22 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `focused_feature_radio_button` | `toggled(bool)` | `this` | `handle_points_region_mode_button(bool)` |
| `lat_lon_extent_radio_button` | `toggled(bool)` | `this` | `handle_points_region_mode_button(bool)` |
| `left_extents_spinbox` | `valueChanged(double)` | `this` | `handle_left_extents_spin_box_value_changed(double)` |
| `right_extents_spinbox` | `valueChanged(double)` | `this` | `handle_right_extents_spin_box_value_changed(double)` |
| `use_global_extents_button` | `clicked()` | `this` | `handle_use_global_extents_button_clicked()` |
| `point_density_spin_box` | `valueChanged(int)` | `this` | `handle_point_density_spin_box_value_changed(int)` |
| `d_plate_id_widget` | `enter_pressed()` | `d_time_period_widget` | `setFocus()` |
| `d_time_period_widget` | `enter_pressed()` | `d_name_widget` | `setFocus()` |
| `d_name_widget` | `enter_pressed()` | `button_next` | `setFocus()` |
| `button_create` | `clicked()` | `this` | `handle_create()` |
| `button_cancel` | `clicked()` | `this` | `handle_cancel()` |
| `button_previous` | `clicked()` | `this` | `handle_previous()` |
| `button_next` | `clicked()` | `this` | `handle_next()` |
| `&d_view_state.get_visual_layers()` | `layer_added(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `handle_visual_layer_added(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` |
| `d_choose_feature_collection_widget` | `item_activated()` | `button_create` | `setFocus()` |

*... and 7 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GenerateDeformingMeshPointsDialog.h
python scripts/gpq.py def GPlatesQtWidgets::GenerateDeformingMeshPointsDialog --body
python scripts/gpq.py uses GenerateDeformingMeshPointsDialog --kind class
python scripts/gpq.py hier GenerateDeformingMeshPointsDialog
```
