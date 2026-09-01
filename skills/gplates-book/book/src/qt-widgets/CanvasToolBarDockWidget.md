# CanvasToolBarDockWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 684 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CanvasToolBarDockWidget.h` | C++ | 272 |
| `src/qt-widgets/CanvasToolBarDockWidget.cc` | C++ | 1124 |
| `src/qt-widgets/CanvasToolBarDockWidgetUi.ui` | Qt form | 930 |

## Overview

Tabbed toolbar organizer for canvas editing tools grouped by workflow (digitization, topology, pole manipulation, etc.). Each workflow tab contains a toolbar with mutually-exclusive tool buttons managed by a `QActionGroup`. Listens to `CanvasToolWorkflows` for tool enable/disable and activation events, updating button states accordingly. Supports keyboard shortcuts for both individual tools and entire workflows, and provides tool actions suitable for inclusion in the main menu bar. Emits `canvas_tool_triggered_by_user()` to distinguish explicit user selections from automatic tool changes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CanvasToolBarDockWidget`](#gplatesqtwidgetscanvastoolbardockwidget) | class | [`DockWidget`](DockWidget.md)<br>`Ui_CanvasToolBarDockWidget` | — | 0 | A tabbed canvas toolbar that groups canvas tools into 'workflows' such as digitisation, topology, etc. |

## Members

### `GPlatesQtWidgets::CanvasToolBarDockWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanvasToolBarDockWidget( GPlatesGui::DockState &dock_state, GPlatesGui::CanvasToolWorkflows &canvas_tool_workflows, ViewportWindow &main_window, const QSize &tool_icon_size = QSize(35,35))` | constructor | `None` | public | — |
| `get_workflow_tool_menu_name( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow)` | method | `QString` | public | Returns the name to use for the canvas tool sub-menu for the specified workflow. |
| `get_workflow_tool_menu_actions( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow)` | method | `QList<QAction *>` | public | Returns the list of tool actions, for the specified workflow, for use in a menu. |
| `canvas_tool_triggered_by_user( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | method | `void` | public | Emitted when a canvas tool action is triggered by the user (as opposed to automatically by GPlates). |
| `use_small_canvas_tool_icons( bool use_small_icons)` | method | `void` | public | Use dimension 16 or 35 icons depending on use\_small\_icons. |
| `set_icon_size( const QSize &icon_size)` | method | `void` | public | Sets the icon size for each tool bar tab. |
| `handle_tool_action_triggered()` | method | `void` | private | — |
| `handle_tool_shortcut_triggered()` | method | `void` | private | — |
| `handle_workflow_shortcut_triggered()` | method | `void` | private | — |
| `handle_workflow_tab_changed( int workflow_tab_index)` | method | `void` | private | — |
| `handle_canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool, bool enable)` | method | `void` | private | — |
| `handle_canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | method | `void` | private | — |
| `Workflow` | struct | `None` | private | Manages information for a specific canvas tool workflow. |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | Manages the canvas tool workflows and tool activation (and which tools are enabled). |
| `d_workflows` | field | `std::vector<Workflow>` | private | A list of all workflows. |
| `d_tool_icon_regular_size` | field | `QSize` | private | The tool icon size to use when not using the small size; |
| `set_up_workflows()` | method | `void` | private | — |
| `set_up_view_workflow()` | method | `void` | private | — |
| `set_up_feature_inspection_workflow()` | method | `void` | private | — |
| `set_up_digitisation_workflow()` | method | `void` | private | — |
| `set_up_topology_workflow()` | method | `void` | private | — |
| `set_up_pole_manipulation_workflow()` | method | `void` | private | — |
| `set_up_small_circle_workflow()` | method | `void` | private | — |
| `set_up_hellinger_workflow()` | method | `void` | private | — |
| `create_workflow( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow_type, const QString &workflow_menu_name, QWidget *tab_widget, QWidget *tool_bar_placeholder_widget)` | method | `Workflow` | private | — |
| `add_tool_action_to_workflow( Workflow &workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool, const QAction *tool_action)` | method | `void` | private | — |
| `set_up_workflow_tab_icons()` | method | `void` | private | — |
| `set_up_canvas_tool_shortcuts()` | method | `void` | private | — |
| `add_canvas_tool_shortcut( GPlatesGui::CanvasToolWorkflows::ToolType tool, QAction *shortcut_tool_action)` | method | `void` | private | — |
| `set_up_canvas_workflow_shortcuts()` | method | `void` | private | — |
| `add_canvas_workflow_shortcut( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, const QKeySequence &shortcut_key_sequence)` | method | `void` | private | — |
| `get_tool_action( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | method | `QAction` | private | — |
| `choose_canvas_tool_selected_by_user( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, boost::optional<GPlatesGui::CanvasToolWorkflows::ToolType> tool = boost::none)` | method | `void` | private | — |
| `connect_to_workflow_tab_changed( bool connect_to_workflow = true)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `TOOL_ACTION_DATA_LIST_WORKFLOW_INDEX` | variable | `unsigned int` | Index into QAction data() list representing the canvas tool workflow. |
| `TOOL_ACTION_DATA_LIST_TOOL_INDEX` | variable | `unsigned int` | Index into QAction data() list representing the canvas tool. |
| `get_workflow_tool_from_action( QAction *tool_action)` | function | `std::pair< GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType>` | Returns the workflow/tool associated with the specified tool action. |
| `is_tool_action( QAction *tool_action, GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | function | `bool` | Returns true if tool\_action corresponds to the specified workflow/tool. |
| `MACOS_STYLESHEET` | variable | `QString` | — |
| `GPLATES_QT_WIDGETS_CANVASTOOLBARDOCKWIDGET_H` | macro | `None` | — |

## Notes

Each workflow maintains a `QActionGroup` with a single checked action at any time. The widget does not own the tool actions themselves (those belong to the main window or CanvasToolWorkflows), but it manages the creation and lifetime of the toolbars and action groups.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 5 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CanvasToolBarDockWidget` | `QDockWidget` | — | 39 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&canvas_tool_workflows` | `canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType, bool)` | `this` | `handle_canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType, bool)` |
| `&canvas_tool_workflows` | `canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` | `this` | `handle_canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` |
| `tool_action` | `triggered()` | `this` | `handle_tool_action_triggered()` |
| `shortcut_tool_action` | `triggered()` | `this` | `handle_tool_shortcut_triggered()` |
| `shortcut_workflow_action` | `triggered()` | `this` | `handle_workflow_shortcut_triggered()` |
| `tab_widget_canvas_tools` | `currentChanged(int)` | `this` | `handle_workflow_tab_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CanvasToolBarDockWidget.h
python scripts/gpq.py def GPlatesQtWidgets::CanvasToolBarDockWidget --body
python scripts/gpq.py uses CanvasToolBarDockWidget --kind class
python scripts/gpq.py hier CanvasToolBarDockWidget
```
