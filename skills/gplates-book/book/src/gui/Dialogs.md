# Dialogs

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 264 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Dialogs.h` | C++ | 465 |
| `src/gui/Dialogs.cc` | C++ | 1058 |

## Overview

[[[PROSE overview unit=gui/Dialogs tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::Dialogs`](#gplatesguidialogs) | class | `QObject`<br>`boost::noncopyable` | — | 0 | Class responsible for managing instances of GPlatesDialog in the application. |

## Members

### `GPlatesGui::Dialogs`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Dialogs( GPlatesAppLogic::ApplicationState &_application_state, GPlatesPresentation::ViewState &_view_state, GPlatesQtWidgets::ViewportWindow &_viewport_window, QObject *_parent)` | constructor | `None` | public | Much like the ApplicationState-members, GPlatesGui::Dialogs should be instantiated and kept somewhere nice. |
| `~Dialogs()` | destructor | `None` | public | — |
| `about_dialog` | field | `GPlatesQtWidgets::AboutDialog` | public | Here are all the accessors for dialogs managed by this class. |
| `age_model_manager_dialog` | field | `GPlatesQtWidgets::AgeModelManagerDialog` | public | — |
| `animate_dialog` | field | `GPlatesQtWidgets::AnimateDialog` | public | — |
| `assign_reconstruction_plate_ids_dialog` | field | `GPlatesQtWidgets::AssignReconstructionPlateIdsDialog` | public | — |
| `calculate_reconstruction_pole_dialog` | field | `GPlatesQtWidgets::CalculateReconstructionPoleDialog` | public | — |
| `choose_feature_collection_dialog` | field | `GPlatesQtWidgets::ChooseFeatureCollectionDialog` | public | — |
| `colouring_dialog` | field | `GPlatesQtWidgets::ColouringDialog` | public | — |
| `configure_canvas_tool_geometry_render_parameters_dialog` | field | `GPlatesQtWidgets::ConfigureCanvasToolGeometryRenderParametersDialog` | public | — |
| `configure_graticules_dialog` | field | `GPlatesQtWidgets::ConfigureGraticulesDialog` | public | — |
| `configure_text_overlay_dialog` | field | `GPlatesQtWidgets::ConfigureTextOverlayDialog` | public | — |
| `configure_velocity_legend_overlay_dialog` | field | `GPlatesQtWidgets::ConfigureVelocityLegendOverlayDialog` | public | — |
| `connect_wfs_dialog` | field | `GPlatesQtWidgets::ConnectWFSDialog` | public | — |
| `create_vgp_dialog` | field | `GPlatesQtWidgets::CreateVGPDialog` | public | — |
| `draw_style_dialog` | field | `GPlatesQtWidgets::DrawStyleDialog` | public | — |
| `export_animation_dialog` | field | `GPlatesQtWidgets::ExportAnimationDialog` | public | — |
| `feature_properties_dialog` | field | `GPlatesQtWidgets::FeaturePropertiesDialog` | public | — |
| `finite_rotation_calculator_dialog` | field | `GPlatesQtWidgets::FiniteRotationCalculatorDialog` | public | — |
| `generate_deforming_mesh_points_dialog` | field | `GPlatesQtWidgets::GenerateDeformingMeshPointsDialog` | public | — |
| `hellinger_dialog` | field | `GPlatesQtWidgets::HellingerDialog` | public | — |
| `kinematics_tool_dialog` | field | `GPlatesQtWidgets::KinematicGraphsDialog` | public | — |
| `log_dialog` | field | `GPlatesQtWidgets::LogDialog` | public | — |
| `manage_feature_collections_dialog` | field | `GPlatesQtWidgets::ManageFeatureCollectionsDialog` | public | — |
| `preferences_dialog` | field | `GPlatesQtWidgets::PreferencesDialog` | public | — |
| `read_error_accumulation_dialog` | field | `GPlatesQtWidgets::ReadErrorAccumulationDialog` | public | — |
| `set_camera_viewpoint_dialog` | field | `GPlatesQtWidgets::SetCameraViewpointDialog` | public | — |
| `set_projection_dialog` | field | `GPlatesQtWidgets::SetProjectionDialog` | public | — |
| `shapefile_attribute_viewer_dialog` | field | `GPlatesQtWidgets::ShapefileAttributeViewerDialog` | public | — |
| `specify_anchored_plate_id_dialog` | field | `GPlatesQtWidgets::SpecifyAnchoredPlateIdDialog` | public | — |
| `symbol_manager_dialog` | field | `GPlatesQtWidgets::SymbolManagerDialog` | public | — |
| `total_reconstruction_poles_dialog` | field | `GPlatesQtWidgets::TotalReconstructionPolesDialog` | public | — |
| `total_reconstruction_sequences_dialog` | field | `GPlatesQtWidgets::TotalReconstructionSequencesDialog` | public | — |
| `velocity_domain_citcoms_dialog` | field | `GPlatesQtWidgets::GenerateVelocityDomainCitcomsDialog` | public | — |
| `velocity_domain_lat_lon_dialog` | field | `GPlatesQtWidgets::GenerateVelocityDomainLatLonDialog` | public | — |
| `velocity_domain_terra_dialog` | field | `GPlatesQtWidgets::GenerateVelocityDomainTerraDialog` | public | — |
| `visual_layers_dialog` | field | `GPlatesQtWidgets::VisualLayersDialog` | public | — |
| `pop_up_about_dialog()` | method | `void` | public | And here are wrappers around various\_dialogs().pop\_up() so that those dialogs which support it can be lazy-loaded after the user triggers their appropriate menu item. |
| `pop_up_age_model_manager_dialog()` | method | `void` | public | — |
| `pop_up_animate_dialog()` | method | `void` | public | — |
| `pop_up_assign_reconstruction_plate_ids_dialog()` | method | `void` | public | — |
| `pop_up_calculate_reconstruction_pole_dialog()` | method | `void` | public | — |
| `pop_up_colouring_dialog()` | method | `void` | public | — |
| `pop_up_configure_canvas_tool_geometry_render_parameters_dialog()` | method | `void` | public | — |
| `pop_up_configure_graticules_dialog()` | method | `void` | public | — |
| `pop_up_configure_text_overlay_dialog()` | method | `void` | public | — |
| `pop_up_configure_velocity_legend_overlay_dialog()` | method | `void` | public | — |
| `pop_up_connect_wfs_dialog()` | method | `void` | public | — |
| `pop_up_create_vgp_dialog()` | method | `void` | public | — |
| `pop_up_draw_style_dialog()` | method | `void` | public | — |
| `pop_up_export_animation_dialog()` | method | `void` | public | — |
| `pop_up_feature_properties_dialog()` | method | `void` | public | — |
| `pop_up_finite_rotation_calculator_dialog()` | method | `void` | public | — |
| `pop_up_generate_deforming_mesh_points_dialog()` | method | `void` | public | — |
| `pop_up_hellinger_dialog()` | method | `void` | public | — |
| `pop_up_and_reposition_hellinger_dialog()` | method | `void` | public | — |
| `pop_up_kinematics_tool_dialog()` | method | `void` | public | — |
| `pop_up_log_dialog()` | method | `void` | public | — |
| `pop_up_manage_feature_collections_dialog()` | method | `void` | public | — |
| `pop_up_preferences_dialog()` | method | `void` | public | — |
| `pop_up_read_error_accumulation_dialog()` | method | `void` | public | — |
| `pop_up_set_camera_viewpoint_dialog()` | method | `void` | public | — |
| `pop_up_set_projection_dialog()` | method | `void` | public | — |
| `pop_up_shapefile_attribute_viewer_dialog()` | method | `void` | public | — |
| `pop_up_specify_anchored_plate_id_dialog()` | method | `void` | public | — |
| `pop_up_symbol_manager_dialog()` | method | `void` | public | — |
| `pop_up_total_reconstruction_poles_dialog()` | method | `void` | public | — |
| `pop_up_total_reconstruction_poles_dialog( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | — |
| `pop_up_total_reconstruction_sequences_dialog()` | method | `void` | public | — |
| `pop_up_velocity_domain_citcoms_dialog()` | method | `void` | public | — |
| `pop_up_velocity_domain_lat_lon_dialog()` | method | `void` | public | — |
| `pop_up_velocity_domain_terra_dialog()` | method | `void` | public | — |
| `pop_up_visual_layers_dialog()` | method | `void` | public | — |
| `close_all_dialogs()` | method | `void` | public | Closes any QDialog instances parented to ViewportWindow. |
| `DialogType` | enum | `None` | private | The different dialog types. |
| `application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Convenience method to get at ApplicationState. |
| `view_state` | field | `GPlatesPresentation::ViewState` | private | Convenience method to get at ViewState. |
| `viewport_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | Convenience method to get at ViewportWindow. |
| `d_application_state_ptr` | field | `QPointer<GPlatesAppLogic::ApplicationState>` | private | We keep guarded pointers to major GPlates classes to help with dialog construction. |
| `d_view_state_ptr` | field | `QPointer<GPlatesPresentation::ViewState>` | private | — |
| `d_viewport_window_ptr` | field | `QPointer<GPlatesQtWidgets::ViewportWindow>` | private | — |
| `d_dialogs` | field | `std::vector< QPointer<GPlatesQtWidgets::GPlatesDialog> >` | private | List of all dialogs managed by this class. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_DIALOGS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/Dialogs tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](FileIOFeedback.md) | gui | 32 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 28 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 27 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 21 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 20 |
| [gui/UnsavedChangesTracker](UnsavedChangesTracker.md) | gui | 13 |
| [qt-widgets/ReconstructLayerOptionsWidget](../qt-widgets/ReconstructLayerOptionsWidget.md) | qt-widgets | 12 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 11 |
| [gui/TrinketArea](TrinketArea.md) | gui | 10 |
| [deprecated/controls/File](../deprecated/controls/File.md) | deprecated | 9 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](../qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 7 |
| [deprecated/controls/Reconstruct](../deprecated/controls/Reconstruct.md) | deprecated | 6 |
| [qt-widgets/ReconstructionLayerOptionsWidget](../qt-widgets/ReconstructionLayerOptionsWidget.md) | qt-widgets | 6 |
| [qt-widgets/AboutDialog](../qt-widgets/AboutDialog.md) | qt-widgets | 5 |
| [gui/HellingerCanvasToolWorkflow](HellingerCanvasToolWorkflow.md) | gui | 4 |
| [presentation/Application](../presentation/Application.md) | presentation | 4 |
| [qt-widgets/VisualLayersWidget](../qt-widgets/VisualLayersWidget.md) | qt-widgets | 4 |
| [deprecated/controls/Dialogs](../deprecated/controls/Dialogs.md) | deprecated | 3 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 3 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 2 |

*... and 8 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Dialogs.h
python scripts/gpq.py def GPlatesGui::Dialogs --body
python scripts/gpq.py uses Dialogs --kind class
python scripts/gpq.py hier Dialogs
```
