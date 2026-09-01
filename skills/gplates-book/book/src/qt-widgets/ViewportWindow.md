# ViewportWindow

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 15 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ViewportWindow.h` | C++ | 603 |
| `src/qt-widgets/ViewportWindow.cc` | C++ | 1932 |
| `src/qt-widgets/ViewportWindowUi.ui` | Qt form | 1436 |

## Overview

The GPlates main window, and the third tier of the application's state trio:
`GPlatesPresentation::Application` is a singleton holding an
`GPlatesAppLogic::ApplicationState`, a `GPlatesPresentation::ViewState` and one
`ViewportWindow`, in that dependency order — app-logic knows nothing of the view,
the view knows nothing of the widgets, and this class sits on top of both. Its
constructor takes references to the other two and it stores them; it does not own
them, and it outlives nothing.

Its actual job is narrower than its size suggests. `ViewportWindowUi.ui` supplies
the menu bar and the whole `QAction` inventory; this class supplies the wiring,
which is why more than half the `.cc` is the `connect_*_menu_actions()` family —
one function per menu, deliberately kept in menu order. Almost every action's
receiver is somewhere else: `GPlatesGui::Dialogs` (which owns every major dialog
so they do not clutter this class), `GPlatesGui::FileIOFeedback` (all file and
project opening and saving), `GPlatesGui::UnsavedChangesTracker`,
`GPlatesGui::SessionMenu`, `GPlatesGui::ImportMenu`, `GPlatesGui::UtilitiesMenu`,
`GPlatesGui::DockState`, `GPlatesGui::FullScreenMode`, `GPlatesGui::TrinketArea`.
The visible canvas is `ReconstructionViewWidget`, set as the central widget;
`globe_canvas()` and `map_view()` are plain forwarders to it. So if you are here
because a menu item does the wrong thing, this file usually tells you where the
work happens rather than doing it.

What it genuinely owns is the state the canvas tools and the task panel share:
`GPlatesCanvasTools::GeometryOperationState`,
`GPlatesCanvasTools::ModifyGeometryState`,
`GPlatesCanvasTools::MeasureDistanceState`, the
`GPlatesGui::CanvasToolWorkflows` registry, and the
`GPlatesViewOperations::CloneOperation` / `DeleteFeatureOperation` pair that back
the Edit menu. These are held by `boost::scoped_ptr` rather than `QPointer`
precisely because they are not `QObject`s parented to the window; the header spells
out that convention. The class also mediates between tools and the UI in both
directions — `handle_canvas_tool_activated()` switches the `TaskPanel` to the tab
matching the newly active tool, and the `canvas_tool_status_message()` callback
handed to `CanvasToolWorkflows::initialise()` lets a tool write to the status bar
with a globe-or-map-appropriate suffix.

Two recipes are maintained as comments in the code and are the intended starting
point for the most common changes here: the numbered list at the top of
`connect_menu_actions()` for adding a menu action, and the one in
`set_up_task_panel_actions()` for putting that action on the Feature tab's button
box.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ViewportWindow`](#gplatesqtwidgetsviewportwindow) | class | `QMainWindow`<br>`Ui_ViewportWindow` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ViewportWindow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewportWindow( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | — |
| `~ViewportWindow()` | destructor | `None` | public | — |
| `load_project( const QString &project_filename)` | method | `void` | public | Loads the specified project file as a convenient alternative to having to explicitly load it by accessing the GUI. |
| `load_feature_collections( const QStringList &filenames)` | method | `void` | public | Loads the specified feature collection files as a convenient alternative to having to explicitly load them by accessing the GUI. |
| `display()` | method | `void` | public | Shows the main window. |
| `get_application_state` | field | `GPlatesAppLogic::ApplicationState` | public | Returns the application state. |
| `get_view_state` | field | `GPlatesPresentation::ViewState` | public | Returns the view state. |
| `reconstruction_view_widget` | field | `ReconstructionViewWidget` | public | — |
| `canvas_tool_bar_dock_widget` | field | `CanvasToolBarDockWidget` | public | — |
| `search_results_dock_widget` | field | `SearchResultsDockWidget` | public | — |
| `globe_canvas` | field | `GlobeCanvas` | public | — |
| `map_view` | field | `MapView` | public | — |
| `dialogs` | field | `GPlatesGui::Dialogs` | public | Accessor for the Dialogs class which manages all the instances of major dialogs/windows that would ordinarily hang off of ViewportWindow and clutter things up. |
| `file_io_feedback` | field | `GPlatesGui::FileIOFeedback` | public | — |
| `canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | public | — |
| `trinket_area` | field | `GPlatesGui::TrinketArea` | public | — |
| `task_panel_ptr()` | method | `TaskPanel` | public | Get a pointer to the TaskPanel \*/ |
| `import_menu` | field | `GPlatesGui::ImportMenu` | public | — |
| `utilities_menu` | field | `GPlatesGui::UtilitiesMenu` | public | — |
| `status_message( const QString &message, int timeout = 20000)` | method | `void` | public | — |
| `enable_or_disable_feature_actions( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | — |
| `handle_load_symbol_file()` | method | `void` | public | — |
| `handle_unload_symbol_file()` | method | `void` | public | — |
| `update_tools_and_status_message()` | method | `void` | public | — |
| `handle_read_errors( const GPlatesFileIO::ReadErrorAccumulation &new_read_errors)` | method | `void` | public | — |
| `install_gui_debug_menu()` | method | `void` | public | Add secret menu filled with actions aid GUI-related debugging. |
| `hide_symbol_menu()` | method | `void` | public | — |
| `hide_python_menu()` | method | `void` | public | — |
| `closeEvent(QCloseEvent *close_event)` | method | `void` | protected | A reimplementation of QWidget::closeEvent() to allow closure to be postponed. |
| `dragEnterEvent( QDragEnterEvent *ev)` | method | `void` | protected | Reimplementation of drag/drop events so we can handle users dragging files onto GPlates main window. |
| `dropEvent( QDropEvent *ev)` | method | `void` | protected | Reimplementation of drag/drop events so we can handle users dragging files onto GPlates main window. |
| `showEvent( QShowEvent *ev)` | method | `void` | protected | — |
| `connect_menu_actions()` | method | `void` | private | Connects all the Signal/Slot relationships for ViewportWindow toolbar buttons and menu items. |
| `connect_file_menu_actions()` | method | `void` | private | — |
| `connect_edit_menu_actions()` | method | `void` | private | — |
| `connect_view_menu_actions()` | method | `void` | private | — |
| `connect_features_menu_actions()` | method | `void` | private | — |
| `connect_reconstruction_menu_actions()` | method | `void` | private | — |
| `connect_utilities_menu_actions()` | method | `void` | private | — |
| `connect_tools_menu_actions()` | method | `void` | private | — |
| `connect_window_menu_actions()` | method | `void` | private | — |
| `connect_help_menu_actions()` | method | `void` | private | — |
| `populate_gmenu_from_menubar()` | method | `void` | private | Copies the menu structure found in ViewportWindow's menu bar into the special full-screen-mode 'GMenu' button. |
| `set_up_task_panel_actions()` | method | `void` | private | Configures the ActionButtonBox inside the Feature tab of the Task Panel with some of the QActions that ViewportWindow has on the menu bar. |
| `set_window_title( boost::optional<QString> project_filename = boost::none)` | method | `void` | private | — |
| `set_visual_layers_dialog_visibility( bool visible)` | method | `void` | private | — |
| `handle_window_menu_about_to_show()` | method | `void` | private | — |
| `enable_static_point_display()` | method | `void` | private | — |
| `enable_static_line_display()` | method | `void` | private | — |
| `enable_static_polygon_display()` | method | `void` | private | — |
| `enable_static_multipoint_display()` | method | `void` | private | — |
| `enable_velocity_arrow_display()` | method | `void` | private | — |
| `enable_topological_section_display()` | method | `void` | private | — |
| `enable_topological_line_display()` | method | `void` | private | — |
| `enable_topological_polygon_display()` | method | `void` | private | — |
| `enable_topological_network_display()` | method | `void` | private | — |
| `enable_raster_display()` | method | `void` | private | — |
| `enable_3d_scalar_field_display()` | method | `void` | private | — |
| `enable_scalar_coverage_display()` | method | `void` | private | — |
| `enable_all_geometries_display()` | method | `void` | private | — |
| `handle_render_settings_changed()` | method | `void` | private | — |
| `enable_stars_display()` | method | `void` | private | — |
| `handle_move_camera_up()` | method | `void` | private | — |
| `handle_move_camera_down()` | method | `void` | private | — |
| `handle_move_camera_left()` | method | `void` | private | — |
| `handle_move_camera_right()` | method | `void` | private | — |
| `handle_rotate_camera_clockwise()` | method | `void` | private | — |
| `handle_rotate_camera_anticlockwise()` | method | `void` | private | — |
| `handle_reset_camera_orientation()` | method | `void` | private | — |
| `handle_canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | method | `void` | private | — |
| `handle_changed_project_filename( boost::optional<QString> project_filename)` | method | `void` | private | — |
| `show_menu_item_status_tip_in_status_bar()` | method | `void` | private | — |
| `pop_up_import_raster_dialog()` | method | `void` | private | — |
| `pop_up_import_raster_dialog( bool time_dependent_raster)` | method | `void` | private | — |
| `pop_up_import_time_dependent_raster_dialog()` | method | `void` | private | — |
| `pop_up_import_scalar_field_3d_dialog()` | method | `void` | private | — |
| `handle_colour_scheme_delegator_changed()` | method | `void` | private | — |
| `handle_visual_layer_added( size_t index)` | method | `void` | private | — |
| `open_new_window()` | method | `void` | private | — |
| `pop_up_background_colour_picker()` | method | `void` | private | — |
| `clone_feature_with_dialog()` | method | `void` | private | — |
| `update_undo_action_tooltip()` | method | `void` | private | — |
| `update_redo_action_tooltip()` | method | `void` | private | — |
| `open_online_documentation()` | method | `void` | private | — |
| `pop_up_python_console()` | method | `void` | private | — |
| `open_dataset_webpage()` | method | `void` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Some pointers below are QPointer and some are boost::scoped\_ptr. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_geometry_operation_state_ptr` | field | `boost::scoped_ptr<GPlatesCanvasTools::GeometryOperationState>` | private | The state targeted by geometry operation canvas tools and displayed in task panel. |
| `d_modify_geometry_state` | field | `boost::scoped_ptr<GPlatesCanvasTools::ModifyGeometryState>` | private | The state targeted by canvas tools that modify geometry and displayed in task panel. |
| `d_measure_distance_state_ptr` | field | `boost::scoped_ptr<GPlatesCanvasTools::MeasureDistanceState>` | private | The state targeted by measure distance canvas tool and displayed in task panel. |
| `d_canvas_tool_workflows` | field | `boost::scoped_ptr<GPlatesGui::CanvasToolWorkflows>` | private | The selected canvas tool state. |
| `d_clone_operation_ptr` | field | `boost::scoped_ptr<GPlatesViewOperations::CloneOperation>` | private | For cloning a feature. |
| `d_delete_feature_operation_ptr` | field | `boost::scoped_ptr<GPlatesViewOperations::DeleteFeatureOperation>` | private | For deleting a feature. |
| `d_dialogs_ptr` | field | `QPointer<GPlatesGui::Dialogs>` | private | Manages all the major dialogs that would otherwise clutter up ViewportWindow. |
| `d_full_screen_mode` | field | `QPointer<GPlatesGui::FullScreenMode>` | private | Handles transitions to/from fullscreen mode. |
| `d_trinket_area_ptr` | field | `QPointer<GPlatesGui::TrinketArea>` | private | Manages the icons in the status bar |
| `d_unsaved_changes_tracker_ptr` | field | `QPointer<GPlatesGui::UnsavedChangesTracker>` | private | Tracks changes to saved/unsaved status of files and manages user notification of same. |
| `d_file_io_feedback_ptr` | field | `QPointer<GPlatesGui::FileIOFeedback>` | private | Wraps file loading and saving, opening dialogs appropriately for filenames and error feedback. |
| `d_session_menu_ptr` | field | `QPointer<GPlatesGui::SessionMenu>` | private | Manages the Open Recent Session menu. |
| `d_import_menu_ptr` | field | `QPointer<GPlatesGui::ImportMenu>` | private | Encapsulates logic regarding the Import submenu of the File menu. |
| `d_utilities_menu_ptr` | field | `QPointer<GPlatesGui::UtilitiesMenu>` | private | Allows Python scripts to be run from the Utilities menu. |
| `d_dock_state_ptr` | field | `QPointer<GPlatesGui::DockState>` | private | Deals with all the micro-management of the ViewportWindow's docks. |
| `d_search_results_dock_ptr` | field | `QPointer<SearchResultsDockWidget>` | private | A tabbed search results dock widget. |
| `d_canvas_tools_dock_ptr` | field | `QPointer<CanvasToolBarDockWidget>` | private | A tabbed toolbar for the canvas tools. |
| `d_reconstruction_view_widget_ptr` | field | `QPointer<ReconstructionViewWidget>` | private | The central widget in the main window containing everything except the menubar, search results dock and canvas tools dock. |
| `d_task_panel_ptr` | field | `QPointer<TaskPanel>` | private | Depends on FeatureFocus, Model, topology sections container. |
| `d_undo_action_ptr` | field | `QPointer<QAction>` | private | — |
| `d_redo_action_ptr` | field | `QPointer<QAction>` | private | — |
| `d_inside_update_undo_action_tooltip` | field | `bool` | private | To prevent infinite loops. |
| `d_inside_update_redo_action_tooltip` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `STATUS_MESSAGE_SUFFIX_FOR_GLOBE` | variable | `char` | — |
| `STATUS_MESSAGE_SUFFIX_FOR_MAP` | variable | `char` | — |
| `canvas_tool_status_message( GPlatesQtWidgets::ViewportWindow &viewport_window, const char *message)` | function | `void` | — |
| `add_shortcut_to_tooltip( QAction *action)` | function | `void` | — |
| `GPLATES_QTWIDGETS_VIEWPORTWINDOW_H` | macro | `None` | — |

## Notes

**Construction order is fragile and partly undocumented by the type system.**
The member initialiser list can only build things that do not need the Designer
form, because `setupUi(this)` runs in the constructor body. That is why
`d_import_menu_ptr`, `d_utilities_menu_ptr`, the two dock widgets and
`d_task_panel_ptr` start as `NULL` and are assigned later. Within the body the
code comments call the ordering "precarious" and pin it down: canvas tools dock,
then task panel, then `CanvasToolWorkflows::initialise()` — because each reaches
back through `*this` for the previous one. `d_dialogs_ptr` is built first among
the members for the same reason, its constructor being the one that touches
nothing else.

**`ViewState` holds a back-pointer to this window that is null until mid-way
through this constructor.** `get_view_state().set_other_view_state(*this)` is the
first statement after `setupUi()`; `ViewState::get_other_view_state()`
dereferences the pointer with no null check. Anything that runs earlier — during
`ViewState` construction, or in a member of this class constructed before that
line — must not call it. The header comment marks the whole mechanism as a
temporary hack pending the migration of non-widget state into `ViewState`.

**Use `display()`, not `show()`.** `display()` calls `show()` and then does the
work that needs a visible window: repositioning the visual layers dialog relative
to its now-laid-out parent, and `CanvasToolWorkflows::activate()`, which will not
activate the default tool while the canvas is invisible. `showEvent()` similarly
defers `update_tools_and_status_message()` until visibility, because
`ReconstructionViewWidget::globe_is_active()` is only meaningful then. Note that
`showEvent()` does not chain to `QMainWindow::showEvent()`.

**`closeEvent()` is the application's entire shutdown sequence, not just a window
close.** It runs the unsaved-changes prompt (and aborts the close if the user
declines), records the session unless changes are being discarded, closes all
dialogs, and calls `QCoreApplication::quit()` explicitly because stray non-Qt
windows such as PyQt consoles would otherwise keep the process alive. It then
calls `RenderedGeometryCollection::begin_update_all_registered_collections()` and
deliberately never balances it — this suppresses rendered-geometry update
signalling for the rest of the process lifetime and is documented as reducing
shutdown from minutes to seconds on large files. Do not "fix" the missing
`end_update` call, and do not expect rendered-geometry updates to work after a
close event. Because the sequence lives in an event handler, programmatic
termination must go through `ViewportWindow::close()` rather than quitting
directly.

**The undo/redo actions are not from the form.** They are created by the global
`GPlatesViewOperations::UndoRedo` singleton's `QUndoGroup` and spliced into the
Edit menu in place of `action_Undo_Placeholder` / `action_Redo_Placeholder`,
inheriting the placeholders' shortcut and icon. The
`d_inside_update_undo_action_tooltip` flags exist because the tooltip updater
calls `QAction::setToolTip()`, which re-emits `QAction::changed()`, which is the
signal that invoked it. Anything you add to those slots must stay inside the
guard.

**One-shot and order-sensitive connections.** `handle_visual_layer_added()`
disconnects itself after firing, so the layers dialog auto-opens only for the
first layer of a session. `populate_gmenu_from_menubar()` copies the top-level
menu actions into the full-screen "GMenu" once, by `findChild` on the object name;
menus created after that call will not appear in full-screen mode.

**Ownership convention.** The header states the rule the members follow:
`QPointer` where the object is a `QObject` parented to this window and Qt will
delete it, `boost::scoped_ptr` where nothing else owns it. `QPointer` is also
being used for its guarded-pointer behaviour, but the comment is explicit that
Qt's detection of premature deletion is a safety net and not to be relied on. The
empty destructor exists only so the `scoped_ptr` members see complete types.

**Smaller surprises.** `dialogs()` is declared `const` yet hands out a non-const
reference. `open_new_window()` does not create a second `ViewportWindow` — it
launches a whole new GPlates process via `QProcess::startDetached`.
`status_message()` rewrites the substring "ctrl" to the command glyph on macOS, so
messages containing that word incidentally will be mangled there.
`install_gui_debug_menu()` is triggered only by the `--debug-gui` command-line
switch and leaks its `GuiDebug` deliberately into Qt's ownership.

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/ChangeLightDirectionGlobe](../canvas-tools/ChangeLightDirectionGlobe.md) | canvas-tools | 16 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 15 |
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 14 |
| [qt-widgets/deprecated/CreateTopologyWidget](deprecated/CreateTopologyWidget.md) | qt-widgets | 14 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 9 |
| [canvas-tools/MovePoleGlobe](../canvas-tools/MovePoleGlobe.md) | canvas-tools | 8 |
| [canvas-tools/MovePoleMap](../canvas-tools/MovePoleMap.md) | canvas-tools | 7 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 7 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 6 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 6 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 6 |
| [presentation/Application](../presentation/Application.md) | presentation | 6 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 5 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 5 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 5 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 5 |
| [qt-widgets/SearchResultsDockWidget](SearchResultsDockWidget.md) | qt-widgets | 5 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 5 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 4 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 4 |

*... and 57 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ViewportWindow` | `QMainWindow` | GPlates | 123 |

**Qt signal/slot connections** (98 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&canvas_tool_workflows()` | `canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` | `this` | `handle_canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` |
| `&get_view_state().get_feature_focus()` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `enable_or_disable_feature_actions(GPlatesGui::FeatureFocus &)` |
| `&get_application_state().get_feature_collection_file_io()` | `handle_read_errors( const GPlatesFileIO::ReadErrorAccumulation &)` | `this` | `handle_read_errors( const GPlatesFileIO::ReadErrorAccumulation &)` |
| `d_modify_geometry_state.get()` | `snap_vertices_setup_changed(bool,double,bool,GPlatesModel::integer_plate_id_type)` | `d_reconstruction_view_widget_ptr` | `setFocus()` |
| `get_view_state().get_colour_scheme_delegator().get()` | `changed()` | `this` | `handle_colour_scheme_delegator_changed()` |
| `&(get_view_state().get_visual_layers())` | `layer_added(size_t)` | `this` | `handle_visual_layer_added(size_t)` |
| `&(get_view_state().get_session_management())` | `changed_project_filename(boost::optional<QString>)` | `this` | `handle_changed_project_filename(boost::optional<QString>)` |
| `action_Open_Feature_Collection` | `triggered()` | `d_file_io_feedback_ptr` | `open_files()` |
| `action_Open_Project` | `triggered()` | `d_file_io_feedback_ptr` | `open_project()` |
| `action_Save_Project` | `triggered()` | `d_file_io_feedback_ptr` | `save_project()` |
| `action_Save_Project_As` | `triggered()` | `d_file_io_feedback_ptr` | `save_project_as()` |
| `action_Clear_Session` | `triggered()` | `d_file_io_feedback_ptr` | `clear_session()` |
| `action_Open_Project` | `hovered()` | `this` | `show_menu_item_status_tip_in_status_bar()` |
| `action_Save_Project` | `hovered()` | `this` | `show_menu_item_status_tip_in_status_bar()` |
| `action_Save_Project_As` | `hovered()` | `this` | `show_menu_item_status_tip_in_status_bar()` |

*... and 83 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ViewportWindow.h
python scripts/gpq.py def GPlatesQtWidgets::ViewportWindow --body
python scripts/gpq.py uses ViewportWindow --kind class
python scripts/gpq.py hier ViewportWindow
```
