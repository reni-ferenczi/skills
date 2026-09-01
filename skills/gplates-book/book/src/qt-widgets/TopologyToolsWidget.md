# TopologyToolsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 217 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TopologyToolsWidget.h` | C++ | 247 |
| `src/qt-widgets/TopologyToolsWidget.cc` | C++ | 713 |
| `src/qt-widgets/TopologyToolsWidgetUi.ui` | Qt form | 366 |

## Overview

`TopologyToolsWidget` is the task-panel form shown while a topology-building or
topology-editing canvas tool is active. It presents the section list, the
"Add"/"Add To Boundary"/"Add To Interior"/"Remove" buttons and the
"Create"/"Apply" buttons that a user works through while assembling a
`TopologyBoundary`, `TopologyLine` or `TopologyNetwork` feature, and it adapts
its labels and which widgets are visible to the `GPlatesAppLogic::TopologyGeometry::Type`
being built (networks show an interior-sections row that boundaries and lines
hide).

The widget itself holds almost no topology logic: `activate()` switches
between `BUILD` mode (constructing a brand-new topological feature, so the
"Create" button is shown) and `EDIT` mode (reusing the feature currently held
by `GPlatesGui::FeatureFocus`, so "Apply" is shown instead and the feature's
`gml:validTime` is read to reactivate the tool over the correct time period),
then delegates the actual section bookkeeping and geometry construction to
`GPlatesGui::TopologyTools` via `d_topology_tools_ptr`. Every button handler in
this class is a thin forward to the matching method on that object;
`CreateFeatureDialog` and `FeatureSummaryWidget` are launched from here to let
the user name the new feature and review the resulting topology, respectively.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TopologyToolsWidget`](#gplatesqtwidgetstopologytoolswidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_TopologyToolsWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::TopologyToolsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanvasToolMode` | enum | `None` | public | What mode the tools were started in ; NOTE this can change during tool use \*/ |
| `TopologyToolsWidget( GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window, QAction *clear_action, GPlatesGui::CanvasToolWorkflows &canvas_tool_workflows, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~TopologyToolsWidget()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `get_clear_action_text()` | method | `QString` | public | — |
| `clear_action_enabled()` | method | `bool` | public | — |
| `handle_clear_action_triggered()` | method | `void` | public | — |
| `activate( CanvasToolMode mode, GPlatesAppLogic::TopologyGeometry::Type topology_geometry_type)` | method | `void` | public | — |
| `deactivate()` | method | `void` | public | — |
| `clear_task_panel()` | method | `void` | public | — |
| `display_number_of_sections_boundary( int i )` | method | `void` | public | — |
| `display_number_of_sections_interior( int i )` | method | `void` | public | — |
| `get_sections_combobox_index()` | method | `int` | public | — |
| `set_sections_combobox_index( int index )` | method | `void` | public | — |
| `handle_sections_combobox_index_changed( int index )` | method | `void` | public | — |
| `handle_clear()` | method | `void` | public | — |
| `handle_clear_action_changed()` | method | `void` | public | — |
| `handle_create()` | method | `void` | public | — |
| `handle_apply()` | method | `void` | public | — |
| `handle_add_to_boundary()` | method | `void` | public | — |
| `handle_add_to_boundary_shortcut_triggered()` | method | `void` | public | — |
| `handle_add_to_interior()` | method | `void` | public | — |
| `handle_remove()` | method | `void` | public | — |
| `handle_remove_shortcut_triggered()` | method | `void` | public | — |
| `choose_topology_tab()` | method | `void` | public | — |
| `choose_section_tab()` | method | `void` | public | — |
| `setup_widgets()` | method | `void` | private | — |
| `setup_connections()` | method | `void` | private | — |
| `display_topology( GPlatesModel::FeatureHandle::weak_ref feature_ref)` | method | `void` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_feature_focus_ptr` | field | `GPlatesGui::FeatureFocus` | private | This is our reference to the Feature Focus, which we use to let the rest of the application know what the user just clicked on. |
| `d_model_interface` | field | `GPlatesModel::ModelInterface` | private | The model |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | To change the canvas tool when we are finished editing/building topology. |
| `d_create_feature_dialog` | field | `CreateFeatureDialog` | private | The dialog the user sees when they hit the "Create" button to build a \*new\* topological feature. |
| `d_topology_tools_ptr` | field | `GPlatesGui::TopologyTools` | private | The tools to create and edit the topology feature \*/ |
| `d_feature_summary_widget_ptr` | field | `FeatureSummaryWidget` | private | the FeatureSummaryWidget pointer \*/ |
| `d_edit_topology_feature_ref` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | The topology feature being edited (if using edit tool) or boost::none (if using the build tool). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `format_time_instant( const GPlatesPropertyValues::GmlTimeInstant &time_instant)` | function | `QString` | Borrowed from FeatureTableModel.cc. |
| `fill_plate_id_field( QLineEdit *field, GPlatesModel::FeatureHandle::weak_ref feature_ref, const GPlatesModel::PropertyName &property_name)` | function | `void` | We now have four of these plate ID fields. |
| `get_topological_geometry_property_name_from_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | function | `boost::optional<GPlatesModel::PropertyName>` | Retrieves the topological geometry property name from the specified feature. |
| `GPLATES_QTWIDGETS_TOPOLOGYTOOLSWIDGET_H` | macro | `None` | — |

## Notes

`d_edit_topology_feature_ref` is `boost::none` in `BUILD` mode and set to the
focused feature in `EDIT` mode; code that reads it must check the mode first.
Entering `EDIT` mode with no valid focused feature disables the whole widget
and returns before the topology tool is activated, so callers cannot assume
`activate()` always leaves the widget usable. `d_create_feature_dialog` is
parented to a Qt widget and is memory-managed by Qt, not explicitly deleted.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 12 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 2 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 2 |
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `TopologyToolsWidget` | `QWidget` | TopologyToolsWidget | 28 |

**Qt signal/slot connections** (10 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `add_to_boundary_shortcut_action` | `triggered()` | `this` | `handle_add_to_boundary_shortcut_triggered()` |
| `remove_shortcut_action` | `triggered()` | `this` | `handle_remove_shortcut_triggered()` |
| `sections_table_combobox` | `currentIndexChanged(int)` | `this` | `handle_sections_combobox_index_changed(int)` |
| `button_create` | `clicked()` | `this` | `handle_create()` |
| `button_apply` | `clicked()` | `this` | `handle_apply()` |
| `button_add_section` | `clicked()` | `this` | `handle_add_to_boundary()` |
| `button_add_interior` | `clicked()` | `this` | `handle_add_to_interior()` |
| `button_remove_section` | `clicked()` | `this` | `handle_remove()` |
| `&d_view_state.get_topology_boundary_sections_container()` | `container_changed(GPlatesGui::TopologySectionsContainer &)` | `this` | `handle_clear_action_changed()` |
| `&d_view_state.get_topology_interior_sections_container()` | `container_changed(GPlatesGui::TopologySectionsContainer &)` | `this` | `handle_clear_action_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TopologyToolsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::TopologyToolsWidget --body
python scripts/gpq.py uses TopologyToolsWidget --kind class
python scripts/gpq.py hier TopologyToolsWidget
```
