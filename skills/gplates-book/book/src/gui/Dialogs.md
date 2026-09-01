# Dialogs

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 264 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Dialogs.h` | C++ | 465 |
| `src/gui/Dialogs.cc` | C++ | 1058 |

## Overview

`Dialogs` is the single owner and lazy factory for GPlates' thirty-five top-level
dialog windows. Every one of them is a `GPlatesQtWidgets::GPlatesDialog` — a
`QDialog` subclass that adds `pop_up()` — and every one is parented to
`ViewportWindow`, so Qt owns them and arranges the window hierarchy. What this class
adds is the *access path*: instead of `ViewportWindow` holding thirty-five members
and including thirty-five headers, it holds one `QPointer<Dialogs>` and exposes it
as `viewport_window().dialogs()`. `Dialogs.cc` is then the only translation unit in
the program that includes every dialog header; `Dialogs.h` forward-declares them all
in `GPlatesQtWidgets`. That containment of include cost is the point, and the class
comment says so, along with the caveat that the intended end state — wiring menu
actions without `ViewportWindow.cc` seeing the dialog headers at all — is not
reached yet.

Each accessor is deliberately identical boilerplate: bind a `DialogType` constant
and a `dialog_typename` typedef at the top, test whether the `QPointer` at that slot
in `d_dialogs` is null, construct on first call with `&viewport_window()` as parent,
and `dynamic_cast` the stored base pointer back to the concrete reference. The
constructor arguments are where the variety lives — most take `view_state()` or
`application_state()`, some reach further (`ColouringDialog` is handed
`viewport_window().reconstruction_view_widget().globe_and_map_widget()` and the
read-error dialog, `AboutDialog` is handed `*this`). This shape is what makes the
laziness real: a dialog is not built at startup, or even at window construction, but
the first time something asks for it.

The `pop_up_*` slots exist so a `QAction::triggered` signal can be connected
straight to `Dialogs` and defer construction until the user first triggers the menu
item. They are not uniform wrappers — they are where per-dialog behaviour that used
to sit in `ViewportWindow` now lives. `pop_up_read_error_accumulation_dialog()` also
clears the read-errors trinket in `TrinketArea`;
`pop_up_set_camera_viewpoint_dialog()` seeds the dialog from the current camera
position and pushes the accepted result back through `SceneView`;
`pop_up_set_projection_dialog()` writes the result into
`GPlatesGui::ViewportProjection` and lets the view state propagate it;
`pop_up_configure_graticules_dialog()` and its text-overlay twin run the dialog
modally over a settings object and repaint only on `QDialog::Accepted`;
`pop_up_specify_anchored_plate_id_dialog()` populates from `ApplicationState` and the
current `FeatureFocus`. The header's own warning is worth heeding: dialogs with tight
integration into the rest of the application can misbehave when their construction is
deferred this way — it names the Configure Animation Dialog's slider as a case where
behaviour differed depending on whether the dialog had yet been shown once.

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

`Dialogs` owns nothing. `d_dialogs` is a vector of `QPointer`, which is
non-owning and self-nulling; the dialogs are owned by `ViewportWindow` through Qt
parenting, and `Dialogs` itself is a `QObject` parented to `ViewportWindow` too.
The consequence is that if a dialog is destroyed by any route other than
`ViewportWindow` going away, its slot silently reverts to null and the next accessor
call constructs a brand-new instance with fresh state. Conversely, the reference an
accessor returns is only valid as long as the dialog lives; nothing hands out a
guarded handle.

The block comment above the accessors in `Dialogs.cc` is stale. It describes an
older implementation using a static member pointer per dialog; the code now uses the
`d_dialogs` vector indexed by `DialogType`. The invariants that actually hold are:
`NUM_DIALOGS` must stay last in the enum, because the constructor sizes `d_dialogs`
with it; and each accessor must pair its own `DialogType` constant with its own
`dialog_typename`. Because these functions are written by copy-and-paste, a mismatched
pair is the realistic failure mode — two accessors sharing a slot compile cleanly and
fail at run time when the `dynamic_cast<dialog_typename &>` throws `std::bad_cast`
(the cast is to a reference, so it throws rather than yielding null). Adding a dialog
means touching the enum, the forward declaration, the include list, the accessor and
usually a `pop_up_` slot.

Accessors call other accessors. `colouring_dialog()` and `hellinger_dialog()` both
construct `read_error_accumulation_dialog()` as a constructor argument, so asking for
one of them materialises the other. There is no re-entrancy guard, and no cycle
exists today, but a new dialog that took a reference to one of its own dependents
would recurse.

`application_state()`, `view_state()` and `viewport_window()` dereference their
`QPointer`s unconditionally. The pointers are guarded — Qt nulls them if the target
is destroyed — but nothing checks, so a `Dialogs` outliving `ViewportWindow` would
dereference null rather than assert. In practice `ViewportWindow` is the parent, so
this cannot happen through the normal path.

`close_all_dialogs()` calls `reject()`, not `hide()` or `close()`, on every
already-constructed dialog and skips the null slots. Any dialog that overrides
`reject()` to discard edits will run that logic here; a dialog the user has never
opened is untouched. Its one caller is `ViewportWindow::closeEvent()`, on the way
out after the close has been accepted — and the comment there records that it is not
sufficient on its own, because dialogs outside this class's registry (PyQt windows
are the example given) can still hold the application open, hence the explicit
`QCoreApplication::quit()` that follows.

Everything here is GUI-thread only: the objects `Dialogs` manages are `QWidget`s,
and several `pop_up_*` slots call `exec()`, which spins a nested event loop. A
modal `exec()` inside a slot means arbitrary other slots can run before it returns,
so anything that pops up a dialog in the middle of a state change should assume the
world may have moved by the time it continues.

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
