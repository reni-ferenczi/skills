# ViewportWindow

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 15 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ViewportWindow.h` | C++ | 603 |
| `src/qt-widgets/ViewportWindow.cc` | C++ | 1932 |
| `src/qt-widgets/ViewportWindowUi.ui` | Qt form | 1436 |

## Overview

[[[PROSE overview unit=qt-widgets/ViewportWindow tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/ViewportWindow tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
