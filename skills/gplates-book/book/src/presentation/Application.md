# Application

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 1132 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/Application.h` | C++ | 170 |
| `src/presentation/Application.cc` | C++ | 148 |

## Overview

`Application` is the top-level singleton that owns the three layers of GPlates
state and wires them together at startup: `GPlatesAppLogic::ApplicationState`
(model and file state), `GPlatesPresentation::ViewState` (how it is displayed)
and `GPlatesQtWidgets::ViewportWindow` (the main window). It constructs them in
that order — `ViewState` is given the `ApplicationState`, `ViewportWindow` is
given both — then runs `initialise()` to make the cross-cutting signal/slot
connections that `ViewportWindow` itself should not have to know about, such as
routing `GPlatesGui::FeatureFocus::focused_feature_modified` into the search
results dock and the shapefile attribute viewer, and connecting the anchored
plate id dialog and the create-feature dialog back into
`ApplicationState::reconstruct()`. It also performs the first reconstruction,
initialises the animation controller's default time range and starts up
`SessionManagement`, all after the three constructors have run.

Because `Application` sits above `ApplicationState` and depends on
`ViewportWindow` and other GUI classes, code at the application-logic level or
below must never include or reference it. It also hosts a `GPlatesGui::CommandServer`
and, lazily, a `GPlatesGui::ExternalSyncController` used to let GPlates act as
master or slave to another running application instance.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::Application`](#gplatespresentationapplication) | class | [`GPlatesUtils::Singleton<Application>`](../utils/Singleton.md) | — | 0 | Stores the application state, the view state and ViewportWindow. |

## Members

### `GPlatesPresentation::Application`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `enable_syncing_with_external_applications( bool gplates_is_master = false)` | method | `void` | public | Enable communication between GPlates and other (external) applications. |
| `set_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time with the presentation-level animation controller. |
| `initialise()` | method | `void` | private | Perform any initialisation that doesn't necessarily belong in the constructors of ViewportWindow, ViewState or ApplicationState. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_main_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | — |
| `d_cmd_server` | field | `GPlatesGui::CommandServer` | private | — |
| `d_external_sync_controller` | field | `boost::optional<GPlatesGui::ExternalSyncController>` | private | Controller for external communication. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_APPLICATION_H` | macro | `None` | — |
| `current_time()` | function | `double` | — |

## Notes

`Application` is a `GPlatesUtils::Singleton` created with the "public
constructor" variant specifically so a single instance can live on the C++
stack (typically in `main()`), giving it deterministic destruction when that
scope exits rather than leaving it as a leaked global. `initialise()` relies on
construction order: `d_application_state`, `d_view_state`, `d_main_window` and
`d_cmd_server` must already exist because it wires signals between objects
reachable from `d_main_window` and slots on `d_application_state`. The
`d_external_sync_controller` is constructed lazily, on the first call to
`enable_syncing_with_external_applications()`, not at startup.

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 3 |
| [gui/GenericColourScheme](../gui/GenericColourScheme.md) | gui | 3 |
| [presentation/DeprecatedSessionRestore](DeprecatedSessionRestore.md) | presentation | 3 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 2 |
| [gui/GPlatesQApplication](../gui/GPlatesQApplication.md) | gui | 2 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 2 |
| [api/PyApplication](../api/PyApplication.md) | api | 1 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 1 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 1 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 1 |
| [presentation/ProjectSession](ProjectSession.md) | presentation | 1 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 1 |

## Related

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_view_state.get_feature_focus()` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `&d_main_window.search_results_dock_widget()` | `highlight_focused_feature_in_table(GPlatesGui::FeatureFocus &)` |
| `&d_view_state.get_feature_focus()` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `&d_main_window.dialogs().shapefile_attribute_viewer_dialog()` | `update()` |
| `&d_main_window.dialogs().specify_anchored_plate_id_dialog()` | `value_changed(GPlatesModel::integer_plate_id_type)` | `&d_application_state` | `set_anchored_plate_id(GPlatesModel::integer_plate_id_type)` |
| `&d_main_window.task_panel_ptr()->digitisation_widget().get_create_feature_dialog()` | `feature_created(GPlatesModel::FeatureHandle::weak_ref)` | `&d_application_state` | `reconstruct()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/Application.h
python scripts/gpq.py def GPlatesPresentation::Application --body
python scripts/gpq.py uses Application --kind class
python scripts/gpq.py hier Application
```
